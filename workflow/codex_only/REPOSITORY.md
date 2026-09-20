# Codex-only Project Repository Contract

This contract applies after root routing has selected `execution_policy: codex_only`.

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
│   ├── TASK_BOARD.yaml        # historical legacy/default recovery input only
│   ├── workstreams/            # branch-isolated managed workstreams
│   │   └── <workstream-id>/
│   │       ├── WORKSTREAM.yaml
│   │       ├── TASK_BOARD.yaml
│   │       ├── cards/
│   │       ├── evidence/
│   │       ├── handoffs/
│   │       └── blockers/
│   ├── milestones/
│   ├── cards/
│   ├── evidence/
│   └── blockers/
├── project-handoffs/          # legacy/default single-workstream cumulative handoffs
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
- selected branch-isolated canonical Task Board → sole mutable Card/milestone execution state for current managed work, including its implementation/recovery Research routing pointer when such an obligation is active; historical root/default boards are recovery/migration input only;
- branch-isolated `WORKSTREAM.yaml` → workstream identity/routing + coarse lifecycle/location metadata only; it never mirrors Card/milestone state from its selected Task Board;
- milestone/Card files → stable contracts, not status mirrors;
- evidence → durable proof when materially useful/required;
- blockers → durable blocker evidence;
- handoffs → completed milestone summaries; legacy/default handoffs use `project-handoffs/`, while branch-isolated handoffs are workstream-owned under `implementation/workstreams/<id>/handoffs/`;
- OpenSpec → selected behavior/design contracts.

Do not mirror current card/milestone/result/branch/review state into `PROJECT.md` or stable contract files. `PROJECT.md` may document the workstream-root convention but is not a mutable global workstream registry.

## PROJECT.md

Keep it small. It should identify:
- project/repository;
- high-level goal/status;
- `execution_policy: codex_only`;
- canonical integrated requirements/plan;
- workstream-root discovery convention when used;
- optional historical/default Task Board and cumulative-handoff pointers for recovery/history navigation only;
- accepted-decision pointers;
- workflow repository/ref.

It is an integrated-project router/index, not a live execution tracker and not workstream-local pre-execution routing state. Active exploratory-scope, pre-execution Research and plan-review locators belong to the exact selected workstream manifest (or its exact pointed artifacts) under the Codex-only lifecycle contracts. Do not mirror those mutable locators into root `PROJECT.md`.

A historical root/default Task Board or cumulative-handoff pointer may remain for recovery of pre-branch-first repositories. Its presence does not authorize further managed mutation there; Recovery must create/recover and bind the exact branch-isolated workstream first.

## Durable state versus local convenience

A local `current.md` or similar checkpoint is optional convenience only.

It is not canonical Task Board/handoff state, must never be the only location of important execution truth, and never outranks durable repository state.

Recovery must be possible from Task Board plus referenced contracts/evidence/Git/runtime state without prior chat.

## Branch-isolated workstream state

When the current branch is a branch-isolated Codex-only workstream, apply `workflow/codex_only/WORKSTREAMS.md` before loading implementation/review/recovery state.

The validated manifest owns the canonical Task Board path for managed work. Historical root/default `implementation/TASK_BOARD.yaml` remains untouched as recovery/migration input and must not become the selected mutable destination.

A branch-isolated workstream also owns its cumulative milestone handoffs under `implementation/workstreams/<id>/handoffs/`. It MUST NOT update `PROJECT.md -> Latest cumulative handoff`; that pointer belongs only to the legacy/default state context. Milestone-local handoff truth is recovered from the selected workstream Task Board.

After final-target integration, the target branch must retain the terminal namespaced workstream package required by `WORKSTREAMS.md#Terminal durable package and branch deletion`. A closure-only target-side commit/PR may reconcile actual merge/result metadata. For an intentionally terminal-unmerged workstream, preserve the namespaced closure/history package independently of the source ref before deletion, without integrating rejected/superseded implementation content. Source-branch deletion is safe only after target readback proves the applicable terminal package is durable and no workstream obligation remains.

Correctness must not require a mutable repository-global workstream registry.

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

## Local concurrent checkout isolation

Branch isolation and filesystem isolation are separate requirements.

When two or more Codex-only workstreams, or two or more lanes in one valid M03 batch, are actively mutating the same local repository storage at the same time:
- each actively mutating workstream/lane must use its own Git worktree or equivalent isolated checkout;
- each checkout must remain on the exact branch/workstream/lane result context it owns while that execution is active;
- one concrete Executor/lane must not switch, reset or otherwise repurpose a checkout underneath another active mutation;
- sharing the same `.git` object database through normal Git worktree mechanics is allowed; the mutable working tree/index must be isolated.

A branch name by itself is not local isolation. Sequential work may reuse one checkout once no other executor is actively relying on that mutable checkout and the exact branch/state is reconciled before reuse.

Remote-only GitHub operations do not require creation of a local worktree because they do not share a mutable local checkout. A local worktree is therefore a runtime isolation precondition when concurrent local mutation exists, not a new durable execution-state source.

Worktree presence does not authorize concurrency. Inside one selected Task Board, multiple `in_progress` Cards are legal only through the exact finite M03 batch/post-batch-drain rules in `STATE.md`; otherwise execution remains serial.

## In-flight branch/runtime state

