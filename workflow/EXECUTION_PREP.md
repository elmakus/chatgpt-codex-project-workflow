# Execution Preparation

Execution preparation converts an approved plan into a bounded execution package without prematurely freezing code-dependent detail.

## Preconditions

Before creating executable cards:
- authoritative requirements are identifiable;
- accepted architecture decisions are recorded;
- current Master Plan/milestone is approved;
- unresolved product questions that would invalidate implementation are either resolved or explicitly blocking.

## Steps

1. Inspect the current project repository and relevant source state.
2. Define or refresh the milestone file.
3. Decompose work into bounded Task Cards under `implementation/cards/`.
4. Record dependencies, priority, complexity, phase and expected code locations.
5. Define acceptance criteria and required tests for every card.
6. Mark OpenSpec candidates according to `workflow/contracts/OPENSPEC.md`; do not create distant specs merely "for later".
7. Initialize/update `implementation/TASK_BOARD.yaml`.
8. Confirm requirement coverage.
9. Audit sizing, dependencies, side effects, idempotency, security and migration concerns.
10. Set a card to `ready` only when its dependencies and prerequisites allow execution.

## Card versus OpenSpec task

A Task Card is a bounded global work package. An OpenSpec `tasks.md` item is a smaller implementation checkbox inside one OpenSpec change. They are not interchangeable.

## Git preparation

Follow `workflow/contracts/PROJECT_REPOSITORY.md#git-and-branch-policy` and `workflow/contracts/GITHUB_STATE.md`.

Large milestone implementation should use an isolated branch/PR when the project normally uses PRs. Do not change repository ownership/topology during an active milestone.

## Handoff input

Execution prep must consult the latest cumulative handoff when one exists. It describes what actually became true at the last green milestone and is a primary input to the next execution package.

## Required completion handoff to the user

Execution preparation is not complete until ChatGPT also tells the user exactly how to start execution. After the durable prep artifacts are written, the final user-visible response must contain all of the following:

1. `EXECUTION PREP COMPLETE:` with the prepared milestone, required prior checkpoint and the durable start/kickoff pointer.
2. `CODEX SESSION RECOMMENDATION:` with exactly one of:
   - `FRESH` — start a new Codex session;
   - `CONTINUE EXISTING` — send the prompt to the currently active Codex session.
3. A short reason for that session recommendation.
4. `CODEX START PROMPT:` followed by a copy-paste-ready prompt that is sufficient to start the prepared milestone from durable repository state.
5. `USER ACTION:` stating the smallest concrete next step, for example `Start a fresh Codex session with the prompt above.` or `Send the prompt above to the current Codex session.`

Do not make the user infer whether a fresh Codex session is preferable, whether the old session should be reused, or what text should be sent to Codex.

### Session recommendation rule

Recommend `FRESH` by default when execution prep starts a new milestone after a completed green checkpoint, especially when the prior Codex session completed the previous milestone. The cumulative handoff and repository state are designed to make that boundary self-contained, and carrying the previous milestone's execution context usually adds stale/noisy context without adding authority.

Recommend `CONTINUE EXISTING` when the prep is for the same still-active milestone and the current Codex session already holds useful, current execution context that materially helps the next step without creating stale-context risk.

Also recommend `FRESH` when a prior session accumulated a major strategic blocker, long investigation, material course correction or other context that is no longer needed after durable reconciliation. If uncertain at a clean milestone boundary, prefer `FRESH`.

A session recommendation is context-hygiene guidance, not a product decision or authorization gate. Never present `FRESH` as mandatory unless an accepted project/milestone contract explicitly requires a fresh context.

### Start-prompt rule

The generated `CODEX START PROMPT` should be short and rely on durable repository artifacts instead of restating the whole plan. It should identify at minimum:
- current workflow authority: `elmakus/chatgpt-codex-project-workflow:main`;
- project repository;
- prepared milestone;
- required prior checkpoint;
- the repo-relative start router and/or Codex kickoff prepared for that milestone when present;
- instruction to recover Task Board/card state, run the Refresh Gate and execute cards according to dependencies;
- instruction to continue automatically between deterministic READY cards;
- instruction to stop only for a genuine strategic blocker, explicit user-authorization gate, recommended session handoff, or final milestone checkpoint;
- instruction not to begin the next milestone silently.

If the project already contains a milestone-specific kickoff file, point Codex to it rather than duplicating its detailed contents in chat.
