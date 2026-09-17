# Execution Preparation

Execution preparation converts an approved plan into bounded executable contracts and Task Board state without prematurely freezing code-dependent detail.

## Preconditions

Before creating executable cards:
- authoritative requirements are identifiable;
- accepted architecture decisions are recorded;
- current Master Plan/milestone is approved;
- unresolved product questions that would invalidate implementation are resolved or explicitly blocking;
- project `execution_policy` is explicitly `chatgpt_only`, `codex_only` or `mixed`.

## State ownership

Execution prep writes:
- milestone/Card **contracts** under `implementation/milestones/` and `implementation/cards/`;
- all mutable readiness/status/executor/result/integration state to `implementation/TASK_BOARD.yaml`.

Do not put live execution state into milestone/Card files or `PROJECT.md`.

## Steps

1. Inspect current project repository and relevant source/runtime/external state.
2. Read current execution policy and Task Board when one exists.
3. Define/refresh milestone contract and branch policy.
4. Decompose work into bounded Task Card contracts.
5. Record dependencies, priority, complexity, phase and expected code locations in card contracts.
6. Define acceptance criteria and required tests/checks for every card.
7. Identify material external writes and required readback/verification evidence.
8. Add explicit `required_capabilities` only for unusual, external, high-risk or routing-significant work; ordinary repo capabilities remain inferred.
9. Classify independent review as REQUIRED/RECOMMENDED/OPTIONAL where material.
10. Mark OpenSpec candidates according to `workflow/contracts/OPENSPEC.md`; do not create distant specs merely for later.
11. Decide execution mode. Default to `serial`. Use `bounded_parallel` only when concrete cards have true dependency independence and bounded mutable ownership.
12. For each parallel candidate record `parallel_safe`, bounded `write_scope` and any `exclusive_resources` in the card contract/Task Board metadata as appropriate.
13. Set a conservative `parallel_card_limit` based on useful independent work, not theoretical platform capacity.
14. Initialize/update Task Board as the sole live execution-state record, including integration branch/base policy and parallel metadata.
15. Confirm requirement coverage.
16. Audit sizing, dependencies, side effects, idempotency, security, migration concerns, write-scope overlap, shared fixtures and external resource conflicts.
17. Set a Task Board card `ready` only when dependencies/prerequisites allow execution.
18. Determine executor from project policy as described below.

## Card versus OpenSpec task

A Task Card is a bounded global work package. An OpenSpec `tasks.md` item is a smaller implementation checkbox inside one change. They are not interchangeable.

## Executor selection

### `chatgpt_only`

Executor is fixed to ChatGPT. **Do not run Capability Gate.**

If execution prep already proves a required capability/evidence path is unavailable in the current ChatGPT session, keep/block the card appropriately and report the concrete blocker. Do not route to Codex or change policy.

### `codex_only`

Executor is fixed to Codex. **Do not run Capability Gate.**

ChatGPT may prepare the initial package and hand it to Codex. Once a Codex-only execution stream is active, Codex Main may perform just-in-time execution preparation for a subsequent already-approved milestone when the Master Plan fully determines its outcome/dependencies/acceptance and no new strategic decision is required.

Codex may refresh implementation details against actual state; it may not invent or revise product requirements/frozen architecture merely to continue. A missing required capability is a blocker, not a reason to fall back to ChatGPT.

### `mixed`

Normal ChatGPT runs `workflow/chatgpt/CAPABILITY_GATE.md` for the next executable card or compatible ready set.

The gate selects `EXECUTE IN CHATGPT`, `HANDOFF TO CODEX`, or `BLOCKED` based on actual current session capability plus material Codex practical advantage. Project routing assumes `ChatGPT capabilities ⊆ Codex capabilities`.

## Parallel preparation rules

Bounded parallelism is allowed only when it improves elapsed execution time without weakening ownership, review or integration evidence.

Do not split one causally coupled change into artificial cards merely to fill concurrency. Prefer parallel cards when they:
- consume the same already-accepted predecessor contract;
- own distinct mutable code/test/documentation surfaces;
- do not require one another's unfinished implementation details;
- can be tested meaningfully in isolation;
- can later be integrated with bounded cross-lane verification.

Project-global execution state remains coordinator-owned. Parallel workers do not independently edit Task Board or milestone-wide handoff/acceptance/integration bookkeeping.

For mutable project-level parallel cards, plan isolated lane branches/worktrees from one exact integration base. Read-only parallel work may share the same immutable repository snapshot.

## Git preparation

Follow `workflow/contracts/PROJECT_REPOSITORY.md#8-git-and-branch-policy` and `workflow/contracts/GITHUB_STATE.md`.

Large milestone implementation should use an isolated branch/PR when the project normally uses PRs. Do not change repository ownership/topology during an active milestone.

For bounded-parallel execution, the milestone/integration branch remains canonical assembly point. Each mutable lane starts from exact recorded integration base and is integrated back one lane at a time with required post-integration verification.

## Handoff input

Execution prep consults the latest cumulative handoff when one exists. It describes what actually became true at the last GREEN milestone and is a primary input to the next package.

## Multi-milestone continuation

A completed GREEN milestone may flow directly into execution preparation for the next already-approved milestone.

Under `chatgpt_only` or `codex_only`, the fixed executor continues without Capability Gate when no explicit strategic/user/deployment authorization gate intervenes. Under `mixed`, ChatGPT reruns Capability Gate for the next new assignment.

A fresh session may still be recommended for context hygiene; that is not an authorization gate.

## Required completion handoff to user

Execution prep is complete when durable contracts/Task Board state are written and the response states:

```text
EXECUTION PREP COMPLETE:
Milestone: <MXX>
Task Card(s): <MXX-TYY[, ...]>
Execution mode: <serial|bounded_parallel>
Parallel card limit: <N | n/a>
Required prior checkpoint: <checkpoint>
Durable start pointer: implementation/TASK_BOARD.yaml
Execution policy: <chatgpt_only|codex_only|mixed>
Routing: <POLICY_FIXED | CAPABILITY_GATE>
Executor: <CHATGPT|CODEX|BLOCKED>
Required capabilities: <explicit or inferred summary>
```

If ChatGPT executes: state `CHATGPT SESSION RECOMMENDATION: CONTINUE CURRENT | FRESH` when useful.

If Codex executes: give a short kickoff from `workflow/codex/HANDOFF.md`. Under `codex_only`, the kickoff may authorize deterministic continuation across the already-approved milestone sequence until a real stop condition occurs.

If blocked: name the exact missing capability/authorization/evidence path.
