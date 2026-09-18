# Migration to policy-driven ChatGPT/Codex Project Workflow

This document covers migration from older `ChatGPT plans → Codex executes` / two-policy workflow revisions to current policy-driven model.

## Current model

Every project has one project-level policy in root `PROJECT.md`:

```yaml
execution_policy: chatgpt_only | codex_only | mixed
```

There are still only two executors: normal ChatGPT and Codex. The three values are execution **policies**.

- `chatgpt_only` — fixed ChatGPT executor, no Capability Gate.
- `codex_only` — fixed Codex executor, no Capability Gate.
- `mixed` — ChatGPT routes new assignments through Capability Gate.

Project routing assumes `ChatGPT capabilities ⊆ Codex capabilities`.

Changing policy requires explicit user decision.

## Execution-state ownership change

Current workflow also makes:

`implementation/TASK_BOARD.yaml = sole authoritative mutable execution state`

Milestone/Card files are contracts; cumulative handoffs are completed-result summaries; `PROJECT.md` is high-level router/policy/index.

Legacy projects may still contain duplicated execution status, executor, SHA/checkpoint and result fields in milestone/Card/PROJECT files. Do not rewrite historical evidence merely for cosmetics. Once current workflow is adopted:

1. Task Board controls all new live execution-state changes.
2. Old duplicate fields are historical/non-authoritative.
3. Stop updating duplicate fields in milestone/Card/PROJECT files.
4. Remove them opportunistically when those contracts are next legitimately revised or at a clean milestone boundary.

## New or idle projects

Before next execution:
1. choose one of `chatgpt_only`, `codex_only`, `mixed` explicitly;
2. add/update `execution_policy` in high-level `PROJECT.md`;
3. ensure Task Board is the only live execution-state record;
4. use current workflow `main` normally.

Missing `execution_policy` is not a fourth mode. Execution must not guess it.

## Active execution started under older workflow

Do not change execution semantics in middle of an active card merely because workflow `main` changed.

For already-active bounded work:
1. preserve exact workflow revision that started it when changing semantics mid-card would invalidate recovery/acceptance;
2. finish/recover that bounded work under frozen contract unless safety/strategic blocker requires otherwise;
3. at next clean GREEN boundary, adopt current policy/state model;
4. reconcile Task Board as authoritative live state;
5. stop mirroring future status/result fields into milestone/Card/PROJECT files.

This is a migration-safety exception to normal current-`main` authority.

## Fixed-policy milestone continuation

After migration, `chatgpt_only` and `codex_only` do not run Capability Gate at each card/milestone.

If approved Master Plan already contains the next milestone and no strategic/user/deployment/live-write gate intervenes, fixed executor may continue automatically across GREEN milestone boundary using normal close/handoff, just-in-time execution prep and fresh Refresh Gate.

Under `codex_only`, this allows Codex Main to orchestrate an approved multi-milestone sequence without returning to ChatGPT just for routing.

## Existing durable history

Do not rewrite old evidence, handoffs or decision records merely to replace historical wording. Historical provenance should remain truthful.

New active artifacts use current state-ownership rules.

## ChatGPT Work

The workflow uses normal ChatGPT chat + Codex only. ChatGPT Work is not a migration target or execution mode.
