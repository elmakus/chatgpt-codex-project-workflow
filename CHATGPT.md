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
5. Recover mutable review/execution state from the canonical source defined by the selected policy route. Do not assume every review lifecycle lives in `implementation/TASK_BOARD.yaml`.
6. Follow exact durable authority refs rather than loading whole trees "just in case".
7. Persist accepted changes to project truth when the task changes durable state.
8. For a newly authorized managed repository change under a branch-first fixed policy, create or recover the exact branch-isolated workstream before the first durable change-specific write. Historical root/default execution state is recovery/migration input only, not a new-work destination.

Progressive disclosure is **lossless by authority, selective by context**.

## Normal ChatGPT scope and session continuity

ChatGPT Work is outside this workflow.

A normal ChatGPT chat may continue deterministic work in the same session while context remains useful and the selected route permits continuation.

A casual fresh-chat recommendation for context hygiene is not a workflow gate. However, a selected policy route may define an explicit context-health gate that turns a safe durable boundary into a required session handoff when continuing the accumulated chat creates a concrete material context-risk. REQUIRED/RECOMMENDED independent-review separation remains a separate hard fresh-chat boundary.

Do not impose a fixed token count, turn count, Card count or milestone cadence for starting fresh chats.

A fresh chat reconstructs authority from the durable project repository and current workflow `main`, not from the previous transcript.

## Execution-surface selection

For every concrete operation, prefer a permitted native ChatGPT runtime/tool or an appropriate purpose-built connector/plugin when it can perform the required work and verification materially equivalently.

User-owned/private remote infrastructure — including hosts reached through general remote desktop, terminal or filesystem bridges — is a **last-resort execution surface**. Do not use it merely because it provides convenient shell access, compute, temporary storage or another shortcut when a materially equivalent native or purpose-built path exists.

Use user-owned/private remote infrastructure only when at least one is true:
- the task intrinsically depends on that specific host, its local state, devices, services or environment; or
- no materially equivalent permitted native or purpose-built path can perform the required operation and verification.

This is an execution-surface selection rule, not a capability inventory. Do not enumerate tools or probe private infrastructure merely to discover whether it could be useful. Escalate to it only from a concrete task need.

When private infrastructure is required, limit access, reads, writes and temporary artifacts to the smallest scope needed for the operation.

## Real-stop response contract

A normal ChatGPT chat should send a final user-facing workflow status message only when the current chat has reached a real stop/boundary or the approved scope is complete.

Before any final user-facing workflow status response, perform a **pre-response router check**:
1. re-evaluate current durable state through the selected policy router;
2. verify that no deterministic authorized role transition remains;
3. treat completion of the role/obligation named in the user request or fresh-session handoff as non-terminal unless the router proves a real stop;
4. if a next legal route exists, continue in the same chat before replying.

A fresh-session continuation target is an entry locator, not a session-scope boundary. Finishing that target does not by itself authorize a user-facing response.

Completing a role is not itself a stop. When the current role finishes and another deterministic route is legal, persist durable state, return to the policy router, assume the next role, load only that role's module(s), and continue before replying to the user.

A real stop includes:
- this chat authored or implemented an exact subject that now requires/recommends independent review by a fresh chat;
- an unresolved strategic/product decision requires user authority;
- an explicit user/deployment/live-write authorization gate is due;
- a concrete runtime/access/input blocker prevents the required operation;
- approved scope is complete and no deterministic next work is authorized;
- the selected route's Context Health Gate returns `FRESH` at a safe durable boundary.

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
