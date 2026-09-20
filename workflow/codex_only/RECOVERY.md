# Codex-only Recovery

> Live Codex-only recovery contract. Recovery reconstructs project obligations from durable Project Workflow state, never from runtime session identity.

Coordinator/session interruption, replacement, transcript loss or context loss is recovered here from durable project state; it is not a Project Workflow Context Health/FRESH/hygiene stop. Once durable state is coherent, deterministic continuation resumes without asking the user solely for a fresh coordinator context.

## Inputs

Recover only truth needed for the selected obligation:

- project `PROJECT.md`;
- exact workstream/branch + validated manifest for active managed work;
- selected manifest-bound Task Board/history source for active managed work; when no workstream is selected and historical root/default `implementation/TASK_BOARD.yaml` exists, read it only as migration input under **Historical root/default migration before mutation** below;
- `workflow/codex_only/INTAKE.md` only when historical migration must recover/create exact workstream identity, target/base or dependency topology;
- exact Git/integration/result state;
- current Card/milestone/plan authority;
- current review history/evidence;
- current parallel batch/history and referenced result evidence;
- implementation/recovery Research pointer + exact record when present;
- selected manifest final-integration review state when applicable;
- relevant runtime/external readback as evidence only.

Previous chat narrative, worker/session handles and concrete worktree paths are not authority.

## Orchestration reconstruction boundary

For a selected branch-first workstream, Recovery also reconstructs the compact orchestration boundary from the selected manifest plus `ORCHESTRATION_KERNEL.md`; it never reconstructs concrete runtime identity.

At known coordinator/transcript/context loss, repository-only recovery, coordinator replacement, or uncertainty about current-context re-bind:

1. treat the conceptual current-context binding latch as absent/uncertain even when the durable fingerprint still matches;
2. validate the selected manifest's `orchestration` shape and durable binding;
3. if the selected pre-schema branch-first manifest has **no `orchestration` block**, perform one bounded schema upgrade: ask the active runtime owner to resolve the currently selected opaque policy/profile, persist exactly `runtime_owner + policy_ref + optional contract_fingerprint`, read it back, then continue;
4. if the block already exists but required `runtime_owner` / `policy_ref` values are missing, unknown or contradictory, fail closed; do not reinterpret it as legacy absence and do not select another policy/harness;
5. before the first subsequent policy-dependent worker realization/re-realization, satisfy `workflow/codex/CODEX_ORCHESTRATION.md#Codex-only pre-dispatch binding gate`.

Fingerprint drift requires re-resolution and durable refresh only after successful resolution. A matching fingerprint suppresses only drift work; it never supplies the non-durable current-context latch.

This recovery read is bounded to `PROJECT.md`, the selected manifest, the kernel and the exact canonical state already needed by the current obligation. Do not reread the entire workflow/project tree or remote `codex_workflow` repository merely to restore orchestration policy.

## Priority

Apply this priority only after one exact branch-isolated workstream Task Board is selected and binding validation is GREEN. Historical root/default state must complete the migration-before-mutation protocol below before normal priority applies.

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

## Historical root/default migration before mutation

When no branch-isolated workstream is selected and historical root/default state contains a live managed-change obligation, migration itself outranks review, Research, Execution Prep, batch recovery and Execution. Do not resume, normalize or advance the root/default board in place.

