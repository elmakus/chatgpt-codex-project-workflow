# M04 Cumulative Handoff

Workstream: `feature-codex-only-policy`
Milestone: `M04`
Status: **GREEN / done**
Checkpoint: `48a56cbd5554b1378fa3727449bfce94e2f7f1df`

## Achieved state

The dedicated `codex_only` namespace is now live at the policy-contract level: root routing selects it explicitly, the full Intake-through-Close lifecycle is represented, and the M02 review/runtime boundary plus M03 bounded-parallel invariants remain integrated.

The exact M04 implementation subject `48a56cbd...` received independent GREEN review. A subsequent assessment against current `main` found no reason to reopen M01-M04.

## Authority now in force

- Requirements: `requirements/CODEX_ONLY_POLICY.md`
- Plan: `planning/CODEX_ONLY_MASTER_PLAN.md`
- Decisions:
  - `decisions/ADR_CODEX_ONLY_DEDICATED_NAMESPACE.md`
  - `decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md`
  - `decisions/ADR_CODEX_ONLY_BOUNDED_PARALLEL_CARDS.md`
- M04 OpenSpec: `openspec/changes/codex-only-m04-lifecycle-cutover/`

## Evidence

- M04 acceptance: `implementation/workstreams/feature-codex-only-policy/evidence/M04-acceptance.md`
- M04 implementation: `implementation/workstreams/feature-codex-only-policy/evidence/M04-T01.md`
- Independent review: `implementation/workstreams/feature-codex-only-policy/evidence/M04-T01-review-01.md`
- Current-main refresh: `implementation/workstreams/feature-codex-only-policy/evidence/M04-current-main-refresh.md`

## Continuation

Next approved milestone: `M05 — End-to-end regression, architecture audit and publication readiness`.

Durable start pointer remains:
`implementation/workstreams/feature-codex-only-policy/TASK_BOARD.yaml`

M05 JIT preparation must explicitly include current-target compatibility, cross-policy regression, semantic merged-result inspection, reconciliation of target-owned global project state (especially root `PROJECT.md`), final-integration review preparation and final target readback.
