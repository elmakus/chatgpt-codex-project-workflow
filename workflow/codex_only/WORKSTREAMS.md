# Codex-only Workstreams

This contract defines how `codex_only` resolves branch-isolated workstream state while preserving serial-default execution and the bounded M03 parallel-Card exception inside one workstream.

It applies only after root routing selected `execution_policy: codex_only`.

## Core model

A **workstream** is one branch-isolated unit of project change with:
- one stable workstream ID;
- one exact branch;
- one durable `WORKSTREAM.yaml` manifest;
- at most one canonical Task Board when implementation state exists;
- its own authority/evidence/review pointers as applicable.

Independent workstreams may execute concurrently. Inside one workstream, execution is serial by default; multiple Cards may execute concurrently only through the explicit bounded M03 batch exception below.

Ordinary execution has one `in_progress` Card. Multiple `in_progress` Cards are legal only when `STATE.md` proves one exact current M03 batch covers them, or when they are integrated members of one just-closed batch in the bounded post-batch review drain.

Historical legacy/default single-workstream state remains recoverable, but it is not a mutable destination for branch-first managed work. When root `implementation/TASK_BOARD.yaml` is the only durable live-state source, use it only to recover/migrate the exact obligation into a branch-isolated workstream before further managed-change mutation.

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
        ├── handoffs/
        └── blockers/
```

A project may adapt subpaths when its manifest identifies the exact canonical paths.

Use:
- `workflow/codex_only/WORKSTREAM_TEMPLATE.yaml`;
- `workflow/codex_only/WORKSTREAM_TASK_BOARD_TEMPLATE.yaml`.

## Manifest ownership

The manifest is authoritative for **workstream identity, routing and workstream-level lifecycle/location metadata**.

It owns:
- stable ID and kind;
- coarse workstream lifecycle status;
- exact branch, creation base and integration target;
- optional stacked parent identity/branch plus the exact parent-only dependency relation;
- active/completed Intake lifecycle + exact intake-record location when the workstream was created/recovered through explicit intake;
- exact nullable pre-execution routing locators for exploratory scope, pre-execution Research and active plan review;
- compact workstream-local `orchestration` policy binding used for Codex runtime recovery;
- exact Task Board location when implementation state exists;
- workstream authority pointers;
- workstream-level final-integration review state when such a gate is active;
- PR/result pointer when applicable.

The manifest does **not** own Card/milestone execution state.

For intake-created workstreams, manifest `intake.state` + `intake.record` are routing/workstream-lifecycle metadata. The pointed `INTAKE.md` owns durable intake scope/findings/classification. Neither may mirror Card/milestone execution/review/result state.

### Orchestration policy binding

For branch-first `codex_only` work, the selected manifest owns one compact orchestration-policy binding:

```yaml
orchestration:
  runtime_owner: null
  policy_ref: null
  contract_fingerprint: null
