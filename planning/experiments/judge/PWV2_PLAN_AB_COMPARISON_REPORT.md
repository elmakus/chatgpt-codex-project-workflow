# PWV2 Strategic Plan Blind A/B Comparison Report

Date: 2026-09-22
Comparison ID: PWV2-PLAN-AB-JUDGE-01
Judge contract: planning/experiments/judge/PWV2_PLAN_AB_JUDGE_CONTRACT.md
Frozen Definition checkpoint: 8055ed00acdb708c79919d470217fd87c920973a
Candidates: PLAN_A.md and PLAN_B.md

## 1. Evaluation boundary and method

This report evaluates only the two anonymized candidate plans against the frozen Definition authority named by the judge contract:

- requirements/PROJECT_WORKFLOW_V2.md;
- ADR-PWV2-001..006;
- brainstorming/V1_TO_V2_COVERAGE_MATRIX.md;
- brainstorming/V2_VALIDATION_MATRIX.md;
- implementation/workstreams/feature-common-preexecution-core/handoffs/DEFINITION_COMPLETE_2026-09-22.md.

No candidate provenance, canonical Plan Review, planner audit, forbidden branch, or model/runtime identity was used.

The contract defines ten dimensions but does not assign unequal weights. This report therefore uses equal weighting: each 1-10 dimension contributes ten points, and the ten scores sum directly to an overall score out of 100.

Raw length, milestone count, table count, and verbosity are not rewarded. Detail receives credit only when it removes a real implementation ambiguity, protects an accepted invariant, reduces likely rework, or creates a materially stronger acceptance/recovery path.

## 2. Executive comparison

Both candidates are strong and both materially cover the frozen Definition. Neither has a missing ADR, missing validation family, or obvious contradiction that makes it non-executable.

Plan A is stronger as a Strategic Plan because it closes more implementation-critical ambiguities before Execution Prep without over-freezing low-level implementation detail. Its most material advantages are:

1. an early, isolated plugin/package compatibility probe before the semantic implementation becomes expensive to reshape;
2. explicit construction custody between the current development/control repository and the new V2 repository, including one-live-owner transfer and interrupted-transfer recovery;
3. row-level V1-to-V2 regression ownership for the entire frozen matrix rather than only grouped disposition coverage;
4. more concrete migration idempotency/crash/retry/rollback rules;
5. earlier placement of real-surface L01-L05 evidence once the relevant slices exist, reducing the risk of discovering packaging/bootstrap behavior only at the final gate;
6. more exhaustive integration/terminal recovery handling, including target movement, deleted source branches, stacked paths, tracker closure, and uncertain external effects.

Plan B has real strengths that should not be lost. Its semantic decomposition is cleaner at the conceptual level: foundation -> pre-execution -> execution -> review/recovery -> close -> delivery -> migration -> cumulative automation -> live acceptance. It also expresses YAGNI and deferred implementation choices very clearly. Its main weakness is not correctness but that several high-cost operational questions are left to later milestones or to re-derivation during execution.

The difference is therefore a strategic/actionability difference, not a presentation-only difference.

## 3. Rubric scores

