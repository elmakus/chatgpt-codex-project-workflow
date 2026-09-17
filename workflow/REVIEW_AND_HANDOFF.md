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

Independence means the reviewer did not implement the reviewed subject, does not rely on implementing-session narrative, and re-reads durable repo/evidence from the exact review subject.

- **REQUIRED** for high-risk work: security/auth, destructive/data migrations, difficult-to-reverse production/live configuration, important external-state protection boundaries or comparable risk.
- **RECOMMENDED** for major architecture, large refactors, complex state machines and broad cross-package changes.
- **OPTIONAL** for simple low-risk mechanical/docs changes.

Reviewer selection follows project policy:
- `chatgpt_only` → required/recommended independent review uses a **fresh normal ChatGPT chat** that did not implement the subject;
- `codex_only` → Codex Main obtains an independent Codex reviewer worker/session that did not implement the reviewed subject; when installed/enabled, `codex_workflow` governs the internal reviewer-worker/session mechanics;
- `mixed` → use an independent reviewer path appropriate to the accepted review contract; the reviewer must not be the implementing worker/session for that subject.

### `chatgpt_only` hard review handoff

A normal ChatGPT chat cannot review its own implementation when review is REQUIRED or RECOMMENDED.

When an implementing ChatGPT chat reaches such a review boundary it must:
1. freeze/persist the exact review subject and all implementation/test evidence;
2. set the relevant Task Board `review_state: pending`, `review_subject: <exact sha/subject>` and review-evidence pointer when available;
3. commit/push durable state when possible;
4. **stop before issuing the independent verdict**;
5. report `USER ACTION REQUIRED: start a fresh normal ChatGPT chat for independent review from implementation/TASK_BOARD.yaml`.

The fresh review chat:
1. recovers Task Board and exact `review_subject`;
2. sets `review_state: in_progress` when it begins the review;
3. independently reads the exact subject/contracts/evidence;
4. persists a GREEN/RED review verdict and evidence;
5. sets `review_state: green | red` and `review_evidence` in Task Board.

After GREEN, that fresh chat may continue subsequent deterministic `chatgpt_only` execution if normal continuation conditions hold. If it later implements a new subject that itself requires/recommends independent review, another fresh ChatGPT chat is required for that later review.

### `codex_only` review continuity

A required/recommended review is **not** a user handoff solely because review is independent. Codex Main remains coordinator and uses an independent reviewer worker/session according to installed `codex_workflow` (or native Codex mechanisms when that workflow is unavailable), while Project Workflow requires only the project-level facts: exact subject, reviewer independence, verdict/evidence and Task Board review state.

Codex Main must not let the implementing worker review its own subject, and worker review completion is not milestone acceptance until Main integrates the verdict into durable project state.

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

ChatGPT remains fixed executor. If next milestone is already approved and no strategic/user/deployment gate intervenes, continue automatically through just-in-time execution prep + fresh Refresh Gate **after every required/recommended independent review gate is GREEN**. Do not run Capability Gate.

A chat that implemented the subject must stop at its required/recommended review boundary as defined above; project continuation resumes in the fresh review chat after GREEN.

### `codex_only`

Codex remains fixed executor. Codex Main may continue automatically into the next already-approved milestone, including deterministic just-in-time execution prep, without returning to ChatGPT merely for routing or independent review. Stop only for real strategic/user/authorization/runtime blockers or when approved scope ends.

### `mixed`

The next new execution assignment returns to normal ChatGPT Capability Gate. Previous executor is not inherited automatically.

A session recommendation for fresh context is context hygiene, not product authorization. The `chatgpt_only` fresh-review requirement above is different: it is a real independence gate.

## System verification and cutover

Independent system verification should act as its own gate when required. Deployment/cutover/migration should be runbook- or Task-Card-driven rather than improvised from chat. Runbooks/checklists do not automatically require OpenSpec unless they change a behavior contract.

Explicit deployment/live-write authorization remains a hard stop regardless of execution policy.
