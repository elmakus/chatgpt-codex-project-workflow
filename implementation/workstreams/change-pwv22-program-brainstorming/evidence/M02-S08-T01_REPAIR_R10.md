# M02-S08-T01 Repair after R10 RED

Classification: bounded correction inside accepted S08 authority.

R10 finding corrected: the stale-card-subject fan-in regression now supplies the required sibling ownership/claim proofs introduced by the R09 correction. The call therefore reaches `compatible_fan_in()` and exercises fail-closed rejection of the stale expected Card subject instead of failing at Python argument binding.

Exact corrected implementation subject: `elmakus/project_workflow_v2@44a146fe99dd8b83435edc220adaeb782a7462f1`; `tools/pwv22_parallel.py` blob `69f89a665dfc68211acfc1bf97e92433d83a6d45`; `tests/test_pwv22_parallel.py` blob `7afaff82c61157f071da82b5cc0bcac534b55399`.

The corrected product branch and exact blobs were read back. The R09 fan-in ownership-proof implementation and its focused mismatch regression are unchanged. No CI execution evidence is claimed by this correction context. Fresh independent review is required.