| Dimension | Plan A | Plan B | Material comparison |
|---|---:|---:|---|
| 1. Requirement coverage quality | 10 | 9 | Both map 76/76. A binds each requirement to a concrete package/oracle and also binds every frozen V1 surface row to a stable S001-S097 owner/assertion. B is complete but some coverage remains grouped and must be re-expanded during implementation. |
| 2. ADR / accepted-DROP fidelity | 10 | 10 | Both preserve ADR-PWV2-001..006 and explicitly reject the frozen DROP set from normal V2 semantics. No material target-semantics contradiction was found. |
| 3. Milestone sequencing and dependency quality | 10 | 9 | A de-risks plugin compatibility in M01 and runs applicable live surface checks in M05; B postpones real delivery inspection to M06 and all mandatory live checks to M09. B's ordering is coherent, but it carries more late-discovery risk. |
| 4. YAGNI / proportionality | 9 | 10 | Both are disciplined. B is slightly cleaner about keeping exact schema, review encoding, plugin metadata, migration handlers, and merge mechanics deferred. A adds more construction-custody and delivery safeguards; most are justified, but they add process surface. |
| 5. JIT boundary quality | 10 | 9 | A has explicit trigger/owner/evidence boundaries and distinguishes strategic decisions from runtime-dependent details especially well. B is also strong, but some later decisions (notably packaging feasibility and exact matrix execution ownership) are deferred far enough to increase rework risk. |
| 6. Migration / cutover safety | 10 | 9 | A specifies dry-run/apply/readback/restart, ambiguity handling, no dual-write, one-live-owner custody transfer, and post-effect rollback limits. B has a sound conceptual migration transaction but less exact custody/idempotency detail. |
| 7. Validation quality | 10 | 10 | Both preserve A01-A17 and L01-L09 as production gates and keep deterministic tests automated. A stages early live evidence; B centralizes cumulative automated and live gates. Both are valid strategies. |
| 8. Recovery / integration / edge-case coverage | 10 | 9 | A is stronger on target races, stacked dependencies, source-ref disappearance, tracker retries, custody interruption, migration crash points, and package/update ambiguity. B covers the core cases but with less operational precision. |
| 9. Implementation actionability | 10 | 9 | A can be decomposed into Execution Prep Cards with less strategic re-derivation because packages, owners, checkpoints, JIT triggers, evidence, and coverage rows are explicit. B remains executable but would require more work to reconstruct exact row-level and construction-custody contracts. |
| 10. Context / complexity efficiency | 8 | 8 | Both repeat authority through requirement/ADR/coverage/validation audits. A's repetition is denser and often executable; B is conceptually cleaner but substantially repeats the same coverage in later audit sections. Neither is maximally compact. |

Overall weighted score:

- Plan A: **97/100**
- Plan B: **92/100**

## 4. Dimension-by-dimension analysis

### 4.1 Requirement coverage quality

#### Plan A

Plan A provides genuine execution ownership for all 76 requirements in Appendix A. The mapping is not merely an ID checklist: rows point to concrete packages and acceptance oracles, for example:

- REQ-005 -> M07.P2 -> L06 cross-runtime continuation;
- REQ-025 -> M03.P2 -> qualifying delegation plus A04/L08;
- REQ-032/033 -> M04.P2 -> uncertain-effect readback and write/readback/verify/evidence;
- REQ-061..065 -> M04.P1/P3 -> target refresh, review reuse/new subject, target-side recovery, safe cleanup;
- REQ-074..076 -> M07 qualification plus A01-A17/L08-L09/A17.

The more important differentiator is Appendix B: every frozen V1 surface is given an explicit S001-S097 row with a target owner and assertion/non-code disposition. This materially strengthens REQ-076 and A17 because execution does not need to reconstruct a row-level regression manifest from prose.

Plan A also avoids making all fields strategic. Section 3.1 fixes artifact ownership and exclusions while explicitly leaving schema/tool details to M01 JIT.

#### Plan B

Plan B also maps all 76 requirements in Section 7 and gives each an implementation owner and acceptance path. This is real coverage, not a nominal list.

Its weaker point is the V1 matrix. Section 9 appears to account for all frozen categories and surfaces, and M07/M08 promises a machine-regressed disposition manifest, but the candidate does not bind each frozen row to a stable per-row execution target in the plan itself. That is not a coverage failure, but it creates a re-expansion step during execution and slightly raises omission/reclassification risk.

A second mild weakness is REQ-017 during V2 construction. Plan B correctly preserves the one-project/one-repository product invariant and bounded migration, but it is less explicit about which repository owns live construction state while code is being produced in the new repository. The frozen Definition explicitly says the current repository remains development/history authority while V2 is built, so this is an execution-recovery question worth resolving strategically.

Verdict: both cover 76/76; A has stronger executable ownership.

### 4.2 ADR / accepted-DROP fidelity

Both candidates faithfully preserve:

