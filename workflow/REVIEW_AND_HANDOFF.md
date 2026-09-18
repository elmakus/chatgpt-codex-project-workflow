# Review and Handoff

## Card close

A card is not done because an executor says it is done. Apply `workflow/contracts/TASK_EXECUTION.md` Definition of Done. Load `GITHUB_STATE.md` additionally only when coordinator/parallel/milestone-close/state-consistency semantics are involved, then persist terminal state/result pointers in Task Board.

For a simple reproducible card, exact result pointers plus a concise `tests_summary` may be sufficient closure evidence. Create a standalone evidence artifact when the proof is materially richer or independently useful: milestone integrated acceptance, REQUIRED/RECOMMENDED independent review, baseline/authorized exception, material external write/readback, complex multi-stage verification, or an explicit contract requirement.

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
5. report `USER ACTION REQUIRED: start a fresh normal ChatGPT chat for independent review from implementation/TASK_BOARD.yaml`;
6. in the same response, include the minimal copy-paste-ready `NEW CHAT START PROMPT` defined below.

### Fresh Chat start prompt

Any mandatory or recommended fresh-ChatGPT handoff must be self-contained for the user's copy/paste action but **must not duplicate durable state**. Canonical reusable shape: `prompts/CHATGPT_FRESH_SESSION.md`.

Use this shape:

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/implementation branch>.
Kontynuuj: <pending independent review for MXX-TYY | exact concise continuation goal>.
Durable start pointer: <implementation/TASK_BOARD.yaml | exact durable pointer>.
Odtwórz aktualny stan, exact review_subject/authority slice/evidence z repo i wykonaj tylko legalny następny krok. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

Rules:
- include repository, exact active project/implementation branch and exact continuation target;
- include the smallest durable start pointer;
- do not paste test counts, SHAs, evidence prose, changed-file lists or implementation summary when recoverable from repo;
- do not ask the user to separately request a start prompt;
- if the fresh chat is only recommended for context hygiene, say so outside the fenced prompt; the prompt itself remains a minimal durable-state recovery instruction.

The fresh review chat:
1. recovers Task Board and exact `review_subject`;
2. sets `review_state: in_progress` when it begins the review;
3. independently reads the exact subject/contracts/evidence;
4. persists a GREEN/RED review verdict and evidence;
5. sets `review_state: green | red` and `review_evidence` in Task Board.

### RED review → automatic bounded remediation under `chatgpt_only`

A RED verdict is **not itself a user stop** when corrective work is already bounded, deterministic and authorized by durable project state.

After persisting RED, the fresh reviewer chat must immediately continue in the **same chat turn** when all are true:
- `execution_policy: chatgpt_only`;
- Task Board / accepted authority identifies bounded corrective work, or the reviewer can create/reopen a bounded corrective card without changing strategic authority;
- remediation is L1/L2 implementation detail, not an L3 strategic/product/architecture decision;
- no explicit user/deployment/live-write/authorization gate is due;
- no concrete runtime blocker prevents the remediation.

In that case:
1. persist the RED review evidence/state first;
2. leave review-only mode and route into normal ChatGPT execution;
3. load the normal ChatGPT execution route/contracts required by the corrective card;
4. perform the remediation immediately;
5. run required checks and persist the corrected result;
6. freeze the **new exact remediation subject**;
7. set the required/recommended review gate back to `review_state: pending` with the new subject/evidence;
8. stop **only now**, before re-reviewing the subject this chat just implemented;
9. in the same final user-facing response, explain the result concisely and include the ready-to-copy branch-aware `NEW CHAT START PROMPT` for fresh independent re-review.

Do **not** end the turn after RED merely to say that remediation is next or that it has not been started. A user response at that intermediate point would unnecessarily require the user to send “continue”.

If remediation hits a real strategic/user/authorization/runtime blocker, stop there and report the smallest required action instead.

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

A cumulative handoff is a compact summary of completed milestone truth, not live execution state. It must be sufficient for a fresh session to understand what became true and where to continue, while Task Board remains authoritative for current execution status.

Record the minimum durable continuation set:
- completed checkpoint and exact implementation head;
- achieved behavior/state;
- accepted authority now in force, preferably by exact requirement/decision/plan/OpenSpec refs;
- concise verification/review/external-readback results with exact evidence pointers;
- only material exceptions/deferred items;
- next durable starting point, required prior checkpoint, authority slice and any explicit authorization gate.

Add schema/API/migration details, changed-package/file notes, idempotency facts or architecture-reopen assessment only when they materially affect later work. Do not copy ordinary Git inventories or mirror Task Board fields simply because a template section exists.

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
