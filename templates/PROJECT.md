# PROJECT

## Identity

- Project: `<name>`
- Repository: `<owner/repo>`
- Lifecycle: `active | maintenance | paused | completed`
- High-level goal: `<short durable goal>`
- High-level status: `<short project-level status; do not mirror current card/milestone state>`

## Execution policy

- execution_policy: `chatgpt_only`

Allowed values:
- `chatgpt_only` — ChatGPT is fixed Task Card executor; no Capability Gate.
- `codex_only` — Codex is fixed Task Card executor; no Capability Gate; approved milestone sequences may continue automatically across GREEN boundaries.
- `mixed` — ChatGPT routes new execution assignments through Capability Gate.

Changing execution policy requires explicit user decision. Default for new project is `chatgpt_only`.

## Canonical authority pointers

- Requirements: `requirements/REQUIREMENTS.md | none`
- Approved plan: `planning/MASTER_PLAN.md | none`
- Task Board: `implementation/TASK_BOARD.yaml | none`
- Latest cumulative handoff: `project-handoffs/MXX_HANDOFF.md | none`
- Accepted decisions index / key pointers:
  - `<decisions/... | none>`

## Workflow

- Workflow repository: `elmakus/chatgpt-codex-project-workflow`
- Workflow ref: `main`

## Context note

This file is a high-level router/policy/index, not live execution state.

Do not record current milestone/card, assigned executor, active branch/HEAD, checkpoint, current OpenSpec or blocker status here. Read `implementation/TASK_BOARD.yaml` for all mutable execution state and follow referenced milestone/Card contracts/evidence/handoffs.
