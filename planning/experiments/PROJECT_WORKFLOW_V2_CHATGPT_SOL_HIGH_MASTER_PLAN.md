# Project Workflow V2 — Experimental Strategic Master Plan (ChatGPT Sol High)

Date: 2026-09-22
Experiment: PWV2-PLAN-AB-CHATGPT-SOL-HIGH
Target production repository: elmakus/project_workflow_v2
Frozen Definition checkpoint: 8055ed00acdb708c79919d470217fd87c920973a
Workflow-process ref used for this experiment: 7aa7512ead67a86256089d1af0171e2e655e700d
Status: planner-complete experimental comparison artifact
Canonical-plan status: NOT CANONICAL / NOT APPROVED FOR EXECUTION
Independent Plan Review: intentionally not performed by experiment contract
Execution Prep: intentionally not entered

## 1. Purpose and authority

This plan organizes the approved Project Workflow V2 Definition into an executable implementation strategy for the clean repository elmakus/project_workflow_v2. It does not redefine product/system intent.

Canonical Definition authority for this plan is limited to the frozen checkpoint listed above:

- requirements/PROJECT_WORKFLOW_V2.md, revision R1;
- ADR-PWV2-001 — one runtime-neutral semantic core;
- ADR-PWV2-002 — one product delivered to ChatGPT from GitHub and Codex through a thin pw plugin;
- ADR-PWV2-003 — branch-first managed changes, mandatory issue alignment, GitHub Issue tracking;
- ADR-PWV2-004 — one active Project Workflow Card, runtime-owned implementation topology;
- ADR-PWV2-005 — exact-subject independent review and premium planning stops A/B/C;
- ADR-PWV2-006 — progressive disclosure, broad prior-art Research, YAGNI and selective technical contracts;
- brainstorming/V1_TO_V2_COVERAGE_MATRIX.md;
- brainstorming/V2_VALIDATION_MATRIX.md;
- the frozen Definition-complete handoff.

The V1 workflow governs only the planning process used to create this experiment. V1 product-specific semantic structure is not a V2 architecture template.

## 2. Strategic implementation thesis

V2 should be built as a small semantic kernel with durable runtime-neutral state, then expanded outward in dependency order:

1. establish one canonical workflow tree, durable artifact model and deterministic progressive-disclosure router;
2. establish the human-control and evidence-producing pre-execution lifecycle on that substrate;
3. establish bounded Task Cards, JIT decomposition and one-Card execution semantics;
4. add exact-subject review, durable recovery and external-effect safety;
5. add integration/close safety and terminal recovery;
6. expose the same completed semantics through thin ChatGPT and Codex delivery surfaces;
7. add bounded V1 migration and trigger-only specialized compatibility modules outside ordinary routing;
8. run the complete automated conformance suite;
9. run the minimum real-product live acceptance suite, then cut over only when every production gate is GREEN.

This ordering is deliberate. Delivery adapters are not allowed to become alternate semantic products, and migration is not allowed to shape the normal V2 workflow.

## 3. Target repository architecture

The exact low-level schema and helper-file names remain implementation-owned where the Definition leaves them open, but the following repository-level separation is strategic and should be stable:

- workflow/
  - one canonical semantic tree only;
  - small ROUTER/semantic index;
  - authority, intake, brainstorming, research, definition, planning, plan review, execution preparation, execution, review, recovery, close and user-stop modules as separate progressively loaded concerns;
  - trigger-only specialized modules only when a concrete requirement justifies them.
- templates/
  - PROJECT, workstream, Task Board, Task Card, Brainstorming, Research, Requirements, Decision, Master Plan and optional evidence/blocker/handoff/technical-contract templates;
  - templates are support surfaces, not duplicate semantics.
- prompts/
  - minimal ChatGPT Project Instructions/bootstrap and locator-only fresh-context prompt support.
- .codex-plugin/, skills/, hooks/
  - packaging/bootstrap only;
  - must point into/package the same canonical workflow tree rather than restating policy.
- migration/
  - bounded V1 migration readers/transformers/fixtures;
  - never part of the normal workflow router.
- tests/
  - contract/schema/router/state/migration/package tests and fixtures.
- docs/
  - user/developer-facing delivery and migration instructions only where they add operational value; not a second semantic manual.

Project repositories using V2 should converge on this durable artifact direction:

- PROJECT.md: small integrated-project marker/index containing the common V2 contract marker and navigation, not runtime identity or execution policy.
- implementation/workstreams/<id>/WORKSTREAM.*: stable branch-first workstream identity, branch/base/parent provenance, tracker correlation, lifecycle routing and final-integration/close ownership.
- implementation/workstreams/<id>/TASK_BOARD.*: the sole mutable Card/milestone execution/review/result/recovery state owner for that workstream.
- implementation/workstreams/<id>/cards/: stable bounded Task Card contracts.
- workstream-local research/evidence/review-attempt/handoff records as needed, referenced exactly from their owning state.
- planning/MASTER_PLAN.* and planning review records when material planning is in scope.
- requirements/ and decisions/ remain accepted Definition authority.

Exact serialization, field names and optional directory splits should be fixed only when the M01/M02 schema fixtures make them necessary. The semantic ownership boundaries above are the stable part.

## 4. Global implementation invariants

Every milestone must preserve these invariants:

- there is one semantic workflow, not product-specific semantic branches;
- durable state contains semantic correctness facts, never ChatGPT/Codex/model/session/worker identity as canonical truth;
- one selected workstream has at most one active Project Workflow Card;
- runtime-internal workers/subagents may be many, but they do not become additional Project Workflow Cards or shared-state writers;
- Main/coordinator remains the sole reconciler/writer of shared Project Workflow state when delegation exists;
- exact durable authority references outrank summaries;
- user/product/repair decisions are never inferred from a marker or implementation convenience;
- Research is evidence, not accepted decision authority;
- every external mutation with meaningful readback follows write -> readback -> verify -> evidence;
- uncertain external-effect occurrence is read back before retry and fails closed when occurrence cannot be established safely;
- review independence is semantic and exact-subject based;
- YAGNI removes speculative machinery but never current correctness, security, testing, maintainability, compatibility, migration or observability obligations;
- normal router continuation is automatic whenever the next obligation is deterministic and already authorized, except real human stops and premium A/B/C;
- no Context Health/FRESH lifecycle exists in V2.

## 5. Milestone dependency graph

M01 Semantic foundation and durable state kernel
  -> M02 Human-control pre-execution lifecycle
      -> M03 Task contracting and execution boundary
          -> M04 Review, recovery and external-effect safety
              -> M05 Integration, close and terminal recovery
M01 + stable M02..M05 semantics
  -> M06 ChatGPT/Codex delivery surfaces
M01..M05
  -> M07 Bounded V1 migration and specialized trigger-only modules
M01..M07
  -> M08 Automated conformance and production hardening
M06 + M08
  -> M09 Real-product live acceptance and cutover

Tests are authored with each milestone; M08 is the cumulative production gate, not the first time testing occurs.

---

# 6. Milestones

## M01 — Semantic foundation and durable state kernel

### Outcome

The new repository has one canonical, runtime-neutral Project Workflow semantic spine with a small router, stable authority boundaries, branch-first workstream identity, a workstream-local Task Board/Card model, progressive-disclosure rules and deterministic validation of core state invariants.

### Requirement ownership

Primary: PWV2-REQ-001..006, 013..023, 051.
Supporting: PWV2-REQ-015..019, 021..023.

### Planned work packages

1. Create the clean repository skeleton and a single workflow/ semantic tree.
2. Define the smallest PROJECT marker/index contract that identifies Project Workflow V2 without execution_policy or runtime identity.
3. Define branch-first WORKSTREAM ownership:
   - stable workstream ID;
   - exact branch/base/integration target;
   - optional genuine stacked-parent dependency;
   - exact tracker reference when present;
   - exact pointers to mutable state and durable evidence;
   - final-integration/close ownership.
4. Define the workstream-local Task Board:
   - stable Card references;
   - exactly one in-progress Card maximum;
   - milestone state where full planning is used;
   - review/result/research/blocker pointers;
   - no batch/lane/scheduler/active_execution/returned/transfer_ready state.
