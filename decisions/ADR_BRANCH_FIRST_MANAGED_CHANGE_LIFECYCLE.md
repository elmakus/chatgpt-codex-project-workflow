# Decision — branch-first managed-change lifecycle

- Decision ID: `ADR-BF-001`
- Date: `2026-09-20`
- Status: `accepted`
- Authority: `user`
- Supersedes: `legacy/default as a valid new-work path`
- Related requirements: `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` REQ-BF-001..007, REQ-BF-011..012, REQ-BF-016
- Related milestone/card: `none yet`

## Context

Project Workflow currently permits a new scope to progress through durable Brainstorming/Definition/Planning state on the integration target unless explicit branch-isolated intake was selected. Users may also begin with read-only exploration and only later decide to implement changes, so requiring early `#issue` / `#feature` syntax leaks workflow mechanics into normal use.

## Decision

Every new managed repository change is branch-first.

Read-only exploration may occur before a workstream exists. Once the user clearly authorizes a managed repository change, Project Workflow must create or recover an exact branch-isolated workstream before the first durable change-specific write. That same workstream spans the applicable lifecycle through final integration.

All managed changes integrate through a pull request and merge, including trivial changes.

`#issue` and `#feature` remain optional explicit shortcuts. Generic natural-language change authorization is a first-class entry and may use a neutral `change` workstream kind/naming convention until a narrower classification is useful.

Legacy/default root state is recovery/migration input only, never a new-work destination.

## Rationale

This makes the integration target unambiguously represent integrated truth, avoids in-progress plan/review state on `main`, enables parallel isolated work without requiring user knowledge of internal markers, and gives one durable identity to the whole change lifecycle.

## Alternatives considered

- Keep legacy/default as an equal new-work mode — rejected because it preserves ambiguous target semantics and two first-class state models.
- Require `#issue` / `#feature` — rejected because the user may not know the classification or even intend a change at the start of exploration.
- Create the branch only at Execution Prep — rejected because Definition/Planning/review state would still mutate the integration target.

## Consequences

- Routers/intake/bootstrap must detect generic managed-change intent.
- Workstream creation moves earlier than current Execution Prep-only cases.
- Existing legacy/default active state needs explicit migration/recovery handling.
- Small changes still get a branch/PR but may use a proportionate bounded lifecycle rather than unnecessary full planning.
- Concurrent branches may modify the same canonical root artifacts; target-refresh/conflict semantics remain mandatory.

## Required authoritative updates

- Requirements / Project Definition: `requirements/BRANCH_FIRST_MANAGED_CHANGES.md`
- Planning: branch-first migration/implementation plan required.
- Task Card/OpenSpec: JIT during Execution Prep.
- PROJECT.md: target model removes active workstream-local pointers.

## Provenance

- Source discussion/request: user explicitly requires no managed work on `main`, branch → PR → merge even for trivial changes, and no required `#issue` / `#feature` marker.
- Evidence/research: current `chatgpt_only` / `codex_only` routers, Intake, Workstreams and Repository contracts inspected from workflow `main`.
- Strategic `request_id`: none
- Exact `DECISION FOR CODEX:` marker: none
- Persisting commit: recorded by Git history.
