# Review and Handoff

## Card close

A card is not done because an executor says it is done. Apply the Task Card Definition of Done contract and GitHub State Contract, then persist terminal state/result pointers in Task Board.

Do not edit Task Card contract files merely to mirror completion status.

## Milestone completion

All required cards being `done` is necessary but not sufficient.

Run integrated milestone acceptance against intended final milestone state.

- **RED:** create/reopen bounded corrective work; milestone is not done.
- **GREEN:** finalize publication/merge according to branch policy, persist acceptance evidence, write/update cumulative handoff, record exact implementation head/checkpoint in Task Board, then set Task Board milestone `done`.

A GREEN milestone may never remain `ready` or `in_progress` in Task Board.

## Independent review policy

Independence means the reviewer does not rely on the implementing worker/session narrative and re-reads durable repo/evidence from the exact subject.

- **REQUIRED** for high-risk work: security/auth, destructive/data migrations, difficult-to-reverse production/live configuration, important external-state protection boundaries or comparable risk.
- **RECOMMENDED** for major architecture, large refactors, complex state machines and broad cross-package changes.
- **OPTIONAL** for simple low-risk mechanical/docs changes.

Reviewer selection follows project policy:
- `chatgpt_only` → use a fresh independent normal ChatGPT chat when review is required/recommended;
- `codex_only` → use an independent Codex reviewer/worker/session that did not implement the reviewed subject; Codex Main remains accountable for exact-subject integration and evidence;
- `mixed` → use an independent reviewer path appropriate to the accepted review contract; prefer a different session/worker from implementation and do not reuse executor narrative as proof.

For high-risk external writes, place independent review at the last useful reversible checkpoint when practical, then perform write + post-write readback/verification.

Do not create a permanent review role or review every trivial Task Card.

## Milestone Acceptance Review vs Publication/PR Verification

These are different gates.

### Milestone Acceptance Review

Purpose: decide whether intended final milestone implementation is correct and satisfies approved acceptance contract.

- Runs on intended final implementation branch state before publication/merge when practical.
- Covers integrated behavior, architecture/contracts, required tests, migrations, rollback/external-state boundaries, frozen assets and milestone-specific evidence as applicable.
- Apply independent review policy above when required/recommended.
- Produces explicit verdict such as `GREEN / PR READY` or `RED / NOT PR READY`.
- If RED, create/reopen bounded corrective work and repeat acceptance only after corrective work closes.

### Publication/PR Verification

Purpose: verify that publication artifact is exactly already-accepted milestone state intended to be merged.

Verify as applicable:
- correct base/head branches;
- expected PR head/publication state;
- PR diff matches accepted implementation state and cumulative handoff;
- commits after reviewed implementation head are only authorized closure/publication changes;
- no unreviewed behavioral/scope drift;
- required status checks/CI/mergeability are understood;
- PR does not perform unauthorized deployment/external action.

Publication verification is intentionally lighter than Milestone Acceptance Review. Re-run substantive tests only when new evidence gives a concrete reason.

## Cumulative handoff

Canonical location: `project-handoffs/MXX_HANDOFF.md`.

A cumulative handoff is a summary of completed milestone truth, not live execution state. It must be sufficient for a fresh session to understand what became true and where to continue, while Task Board remains authoritative for current execution status.

Record as applicable:
- goal/status/checkpoint at completion;
- implemented behavior;
- accepted decisions;
- changed files/packages;
- schemas/migrations/APIs/contracts;
- side effects/idempotency/external readback;
- tests/results and independent review;
- known issues/deferred items;
- provenance/exact Git state;
- architecture reopen assessment;
- requirements satisfied/outstanding;
- next durable starting point;
- exact context needed by next executor/session.

A handoff does not replace Task Board, contracts, specs, evidence or exact Git objects.

## Finalization and checkpoint

When a milestone uses a PR:
1. run Milestone Acceptance Review on intended final implementation branch state;
2. if GREEN / PR READY, open PR according to branch policy;
3. run Publication/PR Verification against actual PR artifact;
4. merge/finalize only after required approval/checks;
5. reconcile Task Board and handoff to actual final merged state;
6. a small closure documentation commit is allowed when required;
7. Task Board `checkpoint` and `implementation_head` identify final verified state.

## Next-milestone continuation

After a GREEN checkpoint:

### `chatgpt_only`

ChatGPT remains fixed executor. If next milestone is already approved and no strategic/user/deployment gate intervenes, continue automatically through just-in-time execution prep + fresh Refresh Gate. Do not run Capability Gate.

### `codex_only`

Codex remains fixed executor. Codex Main may continue automatically into the next already-approved milestone, including deterministic just-in-time execution prep, without returning to ChatGPT merely for routing. Stop only for real strategic/user/authorization/capability/evidence blockers or when approved scope ends.

### `mixed`

The next new execution assignment returns to normal ChatGPT Capability Gate. Previous executor is not inherited automatically.

A session recommendation for fresh context is context hygiene, not product authorization.

## System verification and cutover

Independent system verification should act as its own gate when required. Deployment/cutover/migration should be runbook- or Task-Card-driven rather than improvised from chat. Runbooks/checklists do not automatically require OpenSpec unless they change a behavior contract.

Explicit deployment/live-write authorization remains a hard stop regardless of execution policy.
