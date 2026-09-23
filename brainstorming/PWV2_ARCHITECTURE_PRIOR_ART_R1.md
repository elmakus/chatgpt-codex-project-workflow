# Brainstorm — PWv2 architecture prior art

Date: 2026-09-23
Scope ID: pwv2-architecture-prior-art
Revision: R1
Status: tentative

## Problem / goal

Evaluate whether four named prior-art mechanisms could materially improve the current PWv2 architecture without replacing its durable authority model or implementing changes in this workstream.

## Current understanding

### Verified facts

- Current PWv2 uses repository-backed durable authority and branch-isolated managed workstreams under chatgpt_only.
- WORKSTREAM.yaml, Task Board, Task Cards, requirements, decisions, review evidence and Git remain canonical durable state.
- The current request explicitly limits this scope to research and candidate evaluation.
- Research completed at research/PWV2_ARCHITECTURE_PRIOR_ART_R1.md.

### Existing accepted constraints

- Existing PWv2 durable authority is a constraint, not a target for replacement.
- No complete PWv3 design in this scope.
- No implementation or promotion into accepted requirements/decisions/planning in this scope.
- Session memory, todo UI, classifiers, external workflow engines and Fabric-style machinery cannot become a second authority source.

### Assumptions to verify

Resolved by the research artifact. The four prior-art families all contain useful mechanisms, but their fit differs sharply: graph/cycle validation and derived context/tool views fit incrementally; executable routing is a larger refactor; probabilistic typed classifiers are safe only as bounded/advisory mechanisms unless domain calibration proves otherwise.

## Ideas / alternatives considered

No architecture choice is accepted here. Candidate improvements are grouped in the research artifact under:
- PWv2 — low-risk incremental
- PWv2 — architectural refactor
- PWv3 prior art
- Reject / no material benefit

## Trade-offs / questions

The research records context, determinism/recoverability, role-isolation/review, authority, complexity and failure-mode trade-offs for each prior-art family.

## Adaptive discovery state

### Accepted exploratory choices

| Choice | Counterfactual challenge | Stability note |
|---|---|---|
| Preserve the current durable authority model as a hard constraint. | Not challenged: explicit scope constraint. | Stable for R1. |
| Research only; do not implement or promote findings. | Not challenged: explicit scope constraint. | Stable for R1. |
| Treat external runtimes/classifiers/UI as derived execution aids only. | Research found concrete second-authority failure modes if they own state. | Stable candidate constraint; not promoted. |

### Unresolved material decisions / dependencies

No product/strategic choice was resolved in this scope. Any decision to adopt a candidate must enter the normal future Project Definition / Planning route.

### Reopened choices

None.

## Research needed

Completed for R1. See research/PWV2_ARCHITECTURE_PRIOR_ART_R1.md.

## Open questions

Only future product/architecture choices remain, for example which candidate experiments, if any, the user wants to authorize. They are intentionally not decided here.

## Outcome of this session

- Tentative conclusions: low-risk value exists in derived dependency/cycle validation, on-demand capability discovery, bounded read-only tool composition and schema validation; executable routing/context-package compilation is promising but architectural; probabilistic classification needs domain-specific calibration and must not own hard authority gates.
- Explicit user/product choices to promote through Project Definition: none.
- Research still needed: none within R1.
- Open questions: which candidate improvements, if any, should be promoted into a future definition.
- Next phase/action: approved research scope complete; no deterministic downstream work is authorized.
- Definition promotion authorization: pending
- Definition promotion subject: none

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical requirements/ and decisions/.
