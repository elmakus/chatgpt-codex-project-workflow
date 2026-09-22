# M04 Handoff — Project Workflow V2 construction

Milestone: `M04 — Integration, tracker closure, publication and terminal recovery`
Plan revision: `PWV2-P1`
Status: `GREEN / target integration complete`

## Completed checkpoint

- Control workstream checkpoint: `63989dc6ee404db508d96ada033e83ea8b8dbb55`.
- Exact V2 implementation subject: `elmakus/project_workflow_v2@013c4b405875a356f863b9b381d60faa0ad8935a`.
- Reviewed target tree: `7367d38d41240730530ec3b16174ca7db2738807`.
- Cards `M04-T01` through `M04-T05`: done.
- M04-T05 independent review R02: GREEN.
- Earlier M04-T05 R01 RED remains immutable history for its older subject.
- Target PR: `elmakus/project_workflow_v2#4`.
- Target merge commit / current `main`: `674fb970913c393cfc6ed82a5ef67dda8b8713b7`.
- Target integration evidence: `implementation/workstreams/feature-common-preexecution-core/evidence/M04-target-integration-2026-09-22.md`.
- Deterministic M04 acceptance: `implementation/workstreams/feature-common-preexecution-core/evidence/M04-T05-cumulative-acceptance-R02-2026-09-22.md`.
- Review evidence: `implementation/workstreams/feature-common-preexecution-core/evidence/M04-T05-independent-review-R02-2026-09-22.md`.

## Authority now in force

- Frozen Definition: `requirements/PROJECT_WORKFLOW_V2.md` R1.
- Accepted decisions: ADR-PWV2-001..006 plus trigger-only fork-release lineage authority.
- Approved Strategic Master Plan: `planning/PROJECT_WORKFLOW_V2_MASTER_PLAN.md` revision `PWV2-P1`.
- M04 execution/review state remains owned by this selected branch-isolated control workstream.
- Construction custody remains with the current V1 `chatgpt_only` workstream until the later approved custody-transfer boundary.

## Achieved state

M04 completes the common Close/integration semantics on top of M03:
- semantic refresh before review reuse/integration and exact pre-mutation target reread;
- external-effect readback-before-retry and fail-closed uncertain occurrence;
- final tracker close boundaries that do not turn Issue state into workflow authority;
- target-side recovery independent of source-branch survival, exact-head cleanup and terminal-unmerged history separation;
- trigger-only downstream-fork lineage with exact upstream repo/tag/SHA, baseline-local numeric `private.N`, lineage-aware ordering, immutable history and exact-artifact native-latest semantics;
- true end-of-approved-scope continuation without manufacturing a user gate from deployment/live-write status alone.

R01 identified malformed upstream commit provenance acceptance. The bounded correction on `013c4b405875a356f863b9b381d60faa0ad8935a` now requires an exact lowercase 40-hex SHA and was independently re-reviewed GREEN as R02.

Fresh independent exact-subject verification passed `scripts/test.sh`, 103/103 full unittest discovery, compileall, diff/check and clean-tree checks. Exact-head GitHub Actions runs remained GREEN.

Target integration is GREEN: `main` is `674fb970913c393cfc6ed82a5ef67dda8b8713b7`; reviewed head → `main` is exactly one merge commit with zero changed files. GitHub automatically removed the merged M04 source branch; no ref was recreated.

## Deliberately deferred

M04 does not claim or activate:
- M05 ChatGPT/Codex delivery and update-propagation qualification;
- L01–L05 real-surface acceptance beyond evidence explicitly owned by later milestones;
- V1→V2 migration rehearsal;
- first production adoption/cutover;
- construction custody transfer;
- any actual downstream-fork tag/release/deployment.

## Next durable starting point

M04 is fully closed and integrated. The next approved plan milestone is `M05`, whose M01–M04 prerequisites are satisfied.

Resume from this selected Task Board, the approved `PWV2-P1` M05 contract and target `elmakus/project_workflow_v2@main` at `674fb970913c393cfc6ed82a5ef67dda8b8713b7`. The policy router determines the next legal role.
