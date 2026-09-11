# ChatGPT ↔ Codex Handoff Contract

This is the only Codex-specific module ChatGPT normally needs to read when preparing or interpreting a Codex handoff.

## ChatGPT → Codex

A kickoff stays short and points to durable state. Include:

- workflow authority: `elmakus/chatgpt-codex-project-workflow:main`;
- project repository;
- branch when known;
- current milestone;
- Task Card;
- required prior checkpoint;
- exact durable kickoff/start pointer;
- required capabilities and evidence/readback obligations that materially affect routing;
- instruction to run Refresh Gate;
- stop conditions.

Do not paste the whole plan, project history, OpenSpec tree or large diffs into chat.

Suggested shape:

```text
Use current main of elmakus/chatgpt-codex-project-workflow.
Project repo: <owner/repo>
Branch: <branch>
Milestone: <MXX>
Task Card: <MXX-TYY>
Required prior checkpoint: <sha/tag>
Durable start pointer: <path>
Required capabilities/evidence: <summary>

Recover durable state, verify required capabilities, run the Refresh Gate and execute only this card under shared Project Workflow contracts. Persist tests, result pointers, external readback evidence and Task Board/Card state.

Stop if a required capability is absent, strategic authority must change, explicit user authorization is required, or required acceptance/evidence cannot be produced.
```

## Codex → ChatGPT

Codex returns project truth through the repository, not a multi-page user copy/paste report. Persist Task Card/Task Board state, result commit/PR, tests/evidence, blocker records and milestone handoff as applicable.

A fresh ChatGPT chat recovers from `PROJECT.md` and durable pointers.

## Strategic blocker correlation

When an asynchronous/control-chat correlation mechanism is actually used, use a unique `request_id` and explicit `DECISION FOR CODEX:` marker so Codex never treats arbitrary prose as authorization. Persist the accepted decision in the project repository before resuming.

Do not require this transport mechanism when ChatGPT is itself the executor or when the user is directly resolving a normal ChatGPT blocker.
