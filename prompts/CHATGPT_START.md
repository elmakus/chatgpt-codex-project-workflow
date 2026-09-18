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
5. recover mutable continuation/review/execution state from the canonical source defined by the selected policy route; under `chatgpt_only`, use Task Board for implementation/implementation-review state (including `research_obligation` for implementation/recovery Research), `planning/reviews/<plan-revision>.md` for pre-execution plan review, and the exact `PROJECT.md → Active research obligation` record for pre-execution Research;
6. treat durable repository authority as stronger than stale chat memory;
7. persist changed durable truth when current project capabilities allow it.

Do not paste execution-policy semantics into the start prompt. The repository router owns them.

When a fresh ChatGPT chat is required or recommended later, use the exact canonical branch-aware handoff from `workflow/common/USER_STOP.md`. Keep it locator-only: do not expand it with recoverable workflow semantics, checklists or telemetry, and do not treat the named entry obligation as a session-scope boundary.

## New project

Create/choose project repository, initialize a small `PROJECT.md` with an explicit accepted execution policy, then create only phase-appropriate artifacts. Do not create implementation state before it is needed.
