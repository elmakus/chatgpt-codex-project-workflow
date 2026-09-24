# Master Plan — PWv2.1 Policy Kernel

Plan revision: P3
Planning cycle: 3 (entry subject `definition:R2|planning-cycle:3`)
Lifecycle: owned by `PLANNING.toml`; this P3 text is the immutable review
subject once frozen and states no mutable lifecycle of its own.
Review requirement: REQUIRED independent Stage-6 Plan Review (review_mode `independent`)
Workstream: `change-pwv21-policy-kernel-brainstorming`
Predecessor: cycle 2 / P2 exact frozen subject
`elmakus/chatgpt-codex-project-workflow@ca046952a4d249d9ed74af6408db71b0ded73a8f:planning/PWV21_POLICY_KERNEL_MASTER_PLAN_P2.md@79ee0b6588be32767ba283b9f20a48a192999001`.
Correction authority/derivation:
`implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/DEFINITION_R2_COMPLETE_2026-09-24.md`.
P3 preserves terminal M01/M02 history, adds bounded bootstrap milestone M02R
before the still-unmaterialized M03, and maps all 127 accepted requirements
exactly once. Its material change implements and dogfoods the R2
review-convergence, decomposition-fidelity and live-validation semantics
without rewriting historical M02.

## Authority

- Requirements: `requirements/PWV21_POLICY_KERNEL.md` R2 (status `approved`,
  Definition subject `pwv21-policy-kernel@2`, 127 accepted requirements
  PWV21-REQ-001…PWV21-REQ-127)
- Decisions (all status `accepted`):
  - `decisions/ADR_PWV21_POLICY_KERNEL.md` (ADR-PWV21-001)
  - `decisions/ADR_PWV21_ORCHESTRATION_CONTRACT.md` (ADR-PWV21-002)
  - `decisions/ADR_PWV21_PARALLEL_CARDS.md` (ADR-PWV21-003)
  - `decisions/ADR_PWV21_REVIEW_LIFECYCLE.md` (ADR-PWV21-004)
  - `decisions/ADR_PWV21_RECOVERY_MIGRATION_HANDOFF.md` (ADR-PWV21-005)
  - `decisions/ADR_PWV21_DECOMPOSITION_FIDELITY.md` (ADR-PWV21-006)
  - `decisions/ADR_PWV21_LIVE_VALIDATION.md` (ADR-PWV21-007)
- Definition record:
  `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/DEFINITION.toml`
  (R2, green, premium A satisfied)
- Planning record:
  `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/PLANNING.toml`
  (cycle 3 / P3; that record alone owns mutable lifecycle). Earlier P1/P2
  lifecycle is preserved by immutable historical Git subjects.
- Implementation baseline: the existing executable V2 router/state-contract
  model in `elmakus/project_workflow_v2` (operational authority, current main).
  This plan extends that baseline; it does not rewrite from a Markdown-only
  router and does not create an orchestration platform.

This plan creates no implementation authority. Task Board/Card creation,
Execution Prep, and execution begin only after independent Plan Review GREEN,
approval consumption, and premium C satisfaction through the normal V2 gates.

## Goal

Evolve the existing Project Workflow V2 implementation conservatively into
PWv2.1: deterministic workflow mechanics are derived by a small stateless
policy kernel while semantic reasoning stays role/LLM-owned, Git/repository
state stays canonical, and execution may move between ChatGPT and OR/Paseo
without private runtime state becoming authority.

## Non-goals (from accepted Definition)

- A general workflow programming language or arbitrary-expression DSL.
- Moving semantic product/strategy/review judgment into deterministic code.
- Making OR/Paseo, worker sessions, worktrees, retries, provider/model
  identity, or telemetry canonical PW state.
- Hiding multiple mutating owners inside one Card.
- Allowing overlapping mutating Card scopes to execute concurrently.
- Replacing individual Card review with integration/compatibility review.
- Requiring the Python helper to recover a project.
- Rewriting historical PWv2 state wholesale during migration.
- Automatic worker/reviewer model switching.
- Worker telemetry/progress UI as a PWv2.1 concern.

## Strategy overview

P3 uses one bounded bootstrap correction milestone, `M02R`, between the
already-terminal M02 and the still-unmaterialized M03. M01 and M02 are
historical completed milestones and are not reopened. M02R implements the
R2 workflow-semantic corrections that must exist before downstream dogfood.

```
M01 ──► M02 ──► M02R ──► M03 ──► M04 ──► M05 ──► M06 ──► M07
 done    done
```

Serial order for new work. No downstream milestone may start before its
immediate predecessor is GREEN.

| Milestone | Serial gate | Semantic prerequisites | Rationale |
|---|---|---|---|
| M01 Policy kernel core | — | — | Historical terminal milestone; preserved, not reopened |
| M02 Obligation/Result contracts | M01 | M01 registry + kernel seams | Historical terminal milestone; preserved, not reopened |
| M02R R2 workflow-semantic bootstrap | M02 | Definition R2 + terminal M02 evidence | Implements review convergence, decomposition fidelity and live-validation handling before downstream JIT |
| M03 Portability and parity | M02R | M01/M02 implementation + M02R semantics | First downstream authority-level dogfood and candidate-branch shadow/replay validation |
| M04 Parallel Cards | M03 | M01 validation, M02 per-Card contracts | Kernel validates parallel sets; each Card needs typed obligation/result and staleness handling |
| M05 Review lifecycle integration | M04 | M02R review baseline + M02/M04 subjects | Completes/integrates the full review lifecycle over parallel/invalidation cases without redefining M02R semantics |
| M06 Runtime and handoff | M05 | M02 obligations, M05 stops/freshness | Handoff locator binds entry obligations; auto-continuation interacts with review freshness and stops |
| M07 Recovery, migration, close | M06 | M01–M06 complete surface | Fail-closed integration, lazy migration rehearsal, and close over the complete surface |

### Bootstrap/dogfood boundary

The consumer project continues to use canonical `elmakus/project_workflow_v2@main`
as its workflow authority. The PWv2.1 candidate implementation remains on the
separate `work/pwv21-policy-kernel` branch until normal integration/release.

Therefore:
- M02R is implemented under current canonical V2 governance, with P3 itself
  freezing the bootstrap Card seams needed to prevent another mega-Card;
- M03 is the first **authority-level dogfood** of the R2 decomposition/review
  rules: Execution Prep must follow the accepted P3 seam classifications;
- M03 also runs the candidate PWv2.1 branch in shadow/replay where applicable
  against its real materialization/review evidence;
- this is not misreported as proof that `project_workflow_v2@main` already
  enforces the candidate mechanics;
- the first independent deployed consumer test remains Paseo/Pi after the
  corrected PWv2.1 implementation is integrated/released.

The plan's own execution never requires changing the Project bootstrap to a
candidate workflow branch and never makes candidate runtime state canonical.

## Implementation target and contribution boundary

All milestone outputs are specified as extensions to the executable V2
baseline in `elmakus/project_workflow_v2` (contracts, executable code, and
tests). This plan authorizes no cross-repository writes: the exact
contribution vehicle for landing changes in that repository (branch/PR flow,
Card workspaces) is a bounded Execution Prep choice after premium C, and
any product/strategy question it surfaces returns through the normal
escalation paths. Until then, the baseline remains read-only reference.

## Verified baseline-to-change map

Current PWv2.1 implementation baseline for new work:
`elmakus/project_workflow_v2@work/pwv21-policy-kernel` at
`e7a939e0a37f3cfcb7e39e04d5654b94101a5090` (terminal M02 candidate
subject). Canonical governance authority for this consumer remains current
`elmakus/project_workflow_v2@main`; the candidate branch is implementation
input/shadow-test target, not workflow authority. Each milestone extends the
named observed seams and preserves the named behavior. Future
serialization/naming/layout choices stay flexible under REQ-010.

