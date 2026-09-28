# M02-S08-T01-R03 Independent Review Evidence

Verdict: RED

Exact reviewed Result: `implementation/workstreams/change-pwv22-program-brainstorming/results/M02-S08-T01.md@15a81197fc4b7e5002da54d38021dc9773d8f143:26a29e1b6cf18ee9b82931149eeae6b812f21d19`

Exact implementation subject: `elmakus/project_workflow_v2@c42f3bf05ef1a653776a9adc46b74a3ffbdd1ce4`.

## Finding

R02 correctly made the finite-admission acceptance an exact durable artifact read through `read_acceptance`. The sibling Result acceptance boundary in `compatible_fan_in()` remains caller-authorized, however: the function receives `acceptances: Mapping[str, Mapping]` and passes each in-memory mapping directly to `accepted_dependency()`. That helper checks only `verdict == "green"` and subject equality; it does not verify or read an immutable acceptance artifact.

A caller that knows the expected sibling Result identity can therefore fabricate `{"verdict":"green","subject":expected}` for each sibling and pass fan-in without durable constituent acceptance. The focused tests themselves do exactly this via `{"ra":acc(A),"rb":acc(B)}`. This leaves the Card requirement that sibling fan-in consume exact accepted Result identities, R7 requirement 17 (constituent required Reviews remain required), and the composed R03 acceptance surface unsatisfied.

## Required correction

Bind each sibling acceptance operand to an exact immutable acceptance-artifact identity, read it through the durable acceptance reader before trusting GREEN, and then apply the existing exact-subject constituent check. Add a negative test proving a fabricated/non-durable sibling GREEN cannot authorize fan-in. Preserve exact sibling Result identity/order, admission acceptance/revocation, compatibility and conservative conflict behavior.
