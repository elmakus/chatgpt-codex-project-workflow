# Master Plan — PWv2.1 Policy Kernel

Plan revision: P7
Planning cycle: 7 (entry subject `definition:R3|planning-cycle:7`)
Lifecycle: owned by `PLANNING.toml`; this P7 text becomes the immutable review subject only after the planner audit is GREEN and the exact Git blob is frozen.
Review requirement: REQUIRED independent Stage-6 Plan Review (review_mode `independent`)
Workstream: `change-pwv21-policy-kernel-brainstorming`
Predecessor: cycle 6 / P6 exact GREEN-reviewed frozen subject `elmakus/chatgpt-codex-project-workflow@d4c9c7d4ef23cbce4a5aabc045e75fa3dfbbe0be:planning/PWV21_POLICY_KERNEL_MASTER_PLAN_P6.md@63a85b19a7589e2cdd49ed1be2053925867f3202`.
Replan authority/derivation: Definition R3 (`pwv21-policy-kernel@3`), independently GREEN-reviewed pre-M03 applicability checkpoint `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/PRE_M03_AUDIT_RECONCILIATION_CHECKPOINT.md@1b52d018c3306c7e45d7f38f01a186ee949866cc`, independent review `PRE_M03_AUDIT_RECONCILIATION_REVIEW_R01_2026-09-25.md`, and explicit authorization `PRE_M03_REPLAN_AUTHORIZATION_2026-09-25.md`.
P7 preserves correctly terminal M01, M02 and M02R history and the accepted P6 downstream strategy, but inserts one mandatory pre-M03 corrective milestone, `M02Q`, that owns all 17 unresolved repair families RF001…RF017 under `QUALITY_FIRST_PRE_M03`. No M03 materialization is permitted until M02Q reaches terminal GREEN.

## Authority

- Requirements: `requirements/PWV21_POLICY_KERNEL.md` R3 (status `approved`, Definition subject `pwv21-policy-kernel@3`, 137 accepted requirements PWV21-REQ-001…PWV21-REQ-137).
- Decisions (all status `accepted`): ADR-PWV21-001…ADR-PWV21-008 under `decisions/` as listed by `WORKSTREAM.toml`.
- Definition record: `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/DEFINITION.toml` (R3, GREEN).
- Planning record: `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/PLANNING.toml` (cycle 7 / P7; mutable lifecycle owner).
- Pre-M03 correction basis: checkpoint + four probe reports on exact candidate `elmakus/project_workflow_v2@07c724085de591c2a0bb51aaaae0ec23009880bf`; the candidate branch still resolves to that exact SHA at P7 planning time.
- Historical P6 Plan Review: GREEN R01; P7 does not invalidate P6, but the later quality-first checkpoint created new material planning authority before M03.

Authority input blobs remain unchanged from P6:

| Input | Path | Blob |
|---|---|---|
| Requirements R3 | `requirements/PWV21_POLICY_KERNEL.md` | `6f85eb367e4497b2c43d1075db15daece40cfd81` |
| ADR-PWV21-001 | `decisions/ADR_PWV21_POLICY_KERNEL.md` | `0662b970d80e8b76df79e4dbd458d190ce6d4402` |
| ADR-PWV21-002 | `decisions/ADR_PWV21_ORCHESTRATION_CONTRACT.md` | `051f8fc3f68773349a1fcad39fcf1c60d3157532` |
| ADR-PWV21-003 | `decisions/ADR_PWV21_PARALLEL_CARDS.md` | `437388345d7136cdcdf241bf3ca6aa1016ddb1c0` |
| ADR-PWV21-004 | `decisions/ADR_PWV21_REVIEW_LIFECYCLE.md` | `e5f578d08a4aaf0b14fec33cd7133074887c6ba8` |
| ADR-PWV21-005 | `decisions/ADR_PWV21_RECOVERY_MIGRATION_HANDOFF.md` | `fbaaaedac492ff9e2dbf4db9f8e86b3376df2023` |
| ADR-PWV21-006 | `decisions/ADR_PWV21_DECOMPOSITION_FIDELITY.md` | `615a442671f55a66ecc849f2a5385d298eb62eb0` |
| ADR-PWV21-007 | `decisions/ADR_PWV21_LIVE_VALIDATION.md` | `6adbbef4a40f6005ec09e1a3f73289e256f44b12` |
| ADR-PWV21-008 | `decisions/ADR_PWV21_EXECUTION_DISCIPLINE.md` | `3a6d8324a26bdca17ed294e5398c242815d7862c` |

This plan creates no implementation authority until normal P7 gates complete: planner audit GREEN, immutable freeze, Premium B, independent Plan Review GREEN, approval consumption and Premium C.

## Goal

Evolve the existing Project Workflow V2 implementation conservatively into PWv2.1 while first reconciling every independently verified pre-M03 workflow defect family. Deterministic mechanics remain in a small stateless policy kernel; semantic reasoning remains role/LLM-owned; Git/repository state remains canonical; runtime choice remains non-authoritative.

## Non-goals (from accepted Definition)

