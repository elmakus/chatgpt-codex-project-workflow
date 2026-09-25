# M02Q-T04 Execution Prep — RF017 malformed durable TOML Recovery

Approved P7 order 4 is RF017 / H030, a separate `required_seam` with no RF requirement predecessor. `M02Q-T03` RF005 is DONE with exact Result `results/M02Q-T03.md@96a226cb061210e9ead4bc2599937e4ecfffdefc:1673579041ea1e4bd086d89c4a2cd64e6506703b` and fresh independent R01 GREEN; its trigger is satisfied. The product candidate branch is `elmakus/project_workflow_v2@b47e1bc88e0497d2828ece4b873b0440a86a2ad1`. Canonical workflow main remains `4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`.

The pre-M03 audit H030 showed malformed Board and Workstream TOML escaping `select_route` as `tomllib.TOMLDecodeError`; valid controls routed and parseable semantic-invalid controls recovered. The audit's other selector-owned TOML surfaces share the read boundary but were only inspected statically, so implementation verification must cover representative siblings. P7 and REQ-092/093 authorize fail-closed Recovery, independent from the next RF002 promotion-precedence seam. M03 is prohibited until all 17 RF families and the separate M02Q Milestone Review are terminal GREEN.

## Seven-dimension decomposition audit

- Independent implementability: a durable TOML parser-normalization correction is a complete, useful RF017 outcome without RF002 or any other seam.
- Falsifiability/testability: H030's `revision = [` Board and Workstream fixtures fail before correction; valid, semantic-invalid and additional malformed selector-record controls distinguish the legal outcome.
- Reviewability: one local independent Card Review can assess read-boundary and router behavior without certifying later precedence, exact acceptance or milestone composition.
- Invariant/contract family: every selector-owned durable TOML parse failure must enter the same deterministic Recovery boundary; splitting each TOML file into a separate Card would fragment this one invariant.
- Dependency ordering: RF017 has no RF prerequisite but follows exact DONE/GREEN RF005 in the accepted serial P7 order; RF002 is next.
- Atomic mutation/migration: parser normalization and selector handling must agree in one accepted product subject to avoid leaking an exception from any read path. No historical record migration or rewrite is authorized.
- Cross-surface coupling: state-contract TOML reading, selector catches and focused tests share this RF017-local behavior; there is no cross-RF merger.

Decision: materialize one `M02Q-T04` Card with simple card-local topology. One independently falsifiable parser-family outcome, no preferred-seam merger, milestone absorption, review substitution or material strategy deviation.

## Bounded write/effect scope

Only `elmakus/project_workflow_v2` branch `work/pwv21-policy-kernel` is the product target. Expected edits are durable TOML read/selector normalization and focused tests/docs if necessary. Git commit/push and exact-head CI readback are authorized external effects.
