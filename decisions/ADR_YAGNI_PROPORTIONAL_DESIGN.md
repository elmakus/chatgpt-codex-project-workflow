# Decision — Adopt YAGNI as a policy-neutral proportional-design invariant

- Decision ID: `ADR-YAGNI-001`
- Date: `2026-09-21`
- Status: `accepted`
- Authority: `user`
- Supersedes: `none`
- Related requirements: `requirements/YAGNI_OVERENGINEERING_GUARD.md`
- Related milestone/card: `none`

## Context

Project Workflow already contains local proportionality mechanisms such as lightweight Brainstorming, bounded Task Cards, micro-fix handling, progressive disclosure and JIT planning. It lacks one general engineering rule for deciding whether technically valid extra abstraction/generalization/configuration/infrastructure is justified now or exists only to “future-proof” hypothetical needs.

External Research found a consistent engineering pattern: solve the concrete present problem, avoid speculative abstraction/genericity, keep changes focused, and preserve refactoring/testing/code malleability rather than treating YAGNI as a reason to reduce quality.

## Decision

Adopt YAGNI / proportional design as one policy-neutral engineering invariant across Project Workflow.

The invariant:
- prefers the least-complex solution that fully satisfies current accepted authority and verified evidence;
- rejects speculative abstractions, genericity, extensibility, configuration, dependencies, infrastructure, compatibility paths and future-proofing whose only justification is hypothetical future need;
- requires every material complexity increase to have a concrete present justification;
- explicitly preserves current correctness, security, testing, maintainability/refactoring, compatibility, observability, migration and other applicable obligations;
- permits abstractions/generalization when demonstrated current variation/shared concepts or other current constraints justify them;
- treats existing fitting mechanisms as preferred, not mandatory, when they satisfy the current authority cleanly;
- uses the existing planning/execution/review lifecycle rather than creating a dedicated YAGNI gate/state subsystem.

The operational review question is:

> Which current requirement, accepted constraint, verified evidence, existing contract or demonstrated current reuse justifies this material extra complexity?

“Maybe later” alone is insufficient.

## Rationale

A policy-neutral invariant closes the gap at the earliest decision points and remains available to planning, execution and review without duplicating semantics across policy namespaces.

The concrete-current-justification test is reviewable and evidence-based without inventing numeric complexity metrics. Explicit quality guardrails prevent a simplistic reading of YAGNI from degrading code malleability or current acceptance obligations.

Keeping the rule in existing authority/routing machinery also applies YAGNI to itself: no new lifecycle, score, registry or gate is warranted.

## Alternatives considered

- **Keep only existing local proportionality rules** — rejected because no general engineering decision rule covers speculative implementation/design complexity.
- **Apply YAGNI only during Planning/Execution** — rejected because speculative complexity may be normalized earlier or escape later review.
- **Bare “keep it simple / YAGNI” slogan** — rejected because it can be misread as reducing testing/refactoring/quality rather than speculative complexity.
- **Numeric rule-of-three / complexity score / budget** — rejected because evidence is context-sensitive and extra machinery is not currently justified.
- **Always prefer duplication** — rejected; duplication is only preferable when the alternative is a premature/wrong abstraction and current evidence does not yet reveal a stable shared concept.

## Consequences

- One canonical common invariant must be introduced or extended in policy-neutral workflow authority.
- Policy-local roles should consume/reference that common rule only where needed to make planning, implementation and review behavior explicit.
- Tests must distinguish unjustified speculative complexity from justified current complexity and prove that quality/authority obligations still win.
- Review/audit language can use the concrete-current-justification question without creating new review state.
- Future features that genuinely need extensibility/generalization can still adopt it by documenting the current authority/evidence that justifies the complexity.

## Required authoritative updates

- Requirements / Project Definition: `requirements/YAGNI_OVERENGINEERING_GUARD.md`.
- Planning: create a bounded Master Plan mapping the common invariant and minimum policy-local/test/docs integration.
- Task Card/OpenSpec: determine the smallest behavior-contract/test package in Execution Prep; no YAGNI-specific state object.
- PROJECT.md: workstream-local authority remains in the branch-isolated manifest; no root live-state mirror is needed.

## Provenance

- Source discussion/request: user-promoted `yagni-overengineering-guard@R3`.
- Evidence/research: `research/YAGNI_PRACTICES_R1.md`.
- Strategic `request_id`: none.
- Exact `DECISION FOR CODEX:` marker: none.
- Persisting commit: recorded by repository history.
