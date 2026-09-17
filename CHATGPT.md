# ChatGPT Project Workflow Router

This repository is the canonical project-workflow authority for projects managed through normal ChatGPT chat and/or Codex.

ChatGPT Work is outside this workflow. Do not route project work through ChatGPT Work or make it a prerequisite.

## Authority

- Current `main` of `elmakus/chatgpt-codex-project-workflow` is authoritative for workflow behavior.
- Project knowledge belongs in the project repository, not this workflow repository.
- Accepted durable project state outranks stale chat memory.
- One project uses one repository unless the user explicitly approves a technically justified exception.
- `implementation/TASK_BOARD.yaml` is the sole authoritative mutable execution-state record once implementation state exists.
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

Every project uses exactly one execution policy:

### `chatgpt_only`

Normal ChatGPT is the fixed Task Card executor. Do **not** run the Capability Gate.

Before and during execution, ChatGPT still verifies the capabilities/evidence path actually available to the current session. A missing required capability is a blocker; do not route to Codex or change policy automatically.

### `codex_only`

Codex is the fixed Task Card executor. Do **not** run the Capability Gate.

Normal ChatGPT may still perform strategy, research, planning, user-facing decisions and review when the workflow calls for them, but executable Task Cards are assigned to Codex. Once Codex is running an approved multi-milestone plan, Codex Main may continue automatically across GREEN milestone boundaries when the next milestone is already approved and no strategic/user-authorization gate intervenes.

A required capability missing from Codex is a blocker; do not fall back to ChatGPT or change policy automatically.

### `mixed`

ChatGPT remains project router. Before assigning the next Task Card or compatible ready set, use `workflow/chatgpt/CAPABILITY_GATE.md` to select ChatGPT, Codex or BLOCKED.

Project routing assumes the capability invariant:

`ChatGPT capabilities ⊆ Codex capabilities`

The gate is therefore a routing/practical-advantage mechanism, not a claim that ChatGPT may provide a capability unavailable to Codex.

Changing execution policy requires an explicit user decision.

## Milestone continuity

A milestone boundary is an acceptance/checkpoint boundary, not automatically a human-routing boundary.

Under `chatgpt_only` or `codex_only`, the fixed executor may continue from a GREEN milestone into the next already-approved milestone without a new Capability Gate or user prompt when:
- the next milestone is already accepted in the approved Master Plan;
- execution preparation is deterministic from durable authority;
- no explicit user/deployment/authorization gate is due;
- no strategic requirement/architecture/product decision is unresolved;
- the executor can run the required Refresh Gate and evidence path.

Under `mixed`, the next new execution assignment is routed through the Capability Gate.

## Phase routes

- Brainstorming → `workflow/BRAINSTORMING.md`
- Research → `workflow/RESEARCH.md`
- Planning → `workflow/PLANNING.md`
- Execution preparation → `workflow/EXECUTION_PREP.md`
- Shared execution/recovery → `workflow/EXECUTION.md`
- ChatGPT execution adapter → `workflow/chatgpt/EXECUTION.md`
- Milestone review/close/handoff → `workflow/REVIEW_AND_HANDOFF.md`
- Context rules → `workflow/CONTEXT_ROUTING.md`
