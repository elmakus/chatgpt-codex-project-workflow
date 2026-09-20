# PROJECT

## Identity

- Project: `chatgpt-codex-project-workflow`
- Repository: `elmakus/chatgpt-codex-project-workflow`
- Lifecycle: `active`
- High-level goal: maintain and evolve the repository-backed Project Workflow contracts used by ChatGPT/Codex project execution.
- High-level status: Project Workflow Codex plugin scope `project-workflow-codex-plugin@R1` is promoted into Project Definition on branch `feat/project-workflow-codex-plugin`.

## Execution policy

- execution_policy: `chatgpt_only`

Changing execution policy requires an explicit user decision.

## Canonical authority pointers

- Active exploratory scope: `brainstorming/PROJECT_WORKFLOW_CODEX_PLUGIN.md`
- Active research obligation: `none`
- Requirements: `requirements/CODEX_ONLY_UNMERGED_BRANCH_CLEANUP.md`
- Approved plan: `planning/CODEX_ONLY_UNMERGED_BRANCH_CLEANUP_MASTER_PLAN.md`
- Task Board: `implementation/TASK_BOARD.yaml`
- Latest cumulative handoff: `project-handoffs/CUBC-M01_HANDOFF.md`
- Accepted decisions index / key pointers:
  - `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`
  - `decisions/ADR_CODEX_ONLY_TERMINAL_UNMERGED_BRANCH_DELETE.md`

## Workflow

- Workflow repository: `elmakus/chatgpt-codex-project-workflow`
- Workflow ref: `main`

## Context note

This file is a high-level router/policy/index, not live execution state.

The current project uses the legacy/default Task Board path for its own default implementation state. Branch-isolated workstreams created by the multi-workstream feature use their own validated manifests and Task Boards under the active ChatGPT-only workflow contract.

The active exploratory pointer may temporarily identify the exact promoted branch-isolated Definition subject until Definition completes. Do not use that pointer as mutable execution state.

Do not record current milestone/card, assigned executor, active branch/HEAD, checkpoint, current OpenSpec or blocker status here. Read the canonical Task Board selected by the active ChatGPT-only state context for mutable execution state.
