# M04 Milestone Acceptance — Worktree, stacked branch and integration refresh contracts

Milestone: `M04`
Result: `GREEN`
Accepted implementation subject: `38955588da57039183b0c15a3cd55fbf8b384e80`
Independent Card review: GREEN — `implementation/evidence/M04-T01-review-01.md`

## Integrated acceptance

Verified against the approved M04 milestone contract, M04-T01 Card contract, requirements R7/R8/R9/R10/R11/R12/R14/R15, acceptance scenarios A/B/E, the accepted branch-isolated-workstream ADR, and accepted M01–M03 dependency state.

GREEN:
- concurrent local mutation requires separate worktrees/equivalent isolated checkouts while remote-only GitHub execution remains exempt;
- stacked workstreams durably record parent identity plus the exact parent-only dependency and cannot integrate to the final target as independent while required parent-only content is absent;
- legal stacked integration supports child → parent folding or parent-first integration followed by child refresh/reconciliation;
- final integration compares against the current target, reconciles only material drift inside accepted authority, reruns affected verification, detects textual and material semantic conflicts, and repeats the gate if the target moves again before merge;
- exact-subject review semantics are preserved: target movement/ancestry alone does not invalidate GREEN; materially changed covered content/behavior or acceptance surface requires a new frozen subject and fresh independent review;
- file overlap alone is not a blocker and no unrelated workstream Task Board is inspected/mutated merely because another branch is active;
- M03 Card/milestone review ownership remains Task-Board-local while workstream final-integration review remains manifest-owned;
- legacy/default single-workstream mode remains legal and no global mutable registry/scheduler or foreign-policy execution semantics were added.

## Verification and publication state

- Workflow `main` remains exactly `03035876f3283d33e8a10ff43265f5be21a27a06`; no workflow-authority drift invalidated M04 assumptions.
- Exact M04 behavior delta from `e85acd6aa9a87dc9ab7ac52aa01190aa647d8aba` to the accepted subject changes only `CLOSE.md`, `INTAKE.md`, `REPOSITORY.md`, `WORKSTREAMS.md`, and `WORKSTREAM_TEMPLATE.yaml`.
- Post-subject branch commits through Card finalization change only Task Board/evidence state; no implementation/behavioral drift was introduced after the reviewed subject.
- The accepted subject has no reported combined CI statuses; no CI-execution claim is made.
- PR #28 remains draft/open against `main`; it is intentionally not merged at this milestone because approved scope continues through M05.
- No deployment or material external runtime write is part of M04 close.

## Result

M04 is GREEN and may be closed at implementation checkpoint `38955588da57039183b0c15a3cd55fbf8b384e80`.
