# ChatGPT-only Recovery

Recovery reconstructs execution truth from durable project state without prior chat.

## Inputs

Read:
- project `PROJECT.md`;
- `workflow/chatgpt_only/WORKSTREAMS.md` when branch-isolated;
- exact active branch/HEAD;
- validated workstream manifest + its selected canonical Task Board when branch-isolated, otherwise legacy/default `implementation/TASK_BOARD.yaml`;
- relevant runtime/external state;
- current milestone/Card contracts;
- active review state;
- Task Board `research_obligation` and its exact research record when present;
- referenced evidence/result/OpenSpec/blocker;
- handoff only when materially needed.

Previous chat narrative is not authority.

## Recovery priority

Apply this priority only inside the selected default/workstream Task Board. An unrelated workstream's active Card/review is not a blocker for this one.

1. REQUIRED/RECOMMENDED `review_state: pending | in_progress` outranks later implementation.
2. Task Board `research_obligation` with research `Status: active | blocked | complete` outranks selecting new implementation, including when opened from a RED verdict, and recovers through **Implementation-owned Research** below.
3. A non-terminal REQUIRED/RECOMMENDED subject with `review_state: red` and no already-materialized Research continuation routes to **RED review recovery** below before any unrelated/new Card.
4. An `in_progress` Card with `review_state: green` and complete persisted implementation/result evidence routes to Execution for terminal Post-review Card finalization before any new Card.
5. Any other existing `in_progress` Card outranks selecting a new Card.
6. Existing `blocked` Card must be re-evaluated before dependent work.
7. Only when no active obligation exists may next READY Card be selected.

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

Do not create synchronization edits merely to make documents look consistent.

## Resume

After durable state is coherent, the recovery role is complete.

Return to `workflow/chatgpt_only/ROUTER.md`. The router selects execution, review, close or strategic resolution from the recovered state.

Do not end the turn simply because recovery succeeded if deterministic legal work can immediately continue.

Strategic uncertainty that is classifiable from durable authority returns to the router for Planning / Project Definition / Research. Use root `CHATGPT.md#Real-stop-response-contract` only when recovery still requires unresolved user/product authority, explicit authorization, or concrete runtime/access/input.
