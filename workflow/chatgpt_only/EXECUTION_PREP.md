# ChatGPT-only Execution Preparation

Execution preparation turns approved milestone authority, or a qualified branch-isolated micro-fix intake, into bounded executable Cards and Task Board state.

## Preconditions

Before creating executable work:
- applicable accepted product/behavior authority is identifiable; for a qualified micro-fix this may be the exact completed Intake intent/diagnostic record plus existing requirements/decisions, without requiring a new formal requirements artifact;
- accepted architecture/decisions are recorded;
- either the current Master Plan/milestone is approved, or a selected branch-isolated issue Intake has completed with `path: micro_fix` and durable evidence for every R6 qualification criterion;
- unresolved strategic questions are resolved or explicitly blocking;
- project is routed here under `execution_policy: chatgpt_only`.

## State ownership

Execution prep writes:
- Task Card contracts only in the selected branch-isolated workstream's manifest-bound cards location/conventional `implementation/workstreams/<id>/cards/`; historical root/default Card files are recovery/migration input and do not receive new active contracts;
- optional JIT milestone extension only when it adds material detail beyond the approved Master Plan milestone section; qualified micro-fixes do not create one merely to imitate milestone shape;
- mutable readiness/status/result/review state only to the **selected canonical Task Board** resolved by `workflow/chatgpt_only/WORKSTREAMS.md`.

When creating the first Task Board for active managed work, a validated branch-isolated workstream MUST already be selected. Scaffold only the exact manifest-selected path from `workflow/chatgpt_only/WORKSTREAM_TASK_BOARD_TEMPLATE.yaml`, then persist the manifest `task_board` pointer and exact binding identity. Root `implementation/TASK_BOARD.yaml` and `workflow/chatgpt_only/TASK_BOARD_TEMPLATE.yaml` are historical recovery/migration surfaces only and MUST NOT be scaffolded or selected for new/continued managed work. Do **not** use the shared `templates/TASK_BOARD.yaml`, which belongs to the legacy/other-policy stack and may contain bounded-parallel coordination fields that are illegal in active `chatgpt_only`.

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

1. ensure an exact validated branch-isolated workstream is selected and its manifest-bound Task Board exists; if this is first preparation for that workstream, initialize only `WORKSTREAM_TASK_BOARD_TEMPLATE.yaml` without inventing speculative placeholder Cards;
2. create one exact Research record under `workflow/chatgpt_only/RESEARCH.md#Durable record contract`, with `Origin role: execution_prep`, the exact current milestone/preparation obligation as Origin subject, `Return target: execution_resolution:<same exact subject>`, and `Return reconciliation: pending`;
3. persist the Research record and Task Board `research_obligation` in the same durable transition before yielding;
4. preserve all already-valid preparation/Card state; do not mark unrelated work ready merely to create the handoff;
5. return to the router for Research.

When Research completes, `execution_resolution` classifies the findings. It either keeps the completed record pointed while naming an exact final Return target, or, if classification itself still needs evidence, atomically consumes that record and switches the pointer to one exact next active Research record under the classifier-to-Research chain protocol. A fresh session must therefore recover Research, the classifier, the chained Research obligation, or the final owner without transcript inference.

## Qualified micro-fix preparation

When the selected branch-isolated issue workstream has completed Intake with `path: micro_fix` and exact `next_route: execution_prep:micro_fix`:

1. read `workflow/chatgpt_only/MICRO_FIX.md`, the selected manifest and exact completed Intake record;
2. verify the Intake record proves every accepted R6 criterion; if any criterion is false or materially uncertain, do not force micro-fix—return to the router for the smallest normal Research / Project Definition / Strategic Planning / Execution Prep route supported by evidence;
3. create/reconcile exactly one bounded fix Card contract from the Intake scope/diagnostic evidence and applicable accepted authority;
4. create/reconcile the manifest-selected workstream Task Board with exact binding identity, `plan_revision: micro-fix`, `current_milestone: micro-fix`, empty `milestones`, and that one fix Card;
5. set manifest `task_board` to the exact board path and set the distinct workstream final-integration review requirement to at least `RECOMMENDED` for behavioral/code/runtime-configuration work, or `REQUIRED` when existing risk authority requires it;
6. do not invent a Master Plan, milestone contract or milestone lifecycle solely for the micro-fix;
7. set the one eligible fix Card `ready` when its direct acceptance/tests are executable, then return to the router for normal selected-workstream Execution.

After materialization, the selected Task Board is the sole mutable Card/review/Research state exactly as for any other workstream.

## Preparation steps

1. Inspect current project/source/runtime/external state needed by the milestone.
2. Resolve the exact branch-isolated workstream through `workflow/chatgpt_only/WORKSTREAMS.md`, validate manifest ↔ Task Board binding, then read only that selected workstream Task Board when implementation state exists. Historical root/default state must first complete Recovery migration and is never selected here as an active context.
3. Resolve the current milestone contract from the approved Master Plan, or for a qualified micro-fix resolve the completed Intake + bounded fix authority under `MICRO_FIX.md` without requiring a Master Plan/milestone contract.
4. Create a separate JIT milestone extension only when material execution/acceptance detail is missing.
5. Decompose only work that is deterministic enough to contract now.
6. If later Card scope depends materially on predecessor evidence, persist a JIT trigger instead of creating a placeholder.
7. For each Card record exact authority refs and every must-preserve implementation-shaping constraint.
8. Define bounded included/excluded scope.
9. Define acceptance and required tests/checks.
10. Identify material external writes plus required persisted-state verification.
11. Classify Card/milestone independent review when material. Separately, for a selected intake-created `issue | feature` workstream that changes code, runtime configuration, external behavior or system behavior, ensure manifest `review.requirement` is at least `RECOMMENDED` (or `REQUIRED` under existing high-risk authority); leave its workstream-level `state/subject/evidence` unactivated until an exact final/integrated subject exists or exact stronger-review coverage is proven.
12. Mark OpenSpec candidates using `workflow/common/OPENSPEC.md`.
13. Initialize/reconcile the selected manifest-bound workstream Task Board as the sole live Card/milestone execution state for this managed workstream.
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

Read the latest applicable cumulative handoff from the selected workstream Task Board only when it materially supplies predecessor truth needed by current preparation. A historical `PROJECT.md -> Latest cumulative handoff` or root `project-handoffs/` record may be read only as Recovery migration input and never becomes active workstream state; migrate only the exact predecessor truth needed for continuation.

## Automatic transition into execution

When preparation leaves an unblocked READY Card and no real user/authorization/strategic gate intervenes, **do not end the user turn merely to report preparation**.

The execution-preparation role is complete. Persist its durable state, return to `workflow/chatgpt_only/ROUTER.md`, and let the router select the execution route from the new Task Board state. Continue in the same chat.

A fresh session may be recommended for context hygiene at a clean boundary, but that recommendation is not an execution gate.

If the later execution role implements a subject requiring/recommending independent review, the execution route owns that fresh-review boundary.
