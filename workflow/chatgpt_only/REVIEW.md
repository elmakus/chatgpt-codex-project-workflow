# ChatGPT-only Independent Review

Independent review is performed by a fresh normal ChatGPT chat that did not implement the exact reviewed subject.

## Review levels

- **REQUIRED** — high-risk work such as security/auth, destructive/data migration, difficult-to-reverse live configuration, important external-state protection boundary or comparable risk.
- **RECOMMENDED** — major architecture, large refactor, complex state machine or broad cross-package change.
- **OPTIONAL** — simple low-risk work unless project explicitly activates review.

## Required read set

Read:
- project `PROJECT.md`;
- Task Board;
- exact active branch;
- exact `review_subject`;
- reviewed Task Card or milestone contract;
- the same authority slice that governed implementation;
- required evidence referenced for review;
- actual reviewed diff/source/runtime needed to judge subject.

Read `workflow/common/OPENSPEC.md` only when reviewed authority points to OpenSpec or verdict depends on it.

Read prior handoff/dependency/research/external readback only when reviewed authority/acceptance references it.

Do not use previous implementing-chat narrative as review evidence.

## Review lifecycle

1. Recover exact subject from Task Board.
2. Set `review_state: in_progress`.
3. Independently inspect exact subject/contracts/evidence.
4. Verify acceptance and applicable authority.
5. Persist concise durable GREEN/RED review evidence.
6. Set `review_state: green | red` + evidence pointer.

Do not mutate reviewed subject while judging it.

## GREEN

If GREEN:
- persist verdict/state first;
- if deterministic later work is already legal, continue automatically through router;
- do not stop merely to report GREEN unless a real boundary requires user action.

If this chat later implements a new reviewable subject, it becomes the implementing chat for that new subject and must stop at its fresh-review boundary.

## RED → automatic bounded remediation

RED is not itself a user stop when corrective work is bounded, deterministic, authorized and unblocked.

After persisting RED, continue in the **same turn** when:
- Task Board/accepted authority identifies bounded corrective work, or reviewer can create/reopen a bounded corrective Card without changing strategic authority;
- remediation is L1/L2 implementation detail;
- no explicit user/deployment/live-write authorization gate is due;
- no concrete runtime blocker prevents remediation.

Then:
1. persist RED evidence/state;
2. leave review-only mode;
3. load `EXECUTION_PREP.md` if bounded corrective Card must be created/reopened/reconciled;
4. load `EXECUTION.md` + `STATE.md`;
5. perform remediation immediately;
6. run required checks and persist corrected result;
7. freeze new exact remediation subject;
8. set review back to `pending`;
9. stop only now, before self-reviewing corrected subject;
10. include ready-to-copy fresh independent re-review prompt.

Do **not** end the turn after RED merely to say remediation is next or not started.

Stop earlier only for a real strategic/user/authorization/runtime blocker or when corrective scope cannot safely be bounded.

## High-risk external writes

When practical, place REQUIRED/RECOMMENDED independent review at the last useful reversible checkpoint before a high-risk external write.

After GREEN, perform the authorized write plus required post-write readback/verification.

Do not create a permanent review role or independently review every trivial Card.

## Fresh-review prompt

Whenever a fresh independent review is required, final response includes:

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/implementation branch>.
Kontynuuj: pending independent review dla <MXX-TYY | exact review target>.
Durable start pointer: implementation/TASK_BOARD.yaml.
Odtwórz exact review_subject, authority slice i evidence z repo, wykonaj niezależny review zgodnie z workflow i zapisz verdict/evidence w durable state. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

Prompt is a router into durable truth. Do not duplicate SHAs, test counts/results, evidence prose or implementation summary when Task Board/repo already contains them.

## User-facing review result

Use root `CHATGPT.md` control surface:
- what was found;
- impact;
- what happened next;
- smallest real user action.

Keep review telemetry in durable evidence unless exact detail is materially actionable or user asks.
