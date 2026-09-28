# M02-S08-T01-R09 Independent Review Evidence

Verdict: RED

Exact reviewed Result: `implementation/workstreams/change-pwv22-program-brainstorming/results/M02-S08-T01.md@0eba7baaafad4670c251e6965dabbc8345aa7fb9:c9ead93d22e7a30c482913c2d6ef21cca3ea377d`

Exact implementation subject: `elmakus/project_workflow_v2@6e67e3b0f528434d00e07ddd3df21de75fe9477a`; `tools/pwv22_parallel.py` blob `89a47b37b1c3934f2153cf91c91db69023a33a40`; `tests/test_pwv22_parallel.py` blob `61bfb33c7962d089a8ec1debf25a59d2a323af50`.

## Independence

This fresh review context did not materially produce or repair the exact R09 subject. It independently inspected the frozen Result, the R08 finding/correction, implementation and focused tests against the stable Task Card acceptance surface.

## Finding

The R08 correction is incomplete at fan-in.

The accepted admission now durably binds every admitted Card to one non-empty `mutating_owner`, and `parallel_legal()` correctly rejects claims whose owner differs from that binding. However, `compatible_fan_in()` accepts no claim/owner operand and never checks `a["mutating_owners"]`. It verifies admitted exact Card subjects and accepted exact sibling Results, then delegates only semantic compatibility of those Results.

Therefore a sibling Result can reach fan-in without fan-in proving that the mutation which produced that sibling was owned by the admission-bound mutating domain. The focused regression `test_durable_admission_owner_rejects_later_different_mutator` exercises only `parallel_legal()`; no fan-in test demonstrates rejection of a sibling whose production ownership disagrees with the durable admission owner.

This fails the explicit R08 required correction: require claim consumption to match the durable owner binding before parallel legality **or fan-in** can authorize work. It also leaves the Task Card's one-mutating-owner invariant unenforced at the composition boundary.

## Required correction

Make fan-in consume an exact durable ownership/claim proof for every sibling (or equivalent immutable Result-bound proof) and verify that each proof matches the admitted exact Card subject and its admission-bound `mutating_owner` before compatibility can succeed. Add a focused negative test where exact sibling Result/acceptance identities are otherwise valid but a sibling's production owner differs from the durable admission binding; fan-in must reject it. Preserve the existing exact ordered sibling Result, stale acceptance, revocation, exact-subject and compatibility protections.
