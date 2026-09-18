# Project Repository Contract

## 1. One project = one repository

Every new project receives its own repository from the first brainstorming session.

Do not wait for implementation before creating the repository. The project repository is durable memory across ChatGPT chats and Codex sessions.

By default do not create a separate planning repository, workspace repository, backup workflow-state repository or execution-control repository. A split-repository topology requires concrete technical justification and an explicit user decision.

## 2. Workflow repository versus project repository

`elmakus/chatgpt-codex-project-workflow` contains workflow rules, contracts, templates, prompts and workflow history only.

A project repository contains project-specific knowledge and, when the project has code, the code itself.

## 3. Canonical project layout

```text
<project-repo>/
├── PROJECT.md
├── brainstorming/
├── decisions/
├── research/
├── requirements/
│   └── REQUIREMENTS.md
├── planning/
│   └── MASTER_PLAN.md
├── implementation/
│   ├── TASK_BOARD.yaml
│   ├── milestones/        # optional JIT milestone extensions
│   ├── cards/
│   ├── evidence/          # standalone only when materially useful/required
│   └── blockers/
├── project-handoffs/
│   └── MXX_HANDOFF.md
├── openspec/
│   ├── specs/
│   └── changes/
└── <project source/code, if applicable>
```

Projects may adapt filenames/paths when real repositories require it, but `PROJECT.md` must state actual canonical locations and knowledge-state separation must remain unambiguous.

## 4. Knowledge and state ownership

- `brainstorming/` — tentative ideas, alternatives, hypotheses and experiments.
- `decisions/` — decisions actually accepted by relevant authority.
- `research/` — source-grounded findings, audits, comparisons and analysis.
- `requirements/` — authoritative product/system requirements and constraints.
- `planning/` — approved plan and architecture; approved Master Plan milestone subsections are the default milestone contracts.
- `implementation/TASK_BOARD.yaml` — **sole authoritative mutable execution state**.
- `implementation/milestones/` — optional just-in-time extensions when the Master Plan milestone contract needs material execution/acceptance detail; not live status mirrors.
- `implementation/cards/` — bounded Task Card authority/scope/acceptance/test contracts; not live status/result mirrors.
- `implementation/evidence/` — standalone durable proof when materially useful/required; simple card checks may remain in Task Board `tests_summary`.
- `implementation/blockers/` — durable blocker evidence.
- `project-handoffs/` — summaries of completed milestone truth and next starting context; not live trackers.
- `openspec/` — behavior/design contracts when justified.

Do not duplicate live `execution_status`, active executor, branch/HEAD, result pointers, current card/set or milestone checkpoint state into `PROJECT.md`, milestone files or Task Card files. Those facts live in Task Board and referenced evidence/Git state.

## 5. PROJECT.md

Every project has a small root `PROJECT.md`. It is a high-level router and authority index, not a live task tracker or copy of history.

At minimum identify:
- project name/repository;
- high-level lifecycle/goal/status;
- `execution_policy: chatgpt_only | codex_only | mixed`;
- canonical requirements and approved plan;
- Task Board location when implementation state exists;
- latest cumulative handoff when one exists;
- relevant accepted-decision index/pointers;
- workflow repository/ref.

When a pointer does not yet exist, state `none` instead of inventing an artifact.

Do not mirror current milestone/card/executor/branch/HEAD/checkpoint/active OpenSpec/blocker state into `PROJECT.md`. Read `implementation/TASK_BOARD.yaml` for current execution truth.

### Execution policy

For a new project, default to `chatgpt_only` unless the user explicitly chooses another policy.

`chatgpt_only` means normal ChatGPT is the fixed Task Card executor. No Capability Gate is run. Missing ChatGPT capability blocks execution until the capability is provided or the user explicitly changes policy.

`codex_only` means Codex is the fixed Task Card executor. No Capability Gate is run. Normal ChatGPT may still perform planning/strategy/user decisions and policy-required review, but Task Card execution is Codex-owned. Missing Codex capability blocks execution until supplied or policy is explicitly changed.

`mixed` means ChatGPT remains the project router and uses `workflow/chatgpt/CAPABILITY_GATE.md` before assignment to select ChatGPT, Codex or BLOCKED.

Project routing assumes `ChatGPT capabilities ⊆ Codex capabilities`.

