# Intake — common pre-execution workflow core

Date: 2026-09-21
Workstream ID: `feature-common-preexecution-core`
Kind: `feature`
Status: `active`

## Operator intent

Explore whether the currently duplicated pre-execution lifecycle in `chatgpt_only` and `codex_only` should be consolidated into policy-neutral common contracts, while preserving only the real policy-specific differences as thin adapters.

The starting hypothesis is the current stages from Intake through Strategic Planning:
1. Intake
2. Brainstorming
3. Research
4. Brainstorming → Project Definition promotion gate
5. Project Definition
6. Strategic Planning

## Identity / base classification

- Integration target: `main`
- Base ref: `fd2dc95f539d982e1009d71bbf1301f3098900f6`
- Workstream branch: `feat/common-preexecution-core`
- Parent workstream: none
- Classification: independent workstream

Pre-creation branch discovery found no existing matching feature workstream/branch. The unrelated `work/fork-release-order-latest-alias` branch does not supply parent-only state required for this feature.

## Initial evidence

Direct comparison of current `main` policy-local modules shows:
- `BRAINSTORMING.md`: semantically the same except policy/session wording.
- `DEFINITION.md`: semantically the same except one stale/different pointer-description sentence.
- `RESEARCH.md`: common research lifecycle plus Codex-only Investigator runtime-realization/binding mechanics.
- `PLANNING.md`: common strategic-planning semantics plus policy-specific context-hygiene and independent plan-review transition mechanics.
- `INTAKE.md`: common intake lifecycle plus Codex-only orchestration-binding establishment/readback.

## Intake classification

Path: exploratory feature
Next route: `brainstorming:common-preexecution-core@R1`

The feature requires design exploration before Project Definition because the main open question is contract factoring: which semantics become truly policy-neutral authority and which remain policy adapters without introducing indirection or cross-policy coupling.
