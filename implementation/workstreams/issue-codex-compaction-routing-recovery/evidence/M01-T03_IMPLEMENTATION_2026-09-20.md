# M01-T03 implementation evidence — 2026-09-20

## Subject

- Card: `M01-T03 — Add orchestration recovery regressions and documentation`
- Exact implementation subject: `0a11f92fd03d08d94e4614204eef4dab3813d4bc`
- Execution-start comparison base: `b617fc973435a1b70b0e88c3d04051662a22ed40`
- Independent review requirement: `none`

## Implemented scope

- Added `tests/test_codex_only_orchestration_recovery_contract.py` with focused CCOR-R10 coverage for manifest binding shape/ownership, same-version current-context re-bind, Intake/Recovery schema handling, generic dispatch gating, fail-closed behavior, fingerprint drift, runtime ownership boundaries, bounded canonical recovery reads and ChatGPT-only isolation.
- Added concise README discoverability for the opaque binding + non-durable latch + compact recovery-kernel boundary.
- Added an Unreleased CHANGELOG entry for Codex orchestration context recovery.
- Marked the M01-T03 OpenSpec checklist complete.
- No T01/T02 runtime or lifecycle semantics were modified.

## Verification

Fresh detached worktree at the exact implementation subject:
- `python3 -m unittest tests.test_codex_only_orchestration_recovery_contract` → GREEN, 10/10.
- `python3 -m unittest tests.test_codex_only_continuous_orchestration_contract` → GREEN, 8/8.
- `python3 -m unittest discover -s tests -p 'test_*.py'` → GREEN, 88/88.
- `git diff --check b617fc973435a1b70b0e88c3d04051662a22ed40..0a11f92fd03d08d94e4614204eef4dab3813d4bc` → GREEN.
- Exact implementation diff contains only `README.md`, `CHANGELOG.md`, the OpenSpec task checklist and the new focused test file.

## Acceptance

GREEN. M01-T03 adds regression/documentation coverage only, preserves the independently reviewed M01-T01/T02 behavior and satisfies its Card acceptance.
