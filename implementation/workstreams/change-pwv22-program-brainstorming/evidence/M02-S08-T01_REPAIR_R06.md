# M02-S08-T01 repair after R06 RED

R06 finding was classified as a bounded implementation defect under the unchanged Card contract.

Corrected product subject: `elmakus/project_workflow_v2@f7677652ec447a952ef9e026d95572747ff55e8f` on isolated contribution branch `work/pwv22-native-foundation`.

Readback:
- `tools/pwv22_parallel.py` blob `cc1d4b54307848c0b2607dcbc6d4643be2dee125`
- `tests/test_pwv22_parallel.py` blob `a43f8f6a6ae07a165dac7075f0b771e156bc9f8b`

Correction:
- every finite admission now binds each Card ID to an exact immutable subject locator;
- claims carry that exact subject and parallel legality rejects a changed subject under the same Card ID;
- fan-in receives the exact sibling Card-subject set and rejects stale/mismatched subjects before Result acceptance/compatibility;
- focused stale-subject tests cover both parallel legality and fan-in;
- the R03-R05 durable admission, stale/fabricated acceptance, overlap/uncertainty serialization, one-mutator, exact ordered Result and compatibility protections remain.

No CI evidence is claimed. Exact source/test blobs and final product commit were read back. A fresh independent review is required because this context materially repaired the exact subject.
