# M04 Milestone Acceptance — GREEN

Milestone: `M04 — Full lifecycle integration, routing cutover and compatibility`
Implementation head/checkpoint: `48a56cbd5554b1378fa3727449bfce94e2f7f1df`
Card: `M04-T01`

## Acceptance

GREEN against `planning/CODEX_ONLY_MASTER_PLAN.md#M04--full-lifecycle-integration-routing-cutover-and-compatibility` and the M04 authority slice.

- Root routing explicitly selects the dedicated `codex_only` namespace while preserving isolated `chatgpt_only` and legacy fallback for other accepted non-migrated policies.
- The 22-file Codex-only namespace provides the required live lifecycle from Intake through Close without active cross-policy/legacy execution ownership.
- Default and manifest-selected Task Board recovery, micro-fix, stacked workstreams, current-target refresh, exact final-review coverage and terminal target-side recovery are represented.
- M02 immutable review / Tester non-repair semantics and M03 serial-default bounded-parallel/recovery invariants remain intact.
- Current-main workstream-finalization semantics assessed after implementation are already covered by the frozen M04 subject.
- This repository still declares `execution_policy: chatgpt_only`.
- M04 OpenSpec, static boundary checks, conflict scan and M04-specific whitespace checks are GREEN.

## Review and evidence

- Card implementation evidence: `implementation/workstreams/feature-codex-only-policy/evidence/M04-T01.md`
- Current-main compatibility refresh: `implementation/workstreams/feature-codex-only-policy/evidence/M04-current-main-refresh.md`
- Independent review 01: GREEN — `implementation/workstreams/feature-codex-only-policy/evidence/M04-T01-review-01.md`
- OpenSpec: `openspec/changes/codex-only-m04-lifecycle-cutover/`
- Audit: `docs/audits/CODEX_ONLY_M04_LIFECYCLE_CUTOVER.md`

No milestone-level independent review gate is active beyond the GREEN Card review.

## Deferred final-integration obligation

M04 is a branch-local checkpoint, not final integration to `main`. The already-approved M05 milestone owns end-to-end regression plus current-target/final-integration refresh, including reconciliation of target-owned root `PROJECT.md` state before publication.
