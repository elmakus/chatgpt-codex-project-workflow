# Codex Orchestration Integration Contract

## 1. Domain boundary

This repository governs **project workflow**, not internal runtime orchestration of Codex.

Project Workflow remains authoritative for:
- Task Card scope/dependencies;
- Task Board as sole mutable project execution state;
- project-level serial versus bounded-parallel policy;
- Task Card mutable ownership (`write_scope`) and exclusive resources;
- accepted requirements/planning boundaries;
- Refresh Gate and selective JIT OpenSpec;
- durable GitHub/external execution state, lane/base pointers and integration state;
- acceptance, evidence and Definition of Done;
- strategic escalation boundaries;
- milestone close/cumulative handoff;
- fixed-policy multi-milestone continuation rules.

When owner's `codex_workflow` is installed/enabled for Codex, that workflow is authoritative for internal Codex runtime orchestration, including leaf/Heavy routing, worker roles/models, Companion/worker lifecycle, delegation, wait/event/message behavior, polling/silence, concurrency and worker-runtime recovery.

Source/update channel for runtime workflow is `elmakus/codex_workflow`; Project Workflow must not duplicate/fork those mechanics.

If `codex_workflow` is not installed/enabled, Codex may use native runtime mechanisms while all project-level obligations here still apply.

## 2. Conflict rule

Apply authority by domain:
- project lifecycle/Task Board/Task Cards/OpenSpec/evidence/acceptance/project-level lane ownership → Project Workflow;
- internal Codex worker selection/concurrency/runtime → installed `codex_workflow`;
- accepted product/system intent → canonical requirements/decisions.

Do not use runtime orchestration to override accepted requirements, Task Card dependencies, write ownership, acceptance or user authorization gates.

## 3. Main accountability

Regardless of runtime orchestration, primary Codex Main remains accountable for active Task Card/set: scope/dependencies, lane isolation, integration order, required tests/acceptance, Task Board state, blocker escalation and final result pointers/evidence.

Delegation does not transfer project-level accountability.

Under `codex_only`, Codex Main also owns deterministic continuation across approved milestone boundaries when `workflow/EXECUTION.md` conditions are satisfied. It may perform allowed just-in-time execution prep but may not invent strategic authority.

## 4. Parallel Task Card mapping

When Task Board enables `bounded_parallel`:

1. Main reads coordinator-selected ready set and confirms every selected card is within limit, `parallel_safe`, dependency-complete and pairwise compatible by `write_scope`/`exclusive_resources`.
2. Before workers rely on state, Main ensures Task Board transitions, executor provenance, exact integration base and lane pointers are durably recorded.
3. Each mutable Task Card lane gets isolated branch/worktree or equivalent workspace. Never give two lane workers same mutable worktree/index.
4. Use project Task Card ID as worker Task ID when worker owns that lane. Worker-internal subtasks may use subordinate IDs without creating new project Task Cards.
5. Lane workers own only recorded implementation/test/evidence scope. They do not edit Task Board or milestone-wide handoff/acceptance/integration bookkeeping.
6. Main integrates completed lanes one at a time, performs required cross-lane/post-integration verification, then updates Task Board result state.
7. Unexpected ownership overlap/shared mutable external resource is reported to Main; Main serializes/re-scopes instead of allowing a write race.

`parallel_card_limit` is a ceiling over simultaneously active project Task Cards, not a worker-count target.

## 5. Independent review

When project review policy requires/recommends independent review under `codex_only`, Main may delegate review to a distinct reviewer worker/session that did not implement the subject. The reviewer must read exact durable subject/evidence rather than implementation narrative. Main remains accountable for integrating the verdict into milestone acceptance.

## 6. Worker strategic boundary

Workers/subagents do not independently change product requirements, frozen strategic architecture, milestone acceptance contracts, Task Card dependencies, project-level write ownership or strategic decisions. Evidence implying such change returns to Main, which follows `workflow/codex/HANDOFF.md` when strategic resolution is required.

## 7. Completion boundary

Worker completion is not Task Card completion. Main integrates/verifies delegated output against Task Card, relevant OpenSpec and `workflow/contracts/GITHUB_STATE.md` before Task Board card becomes `done`.

Independent review must remain independent of implementing worker.

## 8. No shadow project-orchestration infrastructure

Do not build a parallel task database, Jira clone, generic project DAG engine, second workflow-state database, custom project workflow engine or infrastructure whose only purpose is to mirror Task Board/Git state.

Explicit `depends_on`, Task Board state, bounded ownership metadata and ordinary Git lane branches/worktrees are sufficient project-level coordination state.

This prohibition concerns project workflow infrastructure. Internal Codex worker/runtime behavior belongs to installed `codex_workflow` when enabled.

## 9. Loading rule

Codex reads this small integration contract for boundary. Do not read remote `elmakus/codex_workflow` repository during ordinary project execution merely because referenced here; installed instructions load according to that workflow's rules.

Normal ChatGPT work does not load this file.