| Milestone | Observed baseline seams extended | Preserved |
|---|---|---|
| M01 | `tools/state_contract.py` validators + `reject_prohibited_keys`; `tools/router.py` `select_route` predicate chain + `result()`/`recovery()`; `workflow/ROUTER.md`, `workflow/STATE.md`, `schemas/STATE_ENVELOPE.md`; `tests/test_router.py`, `tests/test_state_contract.py`, `scripts/test-router.sh`, `scripts/test-state-envelope.sh` | All existing route/stop obligations and record validators; full baseline suite stays GREEN |
| M02 | `tools/execution_contract.py` (`choose_realization`, `classify_return`, `parse_card_result`); `validate_bundle` + `result` locator class; `templates/TASK_CARD.md`, `templates/CARD_RESULT.md`; `workflow/EXECUTION.md`, `workflow/EXECUTION_PREP.md`; `tests/test_execution_contract.py` | Card-as-unit execution; coordinator-owned result persistence; launch-refresh semantics |
| M02R | `workflow/REVIEW.md`, `workflow/EXECUTION_PREP.md`, `workflow/PLANNING.md`, review/Task Board state contracts and tests | Existing subject-relative review and JIT refinement stay valid while gaining exhaustive review, bounded convergence, seam fidelity, topology challenge and live-finding reconciliation |
| M03 | `tests/fixtures/router` + `tests/fixtures/state` corpora; `select_route` as the reference path with its exact `read_set`; `scripts/test-*.sh` gates | Helper-preferred-but-optional posture; progressive-disclosure read order |
| M04 | `validate_board` one-Card `in_progress` invariant + revision mutation guard; `parse_task_card` authority/dependency/tests/review fields (no write-scope fields today); `TASK_BOARD.toml` + `cards/`; `workflow/EXECUTION.md` | Serial default; Card identity/authority; per-Card result/review records |
| M05 | `tools/review_contract.py` `select_review_realization`; `validate_review`/`validate_review_history` (`materially_produced_or_repaired_subject` independence); `REVIEW_ATTEMPT` + `PLAN_REVIEW` records; `close_contract.classify_review_coverage`; `workflow/REVIEW.md`, `workflow/PLAN_REVIEW.md`; `tests/test_review_contract.py` | Subject-relative independence; append-only attempts; evidence-gated verdicts |
| M06 | Router stop taxonomy (`premium_A`/`premium_B`/`premium_C`, `definition_promotion`, `issue_alignment`, `explicit_user_stop`, end-of-scope) + `USER_STOP.md` locator-only handoff rendering; `tests/test_router.py`; `test_chatgpt_delivery.py`/`test_codex_delivery.py` as runtime-neutrality regression | Stop taxonomy; locator-only handoff; no canonical runtime preference |
| M07 | `tools/recovery_contract.py` (`classify_resolution`, `exact_result_subject`, `review_subject`); `tools/migration_apply.py` + `v1_migration.py` + `test_migration_apply.py`/`test_migration_rehearsal.py`/`test_v1_migration.py`; `tools/close_contract.py` (`close_continuation`, `verify_*`, `cleanup_branch_action`); `workflow/RECOVERY.md`, `workflow/CLOSE.md`; `tests/test_recovery_contract.py`, `tests/test_close_contract.py` | Fail-closed recovery; history-preserving migration; close continuation semantics |

Authority input pins for P3 (consumer branch state containing Definition R2):

| Input | Path | Blob |
|---|---|---|
| Requirements R2 | `requirements/PWV21_POLICY_KERNEL.md` | `6f2fd5ace3ef20c708c995115f56efd9de009a33` |
| ADR-PWV21-001 | `decisions/ADR_PWV21_POLICY_KERNEL.md` | `0662b970d80e8b76df79e4dbd458d190ce6d4402` |
| ADR-PWV21-002 | `decisions/ADR_PWV21_ORCHESTRATION_CONTRACT.md` | `051f8fc3f68773349a1fcad39fcf1c60d3157532` |
| ADR-PWV21-003 | `decisions/ADR_PWV21_PARALLEL_CARDS.md` | `437388345d7136cdcdf241bf3ca6aa1016ddb1c0` |
| ADR-PWV21-004 | `decisions/ADR_PWV21_REVIEW_LIFECYCLE.md` | `60f95d9a578b10e367a066599d4a89f02b60717b` |
| ADR-PWV21-005 | `decisions/ADR_PWV21_RECOVERY_MIGRATION_HANDOFF.md` | `fbaaaedac492ff9e2dbf4db9f8e86b3376df2023` |
| ADR-PWV21-006 | `decisions/ADR_PWV21_DECOMPOSITION_FIDELITY.md` | `673a2781d5c6da048e50d27e39cc4857606ec9f8` |
| ADR-PWV21-007 | `decisions/ADR_PWV21_LIVE_VALIDATION.md` | `6adbbef4a40f6005ec09e1a3f73289e256f44b12` |

## M01 — Policy kernel core and mechanical truth

**P3 lifecycle note:** historical terminal milestone. P3 does not reopen or
re-execute M01; its accepted result remains predecessor authority/evidence.


### Outcome

A small stateless read-only policy kernel extends the existing V2 executable
router/state-contract model only for mechanically derivable predicates, with
a versioned machine-readable registry, one canonical representation plus a
checked human-readable projection, and drift tests that fail closed.

### Requirement coverage

Owns PWV21-REQ-001…PWV21-REQ-010 (10 requirements; per-requirement
verification in Appendix A).

### Planned work

1. Derive the mechanical-predicate allowlist from the existing V2
   router/state-contract conditions; each entry names its canonical
   repository-state inputs.
2. Implement the versioned registry (schema + loader + version gate),
   define the stateless read-only kernel seams/interfaces
   (route/validate/compile-obligations/validate-results/reconcile
   signatures over the existing routes), and implement the mechanical
   predicate core. Full Obligation/Result compiler and acceptance
   implementation belongs to M02, which builds on these seams.
3. Write the canonical human-readable contract semantics for every predicate
   and the checked projection from the canonical representation.
4. Implement the drift contract tests (registry ↔ implementation ↔ contracts)
   with fail-closed behavior on disagreement.
5. Document the REQ-010 option space and its invariance boundary so Execution
   Prep cannot silently alter authority or user-visible semantics.

### Acceptance

- Every new predicate traces to canonical repository-state inputs; no
  semantic input is accepted by kernel code.
- Repeated kernel calls over identical inputs return identical outputs; the
  kernel performs no canonical writes.
- Registry entries validate against the fixed vocabulary; arbitrary
  expressions are rejected.
- Regenerated human-readable projection matches the checked-in projection.
- Every registry predicate has a canonical contract section; the coverage
  test enumerates this from the registry (no hand-maintained list).
- Injected registry/implementation/contract disagreement fails closed.
- Existing V2 router/state-contract tests remain GREEN (no regression in the
  baseline).

### Verification strategy

- Unit tests for registry loading/versioning/vocabulary rejection and kernel
  purity/read-only behavior.
- Projection freshness test and predicate contract-coverage test.
- Drift tests with injected disagreement fixtures (fail-closed assertions).
- Full V2 baseline suite as regression gate.

### JIT / implementation boundary

Execution Prep may split M01 into bounded Cards (registry, kernel entry
points, projection/docs, drift tests) only along the seams above. Exact
serialization, naming, and module layout are JIT choices within the REQ-010
boundary. Any new predicate beyond the allowlist, or any semantic input to
the kernel, returns to Strategic Planning.

## M02 — Typed Execution Obligation and Result contracts

**P3 lifecycle note:** historical terminal milestone. M02 has terminal fresh
Card GREEN and fresh Milestone GREEN on the corrected exact subject. P3 does
not reopen it; its real failure history is used only as immutable regression
input for M02R.


### Outcome

Versioned transport-neutral typed `Execution Obligation` and `Execution
Result` contracts (JSON preferred) with PW-owned authority resolution,
deterministic identity/freshness, stale-result reconciliation, mutation
pre/postconditions with governed writes and readback, and no canonical
telemetry.

### Requirement coverage

Owns PWV21-REQ-018…PWV21-REQ-033 (16 requirements; per-requirement
verification in Appendix A).

### Planned work

1. Define the versioned Obligation/Result schemas, JSON serialization, and
   version-compatibility/fail-closed rules.
2. Implement PW authority resolution (exact ref/hash validation, bounded
   bundle materialization) and deterministic obligation derivation
   (identity + minimal freshness fingerprints).
3. Implement result acceptance: identity/fingerprint revalidation,
   stale/conflicted classification, and the reuse/rebase/reconcile vs
   re-execute decision with its proof obligation.
4. Implement mutation pre/postcondition emission, governed-write handoff,
   and mandatory readback/validation; document the OR/Paseo no-direct-mutation
   boundary and the unknown-side-effect readback rule.
5. Add contract tests for schema validation, version rejection, telemetry
   exclusion, determinism, fingerprint minimality, and stale-result handling.

### Acceptance

- Obligations validate against the versioned schema; identical canonical
  inputs derive byte-identical obligations (including `obligation_id`).
- Fingerprints change only when materially determining inputs change
  (minimality test with unrelated-file perturbation).
- Authority resolution rejects inexact refs/hashes; bundles contain only
  the required sources.
- Stale results are classified and reconciled/re-routed; blind acceptance
  is impossible by construction and covered by a negative test.
- Breaking-version payloads fail closed with a typed error, never partial
  application.
- No telemetry field exists in schemas, fixtures, or canonical state; a
  negative vocabulary test guards this.
- Mutation writes occur only through governed coordinator/role actions with
  readback evidence; unknown side effects block retry until reconciled.

### Verification strategy

- Schema unit tests (valid/invalid/version matrix) and golden JSON fixtures
  for representative obligations/results.
- Determinism and fingerprint-minimality tests.
- Stale-result scenario tests (concurrent invalidation, base change,
  safe-reuse proof, forced re-execution).
- Negative tests: telemetry vocabulary, direct-mutation boundary,
  blind-retry prohibition.
- M01 drift tests extended to cover new kernel predicates introduced here.

### JIT / implementation boundary

Execution Prep may split M02 into schema, derivation/resolution, acceptance/
reconciliation, and mutation-handoff Cards. Schema field naming and internal
module layout are JIT choices under REQ-010. Any change to authority
resolution semantics, freshness coverage, or the mutation boundary returns
to Strategic Planning.

