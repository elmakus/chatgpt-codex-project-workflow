# Codex-only Recovery

> M03 contract. Recovery reconstructs project obligations from durable Project Workflow state, never from runtime session identity.

## Inputs

Recover only truth needed for the selected obligation:

- project `PROJECT.md`;
- exact workstream/branch + validated manifest when branch-isolated;
- selected canonical Task Board;
- exact Git/integration/result state;
- current Card/milestone/plan authority;
- current review history/evidence;
- current parallel batch/history and referenced result evidence;
- implementation/recovery Research pointer + exact record when present;
- selected manifest final-integration review state when applicable;
- relevant runtime/external readback as evidence only.

Previous chat narrative, worker/session handles and concrete worktree paths are not authority.

## Priority

Inside the selected context:

1. inconsistent project state -> reconcile/fail closed;
2. non-deferred current review attempt `pending | in_progress` -> Review;
3. active/blocked/complete implementation-owned Research -> exact Research/return owner;
4. non-deferred current review `red` -> RED correction classification;
5. in-progress implementation with non-deferred current review GREEN -> post-review finalization;
6. current parallel batch/member returned or non-terminal -> batch recovery/integration, even when integrated members have frozen `pending` reviews deferred by that exact batch;
7. other in-progress/blocked implementation -> recover it;
8. manifest final-integration review obligation -> review/correction;
9. only then select new work.

Runtime liveness never outranks a durable project verdict or returned lane result.

## Review consistency

Preserve all M02 invariants:

- resolved review requirement matches stable contract;
- current attempt points to an existing immutable-subject attempt;
- no more than one non-terminal attempt per review owner;
- terminal verdict has durable evidence;
- finalized result equals GREEN subject;
- semantic implementation owner is present;
- runtime identity is not required state.

Reviewer loss does not create a new attempt. Complete matching verdict evidence may be reconciled exactly; otherwise re-run full review of the same subject. A reviewable integrated member of the unresolved `current_batch` may have a frozen `pending` attempt, but it MUST NOT have entered `in_progress | red | green`; that state is inconsistent and must be recovered before production correction.

## Parallel batch consistency

For `parallel.current_batch` and every batch history entry require:

- stable unique batch ID;
- current pointer identifies at most one non-complete batch;
- exact immutable `integration_base` once launched;
- immutable finite member list/order after launch;
- durable batch-level evidence for any `blocked`/abandoned outcome;
- unique semantic lane label per member inside the batch;
- each member Card exists and was eligible under its frozen Card contract/current proof;
- all frozen member write scopes are pairwise disjoint and resource tokens non-conflicting;
- returned/integrated states have exact required result/evidence refs;
- integrated member has immutable exact `integrated_commit` coherent with its original Main-integrated Card result and original batch-subject review lineage; a later post-batch RED repair may advance the Card's current result without rewriting this historical member ref;
- multiple `in_progress` Cards occur only when covered by this exact current batch or by one exact completed-batch post-batch review drain in which every remaining `in_progress` Card is an integrated member with an outstanding review/finalization/RED-correction obligation;
- no concrete worker/session/model/profile/invocation/lease/resume/worktree-path key is project authority;
- no worker mutated shared Task Board/manifest/integration state.

Contradiction routes to Recovery; never infer the missing fact from runtime memory.

## Batch recovery by durable boundary

### Prepared

A `prepared` batch has no guaranteed runtime work yet.

1. re-read current branch HEAD and exact frozen base, allowing only the expected Main-owned batch-control bookkeeping committed after that base;
2. revalidate dependencies, Card safety metadata, scope/resource compatibility and workspace-isolation availability;
3. if still current, launch the same frozen batch;
4. if proof/base is stale before launch, use the pre-launch abandonment transition only when every member is still `prepared`, every `result_commit`/`integrated_commit` is null and no member entered runtime-active state;
5. persist one abandonment evidence record, set the batch plus its member history entries to `blocked`, and reconcile each member Card whose `in_progress` status came solely from this freeze back to `ready` when its ordinary serial prerequisites still hold;
6. persist those Card reconciliations before or atomically with clearing `current_batch`; after the transition no Card may remain `in_progress` solely because the abandoned batch once owned it;
7. never reuse that batch ID; form a new batch or execute serially from current truth.

If any member left `prepared`, has a durable result, or runtime-active work may exist, this unwind is illegal. Recover the actual running/returned/integrated state instead.

No worker result is assumed for a legally abandoned prepared batch.

