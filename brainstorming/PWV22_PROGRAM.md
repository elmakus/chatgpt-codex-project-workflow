# PWv2.2 Program Brainstorming — Revision 20

Status: READY FOR DEFINITION
Scope subject: `pwv22-program@20`
Authority: exploratory only; not Definition

## 1. Goal

Explore and challenge the complete PWv2.2 program before any Definition promotion.

The Brainstorming must decide what PWv2.2 actually is, what belongs in its first canonical launch, what should remain optional/gated, what should be simplified or rejected, and how the final PWv2.1 predecessor changes those choices.

## 2. Owner decisions already fixed

- No PWv2.1.x releases.
- Former E/S candidates remain part of the PWv2.2 program rather than separate releases.
- F1-F4 remain PAUSED unless explicitly reauthorized.
- Research and Brainstorming semantics remain runtime-neutral; active realization is ChatGPT-hosted per OD-09.
- Research artifacts are prior-art evidence, not product authority.
- Final Definition requires explicit owner promotion of one exact Brainstorming revision.
- Final semantic choices that depend on PWv2.1 must be rebound to the exact terminal accepted PWv2.1 predecessor.

## 3. Required prior-art inputs

Research repository: `elmakus/project-research`

Primary retained inputs:
- `projects/chatgpt-codex-project-workflow/pwv2.2/research/incremental_adoption_orchestrated/FINAL_RECONCILIATION.md`
- `projects/chatgpt-codex-project-workflow/pwv2.2/research/incremental_adoption_orchestrated/OWNER_PROMOTION_MATRIX.md`
- `projects/chatgpt-codex-project-workflow/pwv2.2/research/simplification_review_formal/FINAL_SYNTHESIS.md`
- `projects/chatgpt-codex-project-workflow/pwv2.2/research/chatgpt_orchestration/OWNER_ORCHESTRATION_DECISIONS.md`

Existing consumer prior art:
- completed YAGNI/overengineering guard workstream on `main`;
- adaptive Brainstorming/grilling behavior already present on `main`.

## 4. Candidate inventory that must not disappear

Retain all reconciled candidate families and open evidence questions from the promotion ledger:
- FR-01 .. FR-19;
- F21-01 .. F21-06;
- RRE-01 .. RRE-02;
- former E/S sequencing/risk classes;
- C core;
- separately gated P/X/R/K;
- final-PWv2.1 rebind requirement.

Brainstorming may merge, split, rename, defer or reject candidates, but every ID needs an explicit disposition before challenge audit can become GREEN.

## 5. Initial thematic grilling map

### Theme A — What is the actual PWv2.2 product boundary?
- minimal native core;
- first-launch scope versus whole program scope;
- whether C/P/X/R/K remain the right decomposition;
- whether any category is missing or redundant.

### Theme B — State / identity / graph
- Work-DAG representation;
- READY/frontier authority;
- predecessor/dependency identity;
- Result publication identity;
- node-local material freshness;
- policy-package evolution;
- migration from final PWv2.1.

### Theme C — Execution / concurrency / effects
- bounded leaf execution and mechanical delegation;
- generalized multi-active mutation and fan-in;
- JIT/dependency semantics;
- external-effect UNKNOWN/readback/compensation;
- rollback and Recovery boundaries.

### Theme D — Review lifecycle
- review_and_repair_if_red realization;
- Reviewer attempt/evidence persistence;
- deterministic finalization;
- independence contamination;
- Plan Review versus implementation Review.

### Theme E — Runtime realization
- ChatGPT-hosted Research/Brainstorming;
- runtime-neutral handoff;
- non-ChatGPT receiver mutation qualification;
- provenance/diagnostics that remain non-authoritative;
- candidate-store physical backend need.

### Theme F — Planning simplification / YAGNI
- Planning-owned Simplification Review checkpoint from FR-19;
- mandatory every material Planning cycle versus conditional applicability;
- evidence inheritance;
- human-interaction-last;
- mid-execution simplification of only unstarted scope;
- preventing simplification machinery itself from becoming overengineering.

### Theme G — Adoption and launch
- exact first 2.2 launch scope;
- migration/cutover strategy;
- backwards compatibility;
- deferred-route mechanical impossibility;
- final-PWv2.1 rebind;
- release/rollback qualification.

## 6. Formal Brainstorming rules

- Adaptive grilling is intrinsic.
- Ask only genuine owner/product/strategy choices; agent-findable facts route to Research.
- Group multiple owner choices thematically and number them.
- Include the current recommendation and tradeoff for each choice.
- Continue while another round has material expected decision value.
- Substantive scope change increments this Brainstorming revision.
- Do not promote to Definition until challenge audit is GREEN and the exact revision receives explicit owner authorization.

## 7. Owner decisions captured in Revision 2

1. **Release model:** PWv2.2.0 ships the accepted safe/core launch scope; additional PWv2.2 capabilities may arrive later as PWv2.2.x. No PWv2.1.x release path is restored.
2. **P/X initial launch:** generalized mutating parallel/fan-in (P) and effect-bearing DAG paths (X) are not mandatory blockers for PWv2.2.0. They remain designed-for and separately gated capabilities.
3. **Simplification Review applicability:** every material Planning cycle gets the simplification/YAGNI review.
4. **Owner authority over simplification:** the review produces a concrete list of simplification candidates with explanation, tradeoffs and recommendation. It does **not** apply material simplifications automatically. The owner decides which proposed simplifications to accept or reject. Accepted choices then route through the normal authority path required by their semantic effect.
5. **R/K initial launch:** still OPEN pending explanation/grilling.

## 8. Revision-2 open decision register

