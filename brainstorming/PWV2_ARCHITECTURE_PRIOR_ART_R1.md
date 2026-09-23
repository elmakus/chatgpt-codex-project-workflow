# Brainstorm — PWv2 architecture prior art

Date: `2026-09-23`
Scope ID: `pwv2-architecture-prior-art`
Revision: `R1`
Status: `tentative`

## Problem / goal

Evaluate whether four named prior-art mechanisms could materially improve the current PWv2 architecture without replacing its durable authority model or implementing changes in this workstream.

## Current understanding

### Verified facts

- Current PWv2 uses repository-backed durable authority and branch-isolated managed workstreams under `chatgpt_only`.
- `WORKSTREAM.yaml`, Task Board, Task Cards, requirements, decisions, review evidence and Git remain canonical durable state.
- The current request explicitly limits this scope to research and candidate evaluation.

### Existing accepted constraints

- Existing PWv2 durable authority is a constraint, not a target for replacement.
- No complete PWv3 design in this scope.
- No implementation or promotion into accepted requirements/decisions/planning in this scope.
- Session memory, todo UI, classifiers, external workflow engines and Fabric-style machinery cannot become a second authority source.

### Assumptions to verify

- The named prior-art projects expose mechanisms materially comparable to PWv2 routing/context/recovery problems.
- Some deterministic or typed mechanisms may reduce interpretation/context cost without weakening role isolation or reviewer freshness.

## Ideas / alternatives considered

Research only. No architecture choice is accepted here.

## Trade-offs / questions

For each prior-art area, determine mechanism, overlap with existing PWv2 behavior, context/determinism/recovery/review impacts, failure modes, and whether it belongs as an incremental PWv2 improvement, architectural refactor, PWv3 prior art, or reject/no material benefit.

## Adaptive discovery state

### Accepted exploratory choices

| Choice | Counterfactual challenge | Stability note |
|---|---|---|
| Preserve the current durable authority model as a hard constraint. | Not challenged: explicit scope constraint. | Stable for R1. |
| Research only; do not implement or promote findings. | Not challenged: explicit scope constraint. | Stable for R1. |

### Unresolved material decisions / dependencies

No product/strategic choice is to be resolved in this scope. The unresolved items are evidence questions delegated to Research.

### Reopened choices

None.

## Research needed

1. `pi-fabric`: code-mode / typed tool composition, capability discovery/search/describe, multi-call branching/loops/fan-out outside the main transcript, intermediate-output/context control.
2. Laya / System One: typed/non-autoregressive classification, choice/score/boolean/probability decisions, routing/tool/evidence classification, escalation, confidence/calibration and safety boundaries.
3. Dagu and comparable deterministic workflow/state-machine patterns: retries, structured validation, approval gates, DAG/state transitions, and whether executable routing can replace some Markdown interpretation without replacing authority.
4. `rpiv-todo`: dependency graph, `blockedBy`, cycle detection, reload/compaction queue recovery, live progress UX, while keeping PWv2 Task Board/Cards canonical.

## Open questions

Evidence-dependent only; no user/product decision is required before the research.

## Outcome of this session

- Tentative conclusions: none before Research.
- Explicit user/product choices to promote through Project Definition: none.
- Research still needed: all four named areas.
- Open questions: source-grounded comparison against the current PWv2.
- Next phase/action: `research`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself.
