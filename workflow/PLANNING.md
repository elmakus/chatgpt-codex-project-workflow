# Planning

## Responsibility

ChatGPT is the strategic planner/project router for problem definition, verified baseline, requirements, architecture, global invariants, milestones and requirement coverage.

The eventual executor reconciles code/runtime-dependent implementation detail against actual current state through the Refresh Gate. Do not freeze detailed implementation design far in advance of the source/runtime it depends on.

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
- requirement coverage;
- dependencies;
- deployment/migration strategy;
- system verification strategy;
- idempotency/data-integrity/security constraints;
- fresh-context boundaries;
- Task Decomposition/OpenSpec/Handoff policy references.

The Master Plan is not the live task tracker. Live execution state belongs in `implementation/TASK_BOARD.yaml`.

## Milestones

A milestone is a stable, integrated, testable checkpoint, not a single small task. Define outcomes/acceptance without pretending distant implementation interfaces are already known.

## Requirement coverage

Every authoritative requirement must have:
- an owner milestone;
- at least one implementation Task Card before execution of that requirement;
- relevant OpenSpec when the behavior/API/schema/state/security/cross-package contract policy requires it.

## Pre-implementation planning audit

Before execution prep, perform an independent plan review when practical. Audit false assumptions, P0/P1 risks, milestone boundaries, task sizing, dependencies, missing acceptance/tests, requirement coverage, data integrity/idempotency/security, migration, OpenSpec boundaries and overengineering.

Resolve or explicitly defer material gaps.

## Competing research/prototype paths

When the project genuinely needs independent alternatives, use separate branches from the same stable checkpoint, e.g. Path A and Path B. Each path produces independent findings/evidence/prototype result. Later comparison leads to an accepted A/B/Hybrid decision before production implementation.

This pattern is optional. It does not add lifecycle states and experimental code is not merged merely because it exists.

## Distant work

Near-term cards may be detailed. Distant work stays functionally specific without freezing nonexistent interfaces. Every card whose details can drift before execution requires the Refresh Gate.
