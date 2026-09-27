# M02Q-T29 repair after R02 RED

## Source closure failure

R02 closure verification kept the existing R01 finding `M02Q-T29-F01` open in material defect class `review-acceptance-required-evidence-completeness`.

R01 had required Board-level regression coverage for review-acceptance migration uniqueness and coherence, explicitly including selected-card/contract/review-locator coherence. The first repair added duplicate-proof, Review-locator, legacy-overlap and statusless-routing negatives, but omitted selected-owner and contract-path mismatch controls.

R02 evidence remains immutable at `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/M02Q-T29_REVIEW_R02_2026-09-27.md`.

## Bounded correction

Product repository: `elmakus/project_workflow_v2`
Branch: `work/pwv21-policy-kernel`

Corrected exact product subject:

- final correction commit: `cf4a84e8a4e8f2e75ae14f3b298f3632aefd9d80`
- tree: `ac6e08484b661d06347f9c6f450559cf07dedfb5`
- base presented to R02: `11dd88d1a1153ca63e55b567f7ba5af24cc3114b`
- base semantic implementation: `0b1bcdf63e4198ae53ace14a69d7c792e620ed19`

The exact `11dd88d1..cf4a84e8` correction changes only `tests/test_state_contract.py`; no production logic or consumer historical bytes changed.

Added Board-coherence regression negatives inside `test_review_acceptance_migration_rejects_duplicate_and_incoherent_board_state`:

- unknown selected Card owner is rejected;
- non-DONE selected owner (`returned`) is rejected by the migration DONE requirement;
- selected Card contract-path mismatch is rejected fail-closed by the exact Card contract invariant.

Together with the earlier repair, the test now covers valid control, duplicate identity, selected owner/DONE coherence, contract-path coherence, source Review-locator coherence and legacy-result overlap. The explicit router negative proving the structured Review migration cannot substitute for the separate statusless legacy-Result path remains intact.

## Verification

- Exact product compare `11dd88d1..cf4a84e8`: one changed file, `tests/test_state_contract.py`, +27/-0.
- Exact product tree: `ac6e08484b661d06347f9c6f450559cf07dedfb5`.
- GitHub Actions pull-request run `36337254680` targets exact head `cf4a84e8a4e8f2e75ae14f3b298f3632aefd9d80` and completed **success**.
- That exact-head run executes `sh scripts/test.sh`; the expanded Board-coherence regression is PASS, the statusless router migration negative is PASS, cumulative unittest discovery is 1221/1221 PASS, and M01 baseline checks PASS.
- A same-head push run first encountered an unrelated `TemporaryDirectory` cleanup error in `test_close_contract` after the T29 tests passed; no production change was made in response. The exact-head successful PR run provides the required full-suite CI proof.
- Product behavior remains unchanged from `0b1bcdf63e4198ae53ace14a69d7c792e620ed19`.
- T09-T12 consumer Review/Card/Result bytes remain untouched; downstream four-record proof population remains outside T29.
- F03 consumed-trigger migration, semicolon residual, milestone re-review and M03 remain outside this correction.

A fresh independent closure verification of the still-open R01 finding `M02Q-T29-F01` is required on the corrected Result subject.
