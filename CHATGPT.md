# ChatGPT Project Workflow Bootstrap

This is the minimal normal-ChatGPT entrypoint.

## Durable authority

- Current `main` of this workflow repository is authoritative for workflow behavior unless an explicitly frozen in-flight boundary says otherwise.
- Project repository is durable project truth.
- Accepted durable repository state outranks stale chat/session narrative.

## Bootstrap

For every normal ChatGPT project task:

1. Read project root `PROJECT.md`.
2. Read `workflow/CONTEXT_ROUTING.md`.
3. Let that router select the execution-policy namespace.
4. Follow only the selected route plus explicitly referenced policy-neutral common modules.
5. When implementation/review state exists, recover it from `implementation/TASK_BOARD.yaml`.
6. Follow exact durable authority refs rather than loading whole trees "just in case".
7. Persist accepted changes to project truth when the task changes durable state.

Progressive disclosure is **lossless by authority, selective by context**.

## Normal ChatGPT scope and session continuity

ChatGPT Work is outside this workflow.

A normal ChatGPT chat may continue deterministic work in the same session while context remains useful and the selected route permits continuation.

A fresh chat may be recommended for context hygiene, but that recommendation is not a workflow gate unless the selected route explicitly defines a real boundary such as REQUIRED/RECOMMENDED independent-review separation.

Do not impose a fixed token count, turn count or milestone cadence for starting fresh chats.

A fresh chat reconstructs authority from the durable project repository and current workflow `main`, not from the previous transcript.

## Real-stop response contract

A normal ChatGPT chat should send a final user-facing workflow status message only when the current chat has reached a real stop/boundary or the approved scope is complete.

Completing a role is not itself a stop. When the current role finishes and another deterministic route is legal, persist durable state, return to the policy router, assume the next role, load only that role's module(s), and continue before replying to the user.

A real stop includes:
- this chat implemented a subject that now requires/recommends independent review by a fresh chat;
- a strategic/L3 decision requires user authority;
- an explicit user/deployment/live-write authorization gate is due;
- a concrete runtime/access/input blocker prevents the required operation;
- approved scope is complete and no deterministic next work is authorized.

At a real stop, read `workflow/common/USER_STOP.md` and use its user-facing contract.

The minimum shape is:
1. what was completed/found;
2. what it means now;
3. the exact next step.

If user action is required, include an explicit `USER ACTION REQUIRED:` line with the smallest action.

If a fresh ChatGPT chat is required or recommended, include the ready-to-copy branch-aware `NEW CHAT START PROMPT` in the same response.

If no user action is required because approved scope is complete, say so plainly.

Do not emit an intermediate status-only response between legal deterministic role transitions.

## Human control surface

These rules apply to every normal ChatGPT route.

By default, user-facing output reports only:
1. what happened / what was found;
2. what it means;
3. what happens next or the smallest user action.

Keep durable execution telemetry in the repository. Do not dump SHAs, branch/HEAD pointers, evidence paths, raw Task Board fields, long test inventories/counts, changed-file lists or internal bookkeeping unless the user asks or the exact value is materially required for action/debugging/recovery/security.

Do not end the chat turn merely to announce deterministic work that the selected route authorizes to continue. Continue first and respond at a real workflow stop/boundary.

Whenever a fresh ChatGPT chat is required or recommended, include the ready-to-copy branch-aware start prompt in that same response.
