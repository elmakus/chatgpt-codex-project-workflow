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
4. shared execution modules/contracts required by the assigned card;
5. `workflow/codex/*` required for execution/runtime boundary.

Codex does **not** automatically read `CHATGPT.md` or `workflow/chatgpt/*`.

ChatGPT may read `workflow/codex/HANDOFF.md` only when preparing/interpreting a Codex handoff; it does not need detailed Codex execution/orchestration for ordinary work.

## Authority before routing

Apply `workflow/contracts/PROJECT_REPOSITORY.md#6-authority-and-conflicts` before interpreting project content.

Accepted decisions/requirements outrank brainstorming, approved plan outranks abandoned alternatives, current Task Board/Card/Git/runtime evidence govern in-flight execution and cumulative handoff records completed milestone truth.

## BRAINSTORMING

Read primarily `workflow/BRAINSTORMING.md`, project `PROJECT.md`, current brainstorming notes, relevant accepted decisions and open questions.

Usually do not load Task Cards, full GitHub State, all OpenSpec, all handoffs or implementation evidence unless the question genuinely depends on them.

## RESEARCH

Read `workflow/RESEARCH.md`, `PROJECT.md`, current research question/notes, relevant requirements/accepted decisions and only needed source/current-state material. Do not load full project history by default.

## PLANNING

Read `workflow/PLANNING.md`, `PROJECT.md`, canonical requirements, relevant verified research, accepted decisions and current approved/draft plan. Load Task Card/OpenSpec execution contracts only when planning reaches execution decomposition.

## EXECUTION PREP

Read `workflow/EXECUTION_PREP.md`, `PROJECT.md`, canonical requirements/approved Master Plan/current milestone/latest handoff, `TASK_CARDS`, `OPENSPEC`, `GITHUB_STATE` and relevant current source/runtime state. ChatGPT then reads `workflow/chatgpt/CAPABILITY_GATE.md`.

## CHATGPT EXECUTION

Read shared `workflow/EXECUTION.md`, `workflow/chatgpt/EXECUTION.md`, project `PROJECT.md`, Task Board, current milestone/card, latest handoff, relevant OpenSpec/plan/source and only contracts needed by the current card.

Do not automatically load Codex execution/orchestration.

## CODEX EXECUTION

Read shared `workflow/EXECUTION.md`, `workflow/codex/EXECUTION.md`, `workflow/codex/CODEX_ORCHESTRATION.md`, project `PROJECT.md`, Task Board, current milestone/card, latest handoff, relevant OpenSpec/plan/source and only needed shared contracts.

Do not load ChatGPT-specific modules.

## STRATEGIC BLOCKER

Read project `PROJECT.md`, specific blocker/evidence/exact commit, current Task Card/Task Board and only authority/source/research needed to decide it.

For Codex correlated ChatGPT control-channel communication, additionally read `workflow/codex/HANDOFF.md`. A strategic blocker never justifies loading all project history.

## MILESTONE REVIEW / CLOSE

Read `workflow/REVIEW_AND_HANDOFF.md`, `PROJECT.md`, Task Board/current milestone, required card results, acceptance/review evidence, relevant OpenSpec/Git/external state and prior cumulative handoff when needed.

## FAILURE RECOVERY

Read `PROJECT.md`, exact branch/HEAD/runtime state, Task Board, any `in_progress`/`blocked` card, recorded executor, latest handoff, relevant OpenSpec/tests/evidence/result pointers.

A local `current.md` may be a convenience hint, but recovery must succeed without it.
