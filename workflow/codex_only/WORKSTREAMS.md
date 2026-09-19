# Codex-only Workstreams

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **adapt**.

## Core model

A branch-isolated workstream has one stable ID, exact branch/base/target, one manifest and at most one canonical Task Board. The manifest owns workstream identity/routing/final-integration review; the selected Task Board owns Card/milestone execution state.

## Foundation invariants

- Validate manifest ID/branch binding before trusting its Task Board.
- Legacy/default Task Board mode remains valid when no branch-isolated workstream is selected.
- Independent workstreams remain distinct from genuinely parent-dependent stacked work.
- No repository-global mutable workstream scheduler is introduced.
- Final integration uses current-target refresh and exact-subject review coverage.
- Codex Main owns shared workstream integration/project state.

M03 adds bounded intra-workstream compatible Card lanes with isolated mutable workspaces and recoverable integration bases while serial remains default. M04 reconciles stacked integration, target refresh, final-review coverage and full Close routing.