Open:
1. whether R (non-ChatGPT canonical continuation) is required in PWv2.2.0;
2. whether K (production future-candidate physical storage) is required in PWv2.2.0;
3. whether the old E/S labels remain useful beyond sequencing/risk notation;
4. exact identity/graph/freshness architecture;
5. FR-08 placement relative to core;
6. whether P/X/R/K remain truly separable after final predecessor rebind;
7. exact representation/output contract for always-on Simplification Review;
8. evidence inheritance scope;
9. receiver/runtime qualification details;
10. candidate-store necessity/backend;
11. migration/cutover model;
12. what to simplify or reject from FR-01..FR-19;
13. any owner decision surfaced by further grilling.

## 9. Current challenge status

`PENDING`.

Revision 2 has fixed the release model, P/X day-one non-blocking status, and always-on owner-controlled Simplification Review. R/K and the remaining architecture/product choices continue through adaptive grilling.


## 10. Owner decisions captured in Revision 3

1. **R and K retention:** R and K are not blockers for PWv2.2.0, but both remain mandatory durable PWv2.2.x backlog capabilities. They may not disappear during Definition/Planning. R remains gated by RRE-02; K remains gated by RRE-01.
2. **E/S labels:** accepted recommendation — retire E/S as top-level architecture/release-phase names. Preserve them only where useful as internal sequencing/risk history/classification.
3. **FR-08:** accepted recommendation — target Reviewer-owned append-only exact attempt/evidence persistence with deterministic finalization, subject to exact eligibility/freshness/CAS/readback and final-PWv2.1 Review-identity rebind.
4. **Core model:** accepted recommendation — PWv2.2 is identity/freshness/guarded-transition centric; Work-DAG/readiness is built on top of those canonical facts rather than being treated as the sole conceptual center.
5. **R product intent:** still OPEN because owner requested a concrete explanation before deciding whether Pi/Paseo should eventually become an autonomous canonical writer.
6. **K implementation choice:** still OPEN; special production candidate store is deferred. Brainstorming must compare Git-native candidate isolation first and only retain a dedicated backend if a real requirement cannot be met otherwise.

### Anti-forgetting invariant

Before Brainstorming can become GREEN/ready_for_definition:
- R/FR-09/RRE-02 must have an explicit disposition;
- K/FR-11/RRE-01 must have an explicit disposition;
- if either is deferred beyond 2.2.0, Definition/Planning must retain a durable post-2.2.0 delivery/gate obligation or explicitly reject it by owner decision;
- neither may disappear merely because it is outside first-launch scope.


## 11. Owner decisions captured in Revision 4

1. **R is required in PWv2.2.0.** Cross-runtime Project Workflow continuation is existing expected product behavior and must not regress in PWv2.2. The R boundary is therefore reinterpreted as a release-critical qualification of existing cross-runtime canonical continuation under the new PWv2.2 identity/freshness model, not as a later optional feature. RRE-02 remains the proof obligation that receivers refetch, bind the exact current subject, and do not continue from stale handoff/session state.
2. **K dedicated candidate store is rejected.** No separate production candidate-store backend is desired. Candidate isolation/publication must use Git-native mechanisms where needed. FR-11/K as a dedicated physical backend is rejected unless a future explicit owner decision reopens it in response to a concrete unmet requirement.
3. **FR-10 may remain only as Git-native logical/isolated candidate mechanics.** Any candidate/candidate-builder semantics must not introduce a second non-Git authority or truth store.
4. **Simplification Review disposition:** accepted recommendation — every material finding must receive explicit owner disposition before plan freeze; the review presents candidate, rationale, tradeoff and recommendation, while the owner chooses accept/reject. The review itself never silently applies material simplifications.
5. **FR-08:** accepted recommendation — include Reviewer-owned append-only attempt/evidence persistence plus deterministic finalization in PWv2.2.0, subject to final-PWv2.1 Review identity rebind and exact freshness/CAS/readback qualification.
6. **READY:** accepted recommendation — READY/frontier is derived from canonical graph/dependency/Result/gate facts and is not an independently mutable canonical truth.
7. **Core architecture remains:** identity + freshness + guarded transitions are foundational; graph/readiness is derived on top.

### R anti-regression requirement

PWv2.2 release qualification must include explicit cross-runtime compatibility/continuation acceptance. A runtime that is an accepted PW host before PWv2.2 must not lose the ability to start/recover/continue a managed workstream merely because the 2.2 state model changes. Any narrower runtime support must be an explicit product decision, not an accidental migration effect.

### K disposition

Current disposition:
- special candidate backend/store: REJECTED;
- Git-native branches/refs/isolated commits/candidate build mechanics: ALLOWED when needed;
- non-Git canonical or shadow truth store: FORBIDDEN without a new explicit owner decision.


## 12. Owner decisions captured in Revision 5

1. **Result identity:** canonical consumed Result identity is exact repository + commit + path + blob, not merely Card ID/status or mutable path.
2. **Dependency binding:** downstream dependency means consumption of an exact accepted predecessor Result, not merely predecessor DONE.
3. **Material freshness:** freshness is node/input-local and derived from the exact authority/Result/material inputs that matter to the Card. Global Task Board revision may protect writes/CAS but is not universal semantic freshness.
4. **2.1 -> 2.2 migration:** compatible reading during migration is allowed, but canonical mutation uses one atomic cutover; no dual canonical writers.
5. **Policy-package evolution / FR-17:** remains OPEN for YAGNI challenge. Owner questions whether explicit package provenance is necessary when an LLM can interpret the current workflow. Brainstorming must distinguish the minimum durable compatibility fact needed for deterministic cross-version recovery from unnecessary per-fact/version bookkeeping.


