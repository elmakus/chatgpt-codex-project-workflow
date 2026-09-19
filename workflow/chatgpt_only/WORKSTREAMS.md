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
        ├── handoffs/
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
- exact branch, creation base and integration target;
- optional stacked parent identity/branch plus the exact parent-only dependency relation;
- active/completed Intake lifecycle + exact intake-record location when the workstream was created/recovered through explicit intake;
- exact Task Board location when implementation state exists;
- workstream authority pointers;
- workstream-level final-integration review state when such a gate is active;
- optional workstream-local branch-cleanup fallback state for a surviving merged branch or terminal unmerged branch;
- PR/result pointer when applicable.

The manifest does **not** own Card/milestone execution state.

For intake-created workstreams, manifest `intake.state` + `intake.record` are routing/workstream-lifecycle metadata. The pointed `INTAKE.md` owns durable intake scope/findings/classification. Neither may mirror Card/milestone execution/review/result state.

When a Task Board exists, it alone owns mutable Card/milestone readiness, execution, executor, implementation/recovery Research pointer, Card/milestone review state, result and evidence fields.

The manifest `review` block is reserved for a **workstream-level final integration review**. It must never mirror a Card or milestone `review_state/review_subject/review_evidence`.

The optional manifest `branch_cleanup` block is a fallback cleanup lifecycle, not execution state and not a registry. It stays null on the normal merged path when GitHub removes the head branch automatically. When activated, it may record only the exact original source ref, the exact source HEAD that passed terminal-safety checks, durable evidence and `safe_to_delete | deleted`. It never renames a ref and never changes manifest/Task Board branch identity.

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

A null workstream review state is therefore not integration approval. Run the Integration refresh contract below before first freezing/reusing this final-integration gate, and repeat it if the target moves again before merge. Target movement by itself does not invalidate a verdict; prior coverage is invalid only when the exact covered workstream content/behavior or acceptance surface materially changes.

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
1. require an exact non-null `task_board` path whenever implementation/review/recovery state exists;
2. for ordinary non-terminal work before integration, require the pointed board to exist on the exact manifest `branch`;
3. after an exact final-target PR/merge has succeeded, a **post-merge closure transition** MAY instead bind the target-side copy of that same manifest/board even when terminal `status/result/pr` reconciliation is not finished and the source branch has already disappeared. This exception is legal only when immutable Git/PR evidence proves the exact manifest source ref/head was merged into the declared `integration_target` and the target contains the workstream package carried by that merge subject;
4. for an integrated terminal workstream with `status: done` and a non-null exact `result`, terminal-history recovery MAY read the target-side durable copy after final integration and closure reconciliation; the deleted source branch is no longer a prerequisite;
5. for a terminal unmerged workstream whose cleanup fallback is target-side durable, recovery MAY read that exact target-side closure package after its source branch disappears; this does not make unmerged implementation content part of the integration target;
6. read only the pointed board's binding identity first;
7. require Task Board `workstream_id` to exactly equal manifest `id`;
8. require Task Board `execution_ref.branch` to exactly equal manifest `branch`; this remains the original workstream identity/provenance and MUST NOT be rewritten to the integration-target branch merely because source-branch existence changed;
9. only after those checks pass may the pointed board become the selected canonical Task Board/history source.

A missing board, null board pointer when implementation/review/recovery state is required, mismatched `workstream_id`, or mismatched/null `execution_ref.branch` is inconsistent branch-isolated state. For ordinary pre-integration non-terminal work, route to Recovery rather than falling back to the legacy/default board. For post-merge closure/terminal history, a missing or non-matching target-side durable package is likewise inconsistent finalization state. The transition exception never turns the workstream Task Board into active target-branch execution state.

This binding check does not create a global registry. It validates only the exact manifest/board pair selected by the current durable locator and lifecycle state.

## Selection before mutable execution state

Before reading implementation/review/recovery state, resolve exactly one state context.

### 1. Explicit workstream locator

When the durable handoff/current request identifies an exact workstream manifest or an exact workstream branch + canonical workstream pointer:
1. read that exact manifest;
2. when the locator names a live/source workstream branch, verify manifest `branch` matches it; when the locator names an integrated terminal target-side manifest with `status: done` + exact `result`, keep manifest `branch` as provenance and use **Integrated terminal workstream** below instead of requiring the current checkout branch to equal it;
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

