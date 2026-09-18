# Master Plan — <project>

Revision: `<R#>`
Status: `draft | approved`
Updated: `<YYYY-MM-DD>`
Independent plan review: `REQUIRED | RECOMMENDED | none`
Plan review status: `pending | in_progress | green | red | not_required`
Plan review evidence: `<planning/reviews/... | none>`

> Planning organizes an already-approved Project Definition. Requirements/accepted decisions remain the product/system authority; this plan does not redefine them.

## 1. Accepted target / canonical inputs

- Requirements: `requirements/REQUIREMENTS.md` (must be `approved`)
- Accepted decisions: ...
- Relevant research/evidence pointers: ...
- Project baseline/reference: ...

## 2. Execution baseline

Only the verified current-state facts needed to organize execution.

...

## 3. Inherited non-goals / invariants / external constraints

Reference exact Definition authority. Repeat only implementation-shaping detail whose omission could cause a different plan.

...

## 4. Milestones

### M01 — <name>

- Outcome: ...
- Checkpoint: ...
- Acceptance: `<stable outcome-level acceptance; defer only detail that genuinely depends on predecessor evidence>`
- Requirement coverage: ...
- Dependencies: ...
- Inherited constraints / rationale: `<exact refs + only material carried context>`
- Planned work packages:
  - `<bounded work package/theme; not a live Task Card>`
- JIT decomposition / deferred-detail trigger: `none | after <exact predecessor/result/evidence>`
- Planning re-evaluation trigger: `<condition that could invalidate milestone structure/order while Definition remains valid | none>`
- Definition re-open trigger: `<condition that could invalidate accepted requirements/decisions/invariants | none>`
- Boundary gate / explicit user authorization: `none | <exact gate>`

An approved milestone sequence may execute continuously under the active execution policy when downstream gates permit it.

Each approved milestone subsection is the default milestone contract. Create a separate `implementation/milestones/MXX.md` only just-in-time when it adds material execution/acceptance detail needed by Execution Prep or integrated acceptance.

## 5. Requirement coverage matrix

| Requirement | Owner milestone | Planned work package or JIT trigger | OpenSpec candidate |
|---|---|---|---|
| REQ-001 | M01 | `<work package>` or `JIT after <exact trigger>` | yes/no |

Do not invent future Task Card IDs merely to make this table look complete. Execution Prep creates concrete Cards before implementation.

## 6. Dependency / execution order

...

## 7. Deployment / migration / rollback strategy

...

## 8. System verification strategy

...

## 9. Idempotency / data-integrity / security strategy

...

## 10. Explicit authorization boundaries

...

## 11. JIT / deferred decomposition map

...

## 12. Fresh-context boundaries

Only when materially useful. Runtime Context Health Gate remains authoritative for actual session-hygiene handoffs.

...

## 13. Pre-implementation planning audit

- Definition Complete still GREEN: ...
- False assumptions / P0/P1 risks: ...
- Milestone boundaries/order: ...
- Dependency completeness: ...
- Outcome-level acceptance: ...
- Requirement coverage: ...
- Migration/rollback: ...
- System verification: ...
- Data integrity/idempotency/security: ...
- Authorization gates: ...
- OpenSpec boundaries: ...
- Overengineering/premature detail: ...
- Remaining blockers: `none | ...`

## 14. Workflow references

- Policy router: `workflow/CONTEXT_ROUTING.md`
- Project Definition: `workflow/common/DEFINITION.md`
- OpenSpec: `workflow/common/OPENSPEC.md`

Policy-specific Planning, plan-review, Execution Prep, Task Card and state modules are selected by the active execution-policy router. Do not hard-code one policy namespace into this shared template.

The Master Plan is not the live task tracker. Mutable execution state belongs only in `implementation/TASK_BOARD.yaml`.
