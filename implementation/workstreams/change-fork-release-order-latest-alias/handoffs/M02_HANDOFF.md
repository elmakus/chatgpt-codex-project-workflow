# M02 Handoff — Fork-channel ordering and moving aliases

## Checkpoint

- Milestone: `M02 — Canonical fork-channel ordering and moving aliases`
- Implementation behavior head: `822c0ee434e5dde5904a3709af5022bc0905bb5b`
- Reconciled pre-merge integration target: `main@fd2dc95f539d982e1009d71bbf1301f3098900f6`
- Integration pull request: pending
- Final integration result: pending
- Integrated milestone acceptance: **GREEN**
- Independent Card review: **GREEN**
- Workstream final-integration review: **GREEN by exact coverage reuse**
- Final-integration refresh evidence: `implementation/workstreams/change-fork-release-order-latest-alias/evidence/M02_FINAL_INTEGRATION_REFRESH_2026-09-21.md`

## Achieved state

M02 extends the existing downstream-fork release contract with one canonical cross-baseline fork-channel order over exact canonical private releases, numeric `(X, Y, Z, N)` ordering, explicit exclusion of upstream-only/legacy/malformed candidates, and an optional native moving-`latest` contract that preserves immutable versioned identity and exact artifact/content identity.

Generic SemVer is explicitly not the canonical fork-channel resolver. No runtime resolver/service, downstream repository mutation, external release/tag/alias write, or change to the repository-local auto-patch tagger is part of this milestone.

## Authority now in force

- `requirements/FORK_RELEASE_VERSIONING.md` R2
- `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` / ADR-FRV-001
- `planning/FORK_RELEASE_VERSIONING_MASTER_PLAN.md` / FRV-P3 / M02
- `openspec/changes/fork-release-versioning/`

## Verification

- M02-T01 implementation + independent review evidence: `implementation/workstreams/change-fork-release-order-latest-alias/evidence/M02-T01.md`
- Exact-subject independent rerun: 12/12 focused FRV tests GREEN; 112/112 full repository unittest discovery GREEN; `git diff --check` GREEN.
- Final target refresh: current `main` is not ahead of the reviewed implementation subject; post-review commits are closure/state/evidence only and do not change reviewed behavior or the acceptance surface.

## Terminal recovery

Before merge, recover from this workstream branch + manifest + selected Task Board. After final-target merge, reconcile the pending PR/result fields from the target-side namespaced package and immutable merge evidence; do not depend on source-branch survival.
