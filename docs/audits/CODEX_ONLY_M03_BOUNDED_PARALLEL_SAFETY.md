# Codex-only M03 — bounded parallel safety scenario audit

Scope: M03 Card safety metadata, current-state JIT eligibility, isolated lane execution, returned-result validation, deterministic Main integration and repository-first recovery.

Authority:

- `requirements/CODEX_ONLY_POLICY.md` — CO-REQ-017..025
- `decisions/ADR_CODEX_ONLY_BOUNDED_PARALLEL_CARDS.md`
- `decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md`
- `planning/CODEX_ONLY_MASTER_PLAN.md#M03--bounded-parallel-task-cards-and-jit-safety`
- `openspec/changes/codex-only-m03-bounded-parallel-safety/specs/bounded-parallel-safety.md`

## Positive compatible-batch trace

Given canonical READY order `T1, T2, T3`:

```yaml
T1:
  parallel_safe: true
  write_scope: ["src/a/"]
  exclusive_resources: []
T2:
  parallel_safe: true
  write_scope: ["src/b/"]
  exclusive_resources: ["db:test-b"]
T3:
  parallel_safe: true
  write_scope: ["docs/"]
  exclusive_resources: []
```

All dependencies are complete, scopes are pairwise disjoint, resources do not conflict, isolated mutable workspaces are available and current Git base is exact `S0`.

Execution Prep deterministically freezes:

```yaml
parallel:
  current_batch: B01
  batches:
    - id: B01
      state: prepared
      integration_base: S0
      evidence: null
      members:
        - {card_id: T1, lane: L01, state: prepared, result_commit: null, integrated_commit: null, evidence: null}
        - {card_id: T2, lane: L02, state: prepared, result_commit: null, integrated_commit: null, evidence: null}
        - {card_id: T3, lane: L03, state: prepared, result_commit: null, integrated_commit: null, evidence: null}
```

Membership/order/base are frozen. Runtime may realize three workers concurrently, but Project Workflow knows only B01/L01..L03.

When results R1/R2/R3 return, Codex Main alone:

1. persists each returned result/evidence;
2. verifies `S0..R#` stays inside that Card scope and does not touch reserved shared state;
3. sets B01 to `integrating` before the first shared application and integrates in L01, L02, L03 order;
4. records each exact immutable historical `integrated_commit` and Card result;
5. freezes ordinary M02 review on each exact integrated result when review applies, but keeps those attempts pending/deferred while B01 remains current;
6. marks B01 complete/current null after every member is integrated;
7. only then dispatches frozen member reviews in canonical Task Board order.

Returned/integrated refs remain durable in B01 history. A later post-batch RED repair may advance a Card's current result/new review attempt but never rewrites the B01 member's original refs.

## Negative eligibility matrix

| Condition | Parallel result | Card result |
| --- | --- | --- |
| `parallel_safe` absent/false | exclude from batch | execute serially when READY |
| dependency incomplete | exclude | wait for dependency |
| empty/invalid/absolute/`..`/glob write scope | exclude | serial fallback |
| scopes equal or ancestor/descendant | incompatible | deterministic serial fallback |
| same `exclusive_resources` token | incompatible | deterministic serial fallback |
| isolated workspace unavailable | do not launch batch | serial fallback |
| exact integration base not recoverable | do not launch batch | serial/recovery from current truth |
| only one compatible candidate remains | no batch | execute serially |

A failed concurrency proof is not itself a user stop or policy switch.

## Reserved shared-state violation

If lane result R2 changes the selected live Task Board, workstream manifest or shared integration bookkeeping, Main rejects integration even if a broad path claim would otherwise contain that path.

The returned result/evidence remains durable for diagnosis. The member/batch becomes blocked and Router/Recovery classifies correction. Scope is never silently widened.

## Scope escape

If T2 owns `src/b/` but `S0..R2` also changes `src/a/file`, R2 is not integrated.

T1 or any already-successful sibling is not rerun. Correction/re-execution applies only to the affected obligation.

## Integration conflict

If a returned result was valid against S0 but a material semantic/textual conflict appears while applying it after earlier frozen members:

- preserve the returned result;
- preserve already-integrated members;
- keep frozen order;
- mark exact blocker;
- route Recovery/current authority;
- do not reorder members or restart the batch to hide the conflict.

## Crash/recovery matrix

