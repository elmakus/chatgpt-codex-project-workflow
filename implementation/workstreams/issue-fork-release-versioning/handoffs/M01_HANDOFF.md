# M01 Handoff — Fork release versioning

## Checkpoint

- Milestone: `M01 — Canonical fork-release contract and publication enforcement`
- Implementation behavior head: `cec373fbfe38ffb1602a17f87f222e244e1f1657`
- Reconciled pre-merge integration target: `main@a52fae6c38944f69c4ec38dc6e77457935146f26`
- Integration pull request: `#40`
- Final integration result: `47c3cae3c1e1eb0ea8065a10b1e5dd052b96ce12`
- Integrated milestone acceptance: **GREEN**
- Independent Card review: **GREEN**
- Workstream final-integration review: **GREEN by exact coverage reuse**
- Target-side closure evidence: `implementation/workstreams/issue-fork-release-versioning/evidence/M01_FINAL_CLOSURE_2026-09-20.md`
- Source branch: automatically deleted by GitHub after successful merge; no fallback cleanup marker required

## Achieved state

The approved FRV-P2/M01 fork-release versioning contract is integrated into `main`. Project Workflow now has one policy-neutral downstream-fork release contract at `workflow/common/FORK_RELEASE_VERSIONING.md`.

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
- Exact-subject full repository discovery: 21/21 GREEN
- Current-main reconciled full repository discovery: 62/62 GREEN
- Exact integration merge-result target readback at `47c3cae3…`: 62/62 GREEN; `git diff --check HEAD^1..HEAD` GREEN; required namespaced package present.

## Terminal recovery

Recover completed truth from the target-side `implementation/workstreams/issue-fork-release-versioning/` package plus manifest result and immutable PR #40 merge evidence. Preserve `fix/fork-release-versioning` as source-workstream provenance even though GitHub automatically deleted that merged head. No live Card, Research, review, stacked-dependency or integration obligation remains.
