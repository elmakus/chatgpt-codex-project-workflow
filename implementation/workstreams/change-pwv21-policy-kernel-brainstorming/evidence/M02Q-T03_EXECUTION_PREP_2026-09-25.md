# M02Q-T03 Execution Prep — RF005 Plan Review verdict domain

Approved P7 order 3 is RF005 / H007, a separate `required_seam` with no RF requirement predecessor. `M02Q-T02` RF007 is DONE with exact result `results/M02Q-T02.md@c085e144d258eed41eed630679608b6be8de97ec:181e850f8f7eee6583d4d185d4044c1952aeb30d` and independent R01 GREEN. Its downstream trigger is satisfied. The product candidate branch is `elmakus/project_workflow_v2@52fa93fe38f69e0955150b0f175e3dde8e63a8c1`; canonical workflow main remains `4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`.

The pre-M03 audit H007 showed `in_progress` accepted by the generic review domain and incorrectly falling through to the frozen Plan Review RED-correction route. Accepted Plan Review lifecycle is `pending`/`green`/`red` only; P7 requires an exhaustive fail-closed state domain. RF017 malformed durable TOML and RF004 exact acceptance binding remain separate seams. M03 is still prohibited until all 17 RF families and the distinct M02Q Milestone Review are terminal GREEN.

## Seven-dimension decomposition audit

- Independent implementability: the Plan Review verdict-domain correction is a complete useful P7 RF005 outcome without RF017/RF004 or later milestones.
- Falsifiability/testability: H007 frozen-plan `in_progress` is an exact failing fixture; `pending`, `green`, `red`, approved and editorial positive/negative controls distinguish the legal routes.
- Reviewability: one local Card Review can assess validator, router and kernel agreement for the verdict domain without certifying Plan Review acceptance binding or M02Q composition.
- Invariant/contract family: accepted verdict validation and exhaustive dispatch are inseparable facets of one Plan Review lifecycle invariant; neither is a separate consumed outcome.
- Dependency ordering: RF005 has no RF prerequisite but follows exact DONE/GREEN RF007 in P7 order; RF017 is next.
- Atomic mutation/migration: validator and frozen-plan dispatch must agree in one accepted subject to avoid an intermediate state that misroutes an unsupported verdict. Historical terminal records stay unchanged.
- Cross-surface coupling: state contract, router, kernel predicate and lifecycle documentation share this RF005-local domain; there is no cross-RF merge or milestone-review substitution.

Decision: materialize one `M02Q-T03` Card. The topology contains one independently falsifiable family, preserves P7 required seams and separate Card/Milestone reviews, and has no risky topology trigger or material plan deviation.

## Bounded write/effect scope

Only `elmakus/project_workflow_v2` branch `work/pwv21-policy-kernel` is the product target. Expected edits are Plan Review validation/routing and their focused tests/docs, not other RF mechanisms. Git commit/push and CI readback are the authorized external effects.