- No general workflow programming language or arbitrary-expression DSL.
- No semantic product/strategy/review judgment moved into deterministic policy code.
- No runtime/session/worker/model/telemetry state made canonical.
- No reopening of correctly terminal M01/M02/M02R merely to rewrite history.
- No M03 dogfood before the 17-family quality-first corrective gate is complete.
- No implementation-time invention of missing authority: P7 establishes the previously absent proof/package mechanisms at Planning level only where R3 and canonical V2 semantics already determine the invariant.

## Strategy overview

P7 inserts one bounded corrective milestone between terminal M02R and unmaterialized M03:

```
M01 ──► M02 ──► M02R ──► M02Q ──► M03 ──► M04 ──► M05 ──► M06 ──► M07
 done    done    done
```

`M02Q` is not a rewrite of earlier terminal milestones. It is a forward corrective gate over the exact current candidate and the 17 independently reconciled repair families. Every RF family is a Planning-level `required_seam`; Execution Prep may split a family further when semantic right-sizing requires it but MUST NOT merge two RF seams merely for convenience.

| Milestone | Serial gate | Semantic prerequisites | Rationale |
|---|---|---|---|
| M01 Policy kernel core | — | — | Historical terminal milestone; preserved |
| M02 Obligation/Result contracts | M01 | M01 | Historical terminal milestone; preserved |
| M02R R2+R3 workflow-semantic bootstrap | M02 | Definition R3 | Historical terminal milestone at Board rev104; preserved |
| M02Q Pre-M03 quality reconciliation | M02R | GREEN-reviewed checkpoint + explicit replan authorization + P7 gates | Owns RF001…RF017 and makes the current candidate safe enough to become the basis of M03 dogfood |
| M03 Portability and parity | M02Q | terminal M02Q evidence | First downstream authority-level dogfood after quality reconciliation |
| M04 Parallel Cards | M03 | M03 | Parallel legality and ownership over corrected foundations |
| M05 Review lifecycle integration | M04 | corrected M02Q review foundations + M04 subjects | Integrates full lifecycle without reintroducing the audited defects |
| M06 Runtime behavior and handoff | M05 | corrected routing/freshness/delivery foundations | Runtime-neutral continuation/handoff |
| M07 Recovery, migration and close | M06 | corrected provenance/package/close foundations | Final recovery/migration/close integration |

### Bootstrap/dogfood boundary

- Canonical governance remains current `elmakus/project_workflow_v2@main`; the PWv2.1 candidate remains an implementation/shadow target until normal integration/release.
- Exact audited candidate for M02Q is `elmakus/project_workflow_v2@07c724085de591c2a0bb51aaaae0ec23009880bf`.
- M02Q is implemented under current canonical V2 governance and must preserve source findings/probes as regression evidence.
- M03 is still the first downstream authority-level dogfood, but only after M02Q terminal GREEN; no prompt or manual waiver may substitute for M02Q.
- Historical M01/M02/M02R remain terminal under REQ-125.

## Implementation target and contribution boundary

All M02Q outputs are extensions to the executable V2 baseline in `elmakus/project_workflow_v2` (contracts, executable code and tests). P7 authorizes the corrective semantics and ownership, not a direct cross-repository mutation mechanism. Exact contribution branch/PR mechanics remain bounded Execution Prep choices after Premium C.

## Verified baseline-to-change map

Current corrective baseline: `elmakus/project_workflow_v2@work/pwv21-policy-kernel` = `07c724085de591c2a0bb51aaaae0ec23009880bf`.

| Milestone | Observed baseline seams extended | Preserved |
|---|---|---|
| M01 | existing policy kernel/state-contract/router registry | terminal result; no reopen |
| M02 | execution obligation/result contracts | terminal result; no reopen |
| M02R | review/decomposition/live-validation/Worker semantics | terminal result; immutable regression evidence |
| M02Q | router/state/review/execution/close/delivery seams named by RF001…RF017 | accepted R3 intent, canonical Git authority, subject-relative review, helper-less recoverability, YAGNI |
| M03 | parity/recovery corpus | now consumes terminal M02Q corrective evidence |
| M04–M07 | downstream feature/integration milestones | consume M02Q foundations and must not duplicate or weaken them |

## M01 — Policy kernel core and mechanical truth

**P7 lifecycle note:** historical terminal milestone. P7 does not reopen or
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

**P7 lifecycle note:** historical terminal milestone. M02 has terminal fresh
Card GREEN and fresh Milestone GREEN on the corrected exact subject. P4 does
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

## M02R — R2+R3 workflow-semantic bootstrap

**P7 lifecycle note:** M02R is now historical terminal state at Task Board revision 104. P7 does not reopen or re-execute it. Its accepted result, reviews and regression evidence are immutable predecessor evidence for M02Q.


### Outcome

Before any M03 Card is materialized, the candidate PWv2.1 implementation
contains the accepted R2+R3 semantics for exhaustive fresh discovery review
and bounded convergence, durable observation closure, semantic Card right-sizing
and Planning-to-Execution-Prep decomposition fidelity, bounded
falsification-first/YAGNI Worker execution, and safe live-finding reconciliation. Historical M02 remains untouched and is replayed
only as regression evidence.

