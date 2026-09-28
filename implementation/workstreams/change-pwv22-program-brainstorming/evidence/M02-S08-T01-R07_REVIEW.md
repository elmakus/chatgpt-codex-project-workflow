# M02-S08-T01-R07 Independent Review Evidence

Verdict: RED

Exact reviewed Result: `implementation/workstreams/change-pwv22-program-brainstorming/results/M02-S08-T01.md@71cc9e162eaa5acc9664926312d3fcd3e0e3177a:6c2e0b5d3ed31d8af029f2284d0347f19041e964`

Exact implementation subject: `elmakus/project_workflow_v2@f7677652ec447a952ef9e026d95572747ff55e8f`; `tools/pwv22_parallel.py` blob `cc1d4b54307848c0b2607dcbc6d4643be2dee125`; `tests/test_pwv22_parallel.py` blob `a43f8f6a6ae07a165dac7075f0b771e156bc9f8b`.

## Finding

The R06 repair binds each admitted Card ID to an exact-identity-shaped subject locator, but it never verifies that any admitted Card subject locator is durable or real.

`typed_admission()` normalizes `subjects[cid]` only with `exact_identity()`, which checks field presence but not repository material. `accepted_admission()` calls `verify_identity()` for the admission artifact itself, then returns the admission without verifying any `a["subjects"]` member. `parallel_legal()` and `compatible_fan_in()` subsequently authorize a Card subject solely by equality with that unverified stored locator.

The focused fixture makes the gap explicit: `verify()` accepts only `A`, `B`, and `ADM`; the admitted Card subjects `CA` and `CB` are never accepted by the verifier, yet disjoint parallel legality and compatible fan-in pass. Therefore a durable GREEN admission can contain a fabricated/non-durable Card-subject locator, and caller operands that repeat that fabricated locator can be treated as exactly admitted.

This fails the Card requirement for explicit finite exact admission and the R06 correction requirement that every admitted member bind to an exact immutable subject identity. Equality of an identity-shaped mapping is not proof that the subject is an immutable durable subject.

## Required correction

When consuming an accepted admission, verify every admitted Card subject identity with the exact durable identity verifier (or an equivalent authoritative material read) before it can authorize parallel work or fan-in. Add focused negative tests proving that a fabricated/non-durable admitted Card subject is rejected even when the claim/fan-in operand exactly repeats that locator. Preserve stale-subject rejection and all prior R03-R06 protections.
