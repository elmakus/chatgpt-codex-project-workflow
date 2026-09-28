# M01-S05-T01 corrective execution after R02 RED

Corrective classification: bounded Execution correction; the stable S05 Card remains valid.

Failed attempt retained:
- M01-S05-T01-R02: RED
- evidence: implementation/workstreams/change-pwv22-program-brainstorming/evidence/M01-S05-T01-R02.md

Corrected product subject:
- repository: elmakus/project_workflow_v2
- branch: work/pwv22-native-foundation
- commit: 6a04e864964eac54246b6cbfd46d6a621593e3ba
- tools/pwv22_native_foundation.py blob: 88612bd5da9f77cf01707ebf2f27de22e6b90c94
- tests/test_pwv22_native_foundation.py blob: 48e52514046f7f219af6194cd2d7617d3a258e67

Correction:
- exact locator now derives repository identity from the configured Git remote and requires it to match both the declared tuple and caller expectation;
- exact locator reads the canonical remote ref and requires the locator commit to be reachable from that published head;
- path validation rejects backslashes;
- tree-entry validation rejects Git symlinks instead of accepting their blob payload;
- focused adversarial coverage now includes wrong derived repository identity, backslash, symlink and local-only/unpublished commit rejection;
- prior Git-native force-with-lease CAS/readback implementation remains unchanged.

Verification:
- GitHub Actions run 36476886552 for exact corrected commit 6a04e864964eac54246b6cbfd46d6a621593e3ba completed SUCCESS.
- Product main was not modified.
- Correction remained confined to the two S05 product files.

A fresh independent exact-subject Review is required.