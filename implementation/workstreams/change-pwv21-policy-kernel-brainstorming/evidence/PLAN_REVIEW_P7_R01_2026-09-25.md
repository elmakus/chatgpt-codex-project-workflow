# Independent Plan Review — P7 / R01

Date: 2026-09-25  
Workstream: `change-pwv21-policy-kernel-brainstorming`  
Planning cycle: 7  
Plan revision: P7  
Verdict: **GREEN**

## Exact subject

`elmakus/chatgpt-codex-project-workflow@71e77c1246ec728dad09879c49cdc44adf98790c:planning/PWV21_POLICY_KERNEL_MASTER_PLAN_P7.md@37aac21d481e8ecf79b42309d023baabe27ebe87`

## Independence

This Premium-B receiving context did not materially author or repair P7. It reconstructed the review from current canonical Project Workflow V2, the exact frozen P7 subject, accepted Definition R3 authority, the pre-M03 checkpoint/raw reconciliation evidence, and the explicit replan authorization.

Before review, durable recovery corrected one stale live locator: `PLAN_REVIEW.toml` still pointed to terminal P6/R01 while current Planning was frozen P7. That mismatch was mechanically reconciled to a pending P7/R01 attempt; P6/R01 evidence remains immutable historical evidence. The P7 plan subject itself was not changed.

## Acceptance surface reviewed

- Definition R3 / `pwv21-policy-kernel@3`.
- All 137 accepted requirements `PWV21-REQ-001..137`.
- All eight accepted ADRs `ADR-PWV21-001..008`.
- Current canonical V2 Planning, Plan Review, Recovery and user-stop semantics.
- Independently GREEN-reviewed pre-M03 reconciliation checkpoint and its four probe batches.
- Explicit pre-M03 replan authorization over all 17 unresolved RF families under `QUALITY_FIRST_PRE_M03`.
- P7 M02Q corrective topology, downstream M03-M07 continuity, gates/escalation, historical-state preservation and verification strategy.

## Mechanical verification

- Exact P7 blob read back as `37aac21d481e8ecf79b42309d023baabe27ebe87`.
- All nine authority pins in P7 match the current selected branch exactly: Requirements R3 plus ADR-PWV21-001..008.
- P7 contains 137/137 unique requirement IDs; 0 missing.
- P7 contains all 17 RF family IDs; 0 missing.
- The M02Q repair table preserves the checkpoint members and dependencies for every RF family with 0 mismatches.
- The P7 RF dependency-aware order exactly matches the independently reviewed checkpoint:
  `RF008 -> RF007 -> RF005 -> RF017 -> RF002 -> RF016 -> RF012 -> RF013 -> RF009 -> RF006 -> RF004 -> RF003 -> RF010 -> RF011 -> RF001 -> RF014 -> RF015`.
- The audited candidate branch still resolves exactly to `elmakus/project_workflow_v2@07c724085de591c2a0bb51aaaae0ec23009880bf`.

## Material review result

### Corrective ownership and history

P7 correctly preserves terminal M01, M02 and M02R rather than retroactively rewriting them. It inserts M02Q as a forward corrective gate before M03 and makes all 17 independently reconciled RF families Planning-level `required_seam` boundaries. This is consistent with the accepted decomposition-fidelity rules: Execution Prep may split a seam further on real semantic evidence but may not merge across required seams.

No M03 Card/JIT materialization is authorized before M02Q terminal GREEN. M02Q itself requires per-RF durable implementation/result/review evidence, replay of the original defect probes plus materially implicated sibling/negative-space cases, full regression, and a separate fresh M02Q Milestone Review.

### Formerly authority-ambiguous mechanisms

The three checkpoint families that required Planning-level authority reconciliation are resolved without changing accepted product intent:

1. **RF006 — review-history identity/completeness:** explicit immutable source-attempt provenance for legacy migration, exact source Git/workstream binding, append-only current attempt identity and complete readback are bounded representations of REQ-097..102 plus the accepted subject/evidence validity and history-preservation rules. Ambiguity still fails closed.
2. **RF008 — editorial exemption proof:** P7 replaces free-text self-attestation with an immutable old/new-subject classification record, inspected diff/evidence and an independent `editorial_only` semantic classification. The proof is narrower than full Plan Review and preserves the already accepted exemption invariant; if the proof is absent or not GREEN, the normal Premium-B -> Plan Review -> Premium-C path remains mandatory. This strengthens proof of the existing exception rather than creating a new product goal.
3. **RF011 — source-ref-independent recovery package:** deriving the mandatory target-side package from lifecycle-critical canonical locators and exact Git identities supplies the missing completeness rule required for Git-first recovery. Empty-package cleanup remains legal only for genuinely empty/no-history workstreams.

These mechanisms remain runtime-neutral, fail closed on ambiguity, and do not move semantic product/strategy authority into the deterministic kernel.

### Downstream strategy

The accepted P6 downstream strategy is preserved. M04, M06, M07, ADR coverage, cross-cutting constraints and planning-level scope exclusions are unchanged; M03/M05/transition/gates are updated only as needed to consume terminal M02Q evidence. Existing review independence, helper-less parity, parallel-safety, YAGNI, migration and final-integration gates remain intact.

## Non-blocking observation

### O1 — inherited stale P4 wording in the M02 lifecycle note

The P7 M02 section is correctly labeled `P7 lifecycle note` but still says “P4 does not reopen it.” This is the same harmless historical wording previously noted in P6/R01. It does not change authority, milestone topology, requirement coverage, acceptance, or gates.

Disposition: **deferred / no material correction required**. Normalize if a later material plan edit touches this prose; no P7 mutation is warranted solely for this wording.

## Verdict rationale

P7 establishes exact corrective ownership for all 17 independently verified pre-M03 defect families, resolves the three previously missing proof/package mechanisms at Planning level, preserves terminal history and accepted downstream strategy, and blocks M03 until the full quality-first corrective milestone is independently GREEN. No material contradiction, uncovered accepted requirement, unauthorized product choice or weakened gate was found.

**Verdict: GREEN.**
