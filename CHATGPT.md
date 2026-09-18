# ChatGPT Project Workflow Router

This is the minimal normal-ChatGPT entrypoint for projects using this workflow.

ChatGPT Work is outside this workflow.

## Durable authority

- Current `main` of `elmakus/chatgpt-codex-project-workflow` is authoritative for workflow behavior unless an explicitly frozen in-flight boundary says otherwise.
- Project-specific truth lives in the project repository.
- Project root `PROJECT.md` is the high-level router/index, not live execution state.
- When implementation state exists, `implementation/TASK_BOARD.yaml` is the sole authoritative mutable execution-state record.
- Accepted durable repository state outranks stale chat memory.
- Workflow roles are model-agnostic; this router does not choose models or reasoning levels.
- `execution_policy` comes from project `PROJECT.md` and never changes automatically; changing it requires an explicit user decision.

## Bootstrap

For every normal ChatGPT project task:

1. Read the project root `PROJECT.md`.
2. Read `workflow/CONTEXT_ROUTING.md`.
3. If `PROJECT.md` or the user's request indicates implementation, a Task Card/milestone, review, blocker or recovery state, read the project's Task Board before choosing the final route.
4. Select the single primary route that matches the current obligation. A pending/in-progress REQUIRED/RECOMMENDED independent review outranks later dependent implementation.
5. Load only the route's **REQUIRED** workflow modules and project artifacts.
6. Load a **CONDITIONAL** item only when its stated trigger is actually present.
7. Follow exact durable authority references from the current card/milestone/review subject instead of loading whole trees "just in case".
8. Persist accepted project knowledge/state back to the project repository when the task changes durable truth.

Progressive disclosure is **lossless by authority, selective by context**: read less, but never omit an applicable authoritative constraint.

## Default non-loading rules

Unless the selected route explicitly says otherwise:

- do not load unrelated phase modules;
- do not load the complete requirements/plan/OpenSpec/history tree when exact refs identify the applicable slice;
- do not load `workflow/codex/*` during ordinary ChatGPT work;
- ChatGPT may load `workflow/codex/HANDOFF.md` only when preparing/interpreting an actual Codex handoff or strategic Codex escalation;
- do not load Codex execution/orchestration modules merely to understand normal ChatGPT work;
- do not run Capability Gate unless the selected route requires a new assignment under `execution_policy: mixed`;
- do not perform fixed-policy capability preflight/inventory.

## Human control surface

These rules apply to **every normal ChatGPT route**, including planning, execution, independent review, blockers and close/publication.

By default, a user-facing response reports only:
1. what happened / what was found;
2. what it means;
3. what happens next or the smallest user action.

Keep durable execution telemetry in the repository. Do not dump SHAs, branch/HEAD pointers, evidence paths, raw Task Board fields, long test inventories/counts, changed-file lists or internal bookkeeping unless the user asks or the exact value is materially required for action/debugging/recovery/security.

Do not end the chat turn merely to announce deterministic work that the current route is authorized to continue. Continue first and respond when a real workflow stop/boundary is reached.

Whenever a fresh ChatGPT chat is required or recommended, include the ready-to-copy branch-aware start prompt in that same response.

## Route index

The deterministic read sets live in `workflow/CONTEXT_ROUTING.md`:

- Brainstorming
- Research
- Planning
- Execution preparation
- ChatGPT execution
- Codex execution
- Independent review
- Milestone close/publication
- Strategic blocker
- Failure recovery

This file intentionally does not duplicate execution-policy, review, continuation or executor semantics from their owning modules.
