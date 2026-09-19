# Master Plan — dedicated codex_only policy namespace

Revision: CO-P1
Status: approved
Updated: 2026-09-19
Independent plan review: RECOMMENDED

Planning organizes approved Definition CO-R1. requirements/CODEX_ONLY_POLICY.md and the accepted ADRs remain authoritative.

## 1. Accepted target / canonical inputs

- Requirements: requirements/CODEX_ONLY_POLICY.md (approved, CO-R1)
- Accepted decisions:
  - decisions/ADR_CODEX_ONLY_DEDICATED_NAMESPACE.md
  - decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md
  - decisions/ADR_CODEX_ONLY_BOUNDED_PARALLEL_CARDS.md
- Exploratory provenance: brainstorming/CODEX_ONLY_POLICY.md
- Intake/base classification: implementation/workstreams/feature-codex-only-policy/INTAKE.md
- Workstream manifest: implementation/workstreams/feature-codex-only-policy/WORKSTREAM.yaml
- Runtime capability evidence: elmakus/codex_workflow v1.1.17-private.12, source d285aa1a271258052d23e3a2d3b585117fc1e862
- Project baseline: Project Workflow main at workstream base 6b0445256b417f82431fb7b2704f56691eb4e7ae

## 2. Execution baseline

- This repository itself remains execution_policy: chatgpt_only.
- workflow/chatgpt_only/ is the lifecycle reference implementation.
- Root policy routing currently sends non-chatgpt_only accepted policies to legacy routing.
- Legacy Codex/shared execution files are compatibility evidence, not the implementation base.
- Old feat/bounded-parallel-task-cards is not a parent dependency.
- codex_workflow can realize stateful logical workers; Project Workflow consumes capability behavior, not runtime session schema.

## 3. Inherited non-goals / invariants / external constraints

- no execution-policy change for this repository;
- no shared ChatGPT/Codex conditional execution core;
- no large deduplication refactor into common;
- no Project Workflow ownership of runtime session/invocation/Muse/model/profile state;
- no codex_workflow ownership of Project Workflow Task Board/router/review state;
- no mandatory second normal-ChatGPT review after a qualifying formal Codex-managed review;
- no generic unrestricted DAG scheduler;
- serial execution remains the safe default;
- exact review subjects remain immutable per attempt;
- reviewer/Tester cannot repair the subject while acting as reviewer;
- Codex Main remains single owner of shared Task Board/integration state;
- parallelism requires current-state JIT proof;
- other legacy policies remain outside this migration.

## 4. Milestones

### M01 — Dedicated namespace foundation and semantic parity inventory

- Outcome: a complete codex_only policy-local namespace structure exists on the feature branch with an auditable mapping from current chatgpt_only plus a legacy Codex behavior inventory; no migrated codex_only semantic depends on the old shared execution core.
- Checkpoint: policy-local modules/templates and parity/delta inventory exist before routing cutover.
- Acceptance:
  - every lifecycle module required by CO-REQ-005 has a codex_only owner;
  - each adapted contract is classified as unchanged lifecycle semantic, Codex-specific delta, or genuinely common;
  - legacy properties in CO-REQ-026 have preserve/adapt/reject dispositions;
  - no new cross-policy execution-core abstraction is introduced;
  - root routing is not switched to an incomplete namespace.
- Requirement coverage: CO-REQ-001..006, CO-REQ-026..028.
- Dependencies: Definition CO-R1.
- Planned work packages:
  - P1: exact chatgpt_only namespace inventory and parity matrix;
  - P2: exact legacy Codex/shared compatibility inventory;
  - P3: create/adapt codex_only policy-local foundational contracts/templates without activating root routing;
  - P4: static policy-boundary checks.
- Candidate parallelism: P1 and P2 are planning-level candidates; Execution Prep must verify actual write scopes/workspaces before concurrent Cards.
- JIT trigger: exact Card boundaries after current branch-tree inventory.
- Planning re-evaluation trigger: a required lifecycle contract cannot be represented without changing accepted namespace architecture.
- Definition re-open trigger: separate namespaces cannot satisfy a MUST invariant without violating an accepted ADR.
- Boundary gate: none.

### M02 — Project/runtime boundary, formal independent review, state and recovery

