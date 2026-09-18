# ChatGPT-only Independent Review

Independent review is performed by a fresh normal ChatGPT chat that did not implement the exact reviewed subject.

## Review requirement

- **REQUIRED** — high-risk work such as security/auth, destructive/data migration, difficult-to-reverse live configuration, important external-state protection boundary or comparable risk.
- **RECOMMENDED** — independent review is intentionally part of the accepted Card/milestone contract even though the work is not intrinsically high-risk.
- **none** — no independent-review gate exists and this route is not entered.

REQUIRED and RECOMMENDED have the same independence mechanics once activated. The difference records why the gate exists, not whether it is real.

If the user explicitly requests review for work previously contracted as `none`, first persist the requirement as `RECOMMENDED`, then create the normal review state.

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

After GREEN:
1. persist verdict/evidence/state;
2. the independent-review role is complete;
3. return to `workflow/chatgpt_only/ROUTER.md`;
4. let the router choose the next legal route from the new durable state;
5. continue in the same chat when that route is deterministic and authorized.

Do not remain in reviewer mode merely because this chat began as a reviewer.

Do not stop merely to report GREEN.

If the router later assigns implementation and this chat creates a new REQUIRED/RECOMMENDED review subject, this chat is the implementing chat for that new subject and must stop at the fresh-review boundary.

## RED → corrective-route transition

RED is not itself a user stop when corrective work can be bounded deterministically inside accepted authority.

After RED:
1. persist the RED verdict/evidence/state;
2. do not mutate the reviewed subject while still acting as reviewer;
3. determine whether corrective work is safely routable as L1/L2 work without a strategic/user/authorization/runtime blocker;
4. if yes, the independent-review role is complete;
5. return to `workflow/chatgpt_only/ROUTER.md`;
6. the router selects `EXECUTION_PREP` when corrective work must be created/reopened/reconciled, otherwise `EXECUTION`;
7. from that point the same chat acts under the selected execution route, not under this review module.

Do not end the turn after RED merely to announce that remediation is next.

If corrective work cannot be safely bounded, requires L3 authority, requires explicit user/deployment/live-write authorization, or is blocked by a concrete runtime/access/input requirement, that is a real stop. Use the global real-stop response contract.

If the same chat later implements the correction and that corrected subject requires/recommends independent review, the execution route freezes a new exact subject as `pending` and stops for a fresh independent reviewer. The former reviewer cannot review the subject it just implemented.

## High-risk external writes

When practical, place REQUIRED/RECOMMENDED independent review at the last useful reversible checkpoint before a high-risk external write.

After GREEN, perform the authorized write plus required post-write readback/verification.

Do not create a permanent review role or independently review every trivial Card.

## Fresh-review handoff

When this chat later reaches a real boundary requiring a fresh independent reviewer, use the independent-review prompt variant from `workflow/common/USER_STOP.md`.

The review module does not own a separate user-response format.

## User-facing response

A review verdict alone is not a reason to reply.

Use root `CHATGPT.md#Real-stop-response-contract` only when the workflow actually reaches a real stop after all legal deterministic role transitions have been exhausted.

Keep review telemetry in durable evidence unless exact detail is materially actionable or the user asks.
