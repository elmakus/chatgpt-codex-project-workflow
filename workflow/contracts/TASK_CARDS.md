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

### Capability routing invariant

Project routing assumes:

`ChatGPT capabilities ⊆ Codex capabilities`

The difference between executors is therefore not that ChatGPT may have a required capability unavailable to Codex. ChatGPT Capability Gate is used **before assignment** to decide whether ChatGPT can execute or, under `mixed`, the card should be handed to Codex.

Once a card has started, a newly discovered missing runtime capability is a blocker for the assigned executor, not a reason for automatic fallback/rerouting. If Codex discovers the missing capability, persist the blocker, report `USER ACTION REQUIRED`, obtain the missing MCP/access/credential/runtime/tooling or other capability from the user, then resume the same Codex card.

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

A READY card may remain unscheduled when the current parallel-card limit is full or when its mutable ownership conflicts with another active card. Readiness and scheduling are separate facts.

Do not ask the user which card comes next when Task Board provides an unambiguous executable card or executable ready set.

## 7. Optional bounded-parallel metadata

Project execution is serial by default. A project or milestone may opt into `execution_mode: bounded_parallel` in its Task Board. This is a scheduling policy over ordinary Task Cards, not a new lifecycle state and not a generic DAG engine.

A card may participate in a parallel execution set only when it explicitly records:

```yaml
parallel_safe: true
write_scope:
  - <repo-relative path or bounded glob>
exclusive_resources:
  - <logical mutable resource, when applicable>
```

Rules:
- omitted `parallel_safe` means `false`;
- a mutable parallel card must have a bounded `write_scope`; a genuinely read-only card may use an empty `write_scope`;
- simultaneously active cards must have non-overlapping mutable `write_scope` and no shared `exclusive_resources`;
- if ownership cannot be bounded confidently, keep the card serial;
- files that hold project-global execution state, such as the Task Board, milestone-wide handoff/acceptance state and shared integration metadata, are coordinator-owned and must not be assigned as worker write scope;
- a dependency must already be `done`; two cards are not made parallel merely because they belong to the same milestone;
- external mutable systems can be named as `exclusive_resources` even when repository write scopes do not overlap;
- unexpected overlap discovered during execution is a coordination blocker for the affected lanes, not permission to race writes.

`code_locations` describes where implementation is expected. `write_scope` is narrower: it defines mutable ownership while the card is running in parallel.

## 8. Refresh Gate

Every card is reconciled immediately before implementation against actual current state.

At minimum compare:
- repo branch/HEAD/working tree and relevant runtime state;
- latest cumulative handoff;
- current milestone/card;
- relevant requirements/accepted decisions/Master Plan;
- relevant OpenSpec;
- completed dependencies;
- actual interfaces;
- required capabilities, tests/checks and evidence/readback path;
- when parallel execution is planned, exact lane base plus current `write_scope`/`exclusive_resources` assumptions.

Implementation-detail drift within approved contracts may be reconciled by the current executor. Material behavior/architecture/requirement/external-contract/milestone-acceptance drift blocks the card and requires strategic resolution.

Before assignment, unavailable required capabilities are handled by project `execution_policy` and the ChatGPT Capability Gate. After assignment/execution start, a newly discovered missing capability follows runtime blocker semantics in `workflow/EXECUTION.md` and `GITHUB_STATE.md`; do not automatically reroute the card.

## 9. Definition of Done

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
13. when executed in a parallel lane, the accepted lane result has been integrated into the intended milestone state and required post-integration checks are green;
14. no unassigned TODO remains inside accepted scope.

`done` is verified state, not an agent assertion.

## 10. Result section

At close persist:

```text
executor:
result_commit:
result_pr:
evidence:
tests_summary:
```

For a parallel lane, evidence also identifies the exact lane base/branch or equivalent isolated workspace and the integrated target state used for final verification.

The same essential pointers appear in Task Board.

## 11. Dependency and parallel-set handling

Completion may unblock dependent cards. A generic DAG engine is unnecessary: explicit `depends_on`, Task Board state and the bounded-parallel ownership rules above are sufficient.

For `serial`, select one deterministic READY card.

For `bounded_parallel`, select a deterministic set of READY cards up to `parallel_card_limit` such that every selected card is `parallel_safe` and pairwise compatible by `write_scope` and `exclusive_resources`. Do not maximize concurrency when a smaller set materially reduces integration risk or duplicated work.

## 12. Near-term versus distant cards

Near-term cards may contain detailed implementation expectations. Distant cards stay functionally precise without freezing interfaces that do not yet exist. Refresh Gate is mandatory before execution.

## 13. Scope discipline

The current executor implements only bounded card scope unless a necessary adjacent change is clearly within the same acceptance contract and documented, a new bounded corrective/dependency card is created, or strategic authority explicitly changes the plan.

Do not hide unrelated cleanup or architecture changes inside a card.
