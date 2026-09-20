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
- independent-review requirement, exact review subject and durable verdict/evidence;
- acceptance, evidence and Definition of Done;
- strategic escalation boundaries;
- milestone close/cumulative handoff;
- fixed-policy multi-milestone continuation rules.

When owner's `codex_workflow` is installed/enabled for Codex, that workflow is authoritative for **internal Codex runtime orchestration**, including leaf/Heavy routing, worker roles/models, execute/review role assignment, Companion/worker lifecycle, delegation, wait/event/message behavior, polling/silence, concurrency and worker-runtime recovery.

Source/update channel for runtime workflow is `elmakus/codex_workflow`; Project Workflow must not duplicate/fork those mechanics.

If `codex_workflow` is not installed/enabled, Codex may use native runtime mechanisms while all project-level obligations here still apply.

## 2. Conflict rule

Apply authority by domain:
- project lifecycle/Task Board/Task Cards/OpenSpec/evidence/acceptance/project-level lane ownership/review requirement → Project Workflow;
- internal Codex worker/reviewer selection, routing, concurrency and runtime mechanics → installed `codex_workflow`;
- accepted product/system intent → canonical requirements/decisions.

Do not use runtime orchestration to override accepted requirements, Task Card dependencies, write ownership, review independence, acceptance or user authorization gates.

## 3. Main accountability

Regardless of runtime orchestration, primary Codex Main remains accountable for active Task Card/set: scope/dependencies, lane isolation, integration order, required tests/acceptance, Task Board state, blocker escalation and final result/review pointers/evidence.

Delegation does not transfer project-level accountability.

Under `codex_only`, Codex Main also owns deterministic continuation across approved milestone boundaries when `workflow/EXECUTION.md` conditions are satisfied. It may perform allowed just-in-time execution prep but may not invent strategic authority.

Coordinator/session context hygiene is not a Project Workflow stop under `codex_only`. If the coordinating runtime is interrupted or replaced, Main reconstructs the exact project obligation from durable Project Workflow state and continues it; `codex_workflow` remains the owner of the concrete resume/replacement/session mechanics.

## 4. Runtime-operation behavior

Project Workflow does not maintain a catalog of Codex tools/capabilities and does not ask Codex Main to inventory them before execution.

Codex starts the approved work with its actual runtime. Ordinary executor-local remediation is handled by Codex/`codex_workflow` when permitted by the environment and accepted constraints.

Project Workflow becomes involved when a concrete required operation still cannot proceed. Persist the exact blocker and request only the smallest user-provided input/access/authorization actually required.

Under `mixed`, pre-assignment executor routing remains owned by ChatGPT Capability Gate; after Codex assignment, a runtime failure does not silently reroute the work.

## 5. Parallel Task Card mapping

When Task Board enables `bounded_parallel`:

1. Main reads coordinator-selected ready set and confirms every selected card is within limit, `parallel_safe`, dependency-complete and pairwise compatible by `write_scope`/`exclusive_resources`.
2. Before workers rely on state, Main ensures Task Board transitions, executor provenance, exact integration base and lane pointers are durably recorded.
3. Each mutable Task Card lane gets isolated branch/worktree or equivalent workspace. Never give two lane workers same mutable worktree/index.
4. Use project Task Card ID as worker Task ID when worker owns that lane. Worker-internal subtasks may use subordinate IDs without creating new project Task Cards.
5. Lane workers own only recorded implementation/test/evidence scope. They do not edit Task Board or milestone-wide handoff/acceptance/review/integration bookkeeping.
6. Main integrates completed lanes one at a time, performs required cross-lane/post-integration verification, then updates Task Board result state.
7. Unexpected ownership overlap/shared mutable external resource is reported to Main; Main serializes/re-scopes instead of allowing a write race.

`parallel_card_limit` is a ceiling over simultaneously active project Task Cards, not a worker-count target.

## 6. Independent review

When project review policy requires/recommends independent review under `codex_only`:

1. Main freezes/persists exact `review_subject`, implementation/test evidence and `review_state: pending` in Task Board.
2. Main delegates review to a distinct reviewer worker/session that did not implement the subject.
3. When installed/enabled, **`codex_workflow` decides the internal reviewer routing/role/model/lifecycle mechanics**; Project Workflow does not prescribe a duplicate reviewer orchestration system.
4. Reviewer reads exact durable subject/evidence rather than implementation narrative.
5. Main persists `review_state: in_progress`, then final `green|red` plus `review_evidence` as appropriate.
6. Main integrates the verdict into milestone acceptance/corrective work.

A reviewer worker must not be the implementing worker for that subject. A required/recommended independent review is not, by itself, a reason to return control to the user or normal ChatGPT under `codex_only`.

## 7. Worker strategic boundary

Workers/subagents do not independently change product requirements, frozen strategic architecture, milestone acceptance contracts, Task Card dependencies, project-level write ownership or strategic decisions. Evidence implying such change returns to Main, which follows `workflow/codex/HANDOFF.md` when strategic resolution is required.

## 8. Completion boundary

Worker completion is not Task Card completion. Main integrates/verifies delegated output against the Task Card, relevant OpenSpec and `workflow/contracts/TASK_EXECUTION.md`; load `GITHUB_STATE.md` additionally when coordinator/parallel/milestone state semantics are involved.

Reviewer-worker completion is not milestone acceptance until Main persists the exact verdict/evidence against the exact review subject.

## 9. No shadow project-orchestration infrastructure

Do not build a parallel task database, Jira clone, generic project DAG engine, second workflow-state database, custom project workflow engine or infrastructure whose only purpose is to mirror Task Board/Git state.

Explicit `depends_on`, Task Board state, bounded ownership metadata and ordinary Git lane branches/worktrees are sufficient project-level coordination state.

This prohibition concerns project workflow infrastructure. Internal Codex worker/runtime behavior belongs to installed `codex_workflow` when enabled.

## 10. Loading rule

Codex reads this small integration contract for boundary. Do not read remote `elmakus/codex_workflow` repository during ordinary project execution merely because referenced here; installed instructions load according to that workflow's own rules.

Normal ChatGPT work does not load this file.