5. Define stable Task Card minimum:
   - exact authority slice;
   - bounded scope;
   - acceptance;
   - tests/verification;
   - external-write/readback obligations;
   - review requirement.
6. Implement schema/state validation and fail-closed routing for malformed workstream/board bindings.
7. Implement the small common router and progressive-disclosure contract:
   - current durable state first;
   - exact current module only;
   - exact authority/evidence refs only;
   - no neighboring lifecycle preload.
8. Add a negative semantic lint/fixture set proving that banned V1 production concepts do not become required V2 state.
9. Add authority/YAGNI common semantics and exact-ref precedence.

### Stable acceptance checkpoint

- A valid V2 project/workstream fixture routes without any execution_policy or runtime identity.
- Invalid manifest/Task Board binding fails closed.
- More than one active Card is invalid.
- No normal workflow path needs chatgpt_only, codex_only, mixed, legacy routes, Context Health, parallel-Card scheduler state or orchestration binding.
- Router fixtures prove unrelated modules/templates/migration docs are not needed for the active route.
- The repository contains exactly one production semantic workflow tree.
- Automated foundations for A01, A02, A03, A04 and A12 are GREEN.

### JIT boundary

Do not freeze every YAML key up front. First fix ownership, invariants, required references and state transitions; then choose the minimum concrete field set needed by schema tests. No generic state framework, plugin abstraction or extensibility registry is justified here.

---

## M02 — Human-control pre-execution lifecycle

### Outcome

A single common lifecycle handles managed intake, adaptive Brainstorming, Research, Definition, Strategic Planning, independent Plan Review and human stops. #issue diagnosis cannot mutate implementation before mandatory post-diagnosis user alignment, while #feature and neutral managed changes remain recoverable and branch-first.

### Requirement ownership

Primary: PWV2-REQ-039..060, 067..071.
Supporting: PWV2-REQ-017..020, 045..052.

### Planned work packages

1. Common Intake:
   - detect/recover matching workstream before creating another;
   - create branch-first workstream before first change-specific durable write;
   - #feature enters discovery/Brainstorming;
   - #issue authorizes diagnosis only;
   - neutral managed-change intake remains available;
   - read-only exploration alone remains branch-free until managed change is authorized.
2. GitHub Issue tracker correlation:
   - capability-conditional create/recover after duplicate checks;
   - exact tracker pointer in workstream state;
   - tracker remains human-visible bookkeeping, never authority or mutation permission;
   - intermediate PRs reference only; final scope-completing PR may close.
3. #issue diagnosis and alignment gate:
   - diagnosis is read-only apart from allowed tracking/workstream records;
   - diagnosis records symptom/evidence, proposed end state, material side effects/safety and recommendation;
   - router enters a durable human-alignment obligation;
   - at least one subsequent user response is mandatory;
   - challenges/questions/alternative desired behavior continue adaptive Brainstorming;
   - implementation authorization is recorded only after aligned user authority.
4. Adaptive Brainstorming:
   - intrinsic grilling; no #grill command;
   - thematic numbered material questions with recommendations;
   - agent-findable facts route to Research;
   - completion challenge/audit before promotion;
   - explicit user promotion into Definition remains required when Definition is needed.
5. Research:
   - mandatory-but-proportional prior-art coverage across official/upstream, actual project/runtime evidence, issue/discussion trackers, and practitioner/community sources where available;
   - explicit weighting and conflict handling;
   - durable Return target and reconciliation.
6. Definition:
   - accepted requirements/decisions remain the authority boundary;
   - completion creates durable premium stop A before material Strategic Planning.
7. Strategic Planning:
   - best-available-model recommendation is human-facing only, never a canonical model name;
   - material planning cannot cross stop A automatically;
   - planner produces exact frozen plan subject;
   - every new/materially revised Master Plan requires independent Plan Review.
8. Premium stop B and independent Plan Review:
   - planner does not spawn its own Stage-6 reviewer;
   - a fresh independent best-model context is required;
   - review subject is immutable and exact;
   - plan review attempt history is durable.
9. Premium stop C:
   - after GREEN review is durably consumed/approved;
   - before Execution Prep;
   - lighter/cheaper downstream model may be recommended, never hard-coded.
10. Material replan:
    - re-enters full A -> Planning -> B -> Plan Review -> C sequence.
11. Micro-fix route:
    - may bypass full material Strategic Planning only after mandatory issue diagnosis + user-alignment boundary;
    - still requires bounded fix contract, tests and applicable review.
12. User-stop semantics:
    - unresolved product/user choice;
    - explicit accepted authorization gate;
    - non-remediable access/runtime/input blocker;
    - explicit user stop;
    - end of approved scope;
    - premium A/B/C.
    Deployment/live-write status alone is not a stop.

### Stable acceptance checkpoint

- Unit/state-machine tests prove initial #issue cannot transition to implementation.
- A second user response is required after diagnosis before repair authorization can be satisfied.
- #feature enters Brainstorming automatically; #grill is absent.
- Research fixtures require source breadth and weighting.
- Premium A/B/C survive recovery and cannot be auto-crossed.
- A new/material plan cannot become execution-ready without an independent Plan Review.
- Tracker create/recover is deduplicated and never used as canonical authority.
- Foundations for A13, A14 and the logic later exercised by L01, L02, L03 and L07 are GREEN.

### JIT boundary

The exact GitHub Issue dedup correlation marker/search strategy is chosen only after implementation checks the actual available GitHub connector/API behavior. The semantic order is fixed: durable exact pointer first when already known, then bounded duplicate discovery, then create only if no exact match is recoverable.

---

## M03 — Task contracting, Execution Prep and runtime execution boundary

### Outcome

Execution Preparation materializes every currently useful well-defined Card, preserves predecessor-dependent JIT triggers and launches exactly one Card at a time. Runtime delegation may use internal subagents without changing Project Workflow semantics or durable state shape.

### Requirement ownership

Primary: PWV2-REQ-021..030, 052.
Supporting: PWV2-REQ-006, 015, 023..027, 051.

### Planned work packages

1. Execution Prep:
   - convert accepted plan/current micro-fix authority into all currently well-defined useful Cards;
   - mark legal READY Cards from authority/dependencies/prerequisites, not from runtime capability;
   - preserve predecessor-dependent JIT triggers;
   - never create “whatever predecessor reveals” placeholder Cards.
2. Delegated L2/JIT authority:
   - split/merge/reorder/refine only not-yet-started Cards;
   - remain inside accepted requirements, strategic decisions, milestone outcomes and authorization boundaries;
   - route strategy change to Planning, accepted intent change to Definition, missing evidence to Research.
3. Launch-time Refresh Gate:
   - reread exact durable authority/state/current source facts needed by the Card;
   - revalidate dependencies, prerequisites and stale assumptions before execution.
4. Single-Card execution:
   - one selected workstream has at most one executing Card;
   - no Project Workflow parallel Card machinery.
5. Runtime realization boundary:
   - when a qualifying delegated implementation context exists, coordinator delegates implementation;
   - runtime may use zero/one/many internal workers, sequentially or concurrently;
   - worker result is bounded evidence/result only;
   - worker never independently finalizes shared Project Workflow state;
   - a runtime without delegation may implement directly with identical Project Workflow semantics.
6. Card Definition of Done:
   - bounded scope complete;
   - tests/evidence complete;
   - external side-effect verification complete where applicable;
   - required/activated recommended review GREEN before terminal completion.
7. Selective technical contract:
   - Task Card is always sufficient as the baseline implementation contract;
   - trigger a separate technical-contract/OpenSpec artifact only when behavior/API/schema/state/security/idempotency/migration/cross-package contract detail materially exceeds what a clear Card can carry;
   - technical contract never replaces requirements, plan or Card authority.

### Stable acceptance checkpoint

- Execution Prep fixture creates all currently knowable useful Cards but no speculative future placeholders.
- One active Card invariant is enforced.
- READY can exist even when the current runtime cannot implement it.
- Stubbed capable runtime delegates; stubbed incapable runtime executes directly; durable state is semantically identical.
- Delegated worker output cannot mark Card/project shared state terminal.
- Simple-fix fixture uses Card only; complex-contract fixture triggers JIT technical contract.
- Foundations for A04 and A11 are GREEN.

