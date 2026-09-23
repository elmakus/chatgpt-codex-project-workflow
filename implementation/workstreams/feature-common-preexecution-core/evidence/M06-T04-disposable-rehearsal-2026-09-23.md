# M06-T04 — disposable migration rehearsal and boundary documentation

Date: 2026-09-23
Result: GREEN

## Exact target

- Repository: `elmakus/project_workflow_v2`
- Branch: `feat/pwv2-m06-migration`
- Commit: `960351d98ff44e6fde60d035ab4b0000eb33c63b`
- Tree: `f7737105fff7840dcbb4b84efaea31103d636441`
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
- run `35848053057`, job `107138872691`: success.

The repository checks include the T01/T02/T03 migration suites plus `tests.test_migration_rehearsal`; the final migration/close/delivery group is 75/75 GREEN and full unittest discovery is 149/149 GREEN.

A semantic audit after the first T04 candidate found one missing edge: an exact migrated `pending`/ `in_progress` review could retain a terminal Card status. The exact target above fixes that by keeping every nonterminal review blocking until GREEN and adds a dedicated pending-review regression.

A17 authority readback against `brainstorming/V1_TO_V2_COVERAGE_MATRIX.md` at blob `aafd4a916ae11f8a3ff0c6edb799d8ced996a4bf` found 97 classified rows, 0 `OPEN`, and no unclassified disposition rows.

## Acceptance

M06-T04 is GREEN on the corrected exact target. A02/A03/A05/A06/A07/A10/A15/A17 migration-relevant boundaries are represented by deterministic repository tests/documented disposition; pending/RED/GREEN review obligations remain blocking until exact GREEN; no real-project migration or production custody transfer was performed.