1. Read root `implementation/TASK_BOARD.yaml` plus only the exact current contracts, review attempts, Research pointer/record, Card/milestone result/evidence, parallel batch/history, handoff and Git/PR state needed to identify the live obligation. This discovery is read-only with respect to root/default execution state.
2. Recover one exact migration topology **before branch creation or adoption**. First recover any existing branch/manifest/PR that durably represents this same obligation. Otherwise recover the repository's intended normal `integration_target` and exact creation base from durable project/Git/PR evidence, then apply `INTAKE.md#Base and dependency classification`: use an independent workstream with null parent fields when no parent-only dependency exists; use a stacked workstream only when exact evidence proves the required parent workstream/branch and concrete `parent_dependency`. The selected base is the exact integration-target base for independent work or the exact required parent-only base for stacked work. If `integration_target`, exact base, parent ownership or dependency classification cannot be proven, fail closed before creating/adopting a branch.
3. Establish one exact migration identity. Reuse an exact coherently recovered workstream identity when one exists. Otherwise use neutral `kind: change` plus deterministic `change-<slug>` / `work/<slug>` collision rules from Intake. A pre-existing non-target branch may be adopted only when exact Git + durable evidence prove it owns this same obligation and establish coherent `base_ref`, `integration_target` and parent metadata; otherwise do not guess or claim it.
4. Ensure the exact workstream branch exists **before** writing migrated managed state. A newly created branch starts from the exact base proven in step 2. Materialize/reconcile one `WORKSTREAM.yaml` and one namespaced `TASK_BOARD.yaml` on that branch, persisting coherent `base_ref`, `integration_target`, `parent_workstream`, `parent_branch`, `parent_dependency`, manifest `task_board`, Task Board `workstream_id` and `execution_ref.branch`. Do not create a second lane when partial migration already materialized the same identity/topology. Once that branch-isolated manifest exists, establish/read back its orchestration binding through **Orchestration reconstruction boundary** before any policy-dependent runtime continuation; never copy a historical root/default runtime profile into it as project authority.
5. Migrate only continuation truth required for coherent recovery: current plan/milestone identity; live/non-terminal Cards and required dependency results; semantic `implementation_owner_role`; exact Card/milestone review requirement/current-attempt/append-only attempt history; implementation/recovery `research_obligation`; Card/milestone result/evidence/test/blocker pointers; and the complete `parallel.current_batch` plus referenced batch/member history needed to preserve frozen base, membership/order, returned/integrated refs and post-batch review-drain lineage. Concrete worker/session/model-instance/invocation/worktree identity is never migrated because it is not Project Workflow authority; the opaque manifest policy/profile selection is established through the runtime owner after the branch-isolated manifest exists, not copied from historical root/default execution state.
6. Preserve immutable completed contracts/evidence/handoffs and batch/review lineage by exact reference when still valid; do not rewrite or duplicate completed history merely for layout. Never reinterpret a historical lane as a new batch or discard an integrated/returned result to simplify migration.
7. If historical root `PROJECT.md` also carries an unreconciled pre-execution exploratory/Research locator for this same obligation, migrate that exact locator into selected manifest `routing.*` ownership defined by M03-T01. Do not mirror lifecycle fields and do not leave two active pointers.
8. Persist concise migration provenance when mapping is non-trivial, including exact source root/default ref, proven target/base/dependency classification and resulting workstream manifest/Task Board ref. The source root/default board remains historical input and is not cleared, advanced or used as a mutable owner merely to mark migration complete.
9. Read back the workstream branch and require manifest ↔ Task Board binding, exact manifest topology matching the proven `integration_target` / `base_ref` / parent classification, and exact preservation of every still-live review/Research/result/dependency/batch obligation. Only after that readback is GREEN may the namespaced Task Board become the selected mutable execution state and normal recovery priority above apply.
10. For a long-lived legacy branch whose root-state files would overwrite independently evolved target-side historical/default files at final integration, apply `REPOSITORY.md#Legacy branch → branch-isolated finalization migration` after active ownership is namespaced. Later root-file reconciliation there is conflict/history preservation, never resumption of root/default execution.
11. If source identity, branch ownership, live obligation, integration target/base/dependency classification, parallel lineage or migration mapping remains ambiguous, preserve source plus any partial target state and fail closed. Ask for user input only when exact durable/Git/PR evidence cannot resolve the ambiguity.

Crash rule: before step 9 succeeds, retry/recover the same deterministic migration identity **and topology** without mutating the source root board. After step 9 succeeds, never route the historical root board as active state; recover the namespaced workstream and its preserved Codex review/batch lineage instead.

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
- multiple `in_progress` Cards occur only when covered by this exact current batch or by one exact post-batch review drain from the same closed `complete` or terminally reconciled `blocked` batch, in which every remaining `in_progress` Card is an integrated member with an outstanding review/finalization/RED-correction obligation;
- no concrete worker/session/model/profile/invocation/lease/resume/worktree-path key is project authority;
- no worker mutated shared Task Board/manifest/integration state.

Contradiction routes to Recovery; never infer the missing fact from runtime memory.

## Batch recovery by durable boundary

Any path in this section that actually launches, resumes, replaces, reruns or re-realizes runtime worker work inherits the single `workflow/codex/CODEX_ORCHESTRATION.md#Codex-only pre-dispatch binding gate` before that runtime operation. The durable batch/member rules below do not duplicate runtime policy interpretation.

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

For member/batch `blocked`, first distinguish pre-launch abandonment from post-launch failure.

A reconciled historical pre-launch abandonment may remain `blocked` with `current_batch: null`; its member Cards must already have been returned to legal READY/serial state and the batch ID is never reused.

For a post-launch blocker such as scope escape, reserved-state mutation, lane failure or material integration conflict:

1. preserve the exact failed/returned result, blocker evidence, every integrated prefix and every unaffected returned sibling;
2. never use the prepared-batch unwind, reset launched members to READY, widen scope or reorder members;
3. if accepted authority plus the frozen Card/base/scope/resource contract are unchanged and the correction is bounded to only the affected member, use same-member retry: preserve the old failed result/ref in durable evidence, clear the member's active `result_commit` while transitioning that member `blocked -> in_progress` under the same batch/lane/base, set the batch back to `running` when no integrated prefix exists or `integrating` when one does, and re-realize only that member from the original base;
4. when the corrected return is durable, repopulate the member's active `result_commit` after the prior failed ref remains recoverable, then validate/integrate it once in the original frozen order;
5. if same-member retry is not legal, terminally reconcile the launched batch: first quiesce/reconcile all runtime-active members, then set every non-integrated member history entry to `blocked` while preserving any returned result/evidence and move every corresponding Card out of batch-owned `in_progress` into durable `blocked` state with exact batch/member/result/evidence linkage;
6. record batch evidence that identifies terminal post-launch reconciliation; after those member/Card transitions are durable, keep the batch as immutable `blocked` history and clear `current_batch`; integrated reviewable members may remain `in_progress` only as the resulting post-batch review drain;
7. after the drain resolves, recover each blocked non-integrated Card serially. A preserved returned result may be reused only after exact revalidation against current authority/head; otherwise re-execute only that affected Card.

