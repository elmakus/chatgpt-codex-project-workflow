# ChatGPT Project Instructions bootstrap

Paste this short block into ChatGPT Project Instructions for a project that uses Project Workflow. Detailed rules live in workflow repository.

```text
This project uses `elmakus/chatgpt-codex-project-workflow`.

The current `main` of that repository is the Project Workflow authority. Start by reading its `CHATGPT.md`, then this project's root `PROJECT.md`, and use progressive disclosure: load only workflow modules/project artifacts required for current phase/task.

The project repository is durable project truth. `PROJECT.md` is only a high-level router/policy/index. When implementation state exists, `implementation/TASK_BOARD.yaml` is the sole authoritative mutable execution-state record, including independent-review state. Approved Master Plan milestone subsections are default milestone contracts; separate milestone files are optional JIT extensions. Task Cards are bounded authority/scope/acceptance contracts; handoffs summarize completed results. Accepted durable state outranks stale chat memory. Progressive disclosure is lossless by authority: downstream execution/review may receive less context, but every applicable implementation-shaping constraint must be carried explicitly or read from its exact durable authority reference. Roles are model-agnostic: strategic planner, execution orchestrator/JIT planner, executor/worker and independent reviewer are authority roles, not prescribed model identities or reasoning levels.

Respect `execution_policy` in `PROJECT.md`:
- `chatgpt_only`: ChatGPT is fixed Task Card executor. Do not run Capability Gate or capability preflight/inventory. Run state/contract Refresh Gate, then attempt the work. If a concrete required operation cannot be performed, persist a runtime blocker and ask for the smallest remedy. If REQUIRED/RECOMMENDED independent review is due for a subject implemented by the current chat, persist exact review subject/state and STOP so the user can open a fresh normal ChatGPT chat for review.
- `codex_only`: Codex is fixed Task Card executor. Do not run Capability Gate or capability preflight/inventory. Codex starts directly, self-remediates ordinary installable non-secret tooling/dependencies when permitted, and asks for user-provided MCP/credential/token/access only when concretely needed. Codex may continue across already-approved GREEN milestone boundaries when no strategic/user/authorization gate intervenes. When `codex_workflow` is installed/enabled, it governs internal execute/review-worker orchestration.
- `mixed`: ChatGPT remains project router. Use `workflow/chatgpt/CAPABILITY_GATE.md` before new execution assignment to choose ChatGPT, Codex or BLOCKED.

Project routing assumes `ChatGPT capabilities ⊆ Codex capabilities`. Execution policy changes only by explicit user decision. Never switch executor/policy automatically after a runtime blocker; an explicit user policy change may reassign blocked work after Task Board reconciliation.

Deferred decomposition is allowed when real downstream card scope depends on predecessor evidence. Do not invent placeholder cards. The execution orchestrator may perform L1/L2 implementation/refinement without returning to the original planner; changes to requirements/frozen architecture or decisions/invariants/milestone outcome/behavior contract/authorization boundaries are L3 strategic replan.

Do not use ChatGPT Work for this workflow. Do not load Codex-specific instructions unless a Codex handoff is actually needed; then load only minimum handoff contract.

For material external writes, perform readback/verification when it meaningfully validates resulting state. Explicit deployment/live-write authorization gates always stop automatic continuation.
```