### JIT boundary

Exact Card IDs and downstream technical interfaces are created only when predecessor evidence makes them deterministic. Runtime-specific worker/session invocation schemas are explicitly outside Project Workflow and must not be introduced here.

---

## M04 — Independent review, recovery and external-effect safety

### Outcome

Implementation/final-integration reviews use immutable exact subjects with append-only attempts; recovery reuses durable completed work; ambiguous external effects are read back before retry and fail closed when safe determination is impossible.

### Requirement ownership

Primary: PWV2-REQ-031..038.
Supporting: PWV2-REQ-006, 015, 021, 033, 051.

### Planned work packages

1. Exact-subject review model:
   - each attempt refers to one immutable subject;
   - RED evidence remains attached permanently to the failed subject;
   - corrected content creates a new subject and new attempt;
   - REQUIRED and activated RECOMMENDED block completion until GREEN.
2. Semantic independence:
   - a context that materially produced/repaired the exact subject cannot independently review it;
   - store only semantic independence basis, not model/session/worker identifiers;
   - capability-first internal review may be used for implementation/final review when it is genuinely independent;
   - Plan Review remains the explicit premium exception from M02.
3. Review coverage reuse contract:
   - coverage is expressed against exact subject + acceptance surface, not merely branch SHA;
   - later Close may reuse GREEN only if refresh proves covered content/behavior/acceptance unchanged and affected compatibility verification is GREEN.
4. Recovery:
   - exact workstream/state/evidence reconstruction from repository truth;
   - durable completed result is reconciled and reused rather than replayed because a session/worker vanished;
   - partial internal work is classified from current durable/source evidence rather than guessed.
5. External-effect protocol:
   - material action/write -> readback -> verify expected state -> evidence;
   - after interruption, read back before retry;
   - if occurrence cannot be established safely, block/fail closed rather than duplicate.
6. Recovery of review state:
   - pending/in-progress/RED/GREEN attempts recover from durable state without runtime identity conversion.

### Stable acceptance checkpoint

- A RED attempt cannot be overwritten into GREEN; correction generates a new subject/attempt.
- Subject producer/repairer cannot satisfy independent review of that subject.
- Runtime identity fields are absent from canonical review provenance.
- Durable completed delegated result is reused after simulated runtime loss.
- Simulated uncertain external effect performs readback first and refuses unsafe blind retry.
- A05, A06 and A07 are GREEN.

### JIT boundary

The exact subject encoding is chosen here after M01 schema fixtures exist. It must be content/authority exact and immutable—typically by immutable Git/object refs plus explicit acceptance-surface refs—without inventing runtime identity. Do not generalize into a universal provenance graph.

---

## M05 — Integration refresh, Close and terminal recovery

### Outcome

Final integration is safe under target movement, review reuse is evidence-based, tracker closure happens only at accepted completion, and recovery survives automatic source-branch deletion.

### Requirement ownership

Primary: PWV2-REQ-038, 056..071.
Supporting: PWV2-REQ-020, 031..037, 051.

### Planned work packages

1. Final-integration review rule:
   - normal behavior/code workstreams retain at least one independent final-integration review;
   - stronger prior review may cover it only when exact final subject and acceptance surface are fully covered.
2. Integration refresh:
   - read current integration target;
   - reconcile only the smallest authorized target movement;
   - run affected semantic/compatibility verification, not only textual merge checks;
   - determine review reuse only after refresh;
   - reread target immediately before mutation when race-sensitive.
3. Review reuse:
   - target SHA movement alone does not invalidate GREEN;
   - unchanged covered content/behavior/acceptance + GREEN affected verification permits reuse;
   - material reconciliation creates a new exact review subject.
4. Publication/integration:
   - branch/PR merge remains managed-change path;
   - no normal force-push-main remediation;
   - external write/readback verification applies to PR merge and tracker mutations.
5. Terminal durable package:
   - all unique recovery-critical workstream artifacts that can be known pre-merge are included in the merge subject / target-side package;
   - post-merge close can proceed from target + immutable PR/merge evidence if source branch disappears immediately.
6. Tracker closure:
   - intermediate PRs never close whole-scope tracker;
   - final scope-completing default-target PR uses closing linkage when supported;
   - Close reads back Issue state;
   - explicit close is allowed only after durable accepted completion if auto-close did not occur.
7. Cleanup:
   - automatic merged-branch deletion is normal;
   - if branch survives but immediate delete cannot be done safely, use only a minimal exact safe_to_delete fallback with verified ref/head/evidence;
   - revalidate current head before deletion.
8. Router continuation/end:
   - deterministic authorized next obligations continue automatically;
   - role boundaries are not stops;
   - no Context Health/FRESH lifecycle;
   - end of approved scope reports durable completion and stops without inventing work.

### Stable acceptance checkpoint

- Target-SHA-only movement fixture reuses GREEN after compatibility verification.
- Material content/acceptance movement creates a new subject.
- Terminal workstream recovers with source branch absent.
- Tracker is not prematurely closed and is read back after merge.
- safe_to_delete refuses deletion when current head differs from verified safe head.
- no deployment/live-write stop occurs unless accepted authority contains an explicit authorization gate.
- A08, A09 and A10 are GREEN; Close logic needed by L03 and continuity tests is ready.

### JIT boundary

Rebase vs merge/update mechanics are repository/environment-specific and remain JIT. The fixed contract is minimal target reconciliation, affected semantic verification, subject comparison, readback and fail-closed safety.

---

## M06 — Thin ChatGPT and Codex delivery surfaces

### Outcome

Normal ChatGPT and Codex enter the same canonical semantics through different thin bootstraps. Codex uses the installed pw plugin and bundled workflow files locally; ChatGPT uses user-owned Project Instructions pointing to the V2 repository.

### Requirement ownership

Primary: PWV2-REQ-007..016.
Supporting: PWV2-REQ-005, 006, 013..015, 071.

### Planned work packages

1. ChatGPT bootstrap:
   - minimal Project Instructions template pointing to elmakus/project_workflow_v2 and its small bootstrap/router;
   - no full workflow copy;
   - optional manual start prompt only if it materially helps recovery.
2. Fresh-context ChatGPT handoff:
   - locator-only ready-to-copy prompt;
   - project/repo, exact branch/workstream, entry obligation and smallest durable pointer;
   - no duplicated evidence/workflow narrative.
3. Codex plugin packaging:
   - namespace pw;
   - Skill project_workflow_v2;
   - acceptance invocation $pw:project_workflow_v2;
   - plugin package directly includes the canonical workflow/ files.
4. Skill and SessionStart hook:
   - tiny local package-router pointer/recovery bootstrap only;
   - no semantic duplication;
   - fail closed if bundled router is missing/broken;
   - ordinary policy acquisition never fetches remote workflow repository.
5. Packaging/update tests:
   - semantic workflow edit that does not change bootstrap/package behavior requires no Skill/hook edit;
   - plugin update includes the changed canonical workflow file.
6. Explicit out-of-scope boundary:
   - repository-local plugin/MCP/Skill provisioning and pinning remains owned by newproject-skill.

### Stable acceptance checkpoint

- One semantic workflow edit propagates through plugin packaging without policy duplication.
- $pw:project_workflow_v2 resolves in package tests.
- Hook/Skill do not embed neighboring lifecycle semantics.
- Missing local router fails closed.
- ChatGPT Project Instructions are a pointer/bootstrap, not a semantic copy.
- No project-local provisioning implementation is added to V2.
- Packaging prerequisites for L01, L04, L05 and L06 are ready.

### JIT boundary

At M06 start, inspect the then-current real Codex plugin/Skill/SessionStart packaging contract and use only the metadata required by that runtime. Do not build a generic plugin abstraction or freeze stale packaging details earlier.

---

## M07 — Bounded V1 migration and specialized trigger-only modules

### Outcome

Representative V1 projects/state can be migrated once into common V2 state without preserving legacy routes in normal semantics, and the accepted fork-release policy remains available only on its trigger.

