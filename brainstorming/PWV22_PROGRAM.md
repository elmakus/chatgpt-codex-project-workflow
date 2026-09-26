# PWv2.2 Program Brainstorming — Revision 1

Status: ACTIVE FORMAL BRAINSTORMING
Scope subject: `pwv22-program@1`
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

## 7. Revision-1 open decision register

Open:
1. exact first-launch boundary: minimal C only versus selected P/X/R/K;
2. whether the old E/S labels remain useful beyond sequencing/risk notation;
3. exact identity/graph/freshness architecture;
4. FR-08 placement relative to core;
5. whether P/X/R/K are truly separable after final predecessor rebind;
6. FR-19 applicability model and representation;
7. evidence inheritance scope;
8. receiver/runtime qualification;
9. candidate-store necessity;
10. migration/cutover model;
11. what to simplify or reject from FR-01..FR-19;
12. any owner decision surfaced by further grilling.

## 8. Current challenge status

`PENDING`.

Revision 1 is intentionally broad. The first grilling round should reduce the problem into a smaller set of real owner choices before any additional Research is launched.