```

This block is **workstream-local routing/recovery metadata**, not Card/milestone execution state.

- `runtime_owner` is an opaque owner identifier for the installed/enabled runtime contract.
- `policy_ref` is the opaque selected orchestration/compute-policy or profile reference interpreted by that runtime owner.
- `contract_fingerprint` is an optional opaque runtime-supplied contract version/epoch/fingerprint used only for stale-binding detection.
- A usable established binding requires non-null/non-empty `runtime_owner` and `policy_ref`; the fingerprint may remain null when no stable runtime fingerprint exists.
- A newly materialized manifest may contain null orchestration fields only during its initial materialization. Before Intake can complete, and before any policy-dependent runtime realization after the manifest exists, the binding must be successfully resolved through the runtime owner and persisted.
- A selected pre-schema branch-first manifest with no `orchestration` block is a distinct bounded Recovery migration case. When the block already exists but required values are missing, unknown or contradictory, the binding is invalid and fails closed rather than being treated as legacy schema absence.
- The binding may differ between workstreams and must not be mirrored into root `PROJECT.md`, Task Board, Task Cards or a repository-global mutable registry.
- Concrete worker/session/process/model-instance/invocation/lease/resume/worktree identity and concrete role→harness/model mappings remain forbidden manifest state.
- The current-context binding latch defined by `ORCHESTRATION_KERNEL.md` is deliberately non-durable and is never serialized into this block or any other Project Workflow state.

Project Workflow owns persistence/recovery of this opaque selection and the re-bind gate. The active runtime remains authoritative for interpreting `policy_ref` and realizing concrete worker roles/models/harnesses.

### Pre-execution routing locators

The manifest `routing` block is **locator-only** pre-execution state:

- `exploratory_scope` locates the exact active exploratory/brainstorming record for this workstream;
- `research_obligation` locates the exact active pre-execution Research record for this workstream;
- `plan_review` locates the exact active plan-review record for this workstream.

Each value is nullable. A non-null value MUST be an exact repository-relative path and, for ordinary pre-integration work, MUST resolve on the exact manifest `branch`. The pointed artifact remains the sole owner of its lifecycle/status, subject/revision, findings/return data or review verdict. Do not copy those fields into the manifest.

Before using a non-null routing locator, validate that the pointed artifact is the expected artifact class and belongs to the selected workstream/authority subject according to that artifact's owning lifecycle contract. A missing path, malformed locator, wrong artifact class, workstream/branch mismatch, plan-subject mismatch or contradictory stale locator is inconsistent state and routes to Recovery. Do not scan another branch, another workstream or a repository-global mutable registry to guess a replacement.

`routing.research_obligation` is only for **pre-execution** Research. Once implementation/recovery state exists, Research continuation remains owned by the selected Task Board's `research_obligation` pointer. The manifest `review` block remains reserved for the distinct workstream final-integration review and MUST NOT be used for plan review.

Locator lifecycle is fail-closed and artifact-first:
- create the pointed artifact before or in the same durable transition that sets its manifest locator; never point at a not-yet-durable record;
- keep `routing.exploratory_scope` through the exact Brainstorming → Definition promotion/Definition recovery obligation and clear it only after the owning Definition result is durable or the exploratory scope is durably closed/superseded;
- keep `routing.research_obligation` through `Status: complete`; clear it only after final-target reconciliation is durably `applied` and the record is `consumed` (except the explicit classifier-to-Research chaining rule, which applies only to Task-Board-owned implementation Research);
- keep `routing.plan_review` through `pending | in_progress | green | red`; the Tester never clears it. Planning consumes the exact verdict: after GREEN it clears the locator only with/after durable plan approval, while a corrective revision repoints it only after the new exact pending review record exists.

A stale non-null locator is not harmless metadata. Validate its record and route to Recovery when the lifecycle/subject no longer coheres; do not silently clear a locator whose owning result has not been reconciled.

When a Task Board exists, it alone owns mutable Card/milestone readiness, execution, semantic implementation-owner provenance, implementation/recovery Research pointer, Card/milestone review attempts, result and evidence fields.

The manifest `review` block is reserved for a **workstream-level final integration review**. It must never mirror a Card or milestone `review_state/review_subject/review_evidence`.

Do not infer a Card/milestone state from the coarse manifest `status`. If manifest status and the selected Task Board appear inconsistent, recover the exact durable facts and reconcile the manifest only at a safe workstream-lifecycle boundary; never overwrite Task Board truth to make the summary match.

## Workstream final-integration review

The manifest `review` block is a distinct workstream-level integration gate.

For intake-created issue/feature work that changes code, runtime configuration, external behavior or system behavior:
- set `review.requirement` to at least `RECOMMENDED`; use `REQUIRED` when existing risk authority requires it;
- keep `review.state/subject/evidence` null until an exact final/integrated subject is ready to freeze or until exact coverage by a stronger existing independent review is proven;
- when active, `pending | in_progress | green | red` uses the same immutable-subject and independent-Tester semantics as `REVIEW.md`, but the selected manifest—not the Task Board—owns this workstream-level review lifecycle;
- `covered_by` may name an exact Task Board Card/milestone review only when that already-independent verdict covers the identical immutable integrated subject and the whole workstream acceptance surface;
- coverage reuse records a distinct gate conclusion; it must not copy ongoing Card/milestone review lifecycle state into the manifest.

If a workstream final review is RED, corrective execution/research remains inside that selected workstream and its selected Task Board. Do not mutate or inspect another workstream Task Board to find a correction lane.

Before final integration/publication of a workstream whose `review.requirement` is REQUIRED/RECOMMENDED, the owning finalization/integration role must do exactly one of:
1. prove an already-independent stronger review covers the identical immutable integrated subject and whole workstream acceptance surface, then reconcile this distinct manifest gate GREEN with exact `covered_by` evidence; or
2. freeze the exact integrated subject as manifest `review.state: pending` and return through the router for a qualifying independent Tester; formal review alone does not require a second normal-ChatGPT boundary.

A null workstream review state is therefore not integration approval. Run the Integration refresh contract below before first freezing/reusing this final-integration gate, and repeat it if the target moves again before merge. Target movement by itself does not invalidate a verdict; prior coverage is invalid only when the exact covered workstream content/behavior or acceptance surface materially changes.

For one-Card qualified micro-fixes, apply `workflow/codex_only/MICRO_FIX.md#Workstream-final-integration-review`.

