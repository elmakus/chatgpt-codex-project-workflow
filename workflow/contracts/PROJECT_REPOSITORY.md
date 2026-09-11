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
│   ├── milestones/
│   ├── cards/
│   ├── evidence/
│   └── blockers/
├── project-handoffs/
│   └── MXX_HANDOFF.md
├── openspec/
│   ├── specs/
│   └── changes/
└── <project source/code, if applicable>
```

Projects may adapt filenames/paths when real repositories require it, but `PROJECT.md` must state actual canonical locations and knowledge-state separation must remain unambiguous.

## 4. Knowledge states

- `brainstorming/` — tentative ideas, alternatives, hypotheses and experiments.
- `decisions/` — decisions actually accepted by relevant authority.
- `research/` — source-grounded findings, audits, comparisons and analysis.
- `requirements/` — authoritative product/system requirements and constraints.
- `planning/` — approved plan, architecture and milestones.
- `implementation/` — live execution state, cards, evidence and blockers.
- `project-handoffs/` — cumulative milestone handoffs.
- `openspec/` — behavior/design contracts when justified.

## 5. PROJECT.md

Every project has a small current root `PROJECT.md`. It is a router and authority index, not a copy of history.

At minimum identify:
- project name/repository;
- current phase/goal/status;
- `execution_policy: chatgpt_only | mixed`;
- canonical requirements and plan;
- current milestone and Task Board;
- latest cumulative handoff;
- active OpenSpec change(s);
- relevant accepted decisions;
- open questions and blockers;
- workflow repository/ref.

When a pointer does not yet exist, state `none` instead of inventing an artifact.

### Execution policy

For a new project, default to `chatgpt_only` unless the user explicitly chooses `mixed`.

`chatgpt_only` means normal ChatGPT chat is the only permitted executor. ChatGPT may execute any work for which the current session has required capabilities/tests/evidence/readback. Missing capability is a blocker; do not route to Codex or mutate policy automatically.

`mixed` means ChatGPT remains project router and may execute itself or route a bounded Task Card to Codex through `workflow/chatgpt/CAPABILITY_GATE.md`.

Changing `chatgpt_only → mixed` requires an explicit user decision. ChatGPT Work is outside this workflow. Missing `execution_policy` in a legacy project must be resolved before new execution; absence is not a third mode.

## 6. Authority and conflicts

Apply authority by domain, not as one simplistic total order:

1. workflow behavior: current workflow `main`, except an explicitly frozen in-flight migration boundary documented by `MIGRATION_DUAL_EXECUTOR.md`;
2. accepted product/system intent: canonical requirements plus accepted decisions;
3. approved execution intent: Master Plan/milestone constrained by requirements/decisions;
4. current execution state: Task Board, Task Card, relevant OpenSpec, exact Git/runtime state and durable evidence;
5. completed milestone truth: cumulative handoff plus its referenced exact state;
6. research: evidence, not decision;
7. brainstorming: tentative until promoted.

`PROJECT.md` points to authority; it does not override referenced artifacts.

If current implementation/runtime evidence materially contradicts an approved behavior/architecture/requirement contract, the current executor does not silently rewrite strategic authority. It blocks and uses the appropriate strategic-resolution path.

## 7. Durable state versus local convenience

A local `current.md` or similar checkpoint is optional. It may help the current session but is not canonical Task Board/handoff, may not be the only location of important state and never outranks durable repository state.

Recovery must be possible from durable repository state without prior chat.

## 8. Git and branch policy

GitHub is the durable source of exact commits, PRs, evidence and checkpoints.

Default policy:
- coherent commits per Task Card/logical slice;
- isolated branch/PR for large milestones when project practice uses PRs;
- a card may be `done` after verified acceptance and durable commit even if several cards share a milestone PR;
- integrated milestone acceptance runs on intended final branch state;
- after merge/finalization, reconcile handoff to exact final state;
- create checkpoint/tag when project policy uses one;
- next milestone starts from the green checkpoint.

Never force-push `main` as a normal workflow action.

### Competing research/prototype paths

When independent alternatives genuinely require experimentation, Path A/Path B branches may start from the same stable checkpoint. Each records isolated findings/prototype evidence. Later comparison produces an accepted A/B/Hybrid decision before production implementation. Do not merge experimental code merely because it exists. This is an optional pattern, not a new lifecycle state.

## 9. In-flight branch/executor state

The repository remains canonical even while execution happens on an implementation branch or external runtime.

For an active card, the exact branch/HEAD/runtime evidence and recorded `executor` are authoritative for in-flight state. Completed milestone truth is reconciled back to canonical project state according to branch policy.

Strategic messages must include exact durable evidence/commit pointers so another session does not guess state.

## 10. External write state

Material external mutations follow `workflow/EXECUTION.md`: when meaningful readback exists, `WRITE → READBACK → VERIFY → EVIDENCE`. A successful write response alone is not complete evidence when persisted state can and should be independently re-read.

## 11. Legacy topology and workflow migration

Do not move active project topology mid-milestone. Legacy split-repository migration occurs at a green milestone boundary with provenance and updated `PROJECT.md` pointers.

Migration from v3.0.3 Codex-default execution to dual-executor semantics follows root `MIGRATION_DUAL_EXECUTOR.md`. In-flight work may temporarily freeze the workflow revision that started it and adopt the new `execution_policy` at the next clean GREEN boundary.

## 12. Initializing a new project

From an empty shell:
1. add `PROJECT.md` from template; it defaults to `chatgpt_only` unless the user explicitly selected `mixed`;
2. create only phase-appropriate knowledge directories;
3. start with brainstorming/research rather than fake implementation state;
4. record accepted choices under `decisions/`;
5. create canonical requirements/planning only when meaningful;
6. create implementation artifacts, Task Cards and OpenSpec just-in-time.

Do not populate placeholders merely to satisfy a directory checklist.
