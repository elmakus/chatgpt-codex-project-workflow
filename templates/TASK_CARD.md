# MXX-TYY — <title>

- Milestone: `MXX`

> This file is the Task Card **contract**, not live state. Decision/execution status, assigned executor, lane/base pointers, review state and result/evidence pointers live only in `implementation/TASK_BOARD.yaml`.

## Authority slice

Use exact durable references at the smallest practical granularity.

- Master Plan / milestone contract: `<planning/MASTER_PLAN.md#... | implementation/milestones/MXX.md#...>`
- Requirements: `<IDs/paths>`
- Accepted decisions: `<IDs/paths>`
- Relevant OpenSpec: `<path | none>`
- Accepted dependency results: `<card/result/evidence refs | none>`

### Must preserve

List every applicable invariant, accepted behavior/architecture choice, failure semantic, compatibility rule, external-write boundary or other constraint that could change implementation or acceptance.

...

### Must not / rationale that must travel (only when material)

Use when a competent downstream executor could otherwise choose a different path than the approved one.

...

> Delegation may reduce context volume, not authoritative constraints. A downstream executor/reviewer must either receive every applicable constraint explicitly or read the exact referenced authority before acting. Summary text never overrides exact authority.

## Dependencies

- `<MXX-T.. | exact predecessor milestone/result | none>`

If this card was created JIT from predecessor evidence, include that exact accepted result in the Authority slice above. Do not create this card before its scope is sufficiently knowable.

## Outcome

...

## Scope

### Included
...

### Excluded
...

## Acceptance

...

## Required tests / checks

...

## Optional execution hints

Delete fields that do not add execution value.

- Priority: `HIGH | MEDIUM | LOW`
- Complexity: `HIGH | MEDIUM | LOW`
- Phase: `<phase>`
- Expected/relevant code locations:
  - `<path>`
- Required capabilities:
  - `<only unusual/external/high-risk/routing-significant capability>`

Under `chatgpt_only` / `codex_only`, capability hints do not trigger preflight. Under `mixed`, material capability hints may affect Capability Gate routing.

## Parallel execution (only when applicable)

- parallel_safe: `true`
- write_scope:
  - `<repo-relative path/glob; empty only for genuinely read-only work>`
- exclusive_resources:
  - `<shared mutable fixture/service/external target | none>`

Project-global Task Board/milestone integration/review state remains coordinator-owned and must not be placed in lane-worker write scope.

## External write/readback needs (only when material)

`none` or exact target + expected readback/verification. Mutable external targets shared across parallel cards also belong in `exclusive_resources`.

## Independent review (only when material)

`REQUIRED | RECOMMENDED` plus rationale.

- `chatgpt_only`: implementing chat stops at the review boundary; a fresh normal ChatGPT chat reviews the exact durable subject.
- `codex_only`: Codex Main uses an independent reviewer worker/session; installed `codex_workflow` governs reviewer orchestration.
- `mixed`: reviewer path follows accepted routing/review contract.

Reviewer must never be the implementing worker/session for the reviewed subject and must verify against the same applicable authority slice.

## Contract overrides (optional)

Workflow-standard runtime behavior, Refresh Gate, blocker handling, evidence rules and Definition of Done are inherited from `workflow/contracts/TASK_EXECUTION.md` and `workflow/EXECUTION.md`. `TASK_CARDS.md` governs authoring/decomposition, not ordinary execution.

Record only material card-specific overrides here. Do not copy standard workflow text merely to fill sections.