The project repository remains canonical while execution is happening on an implementation branch or external runtime.

Task Board records exact active integration/execution Git pointers plus semantic implementation-owner/lane provenance needed for recovery. Concrete runtime worker/session/worktree identity is not project authority. Exact Git/runtime/external readback evidence completes in-flight truth.

Strategic-resolution packages must point to exact durable evidence/result state so another session does not have to infer it from prose.

## External state

Material external mutations require meaningful persisted-state readback when available. A successful write response alone is insufficient when resulting state can and should be independently verified.

## Recovery

Recovery must be possible from:
- `PROJECT.md`;
- for non-terminal branch-isolated work, exact workstream branch + validated `WORKSTREAM.yaml`; for integrated terminal `done` history after source-branch deletion, the target-side namespaced workstream package + exact manifest result; for intentionally terminal-unmerged history after deletion, the target-side namespaced closure package + exact manifest terminal state and delete/readback evidence;
- the PROJECT-pointed active exploratory record when Brainstorming/Definition promotion or recovery is active;
- the PROJECT-pointed active pre-execution research record when Research/return-role recovery is active;
- selected canonical Task Board, including its implementation/recovery `research_obligation` pointer and exact pointed record when present;
- exact Git/runtime/external state;
- current milestone/Card contracts, or the exact bounded micro-fix Card + completed Intake record for a qualified direct fix;
- referenced evidence/OpenSpec/handoff as actually needed.

Previous chat narrative is not required authority.

## Legacy state

Historical root/default state remains readable for recovery and provenance, but it is not a valid destination for further managed-change mutation. Before continuing a live historical obligation, create or recover its exact branch-isolated workstream and migrate only the state required for coherent continuation under Recovery. Do not rewrite historical evidence/handoffs solely because the state model changed.

When old milestone/Card files duplicate mutable status/result fields:
- Task Board controls new execution state;
- duplicated fields are historical/non-authoritative;
- remove or stop updating them only at the next safe contract edit or milestone boundary;
- do not create churn merely to rewrite completed historical artifacts.

Existing milestone files remain valid durable contracts even though separate milestone files are now optional.

Existing standalone evidence and cumulative handoffs remain durable history/evidence.

A legacy Task Board without an explicit milestone contract pointer may recover from its existing plan/milestone references; add the pointer at the next safe execution-prep/state edit rather than performing repository-wide churn.

Do not move active project topology mid-milestone. A legacy split-repository migration occurs only at a GREEN boundary with provenance.

### Legacy branch → branch-isolated finalization migration

A long-lived branch created before branch-isolated layout may have continued mutating root `implementation/TASK_BOARD.yaml`, root `implementation/cards|evidence|blockers/`, root `project-handoffs/`, or the project-global latest-handoff pointer. When that branch must now integrate alongside an independently evolved target-side legacy/default context, migrate only at a GREEN/safe boundary before final integration:

1. create/recover one exact workstream manifest and namespaced Task Board for the long-lived branch;
2. preserve the branch's original exact branch as manifest/Task Board identity;
3. move or copy only branch-owned post-divergence Card/evidence/blocker/handoff artifacts into that workstream namespace and reconcile their pointers; branch-isolated milestone handoffs go under `implementation/workstreams/<id>/handoffs/`;
4. shared historical root artifacts that already exist on the integration target MAY remain referenced in place and MUST NOT be duplicated or rewritten merely for layout consistency;
5. reconcile the branch's root `implementation/TASK_BOARD.yaml` to the current integration-target version so the workstream merge does not overwrite the target's unrelated legacy/default board, unless changing that default context is itself explicitly accepted scope;
6. likewise preserve the target's `PROJECT.md -> Latest cumulative handoff` legacy/default pointer; workstream-specific handoffs stay discoverable from the namespaced Task Board;
7. keep genuinely project-wide accepted requirements/decisions/plan/source changes from the workstream when they are part of the integrated result; do not discard them merely because live execution state is being namespaced;
8. run normal target refresh/review/final integration, then perform target-side terminal closure/readback before deleting the source branch.

This is a bounded state-topology reconciliation, not permission to rewrite completed historical evidence or to infer ownership from filenames alone.

Use current lean JIT rules for newly prepared work.

## Initializing a new project

From an empty project shell or when adopting Project Workflow into a repository with an integration target:
1. perform only read-only discovery needed to establish the repository, integration target and accepted `execution_policy: codex_only`;
2. create or recover the exact branch-isolated workstream before the first durable workflow/project change-specific artifact or project-source write;
3. author the small integrated-project `PROJECT.md` target contract and phase-appropriate artifacts on that workstream branch; do not create root/default execution state as the new-work path;
4. keep active exploratory, pre-execution Research and plan-review locators workstream-local under the selected manifest; do not mirror them into root `PROJECT.md`;
5. use Project Definition to promote accepted intent into `requirements/` + `decisions/` only after the Codex-only promotion gate is satisfied;
6. create an approved Master Plan only after Definition Complete is GREEN;
7. when implementation state becomes necessary, create the manifest-selected workstream Task Board and Task Cards just-in-time through Execution Prep;
8. integrate the managed change through the workstream branch → pull request → merge path; create separate milestone contracts, standalone evidence and OpenSpec only when their material criteria are met.

Do not populate placeholder artifacts merely to satisfy a directory checklist.
