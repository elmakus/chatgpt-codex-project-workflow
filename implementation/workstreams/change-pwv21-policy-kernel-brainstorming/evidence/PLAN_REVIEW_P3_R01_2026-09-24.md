# Independent Plan Review — P3 / R01

Date: 2026-09-24
Workstream: `change-pwv21-policy-kernel-brainstorming`
Review attempt: `R01`
Verdict: **RED**

## Exact subject

`elmakus/chatgpt-codex-project-workflow@77d0104c414f7f2d81a3c961a6cf3efec10a2ce4:planning/PWV21_POLICY_KERNEL_MASTER_PLAN_P3.md@3f75c11c8da01fa05ab39938d44b3e6daa89e933`

The reviewed blob matches the frozen P3 subject and the exact `premium_b_subject`.

## Independence

This review was performed in the fresh context entered for Premium B. This context did not materially produce or repair the exact P3 subject. The P3 planner self-audit was inspected only as supporting evidence and was not treated as review authority.

The review completed the full applicable acceptance surface after identifying blockers; it did not stop at the first finding.

## Authority checked

Accepted Definition R2 authority was reconstructed from the exact P3 pins:

- `requirements/PWV21_POLICY_KERNEL.md` R2 — blob `6f2fd5ace3ef20c708c995115f56efd9de009a33`
- ADR-PWV21-001 — blob `0662b970d80e8b76df79e4dbd458d190ce6d4402`
- ADR-PWV21-002 — blob `051f8fc3f68773349a1fcad39fcf1c60d3157532`
- ADR-PWV21-003 — blob `437388345d7136cdcdf241bf3ca6aa1016ddb1c0`
- ADR-PWV21-004 — blob `60f95d9a578b10e367a066599d4a89f02b60717b`
- ADR-PWV21-005 — blob `fbaaaedac492ff9e2dbf4db9f8e86b3376df2023`
- ADR-PWV21-006 — blob `673a2781d5c6da048e50d27e39cc4857606ec9f8`
- ADR-PWV21-007 — blob `6adbbef4a40f6005ec09e1a3f73289e256f44b12`
- Definition record R2 is GREEN and points to the same requirements plus all seven accepted ADRs.

Current canonical workflow authority was read from `elmakus/project_workflow_v2@main`, including `workflow/ROUTER.md`, `workflow/PLANNING.md`, `workflow/PLAN_REVIEW.md`, and `workflow/STATE.md`.

## Independent checks

### 1. Exact subject and authority pins

GREEN.

The P3 blob matches the frozen Planning/Plan Review subject. All eight P3 authority-input blob pins (requirements + seven ADRs) match the files at the frozen subject commit.

### 2. Requirement coverage

GREEN mechanically.

Independent inspection found exactly 127 accepted requirement IDs in R2 and exactly 127 Appendix-A rows in P3, with zero missing IDs and zero duplicate IDs.

The ownership totals declared by P3 are internally consistent:
M01=10, M02=16, M02R=20, M03=7, M04=22, M05=21, M06=15, M07=16.

### 3. R2 bootstrap / decomposition fidelity

GREEN on strategy shape.

P3 inserts M02R before M03, keeps historical M01/M02 terminal, and freezes three separate non-mergeable bootstrap seams:

- R2-A review completeness/convergence;
- R2-B decomposition fidelity/topology challenge;
- R2-C live-validation/replay.

M03 remains blocked until M02R is terminal GREEN, and the plan distinguishes authority-level dogfood/shadow validation from deployed workflow enforcement.

### 4. Implementation-baseline feasibility

GREEN.

The pinned candidate baseline `elmakus/project_workflow_v2@work/pwv21-policy-kernel@e7a939e0a37f3cfcb7e39e04d5654b94101a5090` contains the named executable seams used by the plan, including:

- `tools/state_contract.py`: `validate_board`, `reject_prohibited_keys`;
- `tools/router.py`: `select_route`, `result`, `recovery`;
- `tools/execution_contract.py`: `choose_realization`, `classify_return`, `parse_card_result`;
- `tools/review_contract.py`: `select_review_realization`;
- `tools/recovery_contract.py`: `classify_resolution`, `exact_result_subject`, `review_subject`;
- `tools/close_contract.py`: `close_continuation`.

No implementation-feasibility blocker was found in the baseline-to-change map.