| Durable boundary | Recovery |
| --- | --- |
| B01 prepared, no lane launched | revalidate base/safety; expected Main-only freeze bookkeeping after S0 is allowed. If proof is stale while every member is still prepared/result-free, persist blocked abandonment evidence, restore batch-owned Card statuses to READY, then clear current_batch; never reuse B01 |
| L02 in_progress, no result | runtime may resume/replace realization of same B01/L02 |
| L02 returned | do not rerun; validate/integrate once when prior frozen members resolved |
| L01 integrated, L01 review frozen pending, L02 returned | keep L01 review deferred; verify L01 shared result and continue L02 in frozen order; never restart B01 from S0 |
| integrated Git result exists, board pointer stale | verify exact Git/result relationship and reconcile Main bookkeeping only |
| all members integrated, batch still integrating | verify all refs, set complete, clear current_batch |
| complete batch, review freeze missing | freeze exact integrated Card subject once when review applies, then dispatch pending member reviews now that current_batch is null |
| runtime worker/session state lost | no Project Workflow identity change; use durable batch/member/result state |

### Pre-launch abandonment invariant

A frozen batch moves its Cards to `in_progress` before runtime launch. Therefore a stale prepared batch cannot be cleared by pointer-only cleanup.

Legal unwind requires all of the following:

1. every member is still `prepared`;
2. no member has `result_commit` or `integrated_commit`;
3. no member entered runtime-active state;
4. Main records the batch/member outcome as `blocked` with durable evidence;
5. each Card whose `in_progress` state came solely from B01 is restored to `ready` when normal serial prerequisites still hold;
6. only after that reconciliation may `current_batch` become null;
7. a later batch uses a new ID.

If any member left `prepared`, Recovery must reconstruct the actual running/returned/integrated state instead of applying this unwind.

## Review preservation

Parallelism does not create a second review model.

- Card implementation owner remains semantic `executor`.
- Review subject is the exact Main-integrated Card result.
- Main freezes that subject when the member is integrated, but the attempt remains pending/deferred until the current batch is complete/current-null.
- Tester remains non-repairing and independent under M02.
- RED correction therefore occurs only after batch closure and produces a new exact subject/attempt.
- The corrected Card result does not overwrite the completed member's original `result_commit` / `integrated_commit`; original review attempt + batch refs preserve lineage.
- Sibling returned/integrated batch results remain durable and are never replayed.

### Active-batch RED-repair trace

Given B01 with L01 and L02, Main integrates L01 to S1 and freezes its review attempt as pending while L02 is returned. Router MUST continue B01 rather than dispatch review. Main integrates L02, records its immutable integration ref, completes B01 and clears `current_batch`. Reviewable members may now coexist as `in_progress` only in the exact completed-batch review drain, which blocks unrelated new implementation. Only then may the S1 review run. If it is RED, Executor repairs the Card to S1c outside B01 and Main appends a new review attempt for S1c. B01 still records L01 `integrated_commit: S1`, the original S1 attempt remains durable, and no sibling result is replayed.

## Forbidden project state

Required schemas must not contain concrete runtime identity/lifecycle keys such as:

- `session_id`
- `invocation_id`
- worker/model/profile/reasoning IDs
- Muse lease/reservation IDs
- resume tokens
- concrete worktree paths

M03 also must not introduce a repository-global scheduler/queue or let worker lanes write the selected Task Board/integration state.

## Static verification contract

M03 verification must prove:

1. Task Card contract/template expose explicit opt-in safety fields while absent metadata remains serial-valid;
2. both codex_only Task Board templates expose optional batch state with exact base/member/result/integration refs;
3. Execution Prep implements deterministic Task-Board-order compatible-set selection and no dynamic refill;
4. Execution/Recovery preserve returned/integrated results and Main-only integration;
5. Workstreams/Repository require isolated mutable workspaces for intra-workstream concurrency without persisting runtime paths;
6. no forbidden runtime identity appears as a required project schema key;
7. no active repository-global scheduler/queue ownership is introduced;
8. modified M03 contracts contain no active dependency on another policy namespace or legacy/shared execution contracts;
9. root `workflow/CONTEXT_ROUTING.md` and `workflow/chatgpt_only/` remain identical to current workflow main;
10. root `PROJECT.md` remains `execution_policy: chatgpt_only`;
11. exact implementation diff has no conflict markers or added-line trailing whitespace;
12. stale prepared-batch fallback cannot leave batch-owned Cards `in_progress` after `current_batch` is cleared, and the abandoned batch ID remains durable history;
13. integrated-member reviews remain pending/deferred until active-batch closure, and later RED repair cannot overwrite historical member integration provenance or make sibling continuation ambiguous.

Parser-based YAML validation is reported only if an actual parser is available.
