# Task Card Contract

## 1. Meaning

A Task Card is a bounded global work-package **contract** for one project. It defines scope, acceptance, tests and execution boundaries. It is not the live execution-state record and it is not an OpenSpec `tasks.md` checkbox.

Live card status, assigned executor, lane/base pointers, review state and result pointers live only in `implementation/TASK_BOARD.yaml`.

## 2. Required contract fields

Keep the mandatory card contract small. Each Task Card defines:
- `id`, `title`, `milestone`;
- `depends_on`;
- exact durable **authority refs / authority slice**;
- outcome and bounded included/excluded scope;
- acceptance criteria and required tests/checks;
- every material constraint, external-write/readback obligation, authorization gate or independent-review requirement that applies.

Priority, complexity, phase, expected/relevant `code_locations`, capability hints and parallel metadata are optional and should exist only when they improve execution/routing/recovery.

Workflow-standard Refresh Gate, blocker/escalation behavior and Definition of Done are inherited from this contract and `workflow/EXECUTION.md`; do not repeat them in every card unless the card has a material override.

Do **not** put mutable `execution_status`, assigned executor, `result_commit`, `result_pr`, review state, evidence status or current branch/HEAD into the Task Card file.

Use `templates/TASK_CARD.md`.

### Authority Preservation Rule

Delegation may reduce context volume, but it must not reduce authoritative constraints applicable to the delegated scope.

The card's authority slice should point as precisely as practical to requirements, accepted decisions, Master Plan/milestone sections, relevant OpenSpec and accepted dependency results. For each downstream execution or review package, the coordinator must either:
1. carry every applicable implementation-shaping constraint explicitly without changing its meaning; or
2. require the worker/reviewer to read the exact durable authority before acting.

Must-carry information includes, when applicable:
- invariants and accepted behavior/architecture choices;
- failure semantics and compatibility requirements;
- explicit exclusions or rejected paths that constrain implementation;
- external-write, security, migration and data-integrity boundaries;
- acceptance/test obligations;
- dependency-result contracts;
- rationale when omitting it could reasonably lead to a different implementation choice.

A summary, title or coordinator paraphrase never outranks exact referenced authority. If the package and authority conflict, stop and reconcile the conflict rather than guessing.

Executor and independent reviewer should evaluate the same applicable authority slice. Worker completion should identify satisfied authority/acceptance and surface material deviation or conflicting evidence; reviewer checks the result against the same authority rather than reviewing only the diff in isolation.

## 3. Optional capability requirements

Add `required_capabilities` only when explicit capabilities materially improve **mixed-policy routing** or document unusual external/security/user-authorization prerequisites.

Example:

```yaml
required_capabilities:
  - liftosaur_write
  - liftosaur_readback
```

Do not require declarations for every trivial repository operation.

### Capability routing invariant

Project routing assumes:

`ChatGPT capabilities ⊆ Codex capabilities`

Capability Gate is used **only** under `execution_policy: mixed` before assignment.

Under `chatgpt_only`, the card is assigned to ChatGPT without Capability Gate or capability preflight. Under `codex_only`, it is assigned to Codex without Capability Gate or capability preflight.

`required_capabilities` metadata does **not** instruct fixed-policy execution to inventory/verify tools before starting. In fixed modes, a capability becomes a blocker only when a concrete required operation cannot proceed.

Once a card has started, a newly discovered runtime capability problem is handled by `workflow/EXECUTION.md`. Ordinary self-remediable Codex tooling/dependency gaps are implementation detail; user-provided MCP/credential/token/access becomes a blocker when concretely needed and unavailable.

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

Independent review has separate mutable Task Board state when active:

`pending | in_progress | green | red`

plus exact `review_subject` and `review_evidence` pointers.

## 6. Readiness

A Task Board card becomes `ready` only when:
- dependencies needed to start are `done`;
- required authoritative inputs exist;
- acceptance is testable enough to execute;
- no known unresolved strategic or explicit authorization blocker exists.

