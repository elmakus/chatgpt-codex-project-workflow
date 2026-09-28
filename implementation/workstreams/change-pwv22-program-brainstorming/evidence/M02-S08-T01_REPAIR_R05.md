# M02-S08-T01 repair after R05 RED

R05 finding was classified as a bounded implementation defect under the unchanged Card contract.

Corrected product subject: `elmakus/project_workflow_v2@1348a6b7c1649c151e5f216520dbf67aafb096e5` on isolated contribution branch `work/pwv22-native-foundation`.

Readback:
- `tools/pwv22_parallel.py` blob `1f3a1e155ecfbf3792ef90d0627e02b027778605`
- `tests/test_pwv22_parallel.py` blob `dc527b38c201ada9c1536fd7a3f6b9b4a755eae4`

Correction:
- admission payload no longer embeds its own Git repository/commit/path/blob identity;
- the external exact immutable admission locator is verified and used to read the durable payload;
- the durable GREEN admission acceptance binds that external exact locator directly;
- finite cards/revocations remain payload semantics and fabricated/non-durable locators still fail closed;
- a focused test serializes a self-reference-free admission payload, computes its real Git blob SHA, binds that hash through the external locator, and rejects a tampered locator;
- R03/R04 protections, conservative conflict serialization, one-mutator enforcement, exact ordered sibling Results and compatibility rejection remain.

No CI evidence is claimed. Exact source/test blobs and final product commit were read back. A fresh independent review is required because this context materially repaired the exact subject.
