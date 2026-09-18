# GitHub State Contract

This is the normative contract for durable execution state in a project repository, independent of whether the active executor is ChatGPT or Codex.

## 1. Single live-state authority

`implementation/TASK_BOARD.yaml` is the **sole authoritative mutable execution-state record**.

The approved Master Plan milestone subsection is the default stable milestone contract; an optional `implementation/milestones/MXX.md` may extend it just-in-time. Task Card files are stable bounded authority/scope/acceptance contracts. `PROJECT.md` is a high-level router. Handoffs summarize completed truth. None of them mirror live status/executor/result/branch state.

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
- card result pointers and concise tests summary, plus standalone evidence pointer when materially required;
- relevant OpenSpec change per card when applicable;
- integration branch/PR/head information needed to recover in-flight work;
- review-state pointers when a card/milestone independent-review gate is active;
- strategic control-chat identity only when that optional Codex communication mechanism is configured.

Serial remains the default when execution mode is omitted in a legacy project.

### Review-state fields

When independent review is active for a card or milestone, Task Board records:

```yaml
review_state: pending | in_progress | green | red
review_subject: <exact sha/subject>
review_evidence: <repo-relative-path-or-null>
```

Omit/null these fields when no review gate is active.

`review_subject` is immutable for one review attempt. If corrective work changes the subject, create/update the next review attempt against the new exact subject rather than silently reusing the old verdict.

## 5. Executor assignment

Read project `execution_policy` from `PROJECT.md`.

- `chatgpt_only` → assign ChatGPT directly. Do not run Capability Gate or capability preflight.
- `codex_only` → assign Codex directly. Do not run Capability Gate or capability preflight.
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
- milestone-wide checkpoint/handoff/acceptance/review pointers;
- integration-base and lane pointers;
- deterministic integration order;
- cross-lane corrective state.

A lane worker may write implementation, tests and card-scoped evidence within its owned scope, but must not independently race edits to Task Board or milestone-wide integration bookkeeping.

When Codex with `codex_workflow` is used, Codex Main is coordinator and internal workers/reviewers may own individual Task Card/review lanes. Worker completion does not itself change Task Board card state to `done` or review state to accepted milestone truth; Main integrates the result.

## 8. Parallel lane integration

Before marking a parallel card `done`:
1. confirm lane/base identity or reconcile documented drift;
2. integrate the accepted lane result into intended milestone state;
3. resolve conflict explicitly rather than weakening ownership assumptions;
4. run required post-integration checks or equivalent proof;
5. persist final result/evidence pointers in Task Board.

Unexpected write-scope conflict means the affected lanes were not safely independent. Pause/serialize/re-scope them.

## 9. Independent-review lifecycle

When a REQUIRED/RECOMMENDED review gate is reached:

1. freeze the exact `review_subject` and implementation/test evidence;
2. set `review_state: pending` in Task Board;
3. persist durable state before the independent verdict;
4. independent reviewer sets `review_state: in_progress` when review begins;
5. reviewer persists GREEN/RED evidence and coordinator sets `review_state: green | red` plus `review_evidence`.

Policy-specific behavior:
- `chatgpt_only` → the implementing ChatGPT chat must stop at `pending`; the user opens a **fresh normal ChatGPT chat** to perform the independent review. The implementing chat must not issue the verdict on its own subject.
- `codex_only` → Codex Main obtains a reviewer worker/session independent of the implementing worker. When installed/enabled, `codex_workflow` governs internal review orchestration; no user handoff is required solely for reviewer independence.
- `mixed` → use an independent reviewer path appropriate to the accepted review contract.

A GREEN review may unblock milestone acceptance/continuation. A RED review creates/reopens bounded corrective work; a changed subject requires a new review attempt.

## 10. Done-card result pointer contract

Before a Task Board card is terminal `done`, record:

```yaml
execution_status: done
executor: chatgpt | codex
result_commit: <sha>
result_pr: <number-or-null>
evidence: <repo-relative-path-or-null>
tests_summary: <concise exact summary or evidence pointer>
```

Rules:
- `result_commit` identifies the commit containing or verifiably representing the accepted result;
- `result_pr` identifies the PR when applicable, otherwise `null`;
- `tests_summary` names exact tests/review/checks; `tests passed` alone is insufficient;
- standalone evidence may be `null` for a simple reproducible card;
- standalone evidence is expected for integrated milestone acceptance, REQUIRED/RECOMMENDED independent review, baseline/authorized exceptions, material external writes/readback, complex multi-stage verification, or an explicit contract requirement;
- for a parallel lane, the durable result record identifies lane base/workspace and integrated verification target;
- for material external writes, standalone evidence records target, readback method and verified persisted state.

The Task Card contract is not edited to duplicate these result fields.

## 11. Capability and blocked-card semantics

When execution is blocked:
- Task Board card `execution_status: blocked`;
- write durable blocker evidence under `implementation/blockers/` when material;
- make a safe commit/push before messaging when possible;
- do not start dependent cards.

Capability routing and runtime capability failure are different stages:
- under `mixed`, Capability Gate is used only **before assignment**;
- under `chatgpt_only`/`codex_only`, there is no routing gate and **no capability preflight/inventory**;
- fixed-policy execution starts directly after state/contract Refresh Gate;
- a capability becomes a workflow blocker only when a concrete required operation cannot proceed.