## Micro-fix state context

A completed issue Intake may select `path: micro_fix`. Execution Prep then applies `workflow/codex_only/MICRO_FIX.md` and materializes one bounded fix Card plus this manifest's selected Task Board.

In micro-fix mode:
- manifest `authority.plan` may remain null because no full Master Plan is required;
- Task Board `plan_revision` and `current_milestone` are `micro-fix`;
- Task Board `milestones` remains empty;
- the bounded fix Card is the direct execution/acceptance contract;
- manifest ↔ Task Board identity binding remains mandatory before any mutable execution/review/Research state is trusted.

## Manifest ↔ Task Board binding validation

For a branch-isolated workstream, the manifest `task_board` value is only a location pointer until the pointed board is proven to belong to that exact workstream.

Before interpreting any Card/milestone/review/Research state from a branch-isolated Task Board:
1. require an exact non-null `task_board` path whenever implementation/review/recovery state exists;
2. for a non-terminal workstream, require the pointed board to exist on the exact manifest `branch`;
3. for a terminal workstream whose source branch is no longer required, terminal-history recovery MAY instead read the target-side durable copy of that same manifest/board after the applicable closure contract has made the namespaced history package self-sufficient; this covers both integrated `status: done` + exact `result` and an intentionally terminal-unmerged workstream whose closure package was persisted before deletion; the deleted source branch is no longer a prerequisite;
4. read only the pointed board's binding identity first;
5. require Task Board `workstream_id` to exactly equal manifest `id`;
6. require Task Board `execution_ref.branch` to exactly equal manifest `branch`; this remains the original workstream identity/provenance and MUST NOT be rewritten to the integration-target branch merely because the workstream is done;
7. only after those checks pass may the pointed board become the selected canonical Task Board/history source.

A missing board, null board pointer when implementation/review/recovery state is required, mismatched `workstream_id`, or mismatched/null `execution_ref.branch` is inconsistent branch-isolated state. For non-terminal work, route to Recovery rather than falling back to the legacy/default board. For either an integrated terminal workstream or an intentionally terminal-unmerged workstream whose source branch was deleted, a missing required target-side durable package is likewise inconsistent finalization state.

This binding check does not create a global registry. It validates only the exact manifest/board pair selected by the current durable locator and lifecycle state.

## Selection before mutable execution state

Before reading implementation/review/recovery state, resolve exactly one state context.

### 1. Explicit workstream locator

When the durable handoff/current request identifies an exact workstream manifest or an exact workstream branch + canonical workstream pointer:
1. read that exact manifest;
2. when the locator names a live/source workstream branch, verify manifest `branch` matches it; when the locator names a target-side terminal package, keep manifest `branch` as provenance and use **Integrated terminal workstream** or **Terminal-unmerged workstream** below as applicable instead of requiring the current checkout branch to equal it;
3. apply **Manifest ↔ Task Board binding validation** to the manifest's exact `task_board` before interpreting mutable or terminal state;
4. if implementation state exists, read only that successfully bound Task Board;
5. do not inspect another workstream Task Board merely because it exists.

A locator is routing input, not authority to ignore mismatches.

### 2. Current branch workstream

When execution is already on an exact non-default workstream branch and no stronger durable locator exists:
1. inspect the branch for workstream manifests under the project's configured/default workstream root;
2. select the one manifest whose exact `branch` matches the active branch;
3. require an unambiguous manifest match, then apply **Manifest ↔ Task Board binding validation** before interpreting its Task Board.

Zero matching manifests means this branch is not resolved as a branch-isolated workstream. More than one matching manifest is inconsistent state and routes to Recovery.

### 3. Integrated terminal workstream

When an explicit durable locator identifies a workstream manifest already integrated into its final `integration_target` and the manifest records `status: done` plus an exact non-null `result`:
- recover its terminal history from the target-side durable copy of the namespaced workstream package;
- keep manifest `branch` and Task Board `execution_ref.branch` as original source-workstream provenance even if that source branch no longer exists;
- do not treat the terminal Task Board as active target-branch execution state;
- do not fall back to or mutate root `implementation/TASK_BOARD.yaml` merely because the source branch was deleted.

