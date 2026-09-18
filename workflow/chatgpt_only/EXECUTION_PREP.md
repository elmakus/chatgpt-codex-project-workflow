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

When creating the first Task Board for this policy, scaffold it from `workflow/chatgpt_only/TASK_BOARD_TEMPLATE.yaml`. Do **not** use the shared `templates/TASK_BOARD.yaml`, which belongs to the legacy/other-policy stack and may contain bounded-parallel coordination fields that are illegal in active `chatgpt_only`.

Do not mirror live state into Card/milestone/`PROJECT.md`.

## Completed Research return into Execution Prep

When Task Board `research_obligation` points to `Status: complete` with exact `Return target: execution_prep:<subject>` for the current preparation obligation, Execution Prep is the final owning Return target.

- verify the pointer plus Origin/Return subjects against current durable Card/milestone state;
- read `Return reconciliation` before editing; if it is `applied`, verify the exact result refs, perform only consume/clear, return to the router, and do not reshape Cards;
- recover whether the intended L2/JIT preparation reconciliation is already durably present before editing;
- perform only missing preparation/reconciliation work; never recreate or reshuffle already-reconciled Cards merely because the Research pointer survived a crash;
- follow `workflow/chatgpt_only/RESEARCH.md#Final Return-target protocol`;
- persist the resulting Card contracts/Task Board reconciliation and `Return reconciliation: applied` + exact result refs in the same durable Git transition;
- only after that applied transition is durable, set the Research record to `Status: consumed` and clear Task Board `research_obligation`;
- if a crash leaves `Return reconciliation: applied` while the record is still `complete` and pointed, re-entry performs only the missing consume/clear transition and then returns to the router.

If the Research record is `active | blocked`, or it is `complete` for a different Return target, do not continue preparation; return to the router.

## Execution Prep → Research handoff

When Execution Prep needs more evidence before it can legally classify or complete L2/JIT preparation:

1. ensure a Task Board exists; if this is first preparation, initialize a minimal board conforming to `workflow/chatgpt_only/TASK_BOARD_TEMPLATE.yaml` without inventing speculative placeholder Cards;
2. create one exact Research record under `workflow/chatgpt_only/RESEARCH.md#Durable record contract`, with `Origin role: execution_prep`, the exact current milestone/preparation obligation as Origin subject, `Return target: execution_resolution:<same exact subject>`, and `Return reconciliation: pending`;
3. persist the Research record and Task Board `research_obligation` in the same durable transition before yielding;
4. preserve all already-valid preparation/Card state; do not mark unrelated work ready merely to create the handoff;
5. return to the router for Research.

When Research completes, `execution_resolution` classifies the findings and keeps the Task Board pointer until an exact final Return target consumes them. A fresh session must therefore recover either Research, the classifier, or the final owner without transcript inference.

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

Evidence requiring authority above delegated L1/L2 stops affected execution and returns to the router for strategic classification: Definition when accepted product/system authority must change, Planning when the accepted Definition remains valid but milestone/plan strategy must change, or Research when more evidence is required first.

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

The execution-preparation role is complete. Persist its durable state, return to `workflow/chatgpt_only/ROUTER.md`, and let the router select the execution route from the new Task Board state. Continue in the same chat.

A fresh session may be recommended for context hygiene at a clean boundary, but that recommendation is not an execution gate.

If the later execution role implements a subject requiring/recommending independent review, the execution route owns that fresh-review boundary.
