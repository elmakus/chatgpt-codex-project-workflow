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

- Active exploratory scope: `brainstorming/<record>.md | none`
- Active research obligation: `research/<record>.md | none`
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

`Active exploratory scope` is a routing pointer to the current brainstorming record when one exists; it is not implementation execution state. Clear or replace it when that exploratory scope is closed/superseded.

`Active research obligation` is a routing pointer for pre-execution Research only. Its pointed research record owns active/complete/blocked/consumed lifecycle state plus exact Origin/Return subjects. Keep the pointer through `complete` and clear it only after the Return target durably consumes the findings. Implementation-triggered Research remains owned by Task Board/blocker state instead of this PROJECT pointer.

Do not record current milestone/card, assigned executor, active branch/HEAD, checkpoint, current OpenSpec or blocker status here. Read `implementation/TASK_BOARD.yaml` for all mutable execution state. The approved Master Plan milestone subsection is the default milestone contract; follow any optional JIT milestone extension, referenced Task Card authority slices, required evidence and handoffs.
