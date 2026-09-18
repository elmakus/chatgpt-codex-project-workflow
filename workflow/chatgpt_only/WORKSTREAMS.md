# ChatGPT-only Workstreams

This contract defines how `chatgpt_only` resolves branch-isolated workstream state without weakening serial execution inside one workstream.

It applies only after root routing selected `execution_policy: chatgpt_only`.

## Core model

A **workstream** is one branch-isolated unit of project change with:
- one stable workstream ID;
- one exact branch;
- one durable `WORKSTREAM.yaml` manifest;
- at most one canonical Task Board when implementation state exists;
- its own authority/evidence/review pointers as applicable.

Concurrency exists **between workstreams**, not between Cards inside one workstream.

Exactly one Card may be `in_progress` in the selected workstream Task Board.

The legacy/default single-workstream mode remains valid. When no branch-isolated workstream is selected, `implementation/TASK_BOARD.yaml` remains the canonical Task Board exactly as before.

## Canonical branch-isolated layout

Default convention:

```text
implementation/
└── workstreams/
    └── <workstream-id>/
        ├── WORKSTREAM.yaml
        ├── INTAKE.md              # when created through explicit intake
        ├── TASK_BOARD.yaml
        ├── cards/
        ├── evidence/
        └── blockers/
```

A project may adapt subpaths when its manifest identifies the exact canonical paths.

Use:
- `workflow/chatgpt_only/WORKSTREAM_TEMPLATE.yaml`;
- `workflow/chatgpt_only/WORKSTREAM_TASK_BOARD_TEMPLATE.yaml`.

## Manifest ownership

The manifest is authoritative for **workstream identity, routing and workstream-level lifecycle/location metadata**.

It owns:
- stable ID and kind;
- coarse workstream lifecycle status;
- exact branch, base and integration target;
- optional stacked parent identity/branch;
- active/completed Intake lifecycle + exact intake-record location when the workstream was created/recovered through explicit intake;
- exact Task Board location when implementation state exists;
- workstream authority pointers;
- workstream-level final-integration review state when such a gate is active;
- PR/result pointer when applicable.

The manifest does **not** own Card/milestone execution state.

For intake-created workstreams, manifest `intake.state` + `intake.record` are routing/workstream-lifecycle metadata. The pointed `INTAKE.md` owns durable intake scope/findings/classification. Neither may mirror Card/milestone execution/review/result state.

When a Task Board exists, it alone owns mutable Card/milestone readiness, execution, executor, implementation/recovery Research pointer, Card/milestone review state, result and evidence fields.

The manifest `review` block is reserved for a **workstream-level final integration review**. It must never mirror a Card or milestone `review_state/review_subject/review_evidence`.

Do not infer a Card/milestone state from the coarse manifest `status`. If manifest status and the selected Task Board appear inconsistent, recover the exact durable facts and reconcile the manifest only at a safe workstream-lifecycle boundary; never overwrite Task Board truth to make the summary match.

## Workstream final-integration review

The manifest `review` block is a distinct workstream-level integration gate.

For intake-created issue/feature work that changes code, runtime configuration, external behavior or system behavior:
- set `review.requirement` to at least `RECOMMENDED`; use `REQUIRED` when existing risk authority requires it;
- keep `review.state/subject/evidence` null until an exact final/integrated subject is ready to freeze or until exact coverage by a stronger existing independent review is proven;
- when active, `pending | in_progress | green | red` has the normal fresh-chat independence semantics, but the selected manifest—not the Task Board—owns this workstream-level review lifecycle;
- `covered_by` may name an exact Task Board Card/milestone review only when that already-independent verdict covers the identical immutable integrated subject and the whole workstream acceptance surface;
- coverage reuse records a distinct gate conclusion; it must not copy ongoing Card/milestone review lifecycle state into the manifest.

If a workstream final review is RED, corrective execution/research remains inside that selected workstream and its selected Task Board. Do not mutate or inspect another workstream Task Board to find a correction lane.

Before final integration/publication of a workstream whose `review.requirement` is REQUIRED/RECOMMENDED, the owning finalization/integration role must do exactly one of:
1. prove an already-independent stronger review covers the identical immutable integrated subject and whole workstream acceptance surface, then reconcile this distinct manifest gate GREEN with exact `covered_by` evidence; or
2. freeze the exact integrated subject as manifest `review.state: pending` and stop at the normal fresh-review independence boundary.

A null workstream review state is therefore not integration approval. M04 owns target-refresh/rebase/retarget ordering around this gate; it may invalidate prior coverage only when the exact integrated subject materially changes.

For one-Card qualified micro-fixes, apply `workflow/chatgpt_only/MICRO_FIX.md#Workstream-final-integration-review`.

## Micro-fix state context

A completed issue Intake may select `path: micro_fix`. Execution Prep then applies `workflow/chatgpt_only/MICRO_FIX.md` and materializes one bounded fix Card plus this manifest's selected Task Board.

In micro-fix mode:
- manifest `authority.plan` may remain null because no full Master Plan is required;
- Task Board `plan_revision` and `current_milestone` are `micro-fix`;
- Task Board `milestones` remains empty;
- the bounded fix Card is the direct execution/acceptance contract;
- manifest ↔ Task Board identity binding remains mandatory before any mutable execution/review/Research state is trusted.

## Manifest ↔ Task Board binding validation

For a branch-isolated workstream, the manifest `task_board` value is only a location pointer until the pointed board is proven to belong to that exact workstream.

