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
- referenced evidence/result/OpenSpec/blocker;
- handoff only when materially needed.

Previous chat narrative is not authority.

## Recovery priority

1. REQUIRED/RECOMMENDED `review_state: pending | in_progress` outranks later implementation.
2. Existing `in_progress` Card outranks selecting a new Card.
3. Existing `blocked` Card must be re-evaluated before dependent work.
4. Only when no active obligation exists may next READY Card be selected.

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

## Inconsistent state

When Task Board, Git/runtime or evidence disagree:
- do not guess;
- inspect exact durable evidence;
- reconcile only facts that can be proven;
- preserve unresolved contradiction as blocker.

Do not create synchronization edits merely to make documents look consistent.

## Resume

After durable state is coherent, route to:
- `EXECUTION.md` for implementation;
- `REVIEW.md` for review;
- `CLOSE.md` for accepted milestone close;
- strategic resolution for L3 blocker.

Do not end the turn simply because recovery succeeded if deterministic legal work can immediately continue.
