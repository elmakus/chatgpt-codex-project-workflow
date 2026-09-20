# Change: branch-first M01 managed-change state and entry contracts

## Why

The approved Definition requires every new managed repository change to acquire an exact branch-isolated workstream before its first durable change-specific write. Current fixed-policy entry is marker-led, root PROJECT owns pre-execution routing pointers, and root/default state is still described as a normal selected mode.

M01 establishes the durable state/transition contract that later policy-local lifecycle migrations can consume without creating shared cross-policy lifecycle mechanics.

## Authority

- requirements/BRANCH_FIRST_MANAGED_CHANGES.md — REQ-BF-001..009, REQ-BF-011, REQ-BF-015..017
- ADR-BF-001, ADR-BF-002, ADR-BF-003
- planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md — M01

## Proposed change

Define a neutral change workstream identity, workstream-local pre-execution routing pointers, deterministic generic natural-language managed-change entry, branch-before-write creation/recovery, and recovery/migration-only treatment of historical root/default state.

## Non-goals

- no full ChatGPT-only lifecycle pointer migration (M02);
- no full Codex-only lifecycle pointer migration (M03);
- no deletion/rewrite of historical default evidence;
- no final README/dogfood cleanup (M04);
- no shared cross-policy Intake/Router/Workstreams implementation.
