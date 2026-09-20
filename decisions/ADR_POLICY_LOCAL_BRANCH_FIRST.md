# Decision — policy-local realization of the shared branch-first invariant

- Decision ID: `ADR-BF-003`
- Date: `2026-09-20`
- Status: `accepted`
- Authority: `user`
- Supersedes: `none`
- Related requirements: `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` REQ-BF-015
- Related milestone/card: `none yet`

## Context

Both migrated fixed policies need the same branch-first product invariant, but `chatgpt_only` and `codex_only` differ materially in execution, review and orchestration semantics. The workflow already restricts `workflow/common/*` to genuinely policy-neutral contracts.

## Decision

The branch-first integration-target invariant may be stated once in genuinely policy-neutral authority documentation when useful, but all lifecycle/routing/intake/workstream/recovery mechanics are implemented and documented separately in `workflow/chatgpt_only/*` and `workflow/codex_only/*`.

No new shared Intake, Workstreams, Router, Execution Prep or lifecycle module is introduced.

## Rationale

This preserves one product invariant without recreating the cross-policy shared execution/lifecycle coupling that policy namespaces were designed to remove.

## Alternatives considered

- Put the whole branch-first implementation in `workflow/common/*` — rejected because policy behavior would quickly require conditional semantics.
- Duplicate even the one-sentence invariant with no shared authority statement — legal but needlessly increases risk of semantic drift.

## Consequences

- Planning must include equivalent policy-local updates and tests for both fixed policies.
- `workflow/common/AUTHORITY.md` may receive only policy-neutral wording about integration-target truth/branch-first managed changes.
- Policy-local route contracts remain the executable semantics.

## Required authoritative updates

- Requirements / Project Definition: `requirements/BRANCH_FIRST_MANAGED_CHANGES.md`
- Planning: separate ChatGPT-only and Codex-only implementation work packages.
- Task Card/OpenSpec: policy-local cards/contracts as needed.
- PROJECT.md: none beyond normal project authority navigation.

## Provenance

- Source discussion/request: user asked whether the change is common or must exist in both policies and accepted policy-local realization.
- Evidence/research: current `workflow/CONTEXT_ROUTING.md` and `workflow/common/AUTHORITY.md` policy-neutral boundary.
- Strategic `request_id`: none
- Exact `DECISION FOR CODEX:` marker: none
- Persisting commit: recorded by Git history.
