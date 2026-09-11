# GitHub State Contract

This is the normative durable execution-state contract for project repositories.

## Card states

`planned | ready | in_progress | blocked | done | superseded`

Decision state, when useful: `accepted | deferred | rejected | review`.

## Milestone lifecycle

`planned → ready → in_progress → done`, with `blocked` or explicit `superseded` where justified.

## Task Board

`implementation/TASK_BOARD.yaml` is the live execution index. It should identify current milestone, card states/dependencies, result pointers, relevant OpenSpec, branch/PR recovery pointers and the active executor where applicable.

## Starting a card

When execution begins:
- card `ready → in_progress`;
- card file reflects `IN_PROGRESS`;
- record `executor: chatgpt | codex`;
- milestone becomes `in_progress` on first real execution;
- persist durable transition according to branch policy.

## Done-card result contract

Before `done`, Task Board and card Result record:

```yaml
execution_status: done
executor: chatgpt | codex
result_commit: <sha>
result_pr: <number-or-null>
evidence: <repo-relative-path>
```

plus a concise tests/checks summary.

A card is done only after scope, acceptance, required tests/checks, relevant OpenSpec, evidence, side effects and Task Board/card consistency are verified. For material external writes, evidence includes readback/verification when required by the shared execution contract.

## Blocked card

When execution cannot meet capability, strategic or evidence requirements:
- set card `blocked`;
- persist exact evidence/reason;
- do not start dependent cards;
- apply project policy before any executor reassignment;
- persist accepted strategic decisions in `decisions/` before resuming.

## Milestone GREEN

After integrated GREEN acceptance:
1. finalize branch/PR as applicable;
2. reconcile cumulative handoff;
3. persist acceptance evidence;
4. record exact `implementation_head` and checkpoint;
5. set milestone `done`;
6. ensure required cards are done with complete result pointers.

Invalid states include done cards without required pointers, done milestones without checkpoint/head/handoff/evidence, dependent work running across blocked dependencies, or important execution truth existing only in chat.
