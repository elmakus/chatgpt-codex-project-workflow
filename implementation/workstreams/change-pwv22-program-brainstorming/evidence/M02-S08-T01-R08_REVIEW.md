# M02-S08-T01-R08 Independent Review Evidence

Verdict: RED

Exact reviewed Result: `implementation/workstreams/change-pwv22-program-brainstorming/results/M02-S08-T01.md@21293712559790a2637352df7b2afe944911f9d4:c5a9f5f3ca297f827a1f14fbdb0ac192306dfa65`

Exact implementation subject: `elmakus/project_workflow_v2@eb4cba175318035c8308f39f4d9abbeca3252214`; `tools/pwv22_parallel.py` blob `7bb3de41c15293e2847138b881f0cddbf6ebfd23`; `tests/test_pwv22_parallel.py` blob `fe7d64f89d026dae95706660f03bf50d57a39c6b`.

## Independence

This fresh review context did not materially produce or repair the exact R08 subject. It independently inspected the frozen Result, implementation and focused tests against the stable Task Card acceptance surface.

## Finding

The implementation does not durably enforce the Card acceptance requirement that each Card have one mutating ownership domain.

`typed_claims()` accepts an arbitrary non-empty `mutating_owner` string supplied by the caller. The accepted finite admission binds Card IDs to exact immutable Card subjects, but it binds no mutating-owner identity/domain. `one_mutating_owner()` only compares owner strings among the claim records supplied to that single invocation. Consequently `one_mutating_owner([claims("a","x")])` is true and, in a later independent operation, `one_mutating_owner([claims("a","y")])` is also true for the same admitted exact Card subject. Nothing in `parallel_legal()` or `compatible_fan_in()` binds either owner to durable admission/authority state.

This makes the invariant invocation-local rather than Card-local. Two distinct mutators can therefore each independently present a singleton or otherwise non-conflicting claim set and both satisfy the purported one-owner gate for the same Card. The current focused test only proves disagreement is rejected when both owner claims are simultaneously supplied in one sequence; it does not prove one authoritative mutating owner per admitted Card.

That violates the Task Card acceptance surface: "each Card has one mutating ownership domain."

## Required correction

Bind the mutating ownership domain for every admitted Card to durable exact admission/authority material (or an equivalent exact immutable owner binding), and require claim consumption to match that binding before parallel legality or fan-in can authorize work. Add a focused negative test showing that the same admitted exact Card subject cannot be accepted under a different mutating owner in a later/separate operation, while preserving the existing overlap/uncertainty, revocation, exact-subject, stale-acceptance and fan-in protections.
