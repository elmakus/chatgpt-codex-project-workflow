# PROJECT

## Identity

- Project: `chatgpt-codex-project-workflow`
- Repository: `elmakus/chatgpt-codex-project-workflow`
- Lifecycle: `active`
- High-level goal: maintain and evolve the repository-backed Project Workflow contracts used by ChatGPT/Codex project execution.
- High-level status: dedicated `codex_only` policy namespace feature workstream is entering Project Definition from approved exploratory scope `codex-only-policy@R1`.

## Execution policy

- execution_policy: `chatgpt_only`

Changing execution policy requires an explicit user decision.

## Canonical authority pointers

- Active exploratory scope: `brainstorming/CODEX_ONLY_POLICY.md`
- Active research obligation: `none`
- Requirements: `requirements/CHATGPT_ONLY_MULTI_WORKSTREAM_INTAKE.md`
- Approved plan: `planning/CHATGPT_ONLY_MULTI_WORKSTREAM_MASTER_PLAN.md`
- Task Board: `implementation/TASK_BOARD.yaml`
- Latest cumulative handoff: `project-handoffs/M05_HANDOFF.md`
- Accepted decisions index / key pointers:
  - `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`

## Workflow

- Workflow repository: `elmakus/chatgpt-codex-project-workflow`
- Workflow ref: `main`

## Context note

This file is a high-level router/policy/index, not live execution state.

The current project itself continues to execute under `chatgpt_only`. The active branch-isolated feature workstream is `feature-codex-only-policy`; its mutable workstream state is selected through its manifest rather than by changing this project's execution policy.

The existing `implementation/TASK_BOARD.yaml` remains the legacy/default board for the completed prior project scope. A workstream-local Task Board will be created only when the new feature reaches Execution Prep.

Do not record current milestone/card, assigned worker session, invocation ID, Muse lease, active worker profile/model, checkpoint or blocker status here.
