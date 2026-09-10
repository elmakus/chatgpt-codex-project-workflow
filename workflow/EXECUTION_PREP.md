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
