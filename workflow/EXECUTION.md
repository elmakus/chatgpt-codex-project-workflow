# Execution

Codex is the implementation/execution authority inside approved product, architecture and behavior contracts.

Read and obey:
- `workflow/contracts/GITHUB_STATE.md`;
- `workflow/contracts/TASK_CARDS.md`;
- `workflow/contracts/OPENSPEC.md`;
- `workflow/contracts/CHATGPT_CODEX.md`;
- `workflow/contracts/CODEX_ORCHESTRATION.md` as the project/runtime authority boundary;
- project `PROJECT.md`.

When the owner's `codex_workflow` is installed and enabled, its installed instructions govern internal Codex runtime orchestration. This Project Workflow continues to govern project scope, state, acceptance, evidence and strategic boundaries.

## Standard card loop

1. Establish repository root, branch, exact HEAD and working-tree state.
2. Read Task Board and recover a valid `in_progress` card if one exists.
3. Otherwise select the first `ready` card whose dependencies are `done`; never select `planned`, `blocked`, `done` or `superseded`.
4. Transition the card to `in_progress`, and the milestone to `in_progress` if this is its first real execution.
5. Run the Refresh Gate before implementation.
6. Create/reconcile OpenSpec just-in-time if required.
7. Implement only the card scope.
8. Run required tests and verify card acceptance plus relevant OpenSpec behavior.
9. If green, persist result/evidence and result pointers before marking the card `done`.
10. Commit/push durable state according to project branch policy.
11. Unblock eligible dependent cards.
12. Continue to the next READY card when milestone policy allows; do not ask the user to choose when the Task Board is unambiguous.
13. After required cards are done, run integrated milestone acceptance.
14. RED → reopen/create corrective work. GREEN → follow milestone close and handoff.

## User-visible continuation status

A user-visible execution checkpoint must never leave it ambiguous whether Codex is waiting for the user or continuing autonomously.

When Codex sends a user-visible status during execution, end it with exactly one explicit continuation state appropriate to the situation:

- `NEXT ACTION: continuing automatically with <card/action>; no user action required.` when the Task Board and milestone policy permit deterministic continuation;
- `USER ACTION REQUIRED: <smallest concrete decision, authorization or input>.` only when execution genuinely cannot continue without the user;
- `SESSION HANDOFF RECOMMENDED: <reason>. NEXT ACTION: start a fresh Codex session from <durable pointer>.` when a fresh context is beneficial for context/recovery reasons rather than a product decision;
- `MILESTONE COMPLETE: <checkpoint>.` when the milestone has been fully closed and checkpointed.

A routine GREEN Task Card is not, by itself, a reason to stop. If the next READY card is deterministic, continue the standard card loop. If execution intentionally ends at a session boundary despite there being no user decision gate, make clear that no approval is needed and provide the exact durable continuation pointer.

Do not use a neutral status-only ending such as `T01 GREEN; T02 planned` when that can be mistaken for a request to intervene. Do not convert an informational checkpoint into an implicit wait.

## Refresh Gate

Before implementation compare at minimum:
- actual HEAD and working tree;
- latest cumulative handoff;
- current milestone;
- current Task Card;
- relevant Master Plan sections / accepted decisions / requirements;
- current relevant OpenSpec;
- completed dependencies;
- actual code locations and interfaces.

If the mismatch is a local implementation detail and remains within approved behavior/architecture/requirements, reconcile the card/OpenSpec within Codex authority.

If evidence materially changes behavior, architecture, a frozen decision, a requirement, an external contract, or milestone acceptance, do not implement the stale card. Persist evidence, set the card `blocked`, and use the strategic blocker protocol.

## Failure recovery

If a session ends unexpectedly:
- recover the existing `in_progress`/`blocked` card;
- inspect Git branch/HEAD/working tree;
- inspect OpenSpec task state;
- inspect relevant tests;
- inspect card `result_*` and evidence pointers;
- use any local `current.md` only as a hint;
- continue the same card unless durable state proves it was completed or superseded.

Do not silently advance to the next card. Recovery must be possible from durable repository state without a local checkpoint.
