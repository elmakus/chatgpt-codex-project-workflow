# Design — codex_only M04 lifecycle cutover

## Baseline

Current `main` `workflow/chatgpt_only/*` is the semantic lifecycle reference. M02/M03 `workflow/codex_only/*` contracts remain authoritative for Codex-specific review, execution, provenance, bounded parallelism and recovery.

## Integration rule

Lifecycle modules are reconciled to semantic parity, not mechanically shared. Policy-local links remain inside `workflow/codex_only/*`; genuinely neutral contracts may use `workflow/common/*`.

Codex-specific deltas are preserved:
- Codex Main is the sole shared-state/integration writer.
- Executor/Tester are semantic roles; concrete runtime realization belongs to `codex_workflow`.
- Independent review is immutable-subject/role based, with Tester non-repair and no mandatory normal-ChatGPT second review.
- Serial execution remains valid; bounded parallelism is finite/JIT-proven and batch recovery remains repository-first.

## Root cutover

`workflow/CONTEXT_ROUTING.md` receives an explicit `codex_only` route between `chatgpt_only` and the legacy fallback. The `chatgpt_only` block is preserved. Every other non-migrated accepted policy continues to legacy.

## Workstream and Close

The live policy must support:
- explicit Intake and durable workstream identity;
- independent vs stacked base/dependency classification;
- manifest-selected/default Task Boards;
- micro-fix materialization;
- target movement refresh;
- exact final-review coverage preservation/invalidation;
- final-target integration and terminal namespaced-package recovery.

Internal M03 batch integration never substitutes for workstream final integration.

## Verification

Static routing/dependency/runtime-ID scans are combined with lifecycle scenario traces and exact protected-tree comparison against current `main`.
