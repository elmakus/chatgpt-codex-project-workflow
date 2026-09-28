# M02-S08-T01 Repair after R08 RED

Classification: bounded correction inside accepted S08 authority.

R08 finding corrected: mutating ownership is no longer invocation-local. The finite accepted admission now binds every admitted Card ID to both its exact immutable Card subject and one non-empty durable `mutating_owner` domain. Admission parsing requires the owner map to exactly cover the finite Card set. `parallel_legal()` requires each claim's mutating owner to equal the durable admitted owner before parallel authorization.

Exact corrected implementation subject: `elmakus/project_workflow_v2@6e67e3b0f528434d00e07ddd3df21de75fe9477a`; `tools/pwv22_parallel.py` blob `89a47b37b1c3934f2153cf91c91db69023a33a40`; `tests/test_pwv22_parallel.py` blob `61bfb33c7962d089a8ec1debf25a59d2a323af50`.

Focused regression added: one operation using the admitted owner remains legal, while a later/separate operation for the same exact admitted Card subject using a different owner is rejected. Invalid/incomplete admission owner bindings are also rejected. Existing exact subject verification, stale/revoked/non-admitted rejection, overlap/uncertainty serialization, sibling acceptance and fan-in protections are retained.

Publication/readback of both corrected blobs succeeded. No CI execution evidence is claimed by this correction context. Fresh independent review is required.
