# M01 Handoff — Fork release versioning

## Checkpoint

- Milestone: `M01 — Canonical fork-release contract and publication enforcement`
- Implementation behavior head: `cec373fbfe38ffb1602a17f87f222e244e1f1657`
- Integration target baseline: `main@f3cdb60367da3e978397409b51c37faa181d613f`
- Integrated milestone acceptance: **GREEN**
- Independent Card review: **GREEN**
- Final integration result: pending final-target PR/merge reconciliation

## Achieved state

Project Workflow now has one policy-neutral downstream-fork release contract at `workflow/common/FORK_RELEASE_VERSIONING.md`.

For durably established downstream forks it requires exact upstream repository/tag/SHA provenance and canonical `v<upstream-version>-private.N` lineage, with numeric per-baseline increments, reset/isolation across accepted upstream baselines, immutable legacy releases, explicit rejection of generic highest-SemVer across mixed lineage, and release-quality independence from the `private` suffix.

ChatGPT-only Close, Codex-only Close, and legacy/shared Review and Handoff all defer release-version selection/validation to that common contract. The repository-local auto-patch tagging workflow remains unchanged.

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
- Current closure branch full repository test discovery: 21/21 GREEN

## Continuation

The closure-ready workstream package is complete except for values inherently dependent on the actual final-target integration result. Continue with final-integration review coverage reconciliation, open/verify the PR to `main`, re-read the target immediately before merge, then reconcile the actual merge result/checkpoint from target-side state.
