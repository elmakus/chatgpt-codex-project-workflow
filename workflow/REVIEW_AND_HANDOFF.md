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

## Milestone Acceptance Review vs Publication/PR Verification

These are two different gates and must not be conflated.

### Milestone Acceptance Review

Purpose: decide whether the intended final milestone implementation is correct and satisfies its approved acceptance contract.

- Runs on the intended final implementation branch state **before publication/merge**; when a PR workflow is used, prefer completing this review before opening the PR unless project policy requires otherwise.
- Covers integrated behavior, architecture/contracts, required tests, migrations, rollback/external-state boundaries, frozen assets and milestone-specific acceptance evidence as applicable.
- Apply the independent review policy above when required or recommended.
- Produces an explicit milestone verdict such as `GREEN / PR READY` or `RED / NOT PR READY`.
- If RED, create/reopen bounded corrective work and repeat acceptance only after that corrective work closes.

This is the substantive final review of the milestone. Opening a PR does not replace it.

### Publication/PR Verification

Purpose: verify that the publication artifact is exactly the already-accepted milestone state that is intended to be merged.

Run after the PR is opened and before merge. Verify as applicable:

- correct base and head branches;
- expected PR head SHA / publication branch state;
- PR diff matches the accepted implementation state and cumulative handoff;
- any commits after the reviewed implementation head are only authorized closure/publication changes;
- no unreviewed behavioral or scope drift was introduced;
- required status checks / CI and mergeability are understood;
- the PR does not perform an unauthorized deployment or other external-state action.

Publication/PR Verification is intentionally lighter than Milestone Acceptance Review. **Do not repeat the full milestone acceptance suite by default.** Re-run substantive tests or acceptance review only when the PR/publication diff, new commits, failed checks or other evidence create a concrete reason to doubt the accepted state.

If publication verification finds material drift from the accepted state, stop publication. Do not approve the merge by merely reviewing the PR diff; return to the appropriate corrective/acceptance path.

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
1. run Milestone Acceptance Review on the intended final implementation branch state;
2. if GREEN / PR READY, open the PR according to branch policy;
3. run Publication/PR Verification against the actual PR artifact;
4. merge/finalize only after required publication approval and checks;
5. reconcile the handoff to the actual final merged state;
6. a small closure documentation commit is allowed when required;
7. recorded checkpoint and `implementation_head` identify final verified state.

The next milestone starts from that GREEN checkpoint and re-runs Capability Gate for its first executable card; it does not automatically inherit the previous executor.

## System verification and cutover

Independent system verification should act as its own gate when required. Deployment/cutover/migration should be runbook- or Task-Card-driven rather than improvised from chat. Runbooks/checklists do not automatically require OpenSpec unless they change a behavior contract.