### Requirement ownership

Primary: PWV2-REQ-072, 073, 076.
Supporting: PWV2-REQ-003..006, 017..023, 031, 064.

### Planned work packages

1. Create migration/v1 outside workflow/.
2. Define representative migration fixtures for:
   - execution_policy-bearing project state;
   - fixed-policy workstreams;
   - root/default Task Board history;
   - runtime/orchestration metadata;
   - completed and live Card/review state;
   - old concurrent/batch/lane scheduler residue;
   - post-merge/branch-deleted terminal state where evidence is available.
3. Migration transformation principles:
   - preserve accepted requirements/decisions, stable Card contracts, results, evidence, review subjects/verdict history, branch/base/integration provenance and valid workstream-local state;
   - map project/workstream state to common V2 contract;
   - drop execution_policy, runtime identity, orchestration binding, Context Health and scheduler-only machinery;
   - do not silently discard unresolved live obligations;
   - if multiple legacy live obligations cannot be deterministically reconciled into the one-Card model without choosing strategy, stop migration with explicit recovery evidence rather than invent ordering;
   - never mutate legacy source state merely to make it look V2-compatible.
4. No legacy semantic route:
   - migration reader/transformer may understand V1;
   - normal workflow router may not.
5. Coverage-disposition regression manifest/test:
   - machine-test every row of the frozen V1->V2 coverage matrix as KEEP/GENERALIZE/TRIGGER-ONLY/MIGRATION-ONLY/BOOTSTRAP/DROP/support/out-of-scope as applicable.
6. Fork release:
   - preserve downstream private revision logic as a trigger-only module;
   - ordinary non-fork routes never load it.
7. Competing research/prototype branches:
   - retain as an optional Research technique only when a real evidence need triggers it;
   - never turn it into permanent lifecycle state.

### Stable acceptance checkpoint

- Representative legacy fixtures migrate into valid common V2 state.
- Banned legacy fields/routes do not appear in normal workflow state after migration.
- Ambiguous legacy live concurrency fails closed rather than fabricating strategy.
- Fork release module is unreachable from ordinary non-fork route.
- A15, A16 and the implementation side of A17 are GREEN.

### JIT boundary

Do not build migration handlers for every historical file ever created. Start from the frozen coverage matrix plus representative actual V1 state families; add a handler only for a concrete migration surface or fixture justified by current compatibility needs.

---

## M08 — Automated conformance and production hardening

### Outcome

All deterministic contracts, state transitions, router boundaries, migration behavior and packaging invariants are enforced by automated tests suitable for regression protection before real-product live acceptance.

### Requirement ownership

Primary: PWV2-REQ-074, 076.
Supporting: all PWV2-REQ-001..073.

### Planned work packages

1. Consolidate milestone-level tests into a stable automated acceptance suite.
2. Add negative tests for every explicit DROP:
   - no fixed policy semantic trees;
   - no execution_policy;
   - no mixed Capability Gate;
   - no Context Health/FRESH lifecycle;
   - no Project-Card parallel scheduler;
   - no active_execution/transfer_ready/returned semantics;
   - no durable runtime/orchestration binding or product role identity;
   - no autonomous #issue -> fix;
   - no planner-spawned Plan Review;
   - no unconditional deployment/live-write stop;
   - no duplicate plugin semantic policy;
   - no Codex ordinary remote semantic fetch;
   - no terminal recovery dependency on source-branch existence.
3. Verify exact progressive-disclosure read sets in fixtures.
4. Verify deterministic recovery/idempotency/external-effect behaviors.
5. Verify package composition and single-source semantics.
6. Verify complete coverage-disposition manifest against the frozen V1 matrix.
7. Produce a machine-readable/concise production acceptance report for A01..A17.

### Automated validation gate

All of the following must be GREEN:

| Validation | Owner |
|---|---|
| A01 Router progressive disclosure | M01/M08 |
| A02 No legacy semantic routing | M01/M08 |
| A03 Workstream/manifest/Task Board binding | M01/M08 |
| A04 One active Project Card | M01/M03/M08 |
| A05 Delegated result recovery | M04/M08 |
| A06 Uncertain external effect | M04/M08 |
| A07 Review attempt model | M04/M08 |
| A08 Review coverage reuse | M05/M08 |
| A09 Integration refresh | M05/M08 |
| A10 Terminal package / branch disappearance | M05/M08 |
| A11 Selective technical contract | M03/M08 |
| A12 YAGNI guard | M01/all/M08 |
| A13 Research source breadth | M02/M08 |
| A14 GitHub tracker dedup logic | M02/M08 |
| A15 Legacy migration fixtures | M07/M08 |
| A16 Fork release module trigger | M07/M08 |
| A17 Coverage-matrix regression | M07/M08 |

### Stable acceptance checkpoint

No deterministic acceptance scenario is left for a user-run test merely because it was easier to test manually. M09 receives only true product/runtime/integration behaviors.

---

## M09 — Real-product live acceptance and production cutover

### Outcome

The implemented V2 is proven on real ChatGPT, real Codex plugin delivery, real GitHub integration and cross-runtime continuity. Only then is V2 accepted for production use.

### Requirement ownership

Primary: PWV2-REQ-074, 075.
Supporting: all requirements whose acceptance depends on real surfaces.

### Live checkpoints and prerequisites

| Live test | Earliest prerequisite | Required role in production gate |
|---|---|---|
| L01 ChatGPT Android bootstrap + adaptive Brainstorming | M02 + M06 + M08 | Required |
| L02 #issue human-control boundary + tracker | M02 + M06 + M08 | Required |
| L03 GitHub Issue/Feature final PR closure | M05 + M06 + M08 | Required; may combine with L02 |
| L04 Codex plugin entry/context economy | M06 + M08 | Required |
| L05 one-product plugin update propagation | M06 + M08 | Required; may combine with L04 |
| L06 ChatGPT -> Codex -> ChatGPT portability | M01..M06 + M08 | Required |
| L07 premium planning block A/B/C | M02 + M06 + M08 | Required |
| L08 N-CAPABLE topology continuity | M03..M06 + M08 | Required |
| L09 N-CHATGPT fresh-context continuity | M02..M06 + M08 | Required |

L08 and L09 are mandatory before first production acceptance, not optional carryover.

Optional exploratory smokes remain nonblocking unless a required live test exposes a related defect:
- second-chat #feature tracker recovery;
- intentionally broken plugin-router fail-closed;
- disposable downstream-fork release;
- explicit safe branch-cleanup fallback;
- real-project legacy migration in addition to fixtures.

### Cutover sequence

1. Freeze the V2 candidate commit that has all A01..A17 GREEN.
2. Run L01..L09 only against that candidate or explicitly tracked corrected descendants.
3. Any live-test RED creates bounded correction evidence and reruns affected automated/live coverage; do not reopen unrelated accepted Definition unless the failure reveals a true semantic contradiction.
4. Verify no production workflow path still requires V1 semantic authority.
5. Verify plugin package from the accepted candidate contains the same canonical workflow/ tree.
6. Verify ChatGPT Project Instructions point to V2.
7. Verify explicit $pw:project_workflow_v2 invocation works from the accepted installed plugin.
8. Declare first production acceptance only when all required live tests are GREEN.
9. Keep the V1 repository/history available as migration/reference authority; do not delete or rewrite it as part of V2 cutover.
10. Migrate existing projects only through explicit bounded migration, project by project. No mass implicit state conversion.
11. After cutover, ordinary semantic development occurs in the V2 repository; migration code remains bounded and outside normal router context.

### Production-readiness criteria

Production readiness is GREEN only when:

- every PWV2-REQ-001..076 has an implemented owner path and passing acceptance evidence;
- ADR-PWV2-001..006 are satisfied with no contradictory implementation;
- A01..A17 are GREEN;
- L01..L09 are GREEN;
- V1 coverage disposition regression is GREEN;
- every explicit DROP is absent from normal V2 semantics;
- ChatGPT and Codex use the same durable state without conversion;
- plugin packaging proves one-source semantics;
- #issue cannot bypass post-diagnosis user alignment;
- one active Project Workflow Card invariant is enforced;
- exact-subject append-only review works across correction and runtime/context transitions;
- uncertain external effects fail closed;
- target movement does not cause needless review churn;
- material subject movement does cause new review;
- merged branch disappearance does not break terminal recovery;
- tracker close/readback is correct;
- migration is bounded and does not become a legacy route;
- no unresolved P0/P1 defect, migration ambiguity affecting supported inputs, or accepted authorization-boundary defect remains.

