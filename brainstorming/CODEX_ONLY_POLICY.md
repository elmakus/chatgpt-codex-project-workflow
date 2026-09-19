# Brainstorm — dedicated codex_only policy namespace

Date: `2026-09-19`
Scope ID: `codex-only-policy`
Revision: `R1`
Status: `ready_for_definition`

## Problem / goal

Migrate `codex_only` out of the legacy/shared execution stack into a complete dedicated `workflow/codex_only/` namespace. Preserve the mature project lifecycle now embodied by `workflow/chatgpt_only/`, but replace ChatGPT-specific execution/review assumptions with a Project Workflow contract suited to Codex Main coordinating `codex_workflow`.

The workflow repository itself continues to execute under `execution_policy: chatgpt_only`; this feature changes the policy implementation available to other projects, not this project's own policy.

## Current understanding

### Verified facts

- Current repository `main` is `6b0445256b417f82431fb7b2704f56691eb4e7ae`.
- Root `PROJECT.md` selects `execution_policy: chatgpt_only`.
- Current `workflow/CONTEXT_ROUTING.md` routes `chatgpt_only` to `workflow/chatgpt_only/...` and all other accepted policies to legacy routing.
- `workflow/chatgpt_only/` is a complete dedicated policy namespace with policy-local Intake, Workstreams, Brainstorming, Research, Definition, Planning, Plan Review, Execution Prep, Execution, Review, State, Recovery, Close and Task Board/Card contracts.
- The ChatGPT-only namespace deliberately excludes legacy bounded-parallel lane state and Codex orchestration/worker semantics.
- ChatGPT-only execution is fixed to normal ChatGPT, serial per selected Task Board, and REQUIRED/RECOMMENDED independent review uses fresh normal-ChatGPT review context.
- Branch-isolated workstream state and the legacy/default Task Board compatibility model are already present on current `main`.
- No open PR or existing dedicated `codex_only` workstream was found.
- The old `feat/bounded-parallel-task-cards` branch is 433 commits behind current `main`, diverged by 13 commits, and modifies the former shared/legacy execution stack. It is useful evidence only, not a valid architectural parent.
- `elmakus/codex_workflow` release `v1.1.17-private.12` exists at source commit `d285aa1a271258052d23e3a2d3b585117fc1e862` and explicitly includes stateful Muse logical worker sessions plus fail-closed reservation/resume handling.

### Existing accepted decisions

The initiating user request accepts all of the following for this scope:

1. `codex_only` gets its own complete policy namespace, parallel in shape to `chatgpt_only`.
2. Do not return to one shared execution core containing ChatGPT/Codex conditionals.
3. Controlled duplication between the two policy namespaces is acceptable.
4. `workflow/common/` may contain only genuinely policy-neutral contracts.
5. Current ChatGPT-only lifecycle semantics are the reference baseline, but the migration is semantic rather than mechanical copy/paste.
6. Project Workflow owns milestones, Cards, dependencies, accepted authority, acceptance, review requirement/subject/state/evidence, parallel-safety/ownership semantics, workstream/integration semantics, durable state and workflow boundaries.
7. `codex_workflow` owns worker role/profile/model/reasoning selection, worker/session lifecycle, invocation mechanics, waiting, runtime recovery and worker concurrency mechanics.
8. Project Workflow must not persist or own runtime identifiers such as `session_id`, `invocation_id`, Muse leases or worker-resume protocol.
9. A qualifying independent Codex worker review may be the formal Project Workflow independent review; no second mandatory normal-ChatGPT review is required merely because the formal reviewer was a `codex_workflow` worker.
10. For implementation review, Tester remains separate from Executor and may not repair production. RED findings return via Codex Main to the owning Executor. A corrected implementation is a new immutable review subject.
11. The same independent Tester may review a new exact subject when independence remains intact and runtime resume is safe; fail-closed replacement is runtime-owned.
12. `codex_only` supports bounded parallel Task Cards inside one workstream, with serial execution as the default.
13. Planning may propose candidate parallel/dependency structure, but Execution Prep/JIT must verify actual current-state safety before concurrent execution.
14. Parallel safety includes completed dependencies, explicit `parallel_safe`, disjoint mutable `write_scope`, no conflicting `exclusive_resources`, isolated lanes/worktrees/equivalent workspaces, recoverable integration base, and Codex Main as sole owner of shared Task Board/integration state.
15. Existing legacy Codex/shared contracts are compatibility/evidence inventory only.

### Policy-specific deltas from chatgpt_only

The new namespace should preserve lifecycle structure unless a policy delta below requires different semantics.

#### Delta A — routing and policy boundary

- Add explicit `codex_only -> workflow/codex_only/...` routing.
- Keep `chatgpt_only` isolated in its own namespace.
- Leave other unmigrated accepted policies on legacy routing.
- Do not introduce cross-imports merely to reduce duplication.

#### Delta B — executor/runtime identity

ChatGPT-only currently states that normal ChatGPT is the fixed executor. Codex-only instead treats Codex Main as the project-level coordinator and uses `codex_workflow` to realize worker roles.

Project Workflow should express the required project role/contract, not the concrete worker model/profile/session mechanics used to satisfy it.

#### Delta C — independent review

ChatGPT-only equates independent review with a fresh normal ChatGPT chat. Codex-only must define independence semantically:

