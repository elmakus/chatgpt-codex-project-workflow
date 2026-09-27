# M02Q-T26 repair after R01 RED

## Source finding

R01 found one blocking provenance defect: `verify_legacy_result_migration` accepted a historical source Board whose `cards.result.commit` was dangling/off-history as long as path/blob matched. That violated the T26 exact immutable source-identity and fail-closed acceptance.

R01 evidence is preserved at `evidence/M02Q-T26_REVIEW_R01_2026-09-27.md`; the failed reviewed subject remains immutable.

## Bounded product correction

Product repository: `elmakus/project_workflow_v2`
Branch: `work/pwv21-policy-kernel`

Corrected exact product subject:

- final correction commit: `4ebe6b6a17ba4b22c9221c519db175ed71ee4995`
- tree: `f899e7850a1ad6805e4d79dc693a9f4d020593f0`
- corrected `tools/legacy_result_provenance.py` blob: `a75a2c7cd5fd6fe314a2a5d5626347947d582361`
- corrected `tests/test_legacy_result_provenance.py` blob: `40abb6a53f779da639362aed2597470f11511c43`

The correction now proves the Result locator recorded by the historical source Board as an actual exact Git `commit:path@blob` subject and additionally requires that Result commit to be an ancestor of the immutable source Board snapshot. Dangling and off-history Result commits therefore fail closed before legacy statusless serving can be authorized.

A publication-only intermediate commit `0a7e6c4425ea37226e6e6508cd463a9284f26f03` accidentally contained a tool-output footer in the two edited files and failed exact-remote compilation. It is preserved as history but is not an accepted implementation subject. `4ebe6b6a...` repairs that publication artifact and is the sole corrected T26 product subject.

## Verification

- focused legacy provenance suite: **6/6 GREEN**;
- new negative matrix: dangling source-Board Result commit rejected; off-history exact Result commit rejected;
- independent reproduction probe that previously returned `BUG_REPRODUCED=YES` now returns `BUG_STILL_PRESENT=NO` with an exact dangling-locator rejection;
- exact remote clean-tree `scripts/test.sh`: **1204/1204 GREEN**, M01 baseline PASS, exit 0;
- `git diff --check`: GREEN;
- remote branch readback: `work/pwv21-policy-kernel -> 4ebe6b6a17ba4b22c9221c519db175ed71ee4995`;
- GitHub Actions exact-head run `36319205407`: completed / **success**.

The repair remains inside the frozen M02Q-T26 acceptance. No consumer historical Result bytes were rewritten, no 23-record consumer migration was materialized, no consumed-trigger migration was performed, and M03 remains unmaterialized.
