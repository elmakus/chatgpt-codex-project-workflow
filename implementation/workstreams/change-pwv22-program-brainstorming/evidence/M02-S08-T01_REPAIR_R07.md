# M02-S08-T01 repair after R07 RED

R07 finding was classified as a bounded implementation defect under the unchanged Card contract.

Corrected product subject: `elmakus/project_workflow_v2@eb4cba175318035c8308f39f4d9abbeca3252214` on isolated contribution branch `work/pwv22-native-foundation`.

Readback:
- `tools/pwv22_parallel.py` blob `7bb3de41c15293e2847138b881f0cddbf6ebfd23`
- `tests/test_pwv22_parallel.py` blob `fe7d64f89d026dae95706660f03bf50d57a39c6b`

Correction:
- accepted finite admission now verifies every admitted Card subject through the exact durable identity verifier before the admission can authorize work or fan-in;
- focused negative coverage injects a fabricated/non-durable admitted subject and requires both parallel legality and fan-in to fail closed even when operands repeat that locator;
- stale-subject fencing and prior admission/acceptance, overlap/uncertainty, one-mutator, exact ordered Result and compatibility protections remain.

No CI evidence is claimed. Exact source/test blobs and final product commit were read back. A fresh independent review is required because this context materially repaired the exact subject.
