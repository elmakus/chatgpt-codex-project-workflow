# Codex-only M02 Handoff — formal review and recovery

## Completed checkpoint

- Milestone: `M02`
- Accepted implementation subject: `b901d1cfa5ca26074b363b0c8980f7a7aaa223f1`
- Result: GREEN
- Integrated acceptance: `implementation/workstreams/feature-codex-only-policy/evidence/M02-acceptance.md`

## Achieved state

The codex_only namespace now has a complete durable formal-review state model decoupled from runtime worker/session identity. Card and milestone review provenance is semantic, review attempts preserve immutable subjects and prior RED/GREEN history, Tester cannot repair production, and repository-first recovery can continue across runtime resume/replacement.

The Attempt-1 milestone provenance/recovery defect was corrected and the corrected exact subject passed independent Attempt-2 review. Serial execution remains the M02 shape; bounded parallel Card safety remains owned by M03.

## Authority in force

- Requirements: `requirements/CODEX_ONLY_POLICY.md` revision `CO-R1`
- Decisions: accepted dedicated-namespace, runtime-boundary and bounded-parallel ADRs
- Plan: `planning/CODEX_ONLY_MASTER_PLAN.md` revision `CO-P1`
- M02 OpenSpec: `openspec/changes/codex-only-m02-formal-review-state/`

## Evidence

- `implementation/workstreams/feature-codex-only-policy/evidence/M02-T01.md`
- `implementation/workstreams/feature-codex-only-policy/evidence/M02-T01-review-01.md`
- `implementation/workstreams/feature-codex-only-policy/evidence/M02-T01-review-02.md`
- `implementation/workstreams/feature-codex-only-policy/evidence/M02-acceptance.md`

## Next durable starting point

M03 is the next approved milestone. Execution Prep should JIT-contract the smallest deterministic Card set for bounded parallel metadata, compatible-ready-set safety, isolated worker-result return and Main-owned integration/recovery while preserving the M02 review-attempt/runtime-identity boundary.