- ADR-PWV2-001: one runtime-neutral semantic core, no execution policy or runtime identity;
- ADR-PWV2-002: ChatGPT GitHub bootstrap, Codex local bundled pw plugin, one semantic source;
- ADR-PWV2-003: branch-first workstreams, #issue diagnosis/alignment boundary, GitHub Issue as bookkeeping;
- ADR-PWV2-004: one active Project Card, runtime-owned worker topology, coordinator-owned reconciliation;
- ADR-PWV2-005: exact-subject review, semantic independence, mandatory A/B/C premium stops;
- ADR-PWV2-006: progressive disclosure, broad proportional Research, YAGNI, selective technical contracts.

Both also explicitly reject the accepted DROP set: fixed product-policy trees, execution_policy, mixed Capability Gate, Context Health/FRESH, Card scheduler/batch/lane machinery, active_execution/transfer_ready/ordinary returned semantics, durable runtime binding, named product roles, autonomous #issue repair, planner-spawned Stage-6 review, deployment-only stop, duplicate plugin semantics, ordinary Codex remote policy fetch, and source-branch-dependent terminal recovery.

Plan A mentions the V1 controller and chatgpt_only in its planning/construction context, but it does not reintroduce that concept into V2 target semantics. That is not an ADR violation.

One Plan A watch item is M04.P4/Section 2.1: it carries detailed fork-versioning behavior and historical V1 evidence beyond what the frozen matrix spells out. The frozen authority does require preserving the trigger-only fork lineage behavior, so this is acceptable if those details remain implementation evidence/JIT and are not treated as new Definition authority.

No material hidden ADR contradiction was found in either candidate.

### 4.3 Milestone sequencing and dependencies

#### Plan A

Plan A uses seven implementation milestones:

- M01 foundation/state/router plus early package feasibility;
- M02 Intake through Definition/Planning;
- M03 JIT execution/delegation/review/recovery;
- M04 integration/close/terminal recovery/fork trigger;
- M05 thin delivery plus L01-L05;
- M06 bounded migration;
- M07 cumulative qualification, L06-L09, and controlled adoption.

Two ordering choices are particularly strong.

First, M01.P3 performs a narrow real package compatibility probe for namespace pw, Skill project_workflow_v2, exact invocation, installed-root layout, and SessionStart/trust behavior. This does not let delivery drive semantics; it only retires a high-impact feasibility risk before building the full core.

Second, M05 executes L01-L05 at the earliest complete semantic/delivery slice rather than waiting until every migration and final qualification task is complete. This can expose real surface failures while correction is still localized.

#### Plan B

Plan B uses nine milestones with a very clean decomposition:

foundation -> pre-execution -> execution -> review/recovery -> close -> delivery -> migration -> automated hardening -> live acceptance/cutover.

This is conceptually excellent and makes ownership easy to reason about. The cost is later risk retirement. The real Codex packaging contract is intentionally inspected only at M06, after M01-M05 common semantics are built. The plan's own challenge audit admits that an earlier packaging spike may be useful, but it is not made a required risk-retirement checkpoint. Likewise all required live tests are grouped in M09 after M08.

This does not make B wrong; it makes the cost of an unexpected plugin/bootstrap constraint larger.

Verdict: A has the safer dependency/risk sequence; B has the cleaner conceptual decomposition.

### 4.4 YAGNI / proportionality

Both candidates are strong.

Plan A explicitly excludes daemon/database/runtime dispatcher/universal ledger/generic DAG engine, runtime role catalogs, plugin updater, version-negotiation service, global registry, Context Health, universal OpenSpec, and speculative Cards. Its technical-contract trigger is material contract value, not ceremony.

Plan B is slightly stronger in presentation and discipline here. Section 12 has a concise deferred-detail table and a direct list of mechanisms not planned. M01 fixes ownership/invariants before fields; M03 makes technical contracts evidence-triggered; M06 defers current plugin metadata; M07 limits migration handlers to concrete supported surfaces.

Plan A's detailed construction custody, plugin source-disambiguation, and transfer procedure all have real current justification, but they add more mechanism to the plan. They are useful rather than speculative, yet B is marginally more proportional as a planning artifact.

### 4.5 JIT boundary quality

Plan A has a particularly strong trigger-based JIT register in Section 7:

