# M02R Execution Prep — P6

Date: 2026-09-24
Plan subject: `elmakus/chatgpt-codex-project-workflow@d4c9c7d4ef23cbce4a5aabc045e75fa3dfbbe0be:planning/PWV21_POLICY_KERNEL_MASTER_PLAN_P6.md@63a85b19a7589e2cdd49ed1be2053925867f3202`
Premium C: satisfied by explicit user choice to continue in the current context.

## Historical trigger reconciliation

The historical `after-M02-T01` trigger was created before R2/R3 and would have materialized M03 directly. P6 explicitly supersedes that continuation. The trigger is consumed by reconciliation into **M02R-first** execution; M03 remains unmaterialized until M02R is terminal GREEN with its milestone review GREEN.

## Right-sizing audit

P6 freezes four non-mergeable Planning-level required seams: BOOT-A/B/C/D. Execution Prep applies the accepted semantic Card rule rather than treating each seam as automatically one Card.

The current decomposition evidence is:

- **BOOT-A** contains three independently falsifiable/reviewable outcomes:
  1. discovery vs finding-closure semantics, causal blast radius, exhaustive finding-set discovery, class/root-cause repair, and fresh rediscovery after known closure;
  2. stable review epochs, 5/4/3 genuinely-new defect-class discovery accounting, per-class 3-round repair/closure breaker, convergence and post-convergence structural routing;
  3. load-bearing vs advisory findings, durable non-load-bearing observation dispositions, pre-Final reconciliation and bounded cleanup lifecycle.
  GREEN on any one of these remains useful if a sibling outcome is RED, so one BOOT-A mega-Card would violate the accepted split presumption absent material atomicity evidence.
- **BOOT-B** currently exposes two meaningful outcomes: seam/topology-fidelity mechanics (REQ-115..121) and semantic Card right-sizing/late oversized-Card routing (REQ-128..130). They remain candidates for separate Cards when materialized.
- **BOOT-C** is currently one coherent live-finding/reconciliation/regression-replay family (REQ-122..127).
- **BOOT-D** is currently one coherent Worker falsification/YAGNI discipline family (REQ-131..132).

File/module/test boundaries alone were not used as split reasons.

## JIT decision

Only the first currently useful BOOT-A outcome is materialized now as `M02R-T01`. Later M02R Cards remain JIT until predecessor implementation evidence can be read back and used to bind exact stable contracts. This avoids speculative downstream contracts while preserving the P6 required seams and the accepted anti-mega-Card rule.

No M03 Card is materialized by this action.
