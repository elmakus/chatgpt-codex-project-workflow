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
      members:
        - {card_id: T1, lane: L01, state: prepared, result_commit: null, integrated_commit: null, evidence: null}
        - {card_id: T2, lane: L02, state: prepared, result_commit: null, integrated_commit: null, evidence: null}
        - {card_id: T3, lane: L03, state: prepared, result_commit: null, integrated_commit: null, evidence: null}
```

Membership/order/base are frozen. Runtime may realize three workers concurrently, but Project Workflow knows only B01/L01..L03.

When results R1/R2/R3 return, Codex Main alone:

1. persists each returned result/evidence;
2. verifies `S0..R#` stays inside that Card scope and does not touch reserved shared state;
3. integrates in L01, L02, L03 order;
4. records each exact `integrated_commit` and Card result;
5. freezes ordinary M02 review only on each exact integrated result when review applies;
6. marks B01 complete/current null after every member is integrated.

Returned/integrated refs remain durable in B01 history.

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
| B01 prepared, no lane launched | revalidate base/safety; launch same batch if current, otherwise record stale prepared outcome and form new batch/serial fallback |
| L02 in_progress, no result | runtime may resume/replace realization of same B01/L02 |
| L02 returned | do not rerun; validate/integrate once when prior frozen members resolved |
| L01 integrated, L02 returned | verify L01 shared result, continue L02; never restart B01 from S0 |
| integrated Git result exists, board pointer stale | verify exact Git/result relationship and reconcile Main bookkeeping only |
| all members integrated, batch still integrating | verify all refs, set complete, clear current_batch |
| complete batch, review freeze missing | freeze exact integrated Card subject once when review applies |
| runtime worker/session state lost | no Project Workflow identity change; use durable batch/member/result state |

## Review preservation

Parallelism does not create a second review model.

- Card implementation owner remains semantic `executor`.
- Review subject is the exact Main-integrated Card result.
- Tester remains non-repairing and independent under M02.
- RED correction produces a new exact subject/attempt.
- Sibling returned/integrated batch results remain durable while RED/Review/Research outranks continued batch integration.

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
11. exact implementation diff has no conflict markers or added-line trailing whitespace.

Parser-based YAML validation is reported only if an actual parser is available.
