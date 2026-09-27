# M02Q-T29 repair after R04 RED

## Source finding

R04 fresh full-scope discovery found one new blocking contract defect, `M02Q-T29-F02`: a `review_acceptance_migrations` proof could claim an `attempt_id` inconsistent with the exact immutable Review locator. Board validation keyed uniqueness by `(card_id, attempt_id)` and matched the source locator independently, so the same exact Review locator could be admitted twice under different claimed attempt identities. Serving could select the valid proof and ignore the contradictory record instead of failing closed.

R04 evidence remains immutable at `evidence/M02Q-T29_REVIEW_R04_2026-09-27.md`.

## Bounded correction

Product repository: `elmakus/project_workflow_v2`
Branch: `work/pwv21-policy-kernel`

Corrected exact product subject:

- final correction commit: `a2bc026262e1f4a16dd06d7b1ef04d8de5a98f9f`
- tree: `f7a89dbf4e321fc0edcd201fe8b3213be13a46b4`
- base reviewed implementation: `cf4a84e8a4e8f2e75ae14f3b298f3632aefd9d80`

The correction is confined to the accepted T29 product contract and regression surface:

- `tools/review_acceptance_provenance.py` now requires `source_path` to be the canonical explicit Review path derived from the proof's exact `card_id + attempt_id`. A proof cannot reuse one Review locator while claiming a different attempt identity.
- `tests/test_review_acceptance_provenance.py` adds a direct proof-shape negative for mismatched `attempt_id`.
- `tests/test_state_contract.py` adds the exact contradictory-pair regression: one valid proof plus a second record with the same immutable source Review locator and a different claimed `attempt_id` must fail closed. The pre-existing unknown-owner control was made internally coherent with the stricter earlier guard so it continues testing its intended boundary.

No router serving semantics, RF004 exact acceptance, T26 legacy-Result compatibility or consumer historical Review/Card bytes were changed.

## Verification

- Exact product diff from `cf4a84e8` to `a2bc0262` changes only `tools/review_acceptance_provenance.py`, `tests/test_review_acceptance_provenance.py`, and `tests/test_state_contract.py`.
- Remote `work/pwv21-policy-kernel` resolves exactly to `a2bc026262e1f4a16dd06d7b1ef04d8de5a98f9f`.
- GitHub Actions push run `36342914095` on exact head `a2bc026262e1f4a16dd06d7b1ef04d8de5a98f9f` completed **success**.
- GitHub Actions pull-request run `36342917095` on the same exact head also completed **success**.
- Final exact-head logs show the Board migration-coherence test PASS, router suite 119/119 PASS, cumulative unittest discovery 1221/1221 PASS and M01 baseline checks PASS.
- Intermediate heads intentionally exposed an obsolete negative-control fixture that became invalid earlier than its asserted boundary after the new guard; the final correction repairs that fixture without weakening the new invariant.
- T09-T12 consumer Review/Card/Result bytes remain untouched; downstream four-record proof population remains outside T29.
- F03 consumed-trigger migration, milestone re-review and M03 remain outside this correction.

Fresh independent closure verification of `M02Q-T29-F02` is required before another fresh full-scope discovery may finalize T29.
