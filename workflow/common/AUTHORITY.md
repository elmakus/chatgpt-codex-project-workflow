# Common Authority Contract

This file contains only policy-neutral authority rules.

## Durable authority

- Current workflow `main` is authoritative for workflow behavior unless an explicitly frozen in-flight boundary says otherwise.
- Project repository is durable project truth.
- Root `PROJECT.md` is a high-level integrated-project router/index, not live workstream execution or pre-execution routing state.
- When implementation state exists, the **canonical Task Board selected by the active policy route** is the sole authoritative mutable Card/milestone execution-state record. A historical root `implementation/TASK_BOARD.yaml` may remain recoverable where a policy route explicitly supports legacy migration, but its existence is not permission to use root/default state as the destination for new branch-first managed work.
- Accepted durable repository state outranks stale chat/session narrative.

## Branch-first managed-change invariant

For execution-policy routes that adopt the branch-first managed-change model:
- the integration target represents integrated project truth;
- read-only exploration may precede workstream creation, but an exact branch-isolated workstream must exist before the first durable change-specific Project Workflow or project-source write;
- managed changes reach the integration target through branch → pull request → merge rather than normal direct target mutation;
- historical root/default mutable state is recovery/migration input, not a new-work destination.

The policy-local route owns Intake, naming, migration, lifecycle, review and recovery mechanics. This common contract states only the policy-neutral invariant.

## Role semantics

Definition owner, strategic planner, execution orchestrator/JIT planner, executor and independent reviewer are authority roles, not prescribed model identities or reasoning levels.

Policy-specific routes decide which runtime performs a role; the common authority model does not.

## Workflow repository versus project repository

The workflow repository contains workflow rules, contracts, templates, prompts and workflow history only.

Project-specific knowledge, decisions, requirements, plans, execution state, evidence, handoffs and project source/code belong in the project repository.

Do not use the workflow repository as a second project-state store.

## Authority precedence

Apply authority by domain:

1. workflow behavior → current workflow `main`;
2. accepted product/system intent → canonical requirements + accepted decisions produced/reconciled by Definition;
3. approved execution intent → Master Plan milestone + valid JIT extension;
4. live execution truth → Task Board + exact Git/runtime/external evidence;
5. bounded implementation/acceptance contract → Task Card + relevant OpenSpec;
6. completed checkpoint summary → cumulative handoff + referenced exact state;
7. research → evidence, not decision;
8. brainstorming → tentative until promoted.

`PROJECT.md` points to authority; it does not override referenced authority.

A Task Card narrows execution scope but does not override richer requirements/decisions/approved-plan authority. Actual code/runtime is implementation evidence, not permission to silently rewrite accepted strategic authority.

## Progressive disclosure

Read the smallest context required for the current obligation, but never omit an applicable implementation-shaping constraint.

Exact durable references outrank summaries. A downstream role may receive less context than an upstream role only when every applicable constraint is either carried explicitly without semantic change or read from its exact durable authority.