### Requirement coverage

Owns PWV21-REQ-108…PWV21-REQ-137 (30 requirements; per-requirement
verification in Appendix A).

### Required decomposition seams — bootstrap authority

Because the generalized semantic right-sizing/topology machinery is itself
implemented by this milestone, P6 froze four **required_seam** boundaries
for M02R. Execution Prep MUST materialize separate Cards for these seams and
MUST NOT merge across them. Further splitting is allowed only when the
right-sizing audit yields another meaningful independently falsifiable outcome.

1. **BOOT-A — review discovery, convergence, and observation closure**:
   REQ-108…114 plus REQ-133…137.
2. **BOOT-B — decomposition fidelity and semantic Card right-sizing**:
   REQ-115…121 plus REQ-128…130.
3. **BOOT-C — live-validation reconciliation and regression replay**:
   REQ-122…127.
4. **BOOT-D — Worker falsification-first and YAGNI discipline**:
   REQ-131…132.

These are semantic outcome boundaries, not file/layer/test-step splits.
They remain separately useful/reviewable when a sibling seam is RED, so the
bootstrap must not collapse them into one whole-milestone Card or fragment
them into meaningless implementation-step micro-Cards.

### Planned work

1. BOOT-A: extend review contracts/state/tests so formal lifecycle distinguishes
   finding-closure verification from fresh full-scope discovery; closure
   verification must evaluate the known findings, repair diff, required
   regression evidence and the materially implicated causal blast radius,
   including reachable callers/consumers/providers/contracts, sibling
   representations and negative-space cases; enforce complete-pass material
   finding collection, class-level/root-cause repair,
   stable authority/acceptance epochs, 5/4/3 genuinely-new material
   defect-class discovery ceilings, default 3 failed repair→closure rounds per
   material defect class, fresh rediscovery after known findings close,
   convergence mode-switch and one post-convergence validation; classify
   load-bearing blockers and durably retain/disposition non-load-bearing
   observations through pre-Final reconciliation.
2. BOOT-B: extend Planning/Execution Prep contracts and validation so
   `required_seam` / `preferred_seam` / `illustrative` intent is durable,
   JIT cannot silently override required seams, preferred-seam deviation
   requires bounded rationale, and materially risky topology receives a
   narrow fresh independent topology challenge; add the semantic Card invariant
   and split presumption for separable acceptance/contract/invariant/useful
   outcomes, with only concrete atomicity/invalid-intermediate-state/
   inseparable-acceptance/material-coupling evidence rebutting the split.
3. BOOT-C: add live-finding classification/reconciliation semantics, downstream
   affected-JIT gate behavior, tracker-non-authority guards, immutable
   historical regression replay, and an M02 regression corpus.
4. BOOT-D: add Worker execution discipline requiring a meaningful failing
   automated or observable check where feasible, minimum in-scope
   implementation to GREEN, binding YAGNI scope discipline, bounded post-GREEN
   refactoring, and DRY as guidance rather than an abstraction mandate.
5. Add bootstrap/regression tests proving the historical M02 one-mega-Card
   topology fails the new decomposition policy absent valid atomicity
   rationale, without modifying historical M02 Task Board/review state.
6. Preserve runtime neutrality: review/topology/Worker obligations remain semantic;
   model/session/worker identity is not made canonical.

### Acceptance

- Known-finding closure verification evaluates the known findings, repair diff,
  required regression evidence and the materially implicated causal blast radius,
  including reachable callers/consumers/providers/contracts, sibling
  representations and negative-space cases; it cannot satisfy a required fresh
  full-scope review.
- A full review continues after first blocker and records the complete
  independently discovered material finding set before repair.
- Class-level repair evidence includes sibling/negative-space coverage.
- Stable authority/acceptance epochs survive ordinary repair. The 5/4/3
  ceilings count only genuinely new material defect-class discovery epochs;
  closure verification, ordinary repair, GREEN review and known-class
  recurrence do not consume them.
- Each material defect class has a default ceiling of 3 failed
  repair→closure rounds before Main convergence analysis. Either ceiling
  routes to convergence analysis, never GREEN; one post-convergence
  validation is permitted and a further RED routes to structural
  classification rather than an automatic new ordinary review.
- After known material findings close, one fresh full-scope rediscovery review
  is required before the applicable review obligation can become GREEN.
- Findings block GREEN only with concrete load-bearing evidence. Every
  non-load-bearing observation remains durable with explicit disposition;
  still-open observations are reconciled before Final Integration, with
  bounded safe cleanup receiving its own subject/evidence/independent review.
- Semantic Card right-sizing splits separable independently verifiable/useful
  outcomes unless concrete coupling/atomicity evidence rebuts the presumption;
  file/module/layer/test/tool/step boundaries alone neither force nor prevent
  a split.
- Newly exposed oversized scope returns to Execution Prep at the smallest safe
  durable boundary while independently valid evidence is preserved; Workers
  cannot self-authorize broaden/merge/split.
