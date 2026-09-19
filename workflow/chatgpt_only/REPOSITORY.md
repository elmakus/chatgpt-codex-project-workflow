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
│   ├── TASK_BOARD.yaml        # legacy/default single-workstream board
│   ├── workstreams/            # optional branch-isolated workstreams
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
- selected canonical Task Board → sole mutable Card/milestone execution state for that default/workstream context, including its implementation/recovery Research routing pointer when such an obligation is active;
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
- `execution_policy: chatgpt_only`;
- active exploratory-scope pointer when Brainstorming/Definition recovery currently needs one;
- active pre-execution research-obligation pointer when Research/return-role recovery currently needs one;
- canonical requirements/plan;
- legacy/default Task Board path when the project uses that mode; branch-isolated Task Boards are located from their validated workstream manifests rather than mirrored into `PROJECT.md`;
- latest legacy/default cumulative handoff when one exists; branch-isolated handoffs are resolved from the selected workstream Task Board and are not mirrored into a project-global "latest" pointer;
- accepted-decision pointers;
- workflow repository/ref.

It is a router, not a live execution tracker. An `Active exploratory scope` pointer is allowed because it locates the canonical Brainstorming/Definition promotion record; promotion authorization/revision remains in that pointed record rather than being duplicated into `PROJECT.md`.

An `Active research obligation` pointer is also allowed for pre-execution Research because it locates the canonical research lifecycle record. Research `Status`, Origin subject and Return target remain in that pointed record. Implementation-triggered Research is routed by Task Board `research_obligation` and is not mirrored into `PROJECT.md`; the pointed research record owns lifecycle Status, Origin and Return target.

## Durable state versus local convenience

A local `current.md` or similar checkpoint is optional convenience only.

It is not canonical Task Board/handoff state, must never be the only location of important execution truth, and never outranks durable repository state.

Recovery must be possible from Task Board plus referenced contracts/evidence/Git/runtime state without prior chat.

## Branch-isolated workstream state

When the current branch is a branch-isolated ChatGPT-only workstream, apply `workflow/chatgpt_only/WORKSTREAMS.md` before loading implementation/review/recovery state.

The validated manifest owns the canonical Task Board path. The legacy/default `implementation/TASK_BOARD.yaml` remains untouched unless that default state itself is the selected context.

A branch-isolated workstream also owns its cumulative milestone handoffs under `implementation/workstreams/<id>/handoffs/`. It MUST NOT update `PROJECT.md -> Latest cumulative handoff`; that pointer belongs only to the legacy/default state context. Milestone-local handoff truth is recovered from the selected workstream Task Board.

For final-target integration, the exact merge subject must already carry the closure-ready namespaced workstream package required by `WORKSTREAMS.md#Terminal-durable-package-and-branch-cleanup`. After merge, the source branch may already be gone; closure/recovery continues from the target-side copy plus immutable PR/merge evidence, and a closure-only target-side commit/PR may reconcile actual merge/result metadata without recreating the source ref.

When a merged branch survives or a terminal unmerged branch later becomes cleanup-eligible, use only the manifest-local exact `branch_cleanup` fallback from `WORKSTREAMS.md`. A terminal-unmerged cleanup marker must itself be durable independently of the ref it authorizes deleting, normally via a closure-only namespaced target-side package that excludes rejected/superseded implementation content.

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

For normal GitHub merged-PR cleanup, repository-level automatic deletion of merged head branches is preferred when repository policy/rules permit it. Workflow correctness MUST NOT depend on that setting: immediate head disappearance is normal, while surviving/terminal-unmerged refs use the exact `branch_cleanup` fallback only after terminal safety. Do not emulate rename by creating `delete/*` or another same-SHA alias ref. Enabling/changing repository auto-delete and physically deleting a fallback ref are separate external configuration/ref writes and follow normal authorization/capability handling.

## Local concurrent checkout isolation

Branch isolation and filesystem isolation are separate requirements.

When two or more ChatGPT-only workstreams are actively executing against the same local repository storage at the same time:
- each actively mutating workstream must use its own Git worktree or equivalent isolated checkout;
- each checkout must remain on the exact branch/workstream it owns while that execution is active;
- one executor must not switch, reset or otherwise repurpose a checkout underneath another active workstream;
- sharing the same `.git` object database through normal Git worktree mechanics is allowed; the mutable working tree/index must be isolated.

A branch name by itself is not local isolation. Sequential work may reuse one checkout once no other executor is actively relying on that mutable checkout and the exact branch/state is reconciled before reuse.

Remote-only GitHub operations do not require creation of a local worktree because they do not share a mutable local checkout. A local worktree is therefore a runtime isolation precondition when concurrent local mutation exists, not a new durable execution-state source.

Worktree presence does not authorize concurrency inside one workstream. The selected Task Board still permits at most one `in_progress` Card.

## In-flight branch/runtime state

The project repository remains canonical while execution is happening on an implementation branch or external runtime.

Task Board records the exact active integration/execution branch pointers and executor provenance needed for recovery. Exact Git/runtime/external readback evidence completes in-flight truth.

Strategic-resolution packages must point to exact durable evidence/result state so another session does not have to infer it from prose.

## External state

Material external mutations require meaningful persisted-state readback when available. A successful write response alone is insufficient when resulting state can and should be independently verified.

## Recovery

Recovery must be possible from:
- `PROJECT.md`;
- for ordinary pre-integration non-terminal branch-isolated work, exact workstream branch + validated `WORKSTREAM.yaml`; for post-merge closure before terminal reconciliation, the merge-result target-side namespaced package + immutable PR/merge evidence; for integrated terminal `done` history after source-branch deletion, the target-side namespaced workstream package + exact manifest result; for terminal-unmerged cleanup history after deletion, the durable closure package + exact `branch_cleanup` evidence;
- the PROJECT-pointed active exploratory record when Brainstorming/Definition promotion or recovery is active;
- the PROJECT-pointed active pre-execution research record when Research/return-role recovery is active;
- selected canonical Task Board, including its implementation/recovery `research_obligation` pointer and exact pointed record when present;
- exact Git/runtime/external state;
- current milestone/Card contracts, or the exact bounded micro-fix Card + completed Intake record for a qualified direct fix;
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
