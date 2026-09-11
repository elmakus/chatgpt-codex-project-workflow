# ChatGPT Project Workflow Router

This repository is the canonical project-workflow authority for projects managed through normal ChatGPT chat, optionally using Codex as a specialized executor.

ChatGPT Work is outside this workflow. Do not route project work through ChatGPT Work or make it a prerequisite.

## Authority

- Current `main` of `elmakus/chatgpt-codex-project-workflow` is authoritative for workflow behavior.
- Project knowledge belongs in the project repository, not this workflow repository.
- Accepted durable project state outranks stale chat memory.
- One project uses one repository unless the user explicitly approves a technically justified exception.
- `elmakus/codex_workflow`, when installed/enabled in Codex, governs only internal Codex runtime orchestration.

## Start here

1. Read project root `PROJECT.md` when it exists.
2. Read `workflow/CONTEXT_ROUTING.md`.
3. Load only the shared phase module and project artifacts required for the current task.
4. Respect `execution_policy` in `PROJECT.md`.
5. Persist accepted project knowledge and execution truth in the project repository.

Do not load execution contracts during ordinary brainstorming/research unless the current task requires them.

Do not load detailed Codex-specific instructions during ordinary ChatGPT work. When preparing or interpreting a Codex handoff, load only `workflow/codex/HANDOFF.md` unless more Codex context is genuinely required.

## Execution policy

### `chatgpt_only`

ChatGPT may brainstorm, research, plan, modify repositories, implement, test, use connected plugins/services, deploy, verify, review and close milestones when the **current ChatGPT chat session** has all required capabilities and can obtain the required evidence.

If a required capability is unavailable, report the exact blocker. Do not hand the task to Codex and do not change policy automatically.

### `mixed`

ChatGPT remains project router. Before executing a Task Card, apply `workflow/chatgpt/CAPABILITY_GATE.md`.

Execute in ChatGPT when the current session can correctly perform the task, run the required tests/checks and obtain the required evidence/readback.

Hand off to Codex only when policy permits and Codex has a required capability/environment, a material repo/runtime advantage, or the approved card/plan explicitly assigns the task to Codex.

## Phase routes

- Brainstorming → `workflow/BRAINSTORMING.md`
- Research → `workflow/RESEARCH.md`
- Planning → `workflow/PLANNING.md`
- Execution preparation → `workflow/EXECUTION_PREP.md`
- Shared execution/recovery → `workflow/EXECUTION.md`
- ChatGPT execution adapter → `workflow/chatgpt/EXECUTION.md`
- Milestone review/close/handoff → `workflow/REVIEW_AND_HANDOFF.md`
- Context rules → `workflow/CONTEXT_ROUTING.md`
