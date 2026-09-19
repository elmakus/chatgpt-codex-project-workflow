# Codex-only Recovery

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **adapt**.

## Ownership

Recovery reconstructs Project Workflow obligations from durable project repository state when execution/review/integration continuity is uncertain.

## Invariants

- Recover from project/workstream identity, canonical Task Board, exact Git/integration state, Card/plan authority and durable evidence.
- Exact review subjects and prior verdict evidence remain project truth across runtime interruption.
- Runtime resume versus replacement must not change Project Workflow semantics.
- Partial or contradictory project-state writes fail closed and are reconciled before unrelated work starts.
- Do not require runtime worker identity as a durable project key.
- Codex Main remains the project-level shared-state owner.

M02 finalizes review/recovery provenance and fail-closed state transitions. M03 adds bounded lane-result/integration recovery semantics.
