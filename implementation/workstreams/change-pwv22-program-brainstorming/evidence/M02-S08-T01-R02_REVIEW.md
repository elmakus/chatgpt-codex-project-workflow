# M02-S08-T01-R02 Independent Review Evidence

Verdict: RED

Exact reviewed Result: `implementation/workstreams/change-pwv22-program-brainstorming/results/M02-S08-T01.md@b9f065b7994986e44e3a5cc5e61fb982a2ec34ec:f690070e3d8469af22ff3171b47ea4ed65373c3d`

Exact implementation subject: `elmakus/project_workflow_v2@11c13b1c62ed4d902d5b153c02ac67f98a187387`.

## Finding

R01 required parallel legality and fan-in to bind to an exact **accepted** finite-admission fact. The repair verifies the admission subject Git identity and compares the supplied acceptance's `subject` to that identity, but the acceptance itself remains an unauthenticated caller-provided mapping.

`accepted_admission()` accepts any mapping containing `{"verdict":"green","subject":<admission subject>}`; it does not bind or verify an exact durable acceptance artifact/fact. The focused tests demonstrate this gap by constructing `acc(ADM)` entirely in memory and using it as sufficient authorization. A caller that knows a valid admission subject can therefore fabricate GREEN and make `parallel_legal()` or `compatible_fan_in()` accept work without a durable accepted-admission fact.

This leaves the Card acceptance and R7 requirement 54 unsatisfied. The R01 defect is narrowed but not closed.

## Required correction

Make admission acceptance itself exact and durable: bind the acceptance operand to a verifiable immutable identity/fact (or the native accepted-fact primitive that owns this contract), verify that identity before trusting its GREEN verdict, and add a negative test proving that a fabricated in-memory GREEN mapping for an otherwise valid admission subject cannot authorize parallel legality or fan-in. Preserve the existing stale/RED/revoked/non-admitted and conservative conflict checks.
