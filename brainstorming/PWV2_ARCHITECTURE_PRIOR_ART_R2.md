# Brainstorm — PWv2 architecture prior art

Date: 2026-09-23
Scope ID: pwv2-architecture-prior-art
Revision: R2
Status: tentative

## Problem / goal

Extend the completed R1 architectural prior-art research with one additional bounded source: `pi-extensible-workflows`. Determine whether it changes, strengthens, narrows or duplicates the R1 candidate improvements for PWv2.

## Current understanding

### Verified facts

- R1 is complete and consumed at `research/PWV2_ARCHITECTURE_PRIOR_ART_R1.md`.
- R1 covered pi-fabric, Laya/System One, Dagu and rpiv-todo.
- The user explicitly requested adding `pi-extensible-workflows` as a fifth prior-art source.
- This is a substantive extension of the exploratory evidence scope, so this record advances the same stable scope ID to R2 rather than rewriting R1 history.

### Existing accepted constraints

- Preserve the existing PWv2 durable authority model.
- Research only; do not implement any candidate.
- Do not design a complete PWv3.
- Do not promote findings into requirements, decisions or planning.
- External workflow/runtime state must not become a second authority source.
- Fresh independent-review boundaries remain a hard constraint.

### Assumptions to verify

- `pi-extensible-workflows` is a distinct enough mechanism to add evidence beyond R1 rather than merely duplicating pi-fabric or existing PWv2 patterns.
- Any useful mechanism can be expressed as a derived/executable aid while keeping canonical durable state in the repository.

## Ideas / alternatives considered

No architecture choice is accepted here.

## Trade-offs / questions

For `pi-extensible-workflows`, determine:
- how it works;
- what PWv2 problem it could solve;
- what PWv2 already solves;
- context impact;
- determinism/recoverability impact;
- role isolation / independent-review impact;
- new failure modes;
- whether it belongs in low-risk PWv2, architectural refactor, PWv3 prior art, or reject/no material benefit;
- whether it changes any R1 candidate classification.

## Adaptive discovery state

### Accepted exploratory choices

| Choice | Counterfactual challenge | Stability note |
|---|---|---|
| Preserve the current durable authority model. | Explicit user constraint and R1 finding. | Stable for R2. |
| Research only; no implementation/promotion. | Explicit user constraint. | Stable for R2. |
| Treat R1 as immutable historical evidence and extend via R2. | Rewriting R1 would obscure the later scope extension. | Stable for R2. |

### Unresolved material decisions / dependencies

No product/strategic decision is to be made in R2. The open item is evidence-only and delegated to Research.

### Reopened choices

None.

## Research needed

1. Identify the authoritative/current `pi-extensible-workflows` repository/source.
2. Inspect architecture, execution/routing model, state/recovery, context/tool behavior and validation.
3. Compare directly against current PWv2 and R1 findings.
4. Update the comparison/candidate analysis only where the new evidence materially changes it.

## Open questions

Evidence-dependent only.

## Outcome of this session

- Tentative conclusions: pending R2 Research.
- Explicit user/product choices to promote through Project Definition: none.
- Research still needed: `pi-extensible-workflows`.
- Open questions: exact fit against current PWv2 and R1.
- Next phase/action: research
- Definition promotion authorization: pending
- Definition promotion subject: none

> Nothing in this file becomes accepted requirement/decision authority by itself.