- schema syntax after first valid state/router slice;
- package details after real installed probe;
- repair choice after diagnosis;
- Card boundaries after predecessor evidence;
- technical contract only after demonstrated interaction complexity;
- runtime delegation/review realization only at launch;
- target reconciliation only after target movement;
- migration mapping only for selected real legacy inputs;
- live fixtures only after delivered candidate exists.

That is exactly the distinction the frozen Definition asks for: freeze strategic invariants now, defer implementation detail until evidence makes it knowable.

Plan B's Section 12 is also good, but two deferrals are slightly aggressive strategically: packaging feasibility waits until M06, and the matrix-to-concrete-regression manifest is not fully instantiated in the plan. Both can be solved during execution, but they can trigger avoidable rework.

### 4.6 Migration / cutover safety

Plan A is materially stronger here.

M06 defines:

- finite recognized V1 input families;
- dry run before mutation;
- preservation of authority/results/review history;
- removal of runtime/policy/scheduler state without semantic loss;
- explicit handling of concurrent V1 Cards by quiescing/serializing under V1 rather than inventing a winner;
- failure when exact review independence cannot be proven;
- repeated apply as same-result/no-op or explicit conflict;
- crash-point tests before/after record/ref/external write;
- no permanent compatibility route.

Section 4 then defines construction custody and the later one-live-owner transfer. Section 8 distinguishes pre-activation rollback from post-effect recovery and correctly refuses to promise a generic inverse converter.

Plan B's Section 11 is sound: classify exact V1 inputs, inventory obligations, stage V2, validate, fail closed on ambiguity, make state durable, verify readback, and avoid permanent compatibility mode. It also warns that post-migration rollback is not simply switching execution_policy back.

What it lacks is A's explicit live construction custody, interrupted ownership-transfer protocol, repeated-apply/idempotency rule, and detailed concurrent-state handling. Those are the kinds of omissions that can cause real implementation rework rather than merely documentation rework.

### 4.7 Validation quality

Both plans are excellent and score equally.

Plan A maps A01-A17 to concrete packages in Section 6.1 and L01-L09 to staged real-surface checkpoints in Section 6.2. It adds supplemental deterministic cases for alignment, premium re-entry, end-of-scope, stacked dependencies, source-head changes, Research return crash points, package failure, and custody interruption. It explicitly rejects relabeling V1/synthetic evidence as V2 live PASS.

Plan B authors tests with each milestone, then uses M08 as the cumulative automated production gate and M09 as the live gate. Section 10 preserves the frozen principle that deterministic behavior should not be shifted to the user. L08/L09 remain mandatory before first production acceptance.

The strategies differ, but neither leaves a material validation hole.

### 4.8 Recovery / integration / edge cases

Plan A has broader and more actionable coverage.

Its router precedence explicitly reconciles durable completed results before replay, routes contradictory ownership to Recovery, and distinguishes human stops from remediable role/technical transitions.

M04 handles:

- target refresh before review reuse;
- compatibility verification for SHA-only target movement;
- new review subject for material change;
- immediate target reread before race-sensitive mutation;
- uncertain external writes with inspect-before-retry;
- intermediate versus final tracker closing;
- target-side terminal package before branch disappearance;
- surviving-ref safe_to_delete with exact-head revalidation;
- unmerged/superseded terminal closure;
- stacked child fold/integration paths;
- end-of-scope without invented follow-up.

M06 adds migration crash/idempotency cases and Section 4 adds custody-interruption recovery.

Plan B covers all frozen core cases: durable result recovery, ambiguous effects, review attempt recovery, target movement, source branch disappearance, tracker close/readback, cleanup, and cross-runtime continuity. It is strategically correct, but the stacked-workstream, construction-custody, migration-crash, and package-source ambiguity cases are less fully closed.

### 4.9 Implementation actionability

Plan A has the highest actionability because each milestone contains outcome, dependencies, packages, checkpoint/acceptance, and JIT boundaries, and the plan gives concrete owners for requirements, validations, and every V1 disposition row.

A capable execution context could generate bounded Cards without redoing Strategic Planning. It would still need implementation research for the intentionally JIT items, but not strategic re-interpretation.

