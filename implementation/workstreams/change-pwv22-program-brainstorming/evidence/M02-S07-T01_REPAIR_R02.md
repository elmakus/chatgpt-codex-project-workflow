# M02-S07-T01 — repair after R02 RED

Corrective scope is limited to the R02 immutable Result-artifact history defect.

Exact repaired implementation subject:
- commit: `b82fe7ae1c44b713d8c22ddb276b2fd4434388dd`
- `tools/pwv22_native_results.py` blob `f87c6f36153f58041d2cbf3c69379c0f8433ce0b`
- `tests/test_pwv22_native_results.py` blob `2baa2db2e41b712187a0df162c086b2591738428`

Correction:
- typed Results now require and preserve an exact `result_artifact` identity;
- dependency consumption uses that typed artifact identity and still requires the injected exact-identity verifier;
- Result-history append rejects reuse of an existing Result artifact locator in addition to duplicate Result IDs and unchanged implementation subjects;
- focused negative tests reject both a missing Result artifact and reuse of a historical Result artifact.

The prior R01 exact-identity verifier correction is preserved. S08 remains outside this repair.

Readback: both repaired implementation/test blobs were read back at the exact final product commit. GitHub reports no commit-status checks for this commit, so no executed test count is asserted here.