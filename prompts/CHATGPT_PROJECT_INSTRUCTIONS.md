# ChatGPT Project Instructions bootstrap

Paste this short block into ChatGPT Project Instructions for a project that uses Project Workflow. It is intentionally only a bootstrap pointer; detailed rules live in this workflow repository.

```text
This project uses `elmakus/chatgpt-codex-project-workflow`.

The current `main` of that repository is the Project Workflow authority. Start by reading its `CHATGPT.md`, then this project's root `PROJECT.md`, and use progressive disclosure: load only the workflow modules and project artifacts required for the current phase/task.

The project repository and `PROJECT.md` are the durable project source/router. Accepted durable state outranks stale chat memory.

Respect `execution_policy` in `PROJECT.md`:
- `chatgpt_only`: execute in normal ChatGPT chat only when the current session has all required capabilities and can produce required verification/evidence. Missing capability is a blocker. Do not hand work to Codex or change policy.
- `mixed`: ChatGPT remains project router. Execute in ChatGPT when the task can be correctly completed and verified here; use Codex only for a required capability/environment, material repo/runtime advantage, or explicit approved assignment.

Do not use ChatGPT Work for this workflow. Do not load Codex-specific instructions unless a Codex handoff is actually needed; then load only the minimum handoff contract.

For material external writes, perform readback/verification when it meaningfully validates the resulting state.
```
