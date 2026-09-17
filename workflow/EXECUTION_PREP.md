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
- all mutable readiness/status/executor/result/integration/review state to `implementation/TASK_BOARD.yaml`.

Do not put live execution state into milestone/Card files or `PROJECT.md`.

## Steps

1. Inspect current project repository and relevant source/runtime/external state.
2. Read current execution policy and Task Board when one exists.
3. Define/refresh milestone contract and branch policy.
4. Decompose work into bounded Task Card contracts.
5. Record dependencies, priority, complexity, phase and expected code locations in card contracts.
6. Define acceptance criteria and required tests/checks for every card.
7. Identify material external writes and required readback/verification evidence.
8. Add explicit `required_capabilities` only when they materially improve **mixed-policy routing** or document unusual external/security/user-authorization prerequisites. Do not turn this metadata into a fixed-policy capability preflight.
9. Classify independent review as REQUIRED/RECOMMENDED/OPTIONAL where material.
10. Mark OpenSpec candidates according to `workflow/contracts/OPENSPEC.md`; do not create distant specs merely for later.
11. Decide execution mode. Default to `serial`. Use `bounded_parallel` only when concrete cards have true dependency independence and bounded mutable ownership.
12. For each parallel candidate record `parallel_safe`, bounded `write_scope` and any `exclusive_resources` in the card contract/Task Board metadata as appropriate.
13. Set a conservative `parallel_card_limit` based on useful independent work, not theoretical platform capacity.
14. Initialize/update Task Board as the sole live execution-state record, including integration branch/base policy, parallel metadata and review-state fields when a review gate becomes active.
15. Confirm requirement coverage.
16. Audit sizing, dependencies, side effects, idempotency, security, migration concerns, write-scope overlap, shared fixtures and external resource conflicts.
17. Set a Task Board card `ready` only when dependencies/prerequisites allow execution and no known strategic/authorization blocker prevents starting.
18. Determine executor from project policy as described below.

Execution preparation under fixed policy does **not** ask whether the fixed executor can theoretically perform every future operation. Actual capability failure is handled at runtime when a concrete operation is attempted.

## Card versus OpenSpec task

A Task Card is a bounded global work package. An OpenSpec `tasks.md` item is a smaller implementation checkbox inside one change. They are not interchangeable.

## Executor selection

### `chatgpt_only`

Executor is fixed to ChatGPT. **Do not run Capability Gate or capability preflight/inventory.**

Prepare the card, assign ChatGPT in Task Board and start execution. If a concrete required operation later cannot be performed with current ChatGPT tools/plugins/connectors, persist a runtime blocker and ask for the smallest remedy. The user may instead explicitly change execution policy, after which Task Board is reconciled before reassignment.

### `codex_only`

Executor is fixed to Codex. **Do not run Capability Gate or capability preflight/inventory.**

ChatGPT may prepare the initial package and hand it to Codex. Once a Codex-only execution stream is active, Codex Main may perform just-in-time execution preparation for a subsequent already-approved milestone when the Master Plan fully determines its outcome/dependencies/acceptance and no new strategic decision is required.

Codex may refresh implementation details against actual state; it may not invent or revise product requirements/frozen architecture merely to continue. Ordinary installable local tooling/dependency gaps are runtime implementation detail when Codex can safely self-remediate them. User-provided MCP/credential/token/access becomes a blocker only when concretely needed and unavailable.

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

Under `chatgpt_only` or `codex_only`, the fixed executor continues without Capability Gate/capability preflight when no explicit strategic/user/deployment authorization gate intervenes and every required/recommended review gate for the completed subject is GREEN. Under `mixed`, ChatGPT reruns Capability Gate for the next new assignment.

A fresh session may still be recommended for context hygiene. Under `chatgpt_only`, a fresh chat is **mandatory** when the current implementing chat reaches a REQUIRED/RECOMMENDED independent-review boundary.

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
Capability preflight: <NOT RUN (fixed policy) | MIXED GATE RESULT>
```

If ChatGPT executes: state `CHATGPT SESSION RECOMMENDATION: CONTINUE CURRENT | FRESH` only when useful for context hygiene. Independent-review handoff uses the stronger mandatory `USER ACTION REQUIRED` wording from `workflow/REVIEW_AND_HANDOFF.md`.

If Codex executes: give a short kickoff from `workflow/codex/HANDOFF.md`. Under `codex_only`, the kickoff may authorize deterministic continuation across the already-approved milestone sequence until a real stop condition occurs.

If a real blocker already exists independent of capability speculation (for example unresolved strategy or explicit authorization), name it precisely.
