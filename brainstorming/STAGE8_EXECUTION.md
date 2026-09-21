# Stage 8 Brainstorming — Execution

Date: 2026-09-21
Scope: common-preexecution-core@R1
Status: active analysis
Production authority: none
Baseline: current main fixed-policy contracts

## Purpose

Merge the proven ChatGPT-only serial Execution behavior with the useful Codex-only bounded-concurrency/recovery behavior, without making the common workflow larger than necessary.

Primary design rule:

> Preserve the proven ChatGPT-only lifecycle and add only the minimum runtime-neutral state needed to support Codex-like delegation, bounded concurrency and safe cross-runtime continuation.

## Current V1 comparison

### ChatGPT-only

The current ChatGPT-only execution path is intentionally simple:

1. select one deterministic READY Card;
2. persist `ready -> in_progress`;
3. refresh current authority/source/evidence;
4. execute in the coordinating chat;
5. persist exact result/tests/evidence;
6. freeze independent review when required, otherwise finalize;
7. return to router.

Recovery prioritizes the existing `in_progress` Card and reconstructs actual durable implementation/result state instead of starting new work.

Its main policy-specific assumptions are:
- exactly one Card may be `in_progress` in the selected workstream;
- `executor: chatgpt` is persisted;
- there is no durable concurrent execution record.

### Codex-only

The serial path is semantically almost the same.

Codex additionally supports bounded concurrency with:
- Main as sole writer of shared Task Board/integration state;
- workers returning bounded results rather than writing shared state;
- frozen compatible member set;
- exact common integration base;
- returned result refs and integrated result refs;
- deterministic reconciliation order;
- preservation of successful sibling results on partial failure;
- recovery that never reruns a durable returned/integrated result just because a runtime worker/session disappeared.

Policy/runtime-specific details include:
- Codex Main / Executor / Tester names;
- orchestration binding;
- batch/lane terminology;
- concrete runtime realization.

## Common behavior to preserve

V2 Execution should preserve:

- existing active obligation outranks selecting unrelated new work;
- Main/coordinating context is the sole writer of shared Project Workflow state;
- delegated workers/subagents receive bounded Card authority and return result/evidence only;
- non-delegating runtime may have the same Main directly implement the Card;
- refresh/revalidation immediately before actual execution;
- exact result/tests/evidence/readback;
- no replay of already durable successful work;
- review is frozen only for the exact produced/integrated subject;
- RED correction is bounded and preserves prior result/review history;
- Research may interrupt execution when missing evidence prevents legal continuation;
- runtime/model/session/worktree identity is not canonical Project Workflow authority.

## Main is an orchestrating brain, not a passive scheduler

The target Main/coordinator remains responsible for reasoning about:
- current durable workflow state;
- Card selection;
- predecessor results;
- whether JIT refinement is needed;
- runtime capability available now;
- serial versus legal concurrent realization;
- validation of returned work;
- integration/reconciliation;
- review boundaries;
- recovery.

Workers may implement bounded work. They do not replace Main as Project Workflow coordinator.

This is semantic responsibility, not a concrete model/product identity.

## READY -> actual execution

Stage 7 may leave several Cards READY.

Stage 8 decides what to execute now:
- serial-only realization: choose one legal READY Card;
- concurrency-capable realization: may choose a compatible subset whose Stage-7 safety claims remain current;
- runtime capability affects scheduling, not READY semantics.

Before launch:
- refresh authoritative current state;
- confirm Card contracts/dependencies remain valid;
- confirm concurrency safety if more than one Card is selected;
- if materially stale, route back to JIT/Recovery instead of launching stale work.

## Result ownership

A delegated execution result is not automatically canonical.

Main validates returned work against:
- exact Card authority/scope;
- accepted base/current state;
- tests/evidence;
- write/resource constraints when relevant.

Only Main reconciles it into shared project state.

Direct serial execution in the coordinating context may naturally produce the canonical result directly.

## Runtime switch at clean Card boundary

If:
- prior Card is terminal/durable;
- exact result/evidence is present;
- no active unresolved execution remains;

then another supported runtime should simply recover the Task Board and continue the next legal obligation.

No special product-specific handoff is semantically required.

## Active-work takeover

Switching runtimes while work may still be active is different.

V2 must not start a duplicate realization merely because the previous chat/runtime is gone.

Safe takeover requires enough durable evidence that:
- prior realization is finished, or
- prior realization is quiesced/stopped at a known checkpoint, or
- a returned result is already durable and must be reconciled rather than rerun.

For external/non-idempotent side effects, uncertainty about whether old work may still continue must fail closed.

The concrete cancel/resume mechanism remains runtime-owned.

## Current design tension: active-execution state

Earlier Brainstorming proposed a generic neutral `active_execution` record that could represent both one-member serial and multi-member concurrent work.

That is portable, but may add ceremony to the already-good simple ChatGPT serial path.

A smaller alternative is:

- ordinary serial execution continues using the Card's existing `in_progress` + result/evidence state;
- introduce an additional neutral execution-set/transfer record only when needed for:
  - more than one concurrently active Card;
  - isolated delegated result reconciliation;
  - explicit cross-runtime quiescent transfer where ordinary Card state is insufficient.

Both approaches can preserve correctness.

The conservative-commonization principle means the universal wrapper should not be chosen merely for schema symmetry.

## Open material questions

1. Do we need one universal `active_execution` wrapper even for ordinary one-Card execution, or only a supplemental record when concurrency/transfer requires it?
2. When Main delegates a single Card to a worker in an isolated workspace, is the existing Card `in_progress` + exact returned result ref sufficient, or does delegation itself justify a generic execution-attempt record?
3. How much durable history of completed concurrent execution is actually needed after Card results/reviews are canonical, versus relying on Git/result/review history?
4. For runtime takeover of active work, should explicit `transfer_ready` be a common state only when a transfer is actually requested, rather than part of every normal execution lifecycle?

