# GitHub State Contract

This is the normative contract for durable execution state in a project repository, independent of whether the active executor is ChatGPT or Codex.

## 1. Single live-state authority

`implementation/TASK_BOARD.yaml` is the **sole authoritative mutable execution-state record**.

Milestone files and Task Card files are stable scope/acceptance contracts. `PROJECT.md` is a high-level router. Handoffs summarize completed truth. None of them mirror live status/executor/result/branch state.

If a legacy project still contains duplicated status/result fields in old milestone/Card files, Task Board controls new execution state after adoption of current workflow; legacy duplicate fields are historical/non-authoritative.

## 2. Card execution states

Allowed Task Board card `execution_status` values:

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

## 3. Milestone execution lifecycle

Normal Task Board milestone lifecycle:

```text
planned → ready → in_progress → done
```

`blocked` is allowed for an unresolved milestone gate/blocker. `superseded` requires an explicit decision.

A milestone that passed its GREEN acceptance gate must not remain `ready` or `in_progress`.

## 4. Task Board minimum state

Task Board should identify at least:
- project and plan revision/reference;
- current milestone;
- project execution mode: `serial` or `bounded_parallel`;
- `parallel_card_limit` when bounded parallelism is enabled;
- milestone decision/execution states and terminal checkpoint/result pointers;
- card decision/execution states, dependencies and assigned executor when applicable;
- per-card parallel metadata when used: `parallel_safe`, `write_scope`, `exclusive_resources`, active lane branch/workspace and exact lane base;
- card result pointers, evidence and concise tests summary;
- relevant OpenSpec change per card when applicable;
- integration branch/PR/head information needed to recover in-flight work;
- strategic control-chat identity only when that optional Codex communication mechanism is configured.

Serial remains the default when execution mode is omitted in a legacy project.

## 5. Executor assignment

Read project `execution_policy` from `PROJECT.md`.

- `chatgpt_only` → assign ChatGPT directly. Do not run Capability Gate.
- `codex_only` → assign Codex directly. Do not run Capability Gate.
- `mixed` → normal ChatGPT runs `workflow/chatgpt/CAPABILITY_GATE.md` before assignment.

Project routing assumes `ChatGPT capabilities ⊆ Codex capabilities`.

Assignment is persisted only in Task Board. Policy never changes automatically because of a blocker.

## 6. Starting cards

### Serial

When serial execution begins:
- Task Board card `ready → in_progress`;
- record `executor: chatgpt | codex` in Task Board;
- milestone `ready → in_progress` when this is its first real started card;
- update `execution_ref` as needed;
- persist Refresh Gate evidence only when the gate discovers something material.

Do not edit the Task Card contract merely to reflect this transition.

### Bounded parallel

Before relying on concurrent mutable execution, the coordinator must durably establish the selected execution set in Task Board:
- every selected card is `ready`, dependency-complete and explicitly `parallel_safe`;
- selected cards fit within `parallel_card_limit`;
- selected cards have pairwise non-overlapping mutable `write_scope` and no shared `exclusive_resources`;
- selected cards transition to `in_progress` and record executor;
- one exact integration base is recorded;
- each mutable card has its own lane branch/worktree or equivalent isolated mutable workspace derived from that base;
- coordinator-owned global execution files are outside lane-worker write scope.

The durable start transition should be committed/pushed on the integration branch before workers rely on it for recovery.

## 7. Coordinator-owned state

While parallel lanes are active, only the project-level coordinator updates shared execution state, including:
- Task Board;
- milestone-wide checkpoint/handoff/acceptance pointers;
- integration-base and lane pointers;
- deterministic integration order;
- cross-lane corrective state.

A lane worker may write implementation, tests and card-scoped evidence within its owned scope, but must not independently race edits to Task Board or milestone-wide integration bookkeeping.

When Codex with `codex_workflow` is used, Codex Main is coordinator and internal workers may own individual Task Card lanes. Worker completion does not itself change Task Board card state to `done`.

## 8. Parallel lane integration

Before marking a parallel card `done`:
1. confirm lane/base identity or reconcile documented drift;
2. integrate the accepted lane result into intended milestone state;
3. resolve conflict explicitly rather than weakening ownership assumptions;
4. run required post-integration checks or equivalent proof;
5. persist final result/evidence pointers in Task Board.

Unexpected write-scope conflict means the affected lanes were not safely independent. Pause/serialize/re-scope them.

## 9. Done-card result pointer contract

Before a Task Board card is terminal `done`, record:

```yaml
execution_status: done
executor: chatgpt | codex
result_commit: <sha>
result_pr: <number-or-null>
evidence: <repo-relative-path>
tests_summary: <concise summary or evidence pointer>
```

