# M02-S07-T01 — repair after R03 RED

Corrective scope is limited to the R03 affected-cone freshness defect.

Exact repaired implementation subject:
- commit: `de6ce5ab6065fa223538a2a825781381f057f171`
- `tools/pwv22_native_results.py` blob `4d5dea6eeabafc9e6e09229b97286c31c26f8106`
- `tests/test_pwv22_native_results.py` blob `fd181e84f1038e78fb3ae51e00a8d31b667289a9`

Correction:
- `affected_results()` now computes a deterministic fixed point over exact Result-artifact identities;
- when a Result becomes affected, its exact Result artifact becomes an affected input for downstream Results;
- a focused regression covers `A -> R1 -> R2` and proves an unrelated Result remains unaffected;
- the prior R01 exact-identity verifier and R02 immutable Result-artifact corrections are preserved.

S08 remains outside this repair.

Readback: the repaired implementation/test blobs were published on `work/pwv22-native-foundation` at the exact commit above. No executed test count is asserted here.
