# Codex Execution Adapter

Read this when:
- project policy is `codex_only`; or
- project policy is `mixed` and Capability Gate assigned work to Codex; or
- recovering already Codex-assigned in-progress work.

Codex follows shared `workflow/EXECUTION.md` plus `workflow/codex/CODEX_ORCHESTRATION.md` for project/runtime authority boundary.

Codex must not load `CHATGPT.md` or `workflow/chatgpt/*` merely because they exist.

## Start/recovery

1. Establish repository root, integration branch, exact HEAD and working-tree/runtime state.
2. Read project `PROJECT.md`, Task Board, current milestone/Card contracts, latest handoff and relevant authority artifacts.
3. Recover every Codex-assigned `in_progress`/`blocked` card and lane/base state before selecting new work.
4. Verify any capability/environment required by current contract before making state changes.
5. Run shared Refresh Gate for each selected card.
6. Execute/test/verify serial card scope or compatible bounded set and persist durable evidence/Task Board state.

When Task Board uses `bounded_parallel`, Codex Main applies `CODEX_ORCHESTRATION.md`: Main remains project coordinator, mutable Task Cards use isolated lane workspaces, compatible cards may be delegated to internal workers, and Main alone integrates/updates shared execution state.

## `codex_only` continuous execution

Under `codex_only`, no Capability Gate is run.

After a GREEN milestone, Codex Main may continue automatically into the next already-approved milestone when shared continuation conditions hold. It may read `workflow/EXECUTION_PREP.md` and perform deterministic just-in-time preparation of milestone/Card contracts and Task Board state from the approved Master Plan.

This permits an approved multi-milestone sequence to run as one orchestrated Codex execution stream. Codex must still stop for:
- strategic/product/architecture/frozen-requirement change;
- explicit user/deployment/live-write authorization gate;
- missing required capability/evidence path;
- milestone RED that requires strategic resolution beyond bounded corrective work;
- end of approved scope.

Implementation-detail reconciliation and bounded corrective work within accepted contracts remain allowed.

## `mixed` boundary

Under `mixed`, Codex executes only its assigned Task Card/set/scope. After finishing a milestone, persist GREEN state and return routing control to ChatGPT before new milestone assignment unless Task Board already contains an explicit still-valid Codex assignment prepared through the mixed-policy gate.

## User-visible continuation status

When surfacing status, use:
- `NEXT ACTION: continuing automatically with <card/set/milestone>; no user action required.`
- `USER ACTION REQUIRED: <smallest real authorization/decision/input>.`
- `SESSION HANDOFF RECOMMENDED: <reason>. NEXT ACTION: start a fresh Codex session from <Task Board pointer>.`
- `MILESTONE COMPLETE: <checkpoint>. CONTINUING TO: <next milestone>` under valid `codex_only` continuation.

## Strategic boundary

Implementation-detail reconciliation inside approved contracts is allowed. Material behavior/architecture/requirement/external-contract/acceptance changes, or ownership conflict that invalidates approved decomposition, must be persisted as blocker and returned to strategic authority through `workflow/codex/HANDOFF.md` when necessary.