## M02R — R2 workflow-semantic bootstrap

### Outcome

Before any M03 Card is materialized, the candidate PWv2.1 implementation
contains the accepted R2 semantics for exhaustive fresh review and bounded
convergence, Planning-to-Execution-Prep decomposition fidelity, and safe
live-finding reconciliation. Historical M02 remains untouched and is replayed
only as regression evidence.

### Requirement coverage

Owns PWV21-REQ-108…PWV21-REQ-127 (20 requirements; per-requirement
verification in Appendix A).

### Required decomposition seams — bootstrap authority

Because the generalized topology-challenge machinery is itself implemented
by this milestone, P3 freezes three **required_seam** boundaries for M02R.
Execution Prep MUST materialize separate Cards for these seams and MUST NOT
merge across them. Further splitting is allowed when current evidence
justifies it.

1. **R2-A — review completeness and convergence**: REQ-108…114.
2. **R2-B — decomposition fidelity and topology challenge**: REQ-115…121.
3. **R2-C — live-validation reconciliation and regression replay**:
   REQ-122…127.

This bootstrap rule prevents M02R from reproducing the M02 mega-Card failure
without pretending the not-yet-implemented generic seam mechanism already
exists.

### Planned work

1. R2-A: extend review contracts/state/tests so formal lifecycle distinguishes
   finding verification from fresh full-scope review; enforce complete-pass
   finding collection, class-level repair evidence, stable review epochs,
   5/4/3 default hard ceilings, convergence mode-switch and one
   post-convergence validation.
2. R2-B: extend Planning/Execution Prep contracts and validation so
   `required_seam` / `preferred_seam` / `illustrative` intent is durable,
   JIT cannot silently override required seams, preferred-seam deviation
   requires bounded rationale, and materially risky topology receives a
   narrow fresh independent topology challenge.
3. R2-C: add live-finding classification/reconciliation semantics, downstream
   affected-JIT gate behavior, tracker-non-authority guards, immutable
   historical regression replay, and an M02 regression corpus.
4. Add bootstrap/regression tests proving the historical M02 one-mega-Card
   topology fails the new decomposition policy absent valid atomicity
   rationale, without modifying historical M02 Task Board/review state.
5. Preserve runtime neutrality: review/topology obligations remain semantic;
   model/session/worker identity is not made canonical.

### Acceptance

- Known-finding verification cannot satisfy a required fresh full-scope review.
- A full review continues after first blocker and records the complete
  independently discovered material finding set before repair.
- Class-level repair evidence includes sibling/negative-space coverage.
- Stable epochs and 5/4/3 hard ceilings are mechanically represented;
  ordinary repair cannot reset the epoch.
- Hard ceiling routes to convergence analysis, never GREEN; one
  post-convergence validation is permitted and a further RED routes to
  structural classification rather than an automatic new ordinary review.
- Required/preferred/illustrative seam semantics are contract-tested.
- Required seam merge is rejected/routed to Planning.
- Preferred seam merge without qualifying durable rationale is rejected.
- Risky topology obtains a distinct fresh topology challenge; trivial
  topology does not incur it.
- Live findings block only explicitly affected downstream JIT boundaries.
- Tracker text never becomes authority.
- M02 regression replay proves the historical mega-Card topology and
  repeated-review failure modes are caught by the corrected semantics while
  `M02-T01` remains terminal and unchanged.
- Full candidate branch baseline + M01 + M02 suites remain GREEN.

### Verification strategy

- State-machine/unit fixtures for review epochs, ceiling counting, verification
  vs full-review distinction and convergence routing.
- Negative fixtures for early-stop review, literal-only repair, epoch-reset
  abuse, required/preferred seam bypass and tracker-as-authority.
- M02-derived immutable regression fixtures for topology and review history.
- Independent topology-challenge fixtures spanning risky and trivial cases.
- Readback/assertions proving no historical M02 mutation.

### JIT / implementation boundary

The three R2-A/R2-B/R2-C seams above are Planning-level `required_seam`
authority for this bootstrap milestone. Execution Prep may split within a seam
but cannot merge seams. Exact schema/field/module naming remains JIT under
REQ-010. Any weakening of 5/4/3 ceilings, exhaustive full-pass semantics,
seam classes, topology-challenge trigger classes, tracker non-authority or
historical-state preservation returns to Strategic Planning/Definition as
appropriate.

## M03 — Portability, helper-less recovery, and parity

### Outcome

Canonical Git/repository state plus portable workflow contracts suffice for
a fresh capable ChatGPT/runtime to reconstruct the exact legal continuation
without OR/Paseo private state or helper cache; helper-derived and
helper-less routing agree on representative states, and a destructive
recovery test proves Git-alone continuation.

### Requirement coverage

Owns PWV21-REQ-011…PWV21-REQ-017 (7 requirements; per-requirement
verification in Appendix A).

### Planned work

1. Define the helper-less derivation procedure as canonical contract text:
   the exact read order, inputs, and decision rules a fresh reasoning
   context follows from Git state alone.
2. Define the independent parity acceptance protocol: a fresh capable
   reasoning context receives ONLY the exact canonical Git state and the
   portable contracts for a fixture — no helper/routing output, no
   expected verdict labels, no old transcript, no OR private state, no
   helper cache — and locks its exact next-obligation/stop verdict plus
   cited source evidence BEFORE any comparison with reference results.
   Disagreement is a parity defect routed fail-closed to Recovery.
3. Build the high-risk fixture corpus (RED/recovery states, fresh-review
   boundaries, parallel Cards, PWv2 migration states, stale results).
4. Implement the destructive recovery acceptance on isolated disposable
   test surfaces only (never user state): discard chat memory, OR/Paseo
   state, and helper cache; a fresh context reconstructs from canonical
   Git alone and locks its verdict+evidence before comparison.
5. Establish the REQ-016 feature-admission rule and apply it to M01/M02
   outputs (retroactive check) and all later milestones (entry check).

### Acceptance

- A fresh capable reasoning context, given only canonical Git state and
  portable contracts, reconstructs the exact legal continuation for every
  corpus fixture; programmatic checks may support coverage but never
  substitute for this acceptance.
- Independent-context verdicts agree with reference results across the
  corpus; every disagreement is recorded as a parity defect and routes
  fail-closed to Recovery (injection tests prove the fail-closed path).
- Seeded fixture corpus covers the classes available at M03
  (RED/recovery, fresh-review boundaries, stale results) with RED/boundary/
  stale variants where applicable, and defines the extension points for the
  parallel-Card, migration, and runtime-switch classes folded in by
  M04–M07 (final all-class corpus audit at M07).
- Destructive acceptance passes on isolated disposable surfaces: after
  discarding memory/runtime/helper state, Git alone yields the exact legal
  continuation, with verdict+evidence locked before comparison; user state
  is never touched.
- M01/M02 outputs pass the REQ-016 admission check; any failure returns to
  the owning milestone as corrective work, not as a helper dependency.
- Raw evidence per fixture (fixture identity, provided inputs, locked
  verdict, cited source evidence) is retained; unavailable required
  acceptance fails visibly as blocked acceptance, never silent GREEN.

### Verification strategy

- Independent-context parity acceptance over the shared corpus (the
  locked-verdict protocol above); disagreement-injection tests assert
  fail-closed routing; programmatic agreement checks are supporting
  coverage only.
- Destructive acceptance as a standalone gate on isolated disposable
  surfaces (documented discard protocol + locked verdict/evidence +
  reconstruction assertions + user-state preservation proof).
- REQ-016 admission checklist applied per milestone and recorded in review
  evidence.
- Helper/router-outage simulation tests assert no user stop when canonical
  contracts suffice (REQ-013).

### Planning decomposition intent / JIT boundary

M03 is the first downstream dogfood of the R2 decomposition semantics.

- `required_seam`: destructive recovery acceptance remains a standalone
  independently observable gate and cannot be merged away.
- `preferred_seam`: helper-less derivation contract.
- `preferred_seam`: independent parity harness + representative corpus.
- `preferred_seam`: REQ-016 feature-admission/revalidation surface.
- Fixture encoding and harness internals remain JIT choices.
- Any merge of preferred seams requires qualifying durable technical rationale
  and the R2 risk-based fresh topology challenge.
- Any weakening of the independent-context protocol, discard protocol or
  admission rule returns to Strategic Planning.

M03 acceptance must retain the actual Execution Prep topology/rationale/
challenge evidence and compare the candidate PWv2.1 branch's shadow/replay
classification against the governed P3 materialization. No special user prompt
may substitute for missing candidate semantics.

## M04 — Parallel Cards and execution ownership

### Outcome

Multiple Cards may execute concurrently inside one workstream only when the
accepted Plan/JIT explicitly declares a finite parallel-safe set; the kernel
validates dependencies, machine-checkable write scopes, external effect
domains, and authority/scope overlap; every Card keeps one primary mutating
Worker, its own obligation/result/review, and integrated compatibility
before combined downstream consumption.

### Requirement coverage