---

# 7. Requirement coverage PWV2-REQ-001..076

Every requirement below has a planned implementation owner and an acceptance path.

| Requirement | Owner | Planned coverage |
|---|---|---|
| PWV2-REQ-001 | M01 | One canonical production semantic tree at workflow/. |
| PWV2-REQ-002 | M01/M08 | Negative lint/tests forbid chatgpt_only/codex_only/legacy/redundant v2 semantic trees. |
| PWV2-REQ-003 | M01/M07 | New state has no execution_policy; migration strips it. |
| PWV2-REQ-004 | M01/M04 | Canonical state/review provenance excludes runtime/model/session/worker identity. |
| PWV2-REQ-005 | M01/M06/M09 | Common state model + L06 cross-runtime continuation without conversion. |
| PWV2-REQ-006 | M01/M03/M04 | PW owns semantics/state/review/recovery; runtime owns topology; coordinator reconciles shared state. |
| PWV2-REQ-007 | M06/M09 | ChatGPT Project Instructions point to V2 GitHub bootstrap/router; L01 verifies. |
| PWV2-REQ-008 | M06/M09 | Codex uses bundled plugin workflow locally; L04 verifies no ordinary remote fetch. |
| PWV2-REQ-009 | M06/M09 | Namespace pw, Skill project_workflow_v2, explicit $pw:project_workflow_v2 acceptance. |
| PWV2-REQ-010 | M06/M08 | Plugin directly packages canonical workflow/; no duplicate semantic copy. |
| PWV2-REQ-011 | M06/M09 | L05 proves semantic edit propagates without Skill/hook edit. |
| PWV2-REQ-012 | M06 | Explicit boundary leaves project-local provisioning/pinning to newproject-skill. |
| PWV2-REQ-013 | M01/M06/M08 | Thin bootstrap -> router -> current module -> exact state -> exact refs; A01/L04. |
| PWV2-REQ-014 | M01/M06/M08 | Negative context-load tests prevent full workflow/docs/template/migration preload. |
| PWV2-REQ-015 | M01..M05 | Durable artifacts carry exact authority/evidence/result refs used by router/recovery. |
| PWV2-REQ-016 | M01 | PROJECT marker identifies common V2 contract; exact minimal schema fixed in M01. |
| PWV2-REQ-017 | M01/M07 | One project repo remains source of truth; migration does not create second control repo. |
| PWV2-REQ-018 | M01/M02 | Branch-first manifest-bound workstreams with local state/evidence/handoffs. |
| PWV2-REQ-019 | M01/M08 | No correctness-critical mutable global workstream registry; negative test. |
| PWV2-REQ-020 | M01/M05 | Stacked workstream only for genuine parent-only dependency with provenance. |
| PWV2-REQ-021 | M01/M03 | Stable Card contract separated from mutable Task Board state. |
| PWV2-REQ-022 | M01/M03/M08 | Validator/state machine enforces one executing Card per selected workstream. |
| PWV2-REQ-023 | M01/M07/M08 | Scheduler/batch/lane/active_execution/returned/transfer_ready absent from normal V2. |
| PWV2-REQ-024 | M03 | Runtime may use internal subagents without extra Cards/shared writers. |
| PWV2-REQ-025 | M03/M09 | Qualifying delegated context causes implementation delegation while coordinator retains semantic duties. |
| PWV2-REQ-026 | M03/M04 | Worker output cannot independently finalize shared state; coordinator validates/reconciles. |
| PWV2-REQ-027 | M03 | Non-delegating runtime may implement directly with same semantics. |
| PWV2-REQ-028 | M03 | Execution Prep materializes useful defined Cards and records JIT triggers without placeholders. |
| PWV2-REQ-029 | M03 | L2/JIT changes only not-yet-started Cards inside accepted authority; strategy/intent escalates. |
| PWV2-REQ-030 | M03 | READY is authority/dependency based; launch-time refresh/revalidation occurs before execution. |
| PWV2-REQ-031 | M04 | Recovery reconciles/reuses durable completed result instead of replaying. |
| PWV2-REQ-032 | M04 | Interrupted uncertain external effect read back before retry; unresolved occurrence fails closed. |
| PWV2-REQ-033 | M03/M04/M05 | Material external writes use action/write -> readback -> verify -> evidence. |
| PWV2-REQ-034 | M04/M05 | Exact immutable review subjects with append-only attempt history. |
| PWV2-REQ-035 | M04 | Subject producer/repairer is ineligible for independent review of that subject. |
| PWV2-REQ-036 | M04/M05 | REQUIRED/activated RECOMMENDED block completion; RED remains durable. |
| PWV2-REQ-037 | M04 | Review provenance stores semantic independence only, not runtime identity. |
| PWV2-REQ-038 | M04/M05 | Normal behavior/code workstream gets independent final integration review unless stronger exact coverage exists. |
| PWV2-REQ-039 | M02 | Every new/material Master Plan gets independent Plan Review; editorial-only exception. |
| PWV2-REQ-040 | M02/M09 | Definition completion creates premium stop A; L07 verifies no automatic planning entry. |
| PWV2-REQ-041 | M02 | Human recommendation uses best available model/context without canonical model name. |
| PWV2-REQ-042 | M02/M09 | Frozen plan creates stop B; planner cannot internally spawn Stage-6 review; L07. |
| PWV2-REQ-043 | M02/M09 | GREEN approved Plan Review creates stop C before Execution Prep; L07. |
| PWV2-REQ-044 | M02 | Material replanning resets full A/B/C block. |
| PWV2-REQ-045 | M02/M03 | Micro-fix bypasses full planning only after diagnosis + user alignment; Card/review rigor remains. |
| PWV2-REQ-046 | M02 | Adaptive grilling intrinsic; #grill absent. |
| PWV2-REQ-047 | M02 | Thematic numbered material questions with recommendations continue while decision value remains. |
| PWV2-REQ-048 | M02 | Agent-findable facts route to Research; Brainstorming ends with final challenge/completeness audit. |
| PWV2-REQ-049 | M02/M08 | Research requires proportional official/upstream + project/runtime + issue/discussion + community prior art. |
| PWV2-REQ-050 | M02/M08 | Research records source weight/conflicts; popularity is not authority. |
| PWV2-REQ-051 | All/M08 | Global YAGNI rule plus negative speculative-complexity tests; present quality obligations preserved. |
| PWV2-REQ-052 | M03/M08 | Every change has precise Card/fix contract; separate technical contract is selective JIT only. |
| PWV2-REQ-053 | M02 | #issue authorizes diagnosis/intake only. |
| PWV2-REQ-054 | M02/M09 | Diagnosis presents end state/safety/recommendation and requires later user response before mutation; L02. |
| PWV2-REQ-055 | M02 | Questions/safety challenges/alternatives keep adaptive Brainstorming active until aligned. |
| PWV2-REQ-056 | M02/M09 | Capability-conditional #issue/#feature tracker create/recover after dedup; L01/L02. |
| PWV2-REQ-057 | M02 | GitHub Issue remains bookkeeping, not authority/authorization. |
| PWV2-REQ-058 | M01/M02 | Workstream retains exact tracker reference through final PR. |
| PWV2-REQ-059 | M02/M05/M09 | Intermediate PRs do not close; final scope-completing default-branch PR uses closing linkage when supported. |
| PWV2-REQ-060 | M05/M09 | Close reads tracker state and explicitly closes only after accepted completion if needed. |
| PWV2-REQ-061 | M05 | Final integration refreshes target, minimally reconciles movement, verifies, decides review reuse, rereads before mutation when needed. |
| PWV2-REQ-062 | M05/M08 | Target SHA movement alone preserves GREEN when covered subject unchanged and compatibility verification GREEN. |
| PWV2-REQ-063 | M05/M08 | Material behavior/content/acceptance reconciliation creates new exact subject. |
| PWV2-REQ-064 | M05/M09 | Terminal target-side package supports recovery after source branch deletion. |
| PWV2-REQ-065 | M05 | Auto-delete is valid; surviving branch may use exact safe_to_delete fallback with head revalidation. |
| PWV2-REQ-066 | M02/M05 | Deployment/live-write status is not a stop absent explicit accepted authorization gate. |
| PWV2-REQ-067 | M02/M05/M09 | Router auto-continues deterministic authorized work except real stops and A/B/C; L08/L09. |
| PWV2-REQ-068 | M02 | Real-stop set implemented explicitly, including premium A/B/C. |
| PWV2-REQ-069 | M01/M05/M08 | No Context Health/FRESH lifecycle; durable recovery handles runtime/context replacement. |
| PWV2-REQ-070 | M05 | End-of-scope durable completion stops without inventing “what next” work. |
| PWV2-REQ-071 | M02/M06 | Genuine fresh-context handoffs are ready-to-copy locator-only prompts. |
| PWV2-REQ-072 | M07/M08 | Legacy support exists only under bounded migration tooling/readers, never normal workflow. |
| PWV2-REQ-073 | M07/M08 | Fork downstream release versioning is trigger-only and unloaded for ordinary work. |
| PWV2-REQ-074 | M08/M09 | Deterministic behavior automated; manual tests reserved for real product/plugin/model/GitHub behavior. |
| PWV2-REQ-075 | M09 | L08 N-CAPABLE and L09 N-CHATGPT are mandatory before first production acceptance. |
| PWV2-REQ-076 | M07/M08 | Frozen V1->V2 matrix becomes explicit regression/disposition checklist with A17. |

