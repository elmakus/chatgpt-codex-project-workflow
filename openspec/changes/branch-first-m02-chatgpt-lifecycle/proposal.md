# Change: ChatGPT-only branch-first lifecycle migration

## Why

M01 established branch-first workstream identity, workstream-local routing locators and recovery-only historical root/default state. ChatGPT-only lifecycle modules still contain pre-M01 root `PROJECT.md` routing pointers and active legacy/default execution-state fallbacks. M02 must move those active paths onto the selected workstream without weakening review, Research, migration or terminal recovery semantics.

## Authority

- `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` — REQ-BF-002..009, REQ-BF-011..014, REQ-BF-016..017 and ChatGPT-only REQ-BF-015
- ADR-BF-001, ADR-BF-002, ADR-BF-003
- `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md` — M02
- M01 GREEN checkpoint and handoff

## Proposed change

Use selected manifest `routing.exploratory_scope`, `routing.research_obligation` and `routing.plan_review` for all ChatGPT-only pre-execution continuation. Then remove root/default as a normal ChatGPT-only execution context: new/live managed work uses the exact manifest-selected Task Board, while historical root/default state routes through deterministic migration before mutation.

## Non-goals

- no Codex-only lifecycle migration (M03);
- no deletion/rewrite of completed historical evidence;
- no workflow-repository dogfood/README closure (M04);
- no weakening of independent review, target refresh, terminal package or source-branch-deletion safety.
