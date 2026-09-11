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
3. determine/confirm phase and `execution_policy`;
4. apply progressive disclosure;
5. treat accepted durable repository knowledge as authority over stale chat memory;
6. persist accepted state when current GitHub/project capabilities allow it;
7. before execution, apply the Capability Gate rather than assuming Codex must execute.

If `chatgpt_only` and a required capability is missing, report the blocker rather than routing to Codex.

If `mixed`, hand work to Codex only under the Capability Gate and use `workflow/codex/HANDOFF.md` for the minimal kickoff.

## New project

Create/choose the project repository, initialize `PROJECT.md` with `execution_policy`, then create only phase-appropriate artifacts. Do not create Task Cards/OpenSpec merely because the repo is new.
