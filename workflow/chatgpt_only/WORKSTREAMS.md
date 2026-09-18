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
- exact Task Board location when implementation state exists;
- workstream authority pointers;
- workstream-level final-integration review state when such a gate is active;
- PR/result pointer when applicable.

The manifest does **not** own Card/milestone execution state.

When a Task Board exists, it alone owns mutable Card/milestone readiness, execution, executor, implementation/recovery Research pointer, Card/milestone review state, result and evidence fields.

The manifest `review` block is reserved for a **workstream-level final integration review**. It must never mirror a Card or milestone `review_state/review_subject/review_evidence`.

Do not infer a Card/milestone state from the coarse manifest `status`. If manifest status and the selected Task Board appear inconsistent, recover the exact durable facts and reconcile the manifest only at a safe workstream-lifecycle boundary; never overwrite Task Board truth to make the summary match.

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

M01 defines the fields only. Rules for choosing a parent, local worktrees, refresh/rebase/retarget and final integration are owned by the later accepted milestones.

## Recovery invariant

A branch-isolated implementation/review/recovery obligation is recoverable from:
- current workflow main;
- project `PROJECT.md`;
- exact workstream branch;
- exact workstream manifest;
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