Plan B is also executable, with outcomes, work packages, checkpoints, and JIT sections. The main areas likely to require extra strategic reconstruction are:

- exact construction control/custody between old and new repositories;
- exact row-level A17 manifest ownership;
- whether/when an early plugin feasibility spike is mandatory;
- exact repeated-migration/idempotency and interrupted-transfer behavior.

These are bounded gaps, not evidence that the plan is incomplete.

### 4.10 Context / complexity efficiency

Neither candidate is highly compact.

Plan A repeats the frozen Definition through Appendix A and the entire V1 matrix through Appendix B, and it includes planning-control/process material in Sections 1/4/Appendix C. However, much of that repetition is operationally useful because it converts frozen inputs into direct owner/assertion mappings. The least efficient parts are the V1 controlling-process detail and some delivery/fork prior-art narrative.

Plan B is conceptually cleaner in its first half but then repeats the same strategy as:

- requirement table;
- six-ADR conformance audit;
- full grouped V1 matrix audit;
- validation integration;
- migration/cutover section;
- JIT audit;
- risk register;
- completeness/challenge audit.

That repetition is useful for auditability but does not create a proportional amount of additional implementation value.

The plans therefore tie on this dimension: both can be compressed materially without losing strategy.

## 5. Coverage verification

### 5.1 PWV2-REQ-001..076

Plan A: **76/76 genuinely covered.**

Every requirement has a primary owner/package and an acceptance/validation path. No requirement was found that exists only as an ID mention.

Plan B: **76/76 covered.**

Every requirement has an owner and planned coverage. The weaker cases are not missing, but are less fully executable:

- REQ-017: product-level one-repository rule is covered, but build-time control/custody across source and target repositories is under-specified compared with A;
- REQ-020: stacked dependency provenance is present, but legal integration/recovery paths are less explicit;
- REQ-076: all matrix surfaces are grouped and accounted for, but exact per-row owner/assertion binding is deferred to the later regression manifest.

These are actionability differences, not requirement failures.

### 5.2 Full V1 -> V2 disposition matrix

Plan A: **full matrix accounted for with explicit S001-S097 mapping.** Every frozen row has a disposition, owner, and assertion/non-code destination. The standalone DROP checklist is also carried into A17.

Plan B: **full matrix accounted for semantically.** Section 9 covers every frozen category/surface and M07/M08 requires a machine-regressed disposition manifest. The coverage is valid, but less directly bound at planning time.

### 5.3 A01-A17 and L01-L09

Plan A:

- A01-A17 all explicitly mapped;
- L01-L05 placed at M05 when delivery plus relevant semantics exist;
- L06-L09 placed at final qualification M07;
- L08/L09 explicitly cannot be substituted by synthetic traces.

Plan B:

- A01-A17 all explicitly assigned to M08 with milestone-level test ownership earlier;
- L01-L09 all mandatory in M09;
- L08/L09 explicitly required before production acceptance.

No validation ID is missing in either plan.

### 5.4 Nominal versus executable coverage

Plan A has no material nominal-only requirement coverage. The main watch item is that detailed trigger-only fork behavior should remain bounded by the frozen accepted disposition and not become new product intent merely because historical evidence exists.

Plan B's grouped V1 regression mapping and build-time custody are the clearest examples of coverage that is correct at the outcome level but requires additional execution-time decomposition before it becomes as directly testable as A.

## 6. Structural comparison

### 6.1 Conceptual decomposition

Plan A: seven broad milestones. It intentionally combines implementation/review/recovery in M03 and integration/close/fork in M04, then treats delivery, migration, and final qualification separately.

Plan B: nine narrower milestones. It separates execution from review/recovery and separates review/recovery from Close. It also creates explicit cumulative automated-hardening and live-acceptance milestones.

The difference is mostly organizational until it affects risk timing. The material timing differences are packaging feasibility and live-surface validation.

### 6.2 Major dependency-order differences

Plan A:
- early package compatibility probe in M01;
- core semantics through M04;
- delivery and first live surface checks in M05;
- migration in M06;
- full qualification/remaining live/cutover in M07.