- Worker fixtures prove falsification-first where meaningful, minimum in-scope
  implementation, YAGNI, bounded refactor, and non-absolute DRY.
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

- State-machine/unit fixtures for discovery-vs-closure, defect-class identity,
  stable epochs, 5/4/3 new-class discovery counting, per-class 3-round repair
  breaker, rediscovery gating and convergence routing.
- Causal-blast-radius closure fixtures proving bounded verification traverses
  materially implicated reachable callers/consumers/providers/contracts,
  sibling representations and negative-space cases in addition to the known
  findings, repair diff and required regression evidence; include unchanged-
  consumer/provider regression cases where applicable.
- Finding-severity/observation fixtures proving load-bearing RED criteria,
  durable dispositions, bounded cleanup promotion and no silent observation loss.
- Semantic Card right-sizing fixtures covering independent implementability,
  falsifiability, reviewability, invariant/contract families, dependencies,
  atomicity, cross-surface coupling, mega-Card and micro-Card negative cases.
- Worker-discipline fixtures with failing automated/observable checks where
  meaningful and negative tests for speculative scope/abstraction.
- Negative fixtures for early-stop review, literal-only repair, epoch-reset
  abuse, required/preferred seam bypass and tracker-as-authority.
- M02-derived immutable regression fixtures for topology and review history.
- Independent topology-challenge fixtures spanning risky and trivial cases.
- Readback/assertions proving no historical M02 mutation.

### JIT / implementation boundary

The four BOOT-A/B/C/D seams above are Planning-level `required_seam`
authority for this bootstrap milestone. Execution Prep may split within a seam
only when the result is itself a meaningful coherent independently falsifiable
outcome; it cannot merge seams. Exact schema/field/module naming remains JIT
under REQ-010. Any weakening of exhaustive discovery, defect-class or per-class
convergence ceilings, durable observation reconciliation, semantic Card
right-sizing, seam classes, topology-challenge triggers, Worker
falsification/YAGNI discipline, tracker non-authority or historical-state
preservation returns to Strategic Planning/Definition as appropriate.


## M02Q — Pre-M03 quality reconciliation

### Outcome

All 17 independently reconciled pre-M03 repair families are corrected on the exact candidate lineage, with exact durable proof for the three formerly authority-ambiguous families, before any M03 Card is materialized. M02Q closes the audit-defined quality gate without rewriting correctly terminal history.

### Corrective authority and formerly ambiguous mechanisms

P7 resolves the three `AUTHORITY_RECONCILIATION_REQUIRED` families without changing accepted product intent:

1. **RF006 — review-history identity/completeness.** Legacy status MUST NOT be inferred from file shape. A legacy review attempt is accepted only through explicit migration provenance bound to the exact immutable source attempt and exact source Git/workstream state. Migration may persist such provenance only when uniquely derivable under REQ-097…102; ambiguous attempts fail closed. New/current attempts use immutable Git-blob identity, append-only history and complete durable readback. Rewriting the same attempt ID to different bytes is invalid.
2. **RF008 — `editorial_exempt` proof.** Free-text `review_exemption_basis` is not proof. Exemption remains available only when an immutable classification record binds the exact prior GREEN-reviewed subject and exact changed subject, records the inspected diff/evidence, and has an independent semantic classification of `editorial_only` showing strategy, milestone topology, requirement coverage, gates and acceptance semantics unchanged. The classifier must not be the context that materially authored the changed subject. Without exact GREEN classification, the normal Premium-B → independent Plan Review → Premium-C path applies.
3. **RF011 — source-ref-independent recovery package.** Package completeness is derived, not caller-attested. The mandatory target-side package is the transitive closure of recovery-critical canonical locators rooted at the workstream identity/provenance and selected Task Board: stable non-discarded Card contracts, required Results, all review attempts needed to justify terminal state, referenced evidence/checkpoints/handoffs/observation reconciliation, plus immutable merge/PR evidence for fields that can only be known after merge. Each required class is lifecycle-derived and every locator must resolve to exact Git identity. An empty package is valid only for a genuinely empty/no-history workstream; it can never justify cleanup of a workstream with accepted history.

These are bounded Planning/technical representations of already accepted invariants. They do not add a new product goal, runtime authority or user-visible discretionary policy.

### Required repair-family seams and dependency order

The following seventeen seams are `required_seam`. They are the minimum semantic ownership units; no two may be merged by Execution Prep merely because they touch the same files.

