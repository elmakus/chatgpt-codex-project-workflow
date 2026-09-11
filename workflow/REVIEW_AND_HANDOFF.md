# Review and Handoff

## Card and milestone close

A card is not done because an executor says so. Apply Task Card Definition of Done and the GitHub State Contract.

All required cards being `done` is necessary but not sufficient for a milestone. Run integrated milestone acceptance on the intended final state.

- RED: create/reopen bounded corrective work.
- GREEN: finalize publication/merge, persist acceptance evidence, reconcile cumulative handoff and exact implementation head/checkpoint, then set the milestone `done`.

## Independent review policy

Use a fresh independent ChatGPT chat that reads durable repo/evidence rather than relying on the executor's narrative:

- **REQUIRED** for high-risk changes: security/auth, destructive/data migrations, hard-to-reverse production/live configuration, important external-state boundaries, or comparable risk.
- **RECOMMENDED** for large architecture changes, major refactors, complex state machines and broad cross-package work.
- **OPTIONAL** for simple low-risk mechanical/docs changes.

For a high-risk external write, place the independent review at the last useful reversible checkpoint when practical, then perform the write and post-write readback/verification.

Do not create a permanent review-agent role or require independent review after every card.

## Cumulative handoff

Canonical location: `project-handoffs/MXX_HANDOFF.md`.

It must let a fresh ChatGPT chat or Codex session recover without prior conversation. Record as applicable goal/status/checkpoint, implemented behavior, decisions, changed areas, schemas/APIs, side effects, tests, evidence, known issues, deferred items, provenance, exact Git state, architecture reopen assessment, requirements satisfied/outstanding and the next durable starting point.

The handoff summarizes durable truth; it does not replace Task Board, cards, specs, evidence or exact Git objects.

## Next executor

Do not assume the next milestone goes to Codex. The next ChatGPT chat reads `PROJECT.md`, applies progressive disclosure and, at execution time, runs the Capability Gate under `execution_policy`.

## System verification and cutover

Independent system verification should be its own gate when the project requires it. Deployment/cutover/migration should be runbook- or Task-Card-driven rather than improvised from chat.