- Outcome: codex_only State/Review/Recovery/Execution contracts express Project Workflow semantics independently of worker/session implementation and allow Codex-managed formal independent review without redundant normal-ChatGPT review.
- Checkpoint: A1 implementation -> B1 independent review -> RED -> owning A1 repair -> new exact subject -> B1 full recheck -> GREEN is represented durably without Project Workflow depending on A1/B1 session identifiers.
- Acceptance:
  - project state contains project review requirement/state/subject/evidence and project role/lane provenance only;
  - runtime-only identifiers/profile/model/session/resume mechanics are absent from required Project Workflow schemas;
  - Tester cannot repair production while acting as reviewer;
  - RED evidence is preserved and corrected subject becomes a new immutable review attempt;
  - same logical Tester reuse is allowed when independence remains valid; replacement remains runtime-owned;
  - no second normal-ChatGPT review is required after a qualifying formal verdict;
  - recovery works from durable project state whether runtime resumes or replaces workers.
- Requirement coverage: CO-REQ-007..016, CO-REQ-024..025.
- Dependencies: M01.
- Planned work packages:
  - P1: codex_only authority/state provenance model;
  - P2: independent Review + plan-review realization contract;
  - P3: RED corrective routing and owning-Executor repair semantics;
  - P4: Recovery contract decoupled from runtime sessions;
  - P5: contract tests for immutable attempts, reviewer non-repair and reuse/replacement transparency.
- JIT trigger: choose minimal provenance fields after M01 reveals current schemas and compatibility needs.
- Planning re-evaluation trigger: deterministic recovery appears to require forbidden runtime identity.
- Definition re-open trigger: satisfying recovery would require changing CO-R1 ownership boundaries.
- Boundary gate: none.

### M03 — Bounded parallel Task Cards and JIT safety

- Outcome: codex_only can execute a bounded compatible ready set of Cards inside one workstream while serial behavior remains valid by default and Codex Main stays the single shared-state/integration owner.
- Checkpoint: Task Board/Card/Execution Prep/Execution/Workstreams/Repository/Recovery contracts coherently represent candidate parallelism, JIT eligibility, isolated lanes, result return and deterministic integration.
- Acceptance:
  - a workstream with no parallel metadata remains serial and valid;
  - plan-level candidates do not become runnable without JIT confirmation;
  - JIT checks dependencies, parallel_safe, disjoint write_scope, non-conflicting exclusive_resources, isolated mutable workspace and recoverable integration base;
  - unsafe candidates fall back to serial deterministically;
  - concurrent workers cannot independently mutate shared Task Board/integration state;
  - lane results/evidence survive recovery and integration;
  - bounded ready-set semantics do not introduce a global mutable scheduler.
- Requirement coverage: CO-REQ-017..023 plus recovery aspects of CO-REQ-024..025.
- Dependencies: M02.
- Planned work packages:
  - P1: codex_only Task Board/Card schema for dependency and parallel-safety metadata;
  - P2: Planning-to-JIT candidate semantics;
  - P3: Execution Prep compatible-ready-set/current-state safety gate;
  - P4: lane/worktree ownership and worker-result contract;
  - P5: Main-owned integration/recovery semantics;
  - P6: positive/negative concurrency tests.
- Candidate parallelism: later tests/docs may be candidates after P1-P5 stabilize; core schema/Execution Prep/Recovery stays ordered until contracts are stable.
- JIT trigger: exact schema fields/Card splits after M02 provenance/review state is finalized.
- Planning re-evaluation trigger: implementation would require a general scheduler or multi-writer shared coordination model.
- Definition re-open trigger: bounded parallelism cannot satisfy single-Main ownership and accepted safety invariants.
- Boundary gate: none.

### M04 — Full lifecycle integration, routing cutover and compatibility

- Outcome: codex_only has lifecycle parity across Intake through Close, root routing selects the dedicated namespace, default/branch-isolated Task Board compatibility remains valid, and migrated codex_only paths no longer fall back to legacy shared execution semantics.
- Checkpoint: a codex_only project can enter from policy routing and proceed through discovery/definition/planning/prep/execution/review/recovery/close using only workflow/common plus workflow/codex_only for migrated semantics.
- Acceptance:
  - workflow/CONTEXT_ROUTING.md explicitly routes codex_only to the dedicated namespace;
  - chatgpt_only remains isolated and unchanged;
  - other policies still route to legacy;
  - Intake/Brainstorming/Research/Definition/Planning/Plan Review/Micro-fix/Close are reconciled with codex_only execution/review semantics;
  - legacy/default Task Board and branch-isolated manifest binding remain supported;
  - stacked workstreams, target refresh, exact-subject invalidation/preservation and Close remain coherent with bounded parallel lanes;
  - no codex_only runtime path imports legacy shared execution ownership.
- Requirement coverage: CO-REQ-001..006, CO-REQ-024, CO-REQ-026..028 plus lifecycle integration of all prior requirements.
- Dependencies: M03.
- Planned work packages:
  - P1: lifecycle parity reconciliation outside core execution;
  - P2: routing cutover after namespace completeness proof;
  - P3: workstream/default-board/stacked/refresh/Close compatibility checks;
  - P4: migration notes and legacy disposition matrix finalization.
