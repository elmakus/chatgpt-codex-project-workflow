# GitHub State Contract

This is the normative contract for durable execution state in a project repository, independent of whether the active executor is ChatGPT or Codex.

## 1. Card execution states

Allowed card `execution_status` values:

```text
planned
ready
in_progress
blocked
done
superseded
```

Decision state is separate and, when used, has:

```text
accepted
deferred
rejected
review
```

Do not infer execution completion from decision acceptance.

## 2. Milestone execution lifecycle

Normal milestone lifecycle:

```text
planned → ready → in_progress → done
```

`blocked` is allowed for an unresolved milestone gate/blocker. `superseded` requires an explicit decision.

A milestone that passed its green acceptance gate must not remain `ready` or `in_progress`.

## 3. Task Board

`implementation/TASK_BOARD.yaml` is the live index of execution state, not the complete implementation narrative.

It should identify at least:
- project;
- plan revision/reference;
- current milestone;
- milestone states and checkpoint fields;
- card states, dependencies and active executor when applicable;
- result pointers;
- relevant OpenSpec change;
- branch/PR information when needed to recover in-flight work;
- strategic control-chat identity only when that optional Codex communication mechanism is configured.

## 4. Starting a card

When execution begins:
- Task Board card `ready → in_progress`;
- card file `Execution status: IN_PROGRESS`;
- record `executor: chatgpt | codex` in card and Task Board;
- milestone `ready → in_progress` when this is its first real started card;
- persist a Refresh Gate note/evidence only when the gate discovers something material.

The durable transition should be committed/pushed according to project branch policy before relying on it for recovery.

## 5. Done-card result pointer contract

Before a card is terminal `done`, both Task Board and card Result section must record:

```yaml
execution_status: done
executor: chatgpt | codex
result_commit: <sha>
result_pr: <number-or-null>
evidence: <repo-relative-path>
```

The card also records a concise `tests_summary`.

Rules:
- `result_commit` identifies the commit containing or verifiably representing the accepted result.
- `result_pr` identifies the PR when applicable. If no PR applies, use `null` and project branch policy must make publication path unambiguous.
- `evidence` points to durable test/review evidence or an unambiguous cumulative evidence section.
- evidence names exact tests/review/checks; `tests passed` alone is insufficient.
- when material external writes require readback under `workflow/EXECUTION.md`, evidence records the target, readback method and verified resulting state.

## 6. Definition of Done state coupling

A card can be `done` only after the Task Card Definition of Done has passed. At minimum:
- scope is complete;
- acceptance criteria are satisfied;
- required tests/checks ran;
- tests/checks are green or a baseline exception was explicitly accepted;
- relevant OpenSpec requirements are satisfied;
- no hidden blocker remains;
- result exists in durable repository state;
- Task Board is updated;
- result pointers/evidence are durable;
- relevant side effects/readback/idempotency/reconciliation are verified;
- no unassigned TODO remains inside accepted scope.

## 7. Blocked card

When execution is blocked:
- card `execution_status: blocked`;
- write durable evidence under `implementation/blockers/` when material;
- make a safe commit/push before messaging when possible;
- do not start dependent cards.

For a missing capability/evidence path, re-apply project `execution_policy` and `workflow/chatgpt/CAPABILITY_GATE.md`. Under `chatgpt_only`, missing ChatGPT capability remains blocked until capability or policy changes by user decision.

For a strategic/product/architecture blocker, obtain the relevant authority decision and persist an accepted decision record under `decisions/`. When Codex uses a correlated ChatGPT control-chat exchange, follow `workflow/codex/HANDOFF.md` including matching `request_id` and `DECISION FOR CODEX:`.

Resume only after the blocker is actually resolved and Task Card/OpenSpec/plan/Task Board are reconciled as required.

## 8. Milestone GREEN

A milestone is not done merely because all cards are done.

After integrated acceptance is GREEN:
1. finalize implementation branch/PR according to project policy;
2. write/reconcile `project-handoffs/MXX_HANDOFF.md`;
3. write acceptance evidence under `implementation/evidence/`;
4. record exact final `implementation_head`;
5. record checkpoint/tag according to project policy;
6. set milestone `execution_status: done`;
7. ensure every required card is `done` and has result pointers.

A done milestone stores at minimum:

```yaml
execution_status: done
checkpoint: <checkpoint-or-tag>
implementation_head: <sha>
handoff: project-handoffs/MXX_HANDOFF.md
acceptance_evidence: implementation/evidence/MXX_ACCEPTANCE.md
```

## 9. Corrective work

If integrated milestone acceptance is RED:
- do not mark the milestone done;
- reopen the appropriate card or create a bounded corrective card;
- record failing evidence;
- preserve dependencies, capability gates and strategic escalation rules.

## 10. Cumulative handoff and recovery

`project-handoffs/MXX_HANDOFF.md` is the canonical cumulative handoff for the completed milestone.

Fresh-session recovery also uses:
- exact Git branch/HEAD;
- Task Board;
- current milestone/card;
- recorded executor for in-flight work;
- relevant OpenSpec;
- evidence/result pointers.

A local `current.md` is optional convenience only and cannot be required for recovery.

## 11. Repository topology changes

Do not change project repository ownership/layout in the middle of an active milestone. Legacy split-repository migration occurs only at a green milestone boundary and follows `PROJECT_REPOSITORY.md`.

## 12. Consistency invariants

Invalid states include:
- card `done` with missing required result pointers or executor provenance;
- milestone `done` with missing checkpoint, `implementation_head`, handoff or acceptance evidence;
- all required cards `done` while a green milestone remains `ready`;
- a dependent card `in_progress` while a required dependency is `blocked`;
- durable state existing only in chat or local `current.md`;
- Task Board/card disagreement left unreconciled at a durable checkpoint;
- claimed external success when required readback/verification evidence shows a different persisted state.