This terminal-history path is valid only after the finalization/readback rules below proved that the workstream package survived on the integration target.

### 4. Terminal-unmerged workstream

When an explicit durable locator identifies a branch-isolated workstream that intentionally reached a terminal state without final integration/merge and the applicable closure evidence proves that no live obligation still requires its source branch:
- recover terminal history from the target-side namespaced closure package persisted before deletion;
- keep manifest `branch` and Task Board `execution_ref.branch` as original source-workstream provenance even if that source branch is absent;
- do not treat rejected/superseded implementation content as integrated merely because its lifecycle/history package was preserved;
- do not fall back to or mutate root `implementation/TASK_BOARD.yaml`;
- derive cleanup completion only from the terminal-unmerged durable state plus exact current existence/absence of the manifest-owned branch.

This path must not require any separate cleanup lifecycle/field. A missing required target-side closure package after source-branch deletion is inconsistent finalization state.

### 5. Historical legacy/default recovery

When no branch-isolated workstream is selected and root `implementation/TASK_BOARD.yaml` exists:
- treat that board as historical recovery/migration input, not as the mutable destination for new or continued managed-change work;
- recover the exact outstanding authority/state and route to policy-local Recovery to create/recover the branch-isolated workstream before further mutation;
- preserve historical evidence and completed state without repository-wide churn;
- absence of a workstream manifest does not make historical state invalid, but it also does not authorize root/default mutation.

### 6. Ambiguity

Do not choose among multiple plausible workstreams from chat history.

If exact branch/manifest/state cannot be resolved from durable project/Git state:
- preserve existing state;
- route to Recovery when evidence can resolve it;
- otherwise stop only for the smallest genuinely required user input.

## Intake identity, naming and recovery

Explicit `#issue` / `#feature` shortcuts and generic natural-language managed-change creation semantics are owned by `workflow/codex_only/INTAKE.md`.

For intake-created workstreams:

- issue IDs use `issue-<slug>` and branches use `fix/<slug>`;
- feature IDs use `feature-<slug>` and branches use `feat/<slug>`;
- neutral generic changes use `change-<slug>` and branches use `work/<slug>`;
- collisions with coherently different durable work use the smallest available shared numeric suffix (`-2`, `-3`, ...);
- an existing exact branch/manifest/PR locator for the same workstream is recovered rather than duplicated;
- a deterministic candidate branch with a missing/malformed/identity-inconsistent manifest fails closed to Recovery and is not silently claimed or bypassed with a suffix;
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

Pre-execution `routing.*` locators are likewise selected-workstream state. They must not be mirrored into a repository-global mutable workstream registry.

## Serial-default execution and filesystem isolation

The default invariant is serial per selected Task Board. M03 permits multiple active Cards only through one finite JIT-proven batch whose membership/order/base are frozen, or through the bounded review/finalization/correction drain of integrated members from one just-closed batch. `STATE.md`, `EXECUTION_PREP.md`, `EXECUTION.md` and `RECOVERY.md` own those exact transitions.

Another independent workstream may execute concurrently with this one. Branch identity and mutable state identity must remain distinct.

Every concurrent local mutation—whether cross-workstream or intra-workstream M03 lanes—must use a separate Git worktree or equivalent isolated checkout as defined by `workflow/codex_only/REPOSITORY.md#Local-concurrent-checkout-isolation`. Different branch/lane labels in one shared mutable checkout are insufficient.

Remote-only GitHub operations do not require a local worktree because they do not share a mutable local working tree/index. Workspace paths and concrete runtime worker identity are runtime facts, never canonical Project Workflow state.

Filesystem isolation is a safety precondition; it does not authorize concurrency. Only the selected Task Board's exact M03 JIT/batch state does.

## Stacked dependency contract

A workstream is **stacked** only when it genuinely requires unmerged parent-only state. Intake owns the initial classification/base selection; this contract owns the durable integration consequences.

For an independent workstream:
- `parent_workstream`, `parent_branch` and `parent_dependency` are null;
- `base_ref` records the exact creation base;
- `integration_target` records the intended final target.

For a stacked workstream:
- `parent_workstream` and `parent_branch` identify the exact parent;
- `parent_dependency` is non-null and concisely states the parent-only behavior/interface/state the child requires;
- `base_ref` remains creation provenance and must not be rewritten later to pretend the child started independently;
- `integration_target` remains the intended final target unless accepted authority explicitly changes that target.

