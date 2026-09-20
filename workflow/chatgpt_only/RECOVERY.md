# ChatGPT-only Recovery

Recovery reconstructs execution truth from durable project state without prior chat.

## Inputs

Read:
- project `PROJECT.md`;
- `workflow/chatgpt_only/WORKSTREAMS.md` when branch-isolated;
- for ordinary pre-integration non-terminal work, exact active workstream branch/HEAD;
- for a successful final-target merge whose closure is not yet terminal, the exact merge-result target-side namespaced workstream package plus immutable PR/merge evidence; the source branch may already be absent;
- for an integrated terminal `done` workstream whose source branch was deleted, the exact target-side namespaced workstream package plus manifest integration result;
- for terminal-unmerged cleanup history after source-branch deletion, the exact durable closure package plus manifest `branch_cleanup` evidence;
- validated workstream manifest + its selected canonical Task Board/history source for active managed work; when no workstream is selected and historical root/default `implementation/TASK_BOARD.yaml` exists, read it only as migration input under **Historical root/default migration before mutation** below;
- relevant runtime/external state;
- current milestone/Card contracts;
- active Card/milestone review state from the selected Task Board;
- selected manifest workstream final-integration review state when branch-isolated;
- Task Board `research_obligation` and its exact research record when present;
- referenced evidence/result/OpenSpec/blocker;
- handoff only when materially needed.

Previous chat narrative is not authority.

## Recovery priority

Apply this priority only after an exact branch-isolated workstream Task Board has been selected and binding validation passed. Historical root/default state must complete the migration-before-mutation protocol below first. An unrelated workstream's active Card/review is not a blocker for this one.

1. REQUIRED/RECOMMENDED `review_state: pending | in_progress` outranks later implementation.
2. Task Board `research_obligation` with research `Status: active | blocked | complete` outranks selecting new implementation, including when opened from a RED verdict, and recovers through **Implementation-owned Research** below.
3. A non-terminal REQUIRED/RECOMMENDED subject with `review_state: red` and no already-materialized Research continuation routes to **RED review recovery** below before any unrelated/new Card.
4. An `in_progress` Card with `review_state: green` and complete persisted implementation/result evidence routes to Execution for terminal Post-review Card finalization before any new Card.
5. Any other existing `in_progress` Card outranks selecting a new Card.
6. Existing `blocked` Card must be re-evaluated before dependent work.
7. When no higher-priority Task Board obligation remains, a selected manifest final-integration `review.state: pending | in_progress` routes to Independent review before new/later implementation for that workstream.
8. A selected manifest final-integration `review.state: red` routes through the same RED corrective classification, with any corrective execution/Research confined to this selected workstream Task Board.
9. Exact immutable PR/merge evidence proving final-target integration while target-side closure/result reconciliation is unfinished routes to Close using the post-merge target-side package, even when the source branch has already disappeared.
10. A qualified micro-fix whose bounded Card is terminal and whose selected workstream is not done routes to Close once higher-priority Task Board or manifest pending/RED review obligations are absent; Close runs target refresh before final-review reuse/freeze and integration. Do not start another Card and do not synthesize a milestone.
11. Only when no active obligation exists may next READY Card be selected.

## Historical root/default migration before mutation

When no branch-isolated workstream is selected and historical root/default state contains a live managed-change obligation, migration itself outranks review, Research, Execution Prep and Execution. Do not resume or normalize the root/default board in place.

1. Read the root `implementation/TASK_BOARD.yaml` plus only its exact current contracts, review/Research pointers, evidence/results, handoff and Git state needed to identify the live obligation. This discovery is read-only with respect to root/default execution state.
2. Establish one exact migration identity. First recover any existing branch/manifest/PR that durably represents this same obligation. Otherwise use neutral `kind: change` identity and the deterministic `change-<slug>` / `work/<slug>` collision rules from `INTAKE.md#Workstream identity and naming`. A pre-existing non-target branch may be adopted as the workstream branch only when exact Git + durable state prove it owns this same obligation and no conflicting manifest exists; ambiguity fails closed.
3. Ensure the exact workstream branch exists **before** writing migrated managed state. Materialize/reconcile one `WORKSTREAM.yaml` plus one namespaced `TASK_BOARD.yaml` on that branch, with exact manifest `id/branch/task_board` ↔ Task Board `workstream_id/execution_ref.branch` binding. Do not create a second lane when a partial migration already materialized the same identity.
4. Migrate only continuation truth required for coherent recovery: current plan/milestone identity, live/non-terminal Cards and required dependency results, exact Card/milestone review fields, implementation/recovery Research pointer, result/evidence/test pointers, blockers and execution provenance. Preserve immutable historical contracts/evidence/handoffs by exact reference when they remain valid; do not rewrite or duplicate completed history merely for layout.
5. If historical root `PROJECT.md` also carries an unreconciled pre-execution exploratory/Research locator for this same obligation, migrate that exact locator into the selected manifest `routing.*` ownership defined by M02-T01. Do not mirror lifecycle fields and do not leave two active pointers.
6. Persist concise migration provenance when the mapping is non-trivial, including the exact source root/default state ref and the resulting workstream manifest/Task Board ref. The source root/default board remains historical input and is not cleared, advanced or used as a mutable owner merely to mark migration complete.
7. Read back the workstream branch and require successful manifest ↔ Task Board binding plus exact preservation of every still-live review/Research/result dependency. Only after that readback is GREEN may the namespaced Task Board become the selected mutable execution state and normal recovery priority above apply.
8. For a long-lived legacy branch whose root-state files would overwrite independently evolved target-side historical/default files at final integration, apply `REPOSITORY.md#Legacy branch → branch-isolated finalization migration` after active ownership is namespaced. Any later root-file reconciliation there is conflict-avoidance/history preservation, never resumption of root/default execution.
9. If source identity, branch ownership, current live obligation or migration mapping remains ambiguous, preserve both source and any partial target state and fail closed. Ask for user input only when exact durable/Git evidence cannot resolve the ambiguity.

