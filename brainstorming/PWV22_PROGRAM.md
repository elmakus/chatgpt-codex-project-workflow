# PWv2.2 Program Brainstorming — Revision 9

Status: ACTIVE FORMAL BRAINSTORMING
Scope subject: `pwv22-program@9`
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
