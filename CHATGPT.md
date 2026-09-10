# ChatGPT Workflow Router

This repository is the canonical workflow authority for ChatGPT ↔ Codex project work.

## Authority

- The current `main` branch of `elmakus/chatgpt-codex-project-workflow` is the workflow source of truth.
- If conversation memory, an old prompt, a ZIP snapshot, or prior workflow text conflicts with current `main`, current `main` wins.
- This repository contains workflow rules only. Project knowledge belongs in the project's own repository.
- One project uses one repository from the first brainstorming session onward unless the user explicitly approves a technically justified exception.

## Start here

For any project:

1. Determine the current phase.
2. If a project repository exists, read its root `PROJECT.md`.
3. Read `workflow/CONTEXT_ROUTING.md`.
4. Load only the workflow modules and project artifacts required for the current phase.
5. Follow the authority order declared by `PROJECT.md` and `workflow/contracts/PROJECT_REPOSITORY.md`.
6. Persist accepted project knowledge in the project repository instead of relying on chat memory.

Do not load execution contracts during ordinary brainstorming unless the current question requires them.

## Knowledge-state rule

`brainstorming/` is tentative. It is not a decision record.

Accepted decisions belong in `decisions/`; authoritative product requirements belong in `requirements/`; approved plans belong in `planning/`; execution state belongs in `implementation/`; milestone truth is summarized cumulatively in `project-handoffs/`.

Never treat an old brainstorm option as current policy merely because it exists in the repository.

## Phase routes

- Brainstorming → `workflow/BRAINSTORMING.md`
- Research → `workflow/RESEARCH.md`
- Planning → `workflow/PLANNING.md`
- Execution preparation → `workflow/EXECUTION_PREP.md`
- Execution / recovery / blocker handling → `workflow/EXECUTION.md`
- Milestone review / close / handoff → `workflow/REVIEW_AND_HANDOFF.md`
- Context selection rules → `workflow/CONTEXT_ROUTING.md`

Load contracts referenced by the selected phase only when needed.
