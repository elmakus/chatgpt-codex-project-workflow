# ChatGPT start prompt

Use this for normal ChatGPT. It deliberately stays short because the workflow repository and project `PROJECT.md` perform context routing.

No installable ChatGPT skill, Custom GPT, `@Project Workflow`, or ChatGPT Work mode is required by this workflow.

## Existing project

```text
Użyj mojego Project Workflow z elmakus/chatgpt-codex-project-workflow.
Repo projektu: <owner/repo>.
Kontynuujemy <phase albo krótki cel>.
```

On receipt, ChatGPT should:
1. read current `main` of the workflow repository starting with `CHATGPT.md`;
2. read the project root `PROJECT.md`;
3. determine/confirm the current phase from project state and the user's instruction;
4. load only phase-required workflow modules and project artifacts;
5. treat accepted repository knowledge as durable authority over stale chat memory;
6. persist newly accepted project knowledge back to the project repository when repository-writing capability and authority are available; do not leave accepted state only in chat. If the current environment is read-only, explicitly identify what durable artifact must be updated.

If the user's stated phase intentionally changes the project phase, reconcile `PROJECT.md` rather than silently treating stale phase metadata as superior to the user's current instruction.

## Completely new project

Create an empty repository for the project first, then use:

```text
Użyj mojego Project Workflow z elmakus/chatgpt-codex-project-workflow.
Nowy projekt. Repo projektu: <owner/repo>.
Zacznij od brainstormingu i zainicjalizuj PROJECT.md według workflow.
```

Initialization uses `templates/PROJECT.md` plus only phase-appropriate project templates. Do not create Task Cards or OpenSpec merely because the repository is new.
