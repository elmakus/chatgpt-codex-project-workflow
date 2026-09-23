# Brainstorm — PWv2 architecture prior art

Date: 2026-09-23
Scope ID: pwv2-architecture-prior-art
Revision: R3
Status: tentative

## Problem / goal

Refactor the R1/R2 conclusions after correcting a key architecture boundary: Project Workflow is not the runtime orchestrator. The project intentionally separates repository-backed governance/policy from agent/model/tool orchestration.

R3 re-evaluates the prior-art set through two distinct target surfaces:

1. **Project Workflow v2.1** — governance, durable authority, legal role/phase transitions, exact subjects, evidence/review semantics, recovery and canonical state.
2. **Orchestration Runtime** — working neutral name for the full replacement of current `codex_workflow`; owns bounded worker/session execution, model/tool/resource selection, fan-out/fan-in, retries, runtime isolation and result transport.

A third classification, **Interface contract**, covers mechanisms whose semantics are owned by Project Workflow but whose technical enforcement belongs in the Orchestration Runtime.

The final product name of the replacement orchestration layer remains intentionally undecided.

## Current understanding

### Verified facts

- R1/R2 remain historical research evidence at `research/PWV2_ARCHITECTURE_PRIOR_ART_R1.md` and `R2.md`.
- All five upstream source HEADs inspected in R1/R2 are unchanged at R3 verification time, so the corrected result is a boundary/ownership reinterpretation rather than a source-mechanism change.
- R2 over-attributed multi-agent orchestration concerns to a PWv2 architectural refactor.
- Current `elmakus/codex_workflow` is an orchestration/swarm runtime fork with worker/profile/session lifecycle machinery; the user explicitly states that this layer is to be rebuilt rather than preserved as target architecture.
- Current `pi-unraid` research records that PWv2 remains workflow authority while external/native subagent orchestration must not silently become a second authority source.
- Current `pi-unraid` accepted governance confirms Project Workflow roles are authority roles distinct from model identities.
- R3 research is complete at `research/PWV2_ARCHITECTURE_PRIOR_ART_R3.md`.

### Existing accepted constraints

- Repository/Git-backed Project Workflow durable state remains canonical.
- Project Workflow does not own runtime scheduling from design.
- Orchestration runtime must not become a second project authority.
- Fresh independent-review semantics are defined by Project Workflow.
- Technical reviewer isolation/fresh-session enforcement belongs to runtime execution.
- No implementation or accepted architecture promotion in this scope.
- The current `codex_workflow` name/architecture is not presumed to survive; replacement naming is open.
- No complete PWv3 design in this scope.

## Corrected architecture boundary

```text
Project Workflow v2.1
  owns:
    canonical state / policy
    exact legal obligation
    role semantics
    authority/evidence requirements
    review freshness semantics
    legal transition/stop
             |
             | typed execution obligation
             v
Orchestration Runtime
  owns:
    worker/session launch
    model/provider/tool/resource mapping
    context transport
    fan-out/fan-in
    retry/runtime journal
    worktree/session isolation
    runtime observability
             |
             | typed result/evidence
             v
Project Workflow v2.1
  revalidates canonical preconditions
  and persists the legal transition
```

The runtime can execute repository/tool mutations as part of a role, but it does not decide that a Project Workflow phase/Card/review obligation has legally advanced.

## Reclassified source conclusions

- **rpiv-todo**: strongest direct PWv2.1 prior art for dependency graph validation, cycle rejection and derived ready/blocked views. Its session-local persistence remains rejected as canonical project state.
- **pi-fabric**: strongest tool-runtime prior art for code-mode composition, lazy capability discovery and bounded outer results. Mostly Orchestration Runtime, not PW policy.
- **Laya / System One**: optional non-authoritative runtime/advisory classifier for bounded semantic choices after calibration; not a Project Workflow route owner.
- **Dagu**: deterministic execution-engine prior art for retries, dependency scheduling, approval waits and schema validation. Useful for Orchestration Runtime and for the general state-machine pattern, but Dagu run state must not become PW authority.
- **pi-extensible-workflows**: strongest concrete Pi-native candidate/substrate for the replacement orchestration layer. It already provides fresh Pi agent sessions, roles/resource restrictions, output schemas, fan-out/pipelines, journaling/replay, worktrees, checkpoints and observability. Its bundled `reviewLoop` does not satisfy PW fresh-independent-review semantics as-is.

