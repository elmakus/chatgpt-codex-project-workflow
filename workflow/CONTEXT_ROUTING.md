# Context Routing

## Purpose

Progressive disclosure reduces what an agent reads for a task while preserving the complete workflow contract.

**Agent reads less at a given stage. Workflow contains no fewer rules.**

## Entrypoints

### Normal ChatGPT chat

1. workflow `CHATGPT.md`;
2. project root `PROJECT.md`;
3. this routing document;
4. phase-specific shared modules;
5. only project artifacts/contracts required by the task;
6. ChatGPT-specific module only when applicable.

Do not use ChatGPT Work.

### Codex

1. `prompts/CODEX_START.md`;
2. project root `PROJECT.md`;
3. this routing document;
4. shared execution modules/contracts required by assigned/continuing scope;
5. `workflow/codex/*` required for execution/runtime boundary.

Codex does **not** automatically read `CHATGPT.md` or `workflow/chatgpt/*`.

ChatGPT may read `workflow/codex/HANDOFF.md` only when preparing/interpreting a Codex handoff.

## Authority before routing

Apply `workflow/contracts/PROJECT_REPOSITORY.md#6-authority-and-conflicts` before interpreting project content.

Accepted decisions/requirements outrank brainstorming, approved plan outranks abandoned alternatives, Task Board + exact Git/runtime evidence govern live execution, the approved Master Plan milestone subsection is the default milestone contract, optional milestone files may extend it just-in-time, Task Cards define bounded execution contracts, and cumulative handoff summarizes completed milestone truth.

### Pending independent review has priority

When Task Board contains `review_state: pending | in_progress` for a REQUIRED/RECOMMENDED review gate, route to **MILESTONE REVIEW / CLOSE** (or the applicable card-review gate) before starting later dependent implementation.

Under `chatgpt_only`, a fresh ChatGPT chat opened after an implementing-chat handoff must treat the pending exact `review_subject` as its first execution obligation. It does not continue implementation first.

Under `codex_only`, Codex Main handles this priority internally through an independent reviewer worker/session according to installed `codex_workflow`.

## BRAINSTORMING

Read primarily `workflow/BRAINSTORMING.md`, project `PROJECT.md`, current brainstorming notes, relevant accepted decisions and open questions.

Usually do not load Task Board/full GitHub State/all OpenSpec/all handoffs unless question genuinely depends on them.

## RESEARCH

Read `workflow/RESEARCH.md`, `PROJECT.md`, current research question/notes, relevant requirements/accepted decisions and only needed source/current-state material.

## PLANNING

Read `workflow/PLANNING.md`, `PROJECT.md`, canonical requirements, relevant verified research, accepted decisions and current approved/draft plan. Load Task Card/OpenSpec execution contracts only when planning reaches execution decomposition. Do not force speculative future Card creation when the plan deliberately records a JIT decomposition trigger.

## EXECUTION PREP

Read `workflow/EXECUTION_PREP.md`, `PROJECT.md`, canonical requirements/approved Master Plan, latest handoff when relevant, Task Board if it exists, `TASK_CARDS`, `OPENSPEC`, `GITHUB_STATE` and relevant current source/runtime state.

Then route by policy:
- `chatgpt_only` → no Capability Gate and no capability preflight/inventory;
- `codex_only` → no Capability Gate and no capability preflight/inventory;
- `mixed` → normal ChatGPT reads/runs `workflow/chatgpt/CAPABILITY_GATE.md`.

During active or automatic `codex_only` execution, the execution orchestrator may read `workflow/EXECUTION_PREP.md` for L2 JIT decomposition/refinement within strategic boundaries, including later cards in the current milestone or the next already-approved milestone.

## CHATGPT EXECUTION

Read shared `workflow/EXECUTION.md`, `workflow/chatgpt/EXECUTION.md`, project `PROJECT.md`, Task Board, current milestone contract (Master Plan subsection or optional JIT extension), candidate Task Cards, their exact authority slices, latest handoff, relevant OpenSpec/source and only contracts needed by current set.

Under fixed `chatgpt_only`, Refresh Gate is state/contract drift checking, not a capability inventory.

Do not automatically load Codex execution/orchestration.

## CODEX EXECUTION

Read shared `workflow/EXECUTION.md`, `workflow/codex/EXECUTION.md`, `workflow/codex/CODEX_ORCHESTRATION.md`, project `PROJECT.md`, Task Board, current milestone contract (Master Plan subsection or optional JIT extension), candidate Task Cards, their exact authority slices, latest handoff, relevant OpenSpec/source and only needed shared contracts.

Under `codex_only`, also load `workflow/EXECUTION_PREP.md` at an approved milestone boundary when deterministic next-milestone preparation is required. Do not run a capability preflight; concrete runtime blockers are handled during execution.

Do not load ChatGPT-specific modules.

## STRATEGIC BLOCKER

Read project `PROJECT.md`, Task Board, specific blocker/evidence/exact commit, current milestone/Card contracts and only authority/source/research needed to decide it.

For Codex correlated ChatGPT control-channel communication, additionally read `workflow/codex/HANDOFF.md`.

## MILESTONE REVIEW / CLOSE

Read `workflow/REVIEW_AND_HANDOFF.md`, `PROJECT.md`, Task Board/current milestone contract, exact `review_subject` when present, the same applicable authority slice that governed implementation, required card results/evidence, relevant OpenSpec/Git/external state and prior cumulative handoff when needed.

For `chatgpt_only` REQUIRED/RECOMMENDED review, the reviewer must be a fresh normal ChatGPT chat that did not implement `review_subject`.

## FAILURE RECOVERY

Read `PROJECT.md`, exact branch/HEAD/runtime state, Task Board, contracts for every `in_progress`/`blocked` card, any `pending`/`in_progress` review gate, recorded executor, latest handoff, relevant OpenSpec/tests/evidence/result/review pointers.

A local `current.md` may be a convenience hint, but recovery must succeed without it.