Coverage result: 76/76 requirements have an owner, execution path and acceptance path.

---

# 8. ADR conformance audit

## ADR-PWV2-001 — one runtime-neutral semantic core

Conformance:
- M01 creates one workflow/ tree.
- no execution_policy or runtime identity in V2 state;
- same durable workstream crosses ChatGPT/Codex boundaries;
- migration understands old policies only outside normal workflow.

Forbidden regression:
- product-specific semantic directories or state conversion between runtimes.

## ADR-PWV2-002 — delivery/bootstrap

Conformance:
- M06 makes ChatGPT GitHub bootstrap and Codex pw plugin two thin entry surfaces to the same workflow files;
- Skill project_workflow_v2 and $pw:project_workflow_v2 are explicit acceptance;
- plugin directly packages workflow/;
- newproject-skill retains project-local provisioning/pinning.

Forbidden regression:
- semantic policy copy in Skill/hook, or Codex ordinary remote-repository fetch.

## ADR-PWV2-003 — managed-change lifecycle

Conformance:
- M01/M02 use branch-first manifest-bound workstreams without global registry;
- #issue is diagnosis only and requires later user alignment;
- #feature enters discovery;
- GitHub Issue tracking is correlated bookkeeping only;
- M05 closes tracker only at final accepted scope.

Forbidden regression:
- initial #issue autonomously repairing/merging.

## ADR-PWV2-004 — execution boundary

Conformance:
- M03 enforces one Project Workflow Card;
- runtime-internal topology is non-canonical;
- coordinator is sole shared-state reconciler;
- capable runtime delegates implementation; incapable runtime may execute directly.

Forbidden regression:
- Project-Card batches/lanes or worker finalization of shared state.

## ADR-PWV2-005 — review and premium planning

Conformance:
- M04 exact-subject append-only implementation/final review;
- M02 mandatory Plan Review for material plans;
- premium A/B/C are durable human stops;
- Stage-6 reviewer is fresh and not spawned by planner;
- material replan repeats A/B/C.

Forbidden regression:
- planner self-review or silent crossing of premium stops.

## ADR-PWV2-006 — context/research/YAGNI

Conformance:
- M01/M06 progressive disclosure;
- M02 proportional multi-source prior-art Research;
- global YAGNI checks in every milestone;
- M03 selective JIT technical contracts;
- adaptive grilling intrinsic, #grill absent.

Forbidden regression:
- broad bootstrap preload, official-docs-only Research, mandatory OpenSpec for trivial work, speculative abstractions.

ADR result: 6/6 accepted ADRs are represented with both implementation and anti-regression coverage.

---

# 9. V1 -> V2 coverage-matrix disposition preservation

The implementation must carry the frozen matrix as a regression checklist, not as architectural inspiration. The following is the planner-side disposition audit.

## Lifecycle / semantic modules

- V1 Brainstorming modules — KEEP CORE -> M02 one adaptive-grilling module.
- common Brainstorming authority — KEEP CORE -> M02 merged common authority boundaries.
- fixed-policy Intake — GENERALIZE -> M02 one runtime-neutral Intake.
- automatic #issue -> micro_fix fast path — DROP -> M02 explicit negative transition test.
- V1 micro-fix contract — GENERALIZE -> M02/M03 proportional route only after alignment.
- Research modules — KEEP CORE -> M02 one broad-prior-art Research module.
- Definition modules — KEEP CORE -> M02 one accepted authority stage.
- Planning modules — KEEP CORE -> M02 one Strategic Planning stage.
- fixed-policy Plan Review — GENERALIZE -> M02 exact-subject premium fresh-context review.
- Execution Prep — GENERALIZE -> M03 JIT decomposition/READY, no policy or parallel scheduler.
- Execution — GENERALIZE -> M03 one serial Project-Card lifecycle.
- Review — GENERALIZE -> M04 append-only exact-subject model.
- Close — KEEP CORE -> M05 refresh/review reuse/publication/readback/terminal package/cleanup.
- Recovery — GENERALIZE -> M04/M05 runtime-neutral durable recovery.
- Routers/CONTEXT_ROUTING — GENERALIZE -> M01 one small router/index.
- USER_STOP — GENERALIZE -> M02/M06 concise stop + locator-only handoff, no Context Health.
- AUTHORITY — KEEP CORE -> M01 authority-by-domain + durable truth + YAGNI.

## Durable project/state model

- repository contracts — GENERALIZE -> M01 one-project-one-repository + small PROJECT + branch-first state.
- one project = one repository — KEEP CORE -> M01.
- branch-first manifest-bound workstreams — KEEP CORE -> M01.
- mutable global workstream registry — DROP -> M01/M08 negative test.
- genuine stacked parent/child workstreams — KEEP CORE -> M01/M05 only when parent-only dependency exists.
- WORKSTREAM final-integration/cleanup ownership — GENERALIZE -> M01/M05.
- TASK_BOARD mutable state — KEEP CORE -> M01.
- stable Card vs mutable Board — KEEP CORE -> M01/M03.
- root/default legacy Task Board as live destination — DROP -> M07 migration input only.
- execution-policy field — DROP -> M01/M07/M08.
- runtime/model/session/worker canonical identity — DROP -> M01/M04/M08.
- durable orchestration binding — DROP -> M01/M08.
- universal active_execution/transfer_ready — DROP -> M01/M08.
- Project-Card batch/lane scheduler — DROP -> M01/M08.
- runtime-internal parallel subagents — KEEP OUTSIDE PW -> M03 runtime boundary.
- cumulative milestone handoff/checkpoint — KEEP CORE -> M05 minimal recovery checkpoint.
- terminal target-side package — KEEP CORE -> M05.
- safe_to_delete fallback — KEEP CORE -> M05 trigger-only cleanup fallback.

## Task / technical contracts

- Task Card contracts — GENERALIZE -> M01/M03 bounded authority/scope/acceptance/tests/readback/review.
- Task execution contract — GENERALIZE -> M03/M04 Refresh/ready/start/DoD/blocker/review boundary without policy/parallel branches.
- GitHub state contract — GENERALIZE/SHRINK -> M01/M04/M05 only needed durable Git/recovery semantics.
- OpenSpec/technical-contract modules — TRIGGER-ONLY/GENERALIZE -> M03 tool-neutral selective JIT module.
- speculative distant OpenSpec — DROP -> M03.
- OpenSpec replacing requirements/plan/Card — DROP -> M03 negative contract test.

