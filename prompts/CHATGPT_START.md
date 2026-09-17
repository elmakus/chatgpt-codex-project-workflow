# ChatGPT start prompt

Use this in normal ChatGPT chat. ChatGPT Work is not part of Project Workflow.

## Existing project

```text
Użyj mojego Project Workflow z elmakus/chatgpt-codex-project-workflow.
Repo projektu: <owner/repo>.
Kontynuujemy <phase albo krótki cel>.
```

ChatGPT should:
1. read current workflow `main`, starting with `CHATGPT.md`;
2. read project root `PROJECT.md`;
3. determine phase and `execution_policy`;
4. apply progressive disclosure;
5. treat accepted durable repository knowledge as authority over stale chat memory;
6. when implementation state exists, read Task Board as sole live execution-state authority;
7. persist accepted state when current GitHub/project capabilities allow it;
8. route execution by policy:
   - `chatgpt_only` → execute in ChatGPT; no Capability Gate;
   - `codex_only` → prepare/hand off to Codex or recover Codex stream; no Capability Gate;
   - `mixed` → run Capability Gate before new assignment.

If fixed-policy executor lacks required capability, report/persist blocker rather than routing to the other executor automatically.

If `mixed`, hand work to Codex only under Capability Gate and use `workflow/codex/HANDOFF.md` for minimal kickoff.

## New project

Create/choose project repository, initialize high-level `PROJECT.md` with explicit `execution_policy`, then create only phase-appropriate artifacts. Do not create Task Cards/OpenSpec merely because repo is new.
