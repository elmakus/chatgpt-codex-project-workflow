# Planning

## Responsibility

The **strategic-planning role** owns problem definition, verified baseline, requirements, architecture, global invariants, milestone outcomes and requirement coverage. Project Workflow does not bind this role to a specific model. Normal ChatGPT commonly performs it, but the role definition remains model-agnostic.

The eventual execution orchestrator/executor reconciles code/runtime-dependent implementation detail against actual current state through the Refresh Gate. Do not freeze detailed implementation design far in advance of the source/runtime it depends on.

Under `codex_only`, an already-approved Master Plan may later be executed continuously by Codex; this does not transfer strategic authority to Codex to invent or revise requirements/architecture.

## Inputs

Use project `PROJECT.md`, canonical requirements, relevant verified research, accepted decisions and current project/source baseline where needed.

## Master Plan

The approved Master Plan normally lives at `planning/MASTER_PLAN.md` and covers as applicable:
- problem/goal;
- current state / verified baseline;
- target state;
- authoritative requirements;
- frozen architecture decisions;
- non-goals;
- global invariants/external constraints;
- known source seams;
- milestones and checkpoint/acceptance for each;
- milestone dependencies and explicit user/authorization gates;
- requirement coverage;
- deployment/migration strategy;
- system verification strategy;
- idempotency/data-integrity/security constraints;
- fresh-context boundaries;
- Task Decomposition/OpenSpec/Handoff policy references.

The Master Plan is not the live task tracker. Live execution state belongs only in `implementation/TASK_BOARD.yaml`.

An approved Master Plan milestone section is the **default milestone contract**. Do not create a separate milestone file merely to restate the same outcome, dependencies, constraints and acceptance. Create `implementation/milestones/MXX.md` just-in-time only when execution preparation needs material contract detail that the approved plan does not already carry.

## Milestones

A milestone is a stable, integrated, testable checkpoint, not a single small task. Define outcomes/acceptance without pretending distant implementation interfaces are already known.

Planner quality must survive execution decomposition. Keep material rationale, invariants, failure semantics, rejected-path constraints and other implementation-shaping intent in durable authority. Later Task Cards may narrow context, but must not replace that authority with a lossy summary.

An approved sequence of milestones is permission to execute that approved scope under the project's execution policy; it is not permission to bypass any explicit deployment/live-write/user authorization gate recorded by the plan or requirements.

Under fixed execution policy (`chatgpt_only` or `codex_only`), GREEN milestone boundaries may be crossed automatically when the next milestone is already approved and no strategic/authorization gate intervenes. The boundary still requires fresh execution preparation/Refresh Gate as applicable.

## Deferred decomposition and delegated planning authority

Planning should freeze only what is knowable and strategically important.

A future milestone may remain intentionally less detailed when correct implementation decomposition depends materially on predecessor results. It must still define enough stable authority to prevent downstream invention:
- outcome / state that must become true;
- requirement ownership;
- dependencies;
- applicable global/milestone invariants and accepted decisions;
- outcome-level acceptance that is already knowable;
- explicit user/deployment/authorization gates;
- the durable evidence/JIT trigger after which deferred detail can be completed.

Do **not** invent downstream Task Cards merely to make the plan look complete. When a real card's scope, number, ordering or technical acceptance depends on predecessor evidence, defer that decomposition.

The execution orchestrator/JIT planner is delegated authority to complete that deferred execution detail from durable predecessor evidence **without returning to the original planner**, provided it stays within accepted strategic authority.

Decision classes:

- **L1 — execution detail:** implementation choices inside an accepted Task Card/milestone contract. Executor/orchestrator decides and records material results normally.
- **L2 — JIT decomposition/refinement:** create/split/merge/reorder/replace not-yet-started cards; complete optional milestone execution detail; refine technical tests/acceptance/interfaces from predecessor evidence. Execution orchestrator decides and persists the updated contracts/Task Board.
- **L3 — strategic replan:** any change to requirements, accepted/frozen architecture or decisions, global invariants, milestone outcome, product/external behavior contract, or explicit authorization boundary. Return to the strategic-planning/user decision path.

Deferred decomposition must never be used to hide an already-known unresolved L3 decision. If the uncertainty is strategic now, record it as unresolved/blocking now.

The strategic-planning role does not need to be performed again at every milestone. A project may execute an entire approved multi-milestone plan through L1/L2 refinement without strategic replanning when predecessor evidence remains compatible with accepted authority.

## Requirement coverage

Every authoritative requirement must have:
- an owner milestone;
- at least one implementation Task Card **before execution of that requirement**, not necessarily at initial Master Plan approval;
- relevant OpenSpec when the behavior/API/schema/state/security/cross-package contract policy requires it.

The coverage matrix may therefore identify a JIT decomposition trigger instead of speculative future Card IDs when the real cards cannot yet be defined responsibly.

## Pre-implementation planning audit

Before execution prep, perform an independent plan review when practical. Audit false assumptions, P0/P1 risks, milestone boundaries, task sizing, dependencies, missing acceptance/tests, requirement coverage, data integrity/idempotency/security, migration, OpenSpec boundaries and overengineering.

Resolve or explicitly defer material gaps.

## Competing research/prototype paths

When the project genuinely needs independent alternatives, use separate branches from the same stable checkpoint, e.g. Path A and Path B. Each path produces independent findings/evidence/prototype result. Later comparison leads to an accepted A/B/Hybrid decision before production implementation.

This pattern is optional. It does not add lifecycle states and experimental code is not merged merely because it exists.

## Distant work

Near-term cards may be detailed. Distant work stays functionally specific without freezing nonexistent interfaces. Every card whose details can drift before execution requires the Refresh Gate.
