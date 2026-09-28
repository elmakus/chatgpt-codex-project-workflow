# M02-S08-T01 Repair after R09 RED

Classification: bounded correction inside accepted S08 authority.

R09 finding corrected: fan-in now consumes one ownership/claim proof per exact sibling and verifies that the proof's Card ID and exact immutable Card subject match the sibling, and that its `mutating_owner` equals the durable owner bound by the accepted admission. Fan-in therefore cannot authorize composition solely from exact Result/acceptance identities while bypassing the admission-bound mutation owner.

Exact corrected implementation subject: `elmakus/project_workflow_v2@1c704352cb814f8b948570409578ab349010d07c`; `tools/pwv22_parallel.py` blob `69f89a665dfc68211acfc1bf97e92433d83a6d45`; `tests/test_pwv22_parallel.py` blob `dc26b8e5fdcef29e39caec4b32ac06c71c595199`.

Focused regression added: otherwise-valid fan-in with exact sibling Results/acceptances is rejected when one sibling ownership proof uses a mutating owner different from the durable admission binding. Existing exact subject, stale/revoked/non-admitted, ordered sibling Result and compatibility checks are retained in the focused fixture.

Publication/readback of the corrected branch files succeeded. No CI execution evidence is claimed by this correction context. Fresh independent review is required.
