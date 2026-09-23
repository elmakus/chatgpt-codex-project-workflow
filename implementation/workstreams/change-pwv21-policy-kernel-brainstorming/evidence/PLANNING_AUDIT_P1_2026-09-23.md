# Planner completeness/challenge audit — P1 (cycle 1)

Date: 2026-09-23
Workstream: `change-pwv21-policy-kernel-brainstorming`
Plan: `planning/PWV21_POLICY_KERNEL_MASTER_PLAN.md` (revision P1; lifecycle owned by PLANNING.toml)
Definition: R1 (`requirements/PWV21_POLICY_KERNEL.md`, approved) + 5 accepted ADRs
Verdict: GREEN — Main strategy acceptance recorded; planner self-audit complete.
Independent Stage-6 Plan Review still pending (not performed here).
Second pass: GREEN — 7 Main-directed corrections applied and re-verified
(see below); still within cycle 1/P1, no material re-entry.
Final pass: GREEN — lifecycle-neutral reference, from-the-start gates,
durable multi-set fail-closed rule; coverage re-verified 107/107.

## Completeness checks

- Requirement inventory mechanically verified: 107/107 IDs
  (PWV21-REQ-001…PWV21-REQ-107) appear exactly once in Appendix A;
  0 unmapped, 0 double-mapped. Per-milestone totals M01: 10, M02: 16,
  M03: 7, M04: 22, M05: 21, M06: 15, M07: 16; ownership ranges match the
  milestone sections.
- Every requirement has a named verification method owned by its milestone
  (contract/unit/scenario/matrix/negative test, harness, rehearsal, or
  bounded review); no vague catch-all ranges.
- ADR coverage: ADR-PWV21-001 → M01+M03; -002 → M02+M06; -003 → M04;
  -004 → M05; -005 → M03+M06+M07. All 5 ADRs mapped.
- Definition non-goals mirrored 1:1 in plan Non-goals; planning-level
  exclusions add only execution-vehicle, REQ-010 option-space, OR/Paseo and
  harness internals, V1 migration, and performance-target items — none of
  which narrows accepted scope.
- Milestone order is serial and acyclic; every stated dependency is
  satisfied by the order; each milestone has outcome, per-requirement
  coverage, planned work, acceptance, verification, and JIT boundary.
- Gates: freeze/B/Stage-6/approval/C sequence stated; per-milestone close
  rule (acceptance GREEN + separate Milestone review); workstream close
  rule (M07 GREEN + fresh final-integration review + complete evidence).
- Escalation paths stated for JIT detail, milestone change, product change,
  and missing facts; unstructured global repair forbidden.
- No Task Board/Cards created; no implementation authority asserted; no
  cross-repository writes authorized (contribution vehicle deferred to
  Execution Prep after premium C).
- No product/strategy decision altered vs accepted Definition; finer
  execution choices (serialization, naming, layout, ceilings, wording,
  rehearsal selection) held at JIT within stated invariance boundaries.

## Challenge audit (adversarial pass)

Challenges raised and dispositioned; ordinary defects were corrected in
the draft:

1. Milestone diagram ambiguity (implied direct M01→M06 edge absent from
   the dependency table). CORRECTED: replaced with the serial chain plus
   an explicit table-reference note.
2. M03 acceptance overclaimed full REQ-015 corpus coverage before M04/M07
   exist. CORRECTED: M03 seeds available classes + extension points; M07
   acceptance gains the final all-class corpus audit.
3. Execution's own review-regime transition (V2 rigor before M05 lands,
   M05 semantics after) needed an explicit validity rule. CORRECTED:
   gates section now applies REQ-099 (closed reviews stay valid; new
   semantics for active stages only).
4. Cross-cutting telemetry enforcement named "M07 review" vaguely.
   CORRECTED: fails M07 acceptance.
5. Implementation target mechanics unstated (baseline lives in
   `elmakus/project_workflow_v2`, a separate repository). CORRECTED: added
   "Implementation target and contribution boundary" — baseline is
   read-only reference; contribution vehicle is bounded Execution Prep
   choice after premium C; no cross-repo writes authorized by the plan.
6. REQ-076 (M05) referenced in M06 acceptance — confirmed integration-only
   wording; ownership and verification stay with M05. No change needed.
7. REQ-010 verification by review — confirmed appropriate: it is a bounded
   option-space record with an invariance rule, not executable behavior.
8. Bootstrap self-reference (plan executes under V2 while specifying v2.1)
   — confirmed coherent: serial V2 execution, no v2.1 feature required to
   implement itself, live conformance evidence via own Card/Milestone/final
   reviews.