The fuller dependency evidence/rationale remains in the Intake record. The manifest keeps only the routing/integration fact needed for recovery.

Likely file overlap, convenience or avoiding a future rebase is not a valid stacked dependency. Conversely, once a real parent dependency exists, do not clear the parent metadata merely to make the child appear independent.

### Legal stacked integration paths

A stacked child has two legal ways forward:

1. **Fold child into the parent before parent integration.**
   - Integrate the child into the declared parent branch, not directly into the parent's final target.
   - The parent workstream now contains the child change; its own integrated subject/acceptance surface must be refreshed and any no-longer-covering final review must be invalidated/re-frozen.
   - Recording the child as merged into the parent is not the same as recording the child as independently integrated to main/default.

2. **Integrate the parent first, then reconcile the child.**
   - After the required parent commits are present in the child's `integration_target`, rebase/merge/retarget/reconcile the child against that current target as appropriate.
   - Run the Integration refresh contract below before the child's final integration.
   - Preserve parent metadata as dependency provenance; parent satisfaction is proven from exact Git/integration evidence, not merely a coarse parent status string.

Direct child → main/default integration is forbidden while commits/content required by `parent_dependency` remain available only on the unmerged parent branch.

If the declared parent dependency is discovered to be wrong or accepted integration intent must change, do not silently rewrite history. Reconcile the manifest/intake evidence inside current L1/L2 authority when the correction is purely technical; otherwise return through the router to Planning / Project Definition / Research as appropriate.

## Integration refresh contract

Before final merge/integration of a branch-isolated workstream, compare the exact frozen/validated workstream state with the **current** `integration_target`.

The gate is scoped to the selected workstream. Do not inspect or mutate unrelated Task Boards merely because another branch is active.

### 1. Establish target movement

Use exact Git/PR evidence to identify:
- current workstream branch/head or other exact covered content identity;
- current integration-target ref;
- the target state against which the workstream was last reconciled/validated, when one exists.

On the first final-integration pass, establish the current target as the compatibility baseline and run the verification required by the workstream acceptance surface.

If the target has not materially moved relative to the validated baseline, no reconciliation is required solely for freshness.

### 2. Reconcile material target movement

When the target moved materially, choose the smallest legal technical reconciliation inside accepted authority:
- fast-forward/rebase when project practice and history policy permit it;
- merge target changes into the workstream when that is the accepted project convention;
- retarget only when the resulting target still matches accepted integration intent;
- for a formerly stacked child whose parent is now integrated, reconcile onto the resulting current integration target.

Never force-push `main` as normal remediation.

After reconciliation:
- rerun only verification materially affected by target movement or conflict resolution;
- verify both textual merge/rebase conflicts and material semantic/interface/behavior conflicts;
- preserve exact evidence sufficient to show whether the covered workstream content/behavior and acceptance surface changed.

If reconciliation would change accepted product/system intent, architecture/strategic decisions or milestone strategy rather than merely technical integration detail, stop the affected integration and return through the router for Project Definition / Planning / Research classification.

### 3. Conflict semantics

File overlap is a diagnostic signal, not a blocker by itself.

Block/depend on another workstream only when there is:
- a real parent/dependency relation;
- incompatible accepted authority;
- an unresolved material semantic/interface conflict;
- or a textual/integration conflict that cannot be reconciled inside current authority.

A clean textual merge is not proof of semantic compatibility. Use the affected tests/checks, interfaces, requirements and accepted decisions needed to detect material semantic conflicts.

### 4. Review-subject preservation or invalidation

Run refresh **before** first freezing or reusing the manifest-owned final-integration review gate.

The final-integration `review.subject` must identify an exact immutable covered workstream content/behavior subject plus its acceptance surface. It must not be only a moving branch name or moving target ref. Exact Git refs/diffs and durable evidence may be used to prove that identity.

Target movement, a changed target commit SHA, or changed commit ancestry does **not** by itself invalidate an existing GREEN verdict when exact evidence proves that:
- the covered workstream-owned content/behavior is unchanged;
- the reviewed acceptance surface is unchanged;
- affected compatibility verification against the new target is GREEN.

When reconciliation materially changes the exact covered workstream content/behavior or the acceptance surface:
- the prior verdict/coverage no longer applies;
- clear stale `covered_by` reuse as applicable;
- freeze the new exact subject in the selected manifest;
- set the required/recommended final-integration review to `pending`;
- persist reconciliation evidence;
- the concrete production worker that performed behavioral reconciliation belongs to the implementation-owner set and cannot be the independent Tester for the new subject.

