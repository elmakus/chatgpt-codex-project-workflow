# Shared Execution Core

This module defines project execution semantics shared by ChatGPT and Codex.

The selected executor also reads its thin adapter:
- ChatGPT → `workflow/chatgpt/EXECUTION.md`;
- Codex → `workflow/codex/EXECUTION.md`.

Read applicable `GITHUB_STATE.md`, `TASK_CARDS.md`, `OPENSPEC.md` and project `PROJECT.md`.

## State authority

`implementation/TASK_BOARD.yaml` is the sole live execution-state authority. Milestone/Card files are contracts; evidence/handoffs prove or summarize results; `PROJECT.md` is high-level routing only.

Do not create synchronization commits whose only purpose is copying live status/result fields into milestone/Card/PROJECT files.

## Execution-set loop

Project execution is serial unless Task Board explicitly opts into `execution_mode: bounded_parallel`.

1. Establish repository root, intended integration branch, exact HEAD, working-tree state and relevant external/runtime baseline.
2. Read project execution policy and Task Board; recover every valid `in_progress` or `blocked` card and lane/base pointer.
3. Read the contracts for current milestone and candidate Task Cards plus relevant OpenSpec/requirements/decisions.
4. Determine READY cards whose dependencies are `done`; never select `planned`, `blocked`, `done` or `superseded`.
5. Build the next execution set:
   - `serial` → choose the first deterministic READY card;
   - `bounded_parallel` → choose up to `parallel_card_limit` READY cards explicitly `parallel_safe` and pairwise non-conflicting by `write_scope`/`exclusive_resources`.
6. Determine executor:
   - `chatgpt_only` → ChatGPT, no Capability Gate;
   - `codex_only` → Codex, no Capability Gate;
   - `mixed` → use the prior ChatGPT Capability Gate assignment for this set.
7. Before work relies on the selection, persist coordinator-owned Task Board transitions for the whole set: executor, `in_progress`, exact integration base and lane/workspace pointers. Transition Task Board milestone to `in_progress` when this is its first real execution.
8. Run Refresh Gate independently for each selected card against the same durable integration base plus completed dependencies.
9. Create/reconcile OpenSpec just-in-time if required.
10. Execute only bounded card scope. Mutable parallel cards use isolated lane branches/worktrees or equivalent isolated workspace.
11. Run required tests/checks and verify card acceptance plus relevant OpenSpec behavior in each lane.
12. For material external mutations, perform required readback/verification. External mutable targets named as exclusive resources remain serialized.
13. Integrate completed parallel lanes into intended milestone branch one at a time; reconcile conflicts explicitly.
14. After integration, run required post-integration checks or equivalent proof. Only then persist result/evidence/result pointers in Task Board and mark card `done`.
15. Commit/push durable coordinator state, unblock newly eligible dependent cards and refill available parallel slots deterministically when safe.
16. Continue automatically while project policy, executor/session capacity and Task Board provide an unambiguous safe execution set. Do not ask the user to choose among equivalent runnable cards.
17. After required cards are done, run integrated milestone acceptance on intended final milestone state.
18. RED → reopen/create corrective work. GREEN → milestone close/handoff under `workflow/REVIEW_AND_HANDOFF.md`.
19. After GREEN, apply next-milestone continuation rules below.

Bounded parallelism is opportunistic, not a utilization target. Run fewer lanes when uncertainty, integration risk, shared fixtures or ownership ambiguity make that safer.

## Coordinator and lane ownership

The project-level coordinator owns shared execution state while parallel lanes are active. At minimum this includes Task Board, milestone-wide handoff/acceptance pointers, lane/base bookkeeping and integration ordering.

A lane owns only bounded implementation/evidence scope. It must not independently rewrite Task Board or shared integration bookkeeping.

When Codex is executor and `codex_workflow` is installed, Codex Main is project-level coordinator; internal workers may own individual Task Card lanes under `workflow/codex/CODEX_ORCHESTRATION.md`.

Parallel worker completion is not card completion. Card completion occurs only after coordinator integration, required post-integration verification and durable Task Board result pointers.

## Next-milestone continuation

A GREEN milestone is a checkpoint, not automatically a stop.

### Fixed policy: `chatgpt_only` or `codex_only`

The same fixed executor may continue automatically into the next milestone when all are true:
- next milestone is already accepted in approved Master Plan;
- preceding GREEN checkpoint satisfies its declared dependencies;
- no explicit user/deployment/live-write/authorization gate is due;
- no strategic requirement/architecture/product decision is unresolved;
- just-in-time execution prep can be derived from durable authority;
- fresh Refresh Gate/evidence path can be satisfied.