## 13. Owner decisions captured in Revision 6

1. **Policy-package evolution / FR-17:** use the minimal semantic migration rule. Do not version-tag every durable fact. When a workflow update materially changes the meaning/validity of existing state, the new workflow must classify affected historical state as preserve / revalidate / stale / Recovery.
2. **Work-DAG representation:** canonical graph storage keeps only minimal direct dependency facts. READY/frontier/reachability and other graph projections are derived, not separately mutable truth.
3. **JIT Cards:** do not create speculative placeholder Cards when a stable Card contract depends on a predecessor result. Keep a bounded JIT obligation and materialize the Card only once its contract is knowable.
4. **External-effect uncertainty:** ambiguous non-idempotent effects use UNKNOWN -> required exact external readback -> only then retry / accept / compensate. Blind retry is forbidden.
5. **RED repair closure:** the original reviewer may perform bounded verification of its specific RED findings, but final full-scope closure after repair requires a fresh independent reviewer.


## 14. Owner decisions captured in Revision 7

1. **PWv2.2.0 parallelism anti-regression:** preserve at least the accepted PWv2.1 model: Plan/JIT-authorized finite parallel-safe Card sets, one primary mutating Worker per Card, serialized overlapping write scopes, stale-result handling, and integrated compatibility before downstream consumption of multiple sibling Results.
2. **Concurrent overlapping mutation:** do not add an override allowing two workers to mutate the same write scope concurrently.
3. **External-effect paths:** every PWv2.2.0 path that can cause real external mutation follows intent -> attempt -> readback -> known result; uncertainty becomes UNKNOWN and blind retry is forbidden.
4. **Required release hosts:** PWv2.2.0 acceptance is required on ChatGPT and Pi/Paseo. Codex is not a release-blocking host.
5. **Simplification Review owner surface:** before Planning freeze, present each material simplification candidate with proposed simplification, rationale, risk/tradeoff, recommendation, and explicit owner disposition. No material simplification is applied without owner accept/reject.
6. **Canonical mutation discipline:** canonical workflow-state transitions use exact-old-state comparison/CAS semantics plus target-side readback; concurrent change causes refetch/re-evaluation rather than overwrite.
7. **Runtime provenance:** runtime/model/provider provenance may be retained diagnostically but must not affect transition legality, freshness, routing, or review eligibility.
8. **Research orchestration:** Main/coordinator owns research questions, lane decomposition, synthesis and return routing. Workers may gather bounded evidence but do not make product/owner decisions.
9. **Brainstorming delegation:** subagents may gather facts, red-team options and prepare alternatives, but they cannot close owner decisions or promote scope into Definition.
10. **Final PWv2.1 rebind:** Brainstorming proceeds now; after PWv2.1 reaches its terminal accepted state, perform one source-bound revalidation against that exact predecessor. Reopen only decisions materially affected by the final predecessor, then allow Definition promotion.
11. **Owner-facing terminology:** use descriptive capability names rather than internal one-letter research labels.


## 15. Owner decisions captured in Revision 8

1. **Distributed semantic owners:** keep multiple small canonical records with bounded semantic ownership; do not collapse the workflow into one global STATE file or universal event ledger.
2. **Task Board ownership:** after implementation state exists, Task Board owns current Card execution state only. It does not absorb Brainstorming, Definition, Planning, or other pre-execution semantic owners.
3. **Result history:** Card Results are immutable historical artifacts. Re-execution/repair creates a new Result; the current Card binds the exact accepted Result without overwriting earlier results.
4. **Review history:** review attempts are append-only. RED/GREEN/recheck attempts remain durable; deterministic finalization identifies the terminal accepted attempt for the exact subject without rewriting prior attempts.
5. **Human-interaction-last ownership:** Planning plus Simplification Review identifies and defers human-interactive work as far as dependencies safely allow; Execution Prep/JIT materializes exact Cards/dependencies/timing. No separate Human Interaction workflow stage is introduced.


## 16. Owner decisions captured in Revision 9

1. **Worker scope discipline:** a worker may report discovered follow-on work but cannot self-authorize a new sibling/successor/JIT obligation outside its assigned scope.
2. **Automatic bounded repair after RED:** repair may start automatically when it stays inside the already-authorized Card scope/requirements/strategy. Owner input is required only when repair needs new scope, requirements, strategy, or authority.
3. **Review cannot expand authority:** a reviewer may identify out-of-scope repair needs but cannot authorize them; routing returns to Execution Prep, Planning, Definition, or another proper owner as required.
4. **Mechanical clean merge:** orchestrator may automatically harvest, clean-merge, test, and read back compatible independent results when there is no semantic conflict or overlapping mutation scope.
5. **Context Compiler:** optional acceleration only; PWv2.2.0 correctness must not depend on it.
6. **Shared CAS/readback mechanics:** use common mechanical helpers for expected-old comparison, guarded write, and target-side readback where practical; helpers do not own semantic transition choice.
7. **Git-native candidate publication:** multi-file canonical changes may be assembled and validated as isolated Git commits/refs before atomic/promotional publication. No separate candidate store is introduced.
8. **Simplification rejection memory:** an owner-rejected simplification for an exact unchanged plan/evidence subject remains dispositioned and is not repeatedly re-asked unless relevant plan/evidence changes.
9. **Human interaction batching:** preserve distinct Cards/authorities but optimize sequencing to minimize attended sessions, grouping compatible login/OTP/pairing/manual-smoke work where dependencies permit.
10. **Mid-execution simplification:** completed or active work is not rewritten merely for simplification. Accepted durable evidence may trigger simplification proposals for unstarted future scope, and the owner explicitly accepts/rejects material removal.