### 3. Post-merge closure workstream

When exact immutable Git/PR evidence proves that the selected workstream's exact source head was merged into its declared final `integration_target`, but target-side terminal `status/result/pr` reconciliation is not yet complete:
- select the namespaced workstream package from the exact merge-result target state;
- validate manifest ↔ Task Board identity there while keeping the original source branch as provenance;
- permit this transition even when GitHub already deleted the source branch;
- use the target-side package only for closure/readback/recovery; do not route it as active target-branch implementation state;
- require exact PR/merge evidence plus target-side package identity sufficient to distinguish this state from an unrelated stale copy;
- route unfinished closure to `CLOSE.md` / Recovery rather than recreating the source ref.

This transition ends once target-side closure reconciliation/readback records the terminal result.

### 4. Integrated terminal workstream

When an explicit durable locator identifies a workstream manifest already integrated into its final `integration_target` and the manifest records `status: done` plus an exact non-null `result`:
- recover its terminal history from the target-side durable copy of the namespaced workstream package;
- keep manifest `branch` and Task Board `execution_ref.branch` as original source-workstream provenance even if that source branch no longer exists;
- do not treat the terminal Task Board as active target-branch execution state;
- do not fall back to or mutate root `implementation/TASK_BOARD.yaml` merely because the source branch was deleted.

This terminal-history path is valid only after the finalization/readback rules below proved that the workstream package survived on the integration target.

### 5. Terminal unmerged cleanup history

When an exact target-side closure package records a workstream as intentionally terminal without final-target integration (for example `status: superseded`) and owns a valid `branch_cleanup: safe_to_delete | deleted` fallback:
- recover only that namespaced closure/history package plus its exact evidence;
- do not treat unmerged implementation content as accepted target content;
- keep manifest/Task Board branch identity as original provenance;
- do not use closed PR state alone as proof of cleanup safety.

### 6. Legacy/default fallback

When no branch-isolated workstream is selected:
- if the project uses `implementation/TASK_BOARD.yaml`, that file remains the canonical mutable implementation state;
- existing active/default state is never moved merely because multi-workstream support exists;
- absence of a workstream manifest never makes a legacy/default project invalid.

### 7. Ambiguity

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

## Seriality and filesystem isolation

The serial invariant is scoped to the selected Task Board:
- one selected workstream may have at most one `in_progress` Card;
- another independent workstream may simultaneously have its own one `in_progress` Card;
- two active Cards in the same selected Task Board remain invalid.

Branch identity and mutable state identity must both be distinct for independent workstreams.

When multiple workstreams actively mutate the same local repository storage concurrently, each must use a separate Git worktree or equivalent isolated checkout as defined by `workflow/chatgpt_only/REPOSITORY.md#Local concurrent checkout isolation`. Different branch names in one shared mutable checkout are insufficient.

Remote-only GitHub operations do not require a local worktree because they do not share a mutable local working tree/index.

Filesystem isolation never creates a second execution lane inside one workstream and never becomes a new canonical state source.

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
   - The parent source branch may already have been automatically deleted; child dependency satisfaction is proven from the integration target plus exact Git/PR evidence and never requires that deleted parent ref.
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
- the chat that performed that behavioral reconciliation cannot independently review the new subject.

Immediately before the actual merge/integration, re-read the current integration target. If it moved again after GREEN review/coverage was established, repeat this refresh gate. Never merge solely on a stale target comparison.

## Terminal durable package and branch cleanup

A merge/closure is not durably safe merely because source/code merged successfully or a PR was closed.

### Closure-ready package before final merge

Before a branch-isolated workstream is merged into its final `integration_target`:
- the exact merge subject MUST already contain every unique workstream-owned artifact needed for recovery that can be known before merge: `WORKSTREAM.yaml`, selected `TASK_BOARD.yaml`, Card contracts, required evidence, material blockers and any cumulative milestone handoff file/pointer needed for the accepted checkpoint;
- branch-isolated cumulative milestone handoffs use the collision-free canonical path `implementation/workstreams/<workstream-id>/handoffs/MXX_HANDOFF.md`; the selected Task Board owns the exact pointer;
- fields that are inherently merge-result-dependent, such as the actual merge commit/result and final PR/result reconciliation, MAY remain pending pre-merge only when their closure path is already deterministic from target-side state + immutable PR/merge evidence;
- exact pre-merge branch/head and reviewed/integrated subject evidence must be sufficient to prove which package the merge carried.

