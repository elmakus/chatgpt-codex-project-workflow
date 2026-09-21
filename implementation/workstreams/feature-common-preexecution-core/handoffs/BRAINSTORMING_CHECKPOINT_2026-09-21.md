# Brainstorming handoff — common pre-execution core

Date: 2026-09-21
Workstream: `feature-common-preexecution-core`
Branch: `feat/common-preexecution-core`
Canonical exploratory record: `brainstorming/COMMON_PREEXECUTION_CORE.md`
Phase: Brainstorming
Scope: `common-preexecution-core@R1`
Definition promotion authorization: `pending`
Definition promotion subject: `none`

## Purpose

This is a context-compaction handoff for a fresh chat. It does not promote the scope to Definition and does not replace the canonical Brainstorming record.

Use this file as the durable start pointer, then read only the referenced parts of the canonical Brainstorming record needed for the next obligation.

## Authority / entry rule

For the next context:

1. use current Project Workflow only for safe repository/bootstrap mechanics;
2. resolve this exact workstream/branch;
3. refresh the authoritative remote branch before selecting the next obligation;
4. treat `brainstorming/COMMON_PREEXECUTION_CORE.md` as canonical exploratory authority;
5. do not infer state from prior chat narrative;
6. do not enter Definition unless the user explicitly authorizes promotion.

For isolated future live tests, the exact live-test durable record is the semantic authority for that experiment and overrides conflicting old `chatgpt_only/*` / `codex_only/*` semantics only within the test boundary.

## Current design direction

The goal has evolved from simple deduplication into **runtime portability of one durable Project Workflow workstream across supported runtimes at safe boundaries**.

Project Workflow should own:
- durable semantic obligations;
- authority and accepted scope;
- lifecycle/correctness invariants;
- project-level safety;
- exact result/review/recovery state.

Runtime should own:
- product/model/worker/session identity;
- worker catalog and role names;
- delegation mechanics;
- scheduling/parallel realization;
- runtime lifecycle and workspaces.

Project Workflow common contracts should not require names such as `ChatGPT`, `Codex Main`, `Executor`, `Tester` or `Investigator` merely to realize the same semantic obligation.

Capability-first rule:
- when an obligation requires independent context and runtime has a qualifying independent/delegated capability, use it;
- otherwise persist the same obligation and hand off to a fresh context;
- a failed invocation of an available capability is runtime failure, not proof that the capability is absent.

## Stage conclusions currently supported

### Stages 1–6

Working direction:
- Intake: mostly common; old Codex orchestration binding is likely removable runtime leakage under the one-fixed-runtime target.
- Brainstorming: common.
- Research: common semantic lifecycle; concrete Investigator realization is runtime-owned.
- Brainstorming -> Definition promotion gate: common and user-owned.
- Definition: common.
- Strategic Planning: common; review transport/context mechanics do not belong in Planning.

### Independent Plan Review

Common semantic contract supported by live tests:
- exact immutable subject;
- independent context requirement;
- durable review lifecycle;
- no product/worker name required;
- fresh-context fallback uses durable realization state:
  `resolve_independent_context -> awaiting_independent_context -> independent_context_active -> satisfied`.

The anti-bounce behavior was validated by live test D.

### Execution Prep

Stage-8 invariant:

`READY = Card is legally executable now from project authority, dependencies, prerequisites and authorization gates.`

All currently executable Cards may be READY regardless of current runtime concurrency capability.

Runtime later chooses one or a compatible subset.

Cross-runtime READY parity passed live test E.

### Execution / State

Working common primitive:

```yaml
active_execution:
  id: X01
  state: prepared | active | transfer_ready
  base_ref: <exact durable base>
  reconciliation_order: [T01, T02]
  members:
    - card_id: T01
      state: prepared | active | quiesced | result_ready | reconciled | blocked
      checkpoint_ref: null
      result_ref: null
      canonical_result_ref: null
      evidence: null
```

`active_execution: null` means no current implementation realization set remains.

One member = serial execution.
Multiple members = bounded concurrent execution.

Important semantics:
- Card `in_progress` means started/non-terminal, not "worker is alive";
- `result_ready` means exact durable non-canonical result exists;
- `reconciled` means accepted canonical result exists;
- `transfer_ready` is an explicit quiescent transfer boundary;
- uncertain old liveness fails closed;
- returned/reconciled work is never replayed just because runtime state disappeared;
- a new runtime may continue remaining members serially after safe transfer;
- concrete worker/session/model/worktree identity is not project state.

Live execution matrix:
- F: completed-Card cross-runtime takeover — PASS.
- G: active single-Card takeover at proven quiescent checkpoint — PASS.
- H: multi-member execution-set takeover — PASS for takeover/reconciliation semantics; actual wall-clock concurrency is only attested by coordinator evidence.
- I: unsafe active takeover without quiescence/result proof — PASS fail-closed.

### Post-implementation review

Target common model is append-only review attempts:

```yaml
review:
  requirement: REQUIRED | RECOMMENDED | none
  current_attempt: R02
  attempts:
    - id: R01
      mode: independent_review
      state: red
      subject: <immutable S1>
      evidence: <durable evidence>
      independence:
        requirement: independent_context
        realization_state: satisfied
        evidence: <runtime-neutral semantic proof>
    - id: R02
      mode: independent_review
      state: pending
      subject: <immutable S2>
      evidence: null
      independence:
        requirement: independent_context
        realization_state: resolve_independent_context
        evidence: null
```