Immediately before the actual merge/integration, re-read the current integration target. If it moved again after GREEN review/coverage was established, repeat this refresh gate. Never merge solely on a stale target comparison.

## Terminal durable package and branch deletion

Deleting a source workstream branch is legal only after the applicable terminal history is durable independently of that source ref and no live Card, Research, review, stacked-dependency or integration obligation still requires it.

### Integrated final-target workstream

A final-target integration is not durably closed merely because source/code merged successfully.

For a branch-isolated workstream that reaches its final `integration_target`:

- the integration target MUST retain the workstream-owned durable package needed to recover completed truth: `WORKSTREAM.yaml`, selected `TASK_BOARD.yaml`, workstream-owned Card contracts, evidence, blockers that remain material, and any cumulative milestone handoffs;
- branch-isolated cumulative milestone handoffs use the collision-free canonical path `implementation/workstreams/<workstream-id>/handoffs/MXX_HANDOFF.md`; the selected Task Board owns the exact milestone handoff pointer;
- if the actual merge result cannot be recorded until after merge, perform a closure-only target-side commit/PR that reconciles manifest `status/result/pr`, selected Task Board final checkpoint/result/handoff pointers, and other required bookkeeping without changing the accepted implementation subject;
- read back the final integration target after that reconciliation and verify that every unique referenced workstream-owned durable artifact needed for recovery is present there;
- only after that readback is GREEN and no active obligation remains may the source workstream branch disappear;
- normal merged-workstream cleanup remains repository-owned automatic branch deletion; Codex-only does not add a merged-branch fallback lifecycle here.

### Intentional terminal-unmerged workstream

When accepted authority makes a branch-isolated Codex-only workstream intentionally terminal without final integration/merge, including `superseded` where applicable:

- first prove all existing terminal-safety conditions: no live Card, Research, review, stacked-dependency, integration or other workstream obligation may still require the source branch;
- before deletion, persist a namespaced closure/history package independently of the source ref, normally on the manifest `integration_target`; preserve the manifest, selected Task Board/history, relevant Card/evidence/blocker material and terminal rationale/provenance needed for later recovery;
- the closure-only package MUST NOT merge or publish rejected/superseded implementation content merely to preserve lifecycle history;
- read back that target-side package and verify it is self-sufficient for terminal history/recovery;
- the only cleanup target is the exact `WORKSTREAM.yaml.branch`; do not derive it from branch prefixes, naming patterns, PR closure or other heuristics;
- Codex Main performs the physical branch deletion through authenticated `gh` only after the durable readback and existing safety gates are GREEN;
- after deletion, read back exact branch absence. If Recovery later finds the exact branch already absent, cleanup is complete and the ref MUST NOT be recreated;
- do not introduce any separate cleanup lifecycle/field, cleanup registry, alias ref or runtime worker/session state for this behavior.

Workstream terminal state remains durable history unless a later explicit archival policy defines a different lifecycle. Do not collapse completed workstream state into the root legacy/default Task Board or a project-global mutable registry.

## Recovery invariant

A branch-isolated intake/implementation/review/recovery obligation is recoverable from:
- current workflow main;
- project `PROJECT.md`;
- for non-terminal work, the exact workstream branch;
- the exact workstream manifest;
- the exact manifest-pointed intake record when `intake.state: active`;
- the exact non-null manifest `routing.*` record(s) required by the active pre-execution phase;
- the manifest-selected Task Board when implementation exists;
- exact authority/evidence/review pointers;
- for an integrated terminal `done` workstream after source-branch deletion, the target-side durable workstream package plus exact manifest `result`/integration evidence;
- for an intentionally terminal-unmerged workstream after source-branch deletion, the target-side closure/history package plus exact manifest terminal state and closure/delete readback evidence.

Previous chat narrative is never required.

For historical legacy/default state, existing `PROJECT.md` + `implementation/TASK_BOARD.yaml` remain valid recovery inputs only. Any live managed-change continuation must migrate to the exact branch-isolated workstream before mutation.

## Foreign-policy boundary

Do not import:
- legacy bounded-parallel lanes;
- mixed-policy Capability Gate routing;
- legacy Codex orchestration as Project Workflow authority; runtime worker realization remains owned by `codex_workflow`.

This contract scopes Codex-only state selection, serial-default/bounded-parallel workstream safety, stacked integration, target refresh and terminal recovery.