## 17. Owner decisions captured in Revision 10

1. **Plan freeze identity:** a frozen Planning subject is bound to exact repository + commit + path + blob so downstream review cannot silently drift onto edited content.
2. **Material change after freeze:** any material plan change returns to Planning, creates a new exact subject, and reruns the applicable Simplification Review plus Plan Review before execution authority resumes.
3. **Deterministic review finalizer:** the finalizer is intentionally non-semantic; it validates exact subject, reviewer eligibility, terminal verdict, required evidence/readback and other formal closure conditions, but does not reinterpret review prose.
4. **Projection/cache disagreement:** stale or divergent Context Compiler/shadow index/cached READY data is discarded and rebuilt from canonical state; cache disagreement alone is not Recovery.
5. **Evidence reuse:** workflow should propose reuse when prior evidence proves the same property for an unchanged relevant subject/environment and all invalidators are ruled out; ambiguity fails closed to a fresh test.
6. **Cheap rerun preference:** if proving reuse equivalence is more complex or less reliable than rerunning the test, rerun the test.
7. **Migration rehearsal:** before PWv2.2 canonical cutover, perform a full rehearsal against an exact copy of terminal PWv2.1 state, including crash/restart/readback paths.
8. **Rollback after cutover:** if post-publication acceptance fails before irreversible external effects make rollback unsafe, restore the exact previous Git state/ref rather than patching a partially migrated canonical state in place.
9. **Cross-host compatibility:** ChatGPT and Pi/Paseo must pass the same canonical behavioral acceptance fixtures; implementation/runtime internals may differ.
10. **Brainstorming completion challenge:** before ready_for_definition, run one final whole-scope challenge focused on YAGNI/removals, missing requirements, contradictions, unnecessary mechanisms and forgotten retained obligations.


## 18. Owner decisions captured in Revision 11

1. **Definition scope:** Definition owns product guarantees, requirements and accepted decisions only; implementation ordering, milestones and Cards remain Planning concerns.
2. **Definition completeness:** Definition reaches GREEN only when every retained Brainstorming capability/obligation has an explicit disposition such as required / deferred / rejected / already satisfied.
3. **Deferred obligations remain durable:** capabilities intentionally deferred beyond PWv2.2.0 remain explicit Definition obligations with their delivery condition/gate; omission is not an allowed form of deferral.
4. **Planning cannot delete product scope:** Planning may decompose and sequence accepted requirements but cannot independently remove or weaken them; material product-scope change returns to Definition/owner authority.
5. **Plan Review role:** Plan Review checks correctness, completeness, Definition alignment, dependencies, rollback/recovery and plan binding; it does not repeat the full Simplification Review.
6. **Execution Prep authority:** Execution Prep/JIT may resolve bounded implementation detail that does not change accepted strategy, outcome, requirement, or gate.
7. **Return to Planning:** changes to strategy, milestone ordering, migration approach, material dependency structure, acceptance gates or equivalent planning semantics return to Planning.
8. **Return to Definition:** changes to product requirements or accepted guarantees return to Definition and require owner authority.
9. **Shared acceptance fixtures:** core PWv2.2 semantics are expressed as common behavioral fixtures/contracts that required hosts must satisfy independently of runtime implementation details.
10. **Release-blocker threshold:** PWv2.2.0 release blockers are violations of canonical semantics, migration/recovery, required cross-host acceptance and other MUST guarantees; noncritical UX/diagnostic defects may be deferred.


## 19. Owner decisions captured in Revision 12

1. Active PWv2.1 workstreams migrate to PWv2.2 before their next canonical mutation.
2. New managed work after PWv2.2.0 starts natively in PWv2.2.
3. PWv2.2 reads/recovers supported PWv2.1 state; reverse compatibility is not required.
4. Canonical schema identity stays minimal: only enough for deterministic parsing, compatibility and migration.
5. Unsupported mandatory semantics fail closed rather than being ignored.
6. Multi-file canonical changes are built and validated Git-native, then published by one guarded ref update/CAS plus readback.
7. Unpublished commits/refs/worktrees are noncanonical and may be cleaned after deterministic readback confirms they are not authoritative.
8. Every official PWv2.2 release has an exact Git commit/tag identity with its policy package, tests and migration tooling.
9. A PWv2.2.x semantic change affecting existing state must define preserve / revalidate / stale / Recovery behavior.
10. Required release hosts are ChatGPT and Pi/Paseo; Codex remains non-blocking unless explicitly restored.

11. Upgrade of an active project occurs only at a quiescent boundary; never mid-mutation or mid-Card.
12. There is no normal automatic downgrade from PWv2.2 to PWv2.1. Emergency rollback restores the exact pre-cutover state under its bounded rollback procedure.
13. PWv2.2.0 uses an exact release candidate. ChatGPT + Pi/Paseo acceptance and migration rehearsal run against that immutable candidate; any candidate change creates a new candidate and requires renewed acceptance.
14. Release-candidate/beta status belongs to the workflow package/release process, not to every project/workstream canonical state.
15. Recovery first derives durable facts and deterministic legal continuation options; owner input is requested only when a genuine owner choice remains.
16. Purely mechanical recoverable drift may be repaired automatically with readback when no semantic decision changes.
17. Acceptance focuses on shared semantic fixtures per required host rather than a host x model x feature combinatorial matrix; model identity is not canonical.
18. Host-specific acceptance is added only for host-specific realization boundaries such as filesystem/Git integration.
19. Stable release may carry dispositioned non-blocking warnings/deferred items once all MUST semantics and required acceptance are GREEN.
20. If one legal next obligation is deterministically derivable and no owner/human stop is due, ChatGPT or Pi/Paseo continues automatically rather than asking for redundant permission.


