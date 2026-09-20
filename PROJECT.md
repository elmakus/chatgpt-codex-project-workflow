# PROJECT

## Identity

- Project: `chatgpt-codex-project-workflow`
- Repository: `elmakus/chatgpt-codex-project-workflow`
- Lifecycle: `active`
- High-level goal: maintain and evolve the repository-backed Project Workflow contracts used by ChatGPT/Codex project execution.
- High-level status: Project Workflow Codex plugin Definition R2 and Master Plan `PWCP-P2` are approved; active implementation resumes from the selected branch-isolated workstream.

## Execution policy

- execution_policy: `chatgpt_only`

Changing execution policy requires an explicit user decision.

## Canonical authority pointers

- Active exploratory scope: `none`
- Active research obligation: `none`
- Requirements: `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md`
- Approved plan: `planning/PROJECT_WORKFLOW_CODEX_PLUGIN_MASTER_PLAN.md`
- Current plan draft: `none`
- Current plan review: `none`
- Open Definition question: `none`
- Task Board: `implementation/workstreams/feature-project-workflow-codex-plugin/TASK_BOARD.yaml`
- Latest cumulative handoff: `project-handoffs/CUBC-M01_HANDOFF.md`
- Accepted decisions index / key pointers:
  - `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_PACKAGING.md`
  - `decisions/ADR_PROJECT_WORKFLOW_CODEX_PLUGIN_ACTIVATION.md`
  - `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`
  - `decisions/ADR_CODEX_ONLY_TERMINAL_UNMERGED_BRANCH_DELETE.md`

## Workflow

- Workflow repository: `elmakus/chatgpt-codex-project-workflow`
- Workflow ref: `main`

## Context note

This file is a high-level router/policy/index, not live execution state.

The selected branch-isolated workstream is identified by `implementation/workstreams/feature-project-workflow-codex-plugin/WORKSTREAM.yaml`. Its canonical Task Board is active. Approved plan authority is `PWCP-P2`; mutable implementation/review state remains solely in the selected Task Board and workstream manifest.

Do not record current milestone/card, assigned executor, active branch/HEAD, checkpoint, current OpenSpec or blocker status here. Once implementation state exists, read the canonical Task Board selected by the active ChatGPT-only state context for mutable execution state.
