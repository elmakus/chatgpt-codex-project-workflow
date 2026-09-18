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
- Active research obligation (only when the selected policy defines this pointer; `chatgpt_only` uses it for pre-execution Research): `research/<record>.md | none`
- Requirements: `requirements/REQUIREMENTS.md | none`
- Approved plan: `planning/MASTER_PLAN.md | none`
- Task Board: `implementation/TASK_BOARD.yaml | none` (legacy/default state context; branch-isolated Task Boards are selected through their manifests)
- Workstream root: `implementation/workstreams/ | none` (optional non-live locator convention; never a registry of active state)
- Latest cumulative handoff: `project-handoffs/MXX_HANDOFF.md | none`
- Accepted decisions index / key pointers:
  - `<decisions/... | none>`

## Workflow

- Workflow repository: `elmakus/chatgpt-codex-project-workflow`
- Workflow ref: `main`

## Context note

This file is a high-level router/policy/index, not live execution state.

`Active exploratory scope` is a routing pointer to the current brainstorming record when one exists; it is not implementation execution state. Clear or replace it when that exploratory scope is closed/superseded.

`Active research obligation` is operative only when the selected policy route defines that continuation contract. Under `chatgpt_only`, it is the routing pointer for pre-execution Research: the pointed record owns active/complete/blocked/consumed lifecycle state plus exact Origin/Return subjects, remains pointed through `complete`, and is cleared only after durable consumption. `chatgpt_only` implementation/recovery Research instead uses Task Board `research_obligation`. A legacy/other-policy route that does not define this pointer keeps it `none`; the field's presence in this shared template does not import `chatgpt_only` routing semantics.

Do not record current milestone/card, assigned executor, active branch/HEAD, checkpoint, current OpenSpec, blocker status, active workstream list or workstream review state here. Under `chatgpt_only`, resolve the selected state context first: legacy/default mode uses `implementation/TASK_BOARD.yaml`, while a branch-isolated workstream uses its exact validated manifest to locate the canonical Task Board and owns its distinct final-integration review in that manifest. `Workstream root` is only a path convention for discovery, never live state. The approved Master Plan milestone subsection is the default milestone contract; follow any optional JIT milestone extension, referenced Task Card authority slices, required evidence and handoffs.
