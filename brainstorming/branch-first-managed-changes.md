# Brainstorm — branch-first managed changes

Date: `2026-09-20`
Scope ID: `branch-first-managed-changes`
Revision: `R1`
Status: `ready_for_definition`

## Problem / goal

Project Workflow currently permits new work to remain in the legacy/default single-workstream context and allows exploratory/Definition/Planning durable state to be authored on the integration target before an implementation workstream branch exists. This makes `main` contain in-progress planning/review state and requires the user to know about `#issue` or `#feature` early enough to obtain branch isolation.

The target is a branch-first model in which the integration target represents integrated project truth and every managed repository change proceeds through a workstream branch, pull request and merge.

## Current understanding

### Verified facts

- Both `chatgpt_only` and `codex_only` currently support branch-isolated workstreams.
- Both policies also retain a legacy/default `implementation/TASK_BOARD.yaml` execution context for new work when no branch-isolated workstream is selected.
- Explicit `#issue` / `#feature` intake already creates a workstream branch before downstream feature/issue lifecycle work.
- Root `PROJECT.md` currently carries active exploratory and pre-execution Research pointers.
- Terminal branch-isolated workstream packages are already designed to survive on the integration target after merge/source-branch deletion.
- `workflow/common/*` remains legal only for genuinely policy-neutral contracts; lifecycle/routing mechanics are policy-local.

### Existing accepted decisions

- Project Workflow uses policy-specific namespaces for migrated `chatgpt_only` and `codex_only` semantics.
- Project repository state is durable truth; chat history is not required for recovery.

### Assumptions to verify

None material to Definition. Exact file-level implementation impact will be handled in Planning/Execution Prep.

## Ideas / alternatives considered

### Keep legacy/default as an equal new-work option

Rejected for new work. It preserves direct/in-progress state on the integration target and creates two first-class state models.

### Require explicit `#issue` / `#feature`

Rejected as a requirement. The user may begin with read-only exploration and only later decide to make a managed change, without knowing its eventual classification.

### Automatic generic managed-change intake

Accepted direction. Natural-language authorization to change the repository creates or recovers a branch-isolated workstream before the first durable project mutation. `#issue` and `#feature` remain optional explicit shortcuts/classifiers.

## Trade-offs / questions

- Branch-first work increases target-refresh/rebase/merge-conflict pressure, but isolates all in-progress state from integrated truth.
- Root canonical requirements/decisions/planning may be modified on the workstream branch as the proposed future project state; the integration-target version remains canonical integrated truth until merge.
- Workstream-local mutable routing/pointers must not use root `PROJECT.md` as a global active-state registry in the target design.

## Research needed

None before Definition.

## Open questions

None blocking.

## Outcome of this session

- Tentative conclusions: replace new-work legacy/default routing with mandatory branch-isolated managed-change workstreams for both fixed policies.
- Explicit user/product choices to promote through Project Definition:
  - every managed repository change uses branch → PR → merge, including trivial changes;
  - read-only exploration may precede workstream creation, but the branch must exist before the first durable managed-change write;
  - natural-language change authorization must be sufficient; `#issue` / `#feature` remain optional shortcuts;
  - legacy/default state remains only for recovery/migration of existing state, never as a destination for new work;
  - a workstream spans the whole managed-change lifecycle from discovery/brainstorming through Definition, Planning, implementation, review and integration;
  - root `PROJECT.md` represents integrated project truth and must not own active workstream-local mutable pointers in the target model;
  - terminal workstream packages remain on the integration target indefinitely as durable provenance;
  - root canonical artifacts may be edited on a workstream branch as proposed future integrated truth and become canonical on merge;
  - branch-first semantics apply to both `chatgpt_only` and `codex_only`; policy-specific mechanics stay in their own namespaces, with only genuinely policy-neutral invariants eligible for `workflow/common/*`.
- Research still needed: none.
- Open questions: none.
- Next phase/action: `ready for definition`
- Definition promotion authorization: `user_authorized`
- Definition promotion subject: `branch-first-managed-changes@R1`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
