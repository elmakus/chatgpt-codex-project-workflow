# Decision — workstream-local mutable routing and durable terminal provenance

- Decision ID: `ADR-BF-002`
- Date: `2026-09-20`
- Status: `accepted`
- Authority: `user`
- Supersedes: `root PROJECT.md active workstream-local exploratory/research pointers in the target model`
- Related requirements: `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` REQ-BF-008..010, REQ-BF-013..014, REQ-BF-017
- Related milestone/card: `none yet`

## Context

Root `PROJECT.md` currently acts as a high-level router but also carries active exploratory and pre-execution Research pointers. With multiple branch-isolated workstreams this makes a project-global file participate in branch-local mutable lifecycle state and creates avoidable merge conflicts.

Terminal workstream packages already provide a natural durable recovery/history unit.

## Decision

Root `PROJECT.md` represents integrated project-level identity, policy and authority navigation only. Active workstream-local mutable routing state belongs to the selected workstream manifest or exact workstream-owned records referenced from it.

Canonical root requirements/decisions/planning/source files may be changed on a workstream branch as the proposed future integrated state. Until merge, the integration-target versions remain canonical integrated truth.

After merge, the full terminal namespaced workstream package remains on the integration target indefinitely as durable provenance. No automatic archival/deletion policy is introduced.

## Rationale

This prevents concurrent workstreams from competing for project-global mutable pointers, keeps recovery branch-local while work is active, and preserves complete audit/recovery evidence after integration and source-branch deletion.

## Alternatives considered

- Keep active pointers in `PROJECT.md` — rejected because it turns a project-level integrated index into shared workstream state.
- Duplicate complete requirements/planning trees under every workstream — rejected because it creates synchronization and authority duplication.
- Delete terminal workstream state after merge — rejected because durable provenance/recovery is valuable and storage cost is acceptable.

## Consequences

- Workstream manifest schema/routing must gain the necessary pre-execution lifecycle pointers.
- Brainstorming/Research/Definition/Planning routes must resolve active state from the selected manifest instead of root `PROJECT.md`.
- Final integration retains namespaced workstream files on target.
- Root canonical artifact conflicts are handled through normal target refresh/PR integration rather than a second canonical tree.

## Required authoritative updates

- Requirements / Project Definition: `requirements/BRANCH_FIRST_MANAGED_CHANGES.md`
- Planning: include manifest schema, router, recovery and terminal package changes.
- Task Card/OpenSpec: JIT if schema contract warrants OpenSpec.
- PROJECT.md: target contract narrowed to integrated project-level pointers.

## Provenance

- Source discussion/request: user chose to keep terminal workstreams and accepted canonical root artifacts becoming truth only on merge.
- Evidence/research: existing target-side terminal package and workstream recovery contracts.
- Strategic `request_id`: none
- Exact `DECISION FOR CODEX:` marker: none
- Persisting commit: recorded by Git history.
