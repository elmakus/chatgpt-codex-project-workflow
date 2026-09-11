# Codex Execution Adapter

Read this only when the project router selected `EXECUTOR: CODEX` under `execution_policy: mixed`, or when recovering an already in-progress Codex-assigned card.

Codex follows the shared `workflow/EXECUTION.md` core plus `workflow/codex/CODEX_ORCHESTRATION.md` for the project/runtime authority boundary.

Codex must not load `CHATGPT.md` or `workflow/chatgpt/*` merely because they exist.

## Start/recovery

1. Establish repository root, branch, exact HEAD and working-tree/runtime state.
2. Read project `PROJECT.md`, Task Board, current milestone/card, latest handoff and relevant authority artifacts.
3. Verify any capability/environment named by the handoff before making state changes.
4. Run the shared Refresh Gate.
5. Execute/test/verify card scope and persist durable evidence.

## Practical-advantage routing

Codex assignment may be justified by local/runtime access, repo-wide implementation, long code→test→fix loops or another concrete advantage. Assignment does not expand card scope or strategic authority.

## User-visible continuation status

When surfacing execution status, make continuation explicit:
- `NEXT ACTION: continuing automatically with <card/action>; no user action required.`
- `USER ACTION REQUIRED: <smallest real authorization/decision/input>.`
- `SESSION HANDOFF RECOMMENDED: <reason>. NEXT ACTION: start a fresh Codex session from <durable pointer>.`
- `MILESTONE COMPLETE: <checkpoint>.`

Do not turn routine progress into an implicit wait.

## Strategic boundary

Implementation-detail reconciliation inside approved contracts is allowed. Material behavior/architecture/requirement/external-contract/acceptance changes must be persisted as a blocker and returned to ChatGPT/user strategic authority through the handoff protocol.