## 20. Owner decisions captured in Revision 13

1. **Automatic continuation exception — Premium A/B/C are mandatory user-facing stops.** Automatic continuation must never cross Premium A, B, or C. Premium A stops before material Planning and offers the choice to continue in the current context or move to a best-available model/context. Premium B stops after exact plan freeze and requires a fresh independent best-available context/harness for Plan Review; the planner/orchestrator must not silently delegate this review to an arbitrary cheap worker. Premium C stops after GREEN Plan Review and offers the choice to continue or move to a lighter/cheaper context for Execution Prep. These stops remain required even when no other product/owner decision is pending.
2. **User-stop quality:** every real user stop states what completed/was found, what it means for durable state, the exact action required, available options when applicable, and a recommendation.
3. **Local invalidation:** changing a Result/input invalidates only Cards/Results whose material freshness actually depends on that exact input, rather than invalidating unrelated downstream work by default.
4. **Bounded revalidation:** when a stale result can be deterministically revalidated against a limited changed input without fresh execution, bounded revalidation is allowed unless accepted authority explicitly requires rerun.
5. **Review-attempt binding:** every review attempt binds the exact reviewed subject/Result; a GREEN verdict for an older Result cannot authorize a repaired/new Result.
6. **Git-native cleanup:** noncanonical candidate refs/worktrees/commits may be cleaned automatically after deterministic proof that canonical state and required rollback/recovery no longer reference them.
7. **Managed-change branch lifecycle:** each managed change keeps its branch through formal Close; branch deletion occurs only after integration/readback is confirmed and required durable history is preserved in the integration target.
8. **Mechanical Close:** when all required results/reviews/integration/readback are GREEN and no human/owner boundary remains, Close may proceed automatically. A user stop remains required only for a real accepted boundary or external/irreversible choice.
9. **Deferred capability visibility:** PWv2.2.x obligations deferred from 2.2.0 remain durably visible until implemented or explicitly rejected by owner authority.
10. **Brainstorming completion rule:** do not continue asking questions merely to extend the process. Before ready_for_definition, run a whole-scope challenge for contradictions, missing requirements, overengineering, duplicate mechanisms, forgotten obligations and simplification opportunities; only material unresolved findings generate another owner-question round.


## 21. Owner decisions captured in Revision 14

1. Premium B remains a mandatory user-facing stop and explicitly signals that a stronger/fresher reviewer may improve assurance.
2. Reviewer quality is a recommendation, not a hard model gate. Canonical requirements are semantic independence from the plan author/repairer and review of the exact frozen subject.
3. In ChatGPT, Premium B provides a fresh-session locator for a new independent chat/context.
4. In Pi/Paseo, after the stop the owner may either move to a new session or explicitly continue; Pi/Paseo may then dispatch its configured independent review worker on its assigned model.
5. Owner-authorized continuation with a lower-cost reviewer is allowed after the stop; the workflow communicates the assurance tradeoff but does not block it.
6. Review remains non-mutating. The main quality risk from a weaker reviewer is false GREEN or missed defects, not modification of the frozen plan.
7. Premium A/C and all previously accepted Revision 13 decisions remain accepted.
8. Handoff remains locator-only and runtime-neutral.
9. Canonical state does not persist current host/model identity.
10. Workflow authority uses the current default branch operationally, with exact commit identity only where release/migration/evidence subjects require it.
11. Semantic workflow updates affecting active durable state use preserve / revalidate / stale / Recovery handling rather than silently reinterpreting prior state.
12. Credentials, tokens, OTPs and secrets never become canonical workflow state.
13. External-effect evidence records only non-secret operation/resource/readback identifiers needed for recovery.
14. Managed-change completion remains integration -> target-side readback -> durable confirmation -> Close/cleanup.


## 22. Owner decisions captured in Revision 15

1. Premium A recommends the best available planning model/context but does not hard-gate a specific model; after the stop the owner may explicitly continue on the current Pi/Paseo Main.
2. Premium C similarly recommends a lighter/cheaper execution-prep context without forcing a model switch.
3. Reviewer independence does not require a different model; a fresh independent context/worker on the same model is valid if it did not author or repair the subject.
4. Pi/Paseo review realization needs semantic independence, exact frozen-subject binding, and non-mutation of the plan; canonical worker/model identity is unnecessary.
5. Final full-scope review after repair may use any fresh independent Pi/Paseo worker; higher-quality models improve assurance but are not canonical requirements.
6. Owner choice may lower reviewer model quality after the Premium B stop, but may not waive semantic independence.
7. Preserve bounded editorial_exempt handling for truly non-material post-review corrections with no strategy/milestone/coverage/gate change.
8. Simplification Review precedes exact plan freeze: planner audit -> Simplification Review -> owner dispositions -> freeze -> Premium B.
9. Owner rejection of all simplification candidates leaves the plan eligible to freeze unchanged.
10. Simplification Review requires owner disposition only for material simplifications; trivial cosmetic/mechanical cleanup may remain planner-owned.
11. Planning may reorder human-interactive Cards later to batch attended work when dependencies/gates remain valid.
12. Do not merge semantically distinct risky human actions into one mega-Card merely for convenience.
13. External mutations should use idempotency/request identifiers when supported by the target system.
14. An ambiguous irreversible external effect with no reliable readback fails closed; blind retry is forbidden.
15. PWv2.2 is host-neutral. ChatGPT and Pi/Paseo are required realizations, replacing product-level ChatGPT-only semantics.
16. Required hosts may implement different orchestration mechanics but consume the same canonical workflow authority.
17. Pi/Paseo may automatically spawn authorized research/review/execution workers without per-worker owner approval; real owner/Premium/human stops still apply.
18. Leaf workers do not autonomously spawn new workflow orchestration outside their assigned scope.
19. Each semantic PWv2.2.x release reruns common core acceptance on required hosts; documentation/cosmetic-only releases do not require the full semantic matrix.
20. After this owner-question round and one additional requested round, Brainstorming proceeds to the previously accepted whole-scope challenge instead of generating questions indefinitely.
21. **Worker lifecycle cleanup:** runtime workers are scoped to a concrete Card/attempt/role. Once that obligation reaches a terminal state and no accepted plan explicitly requires reuse of that same worker, Pi/Paseo closes/releases the worker before moving on. New Cards use fresh appropriately assigned workers. Terminal or abandoned workers must not accumulate as zombie runtime capacity; cleanup is automatic and noncanonical. ChatGPT realization may have nothing explicit to close.


