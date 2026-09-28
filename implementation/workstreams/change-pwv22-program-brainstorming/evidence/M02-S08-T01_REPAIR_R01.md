# M02-S08-T01 repair after R01 RED

R01 finding was classified as a bounded implementation defect under the unchanged Card contract.

Corrected product subject: `elmakus/project_workflow_v2@11c13b1c62ed4d902d5b153c02ac67f98a187387` on isolated contribution branch `work/pwv22-native-foundation`.

Readback:
- `tools/pwv22_parallel.py` blob `04c7f76d615dc114d3be7269e3f78eb0441461f0`
- `tests/test_pwv22_parallel.py` blob `95c787bdfbda38a80235763233c15d3585173459`

Correction:
- admission now carries an exact Git subject;
- `accepted_admission` verifies that exact subject and requires GREEN acceptance bound to it;
- `parallel_legal` cannot authorize from an unaccepted/stale admission;
- `compatible_fan_in` requires the same accepted admission and rejects revoked/non-admitted sibling Card IDs before consuming Results;
- focused tests add stale/RED admission and revoked/non-admitted fan-in negatives.

No host/package/live external mutation was performed. No GitHub Actions run exists for the correction commit; acceptance therefore relies on exact source/test readback plus the required fresh independent Review.
