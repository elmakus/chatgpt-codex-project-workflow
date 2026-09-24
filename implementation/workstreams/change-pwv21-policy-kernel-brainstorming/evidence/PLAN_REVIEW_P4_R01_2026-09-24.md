# Independent Plan Review — P4 / R01

Date: 2026-09-24
Workstream: `change-pwv21-policy-kernel-brainstorming`
Verdict: **GREEN**

## Exact review subject

- Repository: `elmakus/chatgpt-codex-project-workflow`
- Commit: `71de528901e2e19ee2cbdaf2c5caeb47d16296ad`
- Path: `planning/PWV21_POLICY_KERNEL_MASTER_PLAN_P4.md`
- Blob: `abe96de5adf92e46cd1b3cb89466d3f567750792`
- Planning cycle: 4
- Plan revision: P4

The subject blob was read from the exact frozen commit and matched the durable `PLANNING.toml` / `PLAN_REVIEW.toml` binding.

## Independence

This review was performed in the fresh independent Premium-B context named by the durable handoff. The reviewing context did not materially author or repair P4. No earlier review verdict was used as a correctness checklist; the complete current acceptance surface was re-evaluated from accepted authority, the exact frozen subject, and repository evidence.

## Accepted authority verified

Definition record:
- `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/DEFINITION.toml`
- revision R2, state GREEN, source `pwv21-policy-kernel@2`

Requirements:
- `requirements/PWV21_POLICY_KERNEL.md`
- blob `6f2fd5ace3ef20c708c995115f56efd9de009a33`
- 127 accepted requirements, `PWV21-REQ-001` through `PWV21-REQ-127`

Accepted decisions and verified blobs:
- ADR-PWV21-001 — `0662b970d80e8b76df79e4dbd458d190ce6d4402`
- ADR-PWV21-002 — `051f8fc3f68773349a1fcad39fcf1c60d3157532`
- ADR-PWV21-003 — `437388345d7136cdcdf241bf3ca6aa1016ddb1c0`
- ADR-PWV21-004 — `60f95d9a578b10e367a066599d4a89f02b60717b`
- ADR-PWV21-005 — `fbaaaedac492ff9e2dbf4db9f8e86b3376df2023`
- ADR-PWV21-006 — `673a2781d5c6da048e50d27e39cc4857606ec9f8`
- ADR-PWV21-007 — `6adbbef4a40f6005ec09e1a3f73289e256f44b12`

All P4 authority-input pins matched the current accepted R2 authority blobs.

## Full-scope review

The full plan was checked across authority, strategy, milestone ordering, milestone outcomes, acceptance criteria, verification strategy, JIT boundaries, cross-cutting constraints, transition/migration semantics, risks, gates/escalation, ADR coverage, and the complete Appendix-A requirement inventory.

### Requirement coverage

Mechanical inventory audit of Appendix A:
- total rows: 127
- missing requirements: 0
- duplicate requirements: 0
- owner counts:
  - M01: 10
  - M02: 16
  - M02R: 20
  - M03: 7
  - M04: 22
  - M05: 21
  - M06: 15
  - M07: 16

The per-requirement verification methods are materially aligned with their accepted requirement semantics. Cross-milestone checks are explicitly retained where a later integration/final audit must extend an earlier mechanism; no accepted requirement is silently dropped.

### Decision coverage

All seven accepted ADRs are explicitly covered:
- ADR-001: M01/M03
- ADR-002: M02/M06
- ADR-003: M04
- ADR-004: M05, with R2 convergence baseline in M02R
- ADR-005: M03/M06/M07
- ADR-006: M02R/M03
- ADR-007: M02R/M03

### R2 / P4 material checks

- Historical M01/M02 remain terminal and are not retroactively reopened.
- M02R is inserted before M03 and owns the R2 bootstrap semantics required before downstream dogfood.
- M02R freezes three distinct `required_seam` boundaries (R2-A/R2-B/R2-C), preventing Execution Prep from collapsing the bootstrap milestone into one whole-milestone Card.
- M03 cannot materialize before M02R terminal GREEN.
- Authority-level dogfood and deployed-consumer validation are explicitly distinguished.
- Card/Milestone/final review layers remain separate; compatibility/topology checks do not substitute for mandatory local review.
- Live findings are classified before authority mutation; tracker text remains non-authoritative; historical failure evidence is replayed without rewriting terminal history.
- Premium A/C optional handoff semantics preserve a read-only kernel and governed write/readback; Premium B remains a separate mandatory fresh-independent boundary.
- Final workstream close remains gated by a fresh final-integration GREEN plus complete evidence.

### Independent verification of the two P3/R01 correction classes

1. **Review-ceiling authority:** GREEN. P4 fixes the accepted defaults at Card=5, Milestone=4, final-integration=3 per stable epoch, excludes bounded finding-verification passes from the count, makes ceiling hit a convergence mode switch rather than acceptance, and explicitly states that the defaults are **not** a JIT choice. Execution Prep cannot raise them through refinement.
2. **ADR coverage:** GREEN. ADR-PWV21-006 and ADR-PWV21-007 are both explicitly present in the plan authority list and ADR coverage table, with concrete M02R/M03 ownership.

## Baseline plausibility check

The named terminal M02 candidate baseline `elmakus/project_workflow_v2@e7a939e0a37f3cfcb7e39e04d5654b94101a5090` was spot-checked against the plan's seam map. Named files and core symbols used by the plan exist at that subject, including:
- `tools/state_contract.py` / `validate_board` / `reject_prohibited_keys`
- `tools/router.py` / `select_route`
- `tools/execution_contract.py` / `choose_realization` / `classify_return` / `parse_card_result`
- execution/task-card templates and tests
- review/recovery/close contract seams named for downstream extension

No material baseline contradiction was found.

## Findings

No material findings.

The plan is sufficiently bounded and executable for downstream approval consumption. It preserves accepted R2 authority, provides complete requirement/decision coverage, defines milestone and review gates without delegating material strategy to JIT, and does not create implementation authority before the normal post-review approval/Premium-C boundary.

## Verdict

**GREEN**

Return to Strategic Planning for deterministic GREEN consumption. Planning may set P4 to `approved` and Premium C to `due` for the exact frozen subject. GREEN itself does not authorize Execution Prep.