The coordinator may perform allowed next-milestone execution prep, update Task Board to the new milestone and continue. Do **not** run Capability Gate merely because milestone ID changed.

Under `codex_only`, this permits Codex Main to execute an approved M01→M02→… sequence without returning to ChatGPT after every GREEN checkpoint. Strategic/user gates still stop dependent work.

### `mixed`

A new execution assignment is routed by normal ChatGPT through Capability Gate. Previous executor is not automatically inherited.

If current executor is Codex, persist GREEN/handoff/Task Board and return routing control to ChatGPT. If current executor is ChatGPT, it may run the gate inline.

## User-visible continuation status

Execution checkpoints must not make it ambiguous whether work continues or needs user action.

Use an explicit state:
- `NEXT ACTION: continuing automatically with <card/set/milestone>; no user action required.`
- `USER ACTION REQUIRED: <smallest concrete decision/authorization/input>.`
- `SESSION HANDOFF RECOMMENDED: <reason>. NEXT ACTION: start a fresh <ChatGPT chat|Codex session> from <durable pointer>.`
- `MILESTONE COMPLETE: <checkpoint>. CONTINUING TO: <next milestone>` when fixed-policy continuation is valid.
- `MILESTONE COMPLETE: <checkpoint>.` when execution stops at that boundary.

A routine GREEN card is not itself a reason to stop. One parallel lane finishing is not a reason to stop unrelated healthy lanes.

## Refresh Gate

Before implementation compare at minimum:
- actual integration branch/HEAD and relevant runtime/external state;
- exact lane base/workspace when parallel;
- Task Board current milestone/card/set and execution pointers;
- latest cumulative handoff;
- relevant Master Plan/milestone/Card contracts/accepted decisions/requirements;
- current relevant OpenSpec;
- completed dependencies;
- actual code/runtime interfaces;
- capabilities, tests/checks and evidence/readback needed to satisfy the card;
- recorded `write_scope`/`exclusive_resources` assumptions when parallel.

If mismatch is a local implementation detail within approved behavior/architecture/requirements, reconcile it within executor authority.

If evidence materially changes behavior, architecture, frozen decision, requirement, external contract or milestone acceptance, do not implement stale contract. Persist evidence, set affected Task Board card `blocked` and use strategic resolution.

If a parallel lane discovers unexpected mutable overlap, pause affected ownership boundary and let coordinator serialize/re-scope it.

## Capability boundary

Project routing assumes:

`ChatGPT capabilities ⊆ Codex capabilities`

Capability Gate exists only for `mixed` pre-assignment routing.

Under `chatgpt_only` and `codex_only`, executor is fixed by policy and no Capability Gate is run. Capability availability is still verified during preparation/Refresh Gate/runtime because a fixed executor must not pretend a missing capability exists.

After a card starts, if required environment access, MCP, credential, runtime/tool, test path, external write/readback or evidence capability is unavailable:
- stop affected work safely;
- persist exact missing capability and available evidence;
- set affected Task Board card `blocked` when its contract cannot be met;
- report `USER ACTION REQUIRED` with smallest concrete capability/access/configuration needed;
- resume same card with same executor after capability is provided and durable state reconciled.

Do not automatically change executor or execution policy after runtime capability failure.

## External write contract

For material mutation of GitHub, Liftosaur, APIs, calendars, Drive, configuration or another external system:

```text
WRITE → READBACK → VERIFY EXPECTED STATE → EVIDENCE
```

Use readback when it provides meaningful independent confirmation of persisted state. Do not invent verification where meaningful readback does not exist.

An explicit deployment/live-write authorization gate always overrides automatic continuation.

## Strategic blocker handling

A strategic blocker is not a routine executor-routing problem. Persist exact evidence and stop dependent work when a product/behavior/architecture/frozen-requirement/external-contract/acceptance decision exceeds current executor authority.

ChatGPT may resolve strategic questions with the user/accepted governance authority and persist the accepted decision.

When Codex uses a configured correlated ChatGPT control channel, `workflow/codex/HANDOFF.md` defines the `request_id`/`DECISION FOR CODEX:` protocol.

## Failure recovery

If a session ends unexpectedly:
- recover every existing `in_progress`/`blocked` card from Task Board;
- inspect integration branch/HEAD plus recorded lane workspaces and relevant external/runtime state;
- inspect relevant OpenSpec/tests/evidence/result pointers;
- use local `current.md` only as a hint;
- continue each recoverable card with same assigned executor unless durable state proves completion/supersession or explicit user decision changes policy/assignment.

Recovery must be possible from durable repository state without prior chat.
