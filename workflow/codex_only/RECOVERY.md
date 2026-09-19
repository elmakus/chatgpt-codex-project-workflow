# Codex-only Recovery

> M02 contract. Recovery reconstructs project obligations from durable Project Workflow state, never from runtime session identity.

## Inputs

Recover only the project truth needed for the selected obligation:

- project `PROJECT.md`;
- exact workstream/branch + validated manifest when branch-isolated;
- selected canonical Task Board;
- exact Git/integration/result state;
- current Card/milestone/plan authority;
- current review block/attempt history and referenced evidence;
- implementation/recovery Research pointer + exact record when present;
- selected manifest final-integration review state when applicable;
- relevant runtime/external readback only as evidence, not durable project identity.

Previous chat narrative and runtime session handles are not authority.

## Priority

Inside the selected state context:

1. inconsistent project state -> reconcile/fail closed before unrelated work;
2. current review attempt `pending | in_progress` -> formal Review;
3. active/blocked/complete implementation-owned Research -> exact Research/return owner;
4. current attempt `red` -> RED correction classification;
5. in-progress implementation with current attempt `green` -> post-review finalization;
6. other existing in-progress/blocked implementation -> recover it;
7. manifest final-integration review obligation -> review/correction as applicable;
8. only then select new work.

Runtime liveness never outranks a durable project verdict.

## Review-attempt consistency

For each active Card/milestone review block require:

- resolved requirement coherent with the stable contract;
- `current_attempt` null only before activation, otherwise pointing to an existing attempt;
- unique stable attempt IDs;
- no more than one non-terminal attempt;
- immutable subject per existing attempt;
- terminal `green | red` attempt has durable evidence;
- result finalized under GREEN still equals the GREEN subject;
- semantic `implementation_owner_role` is present for every active reviewable Card/milestone subject; for a milestone it represents aggregate `executor` production ownership;
- semantic roles only; no required runtime worker/session identity.

A contradiction routes to Recovery rather than guessing.

## Pending/in-progress attempt recovery

If the current attempt is `pending | in_progress`:

- keep the same exact attempt/subject;
- do not create a new attempt merely because worker runtime state was lost;
- Main asks `codex_workflow` to safely resume or fail-closed replace the reviewer;
- the reviewer performs/reperforms the full review of the same subject;
- Main persists only ordinary attempt progress/verdict/evidence.

If exact complete verdict evidence is already durable while Task Board still says `in_progress`, Main may reconcile the matching verdict after verifying attempt ID + subject + evidence. If that proof is not exact, rerun the full review on the same subject instead of inventing a verdict.

## RED recovery

A durable RED verdict is already a completed review result.

1. Recover the exact RED attempt, subject, evidence and implementation-owner role.
2. Preserve that attempt unchanged.
3. Classify the correction through `REVIEW.md#RED -> owning-Executor repair`.
4. For Card-owned RED, bounded production repair returns through Main to that Card's owning `executor` role.
5. For milestone-owned RED, route through Execution Prep to reopen/create the exact affected corrective Card(s) with `implementation_owner_role: executor`; do not infer a concrete repair worker from runtime/transcript state.
6. If correction is not yet durable, resume/replace the runtime Executor realization as needed and produce it once.
7. If corrected Card result or milestone checkpoint S2 is already durably proven but interruption happened before its next pending attempt was frozen, append exactly one new attempt for S2 and point `current_attempt` to it. Do not redo the correction.
8. If the next attempt already exists, follow its state instead of repeating any prior role.

A runtime replacement that realizes the same project `executor` role does not alter accepted authority or create a review attempt by itself.

## GREEN recovery

A durable GREEN verdict is not replayed because a Tester/session disappeared.

If the implementation/result still equals the GREEN subject, route to Execution for terminal post-review finalization. If production changed after GREEN, do not reuse the verdict; freeze the changed exact subject as a new attempt when review still applies.

## Partial Main writes

Project Workflow fails closed around partial shared-state transitions.

Examples:

- implementation result exists, but Task Board result pointer is stale -> reconcile proven result before review;
- corrected result exists after RED, but new attempt is missing -> append one attempt for the proven corrected subject;
- review evidence exists, but terminal state write is missing -> reconcile only when evidence exactly matches current attempt/subject;
- terminal state claims verdict but evidence is missing/mismatched -> inconsistent; do not proceed;
- multiple non-terminal attempts -> inconsistent; preserve evidence and reconcile before continuing.

Never repair inconsistency by consulting a runtime session ID.

## Implementation-owned Research

Task Board `research_obligation` remains the sole implementation/recovery Research pointer. The pointed record owns lifecycle/Origin/Return target/reconciliation.

Research completion does not erase RED review history. After return, the owning role performs only the authorized correction/classification and then continuation follows the current review attempt/result state.

## Runtime boundary

Project Workflow does not own:

- worker/session IDs;
- invocation IDs;
- model/profile/reasoning selection;
- Muse leases;
- wait/poll mechanics;
- worker resume protocol;
- worker replacement mechanics.

Runtime may resume or replace Executor/Tester realization fail-closed. Durable project role, subject, attempt and verdict semantics remain unchanged.

## M03 boundary

Lane-result/integration recovery and bounded-parallel active-set semantics are M03-owned. M02 remains serial-safe and must not infer parallel lanes from runtime worker concurrency.
