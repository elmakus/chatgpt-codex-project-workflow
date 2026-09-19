# M01 final integration refresh and acceptance — 2026-09-19

Workstream: `feature-branch-delete-prefix`
Pull request: `#34`
Integration target: `main`

## Refreshed target state

- Current target at this refresh: `main@f368b8a33e50cacf46a39c1a9697f4a9be077fe7`.
- Reviewed behavioral implementation subject: `6441fa08a6a6e94fc568ec4804e12582e2adcd96` plus the exact M01-T01 acceptance surface frozen in Task Board review state.
- Current PR source head before closure-package bookkeeping: `841a987ebe108f442855352d05d704549e1351a3`.
- Target movement since Card review consists of the integrated `codex_only` namespace plus later terminal state reconciliation for that separate workstream.
- Of the M01 behavioral files, target movement overlaps only `README.md`. The target-owned README changes are separate codex-only sections; the branch-cleanup hunks merge cleanly and remain semantically unchanged.
- GitHub PR #34 is mergeable. The GitHub virtual merge result at this refresh is `b3ba35f0a6ff11edc07943a9ce0c343af4c1f8b2`.
- Diff/readback of that virtual merge shows no `workflow/codex_only/*` or `workflow/CONTEXT_ROUTING.md` change attributable to PR #34, and `git diff --check` is clean.

## Integrated milestone acceptance

M01 acceptance: GREEN.

The milestone contains one implementation Card, M01-T01. Its stable acceptance contract owns BC-R1 through BC-R12 and the whole approved M01 outcome. M01-T01 is terminal with fresh independent GREEN review on the frozen behavioral subject. No Card, Research, blocker, parent/stacked dependency, strategic decision or authorization gate remains.

The refreshed virtual merge preserves:
- source-branch-independent final-target closure/recovery;
- closure-ready pre-merge durability and target-side post-merge reconciliation;
- exact workstream-local `branch_cleanup` fallback with stale-head protection;
- prohibition on `delete/*` / same-SHA rename emulation;
- stacked-parent recovery after source deletion;
- legacy/default compatibility;
- Codex-only policy isolation.

## Distinct workstream final-integration review coverage

Manifest final-integration review is RECOMMENDED and distinct from the Card review lifecycle.

Coverage reuse is valid because:
1. M01-T01 is the only implementation Card in this workstream.
2. The Card acceptance surface explicitly covers the whole BC-R1 workstream acceptance and was designed to be eligible for manifest coverage reuse.
3. The independent Card review checked the exact frozen behavioral subject plus all BC-R1..BC-R12 acceptance.
4. Post-review commits are review/state/evidence/closure bookkeeping only and do not alter the covered ChatGPT-only behavior.
5. Current-target movement changes separate Codex-only behavior and unrelated target-owned README sections; the workstream-owned branch-cleanup behavior is unchanged.
6. The current virtual merge is conflict-free and preserves both the target's Codex-only README additions and the reviewed branch-cleanup README hunks.

Therefore the manifest final-integration gate may be reconciled GREEN with `covered_by` pointing to the exact independent M01-T01 review evidence. This is coverage reuse, not a second independent verdict.

## Pre-merge condition

Before merge, the source branch must contain the closure-ready namespaced package (manifest, Task Board, Card, evidence and M01 handoff). Immediately before merge, re-read current `main`, PR #34 head/mergeability and the virtual merge result. If target movement or reconciliation materially changes the covered branch-cleanup behavior or acceptance surface, this coverage is stale and a new exact review subject is required.
