# M02Q-T29 repair after R01 RED

## Source finding

R01 found one blocking required-evidence defect, `M02Q-T29-F01`: the structured Review acceptance migration implementation was semantically fail-closed, but the frozen Card's required regression matrix was incomplete. In particular, the exact T29 delta had no Board-level `review_acceptance_migrations` uniqueness/coherence regression and no explicit negative proving that the new migration proof cannot authorize a statusless Result outside the separate T26 legacy-Result path.

R01 evidence remains immutable at `evidence/M02Q-T29_REVIEW_R01_2026-09-27.md`.

## Bounded correction

Product repository: `elmakus/project_workflow_v2`
Branch: `work/pwv21-policy-kernel`

Corrected exact product subject:

- final correction commit: `11dd88d1a1153ca63e55b567f7ba5af24cc3114b`
- tree: `512a8bdb1929f0414a0d351a03658b17b7594fc2`
- parent test-correction commit: `fd36d2b5d1479a4a15134118665cc0920671cc4a`
- base reviewed implementation: `0b1bcdf63e4198ae53ace14a69d7c792e620ed19`

The correction is test-only. Product logic and consumer historical bytes are unchanged.

Added regression coverage:

- `tests/test_state_contract.py`: a valid `review_acceptance_migrations` Board control plus duplicate-proof rejection, exact source Review-locator coherence rejection, and overlap rejection against `legacy_result_migrations`.
- `tests/test_router.py`: explicit statusless DONE Result control carrying an otherwise shape-valid structured Review acceptance migration proof; routing still fails closed with the accepted-success/legacy-Result requirement instead of allowing the T29 compatibility path to substitute for T26.

## Verification

- Exact product diff from `0b1bcdf6` to `11dd88d1` changes only `tests/test_state_contract.py` and `tests/test_router.py`.
- Remote `work/pwv21-policy-kernel` readback resolves exactly to `11dd88d1a1153ca63e55b567f7ba5af24cc3114b`.
- GitHub Actions push run `36336017258` on exact head `11dd88d1a1153ca63e55b567f7ba5af24cc3114b` completed **success**.
- The original semantic implementation at `0b1bcdf6` remains unchanged; the correction only closes the R01 required-evidence gap.
- T09-T12 consumer Review/Card/Result bytes remain untouched; downstream four-record proof population remains outside T29.
- F03 consumed-trigger migration, semicolon residual, milestone re-review and M03 remain outside this correction.

Fresh independent closure verification of `M02Q-T29-F01` is required before a fresh full-scope rediscovery can finalize T29.