Owns PWV21-REQ-034…PWV21-REQ-055 (22 requirements; per-requirement
verification in Appendix A).

### Planned work

1. Define the parallel-set declaration contract (membership, rationale,
   inputs, write scopes, effect domains) and its Plan/JIT ownership rules.
2. Implement kernel validation: dependency analysis, write-scope overlap
   detection, effect-domain checks, authority/scope overlap, uncertainty →
   serial collapse, single-set membership enforcement.
3. Implement parallel execution semantics: subset start, scoped RED/block
   propagation, sibling staleness/reconciliation, unaffected-result
   preservation, integrated compatibility obligation, workstream
   independence.
4. Define the PW-side Card ownership contract as typed semantic
   obligations with eligibility and evidence: single-mutating-owner
   legality, advisory-helper bounds, no-recursive-spawning rule,
   assignment freshness/persistence/replacement/close eligibility, and
   duplicate-mutator prohibition — plus the acceptance boundary PW checks
   on results. OR owns actual assignment, launch, replacement, archive,
   model/session selection, concurrency, and isolation; PW defines no
   scheduler, no runtime topology, and no canonical runtime IDs.
5. Add scenario tests for every rule above, including the no-override
   (REQ-038), uncertainty-collapse (REQ-039), and compatibility-before-
   consumption (REQ-053/054) gates.

### Acceptance

- Kernel validation denies a proposed invalid *parallel authorization*
  (never the Cards themselves) for undeclared pairs, overlapping mutating
  scopes, insufficient independence proof, and proposed multi-set
  memberships; the same valid Cards remain routable and route serially
  instead. In contrast, contradictory ALREADY DURABLE multiple-active-set
  membership in canonical bindings is a binding conflict that fails
  closed to Recovery rather than being silently ignored or normalized
  into a serial run.
- No configuration, flag, or API path permits overlapping mutating scopes
  to run concurrently (negative test over the full option surface).
- RED/block propagation matches REQ-042 exactly on a dependency-matrix
  fixture (self + successors stop; independents continue).
- Each parallel Card produces separate obligation/result/review/evidence;
  downstream combined consumption is impossible without the compatibility
  obligation; compatibility evidence never substitutes for Card review.
- PW ownership acceptance holds on lifecycle-evidence fixtures (fresh
  assignment eligibility, repair persistence, allowed replacement with
  unchanged scope/authority, close on terminal, no duplicate mutators, no
  recursive spawns); fixtures assert PW's semantic verdicts over
  OR-reported lifecycle evidence, never PW-managed runtime state.
- Workstream-independence fixtures prove blockers do not cross workstream
  boundaries.

### Verification strategy

- Kernel validation unit tests over a write-scope/effect-domain matrix
  (overlap, adjacency, insufficient independence proof, proposed multi-set
  denial to serial, durable multi-set binding conflict to Recovery).
- Execution-semantics scenario tests (subset start, propagation, staleness,
  preservation, compatibility gate).
- PW ownership-acceptance tests over lifecycle evidence plus negative
  tests (override absence, duplicate mutators, recursive spawning,
  canonical runtime IDs).
- New fixtures folded into the M03 parity corpus (parallel-Card class).

### JIT / implementation boundary

Execution Prep may split M04 into declaration/validation, execution
semantics, ownership, and scenario-test Cards. Scope-expression syntax
details are JIT choices under REQ-010/037. Any relaxation of validation,
propagation, ownership, or compatibility rules returns to Strategic
Planning.

## M05 — Independent review lifecycle integration

### Outcome

Layered fresh independent review: every Card, every Milestone, and every
completed workstream receives independent review with subject-relative
freshness, complete-evidence GREEN, bounded automatic RED repair/re-review,
targeted revalidation on invalidation, and no user stop when a qualifying
fresh Reviewer can be launched automatically.

### Requirement coverage

Owns PWV21-REQ-056…PWV21-REQ-076 (21 requirements; per-requirement
verification in Appendix A). M02R already owns REQ-108…114 and supplies the
convergence baseline that M05 must integrate across the complete Card/
Milestone/final-integration lifecycle rather than redefine.

### Planned work

1. Define the review-subject, independence-provenance, and evidence
   contracts for Card, Milestone, and final-integration review, including
   contamination rules and the no-prior-opinion information boundary.
2. Implement the review lifecycle state machine: assignment freshness,
   verdict validity (evidence completeness), RED repair/re-review loops
   with failure ceiling, reopening, targeted revalidation, and correction
   routing.
3. Define the independence obligation as a typed PW semantic contract:
   launch-eligibility conditions, subject-relative semantic eligibility
   evidence (which exact subject was produced/repaired by which
   review-candidate context — never provider/session telemetry), and the
   acceptance boundary for a qualifying fresh Reviewer. OR (or direct
   manual execution where it already satisfies independence) performs the
   actual Reviewer launch; where no runtime qualifies, PW emits a precise
   fresh-context handoff requirement (no other user stop).
4. Add lifecycle scenario tests: freshness matrices, contamination
   disqualification, evidence-gated GREEN, bounded repair loops, reopening,
   targeted revalidation, correction routing, and handoff-vs-automatic
   launch.
5. Apply Card/Milestone/final independence rigor to this plan's own
   execution from the start, using current V2 mechanics plus the accepted
   plan controls (separate reviewers, evidence gating, no-prior-opinion
   boundary): every new implementation Card gets independent review, every new milestone
   a separate Milestone review, and — only after M02R plus M03–M07 are
   complete, with historical M01/M02 already terminal — the workstream a
   separate fresh final-integration review
   before Close. The new kernel mechanics are not required to implement
   themselves.

### Acceptance

- Freshness matrices prove producer/repairer contexts cannot verdict their
  subjects at any layer; contaminated contexts are rejected.
- Milestone/final reviewers demonstrably receive no prior verdict
  rationales/opinions by default (information-boundary test).
- GREEN verdicts with missing required evidence are rejected; unrunnable
  required tests without accepted alternates never yield GREEN.
- Repair loops terminate at the configured ceiling with Main
  analysis/escalation records; in-scope defects stay in-Card.
- Reopening, targeted revalidation, and correction routing match
  REQ-072…075 on invalidation fixtures; unaffected GREENs survive.
- Review freshness never creates a user stop when the launch-eligibility
  obligation is satisfiable by an available runtime (OR launch or direct
  compliant execution); the handoff requirement fires exactly when no
  runtime satisfies it.

### Verification strategy

- Lifecycle state-machine tests plus independence/contamination matrices.
- Evidence-gating tests (missing-evidence GREEN rejection, unrunnable-test
  handling, alternate-path acceptance).
- Loop-bound, reopening, revalidation, and routing scenario tests.
- Eligibility-vs-handoff decision tests across runtime capability
  fixtures, asserting PW's obligation verdicts with semantic evidence
  only (no provider/session telemetry in fixtures or canonical state).
- This plan's new execution Card/Milestone reviews serve as live
  conformance evidence during M02R and M03–M07; the workstream final-integration
  review is post-M07 lifecycle evidence, never a prerequisite for M07's
  own GREEN.

### JIT / implementation boundary

Execution Prep may split M05 into contracts, lifecycle, independence/
handoff, and scenario-test Cards. Failure-ceiling values and evidence
packaging details are JIT choices within accepted semantics. Any weakening
of freshness, evidence gating, loop bounds, or routing discipline returns
to Strategic Planning.

## M06 — Runtime behavior and handoff

### Outcome

PW continues automatically across deterministic authorized obligations;
user stops occur only at genuine product/strategy/authorization/input/
blocker boundaries and existing premium gates; runtime choice stays
user-directed and non-canonical. Optional Premium A/C stops expose two
valid alternatives — continue in the present context or use the rendered
fresh-context locator — and the user's deliberate selection of either
offered alternative is the input for that exact gate. A fresh receiver
reconstructs current Git, validates the exact gate subject, and hands the
governed persistence action to the coordinator; the kernel remains
read-only. Once the exact satisfaction write is read back, deterministic
continuation proceeds without a duplicate confirmation. Premium B remains
a distinct mandatory fresh-independent boundary. Model assignment stays
fixed without silent substitution; out-of-scope findings return to PW
authority.

### Requirement coverage

Owns PWV21-REQ-077…PWV21-REQ-091 (15 requirements; per-requirement
verification in Appendix A).

### Planned work

1. Define the stop taxonomy (genuine boundaries + premium gates) and the
   automatic-continuation rule with its re-evaluation loop.
2. Define the locator-only handoff contract and the optional A/C gate-input
   lifecycle: offered stay/fresh alternatives, exact-subject validation,
   canonical reconstruction on the receiver, governed coordinator
   persistence, mandatory readback, then immediate re-routing. The locator
   never becomes authority and carries no runtime/session/model identity.
3. Define idempotent optional-gate recovery rules: an already-satisfied
   exact A/C is consume-only; interrupted/uncertain persistence is read back
   before retry; stale, wrong-cycle, wrong-plan, or otherwise mismatched
   locators cannot satisfy the current gate and route through the existing
   fail-closed/recovery semantics rather than being guessed.