No material Main decision surfaced from schema or strategy ambiguity; the
cycle-1 premium A satisfaction rests on the recorded explicit user
authorization ("Kontynuuj tutaj") documented in
`evidence/PREMIUM_A_SATISFIED_2026-09-23.md`.

## Residual risk for Stage-6 / Main attention

- R-05 (write-scope overlap escape) is Low-likelihood/Critical-impact;
  Stage-6 should confirm the M04 negative-test surface is exhaustive.
- Contribution vehicle for the separate V2 baseline repository is
  intentionally deferred; Main strategy acceptance recorded it as a
  bounded Execution Prep choice after premium C.

## Second pass — Main-directed corrections (same cycle 1/P1)

All corrections are planner self-audit repairs, not Stage-6 review and not
material re-entry. Strategy, milestone structure, requirement coverage, and
gates are unchanged.

1. Route taxonomy: cross-cutting text now distinguishes three outcomes —
   serial routing for overlap/insufficient independence proof
   (REQ-038/039, denial of parallel authorization only), revalidate/
   reconcile/prove-reuse first for stale results (REQ-028/029/051), and
   Recovery only for contradictory authority/state or unresolvable
   mechanical parity ambiguity (REQ-092). M04 acceptance reworded to deny
   the parallel authorization, never the Cards. Appendix rows REQ-038/039/
   028/029/051 verified consistent.
2. PW vs OR boundary: M04 ownership and M05 independence work items now
   specify PW typed semantic obligations, eligibility/evidence, and
   acceptance; OR owns assignment/launch/replacement/archive/model/
   session/concurrency/isolation. Added a cross-cutting PW/OR boundary
   rule; review eligibility is subject-relative semantic evidence, never
   telemetry. Appendix rows REQ-048/049/060/072/076 reworded to PW
   acceptance/eligibility; direct/manual compliant execution preserved.
3. Independent parity: M03 now requires a fresh capable reasoning context
   receiving only canonical Git + portable contracts (no helper output,
   labels, transcript, OR state, or cache), locking verdict+source
   evidence BEFORE comparison. Programmatic checks are supporting
   coverage only. Destructive acceptance is constrained to isolated
   disposable surfaces with user-state preservation proof; raw evidence
   retained; unavailable acceptance fails visibly. Appendix rows
   REQ-011/012/014/017 updated.
4. Final-integration sequencing: M07 has its own acceptance + fresh
   Milestone review and tests close mechanics with fixtures; the actual
   workstream final-integration review is post-M07 lifecycle evidence,
   never a prerequisite for M07 GREEN. Gates, plan-level verification,
   and M05 execution-compliance wording aligned; V2 + plan controls apply
   from the start without requiring new kernel mechanics to bootstrap
   themselves.
5. Serial gates: dependency table now states the immediate serial
   predecessor as a gate plus semantic prerequisites, explicitly
   forbidding bypass. M01 defines kernel seams/interfaces and implements
   the predicate core; full Obligation/Result compiler/acceptance is M02.
6. Baseline map: added a verified baseline-to-change map naming observed
   seams per milestone (router/state/execution/review/recovery/close/
   migration modules, fixtures, suites) at `elmakus/project_workflow_v2`
   commit `986affffb7ba816e260e48549bf56e198ed51c21`, plus authority
   input pins (requirements + 5 ADRs, consumer commit `8793e8cfc35e21f4bf25456ae66dcf9dfebcb64d`,
   blob hashes verified equal to working tree). REQ-010 flexibility kept.
7. Reviewability: removed the 7 repetitive per-REQ prose lists; Appendix A
   remains the single canonical 107-row inventory with ownership
   ranges/counts kept per milestone. Header is lifecycle-neutral
   (PLANNING.toml owns mutable lifecycle).

Re-verification after all corrections: Appendix A mechanical audit 107/107
exactly once; canonical state_contract validators pass on all records;
canonical router returns route/planning for cycle 1; change footprint
remains planning-owned files only.

## Freeze record and downstream gates

1. Main strategy acceptance: recorded (this revision).
2. Freeze: exact immutable Git-blob subject of the accepted plan file
   resolved from the content commit; PLANNING.toml set to frozen with
   GREEN audit, review_mode independent, premium B due bound to that
   exact subject, in a separate metadata commit (frozen subject recorded
   in PLANNING.toml, not duplicated here).
3. Premium B stop with fresh independent best-available-context handoff:
   due after freeze; not satisfied here.
4. Independent Stage-6 Plan Review (never planner-spawned): pending.
5. GREEN consumption → approved + premium C due; C satisfaction →
   Execution Prep: pending.
