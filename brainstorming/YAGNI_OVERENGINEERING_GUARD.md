# Brainstorm — YAGNI / overengineering guard

Date: `2026-09-21`
Scope ID: `yagni-overengineering-guard`
Revision: `R2`
Status: `tentative`

## Problem / goal

Project Workflow already contains several local proportionality rules, but it does not currently state a general engineering principle against adding complexity for hypothetical future needs.

The goal is to add an explicit YAGNI-style invariant: implement the simplest solution that satisfies current accepted requirements and evidence, and do not add speculative abstractions, extensibility, indirection, infrastructure, configuration or generalized machinery without a concrete current need.

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

### Explicit user/product choices from this exploration

- Adopt the global YAGNI-style direction rather than limiting the rule to Planning/Execution or keeping only local proportionality rules.
- Treat YAGNI as a policy-neutral engineering invariant across the workflow.
- The invariant must reject speculative complexity without blocking complexity justified by concrete current requirements/evidence.
- Before Definition promotion, compare this direction against established external engineering practice and concrete public-repository rules.

## Chosen direction

Use one compact policy-neutral engineering invariant rather than a new lifecycle mechanism:

> Prefer the simplest design that fully satisfies current accepted requirements, decisions and evidence. Do not add abstractions, generality, extensibility, configuration, infrastructure or future-proofing for hypothetical needs. Additional complexity requires a concrete present justification.

“Simple” means the least complex solution that satisfies the complete accepted authority surface, not the shortest implementation or fewest files.

The final wording may be refined from Research evidence before Definition promotion.

## Trade-offs / questions

- A YAGNI rule should reject speculative complexity, not necessary complexity.
- The rule should not prevent deliberate extension points when a current requirement, known compatibility surface, safety requirement, migration constraint or demonstrated current reuse case requires them.
- The principle should remain small; scoring systems, complexity budgets or a new lifecycle gate would themselves be suspect unless Research reveals a concrete need.
- Research should distinguish useful operational patterns from slogans so the resulting invariant is actually reviewable.

## Research needed

Active Research: `research/YAGNI_PRACTICES_R1.md`.

Question: how do established engineering sources and public repositories operationalize YAGNI / anti-overengineering, and which concrete practices should Project Workflow adopt or avoid compared with the proposed global invariant?

## Open questions

No unresolved user/product decision is currently blocking Research. After Research returns, reconcile any evidence-backed wording/exception changes before deciding readiness for Definition.

## Outcome of this session

- Tentative conclusions: adopt a global policy-neutral YAGNI invariant, with wording to be refined against external practice.
- Explicit user/product choices to promote through Project Definition: global YAGNI direction and concrete-current-justification exception.
- Research still needed: external-practice comparison in `research/YAGNI_PRACTICES_R1.md`.
- Open questions: none requiring user input before Research.
- Next phase/action: `research`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
