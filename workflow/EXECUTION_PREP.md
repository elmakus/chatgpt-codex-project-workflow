# Execution Preparation

Execution preparation converts an approved plan into a bounded execution package without prematurely freezing code-dependent detail.

## Preconditions

Before creating executable cards:
- authoritative requirements are identifiable;
- accepted architecture decisions are recorded;
- current Master Plan/milestone is approved;
- unresolved product questions that would invalidate implementation are resolved or explicitly blocking;
- project `execution_policy` is explicitly `chatgpt_only` or `mixed`.

## Steps

1. Inspect current project repository and relevant source/runtime state.
2. Define/refresh milestone file and branch policy.
3. Decompose work into bounded Task Cards under `implementation/cards/`.
4. Record dependencies, priority, complexity, phase and expected code locations.
5. Define acceptance criteria and required tests/checks for every card.
6. Identify material external writes and required readback/verification evidence.
7. Add explicit `required_capabilities` only for unusual, external, high-risk or routing-significant work; ordinary repo capabilities remain inferred.
8. Classify independent review as REQUIRED/RECOMMENDED/OPTIONAL where material.
9. Mark OpenSpec candidates according to `workflow/contracts/OPENSPEC.md`; do not create distant specs merely for later.
10. Decide execution mode. Default to `serial`. Use `bounded_parallel` only when concrete cards have true dependency independence and bounded mutable ownership.
11. For each parallel candidate record `parallel_safe`, bounded `write_scope` and any `exclusive_resources`. Keep a card serial when ownership or external side effects cannot be isolated confidently.
12. Set a conservative `parallel_card_limit` based on useful independent work, not theoretical platform capacity. The limit is a ceiling, not a target.
13. Initialize/update `implementation/TASK_BOARD.yaml`, including integration branch/base policy and parallel metadata when used.
14. Confirm requirement coverage.
15. Audit sizing, dependencies, side effects, idempotency, security, migration concerns, write-scope overlap, shared fixtures and external resource conflicts.
16. Set a card `ready` only when dependencies/prerequisites allow execution. Scheduling capacity/conflicts do not change readiness.
17. For the next executable card or compatible ready set, run `workflow/chatgpt/CAPABILITY_GATE.md` for executor routing. A bounded-parallel set may be routed to Codex when Codex has a material repo/runtime orchestration advantage.

## Card versus OpenSpec task

A Task Card is a bounded global work package. An OpenSpec `tasks.md` item is a smaller implementation checkbox inside one change. They are not interchangeable.

## Parallel preparation rules

Bounded parallelism is allowed only when it improves elapsed execution time without weakening ownership, review or integration evidence.

Do not split one causally coupled change into artificial cards merely to fill concurrency. Prefer parallel cards when they:
- consume the same already-accepted predecessor contract;
- own distinct mutable code/test/documentation surfaces;
- do not require one another's unfinished implementation details;
- can be tested meaningfully in isolation;
- can later be integrated with bounded cross-lane verification.

Project-global execution state remains coordinator-owned. Parallel workers do not independently edit the Task Board, milestone-wide handoff/acceptance state or shared integration bookkeeping.

For mutable project-level parallel cards, plan isolated lane branches/worktrees from one exact integration base. Read-only parallel work may share the same repository snapshot when no mutable workspace/index is shared.

## Git preparation

Follow `workflow/contracts/PROJECT_REPOSITORY.md#8-git-and-branch-policy` and `workflow/contracts/GITHUB_STATE.md`.

Large milestone implementation should use an isolated branch/PR when the project normally uses PRs. Do not change repository ownership/topology during an active milestone.

For bounded-parallel execution, the milestone/integration branch remains the canonical assembly point. Each mutable lane starts from the exact recorded integration base and is integrated back one lane at a time with required post-integration verification.

## Handoff input

Execution prep consults the latest cumulative handoff when one exists. It describes what actually became true at the last GREEN milestone and is a primary input to the next package.

## Routing outcome

Execution prep does **not** always generate a Codex start prompt. It ends with one outcome for the next executable Task Card or compatible ready set.

### `EXECUTOR: CHATGPT`

Use when current normal ChatGPT chat has required capabilities, can run/satisfy required tests/checks and can obtain required evidence/readback.

ChatGPT may continue immediately. Recommend a fresh ChatGPT chat only for context hygiene when the current context is materially stale/noisy or at a clean boundary where fresh review/execution is beneficial.

### `EXECUTOR: CODEX`

Allowed only when `execution_policy: mixed` and at least one is true:
- Codex has a required capability/environment unavailable to ChatGPT;
- Codex has a material repo/runtime-heavy practical advantage;
- bounded-parallel repo execution materially benefits from Codex orchestration;
- the approved plan/card explicitly assigns Codex.

Generate a short kickoff using `workflow/codex/HANDOFF.md`. Do not duplicate durable project context in chat. When a compatible ready set is being handed off, name the set and durable Task Board pointer; Codex Main remains responsible for project-level coordination and integration.

### `EXECUTOR: BLOCKED`

Use when required capability/authorization/evidence path is unavailable under current policy. Under `chatgpt_only`, missing ChatGPT capability blocks; do not route to Codex or change policy.

## Required completion handoff to user

Execution prep is complete when durable prep artifacts are written and the response states:

```text
EXECUTION PREP COMPLETE:
Milestone: <MXX>
Task Card(s): <MXX-TYY[, ...]>
Execution mode: <serial|bounded_parallel>
Parallel card limit: <N | n/a>
Required prior checkpoint: <checkpoint>
Durable start pointer: <path>
Execution policy: <chatgpt_only|mixed>
Required capabilities: <explicit or inferred summary>
EXECUTOR: <CHATGPT|CODEX|BLOCKED>
```

If ChatGPT: state `CHATGPT SESSION RECOMMENDATION: CONTINUE CURRENT | FRESH` with brief context-hygiene reason and smallest user action only if fresh context is recommended.

If Codex: state `CODEX SESSION RECOMMENDATION: FRESH | CONTINUE EXISTING`, brief reason, copy-paste kickoff and smallest user action. At a clean new-milestone boundary after GREEN, prefer fresh Codex unless existing context materially helps and remains current.

If blocked: name the exact missing capability/authorization/evidence path.

A session recommendation is context hygiene, not product authorization.