## 23. Owner decisions captured in Revision 16

1. **Worker means all runtime subagents.** Executor, repair, reviewer, tester, research lane, synthesis/helper and equivalent runtime subagents are all subject to the same lifecycle principle: when their bounded obligation is terminal and no accepted active obligation requires them, Pi/Paseo closes/releases them automatically. New Cards/attempts normally use fresh workers.
2. **Worker lifecycle is runtime-local.** Capacity, worker slots, session handles, shutdown mechanics and reuse implementation are runtime concerns, not canonical Project Workflow state.
3. **Runtime cleanup before capacity blocker.** Pi/Paseo should reclaim terminal/stale/abandoned subagents before reporting worker-capacity exhaustion.
4. **No durable worker/session affinity.** Canonical workflow binds semantic roles/obligations, not worker UUIDs, sessions or concrete models. Runtime restart may reconstruct needed workers from durable state.
5. **Late or stale worker output lacks authority.** Output arriving after cancellation/supersession/authority loss may be retained diagnostically but cannot become canonical Result without current legal authority.
6. **Fresh independent review requires a fresh qualifying review context/worker, not persistence of an old runtime worker.**
7. **Research/synthesis workers follow the same cleanup discipline.**
8. **Runtime scheduling never relaxes semantic authority, dependency, independence or Premium-stop rules.**
9. **Project Workflow is a semantic contract: primarily specify what Main/coordinator must guarantee, not how a particular runtime implements it.** A capable Main/runtime owns orchestration mechanics, worker lifecycle, capacity management, session topology, tool selection and other realization details unless a mechanism is itself necessary to preserve a workflow invariant.
10. **Mechanism-admission rule:** prescriptive implementation mechanics belong in canonical Project Workflow only when removing that prescription would make an accepted semantic invariant ambiguous, non-deterministic, unsafe, non-recoverable or non-portable. Otherwise implementation detail stays in runtime-specific adapters/configuration/tooling.
11. All twenty recommendations from the preceding worker-lifecycle round are accepted, including terminal worker cleanup, no canonical worker registry, bounded same-Card reuse, fresh final reviewers, cleanup on fan-in, cancellation of superseded work, authority recheck before mutation, and runtime-local capacity handling.


## 24. Revision 17 whole-scope challenge — semantic contract versus runtime realization

Challenge status: material findings found; owner decisions still required before GREEN.

### 24.1 Top-level finding

PWv2.2 should treat Project Workflow as a semantic obligation/authority/recovery contract. Runtime topology and realization mechanics belong to ChatGPT or Pi/Paseo unless a concrete mechanism is necessary to make a semantic invariant deterministic, portable, safe or recoverable.

Live canonical V2 already substantially follows this boundary. The main over-prescription risk is inherited PWv2.1 consumer requirements that encode worker/session/transport/retry/model or implementation-style choices.

### 24.2 FR-01..FR-19 challenge disposition

- **FR-01:** retain bounded delegation, no self-authorized sibling/successor/JIT work and non-authoritative worker output; do not require a universal runtime assignment/result envelope beyond the semantic Card/Result contract.
- **FR-02:** retain legality-before-concurrency and semantic-conflict return to Main; harvest/merge/scheduling realization is runtime-owned.
- **FR-03:** retain Main-owned Research/Brainstorming semantics but supersede ChatGPT-only realization. PWv2.2 is host-neutral with ChatGPT and Pi/Paseo required realizations.
- **FR-04a:** fold review-and-repair choreography into ordinary Review/repair semantics; do not retain it as a separate named PW capability.
- **FR-04b:** reject new assignment-internal canonical authorization unless a later concrete semantic requirement proves it necessary.
- **FR-05:** diagnostic actor/runtime provenance is optional runtime telemetry, not a canonical PWv2.2 feature.
- **FR-06:** Context Compiler, trace index, shadow DAG/frontier and similar projections are optional disposable runtime optimizations, not release requirements or authority.
- **FR-07:** retain guarded expected-old mutation plus mandatory readback as semantic law; generic helper/candidate-builder implementation is tooling/runtime realization.
- **FR-08:** retain in PWv2.2.0: append-only exact Review attempts/evidence plus deterministic non-semantic finalization, rebound to final PWv2.1 Review identity.
- **FR-09:** retain in PWv2.2.0 as receiver freshness/continuation guarantees for required hosts ChatGPT and Pi/Paseo; exact attestation/transport mechanics are runtime/acceptance realization.
- **FR-10:** collapse into Git-native atomic publication/migration mechanics where needed; no standalone future-candidate product/state model.
- **FR-11:** reject dedicated physical candidate backend/store.
- **FR-12:** retain core exact Result/dependency identity plus node/material-input-local freshness. Exact representation is a Definition/Planning/implementation choice after final PWv2.1 rebind, constrained by accepted semantic invariants.
- **FR-13:** retain minimal direct dependency/Result-binding facts and derived readiness. Do not introduce a separately authoritative Work-DAG subsystem or persisted READY/frontier authority.
- **FR-14:** retain atomic PWv2.1 -> PWv2.2 migration/publication/readback guarantees; tooling mechanics are implementation-owned.
- **FR-15:** PWv2.2.0 must preserve accepted PWv2.1 bounded parallel-safe Card semantics. Generalization beyond that is deferred and separately gated.
- **FR-16:** external-effect intent/attempt/readback/UNKNOWN safety is universal semantic law. Additional new effect-bearing DAG/JIT/fan-in capability is deferred unless later explicitly required.
- **FR-17:** retain minimal semantic-evolution rule: affected historical state is preserve / revalidate / stale / Recovery; avoid pervasive package/version metadata.
- **FR-18:** reject runtime/session/provider identity as canonical semantic identity.
- **FR-19:** retain mandatory Planning-owned Simplification Review for each material Planning cycle, with material owner dispositions before freeze and no new top-level workflow stage.