Crash rule: before step 7 succeeds, retry/recover the same deterministic migration identity without mutating the source root board. After step 7 succeeds, never route the historical root board as active state; recover the namespaced workstream instead.

## In-progress Card

- verify branch/HEAD against Task Board pointers;
- inspect actual implementation/tests/evidence;
- run Refresh Gate;
- continue from proven durable state;
- do not restart completed steps blindly;
- do not claim completion without required verification.

## Blocked Card

Determine whether blocker has been durably resolved.

If yes:
- reconcile Task Board;
- rerun relevant Refresh Gate;
- resume same Card.

If no:
- preserve blocked state;
- report smallest actual required action.

## Pending/in-progress review

Route directly to `REVIEW.md`.

Reviewer recovers exact immutable subject and same authority slice. It must not use previous implementing-session narrative as evidence.

## RED review recovery

A persisted RED verdict is already a completed independent-review result. Recovery must not silently discard it, treat it as generic execution, or re-run review merely to discover continuation.

1. recover the exact `review_subject`, RED review evidence and the reviewed Card/milestone authority;
2. verify the RED evidence still refers to that exact immutable reviewed subject;
3. keep the reviewed Card/milestone non-terminal;
4. read `workflow/chatgpt_only/REVIEW.md#RED → corrective-route transition` and classify the persisted failing evidence against current durable state under that canonical transition;
5. if the failing condition has already been durably reconciled by a completed correction role, do not repeat that role; recover the next downstream obligation from current authority/state. If the corrected implementation subject is already durable but its next REQUIRED/RECOMMENDED review attempt has not yet been frozen, the next obligation is Execution reconciliation that freezes the new exact subject as `pending` before any later work;
6. bounded L1/L2 correction inside accepted authority → return through the router to Execution Prep or Execution;
7. plan-only correction while Project Definition remains valid → Strategic planning;
8. accepted requirement/strategic/global-target change → Project Definition;
9. missing evidence needed before classification/correction → if no matching Research continuation exists, create the exact implementation-owned Research record + Task Board `research_obligation` before yielding, with `Return target: execution_resolution:<exact affected subject>`; if it already exists, reuse it instead of creating another; then route to Research;
10. unresolved user/product authority or another explicit real gate → use the normal user-stop contract.

When correction changes the reviewable implementation subject, preserve the old RED evidence, freeze the new exact subject as a new `pending` review attempt, and require a fresh independent reviewer before terminal Card completion.

## Post-merge closure recovery

When immutable Git/PR evidence proves that the selected workstream's exact source head was merged into its declared final `integration_target`, but terminal target-side reconciliation/readback is incomplete:

- recover the exact namespaced workstream package from the merge-result target state;
- validate manifest ↔ Task Board identity there under `WORKSTREAMS.md#Post-merge-closure-workstream`; keep manifest `branch` and Task Board `execution_ref.branch` as the original source provenance;
- do not require or recreate the source ref merely because GitHub deleted the merged head automatically;
- verify the target-side package is the package carried by that exact merge using immutable PR/merge evidence, not only a matching workstream ID from an unrelated/stale target state;
- do not route that Task Board as active target-branch implementation state;
- route unfinished merge-result bookkeeping/readback to Close;
- if the exact required target-side package is missing, preserve a finalization defect. Never fall back to root `implementation/TASK_BOARD.yaml` and never manufacture a replacement source ref.

This transition ends when target-side closure reconciliation/readback records coherent terminal result state.

## Terminal unmerged cleanup recovery

When a workstream was intentionally closed/superseded without final-target integration and its source branch is cleanup-eligible or already deleted:

- recover from an exact durable closure package independent of that source ref;
- require explicit terminal workstream state and exact `branch_cleanup.ref == manifest.branch`, `verified_head` and durable cleanup evidence;
- require no live Card, Research, review, stacked-dependency or integration obligation;
- a closed PR by itself never establishes deletion safety;
- if `state: safe_to_delete` and the source ref still exists, re-read its HEAD before physical deletion; a mismatch with `verified_head` makes readiness stale and deletion is forbidden until revalidated;
- if `state: deleted`, require durable readback evidence that the exact ref is absent;
- do not import rejected/superseded implementation content into the integration target merely to preserve cleanup history.

