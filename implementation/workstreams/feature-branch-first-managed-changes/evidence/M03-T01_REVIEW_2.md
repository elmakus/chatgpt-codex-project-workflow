# M03-T01 independent review — corrected subject

Date: 2026-09-20
Card: `M03-T01 — Migrate Codex-only pre-execution routing to workstream-local state`
Review subject: `9aa1af79e4e3634c81626fc04fc6c9a7a6874519`
Verdict: **GREEN**

## Authority reviewed

- `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md` — M03
- `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` — REQ-BF-002..009, REQ-BF-011, REQ-BF-016..017 and Codex-only REQ-BF-015
- ADR-BF-001, ADR-BF-002, ADR-BF-003
- `openspec/changes/branch-first-m03-codex-lifecycle/`
- M01 GREEN and M02 GREEN checkpoints
- Card contract `implementation/workstreams/feature-branch-first-managed-changes/cards/M03-T01.md`
- Implementation evidence `implementation/workstreams/feature-branch-first-managed-changes/evidence/M03-T01.md`
- Prior RED evidence `implementation/workstreams/feature-branch-first-managed-changes/evidence/M03-T01_REVIEW.md`
- Exact reviewed source at the immutable subject

## Independent inspection

The corrected subject removes the prior in-scope semantic defect: Definition now distinguishes selected-workstream-manifest pre-execution Research routing from selected-Task-Board implementation/recovery Research and no longer permits pre-execution PROJECT-owned Research.

The complete M03-T01 surface was inspected independently:
- Brainstorming, Definition, Planning, Research, Plan Review and Router use selected-manifest pre-execution locators;
- pointed records retain lifecycle/status/subject/result ownership;
- promotion remains user-owned and exact-subject bound;
- invalid/stale locator semantics are fail-closed through Workstreams/Router;
- Codex Main sole-writer and independent Tester semantics remain intact;
- bounded-batch/Card-review ownership remains unchanged;
- no ChatGPT-only lifecycle import is introduced;
- M03-T02-owned execution/default-state Recovery/Repository migration remains explicitly deferred by the Card contract and its own accepted Card.

Independent replay of the committed focused regression assertions against the exact subject is GREEN for all 9 test methods represented by `tests/test_codex_only_branch_first_preexecution_contract.py`. The implementation evidence also records repository unittest discovery 19/19 PASS on the corrected worktree; this review does not claim a separate CI run.

## Verdict

**GREEN.** The exact subject satisfies M03-T01 acceptance and its bounded authority slice. No corrective work is required before post-review Card finalization.
