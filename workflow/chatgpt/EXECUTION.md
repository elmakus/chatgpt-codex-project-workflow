# ChatGPT Execution Adapter

Read this only when ChatGPT is the assigned executor or is recovering ChatGPT-assigned work.

Shared execution semantics live in:
- `workflow/EXECUTION.md`;
- `workflow/contracts/TASK_EXECUTION.md`.

This adapter adds only ChatGPT-specific runtime/session/user-surface behavior.

## Runtime behavior

Do not inventory or describe ChatGPT's tools/capabilities before work.

Attempt the concrete operation with the runtime available in the current normal ChatGPT chat. Ordinary local remediation is implementation detail when permitted. If a required operation cannot proceed, use shared runtime-blocker semantics and ask only for the smallest user input/access/authorization actually needed.

Do not infer production/runtime success from an isolated local test when they are materially different environments.

If Task Board uses `bounded_parallel`, load the conditional parallel contracts from the shared router. ChatGPT may execute a compatible subset or one card when needed; it does not manufacture concurrency merely because parallel mode is allowed.

ChatGPT Work is outside Project Workflow.

## Human-facing output

Use the global normal-ChatGPT human control surface defined in `CHATGPT.md`. Do not duplicate execution telemetry into the user response.

## Review boundary

When this chat implemented a subject that reaches REQUIRED/RECOMMENDED independent review:

1. apply `workflow/contracts/TASK_EXECUTION.md` review-boundary persistence;
2. load `workflow/REVIEW_AND_HANDOFF.md`;
3. stop before issuing the verdict;
4. require a fresh normal ChatGPT chat for the independent review;
5. include the ready-to-copy fresh-chat prompt in the same response.

The fresh-chat prompt includes project repo, exact active branch, continuation target and durable start pointer, but does not duplicate durable evidence.

OPTIONAL review does not force a new chat unless explicitly activated.

## Session continuity

Workflow roles are not tied to one ChatGPT chat.

Outside REQUIRED/RECOMMENDED independence:
- the same chat may continue deterministic execution while context remains useful;
- a fresh chat is optional context hygiene, not a workflow gate;
- if recommending a fresh chat, include its copy-paste-ready start prompt immediately.

Do not impose a fixed token count or milestone cadence for fresh sessions.

A fresh chat recovers from durable repository state, not from the previous transcript.

## Continuation

Under `chatgpt_only`, continue deterministic READY work automatically until a real review/strategic/user/authorization/runtime/end-of-scope boundary occurs.

Under `mixed`, execute only the assignment established by Capability Gate; route a genuinely new assignment through the gate after assigned scope ends.

Milestone close/next-milestone rules are evaluated through `workflow/REVIEW_AND_HANDOFF.md`, not duplicated here.
