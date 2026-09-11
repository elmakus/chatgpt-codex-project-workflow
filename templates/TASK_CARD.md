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

`none` or exact target + expected readback/verification.

## Independent review (only when material)

`REQUIRED | RECOMMENDED` plus rationale. Omit this section for ordinary low-risk cards where review is optional by default.

## Refresh Gate

Before implementation compare actual branch/HEAD/current state, latest handoff, milestone/Task Board, this card, relevant requirements/decisions/plan/OpenSpec, dependencies, actual interfaces and capability/evidence requirements.

Implementation-detail drift inside accepted contracts may be reconciled. Material strategic drift or inability to satisfy required capability/evidence blocks the card.

## Result

Fill before `DONE`:

- result_commit:
- result_pr:
- evidence:
- tests_summary:

## Definition of Done

- [ ] Included scope complete
- [ ] Acceptance satisfied
- [ ] Required tests/checks executed
- [ ] Tests green or authorized exception recorded
- [ ] Relevant OpenSpec satisfied
- [ ] No hidden blocker
- [ ] Result durable in Git
- [ ] Task Board reconciled
- [ ] Executor/result pointers recorded
- [ ] Evidence identifies exact verification
- [ ] Material external writes read back/verified where required
- [ ] No unassigned TODO in accepted scope
