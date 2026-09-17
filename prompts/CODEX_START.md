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

Recover Task Board/Git/runtime state, verify required capabilities, run Refresh Gate and execute deterministic READY work. After each GREEN milestone, continue automatically into the next already-approved milestone using allowed just-in-time execution prep + fresh Refresh Gate. Do not run Capability Gate.

Persist result pointers/tests/evidence/readback in Task Board/evidence. Stop only for a real missing capability/evidence path, strategic product/architecture/frozen-contract change, explicit user/deployment/live-write authorization gate, RED requiring strategic resolution, or end of approved scope.
```

## Mixed-policy bounded start

```text
Use current main of elmakus/chatgpt-codex-project-workflow.
Project repo: <owner/repo>.
Execution policy: mixed.
Assigned milestone/set: <MXX / MXX-TYY[, ...]>.
Required prior checkpoint: <checkpoint>.
Durable start pointer: implementation/TASK_BOARD.yaml.

Read project PROJECT.md and workflow/CONTEXT_ROUTING.md. Load shared execution contracts and workflow/codex modules only. Recover assigned Task Board/Git state, verify required capabilities, run Refresh Gate and execute assigned scope. Persist result pointers/tests/evidence/readback.

Do not self-assign a new mixed-policy milestone after assigned scope ends; return durable state to ChatGPT routing.
```

Repository state outranks stale conversation history. When installed/enabled, `codex_workflow` controls internal Codex runtime orchestration only.
