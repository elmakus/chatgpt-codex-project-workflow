# Planning

## Responsibility

ChatGPT is the project planning/router layer for problem definition, verified baseline, requirements, architecture, global invariants, milestones and requirement coverage.

Do not freeze detailed code-dependent design far in advance of the source/runtime state it depends on. The eventual executor reconciles implementation details through the Refresh Gate.

## Inputs

Use project `PROJECT.md`, canonical requirements, relevant verified research, accepted decisions and current source/runtime baseline where needed.

## Master Plan

The approved Master Plan lives under `planning/` and covers as applicable:

- problem and goal;
- current state / verified baseline;
- target state;
- authoritative requirements;
- frozen architecture decisions;
- non-goals and invariants;
- external constraints;
- known source seams;
- milestones and acceptance;
- requirement coverage;
- dependencies;
- deployment/migration strategy;
- system verification;
- idempotency/data integrity/security;
- fresh-context boundaries;
- Task Card/OpenSpec/handoff references.

The Master Plan is not the live task tracker. Live execution state belongs in `implementation/TASK_BOARD.yaml`.

## Milestones and competing paths

A milestone is a stable, integrated, testable checkpoint, not a tiny task.

When independent alternatives genuinely need experimentation, planning may use separate research/prototype branches (Path A, Path B, etc.) from the same stable checkpoint. Each path records its own findings/evidence. Later comparison produces an accepted A/B/Hybrid decision before production implementation. This is an optional pattern, not a mandatory lifecycle stage and not a new execution status.

## Requirement coverage

Every authoritative requirement must have an owner milestone and at least one implementation Task Card before execution. Use OpenSpec only when its contract-risk policy justifies it.

## Pre-implementation review

Before execution preparation, independently audit false assumptions, risks, milestone boundaries, dependencies, tests/acceptance, requirement coverage, data integrity, security, migration and overengineering when practical.

Resolve or explicitly defer material gaps.