### In progress

For a member `in_progress` with no durable `result_commit`:

- runtime may resume or fail-closed replace the concrete realization for the same batch/member;
- Project Workflow lane/card identity does not change;
- if runtime evidence cannot prove safe continuation, re-run that member from the same frozen base rather than inventing a result;
- do not restart members that already have returned/integrated results.

### Returned

A `returned` member is durable completed lane work.

- never rerun it because runtime disappeared;
- verify result/evidence against frozen base, write scope and reserved-state rule;
- integrate it exactly once in frozen member order when preceding members are resolved;
- a prior integrated member's review that is merely frozen `pending` by this same current batch is deferred and does not block the next frozen member; preserve all review/result refs while continuing the batch.

### Partially integrated

If earlier members are `integrated` and later members are `returned | in_progress`:

- verify current shared branch contains the recorded integrated commits/authorized Main bookkeeping;
- preserve every completed member/result;
- resume the first unresolved member in frozen order;
- never restart the batch from the original base merely to reconstruct already-integrated work.

### Blocked

For member/batch `blocked`:

- recover exact blocker/result/evidence;
- a reconciled historical pre-launch abandonment may remain `blocked` with `current_batch: null`; its member Cards must already have been returned to legal READY/serial state and the batch ID is never reused;
- scope escape or reserved-state mutation is not integrated;
- material integration conflict preserves returned result;
- classify smallest correction, serial fallback, Planning/Definition/Research or real input/runtime gate through Router;
- do not silently widen write scope, reorder members or discard completed evidence.

### Complete

A complete batch is history. `current_batch` must be null. Its immutable member `result_commit` / `integrated_commit` refs remain original batch provenance. Frozen pending member reviews now lose their deferral and form the bounded post-batch review drain: review/finalization/correction for those integrated Cards outranks any unrelated new implementation until every drain Card leaves `in_progress`. Never reopen a complete batch to add members.

## Partial Main writes

Fail closed around partial transitions.

Examples:

- worker result exists externally but member state lacks exact proof -> verify the result against batch/card/base before reconciling; otherwise re-realize only that member;
- `result_commit` is durable but member still `in_progress` -> verify exact matching evidence, then reconcile to `returned`; do not execute again;
- integrated Git commit is durable but member/Card pointers are stale -> prove exact commit/result relationship and reconcile bookkeeping, not implementation;
- member says integrated but `integrated_commit` is absent or cannot be proven as that member's original batch integration result -> inconsistent; recover Git/review lineage before continuation; do not overwrite history with a later repair result;
- stale prepared batch was cleared but one of its Cards is still `in_progress` solely from the abandoned freeze -> restore the exact pre-launch abandonment reconciliation before any new work;
- all members integrated but batch still `integrating` -> verify each integrated ref, mark complete and clear `current_batch`;
- batch complete but Card review freeze is missing -> freeze the exact integrated Card subject once when review still applies.

## RED recovery

Durable RED is a completed review result and normally outranks unrelated implementation. Under M03, a batch-member review was not allowed to reach RED while its originating batch remained current; if that impossible durable combination is recovered, finish/reconcile the exact batch boundary before any production correction rather than rewriting batch history.

After the originating batch is complete/current-null, Card RED returns through Main to the owning `executor` role. Milestone RED routes through Execution Prep to exact corrective Card(s). Preserve sibling returned/integrated batch results and do not replay them. A post-batch repair advances the Card's current result/new review attempt while the completed batch member's original `result_commit` / `integrated_commit` and prior review attempt remain immutable.

Corrective work is serial unless a new current-state JIT proof independently forms a legal later batch.

## GREEN recovery

A durable GREEN verdict is never replayed because a Tester/session disappeared. If Card result still equals the GREEN subject, finalize it. If implementation changed, freeze a new subject/attempt when review still applies.

## Implementation-owned Research

Task Board `research_obligation` remains the single implementation/recovery Research pointer. Research completion never erases review or batch history.

## Runtime boundary

Project Workflow does not own concrete worker/session/model/profile/reasoning/invocation/lease/wait/resume/replacement/worktree-path state. Runtime may resume or replace a realization fail-closed; durable Card/batch/lane/result/review semantics remain unchanged.

## M04 boundary

M03 recovery covers bounded intra-workstream Card batches. M04 reconciles full lifecycle, stacked-workstream/target-refresh/final-integration recovery and root cutover.

[executed on device: Tower (b030638f-5714-4775-aa64-5babf6677db4)]