# Independent Plan Review — CCOR-P1

Plan revision: CCOR-P1
Review requirement: RECOMMENDED
Review state: red
Review subject: 8dc6178fe8eeee1478a81b4bb94b179a1dab0006:planning/CODEX_ORCHESTRATION_CONTEXT_RECOVERY_MASTER_PLAN.md
Review evidence: RED — bounded plan-only defects; see Findings below.

## Authority

- Approved Definition: `requirements/CODEX_ORCHESTRATION_CONTEXT_RECOVERY.md` R2
- Accepted decision: `decisions/ADR_CODEX_ORCHESTRATION_POLICY_BINDING.md`
- Workstream: `implementation/workstreams/issue-codex-compaction-routing-recovery/WORKSTREAM.yaml`

## Review scope

Audit the exact frozen plan subject for:
- complete CCOR-R1…R10 coverage;
- correct treatment of same-version context compaction as the primary failure;
- separation of durable policy binding from the non-durable current-context latch;
- preservation of the Project Workflow ↔ `codex_workflow` responsibility boundary;
- fail-closed worker dispatch without duplicating concrete role→harness mappings;
- minimal steady-state token/context cost;
- preservation of independent review, ownership, authority and true stop invariants;
- sufficient regression coverage without unnecessary architecture.

## Findings

Verdict: RED. Approved Definition R2 and the accepted ADR remain coherent; the defects are bounded planning gaps.

1. **P1 — no deterministic binding-establishment / schema-upgrade path.** The plan adds a manifest `orchestration` block with null defaults and defines fail-closed use of missing/stale bindings, but it does not assign a route that first resolves and durably records `runtime_owner + policy_ref` for newly materialized workstreams or reconciles already-existing branch-first `codex_only` manifests created before this schema. Without that lifecycle, a valid workstream can reach the first policy-dependent dispatch with no usable binding and only fail closed. Planning must name the creation/recovery transition that establishes the binding and distinguish legacy schema absence from an established-but-invalid binding.
2. **P1 — dispatch coverage is not complete.** Work package B says every policy-dependent dispatch is gated, but its concrete wiring list covers Execution, Review, Plan Review and bounded-parallel launch while current `workflow/codex_only/RESEARCH.md` explicitly allows runtime-owned Investigator realization (and Intake can perform runtime-backed diagnosis). CCOR-R5 covers Tester/Executor/**other** policy-dependent worker dispatch. Planning must make the kernel precondition generic at the orchestration boundary and audit every route that can realize a worker, including Research/Investigator, without duplicating role→harness mappings.
3. **P1 — the persistent-state/cross-boundary contract is not marked for OpenSpec/JIT formalization.** This change introduces a persistent manifest schema plus reconstruction/re-bind semantics across the Project Workflow ↔ runtime boundary. Current planning policy identifies persistent schema/state and cross-package contracts as normal OpenSpec candidates. The plan should mark this as a JIT OpenSpec candidate (or record a concrete reason to skip) so Execution Prep cannot implement the state contract from prose alone.

Required correction remains inside accepted Definition/ADR authority. Create a new plan revision and independent review record; do not mutate this reviewed subject.
