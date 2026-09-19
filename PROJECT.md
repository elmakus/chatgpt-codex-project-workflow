# PROJECT

## Identity

- Project: `chatgpt-codex-project-workflow`
- Repository: `elmakus/chatgpt-codex-project-workflow`
- Lifecycle: `active`
- High-level goal: maintain and evolve the repository-backed Project Workflow contracts used by ChatGPT/Codex project execution.
- High-level status: dedicated `codex_only` policy namespace Definition `CO-R1` is GREEN; strategic Planning is active for workstream `feature-codex-only-policy`.

## Execution policy

- execution_policy: `chatgpt_only`

Changing execution policy requires an explicit user decision.

## Canonical authority pointers

- Active exploratory scope: `none`
- Active research obligation: `none`
- Requirements: `requirements/CODEX_ONLY_POLICY.md`
- Approved plan: `planning/CHATGPT_ONLY_MULTI_WORKSTREAM_MASTER_PLAN.md` (previous completed scope; current codex_only plan not yet approved)
- Task Board: `implementation/TASK_BOARD.yaml` (legacy/default board for previous completed scope)
- Latest cumulative handoff: `project-handoffs/M05_HANDOFF.md` (previous completed scope)
- Accepted decisions index / key pointers:
  - `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`
  - `decisions/ADR_CODEX_ONLY_DEDICATED_NAMESPACE.md`
  - `decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md`
  - `decisions/ADR_CODEX_ONLY_BOUNDED_PARALLEL_CARDS.md`

## Workflow

- Workflow repository: `elmakus/chatgpt-codex-project-workflow`
- Workflow ref: `main`

## Context note

This file is a high-level router/policy/index, not live execution state.

The repository itself continues to execute under `chatgpt_only`. The active branch-isolated feature workstream is `feature-codex-only-policy`; its mutable workstream state is selected through its manifest.

The previous default Task Board remains durable historical state. A workstream-local Task Board for this feature will be created only after an approved new Master Plan reaches Execution Prep.

Do not record current milestone/card, worker session IDs, invocation IDs, Muse leases, model/profile selection or worker runtime state here.
