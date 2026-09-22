# A/B Planning Experiment — ChatGPT Sol High

Date: 2026-09-22
Status: ready
Experiment ID: `PWV2-PLAN-AB-CHATGPT-SOL-HIGH`

## Purpose

Produce an independent Strategic Planning artifact for Project Workflow V2 using ChatGPT GPT-5.6 Sol High, from the same frozen Definition authority available to the Astra XHigh planner, without allowing either planner to read, overwrite or influence the other's plan.

This experiment is comparison-only. It does not replace or mutate the canonical Project Workflow workstream state.

## Frozen inputs

Project/Definition checkpoint:
- repository: `elmakus/chatgpt-codex-project-workflow`
- experiment branch: `exp/v2-plan-chatgpt-sol-high`
- branch base / frozen Definition checkpoint: `8055ed00acdb708c79919d470217fd87c920973a`

Workflow-process authority for fair A/B comparison:
- repository: `elmakus/chatgpt-codex-project-workflow`
- V1 workflow ref observed at experiment creation: `7aa7512ead67a86256089d1af0171e2e655e700d`

Canonical V2 Definition inputs on this experiment branch:
- `requirements/PROJECT_WORKFLOW_V2.md`
- `decisions/ADR_PROJECT_WORKFLOW_V2_SINGLE_SEMANTIC_CORE.md`
- `decisions/ADR_PROJECT_WORKFLOW_V2_DELIVERY_BOOTSTRAP.md`
- `decisions/ADR_PROJECT_WORKFLOW_V2_MANAGED_CHANGE_LIFECYCLE.md`
- `decisions/ADR_PROJECT_WORKFLOW_V2_EXECUTION_BOUNDARY.md`
- `decisions/ADR_PROJECT_WORKFLOW_V2_REVIEW_AND_PREMIUM_PLANNING.md`
- `decisions/ADR_PROJECT_WORKFLOW_V2_CONTEXT_RESEARCH_YAGNI.md`
- `brainstorming/V1_TO_V2_COVERAGE_MATRIX.md`
- `brainstorming/V2_VALIDATION_MATRIX.md`
- supporting Definition handoff:
  `implementation/workstreams/feature-common-preexecution-core/handoffs/DEFINITION_COMPLETE_2026-09-22.md`

Target production repository described by the authority:
- `elmakus/project_workflow_v2`

## Isolation rules

The ChatGPT planner MUST NOT:

1. read `feat/common-preexecution-core` after checkpoint `8055ed00...`;
2. read any Astra-created Project Workflow V2 Master Plan, plan-review record, planning diff, planning summary or later canonical planning commit;
3. inspect later commits on the canonical planning branch for hints about Astra's plan;
4. modify `implementation/workstreams/feature-common-preexecution-core/WORKSTREAM.yaml`;
5. modify any requirements, decisions, Brainstorming records, validation/coverage matrix, Task Board, workstream state, review state or canonical handoff;
6. create or update the canonical Master Plan path;
7. create a Plan Review record or move any canonical lifecycle state toward premium stop B;
8. write to `elmakus/project_workflow_v2`;
9. merge/cherry-pick anything into the canonical branch.

The experiment must remain blind to the Astra result until both plans are complete.

## Allowed writes

The planner may create exactly one primary planning artifact:

`planning/experiments/PROJECT_WORKFLOW_V2_CHATGPT_SOL_HIGH_MASTER_PLAN.md`

No other project-state write is needed.

If the planning artifact needs an internal completeness/challenge audit, requirement coverage table, dependency graph description, risks, validation mapping or alternatives, put them inside that same file.

Normal V1 Planning rules are used as reasoning/process guidance, but this experiment contract intentionally replaces the normal canonical Planning-state mutation/handoff steps with this isolated one-file output.

## Planning task

Create a full executable Strategic Master Plan for implementing Project Workflow V2 in the clean target repository `elmakus/project_workflow_v2`.

The plan must independently derive its structure from the frozen Definition authority.

It must cover every `PWV2-REQ-001..076`, either by:
- an explicit planned implementation scope; or
- a justified JIT trigger where exact implementation detail is intentionally deferred.

It must also preserve every KEEP / GENERALIZE / TRIGGER-ONLY / MIGRATION-ONLY / BOOTSTRAP / DROP disposition in the V1->V2 coverage matrix and every required automated/manual validation scenario in the V2 validation matrix.

Use YAGNI. Do not mechanically clone V1 structure. Do not prematurely freeze detail explicitly intended to remain JIT.

## Required plan quality

The resulting Master Plan should make implementation executable by another capable context without relying on this chat transcript.

At minimum it should establish:
- milestone/workstream ordering and dependencies;
- repository/bootstrap/plugin foundation;
- canonical common workflow modules;
- durable project/workstream/Task Card/Task Board schema direction;
- router/progressive-disclosure strategy;
- ChatGPT bootstrap and Codex plugin/Skill/SessionStart delivery;
- GitHub Issue tracking behavior;
- Research/YAGNI/technical-contract behavior;
- Execution/Recovery/Review/Close semantics;
- V1 migration tooling and cutover;
- automated tests;
- staged live-test checkpoints;
- production-readiness criteria;
- requirement coverage;
- meaningful implementation risks and ordering constraints.

## Completion boundary

When the experimental Master Plan is complete:
- perform a planner-side completeness/challenge audit;
- verify all PWV2-REQ-001..076 are covered;
- verify the V1->V2 coverage matrix and V2 validation matrix are accounted for;
- write the final result only to the allowed experimental plan path;
- STOP.

Do not perform Independent Plan Review.
Do not create premium-stop-B canonical state.
Do not compare against Astra.
Do not continue into Execution Prep.

## Comparison policy

Only after both Astra XHigh and ChatGPT Sol High plans are independently complete may a separate comparison context read both.

Comparison criteria were fixed before seeing either completed plan:
1. complete requirement coverage;
2. fidelity to accepted ADRs and DROP decisions;
3. milestone sequencing and dependency quality;
4. YAGNI / avoidance of premature machinery;
5. appropriate JIT boundaries;
6. migration/cutover safety;
7. validation/test quality;
8. recovery/integration edge-case coverage;
9. implementation actionability;
10. context/complexity efficiency.

The comparison may identify strengths from either plan. It must not retroactively alter the experiment inputs.