Rules:
- `result_commit` identifies the commit containing or verifiably representing the accepted result;
- `result_pr` identifies the PR when applicable, otherwise `null`;
- evidence names exact tests/review/checks; `tests passed` alone is insufficient;
- for a parallel lane, evidence identifies lane base/workspace and integrated verification target;
- for material external writes, evidence records target, readback method and verified persisted state.

The Task Card contract is not edited to duplicate these result fields.

## 10. Blocked card

When execution is blocked:
- Task Board card `execution_status: blocked`;
- write durable blocker evidence under `implementation/blockers/` when material;
- make a safe commit/push before messaging when possible;
- do not start dependent cards.

Capability routing and runtime capability failure are different stages:
- under `mixed`, Capability Gate is used only **before assignment**;
- under `chatgpt_only`/`codex_only`, there is no routing gate;
- **after assignment/start**, a newly discovered missing capability is a runtime blocker, not an automatic executor-routing event.

For a runtime capability blocker, record the exact missing capability, surface `USER ACTION REQUIRED`, and resume the same card with the same executor after capability is provided.

If assigned executor is Codex, do not fall back to ChatGPT. Under the capability invariant, a required capability absent from Codex is not an executor fallback opportunity.

If assigned executor is ChatGPT under `chatgpt_only`, remain blocked until capability is supplied or the user explicitly changes policy.

For a strategic/product/architecture blocker, obtain the relevant authority decision and persist it under `decisions/`. When Codex uses a correlated ChatGPT control channel, follow `workflow/codex/HANDOFF.md`.

## 11. Milestone GREEN

A milestone is not done merely because all required cards are done.

After integrated milestone acceptance is GREEN:
1. finalize publication/merge according to project branch policy;
2. write/reconcile cumulative handoff;
3. write acceptance evidence;
4. record exact final `implementation_head` and checkpoint/tag when applicable;
5. set Task Board milestone `execution_status: done`;
6. ensure every required card is `done` with result pointers.

A done Task Board milestone stores at minimum:

```yaml
execution_status: done
checkpoint: <checkpoint-or-tag>
implementation_head: <sha>
handoff: project-handoffs/MXX_HANDOFF.md
acceptance_evidence: implementation/evidence/MXX_ACCEPTANCE.md
```

Do not mirror those terminal pointers back into the milestone contract file merely for state synchronization.

## 12. Automatic next-milestone continuation

A GREEN milestone does not by itself require a user/router stop.

Under `chatgpt_only` or `codex_only`, the fixed executor may continue automatically into the next milestone when:
- it is already accepted in the approved Master Plan;
- its prerequisites are satisfied by the GREEN checkpoint;
- deterministic execution preparation can be performed from durable authority;
- no explicit user/deployment/authorization gate is due;
- no unresolved strategic decision exists.

The coordinator updates Task Board to the next milestone, performs any allowed just-in-time execution preparation, runs fresh Refresh Gates, and continues. No Capability Gate is run.

Under `mixed`, the next new execution assignment returns to ChatGPT routing and Capability Gate.

An explicit deployment/live-write approval remains a hard stop regardless of execution policy.

## 13. Corrective work

If integrated milestone acceptance is RED:
- do not mark milestone done;
- reopen the appropriate Task Board card or create a bounded corrective card/contract;
- record failing evidence;
- preserve dependencies, execution policy and strategic escalation rules.

## 14. Cumulative handoff and recovery

`project-handoffs/MXX_HANDOFF.md` is the canonical summary for a completed milestone, but Task Board remains the live execution-state authority.

Fresh-session recovery uses:
- `PROJECT.md` for high-level routing/policy;
- exact integration branch/HEAD/runtime state;
- Task Board;
- milestone/Card contracts referenced by active state;
- latest handoff;
- relevant OpenSpec/evidence/result pointers.

A local `current.md` is optional convenience only.

## 15. Consistency invariants

Invalid states include:
- Task Board card `done` with missing required executor/result/evidence pointers;
- Task Board milestone `done` with missing checkpoint, implementation head, handoff or acceptance evidence;
- all required cards `done` while a GREEN milestone remains `ready`/`in_progress`;
- a dependent card `in_progress` while a required dependency is not `done`;
- more concurrently active cards than `parallel_card_limit`;
- concurrently active cards with overlapping mutable `write_scope` or shared `exclusive_resource`;
- a mutable parallel card with no recoverable lane/base pointer;
- lane workers racing coordinator-owned Task Board/global integration state;
- durable execution state existing only in chat, `PROJECT.md`, milestone/Card files or local `current.md`;
- claimed external success contradicted by required readback evidence;
- fixed-policy execution invoking Capability Gate;
- execution policy changing without explicit user decision;
- a runtime capability blocker being silently rerouted instead of remaining blocked for the assigned executor.
