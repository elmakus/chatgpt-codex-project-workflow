# Codex Orchestration Integration Contract

## 1. Domain boundary

This repository governs **project workflow**, not internal runtime orchestration of Codex.

Project Workflow remains authoritative for:
- Task Card scope/dependencies;
- project-level serial versus bounded-parallel execution policy;
- Task Card mutable ownership (`write_scope`) and project-level exclusive resources;
- accepted requirements/planning boundaries;
- Refresh Gate and selective JIT OpenSpec;
- durable GitHub/external execution state, lane/base pointers and integration state;
- acceptance, evidence and Definition of Done;
- strategic escalation boundaries;
- milestone close and cumulative handoff.

When the owner's `codex_workflow` is installed/enabled for Codex, that installed workflow is authoritative for internal Codex runtime orchestration, including leaf/Heavy routing, worker roles/models, Companion/worker lifecycle, delegation, wait/event/message behavior, polling/silence, concurrency and worker-runtime recovery.

Source/update channel for that runtime workflow is `elmakus/codex_workflow`; Project Workflow must not duplicate/fork those mechanics.

If `codex_workflow` is not installed/enabled, Codex may use native runtime mechanisms while all project-level obligations here still apply.

## 2. Conflict rule

Apply authority by domain:
- project lifecycle/state/Task Cards/OpenSpec/evidence/acceptance/project-level lane ownership → Project Workflow;
- internal Codex worker selection/concurrency/runtime → installed `codex_workflow`;
- accepted product/system intent → canonical requirements/decisions.

Do not use runtime orchestration to override accepted requirements, Task Card dependencies, write ownership or acceptance. Do not use Project Workflow to override worker/runtime mechanics owned by installed `codex_workflow`.

## 3. Main accountability at project boundary

Regardless of runtime orchestration, primary Codex Main remains accountable to Project Workflow for the active Task Card or compatible Task Card set: scope/dependencies, lane isolation, integration order, required tests/acceptance, durable state, blocker escalation and final result pointers/evidence.

Delegation does not transfer project-level accountability.

In bounded-parallel mode, Codex Main is the project-level coordinator. It may map compatible Task Cards one-to-one to internal Executor workers, but the Task Card identities, dependencies and durable state remain Project Workflow facts.

## 4. Parallel Task Card mapping

When Task Board enables `bounded_parallel`:

1. Main reads the coordinator-selected ready set and confirms every selected card is within the project `parallel_card_limit`, explicitly `parallel_safe`, dependency-complete and pairwise compatible by `write_scope`/`exclusive_resources`.
2. Before workers rely on the state, Main ensures Task Board/card transitions, executor provenance, exact integration base and lane pointers are durably recorded according to `GITHUB_STATE.md`.
3. Each mutable Task Card lane gets an isolated branch/worktree or equivalent isolated mutable workspace. Never give two project-level lane workers the same mutable worktree/index.
4. Use the project Task Card ID as the worker Task ID when a worker owns that lane. Worker-internal subtasks may use subordinate IDs without creating new project Task Cards.
5. Lane workers own only their recorded implementation/test/evidence scope. They do not independently edit the Task Board, milestone-wide handoff/acceptance state or shared integration bookkeeping.
6. Main integrates completed lanes one at a time into the intended milestone branch, performs required cross-lane/post-integration verification, then updates Task Card result state.
7. If a worker discovers unexpected ownership overlap or a shared mutable external resource, it reports the material event to Main; Main serializes/re-scopes the affected lanes instead of allowing a write race.

The project `parallel_card_limit` is a ceiling over simultaneously active project Task Cards. It is not a replacement for `codex_workflow`'s internal judgment about useful worker count, and it does not require filling all available runtime slots.

## 5. Worker strategic boundary

Workers/subagents do not independently change product requirements, frozen strategic architecture, milestone acceptance, Task Card dependencies, project-level write ownership or strategic decisions. Evidence implying such a change returns to Main, which follows `workflow/codex/HANDOFF.md` when strategic resolution is required.

## 6. Completion boundary

Worker completion is not Task Card completion. Main must integrate/verify delegated output against Task Card, relevant OpenSpec and `workflow/contracts/GITHUB_STATE.md` before `done`.

For a parallel lane, an implementing worker may report GREEN on its isolated lane, but Main still owns integration and required post-integration verification. Independent review follows the Task Card contract and must remain independent of the implementing worker.

## 7. No shadow project-orchestration infrastructure

Do not build a parallel task database, Jira clone, generic project DAG engine, second workflow-state database, custom project workflow engine or infrastructure whose only purpose is to mirror Task Board/Card/Git state.

Explicit `depends_on`, Task Board state, bounded ownership metadata and ordinary Git lane branches/worktrees are sufficient project-level coordination state.

This prohibition concerns project workflow infrastructure. Internal Codex worker/runtime behavior belongs to installed `codex_workflow` when enabled.

## 8. Loading rule

Codex reads this small integration contract for the boundary. Do not read the remote `elmakus/codex_workflow` repository during ordinary project execution merely because it is referenced here; installed instructions are loaded according to that workflow's own rules.

Normal ChatGPT work does not load this file.