| Order | Seam | Findings | Depends on | Required outcome |
|---:|---|---|---|---|
| 1 | RF008 | H012 | — | authority-owned exact old/new-subject editorial classification proof; no self-attestation |
| 2 | RF007 | H010,H020,H029 | — | reusable locator/readback resolver proves existence, semantic root and exact Git object identity; path traversal/symlink escape rejected |
| 3 | RF005 | H007 | — | Plan Review state domain is exhaustive/fail-closed; only accepted lifecycle states can route |
| 4 | RF017 | H030 | — | malformed durable TOML normalizes to deterministic Recovery rather than uncaught parser failure |
| 5 | RF002 | H002,H022 | — | Brainstorm→Definition requires promoted state + exact promotion authorization; explicit user stop has owning precedence |
| 6 | RF016 | H028 | — | SessionStart validates canonical router integrity from exact release/Git manifest identity, not marker strings |
| 7 | RF012 | H021 | RF007 | Planning and Plan Review bind a deterministic exact Definition-authority key covering Definition subject plus exact requirements/decision Git identities; stale authority cannot execute |
| 8 | RF013 | H023,H024 | RF007 | recovered Execution validates the full Card contract first; Execution Result has structured semantic status and only accepted success can authorize reconciliation/review |
| 9 | RF009 | H014,H016 | RF007 | Research origin/return and consumed prior-art result provenance are exact referential bindings read back by owners |
| 10 | RF006 | H008,H009,H018 | RF007 | immutable attempt identity + explicit migration provenance + complete append-only review-history readback |
| 11 | RF004 | H005,H006 | RF007,RF012 | implementation Review and Plan Review bind exact current subject plus exact acceptance/authority key; alternate/stale acceptance cannot authorize GREEN |
| 12 | RF003 | H003 | RF009 | owning explicit/premium/Intake/result/Board boundary is evaluated before generic Research dispatch while exact return ownership is preserved |
| 13 | RF010 | H015 | RF009 | issue alignment requires concrete repair subject plus completed exact diagnosis/prior-art proof; empty subject remains Intake diagnosis |
| 14 | RF011 | H017,H019 | RF006,RF007 | lifecycle-derived source-ref-independent package completeness + exact cleanup proof/readback |
| 15 | RF001 | H001,H004,H025 | RF004,RF006,RF007 | Task Board cross-field coherence and blocker/result/review-first routing; invalid status/result/review combinations fail closed |
| 16 | RF014 | H026 | RF001,RF013 | JIT obligations participate in terminality; consumed state binds exact downstream materialization/consumer proof |
| 17 | RF015 | H027 | RF011,RF014 | production selector composes Close continuation and emits true `end_of_scope_stop` only after durable completion |

Independent seams may be placed in an explicit parallel-safe set only after Execution Prep proves disjoint write/effect scopes under the accepted parallel-Card rules. Absence of a dependency is not itself parallel authorization.

### Accepted-authority mapping

M02Q is corrective and cross-cutting. It does not reassign the primary 137-requirement feature-ownership inventory in Appendix A; instead it operationalizes already accepted authority where the audit proved the current candidate violated it.

| Family | Governing accepted authority |
|---|---|
| RF001 | V2 Execution/Recovery/Close; REQ-028, REQ-077, REQ-092, REQ-105, REQ-107 |
| RF002 | V2 Brainstorming/Definition/User Stop; REQ-077, REQ-106, REQ-107 |
| RF003 | V2 Research/router precedence; REQ-077, REQ-078, REQ-092, REQ-095, REQ-107 |
| RF004 | V2 Review/Plan Review exact subject+acceptance; REQ-020, REQ-056…069, REQ-092 |
| RF005 | V2 Plan Review lifecycle; REQ-056…069, REQ-092 |
| RF006 | REQ-056…076, REQ-097…102, REQ-125, REQ-134…137; ADR-PWV21-004/005 |
| RF007 | REQ-020,022,025,028,031,092…102; ADR-PWV21-005 |
| RF008 | V2 Planning/Plan Review `editorial_exempt`; REQ-092, REQ-094, REQ-106, REQ-107 |
| RF009 | V2 Research; REQ-078, REQ-092, REQ-095, REQ-107 |
| RF010 | V2 Intake/alignment; REQ-077, REQ-078, REQ-107 |
| RF011 | V2 Close/Recovery; REQ-011,017,086,092…105; ADR-PWV21-005 |
| RF012 | V2 Definition/Planning; REQ-020, REQ-028, REQ-077, REQ-082, REQ-092 |
| RF013 | REQ-018…033, REQ-068, REQ-070, REQ-092 |
| RF014 | REQ-077, REQ-115…123, REQ-127…130 |
| RF015 | V2 Close/User Stop; REQ-105…107 |
| RF016 | REQ-011…017, REQ-092 |
| RF017 | REQ-092, REQ-093 |

### Planned work

1. Materialize M02Q only after P7 passes Premium B, independent Plan Review and Premium C.
2. Preserve the checkpoint, four probe reports, independent checkpoint review and P7 authority as exact immutable acceptance inputs.
3. Implement each RF required seam in dependency order, with one independently reviewable Card per RF unless semantic right-sizing requires a further split. Further split is allowed; cross-RF merge is not.
4. Re-run the exact defect-class probes represented by H001…H030, excluding rejected/no-repair H011 and H013, and add generalized sibling/negative-space regression cases for each repaired class.
5. Run the complete candidate regression suite after each materially shared foundation seam and at M02Q composition.
6. Perform a fresh independent M02Q Milestone Review over the composed candidate, raw probe evidence and accepted authority. M03 remains blocked until that review is GREEN and all load-bearing findings are closed under the R3 review lifecycle.

### Acceptance

