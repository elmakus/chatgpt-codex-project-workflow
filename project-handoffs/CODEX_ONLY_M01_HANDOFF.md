# Codex-only M01 Handoff — namespace foundation

## Completed checkpoint

- Milestone: `M01`
- Accepted implementation subject: `8ded26f50275ab04e35a07438ca1abd2836901c2`
- Result: GREEN
- Integrated acceptance: `implementation/workstreams/feature-codex-only-policy/evidence/M01-acceptance.md`

## Achieved state

The workstream now has the complete 22-file `workflow/codex_only/` ownership surface defined by the accepted M01 parity matrix. The namespace remains intentionally non-routable until M04.

Project Workflow/project-state ownership is separated from `codex_workflow` runtime worker/session mechanics. Review foundations preserve immutable subjects and reviewer non-repair; serial execution remains the safe default. Exact review/provenance/recovery mechanics are owned by M02 and bounded-parallel schema/JIT/lane semantics by M03.

## Authority in force

- Requirements: `requirements/CODEX_ONLY_POLICY.md` revision `CO-R1`
- Decisions: the accepted dedicated-namespace, runtime-boundary and bounded-parallel ADRs
- Plan: `planning/CODEX_ONLY_MASTER_PLAN.md` revision `CO-P1`
- Accepted migration baseline: `docs/audits/CODEX_ONLY_M01_BASELINE_MATRIX.md`

## Evidence

- `implementation/workstreams/feature-codex-only-policy/evidence/M01-T01-review-01.md`
- `implementation/workstreams/feature-codex-only-policy/evidence/M01-T02-review-01.md`
- `implementation/workstreams/feature-codex-only-policy/evidence/M01-acceptance.md`

## Next durable starting point

M02 is the next approved milestone. Execution Prep should JIT-contract the smallest deterministic work that finalizes project/runtime ownership, formal independent review state/provenance/RED repair semantics and runtime-decoupled recovery without introducing M03 parallel-lane schema early.
