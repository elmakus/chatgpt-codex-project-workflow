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
- project execution mode: `serial` or `bounded_parallel`;
- `parallel_card_limit` when bounded parallelism is enabled;
- card states, dependencies and active executor when applicable;
- per-card parallel metadata when used: `parallel_safe`, `write_scope`, `exclusive_resources`, active lane branch/workspace and exact lane base;
- result pointers;
- relevant OpenSpec change;
- integration branch/PR/head information needed to recover in-flight work;
- strategic control-chat identity only when that optional Codex communication mechanism is configured.

Serial remains the default when execution mode is omitted in a legacy project.

## 4. Starting cards

### Serial

When serial execution begins:
- Task Board card `ready → in_progress`;
- card file `Execution status: IN_PROGRESS`;
- record `executor: chatgpt | codex` in card and Task Board;
- milestone `ready → in_progress` when this is its first real started card;
- persist a Refresh Gate note/evidence only when the gate discovers something material.

### Bounded parallel

Before relying on concurrent mutable execution, the coordinator must durably establish the selected execution set:
- every selected card is `ready`, has all dependencies `done` and is explicitly `parallel_safe`;
- selected cards fit within `parallel_card_limit`;
- selected cards have pairwise non-overlapping mutable `write_scope` and no shared `exclusive_resources`;
- Task Board/card state transitions the whole selected set to `in_progress` and records `executor`;
- one exact integration base is recorded;
- each mutable card has its own lane branch/worktree or equivalent isolated mutable workspace derived from that base;
- coordinator-owned global execution files are outside lane worker write scope.

The durable start transition should be committed/pushed on the integration branch before workers rely on it for recovery.

Read-only lanes may share the same immutable repository snapshot if they do not share a mutable worktree/index.

## 5. Coordinator-owned state

While parallel lanes are active, only the project-level coordinator updates shared execution state, including:
- Task Board;
- milestone-wide status/checkpoint/handoff/acceptance bookkeeping;
- integration-base and lane pointers;
- deterministic integration order;
- cross-lane corrective state.

A lane worker may write implementation, tests and card-scoped evidence within its owned scope, but must not independently race edits to coordinator-owned global state.

When Codex with `codex_workflow` is used, Codex Main is the coordinator and internal workers may own individual Task Card lanes. Worker completion does not itself change project Task Card state to `done`.

## 6. Parallel lane integration

A completed mutable lane is integrated into the intended milestone/integration branch one lane at a time.

Before marking its card `done`:
1. confirm the lane started from the recorded base or reconcile documented drift;
2. integrate the accepted lane result;
3. resolve any conflict explicitly rather than weakening ownership assumptions;
4. run required post-integration checks or equivalent proof that card acceptance remains valid in integrated state;
5. persist final result/evidence pointers and coordinator state.

An unexpected write-scope conflict means the affected lanes were not safely independent. Pause/serialize/re-scope them; do not allow both writers to continue racing.

## 7. Done-card result pointer contract

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
- `result_commit` identifies the commit containing or verifiably representing the accepted result;
- `result_pr` identifies the PR when applicable. If no PR applies, use `null` and project branch policy must make publication path unambiguous;
- evidence points to durable test/review evidence or an unambiguous cumulative evidence section;
- evidence names exact tests/review/checks; `tests passed` alone is insufficient;
- for a parallel lane, evidence identifies the lane base/branch or equivalent isolated workspace and the integrated target state used for final verification;
- when material external writes require readback under `workflow/EXECUTION.md`, evidence records the target, readback method and verified resulting state.

## 8. Definition of Done state coupling

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
- parallel lane integration/post-integration verification is complete when applicable;
- no unassigned TODO remains inside accepted scope.

## 9. Blocked card

When execution is blocked:
- card `execution_status: blocked`;
- write durable evidence under `implementation/blockers/` when material;
- make a safe commit/push before messaging when possible;
- do not start dependent cards.

In bounded-parallel mode, an unrelated compatible lane may continue only when the blocker does not change its dependencies, ownership, external resources, requirements or acceptance assumptions.

Capability routing and runtime capability failure are different stages:

- **Before assignment**, normal ChatGPT may use `workflow/chatgpt/CAPABILITY_GATE.md` to choose ChatGPT, Codex, or BLOCKED according to project `execution_policy`.
- **After assignment/execution start**, a newly discovered missing capability is a runtime blocker, not an automatic executor-routing event.

For a runtime capability blocker, record the exact missing MCP/access/credential/runtime/tool/test/readback/evidence capability, surface `USER ACTION REQUIRED`, and resume the **same card with the same executor** after the user provides it.

If the assigned executor is Codex, do not re-apply the ChatGPT Capability Gate and do not fall back to ChatGPT. Project routing assumes `ChatGPT capabilities ⊆ Codex capabilities`; therefore a required capability absent from Codex is not available from ChatGPT as an executor fallback.

Under `chatgpt_only`, a ChatGPT runtime capability failure likewise remains blocked until the user provides the missing capability or explicitly changes project policy; policy never changes automatically.

For a strategic/product/architecture blocker, obtain the relevant authority decision and persist an accepted decision record under `decisions/`. When Codex uses a correlated ChatGPT control-chat exchange, follow `workflow/codex/HANDOFF.md` including matching `request_id` and `DECISION FOR CODEX:`.

Resume only after the blocker is actually resolved and Task Card/OpenSpec/plan/Task Board are reconciled as required.

## 10. Milestone GREEN

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

## 11. Corrective work

If integrated milestone acceptance is RED:
- do not mark the milestone done;
- reopen the appropriate card or create a bounded corrective card;
- record failing evidence;
- preserve dependencies, capability gates and strategic escalation rules.

A cross-lane integration defect is assigned to the narrowest owning card(s). Ordinary repair returns to the owning executor and then to the required independent reviewer; do not hide it in milestone acceptance.

## 12. Cumulative handoff and recovery

`project-handoffs/MXX_HANDOFF.md` is the canonical cumulative handoff for the completed milestone.

Fresh-session recovery also uses:
- exact integration branch/HEAD;
- Task Board;
- current milestone and every active card;
- recorded executor for each in-flight card;
- recorded lane branch/base/workspace pointers when parallel;
- relevant OpenSpec;
- evidence/result pointers.

A local `current.md` is optional convenience only and cannot be required for recovery.

## 13. Repository topology changes

Do not change project repository ownership/layout in the middle of an active milestone. Legacy split-repository migration occurs only at a green milestone boundary and follows `PROJECT_REPOSITORY.md`.

Creating temporary bounded lane branches/worktrees inside the same repository for approved parallel execution is execution state, not a repository-topology migration.

## 14. Consistency invariants

Invalid states include:
- card `done` with missing required result pointers or executor provenance;
- milestone `done` with missing checkpoint, `implementation_head`, handoff or acceptance evidence;
- all required cards `done` while a green milestone remains `ready`;
- a dependent card `in_progress` while a required dependency is not `done`;
- more concurrently active parallel cards than `parallel_card_limit`;
- concurrently active cards with overlapping mutable `write_scope` or a shared `exclusive_resource`;
- a mutable parallel card with no recoverable lane/base pointer;
- lane workers racing coordinator-owned Task Board/global milestone state;
- durable state existing only in chat or local `current.md`;
- Task Board/card disagreement left unreconciled at a durable checkpoint;
- claimed external success when required readback/verification evidence shows a different persisted state;
- a Codex runtime capability blocker being rerouted to ChatGPT instead of remaining blocked for user-provided capability.
