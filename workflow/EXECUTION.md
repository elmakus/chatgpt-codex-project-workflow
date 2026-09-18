# Shared Execution Core

This module defines project execution semantics shared by ChatGPT and Codex.

The selected executor also reads its thin adapter:
- ChatGPT → `workflow/chatgpt/EXECUTION.md`;
- Codex → `workflow/codex/EXECUTION.md`.

Read applicable `GITHUB_STATE.md`, `TASK_CARDS.md`, `OPENSPEC.md` and project `PROJECT.md`.

## State authority

`implementation/TASK_BOARD.yaml` is the sole live execution-state authority. The approved Master Plan milestone section is the default milestone contract; an optional `implementation/milestones/MXX.md` may extend it just-in-time. Task Card files are bounded contracts; evidence/handoffs prove or summarize results; `PROJECT.md` is high-level routing only.

Do not create synchronization commits whose only purpose is copying live status/result fields into milestone/Card/PROJECT files.

## Execution-set loop

Project execution is serial unless Task Board explicitly opts into `execution_mode: bounded_parallel`.

1. Establish repository root, intended integration branch, exact HEAD, working-tree state and relevant external/runtime baseline.
2. Read project execution policy and Task Board; recover every valid `in_progress` or `blocked` card and lane/base pointer.
3. Resolve the current milestone contract from the Task Board pointer (normally the approved Master Plan subsection, optionally a JIT milestone extension), then read candidate Task Cards and their exact authority slices plus relevant OpenSpec/requirements/decisions.
4. Determine READY cards whose dependencies are `done`; never select `planned`, `blocked`, `done` or `superseded`.
5. Build the next execution set:
   - `serial` → choose the first deterministic READY card;
   - `bounded_parallel` → choose up to `parallel_card_limit` READY cards explicitly `parallel_safe` and pairwise non-conflicting by `write_scope`/`exclusive_resources`.
6. Determine executor:
   - `chatgpt_only` → ChatGPT, no Capability Gate or capability preflight;
   - `codex_only` → Codex, no Capability Gate or capability preflight;
   - `mixed` → use the prior ChatGPT Capability Gate assignment for this set.
7. Before work relies on the selection, persist coordinator-owned Task Board transitions for the whole set: executor, `in_progress`, exact integration base and lane/workspace pointers. Transition Task Board milestone to `in_progress` when this is its first real execution.
8. Run Refresh Gate independently for each selected card against the same durable integration base plus completed dependencies.
9. Create/reconcile OpenSpec just-in-time if required.
10. Execute only bounded card scope. Before delegation or implementation, preserve the card's applicable authority slice: every implementation-shaping constraint must either be carried explicitly in the execution package or read from exact durable authority. Mutable parallel cards use isolated lane branches/worktrees or equivalent isolated workspace.
11. Run required tests/checks and verify card acceptance plus relevant OpenSpec behavior in each lane. Worker completion must surface material deviations/conflicting evidence rather than silently reinterpret authority.
12. For material external mutations, perform required readback/verification. External mutable targets named as exclusive resources remain serialized.
13. Integrate completed parallel lanes into intended milestone branch one at a time; reconcile conflicts explicitly.
14. After integration, run required post-integration checks or equivalent proof. Persist exact result pointers and `tests_summary`; add a standalone evidence pointer when the evidence policy requires one. Only then mark the card `done`.
15. Commit/push durable coordinator state, unblock newly eligible dependent cards and refill available parallel slots deterministically when safe.
16. Continue automatically while project policy, current review state and Task Board provide an unambiguous safe execution set. Do not ask the user to choose among equivalent runnable cards.
17. When a REQUIRED/RECOMMENDED independent review boundary is reached, apply `workflow/REVIEW_AND_HANDOFF.md` before claiming the reviewed subject GREEN.
18. After required cards and review gates are done, run integrated milestone acceptance on intended final milestone state.
19. RED → reopen/create corrective work. GREEN → milestone close/handoff under `workflow/REVIEW_AND_HANDOFF.md`.
20. After GREEN, apply next-milestone continuation rules below.

Bounded parallelism is opportunistic, not a utilization target. Run fewer lanes when uncertainty, integration risk, shared fixtures or ownership ambiguity make that safer.

## Coordinator and lane ownership

The project-level coordinator owns shared execution state while parallel lanes are active. At minimum this includes Task Board, milestone-wide handoff/acceptance/review pointers, lane/base bookkeeping and integration ordering.

A lane owns only bounded implementation/evidence scope. It must not independently rewrite Task Board or shared integration bookkeeping.

