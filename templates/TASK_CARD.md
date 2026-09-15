# MXX-TYY — <title>

- Decision state: `ACCEPTED | DEFERRED | REJECTED | REVIEW`
- Execution status: `PLANNED | READY | IN_PROGRESS | BLOCKED | DONE | SUPERSEDED`
- Executor: `null | chatgpt | codex`
- Milestone: `MXX`
- Priority: `HIGH | MEDIUM | LOW`
- Complexity: `HIGH | MEDIUM | LOW`
- Phase: `<phase>`

## Dependencies

- `<MXX-T.. | none>`

## Expected code locations

- `<path>`

## Parallel execution (optional)

Delete this section for ordinary serial-only cards. `parallel_safe: true` is valid only when mutable ownership and external resources are bounded enough to run beside another compatible READY card.

- parallel_safe: `true | false`
- write_scope:
  - `<repo-relative path/glob; empty only for genuinely read-only work>`
- exclusive_resources:
  - `<shared mutable fixture/service/external target | none>`

Project-global Task Board/milestone integration state remains coordinator-owned and must not be placed in a lane worker's write scope.

## Required capabilities (optional)

List only unusual/external/high-risk/routing-significant capabilities. Delete this section when ordinary capabilities are obvious.

- `<capability>`

## Canonical sources

- Requirements: `<IDs/paths>`
- Accepted decisions: `<paths>`
- Master Plan: `<section/path>`
- Latest cumulative handoff: `<path | none>`

## OpenSpec

- Required/candidate: `required | candidate | skip`
- Change: `<openspec/changes/... | none>`

## Outcome

...

## Scope

### Included
...

### Excluded
...

## Constraints

...

## Acceptance

...

## Required tests / checks

...

## External write/readback needs

`none` or exact target + expected readback/verification. If a mutable external target must be serialized across parallel cards, also list it under `exclusive_resources`.

## Independent review (only when material)

`REQUIRED | RECOMMENDED` plus rationale. Omit this section for ordinary low-risk cards where review is optional by default.

## Refresh Gate

Before implementation compare actual integration branch/HEAD/current state, exact lane base/workspace when parallel, latest handoff, milestone/Task Board, this card, relevant requirements/decisions/plan/OpenSpec, dependencies, actual interfaces, capability/evidence requirements and recorded parallel-ownership assumptions.

Implementation-detail drift inside accepted contracts may be reconciled. Material strategic drift, unexpected mutable ownership overlap or inability to satisfy required capability/evidence blocks the affected card/lane.

## Result

Fill before `DONE`:

- result_commit:
- result_pr:
- evidence:
- tests_summary:

For parallel execution, evidence also records the lane base/branch or equivalent isolated workspace and post-integration verification target.

## Definition of Done

- [ ] Included scope complete
- [ ] Acceptance satisfied
- [ ] Required tests/checks executed
- [ ] Tests green or authorized exception recorded
- [ ] Relevant OpenSpec satisfied
- [ ] No hidden blocker
- [ ] Result durable in Git
- [ ] Parallel lane integrated and post-integration verification green when applicable
- [ ] Task Board reconciled
- [ ] Executor/result pointers recorded
- [ ] Evidence identifies exact verification
- [ ] Material external writes read back/verified where required
- [ ] No unassigned TODO in accepted scope
