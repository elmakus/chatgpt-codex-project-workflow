# ChatGPT-only Project Repository Contract

This contract applies after root routing has selected `execution_policy: chatgpt_only`.

## One project = one repository

The project repository is durable project truth from brainstorming through implementation and handoff.

Do not create a second planning/state/control repository without explicit technical justification and user approval. A split-repository topology is an exception that requires a concrete technical reason plus an explicit user decision.

## Workflow repository versus project repository

The workflow repository contains workflow rules, contracts, templates, prompts and workflow history only.

This project repository contains project-specific knowledge, durable execution state, evidence, handoffs and source/code.

Do not duplicate project truth into the workflow repository.

## Canonical layout

```text
<project-repo>/
├── PROJECT.md
├── brainstorming/
├── decisions/
├── research/
├── requirements/
├── planning/
│   └── reviews/
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

- brainstorming → tentative ideas plus the exact current exploratory-scope/revision promotion record when that phase is active;
- decisions → accepted decisions;
- research → evidence plus the exact active/complete/blocked/consumed Research continuation record when such an obligation exists; Research is not decision authority;
- requirements → authoritative product/system requirements;
- planning → draft/approved plan authority;
- planning/reviews → mutable pre-execution independent plan-review lifecycle/evidence; not execution state and never a substitute for Task Board;
- Task Board → sole mutable execution state, including the implementation/recovery Research routing pointer when such an obligation is active;
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
- active exploratory-scope pointer when Brainstorming/Definition recovery currently needs one;
- active pre-execution research-obligation pointer when Research/return-role recovery currently needs one;
- canonical requirements/plan;
- Task Board path when implementation exists;
- latest cumulative handoff when one exists;
- accepted-decision pointers;
- workflow repository/ref.

It is a router, not a live execution tracker. An `Active exploratory scope` pointer is allowed because it locates the canonical Brainstorming/Definition promotion record; promotion authorization/revision remains in that pointed record rather than being duplicated into `PROJECT.md`.

An `Active research obligation` pointer is also allowed for pre-execution Research because it locates the canonical research lifecycle record. Research `Status`, Origin subject and Return target remain in that pointed record. Implementation-triggered Research is routed by Task Board `research_obligation` and is not mirrored into `PROJECT.md`; the pointed research record owns lifecycle Status, Origin and Return target.

## Durable state versus local convenience

A local `current.md` or similar checkpoint is optional convenience only.

It is not canonical Task Board/handoff state, must never be the only location of important execution truth, and never outranks durable repository state.

Recovery must be possible from Task Board plus referenced contracts/evidence/Git/runtime state without prior chat.

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

## In-flight branch/runtime state

The project repository remains canonical while execution is happening on an implementation branch or external runtime.

Task Board records the exact active integration/execution branch pointers and executor provenance needed for recovery. Exact Git/runtime/external readback evidence completes in-flight truth.

Strategic-resolution packages must point to exact durable evidence/result state so another session does not have to infer it from prose.

## External state

Material external mutations require meaningful persisted-state readback when available. A successful write response alone is insufficient when resulting state can and should be independently verified.

## Recovery

Recovery must be possible from:
- `PROJECT.md`;
- the PROJECT-pointed active exploratory record when Brainstorming/Definition promotion or recovery is active;
- the PROJECT-pointed active pre-execution research record when Research/return-role recovery is active;
- Task Board, including its implementation/recovery `research_obligation` pointer and exact pointed record when present;
- exact Git/runtime/external state;
- current milestone/Card contracts;
- referenced evidence/OpenSpec/handoff as actually needed.

Previous chat narrative is not required authority.

## Legacy state

Do not rewrite historical evidence/handoffs solely because the state model changed.

When old milestone/Card files duplicate mutable status/result fields:
- Task Board controls new execution state;
- duplicated fields are historical/non-authoritative;
- remove or stop updating them only at the next safe contract edit or milestone boundary;
- do not create churn merely to rewrite completed historical artifacts.

Existing milestone files remain valid durable contracts even though separate milestone files are now optional.

Existing standalone evidence and cumulative handoffs remain durable history/evidence.

A legacy Task Board without an explicit milestone contract pointer may recover from its existing plan/milestone references; add the pointer at the next safe execution-prep/state edit rather than performing repository-wide churn.

Do not move active project topology mid-milestone. A legacy split-repository migration occurs only at a GREEN boundary with provenance.

Use current lean JIT rules for newly prepared work.

## Initializing a new project

From an empty project shell:
1. create a small `PROJECT.md` with the accepted `execution_policy: chatgpt_only`;
2. create only phase-appropriate knowledge directories;
3. begin with brainstorming/research rather than fake implementation state;
4. when substantial exploratory work has a canonical brainstorming record, point `PROJECT.md → Active exploratory scope` to it; do not create a placeholder record merely for the pointer;
5. use Project Definition to promote accepted intent into `requirements/` + `decisions/` only after the chatgpt_only promotion gate is satisfied;
6. create an approved Master Plan only after Definition Complete is GREEN;
7. create Task Board from `workflow/chatgpt_only/TASK_BOARD_TEMPLATE.yaml` and create Task Cards just-in-time through Execution Prep;
8. create separate milestone contracts, standalone evidence and OpenSpec only when their material criteria are met.

Do not populate placeholder artifacts merely to satisfy a directory checklist.