Plan B:
- core semantics through M05;
- delivery in M06;
- migration in M07;
- cumulative automation in M08;
- all live acceptance/cutover in M09.

A therefore retires external-platform uncertainty earlier. B protects semantic purity by waiting longer before delivery work, but at the cost of later discovery.

### 6.3 JIT versus upfront differences

Both correctly defer:
- exact schema keys;
- runtime worker/session realization;
- technical-contract creation;
- merge/rebase mechanics;
- extra migration handlers;
- fork behavior activation;
- concrete live fixtures.

A fixes more strategy around state ownership, router precedence, migration idempotency, construction custody, and terminal recovery.

B fixes the same semantic invariants but leaves more operational form to later implementation milestones.

### 6.4 Migration / cutover differences

A defines a bounded construction exception, one live controller, explicit transfer, interrupted transfer recovery, migration dry-run/apply/readback, and post-effect rollback policy.

B defines clean-build separation, bounded migration transaction, project-by-project cutover, and no permanent compatibility mode, but not the same exact ownership-transfer protocol.

### 6.5 Test / acceptance differences

A uses incremental mandatory evidence:
- automated tests throughout;
- L01-L05 as soon as delivery slices are complete;
- final A01-A17 reconciliation plus L06-L09 before production adoption.

B uses:
- milestone tests throughout;
- M08 consolidated deterministic gate;
- M09 consolidated real-product gate.

Both are valid. A reduces late platform surprise; B has a cleaner final acceptance phase.

## 7. Risk comparison

### 7.1 Plan A — top five risks introduced by the plan itself

1. **Construction-custody complexity.** The explicit V1-control/V2-target transfer protocol is valuable, but it creates more process/state transitions that must themselves be implemented correctly.
2. **Early platform-probe distraction.** M01.P3 could consume effort on volatile plugin/runtime behavior before the semantic kernel is mature if it is not kept strictly as a feasibility probe.
3. **Broad milestone scope.** M03 and M04 each contain several substantial concerns; careless Execution Prep could turn them into oversized Cards rather than preserving the plan's package boundaries.
4. **Over-specific trigger-only fork detail.** Historical fork-versioning details could accidentally be treated as new frozen product intent unless implementation keeps them subordinate to the accepted trigger-only disposition.
5. **Dense owner tables can stale.** Appendix A/B references are highly actionable, but if milestone/package boundaries change, the mapping must be updated coherently rather than becoming false precision.

### 7.2 Plan A — five risks handled particularly well

1. **Delivery architecture surprise** through the early exact plugin/Skill/root probe.
2. **Ambiguous two-repository construction ownership** through the bounded custody model and one-live-owner transfer.
3. **Loss of recovery after branch deletion or target movement** through target-side packages, refresh/reuse rules, and safe cleanup.
4. **Replay/duplication after interrupted external effects or migration** through readback-first, idempotent apply, and crash-point testing.
5. **Regression to V1 rejected machinery** through explicit S001-S097 disposition ownership plus DROP assertions.

### 7.3 Plan B — top five risks introduced by the plan itself

1. **Late plugin feasibility discovery.** Real Codex packaging/Skill/SessionStart assumptions are inspected in M06 after the semantic core and Close are already designed.
2. **Late real-surface discovery.** All mandatory live acceptance is concentrated in M09, increasing the amount of code potentially affected by an unexpected ChatGPT/Codex/GitHub surface behavior.
3. **Under-specified construction custody.** The plan is clear about the target repository and clean migration but less clear about live control/state ownership while V2 is being built from the current repository.
4. **Grouped A17 ownership.** Section 9 proves semantic awareness of the frozen matrix but leaves stable row-level test ownership to M07/M08, creating some re-derivation risk.
5. **Potential duplicate hardening work.** M08 is useful as a cumulative gate, but if milestone tests are not designed as the same reusable suite, the separate hardening phase can become test recreation rather than consolidation.

### 7.4 Plan B — five risks handled particularly well