- 17/17 RF families have durable implementation/result/review evidence; 0 are silently deferred under the quality-first policy.
- RF006, RF008 and RF011 use the exact P7 proof mechanisms above; implementation may not substitute self-attested booleans, free text, path-only identity or an empty package.
- Every original reproducing probe is converted into or backed by a stable regression test that fails before its correction and passes after it, with causal sibling/negative-space coverage where materially implicated.
- Existing valid positive controls remain GREEN.
- Exact locator/readback, Definition-authority freshness and acceptance-binding foundations are reused by dependent families rather than reimplemented inconsistently.
- Historical M01/M02/M02R remain unchanged except as immutable fixtures/evidence.
- No M03 Card/JIT trigger is materialized or consumed before M02Q terminal GREEN.
- A fresh independent M02Q Milestone Review is GREEN on the exact composed candidate subject.

### Verification strategy

- Replay all four pre-M03 probe batches against the corrected exact candidate lineage.
- Dedicated negative suites for dangling locators, symlink/traversal escape, same-path byte mutation, stale Definition authority, alternate acceptance, rewritten attempt IDs, truncated review history, malformed TOML, invalid result status, unconsumed JIT, empty recovery package, marker-preserving router corruption and false Close terminality.
- Full router/state/execution/review/close/delivery regression suites.
- Helper-less parity/readback checks for corrected deterministic routes where applicable.
- Independent Card review for every RF seam and separate M02Q Milestone Review; review convergence follows R3 discovery-vs-closure rules.

### JIT / implementation boundary

Execution Prep owns exact Card IDs, exact files, exact write scopes and legal parallel sets. It MUST preserve all seventeen RF seams. It MAY split one RF into smaller coherent Cards if real atomicity/review evidence requires it, but may not merge across RF seams or weaken the exact P7 authority mechanisms. Any evidence that a P7 mechanism changes accepted product semantics returns to Strategic Planning/Definition rather than being silently implemented.

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

M03 is the first downstream dogfood of the complete R2+R3 decomposition/right-sizing semantics.

- `required_seam`: destructive recovery acceptance remains a standalone
  independently observable gate and cannot be merged away.
- `preferred_seam`: helper-less derivation contract.
- `preferred_seam`: independent parity harness + representative corpus.
- `preferred_seam`: REQ-016 feature-admission/revalidation surface.
- Fixture encoding and harness internals remain JIT choices.
- Any merge of preferred seams requires qualifying durable technical rationale
  and the R2+R3 risk-based fresh topology challenge.
- Any weakening of the independent-context protocol, discard protocol or
  admission rule returns to Strategic Planning.

M03 acceptance must retain the actual Execution Prep topology/rationale/
challenge evidence and compare the candidate PWv2.1 branch's shadow/replay
classification against the governed P7 M02Q-gated materialization. No special user prompt
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
verification in Appendix A). M02R already owns REQ-108…114 and REQ-133…137 and supplies the
fresh-discovery/closure, defect-class convergence and observation-reconciliation
baseline that M05 must integrate across the complete Card/Milestone/
final-integration lifecycle rather than redefine.

### Planned work

1. Define the review-subject, independence-provenance, and evidence
   contracts for Card, Milestone, and final-integration review, including
   contamination rules and the no-prior-opinion information boundary.
2. Implement the review lifecycle state machine: assignment freshness,
   verdict validity (evidence completeness), RED repair/re-review loops with stable material defect-class discovery epochs,
   per-class repair/closure breakers, reopening, targeted revalidation, and
   correction routing.
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
   a separate Milestone review, and — only after terminal M02R, M02Q, and M03–M07 are
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
- Review convergence obeys both accepted breakers: 5/4/3 genuinely-new
  material defect-class discovery epochs by layer and 3 failed repair→closure
  rounds per material defect class. A breaker routes to Main convergence
  analysis and never accepts RED; ordinary in-scope defects stay in-Card.
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
  conformance evidence from terminal M02R and during M02Q plus M03–M07; the workstream final-integration
  review is post-M07 lifecycle evidence, never a prerequisite for M07's
  own GREEN.

### JIT / implementation boundary

Execution Prep may split M05 into contracts, lifecycle, independence/
handoff, and scenario-test Cards. Evidence packaging, internal data
structures, configuration representation, and module layout are JIT choices
within accepted semantics. The default convergence ceilings are accepted authority and are NOT a JIT
choice: Card=5, Milestone=4, final-integration=3 genuinely-new material
defect-class discovery epochs per stable authority/acceptance epoch, plus 3
failed repair→closure rounds per material defect class. Closure verification,
ordinary repair, GREEN fresh review and recurrence of an already-known class
do not consume a discovery epoch. Any accepted change to these defaults or
mode-switch semantics requires Strategic Planning/Definition as appropriate;
Execution Prep cannot tune them.

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
| ADR-PWV21-004 | Layered fresh review, exhaustive discovery, defect-class convergence and durable observations | M02R (bootstrap review/convergence/observation primitives), M05 (full lifecycle integration) |
| ADR-PWV21-005 | Git-first handoff, recovery, migration; fail-closed | M03 (procedure/parity), M06 (handoff), M07 (recovery/migration/close) |
| ADR-PWV21-006 | Preserve planner decomposition intent; semantic Card right-sizing; risk-based topology challenge | M02R (generic seam/right-sizing/topology semantics), M03 (first downstream dogfood) |
| ADR-PWV21-007 | Incorporate live workflow discoveries at safe boundaries without rewriting history | M02R (classification/reconciliation/replay), M03 (first downstream live-consumer/shadow evidence) |
| ADR-PWV21-008 | Bounded falsification-first Worker execution with YAGNI and non-absolute DRY | M02R (BOOT-D), then consumed by all later implementation Cards |

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
- Finding-closure causal blast radius (REQ-108): M02R/BOOT-A requires bounded
  closure verification to cover known findings, repair diff, regression evidence
  and materially implicated reachable callers/consumers/providers/contracts,
  sibling representations and negative-space cases; this remains distinct from
  the mandatory fresh full-scope rediscovery gate.
