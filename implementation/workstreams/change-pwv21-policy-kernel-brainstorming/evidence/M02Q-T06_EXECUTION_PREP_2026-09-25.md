# M02Q-T06 Execution Prep — RF002 split, explicit user-stop precedence

Approved P7 order 5 RF002/H002,H022 was durably split into two independently useful invariant outcomes. `M02Q-T05` promotion-state Definition entry is DONE/GREEN with exact Result `results/M02Q-T05.md@c15151aa8e2250466cd50762fc45ed3f7314bd31:98a6bdd66a8f47635a1a4ef547a3eb5262dd73e1`; its real `after-M02Q-T05` JIT allocation is satisfied and now materializes this separate stop-precedence Card. The product candidate is `elmakus/project_workflow_v2@9077fe867e50462612bc2150610f8ac748429b1d`; canonical main remains `4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`.

Pre-M03 audit A1/A2 showed `explicit_user_stop = true` on a valid promoted/exact-authorized Brainstorming record being shadowed by active Definition and Definition GREEN/A-due branches. A brainstorm-only stop already works. This Card restores owner precedence only after exact durable promotion/Definition consistency checks, without revisiting T05 or generic Research precedence. P7 and V2 Brainstorming/Definition/User Stop with REQ-077/106/107 are accepted authority. After both RF002 Cards reach DONE/GREEN, P7 order-6 RF016 is next; M03 remains blocked until all 17 RF families and separate M02Q Milestone Review are terminal GREEN.

## Seven-dimension decomposition audit

- Independent implementability: explicit-stop precedence is useful while the promotion-entry Card remains separately GREEN; it can be changed without reopening the prior gate.
- Falsifiability/testability: A1/A2 valid promoted/authorized stop fixtures expose shadowing; no-stop and invalid-binding controls discriminate legal dispatch from stop and Recovery.
- Reviewability: a local Card Review can judge stop ownership across Definition/Planning without certifying promotion entry again or whole RF/M02Q composition.
- Invariant/contract family: one explicit-stop owner-ordering invariant applies across pre-execution downstream branches; branch-specific tests are siblings, not separate semantic outcomes.
- Dependency ordering: consumes exact DONE/GREEN T05 and its JIT allocation in P7 order; RF016 follows only after this Card's separate result/review.
- Atomic mutation/migration: preserving validation before the stop prevents invalid durable bindings from bypassing Recovery. No historical migration or coupled RF mutation is required.
- Cross-surface coupling: router priority and kernel stop predicate share one RF002-local outcome; previous promotion gating is a stable dependency, not merged rework.

Decision: materialize one `M02Q-T06` Card for the second split RF002 invariant. Simple card-local topology: one independently falsifiable family, no preferred-seam merge, multi-family Card, milestone absorption or review substitution.

## Bounded write/effect scope

Only `elmakus/project_workflow_v2` branch `work/pwv21-policy-kernel` is the product target. Expected edits are stop precedence in the router and focused tests/docs essential to this behavior. Git commit/push and exact-head CI readback are authorized external effects.