4. Preserve Premium B as mandatory fresh independent review of its exact
   frozen subject; no A/C optional-handoff rule weakens or substitutes B.
5. Define the durable-boundary switching rule, Git-outranks-narrative
   reconstruction procedure, runtime-neutrality and fixed-model-assignment
   boundaries, including explicit approval for exceptional model changes
   and the internal-vs-canonical telemetry split.
6. Define out-of-scope finding classification (in-Card tiny fix vs PW/JIT
   routing vs authority escalation).
7. Add scenario tests covering A-stay, A-fresh, C-stay, C-fresh, interrupted
   persistence/recovery, already-satisfied idempotence, stale/wrong-subject
   locator rejection, B-distinct mandatory freshness, repeated handoff
   round-trips, Git-vs-narrative conflicts, OR outage/session loss, model
   substitution prohibition, and classification routing.

### Acceptance

- No user stop occurs on deterministic authorized routes, helper outages
  with sufficient contracts, or review freshness whose launch-eligibility
  obligation is satisfiable by an available runtime; every stop maps to
  the accepted taxonomy.
- A-stay, A-fresh, C-stay, and C-fresh fixtures each persist satisfaction
  only for the exact current gate subject, perform mandatory readback, and
  continue to the next deterministic obligation without asking the same
  gate question again.
- Fresh-receiver fixtures prove the locator is navigation/input context
  only: current Git is reconstructed first; stale/wrong-cycle/wrong-plan
  subjects cannot satisfy the gate.
- Interrupted-persistence and already-satisfied fixtures are idempotent:
  readback precedes retry, duplicate canonical writes/effects are avoided,
  and exact satisfied gates are consumed rather than re-authorized.
- Premium B fixtures remain mandatory fresh-independent and exact-subject
  bound; optional A/C behavior cannot satisfy or bypass B.
- Handoff fixtures round-trip in both directions repeatedly with Task Board
  semantics preserved; stale-narrative conflicts resolve to current Git.
- Canonical state contains no runtime preference, provider/session/model
  identity, or telemetry; negative vocabulary tests guard the boundary.
- Model substitution without explicit user approval is impossible by
  contract and covered by negative tests.
- Out-of-scope findings route per REQ-090/091 on classification fixtures;
  OR-accepted scope changes are rejected.

### Verification strategy

- Stop-taxonomy decision tests over route/stop matrices.
- Exact-subject optional-gate state-transition matrix covering A/C
  stay/fresh, interrupted write/readback, already-satisfied recovery, and
  stale/wrong-subject rejection.
- B-distinct negative tests proving optional A/C machinery cannot satisfy
  or bypass the mandatory fresh-independent review boundary.
- Handoff round-trip and conflict-resolution scenario tests.
- Outage/loss simulation tests (OR unavailable, session loss with durable
  results present).
- Negative tests: runtime preference, telemetry/identity leakage, silent
  model substitution, OR scope acceptance, duplicate gate confirmation.
- Handoff and gate-input fixtures folded into the M03 parity corpus
  (runtime-switch/premium-gate class).

### JIT / implementation boundary

Execution Prep may split M06 into continuation/stops, optional-gate input,
handoff, neutrality/model assignment, classification, and scenario-test
Cards. Exact event/schema field names and UI wording are JIT choices so
long as the accepted exact-subject, read-only-kernel, coordinator-write,
readback, idempotence, and no-duplicate-confirmation semantics hold. Any
new user stop, canonical runtime signal, weakened B boundary, or
scope-acceptance path returns to Strategic Planning.

## M07 — Recovery, migration, lifecycle continuity, and close

### Outcome

All mechanical ambiguity fails closed to Recovery with safe automatic
continuation where possible; Research/Planning/Definition boundaries route
correctly; PWv2 → PWv2.1 migration is lazy/on-entry with history preserved
and historical GREEN validity intact; workstream close requires GREEN final
integration review plus complete acceptance evidence. User stops state the
durable meaning and smallest next action. After user-supplied input,
including an optional A/C stay-or-fresh selection, the governed exact gate
write/readback is reconciled and deterministic continuation is immediate,
idempotent, and free of duplicate confirmation.

### Requirement coverage

Owns PWV21-REQ-092…PWV21-REQ-107 (16 requirements; per-requirement
verification in Appendix A).

### Planned work

1. Define the fail-closed Recovery taxonomy (ambiguity classes → Recovery
   entry) and the safe-automatic vs user-owned Recovery decision rule.
2. Implement Research/Planning/Definition return routing and the
   technical-equivalent vs product-alternative classification.
3. Implement lazy/on-entry migration: binding validation, uniquely
   derivable field rules, history-preserving normalization, contradiction
   fail-closed, dependent-path-only blocking.
4. Build migration acceptance from real-derived PWv2 workstreams in
   multiple lifecycle states (active Card, review pending, RED/recovery,
   milestone boundary, closed historical).
5. Define close requirements (GREEN final integration review + complete
   acceptance evidence), the user-stop content contract, and the
   post-input re-evaluation loop. For optional A/C, the loop must treat the
   deliberate offered stay/fresh choice as the exact gate input, invoke a
   governed coordinator persistence with preconditions, require readback,
   and continue without a second generic confirmation.
6. Define interrupted/uncertain optional-gate reconciliation: read current
   canonical state before retry, consume already-satisfied exact gates,
   reject stale/wrong-subject locators, and preserve B as a separate
   mandatory fresh-independent boundary.
7. Test the close mechanics with fixtures during M07. M07 has its own
   milestone acceptance and fresh Milestone review; the actual workstream
   final-integration review is post-M07 lifecycle evidence before Close,
   not a prerequisite for M07's own GREEN.

### Acceptance

- Every ambiguity class in REQ-092 fails closed to Recovery on injection
  fixtures; no guess path exists.
- Safe automatic Recovery completes without user input; product/strategy
  alternatives surface to the user exactly once with the smallest next
  action.
- Migration fixtures prove: unambiguous continuation, ambiguous fail-closed,
  historical GREEN preservation, bounded material-only revalidation, no
  retroactive RED, no spurious reopening, history preservation, and
  dependent-path-only blocking.
- Real-derived multi-state migration acceptance is GREEN.
- Final REQ-015 corpus audit proves all high-risk classes are covered after
  M04–M07 folding.
- Stop/input fixtures prove A-stay, A-fresh, C-stay and C-fresh each
  persist/read back the exact current gate then continue without duplicate
  confirmation; interrupted persistence is recovered by readback before
  retry; already-satisfied state is idempotent/consume-only.
- Stale/wrong-cycle/wrong-plan locator fixtures cannot satisfy the current
  gate and fail closed/recover according to current canonical state.
- Premium B remains separately mandatory and fresh-independent for the
  exact frozen plan subject.
- Close mechanics proven on fixtures: close is impossible without GREEN
  final integration review and complete evidence (negative test); user
  stops match the REQ-106 content contract; post-authorization/input
  continuation reaches the next real stop without manual nudging.

### Verification strategy

- Fail-closed injection tests across all REQ-092 ambiguity classes.
- Recovery routing/classification scenario tests (automatic vs user-owned,
  technical-equivalent vs product-alternative, Research return targets).
- Migration rehearsal suite over real-derived multi-state workstreams.
- Optional-gate recovery matrix: interrupted write/readback, exact
  already-satisfied state, stale/wrong-subject locators, and no-duplicate
  confirmation after valid A/C input.
- Close-gate negative tests, stop-content/input contract tests, and
  post-input continuation tests.
- M07's own milestone acceptance plus its fresh Milestone review; the
  workstream final-integration review follows post-M07 as lifecycle
  evidence before Close.

### JIT / implementation boundary

Execution Prep may split M07 into Recovery routing, migration, optional-gate
reconciliation, acceptance rehearsal, and close/stop Cards. Rehearsal
workstream selection, exact event/schema names, and stop wording are JIT
choices. Any new guess path, duplicate authorization loop, retroactive RED,
spurious reopening, weakened B boundary, or close-gate weakening returns to
Strategic Planning.

## ADR coverage

| ADR | Subject | Owning milestones |
|---|---|---|
| ADR-PWV21-001 | Small stateless kernel with helper-less parity | M01 (kernel/registry), M03 (parity/procedure) |
| ADR-PWV21-002 | PW-owned obligation/result authority; OR runtime realization | M02 (contracts/authority), M06 (model assignment, telemetry split) |
| ADR-PWV21-003 | Plan-authorized parallel Cards; one mutating Worker | M04 |
| ADR-PWV21-004 | Layered fresh independent review | M05 |
| ADR-PWV21-005 | Git-first handoff, recovery, migration; fail-closed | M03 (procedure/parity), M06 (handoff), M07 (recovery/migration/close) |

## Cross-cutting constraint reconciliation

These accepted constraints span milestones; each names its enforcement
owner so no milestone can silently weaken another:

- Telemetry exclusion (REQ-027): enforced by M02 schema/vocabulary tests;
  M04 (worker ownership) and M06 (progress/telemetry split) must pass the
  same negative vocabulary test; new telemetry-shaped fields anywhere fail
  M07 acceptance.
