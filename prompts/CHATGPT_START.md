# ChatGPT start prompt

Use this in a normal ChatGPT chat.

## Existing project

```text
Użyj mojego Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Kontynuujemy <krótki cel albo durable continuation pointer>.
```

Normal ChatGPT should:
1. read current workflow `CHATGPT.md`;
2. read project root `PROJECT.md`;
3. read `workflow/CONTEXT_ROUTING.md`;
4. follow only the execution-policy route selected there;
5. recover mutable continuation/review/execution state from the canonical source defined by the selected policy route; under `chatgpt_only`, new managed work uses an exact branch-isolated workstream and its manifest-selected state, while historical root `implementation/TASK_BOARD.yaml` and root workstream-local pointers are recovery/migration input only and must migrate before further managed mutation;
6. treat durable repository authority as stronger than stale chat memory;
7. persist changed durable truth when current project capabilities allow it.

Do not paste execution-policy semantics into the start prompt. The repository router owns them.

When a fresh ChatGPT chat is required or recommended later, use the exact canonical branch-aware handoff from `workflow/common/USER_STOP.md`. Keep it locator-only: do not expand it with recoverable workflow semantics, checklists or telemetry, and do not treat the named entry obligation as a session-scope boundary.

## New project / adoption

Create or choose the project repository and perform only read-only discovery needed to establish the integration target and execution policy. For a managed bootstrap/adoption change, create or recover the exact branch-isolated workstream **before** writing `PROJECT.md`, workflow state or project-source changes. Author phase-appropriate state on that branch and integrate through pull request + merge; do not seed root/default implementation state as the new-work path.
