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
- Workstream root: `implementation/workstreams/ | none` (non-live discovery convention; never a registry of active state)
- Historical/default Task Board: `implementation/TASK_BOARD.yaml | none` (recovery/migration navigation only; never a new-work mutable destination)
- Historical/default cumulative handoff: `project-handoffs/MXX_HANDOFF.md | none` (recovery/history navigation only; branch-isolated handoffs are selected through that workstream's Task Board)
- Accepted decisions index / key pointers:
  - `<decisions/... | none>`

## Workflow

- Workflow repository: `elmakus/chatgpt-codex-project-workflow`
- Workflow ref: `main`

## Context note

This file is a high-level integrated-project router/policy/index, not live workstream execution or pre-execution routing state.

Active workstream-local exploratory, pre-execution Research and plan-review locators belong to the exact selected workstream manifest (or exact artifacts referenced from it) under the owning policy contract. Do not mirror those mutable locators into root `PROJECT.md`.

Historical/default Task Board and handoff pointers may remain only as recovery/history navigation for repositories that predate branch-first managed changes. Their presence does not authorize new or continued managed-change mutation in root/default state; the selected fixed-policy Recovery route must migrate required live state into an exact branch-isolated workstream first.

Do not record current milestone/card, assigned executor, active branch/HEAD, checkpoint, current OpenSpec, blocker status, active workstream list, workstream-local routing locators or workstream review state here. `Workstream root` is only a path convention for discovery, never live state. The approved Master Plan remains integrated project authority; active branch-local proposed changes are recovered through the exact workstream.