- Review-convergence authority (REQ-111…114/137): M02R establishes stable
  authority/acceptance epochs, 5/4/3 genuinely-new material defect-class
  discovery ceilings, the default 3 failed repair→closure rounds per class,
  fresh rediscovery after closure and post-convergence structural routing;
  M05 integrates these fixed semantics into the complete review lifecycle but
  cannot redefine them through JIT. No breaker converts RED to GREEN.
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
- Card right-sizing and late topology evidence (REQ-128…130): M02R owns the
  semantic split/merge decision function. Execution Prep may refine but may
  not collapse required seams; Workers preserve valid evidence and return
  newly exposed separable scope to Execution Prep rather than self-authoring.
- Worker discipline (REQ-131/132): M02R owns falsification-first/YAGNI
  semantics. Later milestones consume it without fixed size/time classes or
  speculative abstraction obligations.
- Review observation closure (REQ-133…136): M02R owns blocking-vs-advisory
  classification and durable dispositions. Final Integration cannot complete
  with unreconciled open observations.

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
   independent Card review and separate Milestone reviews during M02Q and M03–M07 (with terminal M02R retained as historical evidence),
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
- M01/M02/M02R remain terminal. P7 does not reopen them. Their accepted results and failures are immutable regression evidence for M02Q and downstream work.
- The existing waiting `after-M02-T01` JIT state must be reconciled after
  P7 approval: it must not materialize M03 directly. Execution Prep first materializes M02Q under its seventeen required repair-family seams; only after M02Q terminal GREEN may the downstream M03 trigger be created/satisfied/consumed. Historical M02R stays terminal.
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
| R-13 | Execution Prep collapses planner seams/outcomes into another mega-Card | Medium / High | Historical four M02R seams plus seventeen P7 M02Q required RF seams + semantic right-sizing audit + risk-based topology challenge; M02 regression replay |
| R-14 | Review loops stop at first blocker or degenerate into unbounded rediscovery/repair | Medium / High | Exhaustive discovery + class repair + stable epoch + 5/4/3 new-class ceilings + 3-round per-class breaker + fresh rediscovery after closure |
| R-15 | Live finding mutates active history or tracker text becomes authority | Low / High | Classification + affected-downstream reconciliation + tracker non-authority + immutable historical replay |
| R-16 | M03 is falsely presented as deployed PWv2.1 dogfood while consumer authority is still main | Medium / Medium | Explicit authority-level dogfood + candidate shadow/replay distinction; deployed consumer validation deferred to post-release Paseo/Pi |
| R-17 | Right-sizing over-corrects into meaningless micro-Cards | Medium / Medium | Semantic outcome test: independent usefulness/falsifiability required; file/layer/test-step splits alone insufficient; setup stays with consuming outcome |
| R-18 | Advisory review observations disappear or create endless cleanup churn | Medium / High | Durable dispositions + pre-Final reconciliation + bounded explicit cleanup work; no recursive cleanup merely because further improvement is imaginable |
| R-19 | Worker discipline turns into speculative TDD/DRY ceremony or scope expansion | Medium / Medium | Falsification only where meaningful, observable checks otherwise, minimum implementation, binding YAGNI, non-absolute DRY |

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
- Fixed project-size classes or LOC/file/token/time Card limits; Card topology
  remains semantic and outcome-driven.

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
- Each new milestone, including M02Q and M03–M07, closes only on its
  acceptance section GREEN plus its own separate Milestone review. From-the-start
  Card/Milestone/final independence requirements apply to this
  implementation using current V2 mechanics plus the accepted plan
  controls (separate reviewers, evidence gating, no-prior-opinion
  boundary); there is no weaker gate for current implementation
  milestones. Existing correctly closed historical stages still retain
  REQ-099 protection (valid closed reviews stay valid; new semantics
  apply to active stages only).
- Only after M02Q and M03–M07 are complete, with M02R already terminal, with historical M01/M02 already
  terminal, does the separate fresh workstream final-integration review occur; workstream close then requires that
  review GREEN with complete evidence.
- Escalation paths: JIT/Execution Prep detail → Execution Prep; milestone
  strategy/order/outcome change → Strategic Planning (new cycle, new A/B/C
  if material); accepted product/global intent change → Project Definition;
  missing facts → Research. Unstructured global repair is forbidden.

