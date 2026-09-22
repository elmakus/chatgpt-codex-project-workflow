# PWV2 Strategic Plan Blind Comparison Contract

Date: 2026-09-22
Status: ready
Comparison ID: `PWV2-PLAN-AB-JUDGE-01`

## Purpose

Independently compare two completed Strategic Master Plan candidates for Project Workflow V2.

The judge MUST evaluate strategic quality from the accepted frozen Definition authority and the candidate contents only. The judge MUST NOT attempt to identify which model/runtime produced either candidate.

## Frozen Definition authority

Repository:
`elmakus/chatgpt-codex-project-workflow`

Definition checkpoint:
`8055ed00acdb708c79919d470217fd87c920973a`

Required authority:
- `requirements/PROJECT_WORKFLOW_V2.md`
- ADR-PWV2-001..006 at the frozen checkpoint
- `brainstorming/V1_TO_V2_COVERAGE_MATRIX.md`
- `brainstorming/V2_VALIDATION_MATRIX.md`
- `implementation/workstreams/feature-common-preexecution-core/handoffs/DEFINITION_COMPLETE_2026-09-22.md`

## Candidate inputs

Read only these candidate copies:
- `planning/experiments/judge/PLAN_A.md`
- `planning/experiments/judge/PLAN_B.md`

The copies intentionally omit model/provenance/canonical-status metadata.

Do NOT read:
- `feat/common-preexecution-core`;
- `exp/v2-plan-chatgpt-sol-high`;
- canonical Plan Review records/audits;
- model/provenance clues elsewhere in repository history;
- previous chats.

If an exact factual check about Definition authority is needed, use only the frozen Definition checkpoint above.

## Fixed rubric

The rubric was fixed before either completed plan was examined.

Evaluate both plans on these ten dimensions:

1. **Requirement coverage quality** — not merely presence of PWV2-REQ-001..076 in a table, but real implementation ownership and bounded JIT where appropriate.
2. **ADR / accepted-DROP fidelity** — preserves ADR-PWV2-001..006 and does not accidentally reintroduce rejected V1 machinery.
3. **Milestone sequencing and dependency quality** — implementation order minimizes rework and respects prerequisites.
4. **YAGNI / proportionality** — avoids unnecessary abstractions/state/infrastructure while preserving current quality obligations.
5. **JIT boundary quality** — freezes what must be strategic now and deliberately defers implementation detail that should remain JIT.
6. **Migration / cutover safety** — V1->V2 transition, rollback/recovery/adoption and no permanent dual-state ambiguity.
7. **Validation quality** — automated A01-A17 and manual L01-L09 placement, evidence quality, and production gates.
8. **Recovery / integration / edge-case coverage** — external effects, review subjects, target movement, branch disappearance, cross-runtime continuation.
9. **Implementation actionability** — another capable context could execute the plan without redoing Strategic Planning.
10. **Context / complexity efficiency** — amount of plan/state/process complexity relative to the accepted problem.

## Evaluation method

For each dimension:
- give Plan A and Plan B a score from 1-10;
- cite concrete sections/examples from each candidate;
- distinguish **material correctness/strategy differences** from presentation/detail differences;
- identify any hidden contradiction with frozen Definition authority;
- identify any strategically valuable idea present in one and absent/weaker in the other.

Do not reward raw length, number of milestones, number of tables, or verbosity by itself.

Then provide:

### Coverage verification
- confirm whether each candidate truly covers all 76 requirements;
- confirm whether each candidate accounts for the full V1->V2 disposition matrix;
- confirm whether each candidate preserves A01-A17 and L01-L09;
- list any coverage that exists only nominally rather than executably.

### Structural comparison
- milestone count and conceptual decomposition;
- major dependency-order differences;
- key JIT-vs-upfront differences;
- migration/cutover differences;
- test/acceptance differences.

### Risk comparison
For each plan, list:
- top 5 implementation risks introduced by the plan itself;
- top 5 important risks it handles particularly well.

### Cross-pollination value
List the strongest ideas from Plan A that should be considered for the eventual canonical plan, and the strongest ideas from Plan B likewise.

### Overall judgment
Provide:
- overall weighted score out of 100 for each candidate;
- which candidate is stronger **as a Strategic Plan under this frozen Definition**, with concise reasoning;
- confidence: high / medium / low;
- whether the stronger plan should be used unchanged, or whether the best canonical result would benefit materially from importing specific ideas from the other candidate.

This comparison is not an Independent Plan Review and must not mutate either candidate.

## Allowed write

Write exactly one report:

`planning/experiments/judge/PWV2_PLAN_AB_COMPARISON_REPORT.md`

No other mutation is allowed.

## Completion boundary

After writing the complete comparison report:
- reread it;
- verify both candidates were evaluated under the same frozen authority and fixed rubric;
- STOP.

Do not reveal or infer model identities.
Do not modify canonical planning/review state.
Do not perform Independent Plan Review.
Do not continue into Execution Prep.
