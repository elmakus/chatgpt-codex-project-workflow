# Master Plan — YAGNI / Proportional Design

Revision: `YAGNI-P2`
Status: `approved`
Updated: `2026-09-21`
Independent plan review: `RECOMMENDED`

> Planning organizes the approved `requirements/YAGNI_OVERENGINEERING_GUARD.md` Definition. Requirements and `ADR-YAGNI-001` remain product/system authority; this plan does not redefine them.

## 1. Accepted target / canonical inputs

- Requirements: `requirements/YAGNI_OVERENGINEERING_GUARD.md` — `R1`, approved.
- Accepted decision: `decisions/ADR_YAGNI_PROPORTIONAL_DESIGN.md` — `ADR-YAGNI-001`.
- Exploratory provenance: `brainstorming/YAGNI_OVERENGINEERING_GUARD.md` — `yagni-overengineering-guard@R3`, user-promoted.
- Research evidence: `research/YAGNI_PRACTICES_R1.md`.
- Workstream: `implementation/workstreams/feature-yagni-overengineering-guard/WORKSTREAM.yaml`.

## 2. Execution baseline

- Both migrated fixed-policy routers already load `workflow/common/AUTHORITY.md` as policy-neutral authority before policy-local role execution.
- `workflow/common/AUTHORITY.md` currently has no general proportional-design/YAGNI invariant.
- ChatGPT-only and Codex-only Planning already audit for overengineering/premature implementation detail, but there is no canonical definition of what that means.
- Existing review/execution contracts already enforce bounded scope and current authority, but do not provide the concrete-current-justification test for material complexity.
- Existing OpenSpec policy is selective and already supports changed behavior contracts; it does not require a new YAGNI-specific mechanism.
- Existing OpenSpec ownership differs by fixed policy and must be preserved: ChatGPT-only Execution Prep marks candidates while ChatGPT-only Execution reconciles required OpenSpec JIT; Codex-only Execution Prep currently creates/reconciles JIT OpenSpec when warranted.

## 3. Inherited non-goals / invariants / constraints

- One canonical policy-neutral invariant; do not duplicate competing full definitions across policy namespaces.
- No new lifecycle phase, state owner, gate, scoring model, complexity budget, registry or numeric abstraction threshold.
- YAGNI cannot override accepted requirements/decisions, verified hard constraints or current correctness/security/testing/compatibility/maintainability obligations.
- “Simplest” means least unnecessary complexity while satisfying the full applicable authority surface, not minimum LOC/files/effort.
- Existing fitting mechanisms are preferred when adequate, but new machinery remains valid when current authority/evidence justifies it.
- Abstraction/generalization should emerge from demonstrated current need/variation or another concrete current constraint.
- Changes remain focused; unrelated cleanup is not bundled unless current scope requires it.

## 4. Milestones

### M01 — Make YAGNI a shared operational workflow invariant

- Outcome: all Project Workflow roles under the migrated fixed-policy routes inherit one policy-neutral YAGNI/proportional-design invariant, and Planning/Review have a concrete operational check for unjustified complexity without new workflow machinery.
- Checkpoint: canonical common authority, minimal policy-local operational references, contract tests and discoverability documentation agree on one invariant and preserve all quality/authority guardrails.
- Requirement coverage: YAGNI-REQ-001 through YAGNI-REQ-010.
- Dependencies: approved YAGNI R1 Definition and ADR-YAGNI-001.
- Acceptance:
  - `workflow/common/AUTHORITY.md` contains one canonical proportional-design/YAGNI section implementing YAGNI-REQ-001..009;
  - both migrated fixed-policy routers continue to load that common authority, so Brainstorming/Definition/Planning/Execution Prep/Execution/Review inherit the same invariant without copied full definitions;
  - ChatGPT-only and Codex-only Planning explicitly apply the concrete-current-justification question during their existing overengineering/premature-detail audit;
  - ChatGPT-only and Codex-only independent Review explicitly treats unjustified speculative complexity as a review defect while preserving current quality/authority obligations;
  - no YAGNI-specific state/gate/score/registry is introduced;
  - regression/contract tests prove the common invariant, cross-policy loading, operational Planning/Review references, and guardrail language;
  - README or equivalent workflow-facing documentation exposes the principle concisely if needed for user/maintainer discoverability without duplicating the full contract.
- Planned work packages:
  1. Add one canonical YAGNI/proportional-design section to `workflow/common/AUTHORITY.md`.
  2. Add minimal references/operational question to `workflow/chatgpt_only/PLANNING.md` and `workflow/codex_only/PLANNING.md`; do not restate the whole invariant.
  3. Add minimal review criterion/reference to `workflow/chatgpt_only/REVIEW.md` and `workflow/codex_only/REVIEW.md`; do not create new review state.
  4. Add one focused contract test (for example `tests/test_yagni_proportional_design_contract.py`) that verifies canonicality, both router bootstraps, planning/review consumption, anti-speculation language and quality guardrails.
  5. Update README only with a concise discoverability note if the resulting invariant would otherwise be materially hidden; avoid duplicate policy prose.
