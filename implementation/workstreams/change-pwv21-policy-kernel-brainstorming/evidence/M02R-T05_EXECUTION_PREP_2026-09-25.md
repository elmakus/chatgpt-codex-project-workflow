# M02R-T05 Execution Prep — materialization audit

Date: 2026-09-25. Accepted authority: P6/Definition R3 and ADR-PWV21-006. Predecessor: `results/M02R-T04.md@852506eb6a05f25ea207cf632305dff77682df4c:9d25c57b2d07c9902a567b447ceb84acc5c5e54d` with independent R01 GREEN; trigger `after-M02R-T04` is satisfied and is consumed by this materialization.

## Decomposition-quality audit

- Independent implementability/falsifiability/reviewability: semantic Card sizing, its split/merge matrix and the audit that applies it form one testable decision outcome; each can be challenged with candidate-topology fixtures and reviewed without BOOT-C/D. A free-standing audit without a decision invariant would be descriptive, while a decision invariant without the audit would not enforce REQ-118 before materialization. Their shared acceptance is one coherent BOOT-B result.
- Invariant/contract family: REQ-118 and REQ-128/129 all govern the semantic boundary of a Card at Execution Prep. REQ-119..121 are a second-order independent topology challenge and review-layer guard; REQ-130 governs newly discovered oversize after launch. Each can reach its own valid GREEN while a sibling remains RED, so they stay separate JIT outcomes. BOOT-C and BOOT-D are stronger P6 required seams and remain separate.
- Dependency ordering: T05 consumes T04's seam vocabulary/fidelity result. A later risky-topology challenge can inspect the completed sizing audit; late-oversize routing can reuse the decision function. No speculative downstream Card identities or result bindings are needed now.
- Atomic mutation/migration and cross-surface coupling: T05's audit, invariant and split function share the same candidate topology and rejection rules; splitting them would create a temporary policy state with a decision unsupported by its required audit, or an audit without an enforceable semantic criterion. No cross-surface dependency requires merging the later challenge or late-oversize lifecycle into T05.
- Risk/narrowness: T05 stays within one BOOT-B invariant family and leaves independent challenge and late lifecycle handling as separate outcomes. It does not absorb the whole milestone or merge planner-required seams; a fresh topology challenge is not triggered by this bounded materialization itself.

Materialize only M02R-T05 as READY. Retain a waiting `after-M02R-T05` trigger for the remaining BOOT-B outcomes, then BOOT-C/D. Historical M02 state is read-only regression source; M03 remains unmaterialized until all M02R required seams and the Milestone review are GREEN.
