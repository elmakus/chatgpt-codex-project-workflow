# Brainstorm — YAGNI / overengineering guard

Date: `2026-09-21`
Scope ID: `yagni-overengineering-guard`
Revision: `R1`
Status: `tentative`

## Problem / goal

Project Workflow already contains several local proportionality rules, but it does not currently state a general engineering principle against adding complexity for hypothetical future needs.

The goal is to decide whether to add an explicit YAGNI-style invariant: implement the simplest solution that satisfies current accepted requirements and evidence, and do not add speculative abstractions, extensibility, indirection, infrastructure, configuration or generalized machinery without a concrete current need.

## Current understanding

### Verified facts

- Current `main` has no literal rule named `YAGNI`, `KISS`, `overengineering`, `over-engineering`, `keep it simple`, or `future-proof` in repository search.
- The workflow already has narrower anti-complexity/proportionality rules:
  - progressive disclosure reads the smallest context required for the current obligation;
  - private-infrastructure access is limited to the smallest scope needed;
  - Brainstorming explicitly keeps simple scopes lightweight;
  - issue intake has a proportional micro-fix path for bounded low-risk changes;
  - delegated JIT planning forbids speculative placeholder Cards whose real scope depends on future evidence.
- Those rules constrain specific workflow mechanisms, but none acts as a general engineering decision rule when multiple technically valid implementations differ mainly in speculative future flexibility.

### Existing accepted decisions

- Project Workflow prefers proportional process for simple versus complex work.
- Planning and execution may not silently invent accepted product/system intent.
- Future implementation detail should be delayed when predecessor evidence is required.
- Progressive disclosure is selective by context but lossless by authority.

### Assumptions to verify

- A general anti-overengineering rule should be a default engineering invariant rather than an absolute ban on abstraction or extensibility.
- Extra complexity should remain legal when current accepted requirements, concrete evidence, compatibility constraints, safety, migration needs or demonstrated near-term reuse justify it.

## Ideas / alternatives considered

### Option A — Global YAGNI-style engineering invariant

State one policy-neutral principle that applies across Definition, Planning, Execution Prep, implementation and review:

> Prefer the simplest design that fully satisfies current accepted requirements, decisions and evidence. Do not add abstractions, generality, extensibility, configuration, infrastructure or future-proofing for hypothetical needs. Additional complexity requires a concrete present justification.

This would provide a single test reviewers and planners can apply without creating new lifecycle machinery.

### Option B — Planning/execution-only rule

Add the rule only to Planning / Execution Prep / Execution contracts.

This is narrower, but Brainstorming and Definition could still normalize speculative complexity before those phases.

### Option C — Keep only existing local rules

Make no general change and rely on current proportionality rules.

This avoids another invariant, but leaves the exact gap raised by this feature: there is no general criterion for rejecting speculative engineering that is technically valid but not currently needed.

## Trade-offs / questions

- A YAGNI rule should reject speculative complexity, not necessary complexity.
- “Simplest” must mean simplest solution that satisfies the whole accepted authority surface, not shortest code or fewest files.
- The rule should not prevent deliberate extension points when a current requirement, known compatibility surface, safety requirement, migration constraint or already-demonstrated reuse case requires them.
- The principle should remain small; adding scoring systems, complexity budgets or new lifecycle gates would itself violate the intent.

## Research needed

No blocking external research is required to decide the product direction. YAGNI is a well-established software-design principle; the repository-specific gap is already established from current `main`.

## Open questions

1. Should Project Workflow adopt Option A as a global policy-neutral engineering invariant, with the explicit exception that complexity is allowed when justified by a concrete current requirement/evidence?

Assistant recommendation: **yes**. This directly addresses overengineering while preserving necessary architecture and avoids creating extra process machinery.

## Outcome of this session

- Tentative conclusions: Project Workflow has several local proportionality rules but no general anti-overengineering invariant; a compact global YAGNI-style rule is the smallest coherent addition.
- Explicit user/product choices to promote through Project Definition: pending answer to Open question 1.
- Research still needed: none blocking.
- Open questions: 1 material product choice.
- Next phase/action: `continue brainstorming`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
