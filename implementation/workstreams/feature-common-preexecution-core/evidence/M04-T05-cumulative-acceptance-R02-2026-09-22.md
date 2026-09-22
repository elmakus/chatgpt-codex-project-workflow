# M04-T05 — cumulative M04 acceptance R02

Date: 2026-09-22
Card: `M04-T05`
Target: `elmakus/project_workflow_v2@feat/pwv2-m04-integration-close`
Corrected target commit: `013c4b405875a356f863b9b381d60faa0ad8935a`
Corrected target tree: `7367d38d41240730530ec3b16174ca7db2738807`
PR: `elmakus/project_workflow_v2#4`
Prior immutable review: `M04-T05-independent-review-R01-2026-09-22.md` = RED on older subject `f40250fa2fe88477df3f03c26adfeb2d8024581b`.

## R01 bounded correction

R01 found that the trigger-only fork-lineage helper accepted any non-empty upstream commit value even though accepted authority requires exact upstream repository/tag/commit-SHA provenance.

The corrected target:
- requires the upstream commit identity to match the repository's exact lowercase 40-hex Git SHA contract before a downstream-fork release lineage can be accepted;
- rejects empty, non-SHA, uppercase, 39-character and 41-character commit identities;
- preserves the existing trigger-only boundary, baseline-local numeric `private.N`, numeric cross-baseline ordering, immutable history, native-latest exact-artifact rule and non-authorizing publication semantics.

The correction is bounded implementation/test work under existing M04.P4 / ADR-FRV-001 / FRV-REQ-005 authority. Requirements and plan are unchanged.

## Exact GitHub readback

- feature branch HEAD = `013c4b405875a356f863b9b381d60faa0ad8935a`;
- tree = `7367d38d41240730530ec3b16174ca7db2738807`;
- PR #4 remains open/draft against `main@29f5e1880d66949c3009afa399490a6a81bc949a`;
- compare = 10 commits ahead / 0 behind;
- PR #4 is mergeable with `mergeable_state: clean`;
- GitHub Actions push run `35773744806` = completed/success on the exact corrected head;
- GitHub Actions pull-request run `35773750088` = completed/success on the exact corrected head;
- repository-check job is GREEN in both runs.

## Fresh full acceptance execution

A fresh checkout of the exact corrected head was verified independently from the implementation repository state:

- `sh scripts/test.sh`: PASS;
- state contract: 28/28 PASS;
- router: 39/39 PASS;
- execution: 4/4 PASS;
- review: 1/1 PASS;
- recovery: 2/2 PASS;
- Close + fork-lineage: 29/29 PASS;
- full unittest discovery: 103/103 PASS;
- `python3 -m compileall -q .`: PASS;
- `git diff --check`: PASS;
- clean working tree after verification: PASS;
- exact readback: HEAD `013c4b405875a356f863b9b381d60faa0ad8935a`, tree `7367d38d41240730530ec3b16174ca7db2738807`.

## Cumulative M04 acceptance

The corrected exact target retains the previously frozen M04 surface:

- A06 uncertain external effect: exact readback before retry; unresolved occurrence fails closed;
- A08 review coverage reuse: target-SHA movement alone may reuse GREEN only when covered content/behavior/acceptance are unchanged and affected compatibility is GREEN;
- A09 integration refresh: material content/behavior/acceptance reconciliation creates a new immutable review subject;
- A10 terminal package/source disappearance: target-side recovery is independent of source-branch survival, with exact-head cleanup and absence readback;
- A16 fork release module trigger: ordinary Close does not load fork lineage; exact durable downstream-fork lineage is required and malformed upstream commit SHA now fails closed;
- tracker closing linkage remains limited to the final scope-completing default-branch PR, with post-completion readback/fallback rules;
- repeated Close/recovery does not authorize duplicate external effects;
- deployment/live-write state alone creates no human gate and fork lineage does not authorize sync/tag/release/deploy;
- true end of approved scope occurs only after durable completion and no already-authorized obligation remains.

No actual fork tag, release, deployment, upstream sync, branch deletion, PR merge, production migration/adoption or custody transfer was performed.

## Freeze disposition

The R01 subject/evidence remains immutable RED history.

The corrected M04-T05 implementation/evidence is ready to freeze as a new exact immutable subject using:
- target commit/tree above;
- unchanged M04-T05 Card blob;
- this evidence blob.

M04-T05 remains non-terminal until a fresh independent reviewer issues GREEN for that new subject.
