# ChatGPT-only Project Repository Contract

This contract applies after root routing has selected `execution_policy: chatgpt_only`.

## One project = one repository

The project repository is durable project truth from brainstorming through implementation and handoff.

Do not create a second planning/state/control repository without explicit technical justification and user approval.

## Canonical layout

```text
<project-repo>/
├── PROJECT.md
├── brainstorming/
├── decisions/
├── research/
├── requirements/
├── planning/
├── implementation/
│   ├── TASK_BOARD.yaml
│   ├── milestones/
│   ├── cards/
│   ├── evidence/
│   └── blockers/
├── project-handoffs/
├── openspec/
└── <project source/code>
```

Projects may adapt paths, but `PROJECT.md` must identify actual canonical locations.

## State ownership

- brainstorming → tentative ideas;
- decisions → accepted decisions;
- research → evidence;
- requirements → authoritative product/system requirements;
- planning → approved plan/architecture;
- Task Board → sole mutable execution state;
- milestone/Card files → stable contracts, not status mirrors;
- evidence → durable proof when materially useful/required;
- blockers → durable blocker evidence;
- handoffs → completed milestone summaries;
- OpenSpec → selected behavior/design contracts.

Do not mirror current card/milestone/result/branch/review state into `PROJECT.md` or stable contract files.

## PROJECT.md

Keep it small. It should identify:
- project/repository;
- high-level goal/status;
- `execution_policy: chatgpt_only`;
- canonical requirements/plan;
- Task Board path when implementation exists;
- latest cumulative handoff when one exists;
- accepted-decision pointers;
- workflow repository/ref.

It is a router, not a live tracker.

## Git/branch policy

GitHub is durable source for exact commits, PRs, evidence and checkpoints.

Default:
- coherent commits per Card/logical slice;
- implementation branch/PR for substantial milestone work when project practice uses PRs;
- Card may be done after verified acceptance and durable result commit even when several Cards share one milestone PR;
- integrated milestone acceptance runs on intended final branch state;
- after finalization, reconcile Task Board and cumulative handoff;
- create checkpoint/tag when project policy uses one;
- next milestone starts from the GREEN checkpoint.

Never force-push `main` as a normal workflow action.

## External state

Material external mutations require meaningful persisted-state readback when available. A successful write response alone is insufficient when resulting state can and should be independently verified.

## Recovery

Recovery must be possible from:
- `PROJECT.md`;
- Task Board;
- exact Git/runtime/external state;
- current milestone/Card contracts;
- referenced evidence/OpenSpec/handoff as actually needed.

Previous chat narrative is not required authority.

## Legacy state

When old contract files duplicate mutable status/result fields, Task Board controls new execution state. Treat duplicates as historical and remove them only on a safe future edit; do not create repository-wide churn solely for cleanup.