Before interpreting any Card/milestone/review/Research state from a branch-isolated Task Board:
1. when `task_board` is non-null, or implementation/review/recovery state is otherwise referenced for the selected workstream, require an exact non-null `task_board` path and require that file to exist on the exact selected workstream branch;
2. read only the pointed board's binding identity first;
3. require Task Board `workstream_id` to exactly equal manifest `id`;
4. require Task Board `execution_ref.branch` to exactly equal manifest `branch`;
5. only after those checks pass may the pointed board become the selected canonical Task Board and may its mutable execution state be interpreted.

A missing board, null board pointer when implementation/review/recovery state is required, mismatched `workstream_id`, or mismatched/null `execution_ref.branch` is inconsistent branch-isolated state. Route to Recovery; do not fall back to the legacy/default board and do not inspect another workstream board to guess intent.

This binding check does not create a global registry. It validates only the exact manifest/board pair selected by the current durable branch/locator.

## Selection before mutable execution state

Before reading implementation/review/recovery state, resolve exactly one state context.

### 1. Explicit workstream locator

When the durable handoff/current request identifies an exact workstream manifest or an exact workstream branch + canonical workstream pointer:
1. read that exact manifest;
2. verify its `branch` matches the intended exact branch;
3. apply **Manifest ↔ Task Board binding validation** to the manifest's exact `task_board` before interpreting mutable state;
4. if implementation state exists, read only that successfully bound Task Board;
5. do not inspect another workstream Task Board merely because it exists.

A locator is routing input, not authority to ignore mismatches.

### 2. Current branch workstream

When execution is already on an exact non-default workstream branch and no stronger durable locator exists:
1. inspect the branch for workstream manifests under the project's configured/default workstream root;
2. select the one manifest whose exact `branch` matches the active branch;
3. require an unambiguous manifest match, then apply **Manifest ↔ Task Board binding validation** before interpreting its Task Board.

Zero matching manifests means this branch is not resolved as a branch-isolated workstream. More than one matching manifest is inconsistent state and routes to Recovery.

### 3. Legacy/default fallback

When no branch-isolated workstream is selected:
- if the project uses `implementation/TASK_BOARD.yaml`, that file remains the canonical mutable implementation state;
- existing active/default state is never moved merely because multi-workstream support exists;
- absence of a workstream manifest never makes a legacy/default project invalid.

### 4. Ambiguity

Do not choose among multiple plausible workstreams from chat history.

If exact branch/manifest/state cannot be resolved from durable project/Git state:
- preserve existing state;
- route to Recovery when evidence can resolve it;
- otherwise stop only for the smallest genuinely required user input.

## Intake identity, naming and recovery

Explicit `#issue` / `#feature` creation semantics are owned by `workflow/chatgpt_only/INTAKE.md`.

For intake-created workstreams:

- issue IDs use `issue-<slug>` and branches use `fix/<slug>`;
- feature IDs use `feature-<slug>` and branches use `feat/<slug>`;
- collisions use the smallest available shared numeric suffix (`-2`, `-3`, ...);
- an existing exact branch/manifest/PR locator for the same workstream is recovered rather than duplicated;
- durable workstream IDs are never recycled merely because old work is done/superseded.

Naming is a creation convention, not a replacement for identity. After creation, `WORKSTREAM.yaml.id` and `WORKSTREAM.yaml.branch` are authoritative.

When a selected manifest has:

```yaml
intake:
  state: active
  record: <exact intake record>
```

the intake record must exist on that exact branch and the router resumes Intake before later Task Board execution for that workstream.

When `intake.state: complete`, Intake must not be replayed. The completed intake must already have materialized the canonical downstream state needed for normal router recovery. For a qualified micro-fix, the completed Intake record itself may be the pre-Task-Board continuation anchor when it records `path: micro_fix` + `next_route: execution_prep:micro_fix`; Execution Prep then materializes the bounded fix Card/Task Board.

A missing active intake record, an intake record that belongs to another workstream, or contradictory branch/manifest identity is inconsistent state and routes to Recovery rather than guessing.

## No mutable global registry

Correctness must not depend on a repository-global mutable workstream registry.

Active workstreams are recoverable from exact branch/handoff locators plus branch/PR discovery when the owning route requires discovery.

An optional project-level index may exist only as non-authoritative navigation unless a future accepted decision defines conflict-safe authoritative semantics.

`PROJECT.md` may document the workstream-root convention but must not mirror current workstream/Card/review state.

## Seriality and isolation

The serial invariant is scoped to the selected Task Board:
- one selected workstream may have at most one `in_progress` Card;
- another independent workstream may simultaneously have its own one `in_progress` Card;
- two active Cards in the same selected Task Board remain invalid.

Branch identity and mutable state identity must both be distinct for independent workstreams.

Filesystem/worktree isolation for concurrent local execution and detailed stacked/integration-refresh semantics are owned by the later worktree/integration contract; M01 does not weaken those accepted requirements.

## Stacked metadata

The manifest carries `parent_workstream`, `parent_branch`, `base_ref` and `integration_target` so later intake/integration logic can distinguish independent from stacked work.

M01 defines the stacked metadata fields. M02 Intake owns parent/base selection for new workstreams. Local worktrees, refresh/rebase/retarget and final integration remain owned by M04.

## Recovery invariant

A branch-isolated intake/implementation/review/recovery obligation is recoverable from:
- current workflow main;
- project `PROJECT.md`;
- exact workstream branch;
- exact workstream manifest;
- exact manifest-pointed intake record when `intake.state: active`;
- manifest-selected Task Board when implementation exists;
- exact authority/evidence/review pointers.

Previous chat narrative is never required.

For the legacy/default mode, existing `PROJECT.md` + `implementation/TASK_BOARD.yaml` recovery remains unchanged.

## Foreign-policy boundary

Do not import:
- legacy bounded-parallel lanes;
- mixed-policy Capability Gate routing;
- Codex orchestration/worker semantics.

This contract only scopes ChatGPT-only state selection and seriality.
