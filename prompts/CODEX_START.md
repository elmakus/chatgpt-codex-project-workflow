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

Recover Task Board/Git/runtime/review state, run the state/contract Refresh Gate and execute deterministic READY work. Do NOT run Capability Gate or capability preflight/inventory. Attempt concrete operations directly.

If ordinary non-secret local tooling/dependencies are missing, self-remediate them when the environment permits and accepted security/reproducibility constraints allow it. Ask the user only when a concrete operation requires unavailable MCP/credential/token/access/authorization that Codex cannot obtain itself.

When installed/enabled, codex_workflow controls internal orchestration, including execute/review workers, delegation, role/model routing, lifecycle and runtime recovery. REQUIRED/RECOMMENDED independent review uses a reviewer worker/session that did not implement the subject; do not return to ChatGPT merely for reviewer independence.

After each GREEN milestone, continue automatically into the next already-approved milestone using allowed just-in-time execution prep + fresh state/contract Refresh Gate. Persist result/review pointers/tests/evidence/readback in Task Board/evidence.

Stop only for a real concrete runtime blocker that cannot be self-remediated, strategic product/architecture/frozen-contract change, explicit user/deployment/live-write authorization gate, RED requiring strategic resolution, or end of approved scope.
```

## Mixed-policy bounded start

```text
Use current main of elmakus/chatgpt-codex-project-workflow.
Project repo: <owner/repo>.
Execution policy: mixed.
Assigned milestone/set: <MXX / MXX-TYY[, ...]>.
Required prior checkpoint: <checkpoint>.
Durable start pointer: implementation/TASK_BOARD.yaml.

Read project PROJECT.md and workflow/CONTEXT_ROUTING.md. Load shared execution contracts and workflow/codex modules only. Recover assigned Task Board/Git/review state, run state/contract Refresh Gate and execute assigned scope. Persist result/review pointers/tests/evidence/readback.

The mixed-policy Capability Gate already performed pre-assignment routing. After assignment, do not rerun it because of a runtime capability problem; persist the blocker instead.

Do not self-assign a new mixed-policy milestone after assigned scope ends; return durable state to ChatGPT routing.
```

Repository state outranks stale conversation history. When installed/enabled, `codex_workflow` controls internal Codex runtime orchestration only; Project Workflow controls project Task Card/state/review/acceptance boundaries.
