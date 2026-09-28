# M02-S08-T01 repair after R04 RED

R04 finding was classified as a bounded implementation defect under the unchanged Card contract.

Corrected product subject: `elmakus/project_workflow_v2@d27ad6bec471cca1cf1923f51ee5f632f9e9d6a8` on isolated contribution branch `work/pwv22-native-foundation`.

Readback:
- `tools/pwv22_parallel.py` blob `9a1118f133acf2b78777b65372a8ca48b4a91ed0`
- `tests/test_pwv22_parallel.py` blob `fcc0f96bc3af7701c2c020aa4750eb3e5ff19d21`

Correction:
- parallel legality and fan-in no longer consume caller-provided admission membership/revocation material;
- both consume an exact admission-artifact identity, verify it, read the durable admission material through a dedicated reader, and require the material's declared subject to equal that immutable identity;
- the already-durable GREEN acceptance artifact must still bind that exact admission subject;
- fabricated/non-durable admission identity cannot authorize altered membership or fan-in;
- R03 durable sibling acceptance, overlap/uncertainty serialization, one-mutator enforcement, exact ordered sibling Results and compatibility rejection remain.

No CI evidence is claimed. Exact source/test blobs and final product commit were read back. A fresh independent review is required because this context materially repaired the exact subject.
