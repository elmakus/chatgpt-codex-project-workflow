# ChatGPT-only Independent Review

Independent review is performed by a fresh normal ChatGPT chat that did not implement the exact reviewed subject.

## Review requirement

- **REQUIRED** — high-risk work such as security/auth, destructive/data migration, difficult-to-reverse live configuration, important external-state protection boundary or comparable risk.
- **RECOMMENDED** — independent review is intentionally part of the accepted Card/milestone contract or workstream final-integration gate even though the work is not intrinsically high-risk.
- **none** — no independent-review gate exists for that Card/milestone/workstream-final subject and this route is not entered.

REQUIRED and RECOMMENDED have the same independence mechanics once activated. The difference records why the gate exists, not whether it is real.

If the user explicitly requests review for work previously contracted as `none`, first persist the requirement as `RECOMMENDED`, then create the normal review state.

## Review state owner

Resolve exactly one review owner before judging the subject:

- **Card/milestone review** → mutable `review_state/review_subject/review_evidence` live only in the selected canonical Task Board.
- **Workstream final-integration review** → mutable `review.state/subject/evidence/covered_by` live only in the selected branch-isolated `WORKSTREAM.yaml` manifest.

Never mirror one lifecycle into the other. A manifest `covered_by` pointer may reuse an already-independent exact GREEN verdict only under the exact-coverage rules in `WORKSTREAMS.md` / `MICRO_FIX.md`; coverage reuse is not a new review attempt.

## Required read set

Read:
- project `PROJECT.md`;
- `workflow/chatgpt_only/WORKSTREAMS.md` when branch-isolated;
- exact active branch and validated selected manifest when applicable;
- the selected canonical Task Board when Card/milestone execution state or corrective execution/Research exists;
- the exact immutable subject from the owning review state;
- the reviewed Task Card/milestone contract, or for a workstream final-integration review the manifest + exact integrated workstream authority/acceptance surface;
- the same authority slice that governed implementation;
- required evidence referenced for review;
- actual reviewed diff/source/runtime needed to judge the subject.

Read `workflow/chatgpt_only/MICRO_FIX.md` for a qualified micro-fix workstream review.

Read `workflow/common/OPENSPEC.md` only when reviewed authority points to OpenSpec or verdict depends on it.

Read prior handoff/dependency/research/external readback only when reviewed authority/acceptance references it.

Do not inspect another workstream Task Board for evidence merely because it exists. Do not use previous implementing-chat narrative as review evidence.

## Review lifecycle

1. Recover the exact subject and exact review owner from durable state.
2. Set only that owner's review state to `in_progress`.
3. Independently inspect exact subject/contracts/evidence.
4. Verify acceptance and applicable authority.
5. Persist concise durable GREEN/RED review evidence.
6. Set only that owner's state to `green | red` plus its evidence pointer.

Do not mutate reviewed subject while judging it.

## GREEN

After GREEN:
1. persist verdict/evidence/state;
2. the independent-review role is complete;
3. return to `workflow/chatgpt_only/ROUTER.md`;
4. if this was a Card-completion review, the reviewed Card is still non-terminal; route to Execution for deterministic Post-review Card finalization before any dependent/later Card;
5. if this was a workstream final-integration review, keep Card/milestone Task Board state unchanged and let the router continue from the now-GREEN manifest gate;
6. if this was a milestone/other review, let the router choose the owning continuation route;
7. continue in the same chat when that route is deterministic and authorized.

Do not remain in reviewer mode merely because this chat began as a reviewer.

Do not stop merely to report GREEN.

If the router later assigns implementation and this chat creates a new REQUIRED/RECOMMENDED review subject, this chat is the implementing chat for that new subject and must stop at the fresh-review boundary.

## RED → corrective-route transition

RED is not itself a user stop when corrective work can be bounded deterministically inside accepted authority.

After RED:
1. persist the RED verdict/evidence in its exact owner; a Card-completion subject remains non-terminal, while a RED workstream final-integration gate remains manifest-owned and blocks that workstream's integration;
2. do not mutate the reviewed subject while still acting as reviewer;
3. classify the correction against current durable state before deciding whether a stop exists; on recovery from an already-persisted RED verdict, use this same classification and do not repeat a correction role whose failing condition is already durably reconciled. If a corrected implementation subject is already durable but the next REQUIRED/RECOMMENDED `pending` attempt was not yet frozen, route to Execution only to reconcile/freeze that new exact subject and review boundary before any later work;
4. bounded L1/L2 implementation correction inside accepted authority → return to the router for `EXECUTION_PREP` or `EXECUTION`;
5. plan-only milestone structure/order/outcome or execution-strategy correction while Project Definition remains valid → return to the router for Planning;
6. correction to accepted requirements/strategic decisions/global target-state authority → return to the router for Project Definition;
7. missing evidence needed before either can be corrected → before yielding, create/reuse one exact implementation-owned record under `workflow/chatgpt_only/RESEARCH.md#Durable record contract`, with the RED review subject/evidence as Origin, `Return target: execution_resolution:<exact affected subject>`, `Return reconciliation: pending`, and set the selected workstream Task Board `research_obligation`; then return to the router for Research;
8. only unresolved user/product authority, explicit user/deployment/live-write authorization, or a concrete runtime/access/input blocker creates a real stop.

From the selected route onward, the same chat acts under that role rather than under this review module.

Do not end the turn after RED merely to announce deterministic remediation or replanning that the router can perform.

If the same chat later implements the correction and that corrected subject requires/recommends independent review, the execution route freezes a new exact subject as `pending` and stops for a fresh independent reviewer. The former reviewer cannot review the subject it just implemented.

For a workstream final-integration RED, preserve the old manifest RED evidence. After deterministic correction reaches a new exact integrated subject, either prove exact stronger independent coverage under `WORKSTREAMS.md` or set the manifest gate to a new `pending` subject. A chat that implemented any part of that corrected exact subject cannot issue the new verdict.

## High-risk external writes

When practical, place REQUIRED/RECOMMENDED independent review at the last useful reversible checkpoint before a high-risk external write.

After GREEN, perform the authorized write plus required post-write readback/verification.

Do not create a permanent review role or independently review every trivial Card.

## Fresh-review handoff

When this chat later reaches a real boundary requiring a fresh independent reviewer, use the independent-review prompt variant from `workflow/common/USER_STOP.md`.

The handoff names the pending review only as an entry locator. Do not append review checklists, prior findings, remediation proposals, verdict branches or recoverable telemetry to the prompt. If a nonstandard review scope is required, persist it durably first in the reviewed Card/review evidence/other exact scope artifact and reference it from canonical review state/authority. Use the selected Task Board as the start pointer for Card/milestone review; use the exact selected workstream manifest as the start pointer for a workstream final-integration review.

The review module does not own a separate user-response format.

## User-facing response

A review verdict alone is not a reason to reply.

Use root `CHATGPT.md#Real-stop-response-contract` only when the workflow actually reaches a real stop after all legal deterministic role transitions have been exhausted.

Keep review telemetry in durable evidence unless exact detail is materially actionable or the user asks.
