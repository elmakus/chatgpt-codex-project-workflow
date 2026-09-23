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
- R2 Research is complete at `research/PWV2_ARCHITECTURE_PRIOR_ART_R2.md`.
- `pi-extensible-workflows` is a Pi-native deterministic JavaScript workflow runtime with isolated agent sessions, role/resource selectors, output schemas, structural journaling/replay, checkpoints, worktrees and recovery.
- It materially strengthens R1's A2/A3 direction, but does not remove the need for a canonical deterministic PWv2 router/authority-package compiler.

### Existing accepted constraints

- Preserve the existing PWv2 durable authority model.
- Research only; do not implement any candidate.
- Do not design a complete PWv3.
- Do not promote findings into requirements, decisions or planning.
- External workflow/runtime state must not become a second authority source.
- Fresh independent-review boundaries remain a hard constraint.

### Assumptions to verify

Resolved for R2. The source is materially distinct enough to add evidence: it is more directly applicable to a future Pi-native execution substrate than Dagu, but its runtime journal and built-in reviewLoop cannot be adopted as PWv2 authority/review semantics without additional constraints.

## Ideas / alternatives considered

No architecture choice is accepted here.

## Trade-offs / questions

R2 records:
- exact execution/recovery mechanism;
- overlap with R1 pi-fabric/Dagu candidates;
- context, determinism/recoverability and role-isolation effects;
- fresh-review compatibility;
- runtime-state and side-effect failure modes;
- updated candidate classifications.

## Adaptive discovery state

### Accepted exploratory choices

| Choice | Counterfactual challenge | Stability note |
|---|---|---|
| Preserve the current durable authority model. | Explicit user constraint and R1 finding. | Stable for R2. |
| Research only; no implementation/promotion. | Explicit user constraint. | Stable for R2. |
| Treat R1 as immutable historical evidence and extend via R2. | Rewriting R1 would obscure the later scope extension. | Stable for R2. |
| Treat pi-extensible-workflows runtime state as execution cache/journal only, never PWv2 authority. | Its recovery is useful but can be lost/stale independently of Git. | Stable research conclusion, not promoted. |
| Do not use bundled reviewLoop as the PWv2 independent-review gate as-is. | It creates separate reviewer sessions, but explicitly feeds implementation summaries and previous review findings into them. | Stable research conclusion, not promoted. |

### Unresolved material decisions / dependencies

No product/strategic decision was made in R2. Any adoption decision must enter a future normal Project Definition / Planning route.

### Reopened choices

None.

## Research needed

Completed for R2.

## Open questions

Only future product/architecture choices remain:
- whether to evaluate pi-extensible-workflows as a concrete Pi-native execution substrate;
- whether to prototype a custom PWv2 fresh-review worker launch;
- whether to prototype a deterministic context-package compiler feeding its role/contextFiles/tool selectors.

These are intentionally not authorized here.

## Outcome of this session

- Tentative conclusions: pi-extensible-workflows strongly validates the R1 idea of deterministic orchestration around bounded workers and gives a Pi-native implementation path; its role/context isolation and journal replay are particularly relevant. It does not replace the canonical router/authority model, and its bundled reviewLoop is not compatible with PWv2 fresh independent review as-is.
- Explicit user/product choices to promote through Project Definition: none.
- Research still needed: none within R2.
- Open questions: which candidate experiments, if any, should later be promoted.
- Next phase/action: approved R2 research scope complete; no deterministic downstream work is authorized.
- Definition promotion authorization: pending
- Definition promotion subject: none

> Nothing in this file becomes accepted requirement/decision authority by itself.
