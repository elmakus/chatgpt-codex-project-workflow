# PROJECT

## Identity

- Project: `<name>`
- Repository: `<owner/repo>`
- Phase: `brainstorming | research | planning | execution_prep | execution | milestone_review | system_verification | cutover`
- Current goal: `<short goal>`
- Current status: `<short status>`

## Execution policy

- execution_policy: `chatgpt_only | mixed`

`chatgpt_only` blocks Codex routing; missing ChatGPT capability is a blocker. `mixed` lets ChatGPT route individual Task Cards to itself or Codex through the Capability Gate.

## Canonical authority pointers

- Requirements: `requirements/REQUIREMENTS.md | none`
- Approved plan: `planning/MASTER_PLAN.md | none`
- Current milestone: `implementation/milestones/MXX.md | none`
- Task Board: `implementation/TASK_BOARD.yaml | none`
- Latest cumulative handoff: `project-handoffs/MXX_HANDOFF.md | none`
- Active OpenSpec change: `<openspec/changes/... | none>`
- Relevant accepted decisions:
  - `<decisions/... | none>`
- Open questions:
  - `<brainstorming/OPEN_QUESTIONS.md or other path | none>`
- Current blockers:
  - `<implementation/blockers/... | none>`

## Workflow

- Workflow repository: `elmakus/chatgpt-codex-project-workflow`
- Workflow ref: `main`

## Execution ref

Use only when active execution needs an explicit durable pointer.

- Branch: `<branch | none>`
- PR: `<number | none>`
- HEAD: `<sha | none>`

## Context note

This file is a router, not project history. Follow current workflow context routing and referenced canonical artifacts.