Do **not** keep a fixed-policy card unready merely because some future capability may or may not be available. Runtime capability is discovered by executing the concrete operation.

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
- Task Board, milestone-wide handoff/acceptance/review state and shared integration bookkeeping are coordinator-owned and never lane-worker write scope;
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
- required tests/checks, evidence/readback obligations and review requirements;
- when parallel, exact lane base plus current `write_scope`/`exclusive_resources` assumptions.

Refresh Gate is a **state/contract drift gate**. Under fixed policies it is not a capability inventory/checklist.

Implementation-detail drift within approved contracts may be reconciled by the current executor. Material behavior/architecture/requirement/external-contract/milestone-acceptance drift blocks the card and requires strategic resolution.

Under `mixed`, unavailable required capabilities may affect pre-assignment routing through Capability Gate. Under fixed policies, capability problems are runtime blockers only when a concrete required operation cannot proceed.

## 9. Independent review contract

When review is REQUIRED or RECOMMENDED, the Task Card/milestone contract states that requirement but mutable review progress lives in Task Board.

- `chatgpt_only`: the ChatGPT chat that implemented the subject must stop before independent verdict; a fresh normal ChatGPT chat performs review from exact durable `review_subject`.
- `codex_only`: Codex Main obtains an independent reviewer worker/session; installed `codex_workflow` governs internal reviewer orchestration.
- `mixed`: reviewer must be independent of implementing worker/session according to accepted review path.

OPTIONAL review does not create a mandatory review gate unless explicitly activated.

## 10. Definition of Done contract

A Task Board card may be marked `done` only when all applicable items hold:
1. included scope complete and excluded scope not silently expanded;
2. acceptance satisfied;
3. required tests/checks ran;
4. checks green or authorized baseline exception exists;
5. relevant OpenSpec requirements satisfied;
6. required/recommended independent review is GREEN when applicable;
7. no hidden blocker remains;
8. accepted result exists in durable Git/external state;
9. Task Board state/result pointers reconciled;
10. assigned executor and result commit recorded in Task Board;
11. result PR recorded when applicable, otherwise `null`;
12. Task Board `tests_summary` and, when required, standalone durable evidence identify exact checks/review;
13. relevant external side effects/idempotency/reconciliation/readback verified where required;
14. when parallel, the accepted lane result has been integrated and required post-integration checks are green;
15. no unassigned TODO remains inside accepted scope.

`done` is verified state, not an agent assertion. The Task Card file itself is not edited merely to mark these checks complete.

## 11. Result state

At close persist mutable result state in Task Board:

```yaml
execution_status: done
executor: chatgpt | codex
result_commit: <sha>
result_pr: <number-or-null>
evidence: <repo-relative-path-or-null>
tests_summary: <concise exact summary or evidence pointer>
```

For a parallel lane, the durable result record identifies the exact lane base/branch or equivalent isolated workspace and integrated verification target.

A standalone evidence file is optional for a simple reproducible card. It is expected for integrated milestone acceptance, required/recommended independent review, baseline exceptions, material external writes/readback, complex multi-stage verification, or when a contract explicitly requires it.

## 12. Dependency and parallel-set handling

Completion may unblock dependent cards. A generic DAG engine is unnecessary: explicit `depends_on`, Task Board state and bounded-parallel ownership rules are sufficient.

For `serial`, select one deterministic READY card.

For `bounded_parallel`, select a deterministic set of READY cards up to `parallel_card_limit` such that every selected card is `parallel_safe` and pairwise compatible by `write_scope` and `exclusive_resources`.

## 13. Near-term versus distant cards

Near-term cards may contain detailed implementation expectations. Distant cards stay functionally precise without freezing interfaces that do not yet exist. Refresh Gate is mandatory before execution. Detail may be deferred, but accepted planner intent must remain reachable through exact authority refs; do not replace richer durable authority with a thinner card summary.

## 14. Scope discipline

The current executor implements only bounded card scope unless a necessary adjacent change is clearly within the same acceptance contract and documented, a new bounded corrective/dependency card is created, or strategic authority explicitly changes the plan.

Do not hide unrelated cleanup or architecture changes inside a card.
