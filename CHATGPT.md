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

## Human control surface

These rules apply to every normal ChatGPT route.

By default, user-facing output reports only:
1. what happened / what was found;
2. what it means;
3. what happens next or the smallest user action.

Keep durable execution telemetry in the repository. Do not dump SHAs, branch/HEAD pointers, evidence paths, raw Task Board fields, long test inventories/counts, changed-file lists or internal bookkeeping unless the user asks or the exact value is materially required for action/debugging/recovery/security.

Do not end the chat turn merely to announce deterministic work that the selected route authorizes to continue. Continue first and respond at a real workflow stop/boundary.

Whenever a fresh ChatGPT chat is required or recommended, include the ready-to-copy branch-aware start prompt in that same response.
