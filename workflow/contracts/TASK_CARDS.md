# Task Card Contract

## 1. Meaning

A Task Card is a bounded global work package for one project. It is not an OpenSpec `tasks.md` checkbox; OpenSpec tasks are smaller implementation steps inside one behavior/design change.

## 2. Required fields

Each Task Card should define:
- `id`, `title`, `milestone`;
- optional `decision_state`;
- `execution_status`;
- `executor: null | chatgpt | codex`;
- priority, complexity, phase;
- expected/relevant `code_locations`;
- `depends_on`;
- outcome, included/excluded scope, constraints;
- acceptance criteria and required tests/checks;
- relevant Master Plan/requirement/decision refs;
- OpenSpec candidate/ref;
- Refresh Gate;
- blocker/escalation rule;
- Result section and Definition of Done.

Use `templates/TASK_CARD.md`.

## 3. Optional capability requirements

Add `required_capabilities` only when explicit capabilities materially improve routing or safety, especially external, unusual, high-risk or environment-specific work.

Example:

```yaml
required_capabilities:
  - liftosaur_write
  - liftosaur_readback
```

Do not require declarations for every trivial repository operation. Ordinary capabilities are inferred from scope, acceptance, tests/checks, external effects and evidence.

## 4. Executor provenance

Leave `executor: null` while merely planned/ready unless an approved plan intentionally preassigns Codex. At actual start, record `chatgpt` or `codex` in card and Task Board.

This field supports recovery/provenance. It is not an executor score and does not override project `execution_policy`.

## 5. Status model

Execution state is:

`planned | ready | in_progress | blocked | done | superseded`

Decision state, when useful, is independently:

`accepted | deferred | rejected | review`

A decision can be accepted while implementation remains planned.

## 6. Readiness

A card becomes `ready` only when:
- dependencies needed to start are done;
- required authoritative inputs exist;
- acceptance is testable enough to execute;
- no known unresolved strategic blocker exists;
- there is at least a plausible execution/evidence path under project policy.

Do not ask the user which card comes next when Task Board provides one unambiguous READY card.

## 7. Refresh Gate

Every card is reconciled immediately before implementation against actual current state.

At minimum compare:
- repo branch/HEAD/working tree and relevant runtime state;
- latest cumulative handoff;
- current milestone/card;
- relevant requirements/accepted decisions/Master Plan;
- relevant OpenSpec;
- completed dependencies;
- actual interfaces;
- required capabilities, tests/checks and evidence/readback path.

Implementation-detail drift within approved contracts may be reconciled by the current executor. Material behavior/architecture/requirement/external-contract/milestone-acceptance drift blocks the card and requires strategic resolution.

If a required capability/evidence path is unavailable, do not pretend completion; apply `execution_policy` and Capability Gate.

## 8. Definition of Done

A card is `done` only when all applicable items hold:
1. included scope complete and excluded scope not silently expanded;
2. acceptance satisfied;
3. required tests/checks ran;
4. checks green or authorized baseline exception exists;
5. relevant OpenSpec requirements satisfied;
6. no hidden blocker remains;
7. accepted result exists in durable Git state;
8. Task Board/Card states reconciled;
9. `executor` and `result_commit` recorded;
10. `result_pr` recorded when applicable, otherwise `null`;
11. durable evidence identifies exact checks/review;
12. relevant external side effects/idempotency/reconciliation/readback verified where required;
13. no unassigned TODO remains inside accepted scope.

`done` is verified state, not an agent assertion.

## 9. Result section

At close persist:

```text
executor:
result_commit:
result_pr:
evidence:
tests_summary:
```

The same essential pointers appear in Task Board.

## 10. Dependency handling

Completion may unblock dependent cards. A generic DAG engine is unnecessary; explicit `depends_on` plus Task Board state are sufficient unless a concrete project need proves otherwise.

## 11. Near-term versus distant cards

Near-term cards may contain detailed implementation expectations. Distant cards stay functionally precise without freezing interfaces that do not yet exist. Refresh Gate is mandatory before execution.

## 12. Scope discipline

The current executor implements only bounded card scope unless a necessary adjacent change is clearly within the same acceptance contract and documented, a new bounded corrective/dependency card is created, or strategic authority explicitly changes the plan.

Do not hide unrelated cleanup or architecture changes inside a card.
