# Common Authority Contract

This file contains only policy-neutral authority rules.

## Durable authority

- Current workflow `main` is authoritative for workflow behavior unless an explicitly frozen in-flight boundary says otherwise.
- Project repository is durable project truth.
- Root `PROJECT.md` is a high-level router/index, not live execution state. It may locate exact pre-execution continuation records such as an active exploratory scope or active Research obligation; lifecycle/detail remains owned by the pointed record.
- When implementation state exists, `implementation/TASK_BOARD.yaml` is the sole authoritative mutable execution-state record.
- Accepted durable repository state outranks stale chat/session narrative.

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
