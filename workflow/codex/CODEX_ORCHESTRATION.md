# Codex Orchestration Integration Contract

## 1. Domain boundary

This repository governs **project workflow**, not internal runtime orchestration of Codex.

Project Workflow remains authoritative for:
- Task Card scope/dependencies;
- accepted requirements/planning boundaries;
- Refresh Gate and selective JIT OpenSpec;
- durable GitHub/external execution state;
- acceptance, evidence and Definition of Done;
- strategic escalation boundaries;
- milestone close and cumulative handoff.

When the owner's `codex_workflow` is installed/enabled for Codex, that installed workflow is authoritative for internal Codex runtime orchestration, including leaf/Heavy routing, worker roles/models, Companion/worker lifecycle, delegation, wait/event/message behavior, polling/silence, concurrency and worker-runtime recovery.

Source/update channel for that runtime workflow is `elmakus/codex_workflow`; Project Workflow must not duplicate/fork those mechanics.

If `codex_workflow` is not installed/enabled, Codex may use native runtime mechanisms while all project-level obligations here still apply.

## 2. Conflict rule

Apply authority by domain:
- project lifecycle/state/Task Cards/OpenSpec/evidence/acceptance/strategic authority → Project Workflow;
- internal Codex orchestration/runtime → installed `codex_workflow`;
- accepted product/system intent → canonical requirements/decisions.

Do not use runtime orchestration to override accepted requirements/acceptance. Do not use Project Workflow to override worker/runtime mechanics owned by installed `codex_workflow`.

## 3. Main accountability at project boundary

Regardless of runtime orchestration, primary Codex agent remains accountable to Project Workflow for current Task Card outcome, scope/dependencies, integration, required tests/acceptance, durable state, blocker escalation and final result pointers/evidence.

Delegation does not transfer project-level accountability.

## 4. Worker strategic boundary

Workers/subagents do not independently change product requirements, frozen strategic architecture, milestone acceptance or strategic decisions. Evidence implying such a change returns to Main, which follows `workflow/codex/HANDOFF.md` when strategic resolution is required.

## 5. Completion boundary

Worker completion is not Task Card completion. Main must integrate/verify delegated output against Task Card, relevant OpenSpec and `workflow/contracts/GITHUB_STATE.md` before `done`.

## 6. No shadow project-orchestration infrastructure

Do not build a parallel task database, Jira clone, generic project DAG engine, second workflow-state database, custom project workflow engine or infrastructure whose only purpose is to mirror Task Board/Card/Git state.

This prohibition concerns project workflow infrastructure. Internal Codex worker/runtime behavior belongs to installed `codex_workflow` when enabled.

## 7. Loading rule

Codex reads this small integration contract for the boundary. Do not read the remote `elmakus/codex_workflow` repository during ordinary project execution merely because it is referenced here; installed instructions are loaded according to that workflow's own rules.

Normal ChatGPT work does not load this file.