- No Python-only predicates (REQ-008) and drift fail-closed (REQ-009):
  enforced by M01 tests; every later milestone adding kernel predicates
  extends the same registry/coverage/drift suite (verified at M03 parity
  and M07).
- Helper-less admissibility (REQ-016): enforced by the M03 admission
  checklist as a milestone entry/exit check for M04–M07.
- Route taxonomy (REQ-038/039/092 + staleness). Three distinct outcomes,
  never conflated: (a) overlapping mutating scopes or insufficient
  independence proof route valid Cards *serially* (REQ-038/039; denial of
  parallel authorization only); (b) stale/conflicted results first
  revalidate, reconcile, or prove safe reuse, re-executing only when reuse
  cannot be proven safe (REQ-028/029/051); (c) contradictory
  authority/state, unresolved mechanical parity ambiguity (kernel/docs,
  registry/code, helper/independent-context disagreement), and other
  unresolvable mechanical ambiguity fail closed to *Recovery* (REQ-092).
  The M07 taxonomy enforces (c) together with durable binding conflicts
  such as contradictory already-durable multiple-active-set membership;
  M02/M04 enforce (a)–(b) into their own routes, entering Recovery only
  when reconciliation itself is contradictory or unresolvable.
- No deferred GREEN (REQ-069): enforced by M05 verdict validity; M07 close
  re-checks it; unrunnable required tests anywhere need accepted alternate
  verification recorded before GREEN.
- Runtime neutrality (REQ-080) and fixed model assignment (REQ-087/088):
  enforced by M06 negative tests; M02/M04/M05 fixtures must pass them.
- Compatibility-before-consumption (REQ-053/054): enforced by M04; M05
  Milestone review treats missing compatibility evidence as incomplete
  evidence under REQ-069.
- Bounded correction routing (REQ-070/071/074/075): enforced by M05; M07
  Recovery reuses the same routing (no second correction taxonomy).
- PW/OR realization boundary: PW specifies typed semantic obligations,
  eligibility, evidence, and acceptance (M04 ownership, M05 independence);
  OR owns assignment, launch, replacement, archive, model/session choice,
  concurrency, and isolation. No PW scheduler, runtime topology, or
  canonical runtime IDs; review eligibility evidence is subject-relative
  semantics, never leaked provider/session telemetry. Direct/manual
  compliant execution remains legal wherever it satisfies the obligation.
- Optional Premium A/C handoff-input semantics (REQ-004/031/077/081/082/
  106/107): M06 owns the offered stay/fresh alternatives, exact-subject
  handoff/reconstruction semantics, and state-transition scenarios; M07 owns
  durable post-input reconciliation/continuation and stop-content behavior.
  The kernel stays read-only, coordinator writes are preconditioned and
  read back, exact already-satisfied gates are idempotent/consume-only, and
  stale/wrong-subject locators never authorize current gates. Premium B is
  unchanged and remains a separate mandatory fresh-independent boundary.
- History preservation and no retroactive RED (REQ-098/099/101): enforced
  by M07 migration tests; no earlier milestone may rewrite historical
  state to satisfy a new check.

## Verification strategy (plan-level)

Risk-based, heaviest on fail-closed boundaries, parity, review integrity,
and migration:

1. Contract and unit tests own deterministic mechanics (registry, kernel,
   schemas, validation, lifecycle state machines).
2. Scenario and matrix fixtures own semantic boundaries (propagation,
   freshness, routing, classification, handoff round-trips).
3. The M03 independent-context parity protocol + fixture corpus is the
   shared acceptance backbone; M04–M06 fold their fixtures into it; M07
   migration states extend it.
4. Destructive recovery (REQ-017) and real-derived migration rehearsal
   (REQ-103) are standalone acceptance gates, not subsumed by unit tests.
5. Negative tests guard every prohibition (DSL, Python-only predicates,
   telemetry, override hatch, duplicate mutators, recursive spawns,
   runtime preference, silent model switch, OR scope acceptance,
   guess paths, deferred GREEN, premature close).
6. V2 baseline regression stays GREEN throughout; each milestone re-runs
   the baseline suite plus all prior milestone suites.
7. This plan's own execution demonstrates the lifecycle in order:
   independent Card review and separate Milestone reviews during M02R and M03–M07,
   then a separate fresh final-integration review with complete evidence
   before close.

## Transition strategy

- Lazy/on-entry migration only (REQ-096): existing PWv2 workstreams adopt
  PWv2.1 at natural durable boundaries; no flag day.
- Unambiguous work continues after binding validation; ambiguous state
  fails closed to Recovery with the smallest next action (REQ-097/102).
- Historical GREEN results and correctly closed stages are never
  retroactively invalidated; bounded material-only revalidation/backfill
  applies where new evidence is material to active continuation
  (REQ-098/099/125).
- M01/M02 remain terminal. P3 does not reopen them. M02 is additionally
  replayed as immutable regression evidence by M02R.
- The existing waiting `after-M02-T01` JIT state must be reconciled after
  P3 approval: it must not materialize M03 directly. Execution Prep first
  materializes M02R under its three required seams; only after M02R terminal
  GREEN may the downstream M03 trigger be created/satisfied/consumed.
- Migration preserves history, normalizes minimally, adapts valid
  old-format results, and blocks only dependent paths (REQ-100/101/104).
- Workstream close under PWv2.1 requires the full new acceptance surface
  (REQ-105); in-flight work crossing the migration boundary receives new
  review semantics for its active stages only.

## Risk register

| ID | Risk | Likelihood / Impact | Mitigation (owner) |
|---|---|---|---|
| R-01 | Kernel scope creep into orchestration/DSL | Medium / High | Fixed predicate vocabulary + allowlist (M01); admission checklist (M03); plan-review gate on new predicates |
| R-02 | Python-only predicates breaking helper-less recovery | Medium / High | Contract-coverage test from registry (M01); REQ-016 admission (M03); destructive test (M03) |
| R-03 | Parity drift between helper and helper-less routing | Medium / High | Independent-context parity with locked verdicts + disagreement injection (M03); fixture folding from M04–M06 |
| R-04 | Stale-result mishandling under parallelism | Medium / High | Fingerprint revalidation + reconciliation scenarios (M02); sibling-staleness fixtures (M04) |
| R-05 | Write-scope overlap escaping validation | Low / Critical | Overlap matrix tests + no-override negative test over full option surface (M04) |
| R-06 | Review independence erosion (contamination, opinion leakage) | Medium / High | Freshness/contamination matrices + information-boundary tests (M05) |
| R-07 | Review cost/latency resistance weakening gates | Medium / Medium | Loop bounds + launch-eligibility obligation with OR/direct realization (M05); no-deferred-GREEN enforcement (M05/M07); accepted cost recorded in ADR-004 |
| R-08 | Ambiguous legacy migration state guessed instead of fail-closed | Medium / High | Contradiction fail-closed tests + real-derived rehearsal (M07) |
| R-09 | Telemetry/model identity leaking into canonical state | Low / High | Negative vocabulary tests (M02/M06); cross-milestone re-check (M07) |
| R-10 | Serialization/naming choices leaking into authority semantics | Low / Medium | REQ-010 invariance boundary reviewed at plan review and enforced at Execution Prep |
| R-11 | Milestone coupling causing cascade rework (M02↔M04 staleness) | Medium / Medium | Staleness contract finalized in M02 acceptance before M04 starts; M04 consumes, never redefines |
| R-12 | Optional A/C fresh handoff loops on a second confirmation or accepts a stale locator | Medium / High | Exact-subject gate-input matrix, governed write+readback, idempotent recovery, stale/wrong-subject rejection, and B-distinct negative tests in M06/M07 |
| R-13 | Execution Prep collapses planner seams into another mega-Card | Medium / High | M02R seam classes + decomposition audit + risk-based topology challenge; M02 regression replay |
| R-14 | Repeated fresh review degenerates into unbounded serial defect discovery | Medium / High | Exhaustive pass + class repair + stable epoch + 5/4/3 ceilings + convergence mode switch |
| R-15 | Live finding mutates active history or tracker text becomes authority | Low / High | Classification + affected-downstream reconciliation + tracker non-authority + immutable historical replay |
| R-16 | M03 is falsely presented as deployed PWv2.1 dogfood while consumer authority is still main | Medium / Medium | Explicit authority-level dogfood + candidate shadow/replay distinction; deployed consumer validation deferred to post-release Paseo/Pi |

## Scope exclusions (planning-level)

Beyond the Definition non-goals, this plan explicitly excludes:

- Implementation Task Board/Card authoring (Execution Prep, after premium C).
- Exact serialization, naming, and module-layout choices (REQ-010 option
  space; JIT within the invariance boundary).
- OR/Paseo internals: schedulers, worktrees, retry policies, provider
  integrations, telemetry pipelines, progress UI.
- ChatGPT harness internals beyond the portable contracts and handoff format.
- V1 migration (out of scope; only PWv2 → PWv2.1 lazy migration is planned).
- Performance optimization beyond correctness; performance targets, if any,
  are a later Definition concern, not inferred here.

