# M01-T01 independent review

Date: 2026-09-20
Card: `M01-T01 — Define branch-first workstream routing state model`
Review subject: `e80a4b24854fae485e87532f882831291189bece`
Verdict: **GREEN**

## Authority reviewed

- `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md` — M01
- `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` — REQ-BF-001..009, REQ-BF-015..017
- ADR-BF-001, ADR-BF-002, ADR-BF-003
- `openspec/changes/branch-first-m01-state-entry/`
- `implementation/workstreams/feature-branch-first-managed-changes/evidence/M01_JIT_INVENTORY_2026-09-20.md`
- Card contract `implementation/workstreams/feature-branch-first-managed-changes/cards/M01-T01.md`

## Independent inspection

The review re-read the immutable subject and did not rely on implementing-session narrative. The M01-T01 implementation range after the persisted execution-start transition was inspected commit-by-commit through the exact review subject, and the resulting files were read back at that subject.

No blocking findings.

Acceptance checks:

1. GREEN — both fixed-policy manifest templates accept neutral `kind: change`.
2. GREEN — both templates expose the same three nullable pre-execution routing locators: `exploratory_scope`, `research_obligation`, and `plan_review`.
3. GREEN — both policy-local contracts define those fields as locator-only and preserve lifecycle/status plus subject/result ownership in the pointed artifacts.
4. GREEN — selected Task Board ownership for implementation/recovery Research and Card/milestone state is preserved; manifest `review` remains final-integration-review-only.
5. GREEN — both policy-local contracts fail missing, malformed, wrong-class, branch/workstream-mismatched, plan-subject-mismatched, or contradictory stale locators closed to Recovery without a global mutable registry.
6. GREEN — equivalent schema/validation exists in both fixed policies while policy-local lifecycle mechanics remain separate; no cross-policy lifecycle import was introduced.
7. GREEN — OpenSpec design/spec/tasks are coherent with the implemented schema and ownership contract.

Scope remained bounded to the two fixed-policy workstream templates/contracts plus M01 OpenSpec/schema coherence and evidence. Generic natural-language entry, default/root cutover, and full policy lifecycle rewiring remain outside this Card.

## Verdict

**GREEN.** The exact review subject satisfies the M01-T01 Card contract and its accepted authority slice. The Card may proceed to deterministic post-review finalization.
