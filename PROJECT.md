# PROJECT

## Identity

- Project: `chatgpt-codex-project-workflow`
- Repository: `elmakus/chatgpt-codex-project-workflow`
- Lifecycle: `active`
- High-level goal: maintain and evolve the repository-backed Project Workflow contracts used by ChatGPT/Codex project execution.
- High-level status: branch-first managed-change model is the accepted target for the migrated fixed policies; repository evolution remains active.

## Execution policy

- execution_policy: `chatgpt_only`

Changing execution policy requires an explicit user decision.

## Canonical authority pointers

- Requirements: `requirements/BRANCH_FIRST_MANAGED_CHANGES.md`
- Approved plan: `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md`
- Workstream root: `implementation/workstreams/` (non-live discovery convention; never a mutable active-workstream registry)
- Historical/default Task Board: `implementation/TASK_BOARD.yaml` (recovery/migration navigation only; never a new/continued-work mutable destination)
- Historical/default cumulative handoff: `project-handoffs/CUBC-M01_HANDOFF.md` (recovery/history navigation only; branch-isolated handoffs are selected through each workstream Task Board)
- Accepted decisions index / key pointers:
  - `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`
  - `decisions/ADR_CODEX_ONLY_TERMINAL_UNMERGED_BRANCH_DELETE.md`
  - `decisions/ADR_BRANCH_FIRST_MANAGED_CHANGE_LIFECYCLE.md`
  - `decisions/ADR_WORKSTREAM_LOCAL_ROUTING_STATE.md`
  - `decisions/ADR_POLICY_LOCAL_BRANCH_FIRST.md`

## Workflow

- Workflow repository: `elmakus/chatgpt-codex-project-workflow`
- Workflow ref: `main`

## Context note

This file is a high-level integrated-project router/policy/index, not live workstream execution or pre-execution routing state.

Under the migrated fixed-policy branch-first model, active managed-change identity/routing belongs to the exact selected workstream manifest and its pointed artifacts; mutable Card/milestone execution belongs to that manifest-selected Task Board. Active exploratory, pre-execution Research and plan-review locators must not be mirrored here.

Historical/default Task Board and handoff pointers above are retained only so repositories and completed history that predate branch-first remain recoverable. Their presence does not authorize new or continued managed mutation there.

Do not record current milestone/card, assigned executor, active branch/HEAD, checkpoint, current OpenSpec, blocker status, active workstream list, workstream-local routing locators or workstream review state here.
