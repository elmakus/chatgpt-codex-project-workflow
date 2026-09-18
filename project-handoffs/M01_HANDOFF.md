# M01 Handoff — Workstream state model and routing foundation

## Completed checkpoint

- Milestone: `M01`
- Final implementation head / accepted subject: `adba7d1da3641e9bc008483c53246119b20dd066`
- Result: GREEN
- Independent Card review: GREEN — `implementation/evidence/M01-T01-review-02.md`

Subsequent commits after the accepted subject are review/evidence/Task-Board closure state only and do not alter the reviewed workflow behavior.

## Achieved state

ChatGPT-only workflow state can now resolve either the legacy/default `implementation/TASK_BOARD.yaml` or one exact branch-isolated workstream manifest plus its canonical Task Board before implementation/review/recovery state is interpreted.

For branch-isolated state, manifest → Task Board binding is mandatory:
- Task Board `workstream_id` must equal manifest `id`;
- Task Board `execution_ref.branch` must equal manifest `branch`;
- missing/null/mismatched required state routes to Recovery without legacy fallback.

Seriality is scoped per selected Task Board, no mutable global workstream registry is required, and policy-neutral wording preserves the default Task Board for routes that do not define another canonical location.

## Authority in force

- Requirements: `requirements/CHATGPT_ONLY_MULTI_WORKSTREAM_INTAKE.md`
- Accepted decision: `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`
- Approved plan: `planning/CHATGPT_ONLY_MULTI_WORKSTREAM_MASTER_PLAN.md` revision `MW-R1`
- M01 contract: `implementation/cards/M01-T01.md`

## Evidence

- Implementation evidence: `implementation/evidence/M01-T01.md`
- Independent review attempt 1 (RED): `implementation/evidence/M01-T01-review-01.md`
- Independent review attempt 2 (GREEN): `implementation/evidence/M01-T01-review-02.md`

No external runtime/deployment write was required.

## Next durable starting point

Return to the ChatGPT-only router and enter Execution Prep for approved milestone `M02 — Intake route: #issue / #feature`.

M02 must build on the accepted M01 workstream-resolution semantics; it must not weaken the user-owned `#feature` Brainstorming → Definition promotion gate.
