# M06-T04 — disposable migration rehearsal and boundary documentation

Date: 2026-09-23
Result: GREEN

## Exact target

- Repository: `elmakus/project_workflow_v2`
- Branch: `feat/pwv2-m06-migration`
- Commit: `768cf3b3a2fa2013103d43730d3cb9fb0ef0d7b9`
- Tree: `adba3db05aaef2b7825ac4f48be3f7f352b0f12c`
- Draft PR: #6
- Base: `main@27b9132e173850e7d596092e023b0af7e0507472`

## Rehearsal result

M06 now has an automated disposable rehearsal matrix plus explicit migration/cutover documentation.

The bounded V1 reader was tightened so nested manifest structures are also finite and fail closed on unknown semantic fields. The dry run now explicitly surfaces and blocks automatic cutover for V1 states that cannot be safely inferred into common V2 without extra proof:
- exploratory/promotion state;
- active Research;
- Plan Review / premium A/B/C-equivalent pre-execution state;
- unresolved workstream review;
- stacked unmerged parent dependency.

These states remain visible as outstanding obligations rather than being silently dropped or interpreted as authorization.

The rehearsal also verifies:
- one active/in-progress Card survives conversion without scheduler/runtime-policy state;
- a completed Card remains a durable result rather than fresh execution;
- existing review conversion preserves exact append-only semantics or creates a blocker when proof is insufficient;
- legacy-root state remains migration input only;
- changed/unknown/racing/parallel-active/uncertain-effect cases fail closed;
- ordinary `tools/router.py` / `workflow/ROUTER.md` do not import the V1 migration modules;
- source-disappearance recovery and rollback/forward-repair boundaries remain explicit;
- one-live-owner transfer and production adoption remain M07-gated.

Documentation: `docs/V1_MIGRATION_REHEARSAL.md`.

## Verification

Exact-head Actions:
- push run `35847846522`, job `107138204950`: success;
- pull_request run `35847852710`, job `107138225341`: success.

The repository checks include the T01/T02/T03 migration suites plus `tests.test_migration_rehearsal`.

## Acceptance

M06-T04 is GREEN. A02/A03/A05/A06/A07/A10/A15/A17 migration-relevant boundaries are represented by deterministic repository tests/documented disposition; no real-project migration or production custody transfer was performed.