## Gates and escalation

- Plan freeze, premium B, Stage-6 independent Plan Review, approval, and
  premium C follow the normal V2 sequence; freezing requires Main
  strategy acceptance first (mutable lifecycle owned by PLANNING.toml).
- At optional Premium A/C stops, either offered user choice (stay in the
  present context or take the fresh-context locator) supplies the exact
  gate input. The coordinator validates the current subject, persists the
  exact satisfaction, requires readback, and immediately re-routes; a
  second generic confirmation is forbidden. Already-satisfied exact gates
  are consume-only; stale/wrong-cycle/wrong-plan locators cannot satisfy
  the current gate. Premium B is not optional and remains a mandatory
  fresh-independent exact-subject boundary.
- Each new milestone, including M02R and M03–M07, closes only on its
  acceptance section GREEN plus its own separate Milestone review. From-the-start
  Card/Milestone/final independence requirements apply to this
  implementation using current V2 mechanics plus the accepted plan
  controls (separate reviewers, evidence gating, no-prior-opinion
  boundary); there is no weaker gate for current implementation
  milestones. Existing correctly closed historical stages still retain
  REQ-099 protection (valid closed reviews stay valid; new semantics
  apply to active stages only).
- Only after M02R and M03–M07 are complete, with historical M01/M02 already
  terminal, does the separate fresh workstream final-integration review occur; workstream close then requires that
  review GREEN with complete evidence.
- Escalation paths: JIT/Execution Prep detail → Execution Prep; milestone
  strategy/order/outcome change → Strategic Planning (new cycle, new A/B/C
  if material); accepted product/global intent change → Project Definition;
  missing facts → Research. Unstructured global repair is forbidden.

## Appendix A — Auditable requirement coverage inventory

Every accepted requirement ID appears exactly once, with its owning
milestone and verification method. Totals: M01: 10, M02: 16, M02R: 20,
M03: 7, M04: 22, M05: 21, M06: 15, M07: 16 — 127/127 mapped,
0 unmapped, 0 double-mapped.

