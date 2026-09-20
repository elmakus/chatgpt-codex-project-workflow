# M01 Handoff — Fork release versioning

## Checkpoint

- Milestone: `M01 — Canonical fork-release contract and publication enforcement`
- Implementation behavior head: `cec373fbfe38ffb1602a17f87f222e244e1f1657`
- Current reconciled integration target: `main@a52fae6c38944f69c4ec38dc6e77457935146f26`
- Target reconciliation commit: `8fad2acd3a31ccb53012e2f67f3fd8b8df706343`
- Integrated milestone acceptance: **GREEN**
- Independent Card review: **GREEN**
- Workstream final-integration review: **GREEN by exact coverage reuse**
- Pull request: `#40`
- Final integration result: pending final-target merge/result reconciliation

## Achieved state

Project Workflow now has one policy-neutral downstream-fork release contract at `workflow/common/FORK_RELEASE_VERSIONING.md`.

For durably established downstream forks it requires exact upstream repository/tag/SHA provenance and canonical `v<upstream-version>-private.N` lineage, with numeric per-baseline increments, reset/isolation across accepted upstream baselines, immutable legacy releases, explicit rejection of generic highest-SemVer across mixed lineage, and release-quality independence from the `private` suffix.

ChatGPT-only Close, Codex-only Close, and legacy/shared Review and Handoff all defer release-version selection/validation to that common contract. The repository-local auto-patch tagging workflow remains outside this Card.

## Authority now in force

- `requirements/FORK_RELEASE_VERSIONING.md` R1
- `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` / ADR-FRV-001
- `planning/FORK_RELEASE_VERSIONING_MASTER_PLAN.md` / FRV-P2 / M01
- `openspec/changes/fork-release-versioning/`

## Verification

- M01-T01 implementation evidence: `implementation/workstreams/issue-fork-release-versioning/evidence/M01-T01.md`
- Independent review evidence: `implementation/workstreams/issue-fork-release-versioning/evidence/M01-T01-review.md`
- Final integration refresh / milestone acceptance: `implementation/workstreams/issue-fork-release-versioning/evidence/M01_FINAL_INTEGRATION_REFRESH_2026-09-20.md`
- Exact-subject focused tests: 8/8 GREEN
- Exact-subject full repository test discovery: 21/21 GREEN
- Current-main reconciled full repository test discovery: **62/62 GREEN**
- Current-main merge: no textual conflicts; FRV behavior/acceptance surface unchanged; review coverage preserved.

## Continuation

The closure-ready workstream package is complete except for fields inherently dependent on the actual final-target integration result. Re-read `main` and PR #40 immediately before merge, merge only if the refresh remains current, then reconcile the actual merge result/checkpoint from target-side state.