1. **Adapter-driven semantic drift** by keeping delivery after the common lifecycle is stable.
2. **Human-control regressions** with a strong #issue alignment contract, adaptive Brainstorming, and durable A/B/C.
3. **Review/recovery correctness** by separating exact-subject review and external-effect recovery into a dedicated milestone.
4. **Schema/abstraction over-design** through explicit JIT field, plugin, migration-handler, and technical-contract boundaries.
5. **Legacy contamination of normal V2 routing** by placing migration outside workflow/ and gating production on DROP regression tests.

## 8. Cross-pollination value

### 8.1 Strongest ideas from Plan A

The eventual canonical plan should preserve or import these ideas:

1. **Early isolated package compatibility probe** before deep semantic implementation, without turning the adapter into architecture.
2. **Explicit construction custody and one-live-owner transfer** between the current development/control repository and the new V2 target, including interrupted-transfer recovery.
3. **Stable per-row V1 disposition ownership (S001-S097)** as the concrete A17 planning artifact.
4. **Migration dry-run/apply/readback/idempotency/crash semantics** and explicit handling of ambiguous concurrent legacy state.
5. **Staged L01-L05 execution at the earliest complete slice** with exact evidence reuse/invalidation rules.
6. **Target-side terminal package and stacked-workstream recovery detail** before destructive/auto-delete cleanup.

### 8.2 Strongest ideas from Plan B

The eventual canonical plan should preserve or import these ideas:

1. **Cleaner conceptual layer separation**, especially distinct review/recovery and Close/integration concerns even if they ultimately remain packages within fewer milestones.
2. **Explicit cumulative automated conformance gate** as a reusable suite rather than only scattered milestone evidence.
3. **Concise deferred-detail/JIT table** that makes implementation-owned decisions obvious.
4. **Challenge-audit questions** that explicitly test whether milestone order is still justified.
5. **Clean-build migration principle**: migration consumes established V2 semantics and never bootstraps the normal V2 architecture.

## 9. Overall judgment

### Scores

- **Plan A: 97/100**
- **Plan B: 92/100**

### Stronger candidate

**Plan A is stronger as a Strategic Plan under the frozen Definition.**

The decisive reasons are not its detail volume. They are the specific places where the detail prevents plausible implementation rework:

- it retires plugin/package feasibility risk early;
- it defines construction-state custody rather than leaving two-repository execution ownership implicit;
- it turns the frozen V1 matrix into exact row-level regression ownership;
- it gives migration explicit idempotency/interruption/rollback semantics;
- it advances real-surface evidence earlier;
- it closes more integration/recovery edge cases before Execution Prep.

Plan B remains a high-quality plan. It is not missing a Definition requirement and it has a very strong architecture/JIT/YAGNI structure. Its lower score reflects later risk retirement and several areas where execution would need to reconstruct strategic-operational contracts that A already supplies.

### Confidence

**High.**

The judgment is based on direct comparison of both complete candidate copies against the same frozen requirements, six accepted ADRs, full V1->V2 matrix, validation matrix, and Definition-complete handoff.

### Canonical-use recommendation

The stronger plan should **not necessarily be used completely unchanged**.

The best canonical result would use Plan A as the strategic base while materially importing Plan B's cleaner concern separation and concise JIT/deferred-detail framing. In particular, Plan A's broad M03/M04 packages should be decomposed during Execution Prep with B's review/recovery versus Close separation in mind, without changing the accepted milestone outcomes or creating speculative extra architecture.

The import is therefore structural/clarifying rather than a correction of missing Plan A Definition coverage.

## 10. Symmetry / frozen-authority verification

Reread check completed after drafting:

- both candidates were evaluated against the same frozen checkpoint 8055ed00acdb708c79919d470217fd87c920973a;
- the same ten rubric dimensions and equal weighting were applied to both;
- no model/runtime identity was inferred or used;
- no score was awarded for raw length, number of milestones, or number of tables;
- both candidates were credited for complete 76/76 requirement coverage and complete A01-A17/L01-L09 inclusion;
- differences called material are tied to implementation rework, recovery/cutover risk, or acceptance timing rather than presentation preference;
- presentation-only differences were not treated as strategic wins;
- no Independent Plan Review was performed;
- neither candidate nor canonical planning/workstream state was modified.
