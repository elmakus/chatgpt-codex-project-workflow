# Change: codex_only M03 bounded parallel Card safety

## Why

M02 finalized review/provenance/recovery semantics but intentionally remained serial. M03 adds the smallest project-level concurrency state that lets Codex Main launch a finite compatible set of Cards concurrently without turning Project Workflow into a worker scheduler or leaking runtime identity.

## Authority

- `planning/CODEX_ONLY_MASTER_PLAN.md#M03--bounded-parallel-task-cards-and-jit-safety`
- `requirements/CODEX_ONLY_POLICY.md` — `CO-REQ-017..025`
- `decisions/ADR_CODEX_ONLY_BOUNDED_PARALLEL_CARDS.md`
- `decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md`
- accepted M02 checkpoint `b901d1cfa5ca26074b363b0c8980f7a7aaa223f1`

## What changes

Define optional Card safety metadata (`parallel_safe`, `write_scope`, `exclusive_resources`), a per-Task-Board finite frozen batch ledger with exact integration base and semantic lane/result refs, deterministic JIT compatible-set construction, isolated workspace preconditions, Main-only validation/integration, and repository-first recovery.

Serial execution remains the fallback whenever current safety cannot be proven.

## Non-goals

- no repository-global scheduler or dynamically refilled queue;
- no runtime worker/session/model/profile/invocation/lease/resume identifiers in project state;
- no root policy cutover or edits to `workflow/chatgpt_only/*`;
- no M04 lifecycle/Close/stacked-target reconciliation.