- Candidate parallelism: P1 and P4 may be candidates after M03 subject to JIT-disjoint write scopes; routing cutover P2 stays ordered.
- JIT trigger: exact routing/test Cards after M03 integrated checkpoint.
- Planning re-evaluation trigger: cutover needs a new migration phase beyond branch-local activation.
- Definition re-open trigger: another policy must be migrated in the same scope.
- Boundary gate: none.

### M05 — End-to-end regression, architecture audit and publication readiness

- Outcome: the complete feature is proven coherent across namespace isolation, formal review, bounded parallel safety, recovery, compatibility and non-regression before integration/publication.
- Checkpoint: integrated feature subject passes deterministic regression/audit coverage and is ready for workstream final-integration review and Close.
- Acceptance:
  - end-to-end serial codex_only lifecycle passes;
  - RED/repair/new-subject/GREEN formal review path passes;
  - same-reviewer reuse and fail-closed replacement remain semantically valid without Project Workflow session IDs;
  - safe parallel Cards can overlap/integrate and unsafe/overlapping/resource-conflicting Cards serialize;
  - recovery from active/partial lane results preserves project truth;
  - chatgpt_only regression remains intact;
  - remaining legacy policies route as before;
  - static/schema audit finds no forbidden Project Workflow runtime ownership fields;
  - legacy property inventory has no unexplained loss;
  - root PROJECT.md still declares execution_policy: chatgpt_only.
- Requirement coverage: all CO-REQ-001..028.
- Dependencies: M04.
- Planned work packages:
  - P1: cross-policy/static regression suite;
  - P2: codex_only lifecycle scenario matrix;
  - P3: architecture/coherence audit against CO-R1 + ADRs;
  - P4: final docs/changelog/migration notes;
  - P5: workstream integration refresh and review preparation through normal Close semantics.
- Candidate parallelism: P1/P2/P4 may become separate JIT Cards if write scopes remain disjoint; P3 judges the integrated subject after relevant outputs exist.
- JIT trigger: exact final test/audit Cards after M04 checkpoint.
- Planning re-evaluation trigger: a material gap needs a new milestone while Definition remains unchanged.
- Definition re-open trigger: audit finds a contradiction with an accepted requirement/ADR.
- Boundary gate: none beyond normal independent review/integration gates.

## 5. Requirement coverage matrix

| Requirement | Owner milestone | Planned path | OpenSpec candidate |
|---|---|---|---|
| CO-REQ-001 | M01/M04 | namespace foundation + routing cutover | no |
| CO-REQ-002 | M01/M04 | policy isolation checks | no |
| CO-REQ-003 | M04/M05 | legacy-route preservation regression | no |
| CO-REQ-004 | M01/M05 | duplication/common-boundary audit | no |
| CO-REQ-005 | M01/M04 | lifecycle parity map + integration | no |
| CO-REQ-006 | M01/M03 | scheduler-boundary checks | no |
| CO-REQ-007 | M02 | project state/authority model | yes |
| CO-REQ-008 | M02 | runtime ownership boundary | yes |
| CO-REQ-009 | M02/M05 | schema + forbidden-field audit | yes |
| CO-REQ-010 | M02/M05 | ownership boundary tests | yes |
| CO-REQ-011 | M02/M05 | formal reviewer contract/E2E | yes |
| CO-REQ-012 | M02 | independence contract | yes |
| CO-REQ-013 | M02 | Tester non-repair + RED routing | yes |
| CO-REQ-014 | M02 | immutable attempt lifecycle | yes |
| CO-REQ-015 | M02/M05 | reviewer reuse scenario | yes |
| CO-REQ-016 | M02/M05 | replacement transparency scenario | yes |
| CO-REQ-017 | M03 | bounded parallel state model | yes |
| CO-REQ-018 | M03 | plan candidate semantics | yes |
| CO-REQ-019 | M03 | Execution Prep JIT gate | yes |
| CO-REQ-020 | M03 | compatible-ready-set checks | yes |
| CO-REQ-021 | M03 | Main-owned shared state | yes |
| CO-REQ-022 | M03 | bounded deterministic ready-set | yes |
| CO-REQ-023 | M03 | lane/worktree isolation | yes |
| CO-REQ-024 | M02/M03/M04 | durable recovery across review/lanes | yes |
| CO-REQ-025 | M02/M03 | project provenance model | yes |
| CO-REQ-026 | M01/M04/M05 | legacy behavior disposition + audit | no |
| CO-REQ-027 | M01/M04 | evidence-only legacy migration rule | no |
| CO-REQ-028 | M01/M05 | root execution-policy non-regression | no |

