# Brainstorm — PWv2 architecture prior art

Date: 2026-09-23
Scope ID: pwv2-architecture-prior-art
Revision: R3
Status: tentative

## Problem / goal

Refactor the R1/R2 conclusions after correcting a key architecture boundary: Project Workflow is not the runtime orchestrator. The project intentionally separates repository-backed governance/policy from agent/model/tool orchestration.

R3 must re-evaluate the prior-art set through two distinct target surfaces:

1. **Project Workflow v2.1** — governance, durable authority, legal role/phase transitions, exact subjects, evidence/review semantics, recovery and canonical state.
2. **Orchestration Runtime** — working neutral name for the full replacement of current `codex_workflow`; owns bounded worker/session execution, model/tool/resource selection, fan-out/fan-in, retries, runtime isolation and result transport.

A third classification, **Interface contract**, covers mechanisms whose semantics are owned by Project Workflow but whose technical enforcement belongs in the Orchestration Runtime.

The final product name of the replacement orchestration layer is intentionally undecided in this research.

## Current understanding

### Verified facts

- R1/R2 research is durable at `research/PWV2_ARCHITECTURE_PRIOR_ART_R1.md` and `R2.md`.
- R2 over-attributed multi-agent orchestration concerns to a PWv2 architectural refactor.
- Current `elmakus/codex_workflow` is explicitly an orchestration/swarm runtime fork with worker/profile/session lifecycle machinery; the user states it is to be rebuilt rather than treated as the target architecture.
- Current `pi-unraid` research records the intended principle that PWv2 remains workflow authority while external/native subagent orchestration must not silently become a second authority source.
- Current `pi-unraid` accepted governance confirms Project Workflow roles are authority roles distinct from model identities.
- The user explicitly requested that the complete prior-art research be reclassified into PWv2.1 versus a rebuilt orchestration layer.

### Existing accepted constraints

- Repository/Git-backed Project Workflow durable state remains canonical.
- Project Workflow does not own runtime scheduling from design.
- Orchestration runtime must not become a second project authority.
- Fresh independent review semantics are defined by Project Workflow.
- Technical reviewer isolation/fresh-session enforcement belongs to runtime execution.
- No implementation or accepted architecture promotion in this scope.
- The current `codex_workflow` name/architecture is not presumed to survive; replacement naming is open.
- No complete PWv3 design in this scope.

## Research questions

For each of pi-fabric, Laya/System One, Dagu, rpiv-todo and pi-extensible-workflows:

1. Which mechanisms belong to PWv2.1?
2. Which belong to the replacement Orchestration Runtime?
3. Which are interface-contract mechanisms spanning both layers?
4. Which should be rejected?
5. What problem does each solve that the owning layer does not already solve?
6. What are context, determinism/recovery, role-isolation/review and failure-mode effects?
7. Does the mechanism require a new authority decision or can it be derived/implementation-only later?

Also inspect the current `elmakus/codex_workflow` only as legacy/current-state prior art to understand responsibilities worth preserving or discarding, not as target authority.

## Desired boundary to test, not assume

```text
Project Workflow v2.1
  - canonical state / policy
  - exact legal obligation
  - role semantics
  - authority/evidence requirements
  - review freshness semantics
          |
          | bounded execution contract
          v
Orchestration Runtime
  - spawn/select worker
  - model/tools/resources
  - context delivery
  - parallelism/retry/runtime journal
  - worktree/session isolation
          |
          | structured result/evidence
          v
Project Workflow v2.1
  - validate/persist legal transition
```

Research must challenge this split and identify any responsibilities placed on the wrong side.

## Adaptive discovery state

### Accepted exploratory choices

| Choice | Counterfactual challenge | Stability note |
|---|---|---|
| Project Workflow is governance/policy, not the runtime scheduler. | R1/R2 were checked against current codex_workflow and pi-unraid durable material; both support a separate orchestration layer. | Stable for R3. |
| Rebuild orchestration as a separate module/skill/extension rather than embedding scheduling into PWv2.1. | A single combined engine would simplify local control but would blur authority/runtime boundaries and create second-authority risk. | Stable exploratory direction; not promoted. |
| Use a neutral working name "Orchestration Runtime". | Keeping `codex_workflowv2` would prematurely freeze identity around a legacy Codex-specific implementation. | Stable for research only; final name unresolved. |
| Treat R1/R2 as historical evidence, not rewrite them. | Rewriting would hide the corrected architecture interpretation. | Stable. |

### Unresolved material decisions / dependencies

No product architecture choice is authorized in R3. Research should produce candidate sets and recommended ownership only.

### Reopened choices

- R2 Candidate A3/A4 ownership: reopened because multi-agent orchestration belongs primarily to the orchestration layer, not Project Workflow.
- R1/R2 interpretation of Dagu and pi-extensible-workflows: reopened under the corrected layer boundary.
- Context-package compiler ownership: reopened as a likely split semantic/runtime interface.

## Research needed

Re-evaluate all five prior-art sources plus current codex_workflow/current Pi project boundary evidence and produce:
- responsibility matrix;
- PWv2.1 candidate set;
- Orchestration Runtime candidate set;
- shared interface-contract candidate set;
- rejects;
- migration/validation experiments;
- explicit corrections to R1/R2.

## Open questions

- Exact product name and repository placement for the replacement orchestration layer.
- Whether pi-extensible-workflows should be adopted, wrapped, forked, or only mined for mechanisms.
- How much of bounded package compilation belongs in Project Workflow versus runtime transport.

These remain research questions or later product choices, not implicit decisions.

## Outcome of this session

- Tentative conclusions: pending R3 Research.
- Explicit user/product choices to promote through Project Definition: none.
- Research still needed: full boundary-aware re-evaluation.
- Next phase/action: Research.
- Definition promotion authorization: pending
- Definition promotion subject: none

> Nothing in this file becomes accepted requirement/decision authority by itself.
