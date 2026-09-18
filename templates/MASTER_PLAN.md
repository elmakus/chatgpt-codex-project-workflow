# Master Plan — <project>

Revision: `<R#>`
Status: `draft | approved`
Updated: `<YYYY-MM-DD>`

## 1. Problem and goal
...

## 2. Current state / verified baseline
...

## 3. Target state
...

## 4. Canonical inputs
- Requirements: `requirements/REQUIREMENTS.md`
- Accepted decisions: ...
- Relevant research: ...

## 5. Frozen architecture decisions
...

## 6. Non-goals
...

## 7. Global invariants / external constraints
...

## 8. Known source seams
...

## 9. Milestones

### M01 — <name>
- Outcome: ...
- Checkpoint: ...
- Acceptance: ...
- Requirement coverage: ...
- Dependencies: ...
- Must-preserve constraints / implementation-shaping rationale: `<only when material>`
- Boundary gate / explicit user authorization: `none | <exact gate>`

An approved milestone sequence may execute continuously under fixed `chatgpt_only` or `codex_only` policy. GREEN milestone boundaries still require normal close/handoff plus fresh execution prep/Refresh Gate; execution stops at any explicit boundary gate.

Each approved milestone subsection is the default milestone contract. Create a separate `implementation/milestones/MXX.md` only just-in-time when it adds material contract detail needed for execution or integrated acceptance. Never replace richer planner intent with a shorter milestone/card paraphrase; downstream contracts point back to the exact authoritative sections.

## 10. Requirement coverage matrix

| Requirement | Milestone | Planned Task Card(s) | OpenSpec candidate |
|---|---|---|---|
| REQ-001 | M01 | M01-T01 | yes/no |

## 11. Deployment / migration strategy
...

## 12. System verification strategy
...

## 13. Idempotency / data-integrity / security strategy
...

## 14. Fresh-context boundaries
...

## 15. Workflow policy references

- Context routing: `workflow/CONTEXT_ROUTING.md`
- Execution prep: `workflow/EXECUTION_PREP.md`
- Shared execution: `workflow/EXECUTION.md`
- Capability Gate (`mixed` only): `workflow/chatgpt/CAPABILITY_GATE.md`
- Task decomposition: `workflow/contracts/TASK_CARDS.md`
- OpenSpec: `workflow/contracts/OPENSPEC.md`
- GitHub state: `workflow/contracts/GITHUB_STATE.md`
- Handoff/review: `workflow/REVIEW_AND_HANDOFF.md`

The Master Plan is not live task tracker. Live execution state belongs only in `implementation/TASK_BOARD.yaml`.
