# M02-S07-T01 — repair after R04 RED

Corrective scope is limited to the R04 false-unrelated test fixture.

Exact repaired implementation subject:
- commit: `0fbaed93e2632fdf07d7030aeb0e36a850971e2d`
- `tools/pwv22_native_results.py` blob `4d5dea6eeabafc9e6e09229b97286c31c26f8106`
- `tests/test_pwv22_native_results.py` blob `e0609645a18c4105540903cfb604bbea27eca0d2`

Correction:
- preserved the R03 fixed-point implementation unchanged;
- introduced independent identity D into the test fixture/verifier;
- changed the nominally unrelated Result to artifact/material D, so it is genuinely outside the A -> R1(B) -> R2(C) affected cone;
- exact commit diff readback shows only this bounded test-fixture correction.

No test execution count is asserted because this repair context has repository read/write/readback capability but no execution-runner evidence. S08 remains outside this repair.
