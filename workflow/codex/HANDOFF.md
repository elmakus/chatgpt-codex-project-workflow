# ChatGPT ↔ Codex Handoff Contract

This is the only Codex-specific module ChatGPT normally needs when preparing or interpreting Codex execution communication.

## 1. ChatGPT → Codex kickoff

A kickoff stays short and points to durable state. Task Board is the live execution-state authority.

### Mixed-policy bounded assignment

Include:
- workflow authority `elmakus/chatgpt-codex-project-workflow:main`;
- project repository;
- integration branch when known;
- assigned milestone and Task Card/compatible ready set;
- execution mode/parallel-card limit when relevant;
- required prior checkpoint;
- durable Task Board pointer;
- material evidence/readback obligations;
- exact Task Card authority slice/pointers; the kickoff itself need not paste the referenced material;
- instruction to run the state/contract Refresh Gate;
- stop conditions.

Example:

```text
Use current main of elmakus/chatgpt-codex-project-workflow.
Project repo: <owner/repo>
Execution policy: mixed
Durable start pointer: implementation/TASK_BOARD.yaml
Assigned milestone/set: <MXX / MXX-TYY[, ...]>
Required prior checkpoint: <sha/tag>

Recover Task Board/Git state, current Task Card contract and its exact authority slice; run the state/contract Refresh Gate and execute only assigned scope. The mixed Capability Gate already handled pre-assignment routing; do not run another capability preflight. If a concrete runtime operation cannot proceed, persist the blocker. Persist tests/evidence/result/review pointers in Task Board. Stop for a real runtime blocker, strategic authority change, explicit user authorization gate or unsatisfied acceptance/evidence.
```

### Codex-only continuous execution

When user selected `codex_only`, kickoff may authorize the already-approved multi-milestone sequence rather than one card at a time:

```text
Use current main of elmakus/chatgpt-codex-project-workflow.
Project repo: <owner/repo>
Execution policy: codex_only
Durable start pointer: implementation/TASK_BOARD.yaml
Approved plan: <planning/MASTER_PLAN.md>
Start from: <checkpoint/current milestone>

Recover durable state, resolve each Task Card's exact authority slice and execute deterministic READY work. Run state/contract Refresh Gates but do not run Capability Gate or capability preflight/inventory. Attempt concrete operations directly. Self-remediate ordinary non-secret local tooling/dependency gaps when permitted. Ask the user only when a concrete operation requires unavailable MCP/credential/token/access/authorization that Codex cannot obtain itself.

When installed/enabled, codex_workflow controls internal execute/review-worker orchestration. REQUIRED/RECOMMENDED independent review uses a reviewer worker/session that did not implement the exact subject; do not return to ChatGPT merely for reviewer independence.

After each GREEN milestone, continue automatically into the next already-approved milestone using just-in-time execution prep + fresh state/contract Refresh Gate. Stop only for a real non-self-remediable runtime blocker, strategic/product/architecture blocker, explicit user/deployment/live-write authorization gate, RED requiring strategic resolution, or end of approved scope.
```

Do not paste whole plan/history/OpenSpec trees/large diffs into chat. Point to exact authority instead. Context may be smaller than the planner's original context, but applicable authoritative constraints must survive by explicit carry-forward or mandatory exact-reference read.

## 2. Codex → ChatGPT normal return

Codex returns project truth through repository, not a multi-page copy/paste report. Persist Task Board state, result commit/PR, tests/evidence, review state/evidence, external readback, blocker records and milestone handoff as applicable.

Do not duplicate live state into Task Card/milestone/PROJECT files.

For bounded-parallel execution, durable return state identifies every still-active lane/base and every integrated/done card.

A fresh ChatGPT chat recovers from `PROJECT.md` for high-level routing and Task Board for live execution truth.

Under `codex_only`, routine GREEN milestone completion or an internally orchestrated independent review is **not** a reason to return to ChatGPT when automatic continuation conditions hold.

## 3. Strategic escalation

Do not use ChatGPT as a routine Codex message bus.

Use strategic escalation when evidence reveals contradictory requirements, required architecture/product decisions, impossible/wrong acceptance, frozen-plan invalidation, material external-contract change, or behavior/security/schema choices beyond Codex authority.

Routine implementation details within approved contracts remain executor detail. A simple lane conflict that can be serialized without changing accepted scope is coordinator detail; a conflict proving approved decomposition/architecture wrong is strategic.

## 4. Strategic blocker lifecycle

When Codex uses configured ChatGPT control-chat mechanism:
1. stop dependent/affected work and set Task Board card `blocked`;
2. write complete blocker evidence under `implementation/blockers/`;
3. safely commit/push evidence when possible;
4. post short structured request with unique `request_id`;
5. ChatGPT reads durable evidence and only needed context;
6. ChatGPT researches further if required;
7. ChatGPT replies with exact same `request_id` and authoritative `DECISION FOR CODEX:` line;
8. Codex accepts only matching structured decision;
9. Codex persists accepted decision under `decisions/` with provenance;
10. reconcile contracts/OpenSpec/plan/Task Board as required;
11. resume only after blocker is resolved.

Unrelated compatible lanes may continue only when blocker does not invalidate dependencies, ownership, external resources or acceptance assumptions.

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

Please review durable evidence and reply with SAME request_id and one authoritative line beginning:
DECISION FOR CODEX:
```

## 6. Decision format and correlation

```text
request_id: <exact same request_id>
DECISION FOR CODEX: <decision>
```

Codex never treats arbitrary ChatGPT prose as execution decision; matching ID + marker is required.

After receipt, persist project/task, timestamp, chat/thread identity when available, exact request ID/decision marker, concise rationale, impact, artifacts updated and persisting commit.

Chat is transport. Repository is durable truth.

## 7. Channel asymmetry

Do not design around guaranteed ChatGPT→Codex-session-UUID push API. If product capabilities change, correlation/persistence requirements remain unless workflow `main` deliberately changes.

## 8. User interaction

The user should make real strategic/authorization decisions, not manually transport long state. Do not require user to copy plans/OpenSpec/evidence/handoffs or choose next card/ready set/milestone when durable selection is deterministic.
