# Independent Plan Review — P2 / R01

Date: 2026-09-24
Workstream: `change-pwv21-policy-kernel-brainstorming`
Review attempt: `R01`
Verdict: **GREEN**

## Exact subject

`elmakus/chatgpt-codex-project-workflow@ca046952a4d249d9ed74af6408db71b0ded73a8f:planning/PWV21_POLICY_KERNEL_MASTER_PLAN_P2.md@79ee0b6588be32767ba283b9f20a48a192999001`

The reviewed blob matches the frozen P2 subject and the exact `premium_b_subject`.

## Independence

This review was performed in the fresh context entered for Premium B. This context did not materially produce or repair the exact P2 subject. No earlier Plan Review verdict existed for this subject.

The verdict below was derived from the frozen plan, accepted Definition authority, current V2 workflow contracts, and direct mechanical checks. Planner self-audit material was not treated as review authority.

## Authority checked

Accepted Definition authority was reconstructed from exact pinned sources:

- `requirements/PWV21_POLICY_KERNEL.md` R1 — blob `21ee85e6a306ce106cb26e77b0a395a2e671c054`
- ADR-PWV21-001 — blob `0662b970d80e8b76df79e4dbd458d190ce6d4402`
- ADR-PWV21-002 — blob `051f8fc3f68773349a1fcad39fcf1c60d3157532`
- ADR-PWV21-003 — blob `437388345d7136cdcdf241bf3ca6aa1016ddb1c0`
- ADR-PWV21-004 — blob `567988b8789960308d9e5c91ccdc9d004f2f53b1`
- ADR-PWV21-005 — blob `fbaaaedac492ff9e2dbf4db9f8e86b3376df2023`
- Definition record R1 is GREEN and points to the same requirements/ADR authority.
- Current `elmakus/project_workflow_v2@main` still resolves to `986affffb7ba816e260e48549bf56e198ed51c21`, matching the baseline used by P2.

## Independent review checks

### 1. Definition and requirement coverage

GREEN.

P2 preserves the accepted target state and non-goals. Mechanical inspection found exactly seven milestone sections M01–M07 and exactly 107 Appendix-A requirement rows, with 107 unique IDs, zero missing IDs and zero duplicate IDs. Ownership totals remain M01=10, M02=16, M03=7, M04=22, M05=21, M06=15, M07=16.

### 2. Predecessor preservation and correction boundary

GREEN.

The exact P1 predecessor blob is `59c3a3c3927d8572b6a8f98124652c17554cb012`. Direct section comparison shows M01, M02, M03, M04 and M05 are byte-identical between P1 and P2. The material correction is therefore bounded to the intended runtime/handoff/recovery acceptance surface rather than silently changing earlier strategy.

### 3. Optional Premium A/C correction

GREEN.

P2 now makes the missing lifecycle executable and testable:

- A-stay and A-fresh are explicit.
- C-stay and C-fresh are explicit.
- the offered choice is bound to the exact current gate subject;
- a fresh receiver reconstructs canonical Git before accepting the input;
- the policy kernel remains read-only;
- the governed coordinator performs preconditioned persistence;
- mandatory readback occurs before continuation;
- interrupted/uncertain persistence is read back before retry;
- already-satisfied exact gates are consume-only/idempotent;
- stale/wrong-cycle/wrong-plan locators cannot satisfy the current gate;
- deterministic continuation occurs without duplicate confirmation;
- Premium B remains separately mandatory, fresh-independent and exact-subject-bound.

These controls are consistent with REQ-004, REQ-031, REQ-077, REQ-081, REQ-082, REQ-106 and REQ-107 together with the current V2 Premium A/B/C handoff contract. The correction does not weaken B or make locator narrative authoritative.

### 4. Review, runtime and authority boundaries

GREEN.

The plan preserves subject-relative review independence, evidence-gated GREEN, Card/Milestone/final layered review, no compatibility-review substitution, no silent model/provider substitution, no runtime identity/telemetry in canonical state, and the PW-vs-OR authority boundary required by the accepted ADRs.

### 5. Parallelism, staleness and recovery

GREEN.

Parallelism remains explicitly Plan/JIT-authorized; overlapping mutating scopes serialize without override; stale results are reconciled before reuse; contradictory durable state fails closed to Recovery; unaffected sibling/workstream results are preserved where authority allows.

### 6. Migration and close

GREEN.

The plan retains lazy/on-entry PWv2→PWv2.1 migration, historical GREEN preservation, minimal normalization, real-derived migration rehearsal, dependent-path-only blocking, and the requirement that workstream close cannot occur before fresh final-integration GREEN plus complete acceptance evidence.

### 7. Execution boundary

GREEN.

P2 creates no Task Board or implementation authority. Exact serialization, field names, module layout and bounded Card decomposition remain deferred only where REQ-010 permits JIT implementation choices. Strategy/authority changes still escalate to Planning/Definition rather than being silently absorbed during execution.

## Findings

No blocking contradiction, uncovered accepted requirement, duplicate ownership, scope expansion, gate weakening, or missing acceptance path was found.

The main prior semantic gap — optional Premium A/C fresh-handoff selection being treated as navigation rather than exact gate input — is now covered by explicit lifecycle, readback, idempotence, stale-subject rejection and no-duplicate-confirmation scenarios while preserving Premium B as a separate mandatory independent boundary.

## Verdict

**GREEN.** P2 is sufficiently complete, internally consistent, authority-aligned and reviewable to be consumed by Planning as an approved plan for this exact frozen subject.
