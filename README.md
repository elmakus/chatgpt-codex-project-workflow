# ChatGPT ↔ Codex Project Workflow

A GitHub-backed workflow for technical projects managed from normal ChatGPT chat, with execution performed by ChatGPT itself or by Codex according to project policy and the capabilities actually available for the task.

> Scope: this workflow uses **normal ChatGPT chat + Codex only**. ChatGPT Work is not part of the architecture, routing model or required operating mode.

## Core model

**ONE PROJECT = ONE REPOSITORY from the first idea.**

The project repository is durable project truth. It stores brainstorming, research, accepted decisions, requirements, approved planning, implementation state, OpenSpec, evidence and cumulative handoffs. This workflow repository stores only workflow rules, contracts, templates and bootstrap prompts.

Every project has a small root `PROJECT.md`. It is the context router and includes the user-selected execution policy:

- `chatgpt_only` — ChatGPT may execute work when the current chat session has the required capabilities and can produce the required verification/evidence. Missing capability blocks the task; policy never changes automatically.
- `mixed` — ChatGPT remains the project router and may either execute the task itself or hand it to Codex when Codex has a required capability/environment or a material repo/runtime advantage.

Execution is selected by a simple Capability Gate. There is no executor scoring system, capability database, agent graph or generic scheduler.

## Roles

ChatGPT is the strategic/research/planning agent and project router. It is also a full executor when the current session has the capabilities required by the Task Card, tests, evidence and readback obligations.

Codex is a specialized executor used when project policy allows it and it has a concrete capability or practical repo/runtime advantage.

The shared Project Workflow owns lifecycle, durable state, Task Cards, Refresh Gate, selective JIT OpenSpec, evidence, acceptance, recovery and milestone handoffs regardless of executor.

When the owner's `codex_workflow` is installed and enabled, it remains authoritative only for internal Codex runtime orchestration. Project Workflow does not duplicate those mechanics.

## Progressive disclosure

Agents read the smallest applicable path:

- ChatGPT starts at `CHATGPT.md`, then project `PROJECT.md`, then shared phase modules and ChatGPT-specific modules only when needed.
- Codex starts at `prompts/CODEX_START.md`, then project `PROJECT.md`, then shared execution modules and Codex-specific modules. Codex does **not** load `CHATGPT.md` or ChatGPT-specific execution instructions.
- ChatGPT may read `workflow/codex/HANDOFF.md` only when it must prepare or interpret a Codex handoff.

## Start an existing project

Use:

> Użyj mojego Project Workflow z `elmakus/chatgpt-codex-project-workflow`. Repo projektu: `elmakus/example-project`. Kontynuujemy <cel/faza>.

Current `main` is always the canonical Project Workflow authority.
