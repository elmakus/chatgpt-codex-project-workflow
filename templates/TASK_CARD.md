# MXX-TYY — <title>

- Decision state: `ACCEPTED | DEFERRED | REJECTED | REVIEW`
- Execution status: `PLANNED | READY | IN_PROGRESS | BLOCKED | DONE | SUPERSEDED`
- Milestone: `MXX`
- Priority: `HIGH | MEDIUM | LOW`
- Complexity: `HIGH | MEDIUM | LOW`
- Phase: `<phase>`

## Dependencies

- `<MXX-T.. | none>`

## Expected code locations

- `<path>`

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

## Required tests

...

## Refresh Gate

Before implementation compare:
1. actual branch/HEAD/working tree;
2. latest cumulative handoff;
3. current milestone and Task Board;
4. this Task Card;
5. relevant requirements, accepted decisions and Master Plan sections;
6. relevant OpenSpec;
7. completed dependencies;
8. actual code locations/interfaces.

If only implementation detail drifted within accepted contracts, reconcile it. If behavior/architecture/requirement/external-contract/milestone-acceptance drift is material, set `BLOCKED`, persist evidence and use strategic escalation.

## Strategic escalation rule

Do not continue dependent work across a strategic blocker. Follow `workflow/contracts/CHATGPT_CODEX.md`.

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
- [ ] Tests green or authorized baseline exception recorded
- [ ] Relevant OpenSpec requirements satisfied
- [ ] No hidden blocker
- [ ] Result durable in Git
- [ ] Task Board reconciled
- [ ] Result pointers recorded
- [ ] Evidence identifies exact checks/review
- [ ] Side effects/idempotency reconciled where relevant
- [ ] No unassigned TODO in accepted scope
