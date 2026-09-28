# M02-S08-T01 repair after R02 RED

R02 finding was classified as a bounded implementation defect under the unchanged Card contract.

Corrected product subject: `elmakus/project_workflow_v2@c42f3bf05ef1a653776a9adc46b74a3ffbdd1ce4` on isolated contribution branch `work/pwv22-native-foundation`.

Readback:
- `tools/pwv22_parallel.py` blob `20225f74cc1b1fe51bf5ec55e1987066bf08b425`
- `tests/test_pwv22_parallel.py` blob `4b70f430fc6c39e50e326a91753735938b474719`

Correction:
- admission acceptance is no longer accepted as a caller-provided verdict mapping;
- legality/fan-in receive an exact immutable acceptance-artifact identity and obtain its contents only through the durable acceptance reader;
- absent/fabricated acceptance identity fails closed before a GREEN verdict can authorize work;
- exact admission-subject binding, stale/RED rejection, revocation, conservative overlap/uncertainty serialization, one-mutator enforcement and ordered fan-in remain intact;
- focused negative coverage proves a fabricated in-memory/non-durable acceptance identity cannot authorize either parallel legality or fan-in.

GitHub combined status for the correction commit has no reported checks; no CI evidence is claimed. Exact source/test blobs were read back. A fresh independent review is required because this context materially repaired the exact subject.
