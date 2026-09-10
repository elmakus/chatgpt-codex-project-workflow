# Task Card Contract

## 1. Meaning

A Task Card is a bounded global work package for one project.

It is not an OpenSpec `tasks.md` checkbox. OpenSpec tasks are smaller implementation steps inside a behavior/design change.

## 2. Required fields

Each Task Card should define:

- `id`;
- `title`;
- `milestone`;
- optional `decision_state`;
- `execution_status`;
- `priority`;
- `complexity`;
- `phase`;
- expected/relevant `code_locations`;
- `depends_on`;
- outcome;
- included scope;
- excluded scope;
- constraints;
- acceptance criteria;
- required tests;
- relevant Master Plan/requirement/decision references;
- OpenSpec candidate/ref;
- Refresh Gate;
- strategic escalation rule;
- Result section;
- Definition of Done.

Use `templates/TASK_CARD.md`.

## 3. Status model

Card execution state is one of:

`planned | ready | in_progress | blocked | done | superseded`

Decision state, when useful, is independently:

`accepted | deferred | rejected | review`

A decision can be accepted while implementation remains planned.

## 4. Readiness

A card becomes `ready` only when:
- dependencies needed to start are done;
- required authoritative inputs exist;
- acceptance is testable enough to execute;
- there is no known unresolved strategic blocker.

Do not ask the user which card comes next when the Task Board provides one unambiguous READY card.

## 5. Refresh Gate

Every card is reconciled immediately before implementation against actual current state.

At minimum compare:
- repo branch/HEAD/working tree;
- latest cumulative handoff;
- current milestone;
- current card;
- relevant requirements/accepted decisions/Master Plan sections;
- relevant OpenSpec;
- completed dependencies;
- actual code locations/interfaces.

Implementation-detail drift within approved contracts may be reconciled by Codex.

Material behavior/architecture/requirement/external-contract/milestone-acceptance drift blocks the card and requires strategic escalation.

## 6. Definition of Done

A card is `done` only when all applicable items hold:

1. included scope is complete and excluded scope was not silently expanded;
2. acceptance criteria are satisfied;
3. all required tests/checks ran;
4. tests/checks are green or an explicitly authorized baseline exception exists;
5. relevant OpenSpec requirements are satisfied;
6. no hidden blocker remains;
7. the accepted result exists in durable Git state;
8. Task Board and Task Card states are reconciled;
9. `result_commit` is recorded;
10. `result_pr` is recorded when applicable, otherwise explicitly `null`;
11. durable evidence is recorded and identifies exact checks;
12. relevant external side effects/idempotency/reconciliation have been verified;
13. no unassigned TODO remains inside accepted scope.

`done` is a verified state, not an agent assertion.

## 7. Result section

At close, persist:

```text
result_commit:
result_pr:
evidence:
tests_summary:
```

The same essential pointers must appear in the Task Board.

## 8. Dependency handling

Completion of a card may unblock dependent cards.

A generic DAG engine is unnecessary. Explicit `depends_on` relationships plus Task Board state are sufficient unless the project has a concrete reason for more machinery.

## 9. Near-term versus distant cards

Near-term cards may contain detailed implementation expectations.

Distant cards should remain functionally precise but avoid freezing interfaces that do not yet exist. Refresh Gate is mandatory before execution and may update implementation details without changing accepted behavior.

## 10. Scope discipline

Codex implements only the current card's bounded scope unless:
- a necessary adjacent change is clearly within the same acceptance contract and is documented; or
- a new bounded corrective/dependency card is created; or
- strategic authority explicitly changes the plan.

Do not hide unrelated cleanup or architecture changes inside a card.
