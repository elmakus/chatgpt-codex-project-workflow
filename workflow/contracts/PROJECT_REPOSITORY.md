# Project Repository Contract

## 1. One project = one repository

Every new project receives its own repository from the first brainstorming session.

Do not wait for implementation before creating the repository. The project repository is the durable memory of the project across ChatGPT chats and Codex sessions.

By default do not create a separate:
- planning repository;
- workspace repository;
- backup repository for workflow state;
- execution-control repository.

A split-repository topology is an exception. It requires a concrete technical justification and an explicit user decision.

## 2. Workflow repository versus project repository

`elmakus/chatgpt-codex-project-workflow` contains only workflow rules, contracts, templates, prompts and workflow change history.

A project repository contains project-specific knowledge and, when the project has code, the code itself.

Do not create central project workspaces under the workflow repository.

## 3. Canonical project layout

A project repository should converge on:

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

Projects may adapt filenames/paths when a real repository requires it, but `PROJECT.md` must state the actual canonical locations and the same knowledge-state separation must remain unambiguous.

## 4. Knowledge states

- `brainstorming/` — tentative ideas, alternatives, hypotheses and experiments.
- `decisions/` — decisions actually accepted by the relevant authority.
- `research/` — source-grounded findings, audits, comparisons and analysis.
- `requirements/` — authoritative product/system requirements and constraints.
- `planning/` — approved plan, architecture and milestones.
- `implementation/` — live execution state, cards, evidence and blockers.
- `project-handoffs/` — cumulative milestone handoffs.
- `openspec/` — behavior/design contracts when OpenSpec is justified.

The categories may reference each other but may not collapse into one ambiguous notes folder.

## 5. PROJECT.md

Every project repository has a small, current root `PROJECT.md`.

It is a router and authority index, not a copy of project history.

At minimum it should identify:
- project name/repository;
- current phase;
- current goal;
- current status;
- canonical requirements;
- canonical plan;
- current milestone;
- current Task Board;
- latest cumulative handoff;
- active OpenSpec change(s);
- relevant accepted decisions;
- open questions;
- current blockers;
- workflow repository;
- workflow ref, default `main`.

When a pointer does not yet exist, state `none` rather than inventing an artifact.

A fresh agent reads workflow entrypoint → `PROJECT.md` → phase-required context.

## 6. Authority and conflicts

Apply this authority by domain, not as a simplistic single total order:

1. **Workflow behavior:** current `main` of the workflow repository.
2. **Accepted product/system intent:** canonical requirements plus accepted decision records.
3. **Approved execution intent:** approved Master Plan/milestone, constrained by requirements and accepted decisions.
4. **Current execution state:** current Task Board, Task Card, relevant OpenSpec, exact Git branch/HEAD and durable evidence.
5. **Completed milestone truth:** cumulative handoff plus its referenced exact Git/evidence state.
6. **Research:** evidence for decisions/requirements, but not a decision by itself.
7. **Brainstorming:** tentative and non-authoritative until promoted.

`PROJECT.md` points to authority; it does not override the authoritative artifact it references.

If an old brainstorm, chat message or stale plan conflicts with accepted requirements/decisions, the accepted state wins.

If current implementation evidence materially contradicts an approved behavior/architecture/requirement contract, Codex does not silently overwrite strategic authority. It blocks and escalates according to `CHATGPT_CODEX.md`.

## 7. Durable state versus local convenience

A local `current.md` or similar checkpoint is optional. It:
- may remain uncommitted;
- may help the current session;
- is not the canonical Task Board;
- is not a cumulative handoff;
- may not be the only location of important state;
- never outranks durable GitHub state.

Project recovery must be possible from GitHub, cumulative handoff, Task Board/cards/OpenSpec and exact Git state without `current.md`.

## 8. Git and branch policy

GitHub is the durable source of exact commits, PRs, evidence and checkpoints.

Default policy:
- use coherent commits per Task Card or logical slice;
- for a large milestone, use an isolated branch/PR when the project normally uses PRs;
- a card may be `done` after verified acceptance and a durable commit even if several cards share one milestone PR;
- `result_pr` may therefore be the shared milestone PR;
- integrated milestone acceptance runs on the intended final branch state;
- after merge/finalization, reconcile the handoff to the exact final state;
- create a checkpoint/tag when project policy uses one;
- the next milestone starts from the green checkpoint.

Never force-push `main` as a normal workflow action.

## 9. In-flight branch state

The repository is the canonical project home even when execution is happening on an implementation branch.

For an active card, the exact branch/HEAD named by the execution context and durable evidence is authoritative for that in-flight implementation state. Completed milestone truth is reconciled back to the project's canonical `main`/checkpoint according to branch policy.

Strategic messages must include an exact evidence path and commit so ChatGPT does not guess which branch state to inspect.

## 10. Legacy split-repository migration

v3 does not migrate existing projects automatically.

For a legacy project that currently uses separate project/control/implementation repositories:
1. do not move an active milestone;
2. complete it against its frozen current topology;
3. reach a green checkpoint and write a cumulative handoff with exact final SHA;
4. perform the topology change only at the green milestone boundary;
5. start the next milestone in the selected canonical single project repository;
6. copy only canonical/active artifacts needed to preserve project truth, with provenance;
7. leave a pointer/migration note in the legacy location when appropriate;
8. update root `PROJECT.md` and authority pointers.

Do not duplicate active authority across multiple repositories indefinitely.

## 11. Initializing a new empty project repository

From an empty shell:
1. add `PROJECT.md` from `templates/PROJECT.md`;
2. create the phase-appropriate knowledge directories;
3. start with `brainstorming/` and/or `research/` rather than creating fake implementation state;
4. record accepted choices under `decisions/`;
5. create canonical requirements and planning only when they become meaningful;
6. create `implementation/` artifacts, Task Cards and OpenSpec just-in-time as the project reaches execution prep.

Do not populate placeholders merely to satisfy a directory checklist.