### 24.3 Research-blocker disposition

- **F21-01:** exact READY migration/subordination representation is not an owner product choice; choose the minimum technical representation that leaves one derived readiness authority.
- **F21-02:** exact predecessor primitive is not an owner product choice once exact consumed Result binding is guaranteed.
- **F21-03:** exact fan-in compatibility representation is a technical choice subject to the existing bounded-parallel anti-regression contract; broader fan-in remains deferred.
- **F21-04:** owner-level Result identity is fixed as repository + commit + path + blob; publication encoding is technical.
- **F21-05:** owner-level freshness law is fixed as material-input-local; exact fingerprint/read-set encoding is technical.
- **F21-06:** owner-level external-effect law is fixed as intent/attempt/readback/UNKNOWN/no-blind-retry; exact record schema is technical.
- **RRE-01:** closed with rejection of a dedicated candidate backend.
- **RRE-02:** remains release-critical acceptance evidence for ChatGPT + Pi/Paseo.

### 24.4 Superseded research assumptions

- ChatGPT-only Research/Brainstorming realization is superseded by the later host-neutral owner decision.
- A dedicated candidate backend is superseded/rejected.
- The original research idea that generalized parallelism could be absent from 2.2.0 is narrowed: generalized expansion may be deferred, but already-accepted PWv2.1 bounded parallelism may not regress.
- Premium-B best-available-model language is advisory quality guidance; semantic independence and exact-subject review remain mandatory.

### 24.5 Remaining material owner questions

The challenge found a small set of inherited PWv2.1 requirements whose placement in canonical PW versus runtime realization materially affects PWv2.2 scope. These require owner disposition before challenge GREEN.


## 25. Owner decisions captured in Revision 18

1. **Worker cleanup remains an explicit semantic expectation, implementation is runtime-owned.** When subagents are no longer needed for the current Card/attempt/role, the runtime must release/close them before accumulating stale capacity; how Pi/Paseo implements shutdown/reaping is outside Project Workflow.
2. **Mutating ownership:** one Card has one mutating ownership domain. Runtime-internal helpers may exist, but competing independent mutating owners for the same Card are forbidden. Genuine independent mutation belongs in separate Cards.
3. **Recursive subagent mechanics:** Project Workflow does not prescribe whether a runtime technically exposes nested subagent spawn. Canonical law only forbids a subagent from self-authorizing new PW Cards, scope, siblings, successors or authority. Pi/Paseo may disable nested spawn entirely as runtime configuration.
4. **Review convergence ceilings remain canonical PW semantics.** Keep the accepted PWv2.1 discovery/repair ceilings and convergence routing because they define when ordinary repair/re-review must stop and Main/root-cause analysis or broader routing becomes mandatory; these are workflow-control semantics, not worker implementation mechanics.
5. **Execution Obligation/Result serialization remains OPEN for final disposition.**
6. **Falsification-first/test-first placement remains OPEN for final disposition.**


## 26. Owner decisions captured in Revision 19

1. **Execution Obligation / Execution Result interchange:** retain one common typed transport-neutral contract with JSON as the standard portable interchange serialization across supported hosts. A runtime may use RPC, native objects, text, internal APIs or other mechanisms internally, but portable exchange/acceptance must be representable in the shared JSON contract.
2. **Falsification-first / test-first discipline:** retain the accepted PWv2.1 rule as SHOULD, not MUST. When an accepted Card outcome can be meaningfully expressed as an automated or observable failing check, implementation should prove the failing condition first and then make the minimum change required to reach GREEN. Cards where that shape is artificial or inapplicable are not illegal merely for using another execution approach.

## 27. Whole-scope challenge closure

Challenge result: **GREEN**.

The whole-scope review covered:
- FR-01 through FR-19;
- F21-01 through F21-06;
- RRE-01 and RRE-02;
- retained PWv2.1 bounded parallelism and review-convergence semantics;
- ChatGPT and Pi/Paseo host requirements;
- Premium A/B/C stops;
- worker/subagent lifecycle and cleanup;
- Result/review identity and material freshness;
- migration, release, rollback and recovery;
- external-effect UNKNOWN/readback safety;
- Simplification Review/YAGNI;
- separation of canonical semantic law from runtime realization mechanics.

No further material owner/product questions remain at this Brainstorming revision.

The resulting design principle is:
- Project Workflow specifies semantic obligations, authority, invariants, evidence, acceptance, transition legality, recovery and owner boundaries;
- capable runtimes own orchestration mechanics, worker/session lifecycle, scheduling, capacity, tool selection and other realization details unless a specific mechanism is required to preserve a semantic invariant;
- runtime implementation choices must not become hidden authority.