Key rules:
- one attempt = one immutable subject;
- prior attempts are append-only;
- corrected subject appends a new attempt;
- reviewer/context replacement for unchanged subject stays in the same attempt;
- producer/correction context may not review the exact subject it materially produced or repaired;
- this disqualification applies even if its competing local commit lost a push/CAS race;
- GREEN Card review is consumed later by deterministic finalization;
- workstream final-integration review should likely use the same append-only history model, including exact coverage reuse as a distinct terminal gate outcome.

Live review matrix:
- J: independent GREEN in one runtime/context + later Card finalization in another without replay — PASS.
- K: R01 RED(S1) -> bounded correction S2 -> append R02 -> independent R02 GREEN — lifecycle PASS.
- K also showed old-wrapper contamination: Codex persisted `tester` / session / invocation telemetry in evidence. This is not clean evidence against the candidate common contract because current fixed-policy workflow still wrapped the experiment.

Desired common rule remains:
- concrete worker/role/model/session/invocation/worktree identity MUST NOT be canonical Project Workflow state/evidence merely to prove independence;
- canonical evidence should state only semantic independence facts.

## Authoritative-state refresh gate

The K race exposed:

`fresh context != fresh durable repository state`.

Common recovery/entry target:

```text
new context / takeover / recovery
-> resolve exact workstream + authoritative branch/ref
-> refresh authoritative durable source
-> establish exact current authoritative head
-> reconcile/validate local checkout against that head
-> read canonical durable workflow state
-> only then choose the legal obligation
```

Publication still uses expected-base/CAS behavior.

If push/update loses a race:
- refresh;
- reroute from the new durable state;
- never blindly retry the stale phase.

This is common correctness, not a Codex-only rule.

## Live-test harness caveat

Previous tests were started with current Project Workflow, whose current `main` still routes through old fixed-policy modules.

Therefore:
- semantic state-transition evidence from F–K remains useful;
- incidental old-policy vocabulary/telemetry must not be mistaken for the candidate common contract;
- future live tests need a stronger experimental authority boundary.

Use this isolation wording conceptually:

```text
Use current Project Workflow for safe repository/bootstrap mechanics.
This is an isolated live test of the proposed common contract.
For the tested obligation, the exact durable live-test record is the semantic authority
and overrides conflicting chatgpt_only/codex_only semantics only inside this experiment.
Do not import product/worker names, state shape or realization behavior unless the record requires them.
```

## Remaining material work

The live-test harness hardening is now complete and durable at:
`c427bafb31c3f6c79544be3a89300b02503aa7f9:brainstorming/live-tests/ISOLATED_COMMON_CONTRACT_HARNESS.md`.

Live test L is armed with:
- stale local snapshot: `2e52d793c597da27dc1000b126cf60cb90a8a491`;
- current record: `brainstorming/live-tests/CAPABILITY_REFRESH_L.md`;
- current state: `fresh_phase_pending`;
- current legal obligation: `L-FRESH`.

Do these before considering Brainstorming complete:

1. **Run live test L — authoritative-state refresh**
   - start a fresh context with a clean local checkout pinned exactly to the stale snapshot above;
   - require refresh of the authoritative branch before routing;
   - success: it sees `L-FRESH`, does not execute/publish `L-STALE`, and does not need push/CAS rejection to discover freshness.
2. **Live test M — clean review evidence**
   - independent review under the isolated harness;
   - success: canonical durable evidence contains semantic independence only, with no product/worker/session/invocation identity.
3. **Cross-cutting audit**
   - current `ROUTER`;
   - `RECOVERY`;
   - `WORKSTREAMS`;
   - `CLOSE`;
   - relevant templates/tests.
   Reconcile them with capability-first routing, authoritative-state refresh, `active_execution`, append-only review attempts, final-integration review and cross-runtime continuation.
4. **Choose composition architecture**
   - direct routing to `workflow/common/*` where there is zero policy delta;
   - versus tiny policy-local forwarders/adapters;
   - keep policy-local text only for genuine runtime/policy differences.
5. Reconcile the canonical Brainstorming record into one target architecture and decide whether any material design question remains.
6. Only if Brainstorming is truly ready, stop at the user-owned Brainstorming -> Definition promotion gate. Do not self-promote.

## Material questions still open

- Exact composition model: direct common routes versus thin policy-local forwarders/adapters.
- Exact treatment of workstream final-integration review attempt history/coverage reuse in the final common schema.
- Whether any stronger stale-coordinator fencing primitive is needed beyond authoritative refresh + explicit quiescence/transfer + expected-base/CAS. Do not add one speculatively; revisit during Recovery audit if an actual gap remains.
- Final migration/test plan for replacing duplicated fixed-policy modules safely.

No external research is currently needed.

## Things already closed enough not to reopen without new evidence

- The goal is runtime portability, not merely textual dedupe.
- Worker-role/product identity does not belong in common semantic obligations.
- Brainstorming/Research/Definition/Planning semantics are not intentionally different because one runtime delegates and another uses a fresh context.
- READY semantics are independent of runtime concurrency capability.
- Active execution requires more durable state than Card `in_progress` alone.
- Unsafe uncertain-live takeover fails closed.
- Review attempts should be append-only.
- Producer/correction context cannot independently review its exact subject.
- Fresh chat/context alone is not a repository freshness guarantee.

## Next-chat recommended entry

Start from this handoff, refresh the branch, then recover `brainstorming/live-tests/CAPABILITY_REFRESH_L.md`.

For the actual L probe, the execution context must begin with a clean local checkout pinned exactly to `2e52d793c597da27dc1000b126cf60cb90a8a491` while the authoritative remote branch remains newer. Use the isolated harness and let the refreshed durable record select the legal obligation.

Do not run Definition or modify production workflow modules yet.
