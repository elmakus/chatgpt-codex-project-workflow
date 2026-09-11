# Shared Execution Core

This module defines project execution semantics shared by ChatGPT and Codex.

The selected executor also reads its thin adapter:
- ChatGPT → `workflow/chatgpt/EXECUTION.md`;
- Codex → `workflow/codex/EXECUTION.md`.

Read applicable `GITHUB_STATE.md`, `TASK_CARDS.md`, `OPENSPEC.md` and project `PROJECT.md`.

## Standard card loop

1. Establish repository root, primary milestone implementation branch, exact HEAD, working-tree state and relevant external/runtime baseline. Normal production implementation must not run directly on `main`.
2. Read Task Board and recover a valid `in_progress` card if one exists.
3. Otherwise select the first `ready` card whose dependencies are `done`; never select `planned`, `blocked`, `done` or `superseded`.
4. Record the selected `executor`; transition card to `in_progress`, and milestone to `in_progress` if this is its first real execution.
5. Run the Refresh Gate before implementation.
6. Create/reconcile OpenSpec just-in-time if required.
7. Implement only bounded card scope on the primary milestone implementation branch.
8. Run required tests/checks and verify card acceptance plus relevant OpenSpec behavior.
9. For material external mutations, perform required readback/verification.
10. If green, persist result/evidence/result pointers before marking the card `done`.
11. Commit/push durable state to the primary milestone implementation branch according to project policy; do not create per-card PRs.
12. Unblock eligible dependent cards.
13. Continue to the next deterministic READY card on the same milestone branch when project policy, selected executor and session context allow; do not ask the user to choose when Task Board is unambiguous.
14. After required cards are done, run integrated milestone acceptance on the intended final milestone branch HEAD.
15. RED → reopen/create corrective work on the same milestone branch. GREEN → proceed to milestone review/finalization; do not merge directly from card execution.

## Git branch boundary

`main` is the latest accepted GREEN checkpoint, not an active implementation branch.

For every executable milestone:
- all normal production Task Card commits belong on the one primary milestone implementation branch created from the previous GREEN `main` checkpoint;
- corrective work before merge stays on that same branch;
- experimental Path A/Path B branches are separate research/prototype paths only and must be integrated onto the primary milestone branch before production acceptance;
- only the final accepted milestone state goes through the milestone PR to `main`.

If execution is on `main` when a normal production mutation is about to occur, stop before mutation and restore the milestone branch context. A post-merge metadata-only reconciliation commit explicitly allowed by the Git/branch contract is not normal production implementation.

## User-visible continuation status

Execution checkpoints must not make it ambiguous whether work continues or needs user action.

Use an explicit state appropriate to the situation:
- `NEXT ACTION: continuing automatically with <card/action>; no user action required.` when deterministic continuation is valid;
- `USER ACTION REQUIRED: <smallest concrete decision/authorization/input>.` only when execution genuinely cannot continue without the user;
- `SESSION HANDOFF RECOMMENDED: <reason>. NEXT ACTION: start a fresh <ChatGPT chat|Codex session> from <durable pointer>.` when fresh context is beneficial but not a product/authorization gate;
- `MILESTONE COMPLETE: <checkpoint>.` only after the milestone PR is merged and post-merge reconciliation is complete.

A routine GREEN card is not itself a reason to stop.

## Refresh Gate

Before implementation compare at minimum:
- actual branch/HEAD/working tree and relevant runtime/external state;
- previous accepted GREEN `main` checkpoint and current milestone implementation branch;
- latest cumulative handoff;
- current milestone;
- current Task Card;
- relevant Master Plan/accepted decisions/requirements;
- current relevant OpenSpec;
- completed dependencies;
- actual code/runtime interfaces;
- capabilities, tests/checks and evidence/readback needed to satisfy the card.

If mismatch is a local implementation detail within approved behavior/architecture/requirements, reconcile it within executor authority.

If evidence materially changes behavior, architecture, a frozen decision, requirement, external contract or milestone acceptance, do not implement the stale card. Persist evidence, set card `blocked` and use strategic resolution.

## Capability boundary

Starting a card does not authorize pretending a missing capability exists.

Project routing assumes the capability invariant:

`ChatGPT capabilities ⊆ Codex capabilities`

The ChatGPT Capability Gate is a **pre-assignment routing mechanism**. It is not a runtime fallback mechanism after execution has started.

If the selected executor discovers during execution that a required environment access, MCP, credential, runtime/tool, test path, external write/readback or evidence capability is unavailable:
- stop affected work safely;
- persist the exact missing capability and available evidence;
- set the card `blocked` when its contract cannot be met;
- report `USER ACTION REQUIRED` with the smallest concrete capability/access/configuration the user must provide;
- resume the **same card with the same assigned executor** after that capability is provided and durable state is reconciled.

Do not automatically change executors after a runtime capability failure. In particular, when Codex discovers a missing required capability, do **not** invoke `workflow/chatgpt/CAPABILITY_GATE.md` and do not fall back to ChatGPT; under the capability-superset invariant ChatGPT cannot provide a capability that Codex lacks.

## External write contract

For material mutation of GitHub, Liftosaur, APIs, calendars, Drive, configuration or another external system:

```text
WRITE → READBACK → VERIFY EXPECTED STATE → EVIDENCE
```

Use readback when it provides meaningful independent confirmation of persisted state. A write success response alone is not full evidence when target state can and should be re-read.

Do not apply readback mechanically when no meaningful readback exists or a provider already returns sufficient authoritative immutable evidence. Record the limitation rather than inventing verification.

## Strategic blocker handling

A strategic blocker is not a routine executor-routing problem. Persist exact evidence and stop dependent work when a product/behavior/architecture/frozen-requirement/external-contract/acceptance decision exceeds current executor authority.

ChatGPT may resolve strategic questions in normal chat with the user/accepted governance authority and persist the accepted decision.

When Codex uses a configured correlated ChatGPT control channel, `workflow/codex/HANDOFF.md` defines the `request_id`/`DECISION FOR CODEX:` protocol.

## Failure recovery

If a session ends unexpectedly:
- recover existing `in_progress`/`blocked` card;
- inspect Git branch/HEAD/working tree and relevant external/runtime state;
- confirm the recovered branch is the current milestone's one primary implementation branch rather than `main` or an abandoned experimental path;
- inspect OpenSpec task state and tests;
- inspect card `executor`, `result_*` and evidence pointers;
- use any local `current.md` only as a hint;
- continue the same card unless durable state proves completion/supersession or an explicit user/strategic decision changes the assignment.

A runtime capability blocker resumes on the same card/executor after the user supplies the missing capability. Do not silently advance to the next card or reroute through the ChatGPT Capability Gate. Recovery must be possible from durable repository state without prior chat.