- formal reviewer is distinct from the implementation owner for the exact subject;
- reviewer judges an immutable exact subject against the same authority/acceptance surface;
- reviewer does not mutate the judged subject while acting as reviewer;
- implementation RED repair goes back to the owning Executor, not to the Tester;
- each changed implementation subject is a new review attempt;
- runtime may reuse or replace the logical Tester while Project Workflow records only review subject/state/evidence and the independence-relevant project facts.

For plan review or other non-implementation review gates, Codex-only should likewise require an independent reviewer contract rather than a normal-ChatGPT chat identity. The worker type/profile used to satisfy that contract remains a runtime decision.

#### Delta D — seriality versus bounded parallel Cards

ChatGPT-only intentionally permits only one `in_progress` Card per selected Task Board. Codex-only must replace that invariant with:

- serial by default;
- multiple concurrent Cards only when the approved plan identifies compatible candidate packages and current Execution Prep/JIT marks the exact Cards safe to overlap;
- no generic global scheduler;
- dependency graph + bounded ready-set semantics local to the selected workstream;
- shared Task Board/integration state mutated only by Codex Main;
- worker lanes never become independent owners of project state.

#### Delta E — filesystem/lane isolation

Keep existing worktree/equivalent isolation semantics but extend them from cross-workstream concurrency to intra-workstream parallel worker lanes whenever local mutable work overlaps in time.

Branch/worktree/lane mechanics are runtime execution details; Project Workflow records only the project-level lane ownership and safety facts needed for recovery/integration.

#### Delta F — recovery/session semantics

Keep durable locator-only recovery and exact-subject recovery. Remove assumptions that project continuity depends on a fresh normal-ChatGPT chat. Project Workflow recovery must succeed from repository state even if `codex_workflow` resumes A1/B1 or fail-closed replaces them with A2/B2.

Worker session identifiers and leases remain outside Project Workflow durable state.

#### Delta G — state provenance

Replace ChatGPT-only's fixed `executor: chatgpt` provenance with policy-appropriate project provenance that identifies the owning project role/lane without encoding runtime session/profile/model identifiers.

The exact schema is an implementation/planning detail, but it must remain sufficient for project recovery and must not duplicate runtime state.

### Legacy properties to preserve as behavior, not mechanism

Compatibility inventory identifies these useful properties to retain where consistent with the accepted architecture:

- Codex Main accountability for project state and integration;
- continuous deterministic progression across milestones;
- bounded parallel execution rather than unrestricted fan-out;
- Executor/Tester separation;
- strategic escalation back to the correct Project Workflow authority owner;
- lane/worktree isolation;
- single integration owner;
- recoverable exact state and exact review subjects;
- no capability preflight that silently changes a fixed execution policy.

### Assumptions to verify

No strategic assumption remains that blocks Definition. Runtime capability verification is sufficient for Definition because Project Workflow will specify only the boundary/contract it requires, not `codex_workflow` internals.

Implementation will still need exact repository-level inventory of every ChatGPT-only file and every legacy Codex/shared property before editing, but that is planning/execution evidence rather than a product-definition uncertainty.

## Ideas / alternatives considered

### Option A — dedicated full codex_only namespace

Accepted direction. Preserve lifecycle parity with explicit Codex-specific deltas.

### Option B — revive shared execution core with policy conditionals

Rejected by user. It would recreate cross-policy coupling and make future divergence harder to reason about.

### Option C — put most copied logic in workflow/common

Rejected unless the extracted contract is demonstrably policy-neutral. Avoid abstraction solely to reduce duplication.

### Option D — require fresh normal-ChatGPT review after Codex Tester

Rejected. A qualifying independent worker review is itself the formal Project Workflow review.

## Trade-offs / questions

- Controlled duplication increases maintenance cost but keeps policy semantics explicit and independently evolvable.
- Bounded intra-workstream concurrency makes state/recovery more complex; therefore the safety contract must be narrow and Main-owned.
- Codex-only must avoid leaking runtime worker/session mechanics into durable project state even though those mechanics are important to actual execution.

No unresolved user/product choice currently changes the target architecture.

## Research needed

No formal Research obligation is required before Definition.

Already verified evidence:
- current Project Workflow `main` policy structure;
- old bounded-parallel branch relationship to current `main`;
- current `codex_workflow` release and stateful Muse lifecycle capability.

Further source inventory is implementation/planning work, not Definition-blocking Research.

## Open questions

None that require user authority before Definition.

Implementation-time questions intentionally deferred:
- exact file-by-file copy/adaptation sequence;
- exact minimal Task Board/Card schema additions for bounded parallel lanes;
- exact compatibility test matrix and migration sequencing.

These are constrained by the accepted architecture and can be resolved in Planning/Execution Prep without changing it.

## Outcome of this session

- Tentative conclusions: the dedicated namespace can be defined without a new shared execution core; the principal policy deltas are executor/runtime identity, semantic independent review, bounded intra-workstream parallelism, lane isolation and runtime-agnostic recovery/provenance.
- Explicit user/product choices to promote through Project Definition: all accepted decisions listed above.
- Research still needed: none before Definition.
- Open questions: none that materially alter Definition.
- Next phase/action: `ready for definition`
- Definition promotion authorization: `user_authorized`
- Definition promotion subject: `codex-only-policy@R1`

> The initiating user explicitly authorized promotion of this conforming discovered scope after required discovery if no unresolved strategic contradiction remained. That condition is satisfied for this exact R1 scope.
