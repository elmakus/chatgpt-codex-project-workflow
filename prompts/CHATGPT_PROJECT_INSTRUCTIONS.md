# ChatGPT Project Instructions bootstrap

Use a deliberately small bootstrap in ChatGPT Project Instructions. Detailed workflow behavior stays live in the workflow repository.

```text
This project uses `elmakus/chatgpt-codex-project-workflow`.

For project work, treat current `main` of that repository as workflow authority.

Start by reading:
1. workflow `CHATGPT.md`;
2. this project's root `PROJECT.md`;
3. workflow `workflow/CONTEXT_ROUTING.md`.

Follow only the execution-policy route selected by that router. Load only the route's required workflow modules/project artifacts and exact durable authority references.

The project repository is durable project truth. When implementation state exists, `implementation/TASK_BOARD.yaml` is the sole authoritative mutable execution-state record. Accepted durable state outranks stale chat memory.

Progressive disclosure is lossless by authority: read less, but never omit an applicable implementation-shaping constraint.

Do not duplicate workflow policy/execution/review rules in Project Instructions; recover them from current workflow `main` so new chats receive current semantics.

For user-facing normal ChatGPT responses, explain what happened, what it means and what happens next. Keep internal execution telemetry in durable state unless the exact value is materially actionable or explicitly requested.
```
