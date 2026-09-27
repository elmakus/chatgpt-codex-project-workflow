# M02Q-T24 implementation evidence — RF006 legacy full-attempt-id compatibility

## Exact product subject

- Repository/branch: `elmakus/project_workflow_v2@work/pwv21-policy-kernel`.
- Baseline: `ae3d2d303fde8ee67dcfa24342549e96c0cf1d13`.
- Exact corrected HEAD: `445eaa39542bdd272a5347fec29360b07cbe1463`.
- Exact tree: `5ae7709c13ecf92774c60257431ec167261618d3`.
- Changed implementation blob: `tools/review_attempt_provenance.py@c9f7592e9f01b6bb964c0c276088398064fa5356`.
- Changed regression blob: `tests/test_review_attempt_provenance.py@13bcace245b5e94a13e963c72fb175379df8ab2e`.
- Baseline-to-head delta is one commit and exactly those two modified files.

## Implemented behavior

RF006 retains the canonical Review path `reviews/CARD-ID-ATTEMPT.toml` for ordinary/current attempts. It now derives one narrowly bounded historical alternate path only when the persisted attempt ID itself begins with the exact Card ID plus hyphen and the remaining suffix is an `R<number>` attempt token.

The alternate path is accepted only when all of the following are true: the locator path is exactly `reviews/ATTEMPT.toml`; the record is legacy-shaped (no `review_kind`); the verdict is terminal GREEN/RED; a `legacy_migration` table is present; and `verify_legacy_migration` independently proves the exact immutable source attempt, source Board listing, source blob, workstream/card/attempt binding, prior durability and current semantic equality. Current-schema full-ID records and legacy full-ID records without provenance remain fail-closed.

This preserves the six historical M02-T01 R07-R12 attempt identities rather than rewriting their terminal `attempt` fields.

## Tests and exact readback

- Focused `tests.test_review_attempt_provenance`: **31/31 GREEN** on exact remote HEAD.
- Broader state/router/Close suites before push: **259/259 GREEN** on the identical tree.
- Complete `scripts/test.sh` with isolated test dependency environment: **1196/1196 GREEN**, M01 baseline PASS, on tree `5ae7709c13ecf92774c60257431ec167261618d3`.
- Exact consumer phase-1 readback at `a90424383e0613b36c18affbf60c6868c54ffdfa`: **6/6 GREEN** for M02-T01-R07 through R12 through both `verify_legacy_migration` and `verify_review_attempt_locator`, with no historical field rewrite.
- Exact-head GitHub Actions run `36289890345` on `445eaa39542bdd272a5347fec29360b07cbe1463`: **completed / success**.
- Remote product branch readback resolves exactly to `445eaa39542bdd272a5347fec29360b07cbe1463`; exact changed blobs match the locally tested candidate.

## Scope

This Card fixes only the product-side RF006 compatibility returned by T23. It does not complete the consumer's 48 exact Task Board Review locators, which remains the separately allocated `after-M02Q-T24` outcome. OBL-M02Q-03, historical consumed-trigger proof migration, M02Q Milestone Review and M03 remain separate.

This is implementation evidence, not the required independent Card Review.
