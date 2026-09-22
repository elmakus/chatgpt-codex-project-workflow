# PWV2 Meta-Synthesis Contract

Date: 2026-09-22
Status: ready
Experiment ID: `PWV2-P1-P2-META-SYNTHESIS`

## Purpose

Determine whether the completed independent planning/review evidence justifies a **material Strategic Plan revision PWV2-P2**, or whether the approved Plan A/PWV2-P1 should remain canonical and the useful ideas from Plan B/reviews should be consumed only during Execution Prep/JIT.

This is an isolated meta-synthesis. It does not itself revise canonical planning state.

## Frozen Definition authority

Use only Definition checkpoint:
`8055ed00acdb708c79919d470217fd87c920973a`

Authority:
- `requirements/PROJECT_WORKFLOW_V2.md`
- ADR-PWV2-001..006
- `brainstorming/V1_TO_V2_COVERAGE_MATRIX.md`
- `brainstorming/V2_VALIDATION_MATRIX.md`
- `implementation/workstreams/feature-common-preexecution-core/handoffs/DEFINITION_COMPLETE_2026-09-22.md`

## Current canonical boundary

Plan A/PWV2-P1 has completed its canonical independent review GREEN and has been approved. The canonical workstream is at `premium_stop_C` before Execution Prep.

Do not mutate that state.

## Synthesis inputs

Read exactly:
- `planning/experiments/synthesis/PLAN_A.md`
- `planning/experiments/synthesis/PLAN_B.md`
- `planning/experiments/synthesis/REVIEW_A1.md`
- `planning/experiments/synthesis/REVIEW_A2.md`
- `planning/experiments/synthesis/REVIEW_B1.md`
- `planning/experiments/synthesis/BLIND_JUDGE_REPORT.md`

The inputs are intentionally neutralized for model provenance. Do not try to infer model identities or consult other branches/history to discover them.

## Core question

For every meaningful difference, finding, or recommendation, classify it as exactly one of:

### S1 — Material Strategic Revision
The item changes or materially strengthens:
- milestone outcome/order/dependency;
- requirement ownership/coverage;
- accepted invariant/gate;
- migration/cutover/adoption strategy;
- review/recovery/external-effect strategy;
- delivery/bootstrap architecture;
- a strategic contract that Execution Prep cannot safely invent.

If any S1 item is genuinely necessary or materially beneficial, recommend creating PWV2-P2.

### S2 — Execution Prep / JIT Refinement
The item improves:
- Card decomposition;
- package boundaries;
- exact implementation mechanism;
- test fixture detail;
- schema/serialization choice;
- current platform/API syntax;
- bounded risk-handling detail already authorized by P1;
- presentation/clarification useful to implementers,

without changing P1's strategic outcomes or accepted sequencing.

S2 does NOT justify PWV2-P2. It should become Execution Prep guidance.

### S3 — Redundant / Preference / No Action
Already fully represented, merely stylistic, duplicated, or not worth additional process cost.

## Anti-maximalism rule

The goal is NOT to merge every good sentence into one enormous plan.

A larger document is not a better plan.

Recommend P2 only if the expected reduction in implementation/recovery risk is materially greater than:
- re-planning complexity;
- new review cycle cost;
- risk of introducing contradictions;
- extra context load and maintenance burden.

All completed reviews are GREEN. Therefore a P2 recommendation must identify a concrete strategic improvement that cannot be safely realized as S2 under the approved P1.

## Required analysis

1. Build a cross-source synthesis table of all material differences/findings.
2. Classify each S1/S2/S3 with exact source references.
3. Specifically reassess:
   - Plan A broad M03/M04 decomposition versus Plan B concern separation;
   - early plugin feasibility probe;
   - construction custody / one-live-owner transfer;
   - per-row V1 disposition ownership;
   - migration idempotency/crash/rollback detail;
   - staged L01-L05 versus consolidated live acceptance;
   - cumulative automated conformance gate;
   - concise JIT/deferred-detail register;
   - challenge-audit framing;
   - target movement/terminal recovery/stacked paths;
   - all residual risks from A1/A2/B1.
4. Check every proposed S1 against frozen Definition and YAGNI.
5. Check whether each apparent improvement is already semantically present in P1 even if phrased differently.
6. Do not treat reviewer confidence, model identity, verbosity or document length as evidence.

## Required conclusion

Choose exactly one:

### Outcome KEEP_P1
Use when no material S1 remains.

Output:
- why P1 remains strategically sufficient;
- an exact **Execution Prep Guidance Pack** containing only the valuable S2 items that should guide Card decomposition/JIT;
- which Plan B/review ideas are intentionally not imported and why;
- confirmation that no new premium planning/review cycle is needed.

### Outcome CREATE_P2
Use only when one or more real S1 items remain.

Output:
- exact list of S1 deltas;
- why each cannot safely be deferred to Execution Prep;
- smallest possible P2 revision scope;
- exact sections of P1 that must change;
- what must remain byte/semantically unchanged;
- new validation/review implications;
- explicit instruction that P2 must re-enter the full premium A -> Planning -> B -> fresh independent review -> C cycle.

Do NOT draft a giant merged P2 in this experiment. Produce the smallest authoritative delta specification.

## Allowed write

Write exactly one artifact:
`planning/experiments/synthesis/PWV2_META_SYNTHESIS_REPORT.md`

No other mutation is permitted.

## Completion boundary

After writing the report:
- reread it;
- verify every claimed S1 is truly strategic and cannot be S2;
- verify no useful S2 was accidentally promoted into plan churn;
- STOP.

Do not modify Plan A or Plan B.
Do not modify canonical workstream state.
Do not enter Execution Prep.
Do not create PWV2-P2.
Do not perform another Plan Review.
