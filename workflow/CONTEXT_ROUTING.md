# Context Routing

Progressive disclosure reduces context per task without removing workflow obligations.

## Entrypoints

### ChatGPT

`CHATGPT.md → project PROJECT.md → this document → current shared phase module → only required project artifacts/contracts`

Load `workflow/chatgpt/EXECUTION.md` only when ChatGPT is executing. Load `workflow/codex/HANDOFF.md` only when preparing/interpreting a Codex handoff. Do not load detailed Codex execution/orchestration during ordinary ChatGPT work.

### Codex

`prompts/CODEX_START.md → project PROJECT.md → this document → shared execution modules/contracts → workflow/codex/* as required`

Codex must not automatically read `CHATGPT.md` or `workflow/chatgpt/*`.

## Authority before routing

Apply `workflow/contracts/PROJECT_REPOSITORY.md`. Accepted requirements/decisions outrank brainstorming; approved plan constrains execution; current Task Board/Card/Git state govern in-flight execution; cumulative handoffs summarize completed milestones.

## Brainstorming

Read `workflow/BRAINSTORMING.md`, `PROJECT.md`, current brainstorm notes, relevant accepted decisions and open questions. Usually do not load Task Cards, full Git state, OpenSpec archives or execution evidence.

## Research

Read `workflow/RESEARCH.md`, `PROJECT.md`, current research question, relevant requirements/decisions and only needed sources/current repository state.

## Planning

Read `workflow/PLANNING.md`, `PROJECT.md`, canonical requirements, verified research, accepted decisions and current approved/draft plan. Load execution contracts only when decomposition reaches execution prep.

## Execution prep

Read `workflow/EXECUTION_PREP.md`, `PROJECT.md`, canonical requirements/plan/current milestone/latest handoff and relevant `TASK_CARDS`, `OPENSPEC`, `GITHUB_STATE`. ChatGPT then reads `workflow/chatgpt/CAPABILITY_GATE.md`.

## ChatGPT execution

Read shared `workflow/EXECUTION.md`, ChatGPT adapter, `PROJECT.md`, Task Board, current milestone/card, latest handoff, relevant OpenSpec/plan/source and only contracts required by the task.

## Codex execution

Read shared `workflow/EXECUTION.md`, Codex adapter, Codex orchestration boundary, `PROJECT.md`, Task Board, current milestone/card, latest handoff and only relevant OpenSpec/plan/source. Do not load ChatGPT-specific modules.

## Strategic blocker / failure recovery

Read only `PROJECT.md`, exact branch/HEAD/runtime state, current Task Board/card/blocker evidence, latest handoff and authority artifacts needed to resolve the blocker. A blocker never justifies loading the entire project history.

## Milestone review/close

Read `workflow/REVIEW_AND_HANDOFF.md`, `PROJECT.md`, Task Board/current milestone, required card results/evidence, relevant OpenSpec/Git state and prior handoff when needed for cumulative truth.
