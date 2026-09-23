# M06-T05 — independent review R01

Date: 2026-09-23
Verdict: RED

## Exact reviewed subject

`elmakus/project_workflow_v2@commit:5b3d195e61645d541821f238f5374cca7e121e58|tree:82b7a601c3fe21f8f11219b0f5b0cf02e5ee3386|M06-T05-card-blob:ded11bcd22c639d529867adbd95544b198508fa3|acceptance-evidence-blob:c1967e92ff0c213fb4866e0fafa64777d7ac8e05`

The Card blob, cumulative-evidence blob, target commit/tree, PR #6 exact head/base and both recorded exact-head Actions successes were independently read back. M01-M05 handoffs, the approved PWV2-P2 M06 contract, M06 technical contract, M06-T01..T04 evidence, applicable PWV2 requirements and ADRs were inspected.

## Findings

### R01-F1 — dry-run identity is not bound to conversion input

`convert_dry_run()` accepts a GREEN dry-run plan carrying exact board/manifest hashes, but reparses the supplied `board_text` / `manifest_text` without proving they match those hashes. A caller can therefore create a plan for source A, convert different still-valid source B, retain A's source fingerprint/provenance in the bundle, then pass A again to `apply_fixture_conversion()`; apply validates A against the bundle provenance while activating canonical state derived from B.

This breaks the exact-source identity boundary required by M06.P1/P2/P3, the M06 technical contract, and A03/A15. The output fingerprint only proves internal bundle consistency; it does not repair the missing A→conversion binding.

### R01-F2 — V1 workstream final-integration review can be silently lost

The supported real-derived Codex V1 manifest fixture contains an activated `RECOMMENDED` workstream review with `state: green`, subject and evidence. Dry run allows that terminal GREEN state, while conversion migrates only Card-level reviews. It creates neither a common V2 review attempt nor a blocking review obligation for the manifest-owned final review, and the semantic verdict/evidence is absent from normalized review history.

This violates the M06.P2 requirement to preserve exact review history/authorization semantics and the technical contract rule that an unprovable V1 verdict must become an explicit review obligation rather than disappear.

### R01-F3 — activated readback can verify a destination with dangling canonical locators

Conversion creates workstream-local locators for Task Card contracts, DONE results and terminal migrated review evidence. `migration_apply._stage_payloads()` materializes canonical TOML, migration metadata, review-attempt TOML and blockers, but it does not materialize the Task Card, result record or terminal review-evidence targets described by the bundle/`artifact_plan`. `_verify_materialized_root()` validates locator syntax and only hashes files listed in the migration record, so it can return verified — including the source-disappearance recovery path — while those canonical referenced artifacts do not exist.

This contradicts the M06.P2/P3 preservation/readback contract and invalidates the claimed A07/A10/A15 coverage for durable reviewed/result state.

## Verification assessment

The recorded exact-head CI is genuinely GREEN, but the current tests do not exercise the three defects above:
- no plan-A / conversion-B binding regression;
- no assertion preserving or blocking the supported manifest-owned GREEN final review;
- no readback assertion that every materialized canonical Card/result/terminal-review locator resolves after source disappearance.

Therefore the successful test runs are insufficient to satisfy the frozen M06-T05 acceptance subject.

## Corrective route

All findings are bounded L1/L2 implementation/test defects inside already accepted M06 authority. No Definition, Master Plan or user/product decision change is required. Correct the migration conversion/apply contract, add regressions for these cases, rerun exact acceptance, and freeze a new immutable M06-T05 subject for fresh independent review.
