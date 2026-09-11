# Execution Preparation

Execution preparation converts an approved plan into a bounded execution package without prematurely freezing code-dependent detail.

## Preconditions

Before creating executable cards:
- authoritative requirements are identifiable;
- accepted architecture decisions are recorded;
- current Master Plan/milestone is approved;
- unresolved product questions that would invalidate implementation are resolved or explicitly blocking;
- project `execution_policy` is explicitly `chatgpt_only` or `mixed`;
- current `main` is the latest accepted GREEN checkpoint.

## Steps

1. Inspect current project repository and relevant source/runtime state.
2. Verify the exact current GREEN `main` checkpoint and create/reuse exactly one primary implementation branch for the milestone from that checkpoint.
3. Record that milestone branch in the Task Board/execution ref before normal production implementation starts.
4. Decompose work into bounded Task Cards under `implementation/cards/`.
5. Record dependencies, priority, complexity, phase and expected code locations.
6. Define acceptance criteria and required tests/checks for every card.
7. Identify material external writes and required readback/verification evidence.
8. Add explicit `required_capabilities` only for unusual, external, high-risk or routing-significant work; ordinary repo capabilities remain inferred.
9. Classify independent review as REQUIRED/RECOMMENDED/OPTIONAL where material.
10. Mark OpenSpec candidates according to `workflow/contracts/OPENSPEC.md`; do not create distant specs merely for later.
11. Initialize/update `implementation/TASK_BOARD.yaml`.
12. Confirm requirement coverage.
13. Audit sizing, dependencies, side effects, idempotency, security and migration concerns.
14. Set a card `ready` only when dependencies/prerequisites allow execution.
15. For the next executable card, run `workflow/chatgpt/CAPABILITY_GATE.md`.

## Card versus OpenSpec task

A Task Card is a bounded global work package. An OpenSpec `tasks.md` item is a smaller implementation checkbox inside one change. They are not interchangeable.

## Git preparation

Follow `workflow/contracts/PROJECT_REPOSITORY.md#8-git-and-branch-policy` and `workflow/contracts/GITHUB_STATE.md`.

The branch policy is mandatory for normal production execution:
- `main` is the previous accepted GREEN checkpoint;
- one milestone uses one primary implementation branch;
- all Task Cards and pre-merge corrective work are committed on that branch;
- do not create one PR per Task Card;
- do not perform normal production implementation directly on `main`;
- after integrated GREEN acceptance and applicable review, open one milestone PR to `main`;
- RED milestones remain unmerged on the milestone branch.

Experimental Path A/Path B branches may exist, but accepted production work must be integrated onto the primary milestone branch before final milestone acceptance/review/PR.

Do not change repository ownership/topology during an active milestone.

## Handoff input

Execution prep consults the latest cumulative handoff when one exists. It describes what actually became true at the last GREEN milestone and is a primary input to the next package.

## Routing outcome

Execution prep does **not** always generate a Codex start prompt. It ends with one outcome for the next executable Task Card.

### `EXECUTOR: CHATGPT`

Use when current normal ChatGPT chat has required capabilities, can run/satisfy required tests/checks and can obtain required evidence/readback.

ChatGPT may continue immediately on the prepared milestone branch. Recommend a fresh ChatGPT chat only for context hygiene when the current context is materially stale/noisy or at a clean boundary where fresh review/execution is beneficial.

### `EXECUTOR: CODEX`

Allowed only when `execution_policy: mixed` and at least one is true:
- Codex has a required capability/environment unavailable to ChatGPT;
- Codex has a material repo/runtime-heavy practical advantage;
- the approved plan/card explicitly assigns Codex.

Generate a short kickoff using `workflow/codex/HANDOFF.md`. The kickoff must identify the prepared milestone branch/durable pointer. Do not duplicate durable project context in chat.

### `EXECUTOR: BLOCKED`

Use when required capability/authorization/evidence path is unavailable under current policy. Under `chatgpt_only`, missing ChatGPT capability blocks; do not route to Codex or change policy.

## Required completion handoff to user

Execution prep is complete when durable prep artifacts are written and the response states:

```text
EXECUTION PREP COMPLETE:
Milestone: <MXX>
Milestone branch: <branch>
Task Card: <MXX-TYY>
Required prior checkpoint: <main-checkpoint>
Durable start pointer: <path>
Execution policy: <chatgpt_only|mixed>
Required capabilities: <explicit or inferred summary>
EXECUTOR: <CHATGPT|CODEX|BLOCKED>
```

If ChatGPT: state `CHATGPT SESSION RECOMMENDATION: CONTINUE CURRENT | FRESH` with brief context-hygiene reason and smallest user action only if fresh context is recommended.

If Codex: state `CODEX SESSION RECOMMENDATION: FRESH | CONTINUE EXISTING`, brief reason, copy-paste kickoff and smallest user action. At a clean new-milestone boundary after GREEN, prefer fresh Codex unless existing context materially helps and remains current.

If blocked: name the exact missing capability/authorization/evidence path.

A session recommendation is context hygiene, not product authorization.
