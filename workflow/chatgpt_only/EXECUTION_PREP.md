# ChatGPT-only Execution Preparation

Execution preparation turns approved milestone authority into bounded executable Cards and Task Board state.

## Preconditions

Before creating executable work:
- authoritative requirements are identifiable;
- accepted architecture/decisions are recorded;
- current Master Plan/milestone is approved;
- unresolved strategic questions are resolved or explicitly blocking;
- project is routed here under `execution_policy: chatgpt_only`.

## State ownership

Execution prep writes:
- Task Card contracts under `implementation/cards/`;
- optional JIT milestone extension only when it adds material detail beyond the approved Master Plan milestone section;
- mutable readiness/status/result/review state only to `implementation/TASK_BOARD.yaml`.

Do not mirror live state into Card/milestone/`PROJECT.md`.

## Preparation steps

1. Inspect current project/source/runtime/external state needed by the milestone.
2. Read Task Board when implementation state exists.
3. Resolve current milestone contract from the approved Master Plan.
4. Create a separate JIT milestone extension only when material execution/acceptance detail is missing.
5. Decompose only work that is deterministic enough to contract now.
6. If later Card scope depends materially on predecessor evidence, persist a JIT trigger instead of creating a placeholder.
7. For each Card record exact authority refs and every must-preserve implementation-shaping constraint.
8. Define bounded included/excluded scope.
9. Define acceptance and required tests/checks.
10. Identify material external writes plus required persisted-state verification.
11. Classify independent review when material.
12. Mark OpenSpec candidates using `workflow/common/OPENSPEC.md`.
13. Initialize/reconcile Task Board as sole live execution state.
14. Confirm requirement coverage, allowing future requirements to point to a durable JIT trigger.
15. Audit sizing, dependencies, side effects, idempotency, security, migration and explicit authorization gates.
16. Set exactly the next eligible Card `ready` when dependencies/prerequisites allow execution.

ChatGPT is the fixed executor. Do not run an executor-selection or capability-inventory step.

## Incremental JIT preparation

Execution preparation is incremental.

After durable predecessor evidence exists, ChatGPT may create/revise **not-yet-started** Cards when all changes remain inside:
- accepted requirements;
- accepted/frozen architecture/decisions;
- global/milestone invariants;
- approved milestone outcome;
- explicit authorization boundaries.

Allowed L2 refinement includes:
- change Card count/order;
- split/merge Cards;
- refine technical scope/interfaces;
- refine tests/implementation-level acceptance;
- bind exact dependency-result authority;
- complete a JIT milestone extension.

Evidence requiring a change to strategic authority is L3 and stops affected execution for strategic resolution.

## Authority preservation

Every Card must:
- identify exact durable authority refs;
- preserve applicable invariants, accepted behavior/architecture, failure semantics, compatibility rules, external-write boundaries, dependency results and exclusions;
- preserve material rationale when omitting it could cause a different implementation choice.

Exact authority outranks summaries.

## Evidence granularity

A simple reproducible Card may close with Task Board result pointers + concise exact `tests_summary`.

Create standalone evidence when materially useful/required, especially for:
- integrated milestone acceptance;
- REQUIRED/RECOMMENDED independent review;
- baseline/authorized exceptions;
- material external writes/readback;
- complex multi-stage verification;
- explicit contract requirements.

## Git preparation

Use `workflow/chatgpt_only/REPOSITORY.md`.

Substantial milestone implementation should use an isolated branch/PR when project practice does so.

Do not change project topology during active milestone work.

## Prior handoff

Read the latest cumulative handoff only when it materially supplies predecessor truth needed by current preparation.

## Automatic transition into execution

When preparation leaves an unblocked READY Card and no real user/authorization/strategic gate intervenes, **do not end the user turn merely to report preparation**.

Load `workflow/chatgpt_only/EXECUTION.md` + `STATE.md` and start the Card immediately.

A fresh session may be recommended for context hygiene at a clean boundary, but that recommendation is not an execution gate.

When current chat later implements a subject requiring/recommending independent review, stop only at the required fresh-review boundary defined in `REVIEW.md`.
