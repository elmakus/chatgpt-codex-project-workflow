# ChatGPT ↔ Codex Handoff Contract

This is the only Codex-specific module ChatGPT normally needs when preparing or interpreting Codex execution communication.

## 1. ChatGPT → Codex execution kickoff

A kickoff stays short and points to durable state. Include:
- workflow authority `elmakus/chatgpt-codex-project-workflow:main`;
- project repository;
- branch when known;
- current milestone and Task Card;
- required prior checkpoint;
- exact durable start/kickoff pointer;
- required capabilities/evidence/readback obligations that materially affect routing;
- instruction to run Refresh Gate;
- stop conditions.

Do not paste whole plan/history/OpenSpec trees/large diffs into chat.

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

## 2. Codex → ChatGPT normal return

Codex returns project truth through the repository, not a multi-page copy/paste report. Persist Task Card/Task Board state, result commit/PR, tests/evidence, external readback, blocker records and milestone handoff as applicable.

A fresh ChatGPT chat recovers from `PROJECT.md` and durable pointers.

## 3. Strategic escalation: when to use correlated control chat

Do not use ChatGPT as a routine Codex message bus.

Use strategic escalation when evidence reveals contradictory requirements, required architecture/product decisions, impossible/wrong acceptance, frozen-plan invalidation, material external-contract change, or behavior/security/schema choices beyond Codex authority.

Routine implementation details within approved contracts remain executor implementation detail.

## 4. Strategic blocker lifecycle

When Codex uses the configured ChatGPT control-chat mechanism:
1. stop dependent work and set current card `blocked`;
2. write complete blocker evidence under `implementation/blockers/`;
3. safely commit/push evidence when possible;
4. post a short structured request with unique `request_id`;
5. ChatGPT reads durable evidence and only needed context;
6. ChatGPT researches further if required;
7. ChatGPT replies with exact same `request_id` and authoritative `DECISION FOR CODEX:` line;
8. Codex accepts only a matching structured decision;
9. Codex persists accepted decision under `decisions/` with provenance;
10. reconcile Task Card/OpenSpec/plan/Task Board as required;
11. resume only after blocker is resolved.

## 5. Request format

```text
CODEX STRATEGIC REQUEST
request_id: <unique project-milestone-task-nonce>
Project: <project>
Milestone: <milestone>
Task: <task>
Status: BLOCKED

Reason:
<short reason>

Evidence:
<repo-relative path>
Commit: <exact sha>

Options:
A. ...
B. ...

Codex recommendation:
...

Please review the durable evidence and reply with the SAME request_id and one authoritative line beginning:
DECISION FOR CODEX:
```

## 6. Decision format and correlation

```text
request_id: <exact same request_id>
DECISION FOR CODEX: <decision>
```

Codex never treats arbitrary ChatGPT prose as an execution decision; it requires matching ID + marker and remains blocked if either is absent/ambiguous.

After receipt, persist project/task, timestamp, chat/thread identity when available, exact request ID/decision marker, concise rationale, impact, artifacts updated and persisting commit.

Chat is transport. Repository is durable truth.

## 7. Channel asymmetry

Do not design around a guaranteed ChatGPT→Codex-session-UUID push API. The fallback/proven interaction may be Codex posts to a configured ChatGPT control chat, ChatGPT replies there, Codex reads correlated reply. If product capabilities change, correlation/persistence requirements remain unless workflow `main` deliberately changes.

## 8. User interaction

The user should make real strategic/authorization decisions, not manually transport long state. Do not require the user to copy plans/OpenSpec/evidence/handoffs or choose the next card when Task Board selection is deterministic.