Execution Prep must create concrete Cards before implementing each requirement-owned scope.

## 6. Dependency / execution order

Primary order: M01 -> M02 -> M03 -> M04 -> M05.

Namespace/parity inventory precedes state adaptation; state/review/recovery precede parallel lane design; bounded-parallel core precedes lifecycle/Close integration; root routing cutover waits for namespace completeness; final audit judges the integrated subject.

Planning-level parallel candidates are hints only. Execution Prep/JIT owns the actual compatible ready set.

## 7. Deployment / migration / rollback strategy

- Work only on feat/codex-only-policy until normal workstream integration.
- Do not delete legacy Codex/shared files early; keep them as comparison/rollback evidence.
- Build the dedicated namespace before root routing cutover.
- Switch root routing only after M01-M03 semantics exist and M04 pre-cutover checks pass.
- If cutover validation fails, repair/revert branch-local routing while preserving namespace work/evidence.
- Other legacy policy routing remains unchanged.
- Merge only through normal target refresh, workstream final review and Close.

## 8. System verification strategy

1. static namespace/import/routing checks;
2. schema/state contract checks;
3. focused review lifecycle scenarios;
4. serial execution regression;
5. bounded-parallel positive/negative eligibility scenarios;
6. lane integration/recovery scenarios;
7. legacy/default board + branch-isolated compatibility;
8. chatgpt_only non-regression;
9. final architecture/coherence audit against all CO-R1 requirements and ADRs.

Do not claim codex_workflow runtime internals were exercised unless an actual integration test invokes that runtime.

## 9. Idempotency / data-integrity / security strategy

- one durable project-state owner for shared Task Board/integration writes;
- immutable review attempts/evidence across repair;
- lane results/evidence preserved even when concurrency is cancelled/serialized;
- recovery from exact project state rather than transcript/runtime session identity;
- partial project-state writes route to Recovery;
- no credentials, runtime leases or worker session secrets enter Project Workflow state.

## 10. Explicit authorization boundaries

No additional user/product decision is currently required.

Normal gates remain:
- independent plan review before plan approval;
- implementation/final-integration independent review where required/recommended;
- user authority if later evidence changes Definition or adds an external/live-write authorization boundary.

## 11. JIT / deferred decomposition map

- M01: exact file/Card split after tree inventory.
- M02: exact provenance fields after M01 parity matrix.
- M03: exact parallel metadata/ready-set Cards after M02 state/review model.
- M04: exact cutover/integration Cards after M03.
- M05: exact regression/audit Cards after M04 integrated subject.

Execution Prep may split/merge/reorder not-yet-started Cards within accepted milestone outcomes under L2/JIT authority.

## 12. Fresh-context boundaries

This plan is authored while this repository executes under chatgpt_only, so this plan's own RECOMMENDED review uses the current ChatGPT-only fresh independent-review contract.

The codex_only policy being designed must not inherit fresh-normal-ChatGPT identity as a project requirement. Projects that later select codex_only use CO-R1 / ADR-CODEX-RT-001 review semantics.

Normal Context Health Gate remains authoritative for any additional hygiene handoff.

## 13. Pre-implementation planning audit

- Definition Complete: GREEN.
- False assumptions/P0-P1 risks: GREEN; routing cutover delayed, runtime capability separated from authority, JIT parallel proof required.
- Milestone boundaries/order: GREEN.
- Dependency completeness: GREEN.
- Outcome-level acceptance: GREEN.
- Requirement coverage: GREEN; all CO-REQ-001..028 mapped.
- Migration/rollback: GREEN.
- System verification: GREEN.
- Data integrity/idempotency/security: GREEN.
- Authorization gates: GREEN; no hidden user/product choice remains.
- OpenSpec boundaries: state/review/parallel cross-file contracts are JIT candidates.
- Overengineering/premature detail: GREEN; exact schemas/Card IDs/worker profiles deferred.
- Remaining blockers: none.

## 14. Workflow references

- Current execution policy: chatgpt_only
- Policy router: workflow/CONTEXT_ROUTING.md
- Planning contract: workflow/chatgpt_only/PLANNING.md
- Plan review: workflow/chatgpt_only/PLAN_REVIEW.md
- Definition authority: requirements/CODEX_ONLY_POLICY.md + accepted ADRs
- Workstream: implementation/workstreams/feature-codex-only-policy/WORKSTREAM.yaml

The Master Plan is not the live task tracker. No Task Board/Card state is created until plan approval and Execution Prep.