## Reviews / human control

- REQUIRED/RECOMMENDED exact-subject review — KEEP CORE -> M04/M05.
- product-specific reviewer identities — DROP -> M04.
- planner spawning internal Stage-6 reviewer — DROP -> M02.
- capability-first Stage-9 internal independent reviewer — KEEP CORE -> M04 subject-independent runtime realization.
- locator-only fresh ChatGPT handoff — KEEP CORE -> M06.
- Context Health/FRESH lifecycle — DROP -> M01/M05.
- issue auto-implementation — DROP -> M02.
- deployment/live-write automatic stop — DROP -> M02/M05.

## Git / integration / external effects

- GitHub durable commit/PR/evidence source — KEEP CORE -> M05.
- coherent branch/PR managed changes — KEEP CORE -> M01/M05.
- no normal force-push-main remediation — KEEP CORE -> M05.
- integration refresh — KEEP CORE -> M05.
- textual merge cleanliness equals semantic compatibility — DROP -> M05 requires affected semantic verification.
- action/write -> readback -> verify -> evidence — KEEP CORE -> M04/M05.
- blind retry after uncertain effect — DROP -> M04.
- GitHub auto-delete merged branch — KEEP CORE -> M05 terminal recovery.

## Optional / specialized policy

- fork release versioning — TRIGGER-ONLY -> M07.
- private lineage rules — TRIGGER-ONLY -> M07.
- competing prototype branches — TRIGGER-ONLY -> Research technique only.
- BLOCKER support — KEEP SUPPORT -> optional durable blocker only when recovery value exists.
- acceptance evidence template — KEEP SUPPORT -> optional proportional evidence.

## Runtime/product adapters

- mixed/product Capability Gate — DROP as product gate -> no V2 semantic gate.
- ChatGPT execution adapter semantics — GENERALIZE/MINIMIZE -> M06 surface UX only.
- Codex orchestration module — GENERALIZE/MINIMIZE -> M03/M06 runtime boundary only, no policy binding.
- Codex execution adapter semantics — GENERALIZE/MINIMIZE -> M06 bootstrap/runtime realization only.
- cross-product HANDOFF semantic model — MOSTLY DROP -> durable common state replaces it; retain only locator/evidence principles where needed.
- named Codex Main/Executor/Tester/Investigator canonical roles — DROP -> runtime-owned.

## Delivery / plugin / prompts

- .codex-plugin/plugin.json — BOOTSTRAP -> M06.
- marketplace metadata — BOOTSTRAP -> M06 minimal distribution metadata.
- Skill file — BOOTSTRAP -> M06 renamed project_workflow_v2 pointer.
- SessionStart hook + hooks metadata — BOOTSTRAP -> M06 tiny bundled-router pointer/fail-closed.
- Codex normal remote workflow fetch — DROP -> M06 negative test.
- ChatGPT Project Instructions prompt — BOOTSTRAP -> M06 minimal pointer.
- CHATGPT_START — SHRINK/OPTIONAL -> M06 only if it adds manual recovery value.
- CHATGPT_FRESH_SESSION — KEEP SUPPORT -> M06 locator-only.
- CODEX_START — DROP/DEBUG-ONLY -> no normal semantic bootstrap.
- duplicate plugin semantic policy — DROP -> M06 package test.
- project-local provisioning — OUT OF SCOPE -> newproject-skill.

## Templates

- PROJECT — GENERALIZE -> M01 common V2 marker/navigation only.
- BRAINSTORM — KEEP SUPPORT -> M02 durable minimum.
- OPEN_QUESTIONS — KEEP SUPPORT -> optional unresolved material choices/evidence needs.
- RESEARCH — KEEP SUPPORT -> M02 broad prior-art/weighting fields.
- REQUIREMENTS — KEEP SUPPORT -> Definition authority.
- DECISION — KEEP SUPPORT -> accepted decisions.
- MASTER_PLAN — KEEP SUPPORT -> material planning subject.
- MILESTONE — KEEP SUPPORT/OPTIONAL -> JIT extension only when useful.
- TASK_CARD — KEEP SUPPORT -> M01/M03.
- TASK_BOARD — GENERALIZE -> M01 common workstream-local state.
- ACCEPTANCE_EVIDENCE — KEEP SUPPORT -> proportional.
- BLOCKER — KEEP SUPPORT -> proportional.
- HANDOFF — GENERALIZE -> M05 minimal cumulative recovery checkpoint.

## Explicit DROP checklist

The M08 negative suite must assert absence from normal V2 semantics of every matrix DROP:
fixed chatgpt_only tree; fixed codex_only tree; legacy shared route; execution_policy; mixed Capability Gate; Context Health/FRESH; Project-Card parallel execution; batch/lane/frozen-member metadata; scheduler-oriented parallel_safe/write-scope machinery; universal active_execution; transfer_ready; durable orchestration binding; canonical runtime/model/session/worker identity; named product-specific implementation/reviewer roles; automatic #issue -> repair; planner-spawned Stage-6 review; unconditional deployment/live-write stop; duplicate plugin semantics; Codex ordinary remote semantic fetch; source-branch existence requirement for terminal recovery.

## GitHub Issue tracking addition

- #issue tracker — KEEP SUPPORT / DEFAULT TRACKER -> M02 dedup/create/recover.
- #feature tracker — KEEP SUPPORT / DEFAULT TRACKER -> M02.
- workstream -> Issue exact pointer — KEEP CORE POINTER -> M01/M02.
- final PR closing keyword — KEEP SUPPORT -> M05.
- post-merge Issue readback — KEEP CORE CLOSE CHECK -> M05.

Coverage-matrix audit result: every frozen matrix surface has an explicit implementation, trigger, migration, bootstrap, support, out-of-scope or DROP treatment in this plan.

---

# 10. Validation-matrix integration

Automated scenarios A01..A17 are implementation requirements, not documentation-only checks. Each milestone owns its relevant tests and M08 runs the cumulative gate.

Manual scenarios L01..L09 are scheduled only after their prerequisite slices are implemented. No live V1 test is required or useful for accepting V2 behavior.

The minimum manual production set is exactly the frozen recommendation:
- L01;
- L02 + L03 may be combined;
- L04 + L05 may be combined;
- L06;
- L07;
- L08;
- L09.

No deterministic test should be shifted to the user when a repository test can prove it.

---

# 11. Migration and cutover safety strategy

## Build-side migration safety

V2 is built cleanly in elmakus/project_workflow_v2. The V1 repository remains historical/reference authority during implementation and is not incrementally rewritten into V2.

Migration tooling must be one-way/bounded and separated from the normal semantic tree. It should transform a copied or explicitly selected project state, never reinterpret ordinary V2 routing as “maybe legacy.”

## Per-project migration transaction

A migration operation should conceptually:

1. read and classify exact V1 project/workstream/state inputs;
2. inventory accepted authority, live obligations, completed results, reviews, branches/PRs and tracker correlation;
3. prove whether the state can be deterministically represented under V2 invariants;
4. stage a V2 representation without destroying V1 evidence;
5. validate the staged V2 state using normal M01 validators;
6. stop/fail closed on ambiguous live concurrency, missing subject provenance or unsafe external-effect uncertainty;
7. make the V2 state durable atomically enough that recovery never depends on mixed half-converted semantics;
8. verify readback;
9. only then mark migration accepted for that project/workstream.

No permanent “compatibility mode” is introduced.

## Product cutover safety

Do not point normal users at V2 merely because implementation compiles. Cutover requires the M08 + M09 gates.

After production acceptance:
- ChatGPT user-owned Project Instructions may be changed to V2;
- the pw plugin is updated to the accepted V2 package;
- existing project repositories migrate only explicitly;
- V1 stays available as history/migration reference until no supported migration need remains;
- future ordinary semantic changes are made only in V2.

Rollback before broad adoption is operationally simple: keep V1 untouched and do not migrate a project until V2 acceptance. After a project is explicitly migrated, rollback is not “switch the execution_policy back”; it requires an explicit state-safe migration/recovery decision, because V2 intentionally has no permanent dual semantics.

---

# 12. JIT boundaries and YAGNI audit

