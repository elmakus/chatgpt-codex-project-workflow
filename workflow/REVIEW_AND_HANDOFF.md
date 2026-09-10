# Review and Handoff

## Card close

A card is not done because an agent says it is done. Apply the Task Card Definition of Done and GitHub State Contract.

## Milestone completion

All cards being `done` is necessary but not sufficient.

Run integrated milestone acceptance against the final milestone branch state.

- **RED:** create/reopen bounded corrective work; milestone is not done.
- **GREEN:** finalize publication/merge according to branch policy, persist acceptance evidence, write/update the cumulative handoff, record the exact implementation head/checkpoint, then set the milestone `done`.

A green milestone may never remain `ready`. Its terminal durable state must be explicit.

## Cumulative handoff

The canonical project handoff location is `project-handoffs/MXX_HANDOFF.md`.

A cumulative handoff must be sufficient for a fresh session to start without the prior chat. It records, as applicable:

- goal, status and checkpoint;
- implemented behavior;
- accepted decisions;
- changed files/packages;
- schemas/migrations;
- APIs/contracts;
- side effects/idempotency;
- tests/results;
- known issues;
- deferred items;
- provenance;
- exact Git state;
- architecture reopen assessment;
- requirements satisfied;
- outstanding requirements;
- next starting point;
- exact context needed by the next Codex.

A handoff summarizes durable truth; it does not replace Task Board, cards, specs, evidence or exact Git objects.

## Finalization and checkpoint

When a milestone uses a PR:
1. integrated acceptance is performed on the intended final branch state;
2. merge/finalization follows project policy;
3. the handoff is reconciled to the actual final state;
4. if a small closure documentation commit is required, it is allowed;
5. the recorded checkpoint and `implementation_head` must identify the final verified state.

The next milestone starts from that green checkpoint.

## System verification and cutover

Independent system verification should act as its own gate when the project requires it.

Deployment/cutover/migration should be runbook- or Task-Card-driven rather than improvised from chat. It may be represented by dedicated milestones or cards. Runbooks/checklists do not automatically require OpenSpec unless they change a behavior contract.
