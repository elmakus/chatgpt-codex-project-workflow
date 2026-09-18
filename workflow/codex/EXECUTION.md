# Codex Execution Adapter

Read this when:
- project policy is `codex_only`; or
- project policy is `mixed` and Capability Gate assigned work to Codex; or
- recovering already Codex-assigned in-progress work.

Codex follows shared `workflow/EXECUTION.md` plus `workflow/codex/CODEX_ORCHESTRATION.md` for project/runtime authority boundary.

Codex must not load `CHATGPT.md` or `workflow/chatgpt/*` merely because they exist.

## Start/recovery

1. Establish repository root, integration branch, exact HEAD and working-tree/runtime state.
2. Read project `PROJECT.md`, Task Board, current milestone contract (approved Master Plan subsection or optional JIT extension), current Task Cards, their exact authority slices, latest handoff and only relevant authority artifacts.
3. Recover every Codex-assigned `in_progress`/`blocked` card, pending/in-progress review gate and lane/base state before selecting new work.
4. Run shared state/contract Refresh Gate for each selected card. Do not use it as a capability preflight under `codex_only`.
5. Execute/test/verify serial card scope or compatible bounded set using authority-preserving delegation; persist exact result/test state and standalone evidence only when materially required.

When Task Board uses `bounded_parallel`, Codex Main applies `CODEX_ORCHESTRATION.md`: Main remains project coordinator, mutable Task Cards use isolated lane workspaces, compatible cards may be delegated to internal workers, and Main alone integrates/updates shared execution state.

When the owner's `codex_workflow` is installed/enabled, it is authoritative for internal Codex orchestration: worker selection, execute/review roles, delegation, concurrency, lifecycle, waiting and runtime recovery. Project Workflow supplies Task Card/review boundaries, applicable authority slices and durable project state; it does not duplicate those mechanics. Project Workflow's Authority Preservation Rule constrains what project intent must survive delegation, not how `codex_workflow` creates or manages workers.

## `codex_only` capability behavior

Under `codex_only`, no Capability Gate and no capability preflight/inventory is run. Start the allowed work directly.

If an ordinary non-secret local tool/package/dependency is missing, Codex should install/configure it when the execution environment permits and doing so is consistent with accepted security/reproducibility constraints. Treat this as ordinary execution detail rather than a user blocker; record persistent/material dependency changes as normal project evidence/source changes where applicable.

If a concrete operation reaches a missing MCP, credential, token, account permission, privileged access or other user-provided capability that Codex cannot obtain itself, persist the blocker and request the smallest required input/access at that point.

Do not stop merely because a capability might be needed later.

## `codex_only` continuous execution

After a GREEN milestone, Codex Main may continue automatically into the next already-approved milestone when shared continuation conditions hold. It may read `workflow/EXECUTION_PREP.md` and perform deterministic just-in-time preparation of milestone/Card contracts and Task Board state from the approved Master Plan.

This permits an approved multi-milestone sequence to run as one orchestrated Codex execution stream. Codex must still stop for:
- strategic/product/architecture/frozen-requirement change;
- explicit user/deployment/live-write authorization gate;
- a concrete runtime capability/access blocker it cannot self-remediate;
- milestone RED that requires strategic resolution beyond bounded corrective work;
- end of approved scope.

Implementation-detail reconciliation and bounded corrective work within accepted contracts remain allowed.

## Independent review under `codex_only`

A REQUIRED/RECOMMENDED independent review does not require returning control to the user or ChatGPT solely to obtain independence.

Codex Main freezes the exact review subject/evidence in Task Board and obtains a reviewer worker/session that did not implement that subject. When `codex_workflow` is installed/enabled, its orchestration rules determine how that reviewer is created/routed and how worker lifecycle is managed.

Project Workflow requires:
- exact `review_subject`;
- recovery of the same applicable authority slice that governed implementation;
- `review_state: pending → in_progress → green|red`;
- reviewer independence from the implementing worker/session;
- durable review evidence/verdict;
- Main integration of the verdict before milestone acceptance/continuation.

The implementing worker must not review its own subject, but Codex Main may keep the overall multi-milestone orchestration running around the independent review gate.

## `mixed` boundary

Under `mixed`, Codex executes only its assigned Task Card/set/scope. After finishing a milestone, persist GREEN state and return routing control to ChatGPT before new milestone assignment unless Task Board already contains an explicit still-valid Codex assignment prepared through the mixed-policy gate.

## User-visible continuation status

When surfacing status, use:
- `NEXT ACTION: continuing automatically with <card/set/milestone>; no user action required.`
- `USER ACTION REQUIRED: <smallest real authorization/decision/input>.`
- `SESSION HANDOFF RECOMMENDED: <reason>. NEXT ACTION: start a fresh Codex session from <Task Board pointer>.`
- `MILESTONE COMPLETE: <checkpoint>. CONTINUING TO: <next milestone>` under valid `codex_only` continuation.

A reviewer-worker boundary under `codex_only` is not a user-visible stop unless the review discovers a real strategic/user/authorization blocker.

## Strategic boundary

Implementation-detail reconciliation inside approved contracts is allowed. Material behavior/architecture/requirement/external-contract/acceptance changes, or ownership conflict that invalidates approved decomposition, must be persisted as blocker and returned to strategic authority through `workflow/codex/HANDOFF.md` when necessary.