## Candidate ownership after R3

### Project Workflow v2.1

- deterministic policy/state validator and eventual executable policy evaluator for finite transitions;
- Task Card/Task Board dependency graph and cycle validator;
- canonical transition-record/schema validation;
- canonical execution-obligation manifest generation;
- canonical stale-result/precondition validation;
- derived ready/blocked/progress views from Git state.

### Orchestration Runtime

- provider/model-neutral worker launcher and adapter layer;
- fresh/continuation session lifecycle;
- role/tool/resource/context transport;
- fan-out/fan-in and pipeline execution;
- code-mode tool composition and lazy capability discovery;
- output-schema validation and bounded result transport;
- runtime journal/replay, retry, budgets, timeouts and concurrency;
- worktree isolation and mutation ownership;
- event-driven status/observability;
- optional calibrated System-One-style advisory classification.

### Shared interface contract

- typed Execution Obligation;
- typed Execution Result;
- abstract capability/mutation policy;
- fresh-review isolation contract;
- canonical branch/subject/head binding and stale-result rejection;
- user/checkpoint handshake;
- runtime failure taxonomy that reports facts without choosing the next PW route.

## Adaptive discovery state

### Accepted exploratory choices

| Choice | Counterfactual challenge | Stability note |
|---|---|---|
| Project Workflow is governance/policy, not runtime scheduler. | Combining both could reduce interfaces but would duplicate/blur authority and make runtime state part of project recovery. | Stable R3 conclusion. |
| Rebuild orchestration as a separate module/skill/extension. | Embedding scheduling into PW would violate the intended separation and make PW provider/runtime-specific. | Stable exploratory direction; not promoted. |
| Use "Orchestration Runtime" as a neutral research name. | Keeping `codex_workflowv2` would imply Codex-specific target semantics before a naming/product decision. | Stable for research only. |
| R1/R2 remain immutable historical research. | Rewriting them would erase the reason for R3 and obscure the corrected boundary. | Stable. |
| PW owns package semantics; runtime owns package delivery. | Letting runtime choose canonical authority would make orchestration a policy source; letting PW dictate concrete tool/provider wiring would over-couple governance to execution. | Stable R3 conclusion. |
| Fresh review requires both semantic and technical isolation. | A new session alone is insufficient if developer narrative is injected; canonical evidence alone is insufficient if runtime reuses contaminated session history. | Stable R3 conclusion. |

### Unresolved material decisions / dependencies

No architecture is accepted by this research.

Future Definition must decide, among other things:
- whether to adopt/wrap/fork pi-extensible-workflows or build a thinner Pi-native runtime from subagent primitives;
- final name/repository placement of the orchestration layer;
- exact typed execution-obligation/result schema;
- whether any optional classifier is worth operating after calibration.

### Reopened choices resolved by R3 research

- R2 A3/A4 are no longer classified primarily as PW architectural refactors; orchestration ownership moves to the replacement runtime.
- Context-package compilation is split: canonical authority selection/manifest belongs to PW, runtime delivery/materialization belongs to orchestration.
- Dagu and pi-extensible-workflows are execution prior art, not proposed PW authority engines.

## Research needed

Completed within R3.

Live prototype research would be needed only after a future Definition authorizes one of the runtime directions.

## Open questions

- Final orchestration product name. A provider-neutral name should probably avoid both `codex` and `workflow` to reduce confusion with Project Workflow; `Pi Role Runtime` is a descriptive candidate, not a decision.
- Adopt/wrap/fork `pi-extensible-workflows` versus implement a minimal role runtime directly on Pi-native subagent primitives.
- Exact capability abstraction exposed by Project Workflow versus concrete Pi tool selectors chosen by runtime.

## Outcome of this session

- Tentative conclusions: the clean target is **PWv2.1 policy kernel + separate provider-neutral role/orchestration runtime + typed boundary**. Most multi-agent/runtime mechanisms move out of PW. PWv2.1 should focus on deterministic policy enforcement, graph/state validation and canonical obligation production.
- Explicit user/product choices to promote through Project Definition: none beyond the user-supplied separation requirement used as a research constraint.
- Research still needed: none within R3.
- Next phase/action: R3 research scope complete; no implementation or Definition promotion is authorized.
- Definition promotion authorization: pending
- Definition promotion subject: none

> Nothing in this file becomes accepted requirement/decision authority by itself.
