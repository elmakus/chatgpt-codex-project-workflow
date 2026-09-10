# Codex Orchestration Integration Contract

## 1. Domain boundary

This repository governs **project workflow**, not the internal runtime orchestration of Codex.

Project Workflow remains authoritative for:
- Task Card scope and dependencies;
- accepted project requirements and planning boundaries;
- Refresh Gate and selective JIT OpenSpec obligations;
- durable GitHub execution state;
- acceptance, evidence and Definition of Done;
- strategic escalation boundaries;
- milestone close and cumulative handoff.

When the owner's `codex_workflow` is installed and enabled for Codex, that installed workflow is authoritative for **Codex runtime orchestration**, including matters such as:
- leaf versus Heavy routing;
- worker roles and model/reasoning choices;
- Companion/worker lifecycle;
- delegation mechanics;
- wait/event/message behavior;
- polling/silence policy;
- concurrency and worker-runtime recovery.

The source/update channel for that runtime workflow is `elmakus/codex_workflow`; Project Workflow must not duplicate or fork those runtime mechanics.

If `codex_workflow` is not installed or enabled, Codex may use its native runtime mechanisms, while all project-level obligations in this repository still apply.

## 2. Conflict rule

Apply authority by domain:

- project lifecycle, project state, Task Cards, OpenSpec obligations, evidence, acceptance and strategic authority → this Project Workflow;
- internal Codex orchestration/runtime mechanics → the installed/enabled `codex_workflow`;
- accepted product/system requirements and strategic decisions → the project's canonical requirements/decision artifacts.

Do not use a runtime-orchestration rule to override accepted project requirements or project acceptance criteria.

Do not use this Project Workflow to override worker/runtime mechanics owned by the installed `codex_workflow`.

## 3. Main accountability at the project boundary

Regardless of how runtime orchestration is implemented, the primary Codex agent remains accountable to Project Workflow for:
- the current Task Card outcome;
- scope and dependency boundaries;
- integration;
- required tests and acceptance;
- durable Git state;
- blocker escalation;
- final result pointers and evidence.

Delegation does not transfer project-level accountability for a card.

## 4. Worker strategic boundary

Workers/subagents do not independently change:
- product requirements;
- frozen strategic architecture;
- milestone acceptance criteria;
- strategic decisions.

If delegated evidence implies such a change, it must return to Main, which follows `workflow/contracts/CHATGPT_CODEX.md` when a strategic decision is required.

## 5. Completion boundary

Worker completion is not equivalent to Task Card completion.

Main must integrate and verify delegated output against the Task Card, relevant OpenSpec and `workflow/contracts/GITHUB_STATE.md` before the card can become `done`.

## 6. No shadow project-orchestration infrastructure

Do not build a parallel project-management/orchestration system without a concrete project need, such as:
- a task database;
- a Jira clone;
- a generic project DAG engine;
- a second workflow-state database;
- a custom project workflow engine;
- infrastructure whose only purpose is to mirror Task Board / Task Card / GitHub state.

This prohibition is about **project workflow infrastructure**. Internal Codex worker/runtime behavior belongs to the installed `codex_workflow` when enabled and is intentionally not re-specified here.

## 7. Loading rule

Project Workflow only requires this small integration contract to understand the boundary.

Do not read the remote `elmakus/codex_workflow` repository during ordinary project planning or execution merely because it is referenced here. When Codex has `codex_workflow` installed/enabled, its installed instructions are the runtime authority and are loaded according to that workflow's own rules.
