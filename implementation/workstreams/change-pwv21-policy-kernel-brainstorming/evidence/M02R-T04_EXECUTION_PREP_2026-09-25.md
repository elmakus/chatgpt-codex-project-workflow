# M02R-T04 Execution Prep — materialization audit

Date: 2026-09-25
Plan subject: `elmakus/chatgpt-codex-project-workflow@d4c9c7d4ef23cbce4a5aabc045e75fa3dfbbe0be:planning/PWV21_POLICY_KERNEL_MASTER_PLAN_P6.md@63a85b19a7589e2cdd49ed1be2053925867f3202`
Predecessor: `results/M02R-T03-R02.md@5b76ffe03259ff141afc6bfb5b7b546041a48b41:b357ba85d4975540f3ae87b05e73e3fcf8e0471a` (R02 GREEN; BOOT-A complete)
Trigger consumed: `after-M02R-T03` (satisfied → consumed)

## Right-sizing audit (why one Card, why these REQs)

- REQ-115 (durable seam declaration without speculative Card IDs) and
  REQ-116/117 (JIT enforcement: no required_seam merge, preferred_seam
  default with qualifying rationale) share one invariant: the seam-class
  vocabulary is meaningless without its enforcement, and the enforcement
  has nothing to enforce without the vocabulary. Splitting declaration
  from enforcement would produce an invalid intermediate state (declared
  seams with no fidelity semantics, or fidelity rules over undeclared
  classes), so the accepted split presumption (ADR-PWV21-006) is rebutted
  within this outcome by concrete invalid-intermediate-state evidence.
- REQ-118 (decomposition-quality audit), REQ-128..130 (semantic Card
  invariant / split function / late-oversize routing) are consumers of the
  seam vocabulary, not parts of it: they are separate downstream outcomes
  materialized after this Card is GREEN. They remain JIT, and a later RED
  in audit/sizing/topology does not invalidate M02R-T04's independently
  reviewed seam-fidelity result.
- REQ-119..121 (topology challenge, narrowness, layered review) are a
  second-order safeguard over materialized topology, separable from the
  seam declaration/enforcement contract itself. They remain JIT.
- BOOT-C (REQ-122..127) and BOOT-D (REQ-131..132) are separate P6
  required_seams and cannot merge with this Card.

## Falsifiability and risk

- Independently falsifiable: seam-schema fixtures, required-merge
  rejection routing, and preferred-deviation rationale gating each fail
  observably without any sibling BOOT-B outcome implemented.
- Non-risky topology: one invariant family (seam intent + fidelity),
  bounded Planning/Execution Prep contract surface, no multi-family
  absorption, no preferred-seam merger. No fresh topology challenge is
  triggered by this materialization itself.

## JIT decision

Materialize only `M02R-T04` (READY) now. Retain waiting trigger
`after-M02R-T04` for the remaining BOOT-B outcomes, then BOOT-C/D. No M03
materialization: all M02R required seams and Milestone review are still
outstanding.
