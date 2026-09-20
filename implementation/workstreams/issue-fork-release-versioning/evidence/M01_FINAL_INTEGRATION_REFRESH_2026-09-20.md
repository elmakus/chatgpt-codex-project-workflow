# M01 — final integration refresh and acceptance evidence

Date: 2026-09-20
Workstream: `issue-fork-release-versioning`
Integration target: `main`

## Refreshed exact state

- Current integration target: `main@f3cdb60367da3e978397409b51c37faa181d613f`.
- The workstream is `behind_by: 0`; the target is still the exact baseline used for implementation and independent Card review, so no rebase/merge/retarget reconciliation is required.
- Independently reviewed immutable workstream content/behavior subject: `cec373fbfe38ffb1602a17f87f222e244e1f1657`.
- Commits after that subject contain only review, evidence and Task Board state transitions. They do not alter workflow behavior, accepted authority, OpenSpec, tests, or the workstream acceptance surface.
- Full current-branch repository test discovery after Card finalization: **21/21 passed**.

## Integrated milestone acceptance

**GREEN** for M01 — Canonical fork-release contract and publication enforcement.

M01 contains one implementation Card, `M01-T01`, which owns FRV-REQ-001..012 and the full milestone outcome. The Card is terminal with independent review GREEN for the exact immutable subject above.

Acceptance was checked against:
- `requirements/FORK_RELEASE_VERSIONING.md` R1 / FRV-REQ-001..012;
- `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` / ADR-FRV-001;
- `planning/FORK_RELEASE_VERSIONING_MASTER_PLAN.md` / FRV-P2 / M01;
- the M01-T01 Card acceptance and required checks;
- the JIT OpenSpec under `openspec/changes/fork-release-versioning/`;
- implementation and independent review evidence.

The accepted result has one common policy-neutral fork-release contract, all three supported publication surfaces defer to it without duplicating the lineage algorithm, canonical `v<upstream>-private.N` semantics and migration/provenance rules are covered, historical release mutation/upstream-sync are excluded, and the repository-local auto-patch workflow remains unchanged.

No unresolved Card, Research obligation, blocker, stacked dependency, strategic decision, deployment/live-write authorization gate, target drift, or behavioral acceptance defect remains.

## Distinct workstream final-integration review coverage

The manifest final-integration gate is RECOMMENDED and distinct from the Card review lifecycle.

Coverage reuse is valid because:
1. this workstream has one implementation Card only;
2. M01-T01 owns the complete M01/workstream behavior and requirement surface;
3. its independent review checked the full authority slice, OpenSpec coherence, all three publication integrations, migration/provenance/non-goal boundaries, and regression coverage;
4. the immutable workstream content/behavior subject remains exactly `cec373fbfe38ffb1602a17f87f222e244e1f1657`;
5. post-subject commits are closure/review/state/evidence-only and do not change behavior or the acceptance surface;
6. the integration target has not moved and current-branch verification remains GREEN.

Therefore the distinct manifest gate may be reconciled GREEN with `covered_by` pointing to the exact independent M01-T01 review evidence. This is coverage reuse, not a second review verdict.

## Pre-merge condition

Immediately before merge, re-read `main` and the actual PR artifact. If the target or covered workstream behavior changes, rerun the integration refresh and invalidate coverage when required.
