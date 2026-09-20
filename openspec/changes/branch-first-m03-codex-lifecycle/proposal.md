# Proposal — Codex-only branch-first lifecycle migration

## Why

The approved branch-first Definition requires active managed-change routing and execution state to remain workstream-local. M01 introduced the shared workstream routing schema and generic managed-change entry, while M03 must realize that invariant inside `codex_only` without importing ChatGPT-only lifecycle mechanics or weakening Codex Main / Executor / Tester / bounded-batch semantics.

## What changes

M03 migrates Codex-only lifecycle ownership in two bounded steps:

1. pre-execution Brainstorming, Research, Definition, Planning and plan-review routing use selected `WORKSTREAM.yaml -> routing.*` locators rather than mutable root-`PROJECT.md` pointers;
2. active execution/default-state handling migrates to manifest-bound workstream Task Boards, with historical root/default state remaining recovery/migration input only.

This change preserves:
- explicit user ownership of Brainstorming → Definition promotion;
- Codex Main as sole shared Project Workflow state writer;
- independent exact-subject Tester semantics;
- runtime identity exclusion from durable project state;
- serial-default plus bounded M03 batch/post-batch-drain semantics;
- target refresh, terminal package and branch-cleanup safety.

## Authority

- `requirements/BRANCH_FIRST_MANAGED_CHANGES.md`
- ADR-BF-001..003
- `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md@BF-R3#M03`
- M01 and M02 GREEN checkpoint evidence
