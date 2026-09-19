# Codex-only Execution

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **adapt**.

## Fixed executor model

Codex Main is the fixed project execution coordinator for `codex_only`. Project Workflow defines Card authority, durable project state, acceptance and review boundaries. `codex_workflow` owns concrete worker-role realization and runtime lifecycle mechanics.

## Foundation execution loop

1. Resolve the exact project/workstream state context and canonical Task Board.
2. Recover any existing project obligation before selecting new work.
3. Respect pending/RED review, Research, authorization and strategic gates before unrelated implementation.
4. Select only authority-valid READY work.
5. Run a state/contract refresh against current repository/runtime evidence.
6. Execute bounded Card scope using the actual runtime; do not run a capability inventory or switch execution policy because a capability might be needed.
7. Persist implementation result, tests/evidence and exact review subject when a project review gate applies.
8. Let Codex Main integrate worker results and update shared Project Workflow state.
9. Return through the policy router after each durable obligation boundary; continue automatically when the next route is deterministic and authorized.

## Review boundary

The implementation owner does not issue its own formal verdict. A distinct independent reviewer judges the immutable exact subject. A reviewer does not repair production while acting as reviewer; RED returns through Main to the owning Executor.

## Deferred contract work

M02 finalizes review/state/recovery provenance and RED/repair semantics. M03 replaces the serial-safe foundation with the accepted bounded compatible-ready-set semantics while preserving serial execution as valid default. M04 completes lifecycle/routing integration.
