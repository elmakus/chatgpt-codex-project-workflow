# ChatGPT-only Recovery

Recovery reconstructs execution truth from durable project state without prior chat.

## Inputs

Read:
- project `PROJECT.md`;
- `implementation/TASK_BOARD.yaml`;
- exact active branch/HEAD;
- relevant runtime/external state;
- current milestone/Card contracts;
- active review state;
- Task Board `research_obligation` and its exact research record when present;
- referenced evidence/result/OpenSpec/blocker;
- handoff only when materially needed.

Previous chat narrative is not authority.

## Recovery priority

1. REQUIRED/RECOMMENDED `review_state: pending | in_progress` outranks later implementation.
2. A non-terminal REQUIRED/RECOMMENDED subject with `review_state: red` routes to **RED review recovery** below before any new Card.
3. An `in_progress` Card with `review_state: green` and complete persisted implementation/result evidence routes to Execution for terminal Post-review Card finalization before any new Card.
4. Task Board `research_obligation` with research `Status: active | blocked | complete` outranks selecting new implementation and recovers through **Implementation-owned Research** below.
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
4. read `workflow/chatgpt_only/REVIEW.md#RED → corrective-route transition` and classify the persisted failing evidence under that canonical transition;
5. bounded L1/L2 correction inside accepted authority → return through the router to Execution Prep or Execution;
6. plan-only correction while Project Definition remains valid → Strategic planning;
7. accepted requirement/strategic/global-target change → Project Definition;
8. missing evidence needed before classification/correction → create the exact implementation-owned Research record + Task Board `research_obligation` before yielding, with `Return target: execution_resolution:<exact affected subject>`, then route to Research;
9. unresolved user/product authority or another explicit real gate → use the normal user-stop contract.

When correction changes the reviewable implementation subject, preserve the old RED evidence, freeze the new exact subject as a new `pending` review attempt, and require a fresh independent reviewer before terminal Card completion.

## Implementation-owned Research

When Task Board `research_obligation` points to an implementation/recovery Research record:
- read that exact record; Task Board stores only the pointer while the research record owns Status, Origin and Return target;
- `active | blocked` → route to Research;
- `complete` → route to the exact recorded Return target, normally `execution_resolution:<subject>`, without clearing the pointer first;
- `consumed` → clear the stale Task Board pointer at the next safe edit;
- missing/mismatched pointer, Origin subject or Return target → preserve as inconsistent state rather than infer from chat.

The Return target must durably reconcile/classify the findings before setting the record to `consumed` and clearing Task Board `research_obligation`.

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
