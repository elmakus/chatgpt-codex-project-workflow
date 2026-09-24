# Independent Plan Review — P5 / R01

Date: 2026-09-24  
Workstream: `change-pwv21-policy-kernel-brainstorming`  
Planning cycle: 5  
Plan revision: P5  
Verdict: **RED**

## Exact subject

`elmakus/chatgpt-codex-project-workflow@5b4270fecd246cac8f6fac459a9887c82d0d348b:planning/PWV21_POLICY_KERNEL_MASTER_PLAN_P5.md@ef82cfa76bf5af9ea336902ca4bfd39891e4a2a9`

## Independence

This review was performed in a fresh Premium-B context that did not materially author or repair P5. The review consumed the exact frozen subject and accepted Definition R3 authority rather than planner verdict/opinion as correctness authority.

## Acceptance surface reviewed

- Definition R3 / `pwv21-policy-kernel@3`.
- All 137 accepted requirements `PWV21-REQ-001..137`.
- All eight accepted ADRs `ADR-PWV21-001..008`.
- P5 milestone topology, required/preferred seams, gates, escalation, historical-state preservation, authority/runtime boundary, requirement ownership and verification strategy.
- Exact P5 authority input pins against current accepted blobs.
- Candidate implementation baseline at `elmakus/project_workflow_v2@e7a939e0a37f3cfcb7e39e04d5654b94101a5090`.

Mechanical audit:
- 137/137 requirement rows are present exactly once.
- Requirement ownership for REQ-001..127 is unchanged from GREEN-reviewed P4.
- REQ-128..137 are all assigned to M02R.
- All four BOOT-A/B/C/D required seams are represented.
- All eight ADRs have explicit milestone ownership.
- All pinned R3 authority blobs still match the accepted branch state.

The review continued across the complete acceptance surface after finding the blocker below.

## Material findings

### F1 — REQ-108 causal-blast-radius closure semantics are not planned or verified

**Classification:** material requirement-coverage defect.

Accepted `PWV21-REQ-108` requires bounded finding-closure verification to evaluate not only known findings, repair diff and regression evidence, but also the **materially implicated causal blast radius**, explicitly including reachable callers, consumers, providers, contracts, sibling representations and negative-space cases.

P5 correctly plans the discovery-vs-closure distinction, exhaustive discovery, defect-class/root-cause repair, sibling/negative-space coverage, fresh rediscovery and bounded convergence. However, the frozen P5 subject contains no planning or verification obligation for causal-blast-radius tracing during closure verification. In particular:

- BOOT-A planned work defines finding-closure verification and class-level repair but does not require traversal of materially reached callers/consumers/providers/contracts;
- BOOT-A acceptance omits causal-blast-radius closure verification;
- BOOT-A verification strategy omits causal-blast-radius fixtures;
- Appendix A's REQ-108 row only proves that bounded finding verification cannot substitute for fresh full-scope review and does not verify the causal-blast-radius requirement.

This omission is material because the causal-blast-radius rule was an explicit R3 correction derived from the research case where a fix can satisfy the named finding while breaking unchanged consumers. An implementation following P5 as written could pass every planned REQ-108 test while still violating accepted REQ-108.

**Required correction:** the next material Planning cycle must explicitly bind causal-blast-radius closure semantics into BOOT-A planned work, acceptance and verification. It must cover materially reachable callers/consumers/providers/contracts in addition to the repair diff, regression evidence, sibling representations and negative-space cases.

## Non-blocking observations

### O1 — stale P4 wording in the P5 dogfood summary

P5 line 109 says M03 Execution Prep must follow the “accepted P4 seam classifications”. P5 later restates the same M03 decomposition intent and the exact P4 predecessor is pinned, so no current semantic conflict was found. In the next plan revision, referring to the current P5/P6 accepted seam authority would be clearer and avoid future stale-authority ambiguity.

### O2 — REQ-061 Appendix wording still reflects the older generic “recheck” phrasing

Appendix A describes REQ-061 as “same Reviewer rechecks Worker repairs it did not make”. The aggregate P5 review model does distinguish closure verification from fresh rediscovery, so this does not independently create a blocking gap. The next revision should nevertheless phrase REQ-061 verification explicitly as **bounded finding-closure verification by the discovering Reviewer when it did not repair the subject**, with the later fresh full-scope discovery obligation remaining separate.

## Areas found GREEN

- P5 preserves the P4 milestone chain and truthful terminal M01/M02 history.
- M02R precedes M03 and prevents the waiting historical trigger from materializing M03 directly.
- Four Planning-level M02R required seams BOOT-A/B/C/D prevent whole-M02R mega-Card collapse while permitting meaningful additional splitting.
- Semantic Card right-sizing correctly rejects both independent-outcome mega-Cards and file/layer/test-step micro-Cards.
- 5/4/3 is correctly bound to genuinely new material defect-class discovery epochs rather than every review invocation.
- The separate default three-round per-defect-class repair/closure breaker is correctly represented as a mode switch, never RED acceptance.
- Fresh rediscovery after known-finding closure is retained.
- Load-bearing vs non-load-bearing finding semantics, durable observation disposition and pre-Final reconciliation/cleanup are represented.
- Worker falsification-first/YAGNI/non-absolute-DRY discipline is represented without fixed project-size or wall-clock policy.
- Git remains canonical; PW remains policy/authority, not scheduler/orchestrator.
- M03 remains authority-level dogfood/shadow replay rather than false deployed-PWv2.1 proof.
- Premium A/B/C, independent Plan Review, milestone review and final-integration boundaries remain intact.

## Verdict rationale

P5 is structurally strong and otherwise substantially covers Definition R3, but F1 allows accepted REQ-108 to be implemented incompletely. Because this is a material accepted-requirement coverage gap, the exact frozen P5 subject is **RED** and must not advance to Premium C or Execution Prep.
