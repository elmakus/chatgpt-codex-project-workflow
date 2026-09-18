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
- Task Card **contracts** under `implementation/cards/`;
- an optional milestone contract under `implementation/milestones/` only when it adds material execution/acceptance detail beyond the approved Master Plan milestone section;
- all mutable readiness/status/executor/result/integration/review state to `implementation/TASK_BOARD.yaml`.

The approved Master Plan milestone section is the default milestone contract. Do not create a second milestone document merely to duplicate it.

Do not put live execution state into milestone/Card files or `PROJECT.md`.

## Steps

1. Inspect current project repository and relevant source/runtime/external state.
2. Read current execution policy and Task Board when one exists.
3. Resolve the milestone contract from the approved Master Plan. Create/refresh a separate milestone file only when just-in-time preparation needs material detail not already present there; record branch policy where applicable.
4. Decompose only the work that is deterministic enough to contract now. If later card scope materially depends on predecessor evidence, persist the dependency/JIT trigger and defer those cards instead of creating placeholders.
5. For each card record dependencies plus an exact authority slice: applicable requirement/decision/plan/milestone/dependency-result references and every must-preserve constraint that could change implementation or acceptance. Priority, complexity, phase and expected code locations are optional execution hints, not mandatory boilerplate.
6. Define acceptance criteria and required tests/checks for every card.
7. Identify material external writes and required readback/verification evidence.
8. Add explicit `required_capabilities` only when they materially improve **mixed-policy routing** or document unusual external/security/user-authorization prerequisites. Do not turn this metadata into a fixed-policy capability preflight.
9. Classify independent review as REQUIRED/RECOMMENDED/OPTIONAL where material.
10. Mark OpenSpec candidates according to `workflow/contracts/OPENSPEC.md`; do not create distant specs merely for later.
11. Decide execution mode. Default to `serial`. Use `bounded_parallel` only when concrete cards have true dependency independence and bounded mutable ownership.
12. For each parallel candidate record `parallel_safe`, bounded `write_scope` and any `exclusive_resources` in the card contract/Task Board metadata as appropriate.
13. Set a conservative `parallel_card_limit` based on useful independent work, not theoretical platform capacity.
14. Initialize/update Task Board as the sole live execution-state record, including integration branch/base policy, parallel metadata and review-state fields when a review gate becomes active.
15. Confirm requirement coverage, allowing future requirements to point to a durable JIT decomposition trigger when their implementation cards are not yet responsibly knowable.
16. Audit sizing, dependencies, side effects, idempotency, security, migration concerns, write-scope overlap, shared fixtures and external resource conflicts.
17. Set a Task Board card `ready` only when dependencies/prerequisites allow execution and no known strategic/authorization blocker prevents starting.
18. Determine executor from project policy as described below.

Execution preparation under fixed policy does **not** ask whether the fixed executor can theoretically perform every future operation. Actual capability failure is handled at runtime when a concrete operation is attempted.

## Incremental execution preparation

Execution Prep is incremental. It does not require every Task Card in the current or future milestone to exist before the first deterministic card starts.

The execution orchestrator/JIT planner may create or revise **not-yet-started** cards after predecessor cards/milestones produce durable evidence. It may also create/complete an optional JIT milestone extension when the Master Plan intentionally deferred implementation-level detail.

This is allowed without strategic replanning when all changes remain inside:
- accepted requirements;
- accepted/frozen architecture and decisions;
- global/milestone invariants;
- approved milestone outcome;
- explicit boundary/authorization gates.

The orchestrator may change card count/order, split/merge cards, refine technical scope, tests and implementation-level acceptance, and bind newly known dependency-result authority.

It may not reinterpret a strategic ambiguity as implementation freedom. Evidence requiring a change to the bounded strategic authority above is an L3 strategic replan/blocker.

Do not create “future placeholder cards” with unknowable scope. A Task Board may contain only the cards currently contractible plus milestone/plan references that state the JIT trigger for later decomposition.

## Authority preservation during decomposition

Execution preparation may reduce context volume but must not reduce applicable authoritative constraints.

For every Task Card:
- identify exact durable authority references at the smallest practical section/ID granularity;
- carry forward every invariant, accepted behavior/architecture choice, failure semantic, compatibility rule, external-write boundary, dependency result and exclusion that can materially change implementation or acceptance;
- preserve rationale when omitting it could make a competent downstream executor reasonably choose a different path than the approved one;
- prefer exact authority references over paraphrase; summaries are navigation aids and never override the referenced authority;
- if a downstream executor/reviewer will not read a referenced artifact directly, its execution/review package must explicitly carry the applicable constraints without changing their meaning.

This is **lossless by authority, selective by context**: fewer documents and smaller worker packages are allowed; semantic compression of accepted intent is not.

## Evidence granularity

A simple Task Card does not require a standalone evidence file merely because it completed. `tests_summary` plus exact result pointers in Task Board may be sufficient when the result is straightforward and reproducible.

Create standalone durable evidence when materially useful or required, including:
- milestone integrated acceptance;
- REQUIRED/RECOMMENDED independent review;
- baseline/authorized exceptions;
- material external writes/readback/reconciliation;
- complex or multi-stage verification whose proof cannot be represented safely by a concise Task Board summary;
- an explicit contract requirement.

When no standalone evidence artifact is required, keep `evidence: null` and record a concise exact `tests_summary`.

## Card versus OpenSpec task

A Task Card is a bounded global work package. An OpenSpec `tasks.md` item is a smaller implementation checkbox inside one change. They are not interchangeable.

## Executor selection

### `chatgpt_only`

Executor is fixed to ChatGPT. **Do not run Capability Gate or capability preflight/inventory.**

Prepare the card, assign ChatGPT in Task Board and start execution. Project Workflow does not prescribe ChatGPT's tool inventory. If a concrete required operation later cannot be performed with the actual runtime, persist a runtime blocker and ask only for the smallest user-provided input/access/authorization actually required. The user may instead explicitly change execution policy, after which Task Board is reconciled before reassignment.

### `codex_only`

Executor is fixed to Codex. **Do not run Capability Gate or capability preflight/inventory.**

ChatGPT may prepare the initial package and hand it to Codex. Once a Codex-only execution stream is active, the execution orchestrator may perform just-in-time execution preparation both **within the active milestone** and for a subsequent already-approved milestone when durable authority plus predecessor evidence determine the required L1/L2 refinement and no new strategic decision is required.

Codex may refresh implementation details against actual state; it may not invent or revise product requirements/frozen architecture merely to continue. Project Workflow does not prescribe Codex's tool inventory. Ordinary executor-local remediation is runtime implementation detail when permitted; a blocker exists only when a concrete required operation still cannot proceed and needs user-provided input/access/authorization.

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
