# Codex start prompt

Codex may be the fixed executor in a `codex_only` project, an assigned executor in a `mixed` project, or recover previously Codex-assigned in-progress work.

## Codex-only continuous start

```text
Use current main of elmakus/chatgpt-codex-project-workflow.
Project repo: <owner/repo>.
Execution policy: codex_only.
Durable start pointer: implementation/TASK_BOARD.yaml.
Approved plan: <planning/MASTER_PLAN.md>.
Required prior checkpoint: <checkpoint/current Task Board state>.

Read project PROJECT.md and workflow/CONTEXT_ROUTING.md. Load shared execution contracts and workflow/codex modules only. Do not load CHATGPT.md or workflow/chatgpt/*.

Recover Task Board/Git/runtime/review state, resolve the current milestone contract and each READY Task Card's exact authority slice, then read `workflow/EXECUTION.md`, `workflow/contracts/TASK_EXECUTION.md` and the required `workflow/codex/*` modules. Run the state/contract Refresh Gate and execute deterministic READY work. Do NOT run Capability Gate or capability inventory/preflight.

Project Workflow does not tell Codex which tools/capabilities it has. Attempt concrete operations with the actual runtime, handle ordinary executor-local remediation when permitted, and ask the user only when a concrete required operation still needs user-provided input/access/authorization.

When installed/enabled, codex_workflow controls internal orchestration, including execute/review workers, delegation, role/model routing, lifecycle and runtime recovery. REQUIRED/RECOMMENDED independent review uses a reviewer worker/session that did not implement the subject; do not return to ChatGPT merely for reviewer independence.

Within the active milestone and after each GREEN milestone, perform allowed L2 just-in-time decomposition/refinement from durable predecessor evidence when deferred detail becomes knowable. Create/revise only not-yet-started cards, preserve strategic authority, reconcile Task Board, then continue automatically into the next deterministic work using fresh state/contract Refresh Gate. Persist result/review pointers/tests/evidence/readback in Task Board/evidence.

Stop only for a real concrete runtime blocker that cannot be self-remediated, L3 strategic replan (requirements/frozen architecture or decisions/invariants/milestone outcome/behavior contract must change), explicit user/deployment/live-write authorization gate, RED requiring strategic resolution, or end of approved scope.
```

## Mixed-policy bounded start

```text
Use current main of elmakus/chatgpt-codex-project-workflow.
Project repo: <owner/repo>.
Execution policy: mixed.
Assigned milestone/set: <MXX / MXX-TYY[, ...]>.
Required prior checkpoint: <checkpoint>.
Durable start pointer: implementation/TASK_BOARD.yaml.

Read project PROJECT.md and workflow/CONTEXT_ROUTING.md. Load `workflow/EXECUTION.md`, `workflow/contracts/TASK_EXECUTION.md` and required `workflow/codex/*` modules only. Recover assigned Task Board/Git/review state, resolve the assigned Task Card authority slice, run state/contract Refresh Gate and execute assigned scope. Persist result/review pointers/tests/evidence/readback.

The mixed-policy Capability Gate already performed pre-assignment routing. After assignment, do not rerun it because of a runtime capability problem; persist the blocker instead.

Do not self-assign a new mixed-policy milestone after assigned scope ends; return durable state to ChatGPT routing. Within an already assigned scope, allowed L2 refinement may create/revise not-yet-started cards only when the assignment and strategic authority still cover them.
```

Progressive disclosure is lossless by authority: do not replace applicable requirements/accepted decisions/approved-plan constraints with a thinner coordinator summary. Carry them explicitly or read the exact durable refs before implementation/review.

Repository state outranks stale conversation history. When installed/enabled, `codex_workflow` controls internal Codex runtime orchestration only; Project Workflow controls project Task Card/state/review/acceptance boundaries.
