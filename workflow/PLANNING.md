# Planning

## Responsibility

ChatGPT is the strategic planner for problem definition, verified baseline, requirements, architecture, global invariants, milestones and requirement coverage. Codex owns implementation details that must be reconciled against actual current code.

Do not freeze detailed code-dependent design far in advance of the code it depends on.

## Inputs

Use:
- project `PROJECT.md`;
- canonical requirements;
- relevant verified research;
- accepted decisions;
- current project/source baseline where needed.

## Master Plan

The approved Master Plan lives under `planning/`, normally `planning/MASTER_PLAN.md`, and should cover as applicable:

- problem and goal;
- current state / verified baseline;
- target state;
- authoritative requirements;
- frozen architecture decisions;
- non-goals;
- global invariants;
- external constraints;
- known source seams;
- milestones and checkpoint/acceptance for each;
- requirement coverage;
- dependencies;
- deployment/migration strategy;
- system verification strategy;
- idempotency/data-integrity constraints;
- fresh-context boundaries;
- Task Decomposition Policy references;
- OpenSpec Policy references;
- Handoff Policy references;
- Strategic Communication Policy references.

The Master Plan is not the live task tracker. Live execution state belongs in `implementation/TASK_BOARD.yaml`.

## Milestones

A milestone is a stable, integrated, testable checkpoint, not a single small task.

Planning should define milestone outcomes and acceptance without pretending that distant implementation interfaces are already known.

## Requirement coverage

Every authoritative requirement must have:
- an owner milestone;
- at least one implementation Task Card before execution of that requirement;
- a relevant OpenSpec change when the requirement establishes a behavior/API/schema/state/security/cross-package contract covered by the OpenSpec policy.

## Pre-implementation planning audit

Before execution preparation, perform an independent plan review when practical; whether performed by a separate reviewer/subagent or by a fresh review pass, audit:
- false assumptions;
- P0/P1 risks;
- milestone boundaries;
- task sizing;
- dependency correctness;
- missing acceptance/tests;
- requirement coverage;
- idempotency/data integrity;
- security;
- migration;
- OpenSpec boundaries;
- overengineering.

Resolve or explicitly defer material gaps.

## Distant work

Near-term Task Cards may be detailed. Distant work should be functionally specific but must not freeze nonexistent interfaces. Every card whose details can drift before execution requires the Refresh Gate.