### 5. Review lifecycle / convergence

RED — blocking authority contradiction.

Accepted R2 requirement `PWV21-REQ-112` fixes the **default hard ceilings** per stable review epoch at Card=5, Milestone=4, final-integration=3. ADR-PWV21-004 repeats those exact defaults. P3 itself correctly encodes 5/4/3 in M02R planned work, acceptance, risk mitigation, and states that weakening 5/4/3 must return to Strategic Planning/Definition.

However, the M05 JIT boundary states:

> "Failure-ceiling values and evidence packaging details are JIT choices within accepted semantics."

That leaves the numeric ceiling values themselves as an Execution-Prep/JIT choice, which is broader than accepted authority and conflicts with both R2/ADR-004 and P3's own M02R boundary. A downstream JIT implementation could therefore change the 5/4/3 values without an accepted Planning revision.

Required correction: remove the authority leak. M05 may leave implementation/configuration/packaging details to JIT, but the accepted default hard-ceiling values and the rule for changing them must remain fixed by authority.

This is not safely classifiable as a pure editorial exemption for the current unapproved subject because it changes the explicit Planning-to-JIT authority boundary.

### 6. ADR coverage completeness

RED — blocking planning-traceability incompleteness.

P3 names seven accepted ADRs in its Authority section and pins all seven exact blobs. The section titled `## ADR coverage`, however, contains rows only for ADR-PWV21-001 through ADR-PWV21-005. ADR-PWV21-006 (decomposition fidelity) and ADR-PWV21-007 (live validation) are absent from that accepted-decision ownership table.

The body does materially implement both decisions through M02R and M03, so this is not an uncovered product behavior. It is nevertheless an incomplete accepted-decision traceability surface in a Master Plan that claims comprehensive authority coverage. P4 must explicitly map ADR-006 and ADR-007 to their owning milestones/verification surfaces so downstream review does not rely on inference.

### 7. Runtime, parallelism, recovery, migration and close

GREEN apart from the two findings above.

The plan preserves:

- PW-owned authority vs OR/Paseo runtime realization;
- one primary mutating Worker per Card;
- no overlapping mutating-scope parallel override;
- compatibility review not substituting for Card review;
- subject-relative independent review;
- no silent model/provider substitution;
- runtime/session/model/telemetry exclusion from canonical state;
- stale-result reconciliation before reuse;
- fail-closed Recovery on contradictory mechanical state;
- lazy/on-entry PWv2→PWv2.1 migration;
- historical GREEN preservation/no retroactive RED;
- final-integration GREEN plus complete evidence before Close;
- Premium B as a distinct mandatory fresh-independent exact-subject boundary.

## Supporting evidence note

`PLANNING_AUDIT_P3_2026-09-24.md` was created after the immutable plan-content commit and therefore is not present inside commit `77d0104c...`. It exists on the current workstream branch and binds the exact P3 subject. This is not itself a Plan Review defect because the audit is supporting Planning evidence, not part of the immutable plan blob or accepted Definition authority, and the independent verdict above does not rely on it as authority.

## Findings summary

1. **F1 — blocking authority leak:** M05 incorrectly leaves failure-ceiling values to JIT despite R2/ADR-004 fixing default hard ceilings at 5/4/3 and P3 elsewhere forbidding their weakening without Planning/Definition.
2. **F2 — blocking completeness/traceability defect:** the `ADR coverage` table omits accepted ADR-PWV21-006 and ADR-PWV21-007 even though both are part of Definition R2 authority.

No additional material finding was identified after completing the rest of the plan/authority/baseline review surface.

## Correction classification

The findings do not require a Definition change and do not require Research. They require a **material Strategic Planning correction** because F1 changes the explicit boundary of what Execution Prep/JIT is authorized to decide.

Therefore:

- P3/R01 remains immutable RED history;
- Planning must open a new material cycle/revision;
- the new cycle requires a new Premium A before material repair;
- the Plan Review role must not repair P3 itself;
- after corrected plan freeze, the normal new B → independent Plan Review → C sequence applies.

## Verdict

**RED.**

P3 is close to authority-aligned and mechanically complete, but it cannot be approved while the M05 JIT boundary can vary accepted review-ceiling values and the accepted ADR coverage inventory omits two R2 decisions.