| Requirement | Owner | Verification |
|---|---|---|
| PWV21-REQ-001 | M01 | Predicate-allowlist trace test: each predicate maps to canonical state inputs |
| PWV21-REQ-002 | M01 | Negative test: kernel rejects semantic inputs; role-ownership docs review |
| PWV21-REQ-003 | M01 | Purity/repeatability test; no-write assertion over canonical paths |
| PWV21-REQ-004 | M01 | Read-only test: routes/validations only; writes observed solely via coordinator/role fixtures |
| PWV21-REQ-005 | M01 | Registry schema/version/loader tests; metadata completeness test |
| PWV21-REQ-006 | M01 | Negative vocabulary test: arbitrary-expression entries rejected |
| PWV21-REQ-007 | M01 | Projection freshness test: regenerated output matches checked-in projection |
| PWV21-REQ-008 | M01 | Contract-coverage test enumerating registry predicates against contract sections |
| PWV21-REQ-009 | M01 | Drift tests with injected registry/impl/contract disagreement asserting fail-closed |
| PWV21-REQ-010 | M01 | Invariance-boundary review: option space recorded; authority/semantics leak check |
| PWV21-REQ-011 | M03 | Independent fresh-context derivation from Git+contracts alone over corpus; verdict+evidence locked before comparison |
| PWV21-REQ-012 | M03 | Independent-context derivation passes all legal-continuation fixtures without helper |
| PWV21-REQ-013 | M03 | Outage simulation: no user stop when contracts suffice |
| PWV21-REQ-014 | M03 | Independent-context vs reference agreement over corpus; disagreement is a parity defect failing closed; injection tests |
| PWV21-REQ-015 | M03 | Corpus coverage audit: each high-risk class present with RED/boundary/stale variants |
| PWV21-REQ-016 | M03 | Admission checklist applied retroactively (M01/M02) and at each later milestone entry |
| PWV21-REQ-017 | M03 | Standalone destructive acceptance on isolated disposable surface: fresh context, verdict locked pre-comparison, raw evidence; unavailable acceptance fails visibly |
| PWV21-REQ-018 | M02 | Schema validation + version matrix + golden JSON fixtures |
| PWV21-REQ-019 | M02 | Obligation binding completeness test over required fields |
| PWV21-REQ-020 | M02 | Authority resolution tests: exact ref/hash validation, bundle minimality |
| PWV21-REQ-021 | M02 | Negative test: authority-altering transport payloads rejected |
| PWV21-REQ-022 | M02 | Negative test: summary-only authority bundles rejected |
| PWV21-REQ-023 | M02 | Derivation test: obligations rebuild identically from canonical state; no canonical reads from stored obligations |
| PWV21-REQ-024 | M02 | Determinism test: identical inputs yield identical obligation_id |
| PWV21-REQ-025 | M02 | Fingerprint minimality test: unrelated-file perturbation leaves fingerprints unchanged |
| PWV21-REQ-026 | M02 | Result schema/content test: only PW-relevant semantic fields accepted |
| PWV21-REQ-027 | M02 | Negative vocabulary test: telemetry fields absent from schemas, fixtures, canonical state |
| PWV21-REQ-028 | M02 | Stale-result classification tests: revalidation before acceptance; blind acceptance impossible |
| PWV21-REQ-029 | M02 | Reuse/rebase/reconcile vs re-execute scenario tests with safety-proof assertions |
| PWV21-REQ-030 | M02 | Breaking-version rejection tests: typed fail-closed errors, no partial application |
| PWV21-REQ-031 | M02 | Mutation handoff tests: pre/postconditions emitted, governed write, readback evidence required |
| PWV21-REQ-032 | M02 | Negative test: direct canonical mutation from Card execution path rejected |
| PWV21-REQ-033 | M02 | Unknown-effect fixtures: retry blocked until readback/reconciliation |
| PWV21-REQ-034 | M04 | Negative test: undeclared Card pairs never concurrent |
| PWV21-REQ-035 | M04 | Negative test: absent-dependency pairs without declaration never concurrent |
| PWV21-REQ-036 | M04 | Validation unit tests: dependencies, scopes, effect domains, overlap |
| PWV21-REQ-037 | M04 | Scope-expression tests: paths/globs + named resources/domains; free-text-only rejected |
| PWV21-REQ-038 | M04 | Negative test over full option surface: no overlapping-mutation concurrency path |
| PWV21-REQ-039 | M04 | Uncertainty fixtures collapse to serial route |
| PWV21-REQ-040 | M04 | Membership tests: Plan/JIT ownership; proposed multi-set denied to serial, durable multi-set conflict fails closed to Recovery |
| PWV21-REQ-041 | M04 | Subset-start scenario tests with prerequisite gating |
| PWV21-REQ-042 | M04 | Dependency-matrix propagation fixtures: self+successors stop, independents continue |
| PWV21-REQ-043 | M04 | Boundary test: legality decided before scheduling fixtures vary; scheduling variance never changes legality |
| PWV21-REQ-044 | M04 | Per-Card artifact separation test: obligation/result/review/evidence per Card |
| PWV21-REQ-045 | M04 | Ownership test: single mutating Worker; parallel mutation requires separate Cards |
| PWV21-REQ-046 | M04 | Helper-bound test: advisory helpers perform no mutation (write-attempt detection) |
| PWV21-REQ-047 | M04 | Negative test: worker-spawned subagents rejected; sibling-helper path exercised |
| PWV21-REQ-048 | M04 | PW acceptance over lifecycle evidence: fresh-assignment eligibility, repair persistence, close on terminal |
| PWV21-REQ-049 | M04 | PW acceptance of replacement evidence: scope/authority unchanged, Card identity/authority preserved |
| PWV21-REQ-050 | M04 | Negative test: duplicate mutating Workers rejected; advisory-lane fixtures pass |
| PWV21-REQ-051 | M04 | Sibling-invalidation fixtures: stale/conflicted classification before integration |
| PWV21-REQ-052 | M04 | Preservation fixtures: unaffected valid results survive sibling block/RED |
| PWV21-REQ-053 | M04 | Gate test: combined consumption impossible without compatibility obligation |
| PWV21-REQ-054 | M04 | Substitution test: compatibility evidence rejected as Card-review substitute; bounded-correction preservation fixtures |
| PWV21-REQ-055 | M04 | Workstream-independence fixtures: blockers do not cross workstreams |
| PWV21-REQ-056 | M05 | Lifecycle test: Card without independent review cannot complete |
| PWV21-REQ-057 | M05 | Lifecycle test: Milestone without separate review cannot complete |
| PWV21-REQ-058 | M05 | Lifecycle test: workstream without fresh final-integration review cannot close |
| PWV21-REQ-059 | M05 | Independence matrix: producer/repairer contexts cannot verdict their subjects |
| PWV21-REQ-060 | M05 | Eligibility test: fresh Reviewer distinct from other Cards; semantic evidence only |
| PWV21-REQ-061 | M05 | Recheck fixtures: same Reviewer rechecks Worker repairs it did not make |
| PWV21-REQ-062 | M05 | Repair-disqualification fixtures: Reviewer repair forces fresh Reviewer |
| PWV21-REQ-063 | M05 | Milestone freshness fixtures: constituent implementers/reviewers excluded |
| PWV21-REQ-064 | M05 | Information-boundary test: subject+authority+outputs+evidence present, prior rationales absent |
| PWV21-REQ-065 | M05 | Milestone recheck fixtures: allowed only without Reviewer repair |
| PWV21-REQ-066 | M05 | Final-review freshness fixtures: judged from authority/raw evidence, prior GREENs excluded |
| PWV21-REQ-067 | M05 | Contamination fixtures: transcript-contaminated Reviewers rejected |
| PWV21-REQ-068 | M05 | Negative test: self-test evidence rejected as formal review |
| PWV21-REQ-069 | M05 | Evidence-gating tests: incomplete-evidence GREEN rejected; unrunnable-test alternate-path rules |
| PWV21-REQ-070 | M05 | Repair-loop fixtures: in-scope RED stays in-Card with automatic repair/re-review |
| PWV21-REQ-071 | M05 | Ceiling fixtures: loops terminate with Main analysis; escalation only for real user-owned blockers |
| PWV21-REQ-072 | M05 | Reopening fixtures: fresh Worker + fresh Reviewer eligibility satisfied |
| PWV21-REQ-073 | M05 | Invalidation fixtures: affected surface revalidated, unaffected work preserved |
| PWV21-REQ-074 | M05 | Correction-routing fixtures: identified/bounded Cards only, no global repair |
| PWV21-REQ-075 | M05 | Final-RED fixtures: automatic bounded correction; earlier GREENs survive absent reaching evidence |
| PWV21-REQ-076 | M05 | Eligibility-vs-handoff decision tests across runtime capability fixtures; semantic evidence only |
| PWV21-REQ-077 | M06 | Stop-taxonomy + optional-gate transition tests: after exact A/C input/readback, deterministic continuation occurs without a duplicate stop |
| PWV21-REQ-078 | M06 | Resolution-path tests: tool/readback/Research preferred over user delegation |
| PWV21-REQ-079 | M06 | Progress-level review: user-facing output is Card/workstream-level; worker UI absent from PW |
| PWV21-REQ-080 | M06 | Negative test: canonical state contains no runtime preference |
| PWV21-REQ-081 | M06 | Locator-only handoff tests: A/C fresh selection is exact gate input while payload stays locator-only and runtime-neutral |
| PWV21-REQ-082 | M06 | Receiver/conflict fixtures: current Git and exact gate subject outrank locator narrative; stale/wrong-subject handoff cannot authorize and valid input continues deterministically |
| PWV21-REQ-083 | M06 | Switching fixtures: durable-boundary preference; minimal resumable state persisted on early switch |
| PWV21-REQ-084 | M06 | Repeated round-trip fixtures preserving Task Board semantics |
| PWV21-REQ-085 | M06 | Outage fixtures: ChatGPT-legal obligations continue without OR |
| PWV21-REQ-086 | M06 | Session-loss fixtures: Git recovery preferred; durable results reused before replay |
| PWV21-REQ-087 | M06 | Negative test: silent model fallback/escalation rejected |
| PWV21-REQ-088 | M06 | Approval-path test: exceptional model change requires explicit user approval |
| PWV21-REQ-089 | M06 | Boundary test: retry/session signals never surface as PW semantics |
| PWV21-REQ-090 | M06 | Classification fixtures: out-of-Card proposals route to PW authority; OR acceptance rejected |
| PWV21-REQ-091 | M06 | Classification fixtures: tiny in-scope fixes stay; out-of-scope routes to PW/JIT |
| PWV21-REQ-092 | M07 | Ambiguity-injection tests: every class fails closed to Recovery |
| PWV21-REQ-093 | M07 | Automatic-Recovery fixtures: completion without user input; surfacing without stop |
| PWV21-REQ-094 | M07 | Classification fixtures: accepted-plan following vs technical-equivalent vs user-owned alternative |
| PWV21-REQ-095 | M07 | Research-return routing fixtures: Planning vs Definition/Brainstorming boundary |
| PWV21-REQ-096 | M07 | Migration-mode test: lazy/on-entry only; no flag-day path exists |
| PWV21-REQ-097 | M07 | Continuation fixtures: unambiguous validated continuation; ambiguous fail-closed |
| PWV21-REQ-098 | M07 | Preservation fixtures: historical GREEN valid; bounded material-only revalidation; no retroactive RED |
| PWV21-REQ-099 | M07 | Stage-preservation fixtures: no spurious reopening; material-only Milestone backfill |
| PWV21-REQ-100 | M07 | Field-addition fixtures: uniquely derivable added; interpretation-gated routed to Recovery/user gate |
| PWV21-REQ-101 | M07 | History-preservation + normalization-minimality + old-format adaptation fixtures |
| PWV21-REQ-102 | M07 | Contradiction fixtures fail closed; safe migration creates no user stop |
| PWV21-REQ-103 | M07 | Real-derived multi-state migration rehearsal suite GREEN |
| PWV21-REQ-104 | M07 | Blocking-scope fixtures: only dependent paths block |
| PWV21-REQ-105 | M07 | Close-gate negative tests: close impossible without GREEN final review + complete evidence |
| PWV21-REQ-106 | M07 | Stop/input contract tests: durable meaning + smallest action + A/C offered choice semantics + locator handoff; no second generic confirmation |
| PWV21-REQ-107 | M07 | Post-input continuation tests: governed exact gate write/readback, interrupted/already-satisfied recovery, then deterministic continuation to the next real stop |
| PWV21-REQ-108 | M02R | Lifecycle fixture: bounded finding verification cannot satisfy required fresh full-scope review |
| PWV21-REQ-109 | M02R | Exhaustive-review fixture: first blocker does not terminate pass; complete material finding set frozen |
| PWV21-REQ-110 | M02R | Repair-class fixture: root cause + sibling/negative-space generalized regression required |
| PWV21-REQ-111 | M02R | Epoch fixtures: ordinary repair preserves epoch; accepted authority redesign records explicit reset |
| PWV21-REQ-112 | M02R | Ceiling matrix: Card=5, Milestone=4, final=3; verification attempts excluded |
| PWV21-REQ-113 | M02R | Ceiling route fixture: hard ceiling enters convergence analysis and never accepts RED |
| PWV21-REQ-114 | M02R | Post-convergence RED fixture routes to structural classification, not ordinary review N+1 |
| PWV21-REQ-115 | M02R | Seam-schema/contract tests for required/preferred/illustrative without speculative Card IDs |
| PWV21-REQ-116 | M02R | Negative test: required-seam merge rejected and routed to Planning |
| PWV21-REQ-117 | M02R | Preferred-seam deviation fixtures require qualifying durable technical rationale |
| PWV21-REQ-118 | M02R | Decomposition-quality audit fixtures cover implementability/falsifiability/reviewability/coupling/atomicity |
| PWV21-REQ-119 | M02R | Risky topology fixtures require fresh independent topology challenge before launch |
| PWV21-REQ-120 | M02R | Trivial topology fixture proves no mandatory fresh topology review; challenge remains narrower than Plan Review |
| PWV21-REQ-121 | M02R | Layering fixture rejects Card topology that collapses local Card Review into Milestone integration scope |
| PWV21-REQ-122 | M02R | Classification fixtures distinguish five live-finding classes before authority mutation |
| PWV21-REQ-123 | M02R | Downstream gate fixtures block only findings explicitly classified as material to affected JIT |
| PWV21-REQ-124 | M02R | Negative tests prove tracker issue/comment cannot authorize scope/repair/epoch reset |
| PWV21-REQ-125 | M02R | Historical-state preservation fixture: terminal M02 remains unchanged under new semantics |
| PWV21-REQ-126 | M02R | M02-derived regression corpus covers mega-Card, review completeness, class repair and convergence |
| PWV21-REQ-127 | M02R | Downstream dogfood fixture requires corrected authority/gates and forbids special prompt substitution |

## Planning audit (planner's summary)

Full P3 audit evidence:
`implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/PLANNING_AUDIT_P3_2026-09-24.md`.

- Definition R2 is GREEN with 127 accepted requirements and 7 accepted ADRs.
- Premium A for `definition:R2|planning-cycle:3` was satisfied before
  material P3 planning.
- M01/M02 remain terminal and are not rematerialized.
- P3 adds one bounded bootstrap milestone M02R with 3 required seams and
  unique ownership of REQ-108…127.
- Original M03–M07 semantic outcomes remain in order; M03 gains explicit
  seam classifications and dogfood/shadow acceptance.
- Requirement inventory is 127/127 unique, 0 missing, 0 duplicate.
- M03 cannot materialize before M02R terminal GREEN.
- The plan explicitly distinguishes authority-level dogfood from deployed
  workflow enforcement while `project_workflow_v2@main` remains canonical.
- Planner completeness/challenge audit: GREEN. Independent Stage-6 Plan
  Review remains pending and must occur only after Premium B in a fresh
  independent context.
