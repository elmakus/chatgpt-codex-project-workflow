# M02-S07-T01 — repair after R05 RED

Corrective scope is limited to restoring the R01 forged-locator negative regression and producing required executed-test evidence.

Exact repaired implementation subject:
- commit: `9cb2ebabad79c07b81fac4317ef159b44e8fe98d`
- `tools/pwv22_native_results.py` blob `4d5dea6eeabafc9e6e09229b97286c31c26f8106`
- `tests/test_pwv22_native_results.py` blob `e1e3b29d53c91d66ba135193eb7c2074999d8561`

Observed failure on prior exact subject `0fbaed93e2632fdf07d7030aeb0e36a850971e2d`:
- command: `python3 -m unittest -v tests.test_pwv22_native_results`
- outcome: 9 tests run; 8 passed, 1 failed.
- failure: `test_consistently_forged_locator_fails_closed` no longer raised because R04 had made identity D valid in the shared verifier while the older negative test still used D as its forged identity.

Correction:
- implementation code remains byte-identical;
- introduced identity E solely as the deliberately unverifiable forged locator;
- retained D as the genuinely unrelated valid identity for the R04 affected-cone regression.

Final execution/readback:
- fetched remote `work/pwv22-native-foundation` at exact commit `9cb2ebabad79c07b81fac4317ef159b44e8fe98d`;
- clean reset/readback to that remote-published commit;
- command: `python3 -m unittest -v tests.test_pwv22_native_results`;
- outcome: 9 tests run, 9 passed, OK;
- exact implementation and test blobs were read back from GitHub at the final commit.

S08 remains outside this repair and may not consume S07 until the required acceptance boundary is satisfied.
