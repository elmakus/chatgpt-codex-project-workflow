# Task Card Contract

## 1. Meaning

A Task Card is a bounded global work-package **contract** for one project. It defines scope, acceptance, tests and execution boundaries. It is not the live execution-state record and it is not an OpenSpec `tasks.md` checkbox.

Live card status, assigned executor, lane/base pointers and result pointers live only in `implementation/TASK_BOARD.yaml`.

## 2. Required contract fields

Each Task Card should define:
- `id`, `title`, `milestone`;
- priority, complexity, phase;
- expected/relevant `code_locations`;
- `depends_on`;
- outcome, included/excluded scope and constraints;
- acceptance criteria and required tests/checks;
- relevant Master Plan/requirement/decision refs;
- OpenSpec candidate/ref;
- Refresh Gate requirements;
- blocker/escalation rule;
- Definition of Done contract.

Do **not** put mutable `execution_status`, assigned executor, `result_commit`, `result_pr`, evidence status or current branch/HEAD into the Task Card file.

Use `templates/TASK_CARD.md`.

## 3. Optional capability requirements

Add `required_capabilities` only when explicit capabilities materially improve safety or mixed-policy routing, especially external, unusual, high-risk or environment-specific work.

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

Capability Gate is used **only** under `execution_policy: mixed` before assignment.

Under `chatgpt_only`, the card is assigned to ChatGPT without Capability Gate. Under `codex_only`, it is assigned to Codex without Capability Gate. A known or discovered missing capability becomes a blocker for the fixed executor; policy does not change automatically.

Once a card has started, a newly discovered missing runtime capability is a blocker for the assigned executor, not a reason for automatic fallback/rerouting.

## 4. Executor provenance

Executor provenance is mutable execution state and therefore lives in Task Board only.

At actual start record `executor: chatgpt | codex` in the Task Board card entry. Do not mirror that value into the Task Card contract.

Policy determines assignment as follows:
- `chatgpt_only` → ChatGPT;
- `codex_only` → Codex;
- `mixed` → result of Capability Gate.

## 5. Status model

Execution state is stored only in Task Board:

`planned | ready | in_progress | blocked | done | superseded`

Decision state, when useful, is independently:

`accepted | deferred | rejected | review`

A decision can be accepted while implementation remains planned.

## 6. Readiness

A Task Board card becomes `ready` only when:
- dependencies needed to start are `done`;
- required authoritative inputs exist;
- acceptance is testable enough to execute;
- no known unresolved strategic blocker exists;
- there is at least a plausible execution/evidence path under project policy.

A READY card may remain unscheduled when the current parallel-card limit is full or its mutable ownership conflicts with another active card. Readiness and scheduling are separate facts.

Do not ask the user which card comes next when Task Board provides an unambiguous executable card or compatible ready set.

## 7. Optional bounded-parallel contract metadata

Project execution is serial by default. A project or milestone may opt into `execution_mode: bounded_parallel` in Task Board.

A Task Card contract may participate in a parallel execution set only when it explicitly records:

```yaml
parallel_safe: true
write_scope:
  - <repo-relative path or bounded glob>
exclusive_resources:
  - <logical mutable resource, when applicable>
```

Rules:
- omitted `parallel_safe` means `false`;
- a mutable parallel card must have bounded `write_scope`; a genuinely read-only card may use an empty scope;
- simultaneously active cards must have non-overlapping mutable `write_scope` and no shared `exclusive_resources`;
- if ownership cannot be bounded confidently, keep the card serial;
- Task Board, milestone-wide handoff/acceptance state and shared integration bookkeeping are coordinator-owned and never lane-worker write scope;
- a dependency must already be `done` in Task Board;
- external mutable systems can be named as `exclusive_resources` even when repository scopes do not overlap;
- unexpected overlap discovered during execution is a coordination blocker, not permission to race writes.

`code_locations` describes expected implementation surface. `write_scope` defines mutable ownership while a card is running in parallel.

## 8. Refresh Gate

Every card is reconciled immediately before implementation against actual current state.

At minimum compare:
- repo branch/HEAD/working tree and relevant runtime/external state;
- Task Board current milestone/card/set and exact execution pointers;
- latest cumulative handoff;
- relevant requirements/accepted decisions/Master Plan/milestone contract;
- relevant OpenSpec;
- completed dependencies;
- actual interfaces;
- required capabilities, tests/checks and evidence/readback path;
- when parallel, exact lane base plus current `write_scope`/`exclusive_resources` assumptions.

Implementation-detail drift within approved contracts may be reconciled by the current executor. Material behavior/architecture/requirement/external-contract/milestone-acceptance drift blocks the card and requires strategic resolution.

Under `mixed`, unavailable required capabilities may affect pre-assignment routing through Capability Gate. Under fixed policies, and after any assignment, missing capability follows runtime blocker semantics in `workflow/EXECUTION.md`; do not automatically change executor or policy.

## 9. Definition of Done contract

A Task Board card may be marked `done` only when all applicable items hold:
1. included scope complete and excluded scope not silently expanded;
2. acceptance satisfied;
3. required tests/checks ran;
4. checks green or authorized baseline exception exists;
5. relevant OpenSpec requirements satisfied;
6. no hidden blocker remains;
7. accepted result exists in durable Git/external state;
8. Task Board state/result pointers reconciled;
9. assigned executor and result commit recorded in Task Board;
10. result PR recorded when applicable, otherwise `null`;
11. durable evidence identifies exact checks/review;
12. relevant external side effects/idempotency/reconciliation/readback verified where required;
13. when parallel, the accepted lane result has been integrated and required post-integration checks are green;
14. no unassigned TODO remains inside accepted scope.

`done` is verified state, not an agent assertion. The Task Card file itself is not edited merely to mark these checks complete.

## 10. Result state

At close persist mutable result state in Task Board:

```yaml
execution_status: done
executor: chatgpt | codex
result_commit: <sha>
result_pr: <number-or-null>
evidence: <repo-relative-path>
tests_summary: <concise summary or evidence pointer>
```

For a parallel lane, evidence also identifies the exact lane base/branch or equivalent isolated workspace and integrated verification target.

## 11. Dependency and parallel-set handling

Completion may unblock dependent cards. A generic DAG engine is unnecessary: explicit `depends_on`, Task Board state and bounded-parallel ownership rules are sufficient.

For `serial`, select one deterministic READY card.

For `bounded_parallel`, select a deterministic set of READY cards up to `parallel_card_limit` such that every selected card is `parallel_safe` and pairwise compatible by `write_scope` and `exclusive_resources`.

## 12. Near-term versus distant cards

Near-term cards may contain detailed implementation expectations. Distant cards stay functionally precise without freezing interfaces that do not yet exist. Refresh Gate is mandatory before execution.

## 13. Scope discipline

The current executor implements only bounded card scope unless a necessary adjacent change is clearly within the same acceptance contract and documented, a new bounded corrective/dependency card is created, or strategic authority explicitly changes the plan.

Do not hide unrelated cleanup or architecture changes inside a card.