When Codex is executor and `codex_workflow` is installed, Codex Main is project-level coordinator; internal workers/reviewers may own individual Task Card/review lanes under `workflow/codex/CODEX_ORCHESTRATION.md`.

Parallel worker completion is not card completion. Reviewer-worker completion is not milestone acceptance. Main/coordinator integrates and persists project-level state.

## Authority-preserving delegation

Progressive disclosure is **lossless by authority, selective by context**.

A coordinator may send a worker less total context than the planner originally used, but may not drop an authoritative constraint that can affect the worker's implementation or acceptance. For each worker package, either carry the applicable constraint explicitly without semantic change or require the worker to read the exact durable authority reference before acting.

This rule applies equally to ChatGPT execution and Codex project-level delegation. It does not prescribe Codex worker mechanics owned by `codex_workflow`; it constrains only the project information that must survive delegation.

The independent reviewer uses the same applicable authority slice as the executor. Reviewing only the diff while omitting relevant requirements/decisions/plan constraints is insufficient when those constraints can change the verdict.

## JIT planning during execution

The execution orchestrator may perform L2 JIT decomposition/refinement whenever new durable predecessor evidence makes previously deferred execution detail knowable.

Allowed without strategic replan:
- create real Task Cards after their JIT trigger is satisfied;
- split/merge/reorder/replace not-yet-started cards;
- bind exact predecessor-result authority;
- refine technical scope, interfaces, tests and implementation-level acceptance;
- create/complete an optional JIT milestone extension.

Before relying on the refinement, persist the updated stable contracts and reconcile Task Board.

This authority stops at L3. If the new evidence requires changing accepted requirements, frozen architecture/decisions, global invariants, milestone outcome/product behavior contract or an explicit authorization boundary, block affected execution and route to strategic replanning.

The execution orchestrator does not need to return to the same model/session that authored the Master Plan for L1/L2 work.

## Independent review boundary

Task Board may carry `review_state`, `review_subject` and `review_evidence` for a card or milestone review gate.

- `review_state: pending` means implementation subject is frozen and independent verdict is still required.
- `in_progress` means an independent reviewer is actively reviewing the exact subject.
- `green` or `red` is the durable verdict state.

Under `chatgpt_only`, a ChatGPT chat that implemented the review subject **must stop** at a REQUIRED/RECOMMENDED review boundary after persisting exact subject/evidence. The user starts a fresh normal ChatGPT chat for the independent review. That fresh review chat may resume deterministic execution after a GREEN verdict.

Under `codex_only`, Codex Main uses an independent reviewer worker/session according to installed `codex_workflow` (or native Codex mechanisms if unavailable). This review boundary does not require a user handoff solely for independence.

Under `mixed`, follow the accepted review path and ensure the reviewer did not implement the subject.

Regardless of policy, the reviewer must recover the same applicable authority slice used to define the reviewed scope, plus exact subject/evidence. Reviewer independence is not permission to substitute a thinner interpretation of the accepted plan.

## Next-milestone continuation

A GREEN milestone is a checkpoint, not automatically a stop.

### Fixed policy: `chatgpt_only` or `codex_only`

The same fixed executor may continue automatically into the next milestone when all are true:
- next milestone is already accepted in approved Master Plan;
- preceding GREEN checkpoint satisfies its declared dependencies;
- every required/recommended review gate for the completed subject is GREEN;
- no explicit user/deployment/live-write/authorization gate is due;
- no strategic requirement/architecture/product decision is unresolved;
- just-in-time execution prep can be derived from durable authority.

The coordinator may perform allowed next-milestone execution prep, update Task Board to the new milestone and continue. Do **not** run Capability Gate or a capability preflight merely because milestone ID changed.

Under `chatgpt_only`, if the completed milestone requires/recommends independent review, the implementing chat stops and the fresh review chat becomes the session that may continue after GREEN.

Under `codex_only`, Codex Main may execute an approved M01→M02→… sequence without returning to ChatGPT after every GREEN checkpoint or review.

### `mixed`

A new execution assignment is routed by normal ChatGPT through Capability Gate. Previous executor is not automatically inherited.

If current executor is Codex, persist GREEN/handoff/Task Board and return routing control to ChatGPT. If current executor is ChatGPT, it may run the gate inline.

## User-visible continuation status

Execution checkpoints must not make it ambiguous whether work continues or needs user action.