## Appendix A — Auditable requirement coverage inventory

Every accepted requirement ID appears exactly once, with its owning
milestone and verification method. Totals: M01: 10, M02: 16, M02R: 30,
M03: 7, M04: 22, M05: 21, M06: 15, M07: 16 — 137/137 mapped,
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
| PWV21-REQ-061 | M05 | Bounded finding-closure fixtures: discovering Reviewer may verify Worker repair only when it did not repair the subject; closure remains distinct from the next fresh full-scope discovery review |
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
| PWV21-REQ-108 | M02R | Closure-verification fixtures cover known findings + repair diff + required regression evidence + materially implicated reachable callers/consumers/providers/contracts + sibling representations + negative-space cases; negative test proves closure cannot satisfy required fresh full-scope review |
| PWV21-REQ-109 | M02R | Exhaustive-review fixture: first blocker does not terminate pass; complete material finding set frozen |
| PWV21-REQ-110 | M02R | Repair-class fixture: root cause + sibling/negative-space generalized regression required |
| PWV21-REQ-111 | M02R | Epoch fixtures: ordinary repair preserves epoch; accepted authority redesign records explicit reset |
| PWV21-REQ-112 | M02R | Discovery-epoch matrix: Card=5, Milestone=4, final=3; only genuinely new material defect classes count; closure/repair/GREEN/known recurrence excluded |
| PWV21-REQ-113 | M02R | Breaker fixtures: discovery ceiling or per-class repair/closure ceiling enters Main convergence analysis and never accepts RED |
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
| PWV21-REQ-128 | M02R | Semantic Card invariant fixtures: one coherent independently falsifiable outcome substantial enough for its own lifecycle |
| PWV21-REQ-129 | M02R | Split/merge decision matrix: separable acceptance/contract/invariant/useful outcomes split unless concrete atomicity/coupling rebuttal; file/layer/test-step boundaries insufficient |
| PWV21-REQ-130 | M02R | Late-oversize fixtures preserve independently valid evidence and route remaining scope to Execution Prep; Worker self-split/merge/broaden rejected |
| PWV21-REQ-131 | M02R | Worker fixtures start from meaningful failing automated/observable check and reach GREEN with minimum in-scope implementation |
| PWV21-REQ-132 | M02R | YAGNI/DRY negative fixtures reject speculative scope/abstraction; bounded post-GREEN refactor remains in Card authority |
| PWV21-REQ-133 | M02R | Finding-severity fixtures require concrete load-bearing evidence to block GREEN; advisory/speculative observations alone cannot keep RED |
| PWV21-REQ-134 | M02R | Durable observation fixture retains origin + explicit disposition until reconciliation; real blocking findings cannot be downgraded for convenience |
| PWV21-REQ-135 | M02R | Pre-Final reconciliation gate requires every open non-load-bearing observation resolved/cleanup_candidate/deferred/promoted/tracked; tracker remains optional bookkeeping |
| PWV21-REQ-136 | M02R | Cleanup fixtures group bounded safe in-scope work under exact subject/evidence/independent review and terminate without recursive speculative cleanup |
| PWV21-REQ-137 | M02R | Review lifecycle fixture requires fresh full-scope rediscovery after closure, counts only genuinely new defect-class discovery epochs, and enforces 3 failed repair→closure rounds per class before convergence |


## Planning audit (planner's summary)

Planner completeness/challenge result: **GREEN**.

- Premium A for `definition:R3|planning-cycle:7` was durably satisfied before material P7 planning.
- Definition R3 and all nine pinned authority blobs are unchanged from the independently GREEN-reviewed P6 authority set.
- The pre-M03 checkpoint was independently reviewed GREEN and reconciles 17/17 repair families with 14 STILL_APPLICABLE, 3 AUTHORITY_RECONCILIATION_REQUIRED and 0 already satisfied.
- Explicit user authorization permits a material pre-M03 replan over all 17 families while forbidding implementation-time invention of product semantics.
- P7 resolves RF006/RF008/RF011 at Planning level using bounded durable mechanisms that enforce already accepted invariants; no unresolved product/goal choice remains and no Definition rewrite is required.
- All seventeen repair families are exact `required_seam` ownership boundaries in M02Q; the checkpoint dependency DAG is preserved.
- Correctly terminal M01/M02/M02R remain terminal under REQ-125.
- The primary 137/137 requirement inventory remains unchanged; M02Q is a corrective cross-cutting gate mapped to existing authority, not a second competing requirement-owner map.
- M03 and every downstream milestone now consume terminal M02Q evidence; no M03 materialization is legal before M02Q GREEN.
- The exact audited candidate branch still resolves to `07c724085de591c2a0bb51aaaae0ec23009880bf`, so the checkpoint findings and P7 corrective baseline are not stale at planning time.
- The plan retains independent Stage-6 Plan Review and normal Premium B/C gates. This planning context must not review the frozen P7 subject.

Full audit evidence is persisted separately under the workstream evidence directory after plan creation/freeze preparation.
