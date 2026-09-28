# M02-S07-T01 — repair after R01 RED

Corrective scope is limited to the R01 acceptance-identity defect.

Exact repaired implementation subject:
- commit: `bab5c53d62d435c3f00af8cc0f611f0b9225e761`
- `tools/pwv22_native_results.py` blob `7a3fab3ae7e653491adb993879a2119faf1e52a9`
- `tests/test_pwv22_native_results.py` blob `224fe3be19cdc349463e6c2c304bba550f1df383`

Correction:
- accepted dependency consumption now requires an identity verifier and applies it to the Result artifact, implementation subject and every material input before GREEN acceptance can authorize consumption;
- readiness/frontier propagate the same verifier;
- a focused negative test rejects a consistently matching but unverifiable locator.

The verifier is intentionally injected: the accepted S05 foundation already owns the concrete Git proof primitive (`exact_blob`), while S07 remains runtime-neutral and does not duplicate repository access policy.

Readback: product branch `work/pwv22-native-foundation` resolves to the repaired commit and both repaired blobs were read back from that commit. No executed test count is asserted in this environment.