Do not leave a unique recovery artifact only on the source branch with the intention of writing it after merge.

### Post-merge closure when the source branch may already be gone

After a successful final-target merge:
- treat immediate GitHub deletion of the PR head branch as normal success;
- continue from the merge-result target-side workstream package plus immutable PR/merge metadata under **Post-merge closure workstream** above; never recreate the source ref merely to close bookkeeping;
- when actual merge-result metadata was unknowable pre-merge, use a closure-only target-side commit/PR to reconcile manifest `status/result/pr`, selected Task Board final checkpoint/result/handoff pointers and other required terminal bookkeeping without changing the accepted implementation subject;
- read back the reconciled target and verify every unique referenced workstream-owned artifact required for terminal recovery;
- keep manifest `branch` and Task Board `execution_ref.branch` as original provenance whether or not the ref still exists.

Once that readback is GREEN and no Card/Research/review/integration obligation remains, terminal recovery no longer depends on the source branch.

### Fallback `branch_cleanup` lifecycle

The manifest-local `branch_cleanup` block is activated only when a surviving merged branch or terminal unmerged branch needs later physical cleanup.

For `state: safe_to_delete`:
- `ref` MUST equal the original manifest `branch`;
- `verified_head` MUST be the exact current HEAD re-read when terminal safety was proven;
- `evidence` MUST point to durable terminal-safety proof independent of the source ref;
- no live Card, Research, review, stacked-dependency or integration obligation may remain for that ref;
- a closed PR by itself is never sufficient.

Before a cleanup-capable actor deletes a `safe_to_delete` ref, re-read it. If the ref exists at a different HEAD than `verified_head`, the readiness is stale: do not delete, clear/reconcile the cleanup readiness, and repeat terminal-safety validation. Never force-update, force-rename or create a second ref to manufacture a match.

After physical deletion, `state: deleted` may be recorded only from durable state independent of the deleted ref and only after readback proves the exact ref is absent. Preserve the original `ref`, last verified HEAD and evidence/provenance.

If GitHub already removed a merged head automatically, the fallback lifecycle need not be activated merely to mirror that normal success.

### Terminal unmerged branches

A branch intentionally closed/superseded without final-target merge may become `safe_to_delete` only when:
- the workstream has explicit durable terminal closure;
- all unique closure/recovery/history needed after deletion is preserved independently of the source ref;
- no live workstream obligation remains;
- exact current ref/head has been re-read and verified.

When project-repository durability is required, persist a **closure-only namespaced workstream package** on the integration target (or another exact accepted durable project ref) before `safe_to_delete`. That package may contain manifest/Task Board/Card/evidence/history needed for recovery, but MUST NOT integrate rejected/superseded implementation content merely to preserve metadata. The target-side package, not a soon-to-be-deleted source-only copy, owns the durable cleanup marker.

Workstream terminal state remains durable history unless a later explicit archival policy defines a different lifecycle. Do not collapse completed/closed workstream state into the root legacy/default Task Board or a project-global mutable registry.

## Recovery invariant

A branch-isolated intake/implementation/review/recovery obligation is recoverable from:
- current workflow main;
- project `PROJECT.md`;
- for ordinary pre-integration non-terminal work, the exact workstream branch;
- for a successful merge whose closure is not yet terminal, the exact target-side package carried by that merge plus immutable PR/merge evidence;
- the exact workstream manifest;
- the exact manifest-pointed intake record when `intake.state: active`;
- the manifest-selected Task Board when implementation exists;
- exact authority/evidence/review pointers;
- for an integrated terminal `done` workstream after source-branch deletion, the target-side durable workstream package plus exact manifest `result`/integration evidence;
- for a terminal unmerged cleanup history after source-branch deletion, the exact durable closure package + `branch_cleanup` evidence independent of that ref.

Previous chat narrative is never required.

For the legacy/default mode, existing `PROJECT.md` + `implementation/TASK_BOARD.yaml` recovery remains unchanged.

## Foreign-policy boundary

Do not import:
- legacy bounded-parallel lanes;
- mixed-policy Capability Gate routing;
- Codex orchestration/worker semantics.

This contract only scopes ChatGPT-only state selection and seriality.
