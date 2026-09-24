# M02-T01 bounded correction after Milestone Review R01 — 2026-09-24

## Trigger

Independent full-scope Milestone Review `M02-MILESTONE-R01` returned RED for one bounded M02 defect in exact implementation subject `af8610dda5b8efa9be5083bad1dac5b6ec596003`: governed mutation pre/postcondition verification used Python equality, allowing JSON boolean/integer coercion such as `true == 1`.

## Bounded correction

Target repository: `elmakus/project_workflow_v2`  
Target branch: `work/pwv21-policy-kernel`  
Pre-correction subject: `af8610dda5b8efa9be5083bad1dac5b6ec596003`  
Repaired subject: `6e5ce957e3775fc20887e8112dae60a9af21cb8b`

Correction stayed entirely inside M02:

- mutation precondition/postcondition readback now compares canonical JSON bytes, preserving JSON type identity;
- boolean/integer mismatch regression coverage was added for both precondition and postcondition verification;
- the human-readable M02 execution contract now states the type-exact equality rule.

No M03 artifact or behavior was added.

## Exact CI/readback

GitHub Actions workflow `test`, run #380 / ID `35945949883`, exact `head_sha=6e5ce957e3775fc20887e8112dae60a9af21cb8b`:
- status: `completed`;
- conclusion: `success`;
- job `test` ID `107463786777`: `success`;
- dedicated M02 typed-contract suite: 13 tests, all GREEN;
- full discovered suite: 185 tests, all GREEN;
- final `M01 baseline checks: PASS`.

## Review consequence

The correction changes the exact M02 implementation subject. The current context materially performed this repair and is therefore ineligible to issue the required independent Card-review verdict on the repaired subject. A new append-only Card review attempt is required before the separate Milestone re-review. The `after-M02-T01` JIT trigger remains `waiting`, and M03 must not be materialized.