This transition is the only legal terminal escape from a launched blocked batch. It preserves successful work without inventing a new batch lineage.

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
- post-launch batch is `blocked` and its affected member is still batch-owned `in_progress` -> recover whether a same-member retry was durably started; if not, either start the bounded retry under the unchanged frozen contract or perform terminal post-launch reconciliation before clearing `current_batch`;
- post-launch batch was cleared while a non-integrated member Card remained `in_progress` -> restore the missing terminal reconciliation by proving runtime quiescence, preserving result/evidence, and moving that Card to `blocked` before later work;
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

Project Workflow does not own concrete worker/session/model-instance/reasoning/invocation/lease/wait/resume/replacement/worktree-path state. Opaque policy/profile selection is durable only in the selected manifest `orchestration` binding. Runtime may resume or replace a realization only after the shared pre-dispatch binding gate; durable Card/batch/lane/result/review semantics remain unchanged.

## Integrated terminal workstream recovery

When an exact durable locator points to a branch-isolated manifest with `status: done` and non-null exact `result`, and finalization evidence shows the workstream reached its final `integration_target`:

- the original source branch may supply provenance but is not required for terminal history;
- after source-branch deletion, recover from the integration-target copy of `implementation/workstreams/<id>/` and validate manifest ↔ Task Board identity there;
- keep Task Board `workstream_id` and `execution_ref.branch` equal to original workstream identity, never the target branch;
- verify referenced terminal Card/evidence/handoff state exists on target and agrees with manifest `result`/PR plus final checkpoint/result pointers;
- do not route a terminal workstream Task Board as active target-branch execution state;
- missing target-side artifacts after source-branch deletion are a finalization defect, never a reason to fall back to root `implementation/TASK_BOARD.yaml`.

Branch-isolated handoffs are recovered through the selected terminal Task Board, not `PROJECT.md -> Latest cumulative handoff`.

## Terminal-unmerged workstream recovery

When a target-side namespaced closure package proves that a branch-isolated Codex-only workstream intentionally reached a terminal state without final integration/merge:

1. validate the package's manifest identity and selected Task Board/history binding when implementation state exists;
2. verify accepted authority for the terminal state and prove no live Card, Research, review, stacked-dependency, integration or other workstream obligation still requires the source branch;
3. use only the exact manifest `branch` as the cleanup target;
4. read current GitHub state for that exact branch:
   - branch exists → Codex Main completes the already-authorized cleanup through authenticated `gh`, then reads back exact absence;
   - branch absent → cleanup is already complete;
5. never recreate the branch, synthesize an alias ref, infer another target from naming/PR state, or create separate cleanup lifecycle/state;
6. preserve terminal history from the target-side closure package even though rejected/superseded implementation content was never integrated.

An interruption after durable closure but before deletion therefore resumes only the delete/readback step. An interruption after deletion resumes as a no-op success. Runtime worker/session identity is never required to decide either case.

## Workstream final-integration review recovery

Manifest final-integration review is independent from Card/milestone Task Board review:

- `pending | in_progress` -> route to `REVIEW.md` with manifest review owner and exact subject;
- `green` -> do not replay review; continue only while exact coverage remains valid under `WORKSTREAMS.md#Integration-refresh-contract`;
- `red` -> preserve the manifest gate/evidence and route deterministic correction; bounded implementation/Research stays on the selected Task Board;
- qualified micro-fix with terminal reviewed Card and no active manifest pending/RED gate -> Close runs target refresh before coverage reuse/freeze;
- changed integrated subject invalidates stale coverage and requires a new immutable formal-review subject.

Never inspect or mutate another workstream Task Board to recover this gate.

## Full lifecycle resume

Recovery may also restore active Intake, selected-manifest exploratory/pre-execution Research locators, plan review, migrated historical state, stacked dependency/refresh state, terminal-unmerged closure/delete obligations and other Close obligations through the exact owning modules referenced by `ROUTER.md`. Historical root `PROJECT.md` routing pointers and root/default Task Board state are migration inputs only and never resume as active owners.

After durable state is coherent, return to `workflow/codex_only/ROUTER.md`. Do not stop merely because recovery succeeded when deterministic legal work can continue. Use the normal human-facing stop contract only for unresolved user/product authority, explicit authorization or a concrete unremediable runtime/input blocker.
