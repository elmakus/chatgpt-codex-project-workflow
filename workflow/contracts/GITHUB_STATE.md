# GitHub State Contract

This is the normative contract for durable execution state in a project repository.

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
- card states and dependencies;
- result pointers;
- relevant OpenSpec change;
- branch/PR information when needed to recover in-flight work;
- strategic control-chat identity when that mechanism is configured.

## 4. Starting a card

When execution begins:
- Task Board card `ready → in_progress`;
- card file `Execution status: IN_PROGRESS`;
- milestone `ready → in_progress` when this is its first real started card;
- persist a Refresh Gate note/evidence only when the gate discovers something material.

The durable transition should be committed/pushed according to the project branch policy before relying on it for recovery.

## 5. Done-card result pointer contract

Before a card is terminal `done`, both Task Board and card Result section must record:

```yaml
execution_status: done
result_commit: <sha>
result_pr: <number-or-null>
evidence: <repo-relative-path>
```

The card also records a concise `tests_summary`.

Rules:
- `result_commit` identifies the commit containing or verifiably representing the accepted result.
- `result_pr` identifies the PR when applicable. If no PR applies, use `null` and the project branch policy must make the publication path unambiguous.
- `evidence` points to durable test/review evidence or an unambiguous cumulative evidence section.
- evidence names the exact tests/review/checks; `"tests passed"` by itself is insufficient.

## 6. Definition of Done state coupling

A card can be `done` only after the Task Card Definition of Done has passed. At minimum:
- scope is complete;
- acceptance criteria are satisfied;
- required tests ran;
- tests are green or a baseline exception was explicitly accepted;
- relevant OpenSpec requirements are satisfied;
- no hidden blocker remains;
- result exists in the repository;
- Task Board is updated;
- result pointers/evidence are durable;
- relevant side effects are reconciled;
- no unassigned TODO remains inside the card's accepted scope.

## 7. Blocked card

When a strategic blocker is found:
- card `execution_status: blocked`;
- write durable evidence under `implementation/blockers/`;
- make a safe commit/push before messaging when possible;
- send a strategic request with a unique `request_id`;
- after an authoritative matching decision, write its accepted decision record under `decisions/`;
- reconcile Task Card/OpenSpec/plan/Task Board as required;
- resume only after the blocker is actually resolved.

Do not start dependent cards while their dependency is blocked.

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
- record the failing evidence;
- preserve dependencies and strategic escalation rules.

## 10. Cumulative handoff and recovery

`project-handoffs/MXX_HANDOFF.md` is the canonical cumulative handoff for the completed milestone.

Fresh-session recovery also uses:
- exact Git branch/HEAD;
- Task Board;
- current milestone/card;
- relevant OpenSpec;
- evidence/result pointers.

A local `current.md` is optional convenience only and cannot be required for recovery.

## 11. Repository topology changes

Do not change project repository ownership/layout in the middle of an active milestone.

Legacy split-repository migration occurs only at a green milestone boundary and follows `PROJECT_REPOSITORY.md`.

## 12. Consistency invariants

The following states are invalid:
- card `done` with missing required result pointers;
- milestone `done` with missing checkpoint, `implementation_head`, handoff or acceptance evidence;
- all required cards `done` while a green milestone remains `ready`;
- a dependent card `in_progress` while a required dependency is `blocked`;
- durable state existing only in chat or local `current.md`;
- Task Board/card disagreement left unreconciled at a durable checkpoint.
