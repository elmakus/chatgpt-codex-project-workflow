# Codex start prompt

Codex is a specialized executor inside a `mixed` project or may recover a previously Codex-assigned in-progress card.

```text
Use current main of elmakus/chatgpt-codex-project-workflow.
Project repo: <owner/repo>.
Milestone: <MXX>.
Task Card: <MXX-TYY>.
Required prior checkpoint: <checkpoint>.
Durable start pointer: <path>.

Read project PROJECT.md and workflow/CONTEXT_ROUTING.md. Load the shared execution core, required shared contracts and workflow/codex modules only. Do not load CHATGPT.md or workflow/chatgpt/*.

Recover durable Task Board/card/Git state, verify required capabilities, run the Refresh Gate and execute the assigned card according to acceptance/dependencies. Persist result pointers, tests/evidence and required external readback verification. Stop for a real capability blocker, strategic contract change, explicit user authorization gate or final milestone checkpoint.
```

Repository state outranks stale conversation history. When installed/enabled, `codex_workflow` controls internal Codex runtime orchestration only.
