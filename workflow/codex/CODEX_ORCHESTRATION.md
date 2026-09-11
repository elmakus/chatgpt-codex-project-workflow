# Codex Orchestration Integration Contract

## Domain boundary

Project Workflow governs Task Card scope/dependencies, accepted requirements/planning boundaries, Refresh Gate, JIT OpenSpec, durable state, acceptance/evidence, strategic escalation and milestone handoff.

When the owner's `codex_workflow` is installed and enabled, it governs only internal Codex runtime orchestration: worker/model routing, delegation mechanics, Companion/worker lifecycle, waits/events/messages, polling/silence, concurrency and worker-runtime recovery.

Project Workflow must not duplicate or fork those runtime mechanics.

If `codex_workflow` is absent, Codex may use its native runtime mechanisms while all Project Workflow obligations remain unchanged.

## Conflict rule

- project lifecycle/state/scope/evidence/acceptance → Project Workflow;
- internal Codex orchestration → installed `codex_workflow`;
- product/system intent → canonical project requirements/decisions.

Runtime mechanics never override accepted project requirements.

## Main accountability

Regardless of delegation, the primary Codex agent remains accountable for current Task Card scope, integration, required tests/acceptance, durable state, blockers and evidence. Worker completion is not Task Card completion.

Workers/subagents do not independently rewrite requirements, frozen architecture, milestone acceptance or strategic decisions.

## No shadow project orchestration

Do not build a parallel task database, Jira clone, generic project DAG engine, second state database or custom project workflow engine merely to mirror Task Board/Card/Git state.

## Loading rule

Codex reads this small boundary contract when executing. ChatGPT does not need it during ordinary project work or its own execution.