Use an explicit state:
- `NEXT ACTION: continuing automatically with <card/set/milestone>; no user action required.`
- `USER ACTION REQUIRED: <smallest concrete decision/authorization/input>.`
- `USER ACTION REQUIRED: start a fresh normal ChatGPT chat for independent review from implementation/TASK_BOARD.yaml.` when `chatgpt_only` implementation reaches a required/recommended review boundary;
- `SESSION HANDOFF RECOMMENDED: <reason>. NEXT ACTION: start a fresh <ChatGPT chat|Codex session> from <durable pointer>.` only for context hygiene, not mandatory review;
- `MILESTONE COMPLETE: <checkpoint>. CONTINUING TO: <next milestone>` when fixed-policy continuation is valid;
- `MILESTONE COMPLETE: <checkpoint>.` when execution stops at that boundary.

Whenever the response tells the user to open a **fresh ChatGPT chat** — whether mandatory for independent review or merely recommended for context hygiene — the same response must immediately include a **copy-paste-ready fenced Markdown prompt** for that new chat.

Use:
```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/implementation branch>.
Kontynuuj: <exact card/milestone/review gate or concise goal>.
Durable start pointer: <implementation/TASK_BOARD.yaml | other exact durable pointer>.
Odtwórz aktualny stan, exact subject, authority slice i wymagane evidence z repo. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

Prompt is routing only. It must include the exact active project/implementation branch (including `main` when applicable). Do **not** duplicate SHAs, test results, evidence summaries, implementation details or other facts already recoverable from durable repository state. Include a card/milestone/review-gate ID when it helps route the fresh chat. Add only non-durable user intent that the repository cannot recover.

A routine GREEN card is not itself a reason to stop. One parallel lane finishing is not a reason to stop unrelated healthy lanes.

## Refresh Gate

Refresh Gate is a **state/contract drift gate**, not a fixed-policy capability inventory.

Before implementation compare at minimum:
- actual integration branch/HEAD and relevant runtime/external state;
- exact lane base/workspace when parallel;
- Task Board current milestone/card/set and execution pointers;
- latest cumulative handoff;
- relevant Master Plan/milestone/Card contracts/accepted decisions/requirements;
- current relevant OpenSpec;
- completed dependencies;
- actual code/runtime interfaces;
- required tests/checks, evidence/readback obligations and review requirements;
- recorded `write_scope`/`exclusive_resources` assumptions when parallel.

Do **not** proactively inventory or prove tool/MCP/environment availability under `chatgpt_only` or `codex_only` as part of Refresh Gate. Fixed policy already selected the executor.

If mismatch is a local implementation detail within approved behavior/architecture/requirements, reconcile it within executor authority.

If evidence materially changes behavior, architecture, frozen decision, requirement, external contract or milestone acceptance, do not implement stale contract. Persist evidence, set affected Task Board card `blocked` and use strategic resolution.

If a parallel lane discovers unexpected mutable overlap, pause affected ownership boundary and let coordinator serialize/re-scope it.

## Capability boundary

Project routing assumes:

`ChatGPT capabilities ⊆ Codex capabilities`

Capability Gate exists only for `mixed` pre-assignment routing.

### Fixed-policy rule

Under `chatgpt_only` and `codex_only`, **do not run a capability preflight, inventory, checklist or availability gate** during execution preparation or Refresh Gate. Start the allowed work directly.

A capability problem becomes workflow state only when a concrete operation required by the current card cannot proceed.

- ChatGPT uses the tool/plugin/connector surface actually available in the current chat. If a required concrete operation is unavailable, persist a runtime blocker and ask for the smallest remedy.
- Codex should self-remediate ordinary non-secret local tooling/dependency gaps when the execution environment permits it and doing so does not violate accepted security/reproducibility constraints. Persistent/material dependency changes belong in normal project evidence/source control as applicable.
- A missing MCP, credential, token, account permission, privileged access or explicit authorization that Codex cannot obtain itself becomes `USER ACTION REQUIRED` at the point it is actually needed.

Do not block merely because a capability *might* be needed later.

### Runtime blocker

When a concrete required operation cannot proceed:
- stop affected work safely;
- persist the exact missing capability/access and available evidence;
- set affected Task Board card `blocked` when its contract cannot be met;
- report `USER ACTION REQUIRED` with the smallest concrete capability/access/configuration needed.

If the user supplies the missing capability, resume the same card. If the user explicitly changes `execution_policy`, durable Task Board state may be reconciled and the blocked card reassigned under the new policy. **Never reroute or change policy automatically.**

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
- recover every existing `in_progress`/`blocked` card and pending/in-progress review gate from Task Board;
- inspect integration branch/HEAD plus recorded lane workspaces and relevant external/runtime state;
- inspect relevant OpenSpec/tests/evidence/result/review pointers;
- use local `current.md` only as a hint;
- continue each recoverable card/review from durable state under current explicit policy.

Recovery must be possible from durable repository state without prior chat.