- OpenSpec candidate: **yes, JIT and minimal** — this changes a shared behavior contract across policy routes. Execution Prep should make/record the selective candidate/need decision using the selected route's existing contract; if OpenSpec is required, actual creation/reconciliation must remain with the role already assigned by that policy rather than introducing a new cross-policy owner. No separate design document unless current implementation risk actually warrants it.
- JIT decomposition trigger: Execution Prep may use one bounded Card if the exact diff remains cohesive; split only if review/write-scope/test isolation materially benefits from separation.
- Planning re-evaluation trigger: implementation shows the common authority bootstrap cannot make the invariant effective without materially wider policy-local duplication or a new lifecycle mechanism.
- Definition re-open trigger: implementation requires weakening current quality obligations, adding a YAGNI-specific state/gate/score, or changing the accepted meaning of present justification.
- Boundary gate / explicit user authorization: none beyond normal independent review gates.

## 5. Requirement coverage matrix

| Requirement | Owner milestone | Planned work package / verification |
|---|---|---|
| YAGNI-REQ-001 | M01 | Common authority invariant + contract test |
| YAGNI-REQ-002 | M01 | Common anti-speculation language + tests |
| YAGNI-REQ-003 | M01 | Concrete-current-justification rule + Planning/Review references |
| YAGNI-REQ-004 | M01 | Quality/authority guardrail language + tests |
| YAGNI-REQ-005 | M01 | “Simplest” definition + tests |
| YAGNI-REQ-006 | M01 | Existing-fitting-mechanism preference in common invariant |
| YAGNI-REQ-007 | M01 | Evidence-based abstraction/generalization corollary |
| YAGNI-REQ-008 | M01 | Focused-change corollary + existing bounded-scope contracts |
| YAGNI-REQ-009 | M01 | Explicit no-new-YAGNI-machinery invariant + test absence/contract checks |
| YAGNI-REQ-010 | M01 | Planning/Review operational question and regression tests |

## 6. Execution order

1. JIT-confirm through the selected route's existing OpenSpec decision/ownership flow whether one compact OpenSpec change is warranted by the current shared behavior-contract risk.
2. Add the canonical common invariant.
3. Add only the minimum policy-local Planning/Review references needed for operational enforcement.
4. Add focused tests against the exact resulting contract.
5. Add only necessary discoverability documentation.
6. Run focused and full repository contract tests.

The implementation should prefer one cohesive Card unless actual write/review boundaries prove a split useful.

## 7. Migration / rollback / compatibility

- Documentation/workflow-contract change only; no data migration, runtime deployment or live-write gate.
- Existing projects automatically consume the invariant through current workflow `main` when their selected routes load common authority.
- No existing accepted project requirement is rewritten by the invariant; it only constrains future workflow design/execution choices.
- Rollback is ordinary Git revert of the contract change and associated tests/docs.
- Compatibility: existing requirements that already justify complexity remain valid; the invariant must not retroactively invalidate them merely because they are complex.

## 8. Verification strategy

- Focused contract test asserts:
  - canonical YAGNI section exists in common authority;
  - both fixed-policy routers require common authority;
  - planning/review modules consume/reference the canonical rule rather than duplicate a second full definition;
  - speculative future abstraction/config/extensibility is prohibited without present justification;
  - current correctness/security/testing/maintainability/compatibility obligations remain protected;
  - no numeric threshold/score/state/gate is introduced by the feature.
- Run all existing repository tests to catch route/contract regressions.
- Use textual checks only as contract regression support; final review must also inspect semantic consistency and absence of contradictory policy-local wording.

## 9. OpenSpec strategy

- Treat M01 as a candidate for one JIT OpenSpec behavior change because the invariant is shared across policy routes.
- Preserve the selected route's existing ownership semantics: Execution Prep decides/marks the candidate as defined by that route, and the role already responsible for JIT creation/reconciliation performs it. This YAGNI change must not move OpenSpec ownership.
- Do not create multiple OpenSpec changes or a design document merely for ceremony.
- If the common authority + exact requirement/ADR already makes the Card contract unambiguous and OpenSpec adds no risk reduction, the JIT decision may record that it is unnecessary under the selective policy.

## 10. Pre-implementation planning audit

Planner audit: **GREEN**.

- Definition consistency: GREEN — all planned work maps directly to YAGNI-REQ-001..010 and ADR-YAGNI-001.
- Milestone proportionality: GREEN — one milestone; no speculative future milestones.
- Dependency completeness: GREEN — no predecessor evidence required.
- Acceptance completeness: GREEN — canonicality, cross-policy inheritance, operational Planning/Review use, quality guardrails and tests are explicit.
- Migration/security/data integrity: GREEN — no migration/live-write surface; existing security/compatibility obligations are explicitly preserved.
- OpenSpec boundary: GREEN — candidate only, JIT-selective, with current policy-specific ownership preserved rather than changed by this feature.
- Overengineering audit: GREEN — no new lifecycle/state/scoring subsystem; one common invariant plus minimal consumers/tests.
- Unresolved Definition/user questions: none.
- Independent plan review: `RECOMMENDED` because this is a new cross-policy workflow-behavior plan and independent review is practical.

## 11. Plan-review handoff

Freeze this exact `YAGNI-P2` draft for independent plan review before approval. Any substantive correction after review creates a new plan revision/subject.