A cleanup marker that exists only on the source branch it authorizes deleting is not durable terminal recovery state.

## Integrated terminal workstream recovery

When an exact durable locator points to a branch-isolated manifest with `status: done` and non-null exact `result`, and finalization evidence shows the workstream reached its final `integration_target`:

- if the original source branch still exists, it may supply additional Git provenance but is not required for terminal history;
- if the source branch was deleted, recover from the integration-target copy of `implementation/workstreams/<id>/` and validate manifest ↔ Task Board identity there;
- require Task Board `workstream_id` and `execution_ref.branch` to remain equal to the original manifest identity; do not rewrite them to the target branch;
- verify referenced terminal Card/evidence/handoff state exists on the target and that manifest `result`/PR plus Task Board final checkpoint/result pointers agree with the recorded integration outcome;
- do not route a terminal workstream Task Board as active target-branch execution state;
- if required terminal artifacts exist only on a deleted branch, preserve the inconsistency as a finalization defect rather than falling back to root `implementation/TASK_BOARD.yaml`.

`PROJECT.md -> Latest cumulative handoff` is not a branch-isolated recovery pointer. Resolve branch-isolated milestone handoffs through the selected terminal Task Board.

## Workstream final-integration review recovery

For a selected branch-isolated workstream, manifest final-integration review is recovered independently from Card/milestone Task Board review.

- `pending | in_progress` → route to `REVIEW.md` with the exact manifest as review owner and exact manifest `review.subject`;
- `green` → do not replay review; continue only if the GREEN subject still equals the exact integrated subject;
- `red` → keep the manifest gate RED and classify deterministic correction under `REVIEW.md#RED → corrective-route transition`; bounded correction and implementation-owned Research stay on the selected Task Board;
- qualified micro-fix with terminal GREEN-reviewed fix Card and no active pending/RED manifest gate → route to Close for integration refresh first, then exact coverage reuse or a newly frozen manifest review subject;
- a manifest review subject that no longer matches the integrated subject is not GREEN coverage; freeze/review the changed exact subject before integration.

Never inspect or mutate another workstream Task Board to recover or repair this gate.

## Implementation-owned Research

When Task Board `research_obligation` points to an implementation/recovery Research record:
- read that exact record; Task Board stores only the pointer while the research record owns Status, Origin and Return target;
- `active | blocked` → route to Research;
- `complete` → route to the exact recorded current Return target without clearing the pointer first;
- when that target is `execution_resolution:<subject>`, recover the classifier; it either durably refines Return target to the exact final owning role/subject while keeping `Status: complete`, `Return reconciliation: pending` + the Task Board pointer, or—when classification itself needs more evidence—uses `RESEARCH.md#Intermediate execution-resolution classifier` to atomically consume `R1`, create `R2 active`, and switch the pointer to `R2`;
- at a final Return target, apply `workflow/chatgpt_only/RESEARCH.md#Final Return-target protocol`; `Return reconciliation: applied` means target work is already durable and recovery is consume/clear-only;
- normally only the final owning Return target marks the record `consumed` and clears Task Board `research_obligation`; classifier-to-Research chaining is the sole exception and must replace the pointer with the exact new active record in the same durable transition;
- `consumed` with a leftover pointer → if its reconciliation result names an exact active chained Research record, reconcile the pointer to that record; otherwise clear the stale pointer at the next safe edit;
- missing/mismatched pointer, Origin subject or Return target → preserve as inconsistent state rather than infer from chat.

Thus a fresh session always recovers either Research, the classifier, or the final owning return role from one durable pointer/record.

## Inconsistent state

When Task Board, Git/runtime or evidence disagree:
- do not guess;
- inspect exact durable evidence;
- reconcile only facts that can be proven;
- preserve unresolved contradiction as blocker.

A `branch_cleanup: safe_to_delete` record is inconsistent when its ref differs from manifest `branch`, required exact head/evidence is missing, current surviving ref HEAD differs from `verified_head`, or terminal-unmerged cleanup truth exists only on the source ref. A missing post-merge target-side package after automatic source deletion is a finalization defect, not permission to select the legacy/default Task Board.

Do not create synchronization edits merely to make documents look consistent.

## Resume

After durable state is coherent, including selected manifest review state when branch-isolated, the recovery role is complete.

Return to `workflow/chatgpt_only/ROUTER.md`. The router selects execution, review, close or strategic resolution from the recovered state.

Do not end the turn simply because recovery succeeded if deterministic legal work can immediately continue.

Strategic uncertainty that is classifiable from durable authority returns to the router for Planning / Project Definition / Research. Use root `CHATGPT.md#Real-stop-response-contract` only when recovery still requires unresolved user/product authority, explicit authorization, or concrete runtime/access/input.
