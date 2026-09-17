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

Normal ChatGPT is the fixed Task Card executor. Do **not** run the Capability Gate and do **not** run a capability preflight/inventory/checklist before starting fixed-policy work.

Run the normal state/contract Refresh Gate and attempt the actual Task Card. If a concrete required operation cannot be performed with the current chat's tools/plugins/connectors, persist a runtime blocker and ask for the smallest remedy. The user may provide the missing access/tool or explicitly change execution policy; policy never changes automatically.

When REQUIRED/RECOMMENDED independent review is due, a chat that implemented the reviewed subject must persist exact review state and stop. A **fresh normal ChatGPT chat** performs that independent review.

### `codex_only`

Codex is the fixed Task Card executor. Do **not** run the Capability Gate and do **not** run a capability preflight/inventory/checklist before starting fixed-policy work.

Codex starts the approved work directly. Ordinary non-secret local tooling/dependency gaps should be self-remediated when the environment permits and accepted security/reproducibility constraints allow it. Missing MCP/credential/token/account permission/privileged access becomes a blocker only when a concrete required operation reaches it and Codex cannot obtain it itself.

Normal ChatGPT may still perform strategy, research, planning and user-facing decisions when the workflow calls for them. Once Codex is running an approved multi-milestone plan, Codex Main may continue automatically across GREEN milestone boundaries when no strategic/user-authorization gate intervenes.

When `codex_workflow` is installed/enabled, it controls internal Codex orchestration, including execute/review workers. REQUIRED/RECOMMENDED independent review is handled by an independent Codex reviewer worker/session without returning to ChatGPT merely for reviewer independence.

### `mixed`

ChatGPT remains project router. Before assigning the next Task Card or compatible ready set, use `workflow/chatgpt/CAPABILITY_GATE.md` to select ChatGPT, Codex or BLOCKED.

Project routing assumes the capability invariant:

`ChatGPT capabilities ⊆ Codex capabilities`

The gate is therefore a routing/practical-advantage mechanism, not a claim that ChatGPT may provide a capability unavailable to Codex.

Changing execution policy requires an explicit user decision.

## Milestone continuity

A milestone boundary is an acceptance/checkpoint boundary, not automatically a human-routing boundary.

Under `chatgpt_only` or `codex_only`, the fixed executor may continue from a GREEN milestone into the next already-approved milestone without a new Capability Gate or capability preflight when:
- the next milestone is already accepted in the approved Master Plan;
- execution preparation is deterministic from durable authority;
- every REQUIRED/RECOMMENDED independent-review gate for the completed subject is GREEN;
- no explicit user/deployment/authorization gate is due;
- no strategic requirement/architecture/product decision is unresolved.

Under `chatgpt_only`, the implementing chat must hand off to a fresh ChatGPT chat at required/recommended review boundaries; after GREEN, that fresh chat may continue deterministic execution.

Under `codex_only`, Codex Main may orchestrate execute/review workers according to installed `codex_workflow` and continue without a user handoff solely because a milestone/review boundary was crossed.

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
