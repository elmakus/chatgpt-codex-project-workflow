# M02-S08-T01-R04 Independent Review Evidence

Verdict: RED

Exact reviewed Result: `implementation/workstreams/change-pwv22-program-brainstorming/results/M02-S08-T01.md@9e716212f6b13cefb3d3168d8c9baa2252674fdf:47b50c8aab150f666eb37fec9f4237db469dc70f`

Exact implementation subject: `elmakus/project_workflow_v2@b0bef6622dc6d5b1404c518ef4444554d93b31f2`; `tools/pwv22_parallel.py` blob `cf1e93e6f08f682d4ce73be38de84fabfaedad12`; `tests/test_pwv22_parallel.py` blob `eafba11abad965a50079a5c652001afe588e110e`.

## Finding

R03 repair correctly stopped trusting caller-provided sibling GREEN mappings and now reads exact sibling acceptance-artifact identities durably. The finite admission fact itself is still not bound to durable admission material.

`accepted_admission()` receives the admission record as a caller-provided mapping. It validates the record with `typed_admission()`, verifies only the record's declared `subject` Git identity, then reads a durable acceptance artifact and checks that its GREEN subject equals that declared identity. It never reads the admission record from the declared immutable subject nor proves that the caller-provided `cards` / `revoked` fields are the bytes/material accepted under that subject.

Consequently, a caller can take a real accepted admission subject plus its real durable GREEN acceptance, manufacture a different in-memory admission mapping with the same `subject` but altered `cards` or `revoked`, and have `parallel_legal()` / `compatible_fan_in()` treat the altered membership as accepted. The focused tests do not cover this substitution.

This leaves the Card's “explicit finite exact admission” acceptance property and R7 requirement 54 (“explicit finite accepted admission fact for the exact Cards/subjects involved”) unsatisfied. Verifying that an identity exists is not equivalent to binding the semantic admission payload to the immutable accepted artifact.

## Required correction

Make the admission payload itself durable/exact-subject-bound before using its membership or revocation fields: read/derive the admission material through an immutable identity/material reader (or equivalent native primitive) and verify that the accepted subject is exactly that material. Do not trust caller-supplied `cards` / `revoked` under a separately verified subject identity.

Add negative coverage proving that, with a real accepted admission subject and real durable GREEN acceptance, altering the caller-provided admission membership/revocation cannot authorize a card or fan-in that the durable admission did not authorize. Preserve the R03 durable sibling-acceptance fix, conservative conflict serialization, one-mutator enforcement, exact ordered sibling Results and compatibility rejection.
