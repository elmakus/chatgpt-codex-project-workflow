# M04 Handoff — Worktree, stacked branch and integration refresh contracts

## Completed checkpoint

- Milestone: `M04`
- Final implementation head / accepted subject: `38955588da57039183b0c15a3cd55fbf8b384e80`
- Result: GREEN
- Independent Card review: GREEN — `implementation/evidence/M04-T01-review-01.md`
- Integrated milestone acceptance: GREEN — `implementation/evidence/M04-acceptance.md`

Subsequent commits after the accepted subject are review/evidence/Task-Board closure state only and do not alter the reviewed workflow behavior.

## Achieved state

ChatGPT-only now defines the M04 local-concurrency and integration layer on top of the accepted M01–M03 workstream model.

- Concurrent local workstreams require isolated worktrees/equivalent checkouts; remote-only operations remain legal without local worktrees.
- Stacked work records an explicit parent-only dependency and preserves base/parent provenance.
- Direct child → final-target integration is forbidden while required parent-only state remains absent from that target.
- Parent-first and child-into-parent integration paths are explicit and recoverable.
- Final integration performs target refresh, bounded reconciliation, affected verification, textual + semantic conflict checks, and a final target re-read.
- Independent review validity is tied to the exact covered subject/acceptance surface rather than target SHA movement alone.
- File overlap alone does not create dependency/blocking.
- Legacy/default mode and M03 review/recovery ownership remain intact.

## Authority in force

- Requirements: `requirements/CHATGPT_ONLY_MULTI_WORKSTREAM_INTAKE.md`
- Accepted decision: `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`
- Approved plan: `planning/CHATGPT_ONLY_MULTI_WORKSTREAM_MASTER_PLAN.md` revision `MW-R1`
- M04 contract: `implementation/cards/M04-T01.md`

## Evidence

- Implementation evidence: `implementation/evidence/M04-T01.md`
- Independent review: `implementation/evidence/M04-T01-review-01.md`
- Integrated milestone acceptance: `implementation/evidence/M04-acceptance.md`

PR #28 remains draft/open because approved implementation scope continues through M05. No external runtime/deployment write was required.

## Next durable starting point

Return to the ChatGPT-only router and enter Execution Prep for approved milestone `M05 — UX, templates, migration and regression coverage`.

M05 must consume the accepted M01–M04 contracts, complete fresh-handoff/template/migration/regression coverage, run the required logical E2E matrix, and prepare the exact final architecture/coherence review boundary before project integration.
