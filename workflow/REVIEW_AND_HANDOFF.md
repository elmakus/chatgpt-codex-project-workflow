# Review and Handoff

## Card close

A card is not done because an executor says it is done. Apply Task Card Definition of Done and GitHub State Contract.

## Milestone completion

All required cards being `done` is necessary but not sufficient.

Run integrated milestone acceptance against intended final milestone state.

- **RED:** create/reopen bounded corrective work; milestone is not done.
- **GREEN:** finalize publication/merge according to branch policy, persist acceptance evidence, write/update cumulative handoff, record exact implementation head/checkpoint, then set milestone `done`.

A green milestone may never remain `ready`. Its terminal durable state must be explicit.

## Independent review policy

Use a fresh independent **normal ChatGPT chat** that reads durable repo/evidence rather than relying on executor narrative:

- **REQUIRED** for high-risk work: security/auth, destructive/data migrations, difficult-to-reverse production/live configuration, important external-state protection boundaries, or comparable risk.
- **RECOMMENDED** for major architecture, large refactors, complex state machines and broad cross-package changes.
- **OPTIONAL** for simple low-risk mechanical/docs changes.

For high-risk external writes, place independent review at the last useful reversible checkpoint when practical, then perform write + post-write readback/verification.

Do not create a permanent review role or review every trivial Task Card.

## Cumulative handoff

Canonical location: `project-handoffs/MXX_HANDOFF.md`.

A cumulative handoff must be sufficient for a fresh ChatGPT chat or Codex session to start without prior conversation. Record as applicable:
- goal/status/checkpoint;
- implemented behavior;
- accepted decisions;
- changed files/packages;
- schemas/migrations/APIs/contracts;
- side effects/idempotency/external readback;
- tests/results and independent review;
- known issues/deferred items;
- provenance and exact Git state;
- architecture reopen assessment;
- requirements satisfied/outstanding;
- next durable starting point;
- exact context needed by the next executor/session.

A handoff summarizes durable truth; it does not replace Task Board, cards, specs, evidence or exact Git objects.

## Finalization and checkpoint

When a milestone uses a PR:
1. integrated acceptance runs on intended final branch state;
2. merge/finalization follows project policy;
3. handoff is reconciled to actual final state;
4. a small closure documentation commit is allowed when required;
5. recorded checkpoint and `implementation_head` identify final verified state.

The next milestone starts from that GREEN checkpoint and re-runs Capability Gate for its first executable card; it does not automatically inherit the previous executor.

## System verification and cutover

Independent system verification should act as its own gate when required. Deployment/cutover/migration should be runbook- or Task-Card-driven rather than improvised from chat. Runbooks/checklists do not automatically require OpenSpec unless they change a behavior contract.
