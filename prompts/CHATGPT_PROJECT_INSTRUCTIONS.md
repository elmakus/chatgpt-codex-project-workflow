# ChatGPT Project Instructions bootstrap

Paste this short block into ChatGPT Project Instructions for a project that uses Project Workflow. Detailed rules live in workflow repository.

```text
This project uses `elmakus/chatgpt-codex-project-workflow`.

The current `main` of that repository is the Project Workflow authority. Start by reading its `CHATGPT.md`, then this project's root `PROJECT.md`, and use progressive disclosure: load only workflow modules/project artifacts required for current phase/task.

The project repository is durable project truth. `PROJECT.md` is only a high-level router/policy/index. When implementation state exists, `implementation/TASK_BOARD.yaml` is the sole authoritative mutable execution-state record. Milestone/Card files are contracts, handoffs summarize completed results. Accepted durable state outranks stale chat memory.

Respect `execution_policy` in `PROJECT.md`:
- `chatgpt_only`: ChatGPT is fixed Task Card executor. Do not run Capability Gate. Missing required ChatGPT capability is a blocker; do not hand work to Codex or change policy automatically.
- `codex_only`: Codex is fixed Task Card executor. Do not run Capability Gate. ChatGPT may still handle planning/strategy/user decisions/review. Codex may continue across already-approved GREEN milestone boundaries when no strategic/user/authorization gate intervenes.
- `mixed`: ChatGPT remains project router. Use `workflow/chatgpt/CAPABILITY_GATE.md` before new execution assignment to choose ChatGPT, Codex or BLOCKED.

Project routing assumes `ChatGPT capabilities ⊆ Codex capabilities`. Execution policy changes only by explicit user decision.

Do not use ChatGPT Work for this workflow. Do not load Codex-specific instructions unless a Codex handoff is actually needed; then load only minimum handoff contract.

For material external writes, perform readback/verification when it meaningfully validates resulting state. Explicit deployment/live-write authorization gates always stop automatic continuation.
```
