# M02Q-T05 Execution Prep — RF002 split, promotion entry gate

Approved P7 order 5 is RF002 / H002,H022, a `required_seam` with no RF requirement predecessor. `M02Q-T04` RF017 is DONE with exact Result `results/M02Q-T04.md@f9799ca25c65db079bc40852bc63721316764355:66ae632e15ad99a91cb0321256b200880ae884fb` and fresh independent R01 GREEN; its trigger is satisfied. The product candidate is `elmakus/project_workflow_v2@8c3c751751e5d954f2aba2aa3b7b9b6d54f5fc30`; canonical workflow main remains `4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`.

The pre-M03 audit found two separable RF002 outcomes. B1/B2 showed `active` or `ready_for_definition` Brainstorming with exact authorization incorrectly entering active Definition; A1/A2 showed an explicit Brainstorming user stop shadowed by downstream Definition. The former is this Card's entry invariant. The latter has a real downstream JIT allocation at `after-M02Q-T05`, to be materialized as a distinct Card after this result is DONE/GREEN. P7 and V2 Brainstorming/Definition/User Stop with REQ-077/106/107 are the accepted authority; the audit is defect evidence, not a separate scope approval. M03 remains blocked until all 17 RF families and the separate M02Q Milestone Review are terminal GREEN.

## Seven-dimension decomposition audit

- Independent implementability: promoted-state-plus-exact-authorization gating can be corrected and remain useful even while explicit-stop precedence remains RED; the stop can be corrected later without invalidating this gate.
- Falsifiability/testability: B1/B2 active/ready with exact authorization distinguish forbidden Definition entry from valid promoted/exact authorization; A1/A2 remain separately falsifiable for the downstream stop Card.
- Reviewability: one Card Review can certify only promotion entry and its negative siblings, while a separate review judges explicit stop precedence; neither substitutes for the composed M02Q Milestone Review.
- Invariant/contract family: Definition entry requires a coherent Brainstorming promotion/authorization/source binding. Explicit stop precedence is a different owner-ordering invariant, not a file or test-step split.
- Dependency ordering: RF002 has no RF prerequisite but follows exact DONE/GREEN RF017 in P7 serial order; stop precedence follows this Card by its JIT trigger, then RF016 is next.
- Atomic mutation/migration: correcting the promotion gate first produces a safe fail-closed intermediate state for contradictory records; valid promoted Definition continues. No historical migration or rewrite is needed.
- Cross-surface coupling: Brainstorming validation and Definition router entry share this Card's gate; user-stop owner ordering is separately consumable and remains outside this Card.

Decision: split RF002 into two meaningful Cards. `M02Q-T05` retains promotion-entry gating and the real unconsumed `after-M02Q-T05` JIT trigger owns explicit-stop precedence. Simple card-local topology holds because each Card owns one invariant family, without required-seam merger, milestone absorption or review substitution.

## Bounded write/effect scope

Only `elmakus/project_workflow_v2` branch `work/pwv21-policy-kernel` is the product target. Expected edits are Brainstorming/Definition entry validation/routing and focused tests/docs essential to this gate. Git commit/push and exact-head CI readback are authorized external effects.