The plan intentionally does not freeze the following before evidence exists:

| Deferred detail | Trigger that makes it knowable |
|---|---|
| exact YAML/JSON field names beyond required semantic ownership | M01 schema fixtures/validators need them |
| exact review-subject serialization | M04 can bind it to actual M01 Git/state model |
| exact GitHub tracker dedup marker/query | M02 inspects actual GitHub capability/API behavior |
| exact plugin metadata/hook API details | M06 inspects current real Codex packaging/runtime |
| downstream Card IDs and predecessor-dependent technical interfaces | predecessor evidence satisfies M03 JIT trigger |
| separate technical-contract/OpenSpec artifact | Card scope materially needs contract detail beyond Card |
| rebase vs merge target refresh mechanics | M05 current repository rules/source state |
| fork release module | durably declared downstream-fork release/version operation |
| competing prototype branches | Research proves real A/B evidence need |
| extra migration handlers | concrete supported V1 fixture/state requires them |

Explicitly not planned because current authority rejects or does not justify them:

- generic runtime adapter framework;
- plugin/provider registry;
- global workstream registry;
- project DAG engine;
- Project-Card scheduler;
- capability inventory/preflight state;
- runtime/model/session telemetry store;
- Context Health lifecycle;
- universal OpenSpec;
- second project-control database;
- permanent legacy compatibility router;
- exact project workflow patch pin per project;
- speculative distant interfaces/cards.

YAGNI result: each material mechanism in the plan traces to a current requirement/ADR/validation obligation. No major subsystem exists solely for hypothetical extensibility.

---

# 13. Key implementation risks and ordering constraints

## R1 — Semantic duplication reappears through delivery adapters

Risk: Skill/hook/ChatGPT prompt starts restating policy and drifts from workflow/.

Control: M06 packaging tests compare behavior/source composition and forbid semantic duplication. Ordinary semantic edits must not require adapter changes.

## R2 — Progressive disclosure becomes a slogan rather than an enforced contract

Risk: router/Skill preloads neighboring stages or all docs, wasting Codex context.

Control: M01/M08 use negative read-set fixtures for A01/A02; bootstrap text is deliberately small.

## R3 — #issue regresses into autonomous repair

Risk: diagnosis recommendation is mistaken for implementation authorization.

Control: M02 durable alignment state requires a subsequent user response and explicit aligned authorization; L02 is mandatory.

## R4 — Semantic review independence is weakened by omitting runtime identity

Risk: durable state cannot prove reviewer independence if it simply drops all provenance.

Control: record semantic independence basis and subject-production relationship, not product/session identifiers. Runtime must refuse self-review when current context produced/repaired subject; attempt record proves the required semantic condition.

## R5 — Review reuse either churns unnecessarily or becomes unsafe

Risk: any SHA drift forces re-review, or material change slips through reused GREEN.

Control: M05 compares exact covered subject/acceptance plus affected verification. SHA-only drift is insufficient; material content/behavior/acceptance change creates new subject.

## R6 — Source branch disappears before terminal recovery data is durable

Risk: GitHub auto-delete makes Close unrecoverable.

Control: M05 requires all unique pre-merge recovery artifacts in merge subject/target-side package before merge.

## R7 — Legacy migration imports forbidden scheduler/runtime state

Risk: V2 silently becomes a legacy compatibility product.

Control: M07 explicit transformation/drop rules plus A15/A17 and M08 negative lint. Ambiguous live concurrency fails closed.

## R8 — GitHub tracker duplicates or closes early

Risk: retries create duplicate Issues or intermediate PR closes full scope.

Control: durable tracker pointer, dedup before create, final-scope-only closing linkage, post-merge readback.

## R9 — Plugin packaging assumptions stale by implementation time

Risk: plan hard-codes obsolete Codex plugin details.

Control: metadata/API details are M06 JIT after inspecting current runtime; semantic package constraints remain fixed.

## R10 — Automated tests pass but real product surfaces differ

Risk: ChatGPT Android, Codex SessionStart, model switching or real GitHub semantics do not match fixtures.

Control: M09 required L01..L09, including deferred N-CAPABLE and N-CHATGPT continuity.

## R11 — Schema over-design before execution evidence

Risk: V2 recreates V1 complexity under new names.

Control: M01 fixes ownership/invariants first; exact fields are introduced only to satisfy concrete transitions/tests.

## R12 — Runtime internal concurrency leaks into Project Workflow state

Risk: delegated workers become Cards or competing writers.

Control: M03 hard boundary: one Project Card, coordinator-only shared reconciliation, worker result packages only.

---

# 14. Planner-side completeness and challenge audit

## Completeness checks

- PWV2-REQ-001..076: GREEN — 76/76 explicitly mapped.
- ADR-PWV2-001..006: GREEN — 6/6 explicitly preserved with anti-regression boundaries.
- V1->V2 coverage matrix: GREEN — every identified surface has a disposition in Section 9; A17 makes this machine-regressed.
- V2 validation matrix: GREEN — A01..A17 and L01..L09 all have milestone owners and execution timing.
- Milestone ordering/dependencies: GREEN — state kernel precedes lifecycle, lifecycle precedes execution, execution precedes close, adapters follow stable semantics, migration remains outside normal routes, validation precedes cutover.
- Migration/cutover: GREEN — V1 remains untouched until accepted V2; bounded migration only; no dual semantic mode; cutover gated by automated + real-product validation.
- JIT boundaries: GREEN — predecessor/runtime-dependent details are deferred with exact triggers; strategic invariants are not deferred.
- YAGNI: GREEN — rejected machinery remains absent; selective technical contract and migration handlers are evidence-triggered.
- Production readiness: GREEN as a plan — concrete A/L gates and no unresolved acceptance category are missing.

## Challenge pass

Question: Could M06 be built before M04/M05 to get faster product smoke tests?
Answer: packaging skeleton may be scaffolded earlier, but binding final delivery semantics before review/recovery/close stabilize risks adapter-driven design. Keep M06 acceptance after common semantics are stable; early noncanonical packaging spikes are allowed only if they do not become authority.

Question: Should GitHub Issue integration be postponed to Close?
Answer: no. Dedup/correlation begins at Intake and must be durable early; only closure belongs to Close.

Question: Should exact review subject schema be frozen in M01?
Answer: no. M01 must provide immutable-reference primitives, but M04 should choose the minimal encoding after actual workstream/Card/Git representation exists.

Question: Should legacy migration be used to bootstrap the V2 workflow itself?
Answer: no. V2 is built clean. Migration is a bounded consumer of V2 semantics, deliberately after the normal lifecycle is defined.

Question: Does one active Project Card prevent runtime parallelism?
Answer: no. It deliberately limits Project Workflow state concurrency while allowing runtime-owned subagent concurrency inside the Card.

Question: Could premium A/B/C be represented only as chat instructions?
Answer: no. They must survive Recovery, therefore the semantic obligation must be durably recoverable even though model choice itself is not canonical state.

Question: Does “best available model” require a named model in workflow?
Answer: no. The recommendation is human-facing and runtime-relative; canonical workflow stores the stop/role requirement, not a product model name.

Question: Is a separate OpenSpec required to preserve rigor?
Answer: no. Every change has a precise Card. A separate technical contract is triggered only when it materially improves behavior/design-contract precision.

Question: Could target SHA drift alone force a fresh final review for safety?
Answer: that would contradict accepted authority. Safety comes from affected compatibility verification and exact subject comparison; only material covered change creates a new subject.

Question: Is a repository-global workstream index useful?
Answer: an optional non-authoritative navigation aid could be introduced later only with concrete current value, but correctness must not depend on one and this plan does not require it.

## Planner verdict

GREEN.

The plan is executable from the frozen Definition without inventing product/system intent. It deliberately preserves strategic invariants, defers implementation detail only where predecessor/runtime evidence is required, gives every requirement and validation scenario an owner, and keeps V1 migration/delivery adapters from becoming competing semantic products.

Per the experiment contract, this planner-side verdict is the terminal action for this artifact. No Independent Plan Review, canonical plan mutation, premium-stop-B state mutation or Execution Prep follows from this experiment.