For a runtime capability blocker, record the exact missing capability/access and surface `USER ACTION REQUIRED` with the smallest concrete remedy.

Codex should self-remediate ordinary non-secret local tooling/dependency gaps when the environment allows and accepted security/reproducibility constraints permit it. User-provided MCP/credential/token/account permission/privileged access becomes a blocker when actually needed and unavailable.

If the user supplies the missing capability, resume the same card. If the user explicitly changes `execution_policy`, reconcile Task Board and reassign the blocked card under the new policy. Do not reroute or mutate policy automatically.

For a strategic/product/architecture blocker, obtain the relevant authority decision and persist it under `decisions/`. When Codex uses a correlated ChatGPT control channel, follow `workflow/codex/HANDOFF.md`.

## 12. Milestone GREEN

A milestone is not done merely because all required cards are done.

After integrated milestone acceptance is GREEN:
1. finalize publication/merge according to project branch policy;
2. write/reconcile cumulative handoff;
3. write acceptance evidence;
4. record exact final `implementation_head` and checkpoint/tag when applicable;
5. set Task Board milestone `execution_status: done`;
6. ensure every required card is `done` with result pointers;
7. ensure every required/recommended independent-review gate for the accepted subject is `green`.

A done Task Board milestone stores at minimum:

```yaml
execution_status: done
checkpoint: <checkpoint-or-tag>
implementation_head: <sha>
handoff: project-handoffs/MXX_HANDOFF.md
acceptance_evidence: implementation/evidence/MXX_ACCEPTANCE.md
```

Do not mirror those terminal pointers back into the milestone contract file merely for state synchronization.

## 13. Automatic next-milestone continuation

A GREEN milestone does not by itself require a user/router stop.

Under `chatgpt_only` or `codex_only`, the fixed executor may continue automatically into the next milestone when:
- it is already accepted in the approved Master Plan;
- its prerequisites are satisfied by the GREEN checkpoint;
- every required/recommended review gate for the completed subject is `green`;
- deterministic execution preparation can be performed from durable authority;
- no explicit user/deployment/authorization gate is due;
- no unresolved strategic decision exists.

The coordinator updates Task Board to the next milestone, performs allowed just-in-time execution preparation, runs fresh state/contract Refresh Gates and continues. No Capability Gate or fixed-policy capability preflight is run.

Under `chatgpt_only`, if the current chat implemented the subject and review is required/recommended, the current chat stops at `review_state: pending`; continuation resumes in the fresh review chat after GREEN.

Under `codex_only`, Codex Main may orchestrate independent reviewer workers under installed `codex_workflow` and continue without a user handoff solely for review.

Under `mixed`, the next new execution assignment returns to ChatGPT routing and Capability Gate.

An explicit deployment/live-write approval remains a hard stop regardless of execution policy.

## 14. Corrective work

If integrated milestone acceptance or independent review is RED:
- do not mark milestone done;
- reopen the appropriate Task Board card or create a bounded corrective card/contract;
- record failing evidence;
- preserve dependencies, execution policy and strategic escalation rules;
- after corrective work changes the subject, run a fresh independent review when still required/recommended.

## 15. Cumulative handoff and recovery

`project-handoffs/MXX_HANDOFF.md` is the canonical summary for a completed milestone, but Task Board remains the live execution-state authority.

Fresh-session recovery uses:
- `PROJECT.md` for high-level routing/policy;
- exact integration branch/HEAD/runtime state;
- Task Board including review state;
- current milestone contract referenced by Task Board (Master Plan subsection or optional JIT extension) and active Task Card contracts;
- latest handoff;
- relevant OpenSpec/evidence/result/review pointers.

A local `current.md` is optional convenience only.

## 16. Consistency invariants

Invalid states include:
- Task Board card `done` with missing required executor/result/tests summary or a missing standalone evidence pointer when that evidence is required;
- Task Board milestone `done` with missing checkpoint, implementation head, handoff or acceptance evidence;
- Task Board milestone `done` while a required/recommended review gate for the accepted subject is `pending`, `in_progress` or `red`;
- a `green` review whose `review_subject` does not match the accepted subject it claims to review;
- all required cards `done` while a GREEN milestone remains `ready`/`in_progress`;
- a dependent card `in_progress` while a required dependency is not `done`;
- more concurrently active cards than `parallel_card_limit`;
- concurrently active cards with overlapping mutable `write_scope` or shared `exclusive_resource`;
- a mutable parallel card with no recoverable lane/base pointer;
- lane workers racing coordinator-owned Task Board/global integration state;
- durable execution state existing only in chat, `PROJECT.md`, milestone/Card files or local `current.md`;
- claimed external success contradicted by required readback evidence;
- fixed-policy execution invoking Capability Gate or capability preflight/inventory;
- execution policy changing without explicit user decision;
- a runtime capability blocker being silently rerouted instead of being resolved or explicitly reassigned after user policy change;
- a `chatgpt_only` implementing chat issuing its own REQUIRED/RECOMMENDED independent-review verdict.