Changing between any execution-policy modes requires an explicit user decision. Policy never changes automatically because of a blocker. ChatGPT Work is outside this workflow. Missing `execution_policy` in a legacy project must be resolved before new execution.

## 6. Authority and conflicts

Apply authority by domain, not as one simplistic total order:

1. workflow behavior: current workflow `main`, except an explicitly frozen in-flight migration boundary;
2. accepted product/system intent: canonical requirements plus accepted decisions;
3. approved execution intent: Master Plan milestone contracts plus any JIT milestone extension, constrained by requirements/decisions;
4. current execution state: Task Board plus exact Git/runtime/external state and durable evidence;
5. bounded execution/acceptance contracts: Task Cards plus relevant OpenSpec;
6. completed milestone summary: cumulative handoff plus its referenced exact state;
7. research: evidence, not decision;
8. brainstorming: tentative until promoted.

`PROJECT.md` points to authority; it does not override referenced artifacts. A separate milestone file is optional and extends rather than replaces the approved Master Plan subsection. Task Cards narrow execution scope but do not override richer requirements/decisions/plan authority. None of these contract artifacts override newer Task Board execution state.

If current implementation/runtime evidence materially contradicts an approved behavior/architecture/requirement contract, the current executor does not silently rewrite strategic authority. It blocks and uses the appropriate strategic-resolution path.

## 7. Durable state versus local convenience

A local `current.md` or similar checkpoint is optional. It may help the current session but is not canonical Task Board/handoff, may not be the only location of important state and never outranks durable repository state.

Recovery must be possible from Task Board + referenced contracts/evidence/Git state without prior chat.

## 8. Git and branch policy

GitHub is the durable source of exact commits, PRs, evidence and checkpoints.

Default policy:
- coherent commits per Task Card/logical slice;
- isolated branch/PR for large milestones when project practice uses PRs;
- a card may be `done` in Task Board after verified acceptance and durable commit even if several cards share a milestone PR;
- integrated milestone acceptance runs on intended final branch state;
- after merge/finalization, reconcile Task Board and cumulative handoff to exact final state;
- create checkpoint/tag when project policy uses one;
- the next milestone starts from the GREEN checkpoint.

Never force-push `main` as a normal workflow action.

### Competing research/prototype paths

When independent alternatives genuinely require experimentation, Path A/Path B branches may start from the same stable checkpoint. Each records isolated findings/prototype evidence. Later comparison produces an accepted A/B/Hybrid decision before production implementation. Do not merge experimental code merely because it exists. This is an optional pattern, not a new lifecycle state.

## 9. In-flight branch/executor state

The repository remains canonical even while execution happens on an implementation branch or external runtime.

For active work, Task Board records the exact integration/lane pointers and assigned executor. Exact Git/runtime/external readback evidence completes the in-flight truth.

Strategic messages must include exact durable evidence/commit pointers so another session does not guess state.

## 10. External write state

Material external mutations follow `workflow/EXECUTION.md`: when meaningful readback exists, `WRITE → READBACK → VERIFY → EVIDENCE`. A successful write response alone is not complete evidence when persisted state can and should be independently re-read.

## 11. Legacy state migration

Do not rewrite historical evidence/handoffs solely because the state model changed.

For a legacy project whose milestone/Card files still duplicate live status/result fields:
- Task Board becomes authoritative for new execution state when the project adopts current workflow;
- duplicated fields in old contract files are treated as historical/non-authoritative;
- remove or stop updating those duplicate fields at the next safe contract edit or milestone boundary;
- do not create churn merely to rewrite completed historical artifacts.

Do not move active project topology mid-milestone. Legacy split-repository migration still occurs at a GREEN boundary with provenance.

## 12. Initializing a new project

From an empty shell:
1. add `PROJECT.md` from template; it defaults to `chatgpt_only` unless the user explicitly selected `codex_only` or `mixed`;
2. create only phase-appropriate knowledge directories;
3. start with brainstorming/research rather than fake implementation state;
4. record accepted choices under `decisions/`;
5. create canonical requirements/planning only when meaningful;
6. create Task Board and Task Cards just-in-time; create separate milestone contracts, standalone evidence and OpenSpec only when their material criteria are met.

Do not populate placeholders merely to satisfy a directory checklist.