Final PWv2.1 predecessor rebind/revalidation remains mandatory before Definition is allowed to finalize any representation choice or implementation plan that depends on the terminal PWv2.1 contract. The rebind reopens only decisions materially affected by the final predecessor.

Revision 19 is ready for Definition promotion, but promotion still requires explicit owner authorization for the exact subject pwv22-program@19.


## 28. Owner decisions captured in Revision 20 — deferred defects and final qualification

Evidence basis:
- integrated formal research: `elmakus/project-research:projects/chatgpt-codex-project-workflow/pwv2.2/research/deferred_defects_final_qualification/FINAL_SYNTHESIS.md`;
- validated orchestration experiment: `elmakus/project-research:experiments/identical-multilane-v1/RESULT.md`;
- owner decisions in the continuation discussion after consuming that research.

1. **Review verdicts remain binary.** Canonical independent Review verdicts remain `GREEN` or `RED`; there is no `CONDITIONAL_GREEN`, provisional-green or third acceptance verdict.
2. **Deferred findings are orthogonal durable obligations.** A known finding may remain open only when the exact current acceptance still remains true and the defective property is positively proven irrelevant to all authorized work before its repair boundary. The finding remains durable and visible with exact affected subject/scope, blocking scope, release relevance, latest-safe repair boundary and closure evidence.
3. **DONE remains truthful.** If a finding does not falsify a Card's exact acceptance, that Card may still reach ordinary GREEN/DONE while the separate finding remains open. If a finding falsifies the Card's exact acceptance, the Card may not be marked DONE merely to preserve throughput.
4. **Blocking is dependency-local, not automatically workstream-global.** A non-accepted Card blocks only work whose accepted dependency/acceptance surface actually requires the defective property/Result. Unaffected independent Cards may continue. Unknown impact fails closed.
5. **Repair timing is bounded by need.** A deferred defect must be repaired at the earlier of: (a) the first authorized downstream consumption that requires the defective property/acceptance, or (b) its exact latest-safe repair boundary, which cannot be later than final qualification/release gating for a current-release defect.
6. **Post-repair impact is material-local.** After repair, preserve immutable historical Results/Review attempts and classify affected downstream surfaces as preserve / revalidate / stale / Recovery. Revalidate unchanged implementation/output rather than fabricating a new Result; create a new Result only for genuinely changed/re-executed result-producing work.
7. **Final Qualification is standard Project Workflow behavior.** Every PW-managed change uses the final-qualification obligation family before release/Close, with proportional execution cost but without an opt-out merely because the change is small:
   - Final Qualification Handoff real stop;
   - Known Defect Cleanup (zero-work when no deferred findings exist);
   - Targeted Bug Hunt using risk/coverage-driven independent prompts;
   - Global identical-prompt Bug Hunt using an owner-selected number of fresh isolated runs;
   - integrated finding classification/deduplication and bounded repair;
   - post-repair material-local impact/revalidation when repairs occurred;
   - fresh eligible independent full-scope final acceptance on the exact final subject;
   - release/publication/readback/Close continuation under ordinary authority.
8. **No acceptance by swarm count.** Targeted/Global hunts are defect-discovery mechanisms. Zero findings, duplicate findings, majority agreement or any fixed worker count never substitutes for exact final acceptance.
9. **Final Qualification Handoff is mandatory.** The handoff before Known Defect Cleanup is a standard real user-facing stop and uses the existing exact-obligation/locator-only handoff primitive rather than introducing a new lifecycle stage.
10. **Repair swarms use parallel repair with serial candidate integration.** Independent repair units may execute in parallel only under explicit finite accepted admission with write/semantic/effect conflict classification. One integration owner mutates/composes the shared candidate deterministically; workers do not self-merge or self-accept.
11. **Orchestration mechanics are non-authoritative.** Chat/worker counts, models/providers, branch allocators, `finite_branch_claim`, `NEXT_RUN_ID`, prompt-launch mechanics and worker/session identity remain coordinator/runtime details.
12. **P1 is superseded if this revision is promoted.** The current approved P1 cannot proceed through Premium C because it predates these material semantics and explicitly schedules mutating PWv2.2 program Cards serially. A promoted Definition R5 requires a new Planning P2 and fresh applicable Planning review/gates before Execution Prep.
13. **PWv2.1 donor boundary remains separate.** PWv2.2 Definition/Planning may proceed, but Initial Execution Prep remains held until the separately authorized PWv2.1 pre-M03 donor boundary is complete. PWv2.1 M03 is not authorized by this decision.

## 29. Revision 20 whole-scope challenge closure

Challenge result: **GREEN**.

The integrated 15-lane formal research independently challenged acceptance-state representation, safe deferral, dependency freshness, defect classification, review topology, targeted/global bug hunts, repair swarms, post-repair revalidation, handoff UX, release/Close, concurrency/integration, YAGNI and identical heterogeneous launch mechanics. The integration preserved material dissent and identified the research-base packaging provenance defect; that defect did not change the common frozen consumer/P1 analysis subject and has since been addressed operationally by one-source manifest/branch-claim validation.

The owner deliberately adopts a stronger product policy than the research YAGNI recommendation on one point: Targeted + Global final defect discovery and the Final Qualification Handoff are standard PW behavior rather than merely project-local optional strategy. Their realization remains proportional and runtime-owned, so small changes need not use large worker counts.

No further material owner/product questions remain in Revision 20.

Revision 20 is `ready_for_definition`, but promotion still requires explicit owner authorization for the exact subject `pwv22-program@20`.
