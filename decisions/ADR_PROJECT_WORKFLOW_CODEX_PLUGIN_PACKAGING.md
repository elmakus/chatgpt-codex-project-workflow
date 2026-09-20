# Decision — Project Workflow Codex plugin uses same-repository thin-wrapper packaging

- Decision ID: `ADR-PWCP-001`
- Date: `2026-09-20`
- Status: `accepted`
- Authority: `user/product`
- Supersedes: `none`
- Related requirements: `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md`
- Related milestone/card: `none`

## Context

Project Workflow needs a Codex plugin distribution surface. A separate plugin repository or a Skill containing copied Codex-only workflow semantics would introduce another synchronization boundary and risk drift from the canonical workflow.

## Decision

Package the Codex plugin from the existing `elmakus/chatgpt-codex-project-workflow` repository.

The plugin Skill is a thin wrapper/bootstrap that resolves the installed plugin root and enters normal Project Workflow routing. Canonical policy semantics remain in existing workflow files, including `workflow/codex_only/*`.

Routine changes to Codex-only workflow modules do not require Skill edits unless the bootstrap/entry contract itself changes.

A separate plugin repository may be introduced only if implementation proves a hard current-platform packaging constraint that cannot be satisfied in the existing repository; such evidence would require Definition reconsideration rather than an ad-hoc copy.

## Rationale

- preserves one source of truth;
- prevents manual workflow → Skill synchronization;
- allows marketplace/plugin updates to carry canonical workflow changes directly;
- keeps the Skill small enough for progressive disclosure;
- minimizes release and maintenance surfaces.

## Alternatives considered

### Separate Project Workflow plugin repository

Rejected for the accepted architecture because it creates duplicated packaging/state and a synchronization burden.

### Copy Codex-only routing/policy into SKILL.md

Rejected because it creates competing workflow authority.

### Fetch workflow from GitHub on every invocation

Rejected as the normal operating model because installed plugin contents should provide the versioned workflow snapshot and avoid unnecessary runtime network/context work.

## Consequences

- Plugin package layout must expose the canonical workflow files to its wrapper.
- Tests must prove wrapper path resolution and update propagation.
- `SKILL.md` changes only for bootstrap-contract changes, not ordinary workflow evolution.

## Required authoritative updates

- Requirements / Project Definition: `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md`.
- Planning: cover packaging, path resolution, update propagation and drift-prevention verification.
- Task Card/OpenSpec: materialize during Execution Prep if behavior-contract detail warrants it.
- PROJECT.md: point the active workstream to this accepted decision.

## Provenance

- Source discussion/request: user-authorized `project-workflow-codex-plugin@R1`.
- Evidence/research: existing repository structure and qualified Git-backed plugin baseline.
- Strategic `request_id`: none.
- Exact `DECISION FOR CODEX:` marker: none.
- Persisting commit: recorded by Git history.