These are Stage-8 design questions, not accepted Definition decisions.


## Grilling decisions — minimal execution state

User accepted the first Stage-8 execution decisions:

1. Ordinary one-Card execution does **not** get a universal extra `active_execution` wrapper merely for schema symmetry. Preserve the simple proven Card lifecycle.
2. Delegating one Card to a worker/subagent also does not by itself require a new Project Workflow execution-attempt object. The Card remains `in_progress`; Main owns recovery and result reconciliation.
3. Bounded parallel execution remains fully supported. Additional durable group state is introduced only when multiple Cards are actually active together and project correctness/recovery needs shared base/member/result/reconciliation information.
4. Cross-runtime takeover of active work is not blind hot migration. Normal switching happens at safe durable boundaries; active-work transfer requires explicit quiescence/checkpoint evidence sufficient to prevent duplicate execution.

Clarification:

> Removing the universal wrapper does **not** remove parallel execution. It removes unnecessary extra state from the common serial path.

Target shape:

```text
serial/direct or single delegated Card
  ready -> in_progress -> result/review -> done

multiple concurrent Cards
  Cards become in_progress
  + one minimal neutral concurrent-execution record
    covering frozen members/base/result reconciliation/recovery
```

This preserves the simple ChatGPT-only serial behavior while retaining Codex-only bounded-parallel capability where it is actually needed.


## User decision — remove parallel Card execution from V2

The user explicitly removed Project Workflow parallel execution from the target V2.

Decision:

- exactly one Card may be actively executing per selected workstream;
- V2 does not form concurrent Card groups/batches;
- V2 does not need durable parallel member/base/lane reconciliation state;
- Codex-only bounded-parallel batch semantics are **not** carried into the common V2;
- useful Codex behavior that is not inherently parallel remains eligible for preservation, especially:
  - Main as sole writer of shared Project Workflow state;
  - delegation of one bounded Card to a runtime worker/subagent;
  - durable result/evidence reconciliation;
  - do not replay already durable successful work;
  - runtime/session/worker identity is not canonical Project Workflow state;
  - safe recovery of an in-progress Card.

Target ordinary execution therefore remains intentionally simple:

```text
planned -> ready -> in_progress -> review/finalization -> done
```

At most one Card is `in_progress` in the selected workstream.

This intentionally favors the already-proven ChatGPT-only serial lifecycle over importing Codex-only M03 bounded-parallel machinery.

### Consequences

The following candidate/common concepts are no longer needed for V2 Card execution:

- universal `active_execution` wrapper;
- optional concurrent execution-set record;
- batch IDs;
- lane IDs;
- frozen multi-member set/order;
- concurrent integration base;
- multi-member result reconciliation;
- post-batch review drain;
- same-member retry inside an unresolved batch;
- parallel Card metadata as a V2 requirement.

Stage 7 concurrency-safety metadata decisions are superseded by this later user decision. V2 does not need `parallel_safe`, `write_scope` or `exclusive_resources` for the purpose of Card concurrency.

Repository/file scope and external-write boundaries may still exist where needed for ordinary Card authority/safety, but not as a concurrency scheduler contract.

### Scope of this decision

This removes **Project Workflow-level concurrent Card execution**.

It does not prohibit a runtime from using internal implementation techniques inside one active Card, provided:
- one Card remains the single Project Workflow execution obligation;
- Main remains responsible for the Card result;
- no second Card becomes concurrently active;
- internal worker/session topology does not become Project Workflow state.


## Grilling decisions — delegated execution and recovery

User accepted:
- worker/subagent does not finalize shared Task Board state; Main validates and persists project truth;
- if a delegated worker result already exists durably after coordinator/runtime interruption, Main recovers and reuses it rather than rerunning the Card;
- uncertain external side effects require readback/recovery before retry; if safe state cannot be established, fail closed instead of duplicating a non-idempotent operation;
- no separate `transfer_ready` Card lifecycle state is added solely for runtime switching.

### Important correction — Main must delegate implementation when executor capability exists

For a runtime that provides qualifying implementation workers/subagents, Main is an orchestrator/reasoning coordinator and **must delegate Card implementation** rather than spending coordinator reasoning budget implementing the Card itself.

Project Workflow V2 should state only the semantic boundary:

> If the active runtime can realize a qualifying delegated implementation context for the Card, Main delegates the implementation. Main remains responsible for routing, JIT reasoning, authority, validation, integration, review boundaries and recovery.

If the active runtime genuinely has no delegated implementation capability, common Project Workflow may still allow direct implementation by the coordinating context so the same workflow remains usable in a normal ChatGPT-style runtime.

A failed invocation of an available implementation capability is not capability absence and must not silently authorize Main to implement the Card itself; it follows runtime retry/blocker/recovery behavior.

The stronger runtime-specific rule — e.g. that a Codex Main with installed executor workers never acts as the implementation worker — belongs primarily to runtime orchestration such as `codex_workflow`, not to a duplicated Project Workflow worker catalog.

This preserves:
- Main as the project brain;
- worker execution when workers exist;
- runtime portability when they do not;
- no product/model/worker names in canonical project state.

### Recovery of an interrupted delegated Card

For one `in_progress` Card:

1. recover current authoritative state;
2. determine whether an exact delegated result is already durable/recoverable;
3. if yes, validate/reconcile it once and do not rerun;
4. if no result exists and the prior realization cannot continue, re-realize the same Card through a qualifying implementation capability;
5. do not fall back to Main implementation merely because the previous worker disappeared when delegation capability still exists;
6. for uncertain external side effects, read back before any retry and fail closed when duplication safety cannot be proven.
