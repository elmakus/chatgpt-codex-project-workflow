# Migration to dual-executor Project Workflow

This document covers migration from the v3.0.3 `ChatGPT plans → Codex executes` model to the dual-executor model.

## What changes

Every project gains one project-level policy in root `PROJECT.md`:

```yaml
execution_policy: chatgpt_only | mixed
```

No second repository, capability registry, agent graph or executor-scoring configuration is required.

Task Cards may gain `executor` provenance and optional `required_capabilities` only when useful. Existing project knowledge/layout remains valid.

## New or idle projects

Before the next execution prep/execution:

1. choose `chatgpt_only` or `mixed` explicitly;
2. add `execution_policy` to `PROJECT.md`;
3. update any project-local workflow links that point directly to removed `workflow/contracts/CHATGPT_CODEX.md` or old `workflow/contracts/CODEX_ORCHESTRATION.md`;
4. use current workflow `main` normally.

Missing `execution_policy` is not a third mode. Execution must not guess it.

## Active execution started under v3.0.3

Do not change execution semantics in the middle of an active card merely because workflow `main` changed.

If a project has an active `in_progress` Codex card/milestone whose execution package was prepared under pre-cutover Project Workflow:

1. preserve the exact workflow revision that started that active execution (`3374232680a9b8a3de440e08257e003bdd706cee` or its corresponding immutable release tag if available);
2. finish/recover that active bounded work under its frozen execution contract unless a safety/strategic blocker requires otherwise;
3. at the next clean GREEN boundary, choose the project's `execution_policy`;
4. update `PROJECT.md` and any stale workflow pointers;
5. start subsequent execution preparation under current `main` and the Capability Gate.

This is a migration-safety exception to the normal rule that current workflow `main` is authoritative. It exists only to avoid changing an already-started execution contract mid-flight.

## Existing durable state

Do not rewrite old evidence, handoffs or decision records merely to replace historical words such as `Codex`. Historical provenance should remain truthful.

New/updated active artifacts should use executor-neutral wording and record the actual current executor where relevant.

## Policy choice

- Choose `chatgpt_only` when the project must not automatically use Codex. Missing ChatGPT capability blocks execution until the user changes policy or the capability becomes available.
- Choose `mixed` when ChatGPT may route bounded tasks to Codex when the Capability Gate finds a real capability/environment/practical advantage.

The workflow uses normal ChatGPT chat + Codex only. ChatGPT Work is not a migration target or execution mode.
