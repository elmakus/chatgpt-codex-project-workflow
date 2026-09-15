# Codex Execution Adapter

Read this only when the project router selected `EXECUTOR: CODEX` under `execution_policy: mixed`, or when recovering already in-progress Codex-assigned work.

Codex follows the shared `workflow/EXECUTION.md` core plus `workflow/codex/CODEX_ORCHESTRATION.md` for the project/runtime authority boundary.

Codex must not load `CHATGPT.md` or `workflow/chatgpt/*` merely because they exist.

## Start/recovery

1. Establish repository root, integration branch, exact HEAD and working-tree/runtime state.
2. Read project `PROJECT.md`, Task Board, current milestone, active/ready Task Card set, latest handoff and relevant authority artifacts.
3. Recover every Codex-assigned `in_progress`/`blocked` card and its lane/base state before selecting new work.
4. Verify any capability/environment named by the handoff before making state changes.
5. Run the shared Refresh Gate for each selected card.
6. Execute/test/verify serial card scope or the bounded compatible ready set and persist durable evidence.

When Task Board uses `bounded_parallel`, Codex Main applies `CODEX_ORCHESTRATION.md`: Main remains project coordinator, mutable Task Cards use isolated lane workspaces, compatible cards may be delegated to internal workers, and Main alone integrates/updates shared project execution state.

## Practical-advantage routing

Codex assignment may be justified by local/runtime access, repo-wide implementation, long code→test→fix loops, useful bounded parallelism or another concrete advantage. Assignment does not expand card scope or strategic authority.

## User-visible continuation status

When surfacing execution status, make continuation explicit:
- `NEXT ACTION: continuing automatically with <card/set/action>; no user action required.`
- `USER ACTION REQUIRED: <smallest real authorization/decision/input>.`
- `SESSION HANDOFF RECOMMENDED: <reason>. NEXT ACTION: start a fresh Codex session from <durable pointer>.`
- `MILESTONE COMPLETE: <checkpoint>.`

Do not turn routine progress into an implicit wait. One parallel lane becoming GREEN is not itself a reason to stop unrelated healthy lanes.

## Strategic boundary

Implementation-detail reconciliation inside approved contracts is allowed. Material behavior/architecture/requirement/external-contract/acceptance changes, or a discovered ownership conflict that invalidates the approved parallel decomposition, must be persisted as a blocker and returned to ChatGPT/user strategic authority through the handoff protocol when necessary.
