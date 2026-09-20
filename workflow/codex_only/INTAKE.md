# Codex-only Intake

This contract owns managed-change intake for new branch-isolated Codex-only workstreams. Explicit markers are shortcuts; clear natural-language authorization for a new managed repository change is also a first-class entry.

It applies only after root routing selected `execution_policy: codex_only`.

## Entry directives

The explicit operator directives are:

- `#issue <problem>` — diagnose/classify a problem and create or recover an issue workstream;
- `#feature <goal>` — create or recover a feature workstream and enter discovery.

A third first-class entry form is clear natural-language authorization to implement, apply or adopt a **new managed repository change** without a marker; it creates or recovers a neutral `change` workstream.

`#grill` is explicitly **not** an Intake directive. It may only force the grilling interaction method after the router has resolved an already active Brainstorming scope; it never creates or recovers a workstream or exploratory scope.

Treat a marker as an intake directive only when the current user request intentionally uses it as an operator command. A quoted marker, code/example text, documentation discussion, or incidental mention is not an intake directive.

Read-only inspect/compare/analyze requests do not create a workstream merely because they may reveal a possible change. They remain branch-free until the user clearly authorizes repository/project mutation. When that authorization arrives without `#issue` or `#feature`, use neutral `kind: change`; do not guess a narrower classification.

An explicit marker selects `issue` or `feature` even when the same request also contains ordinary implementation language. If one request intentionally supplies conflicting `#issue` and `#feature` directives for the same new work and the intended kind cannot be determined, do not guess; request only the smallest clarification.

The intake trigger selects the **entry route only**. After intake has durably established the workstream and downstream state, return to `workflow/codex_only/ROUTER.md`. The trigger is not a permanent session-scope boundary.

## Precedence

A current intake trigger — explicit `#issue` / `#feature` or clear natural-language authorization for a new managed change — is evaluated before ordinary implementation/review route selection for whatever unrelated default/workstream state happened to be active before the request.

Reason: a new independent workstream must not be blocked merely because another unrelated workstream has an `in_progress` Card, pending review or other mutable state.

This precedence does not authorize mutation of unrelated state. Intake discovers relevant branches/PRs/manifests only far enough to classify identity, base/dependency and conflicts. It must not adopt another workstream's Task Board as the new workstream's mutable state.

Generic natural-language precedence applies only to a **new** managed change, not to an exact continuation/handoff already bound to an existing workstream/PR/manifest. Read-only requests without change authorization leave normal router precedence unchanged. An already-created workstream whose manifest records active intake is recovered through that durable intake state.

## Durable intake state

A branch-isolated intake uses:

- `implementation/workstreams/<workstream-id>/WORKSTREAM.yaml` for durable identity/routing and coarse intake lifecycle;
- `implementation/workstreams/<workstream-id>/INTAKE.md` for the durable intake scope/findings/classification;
- the workstream Task Board only when implementation state is actually created later.

The manifest owns:

```yaml
intake:
  state: active | complete | null
  record: implementation/workstreams/<workstream-id>/INTAKE.md | null
```

This is workstream routing/lifecycle metadata, not Card/milestone execution state. Do not copy Card status, Card review or execution result fields into the manifest.

The intake record should contain only durable material needed to recover the intake and downstream choice, including as applicable:

- exact workstream ID and intake kind, matching the selected manifest;
- original operator intent or a faithful bounded scope statement;
- reproduction/diagnostic evidence references;
- discovered relevant branch/PR/workstream references;
- selected integration target and exact base;
- independent versus stacked classification and rationale;
- parent workstream/branch when stacked;
- chosen path classification and exact `next_route` when the downstream route has a named recovery entry;
- any unresolved evidence/gate;
- exact durable artifact that owns the next route once intake completes, or for qualified micro-fix the exact completed Intake record itself as the pre-Task-Board continuation anchor.

Do not use chat history as the only copy of these facts.

## Workstream identity and naming

Identity must be stable after creation.

For an intake-created workstream:

- issue ID: `issue-<slug>`;
- feature ID: `feature-<slug>`;
- generic change ID: `change-<slug>`;
- issue branch: `fix/<slug>`;
- feature branch: `feat/<slug>`;
- generic change branch: `work/<slug>`.

`<slug>` is a short lowercase hyphenated identifier derived from the durable subject. Use ASCII letters/digits/hyphens where practical, collapse repeated separators, and keep it concise enough to remain readable in branch names.

Collision handling is deterministic:

1. discover existing relevant branch names and workstream IDs before creation;
2. if the exact discovered branch/manifest is already the same durable workstream, recover it instead of creating another lane;
3. if the deterministic candidate branch exists but has no coherent matching manifest, or its manifest is missing/inconsistent with that branch/workstream identity, fail closed to Recovery; normal Intake must not claim, overwrite or silently suffix past an unresolved orphan/inconsistent candidate;
4. if the candidate ID or branch is coherently owned by different durable work, append the smallest available numeric suffix (`-2`, `-3`, ...) to the slug and use the same suffixed slug for both ID and branch;
5. never recycle an existing durable workstream ID merely because that workstream is done/superseded.

A stable workstream ID is not inferred from a branch name alone after creation; the manifest remains the identity authority.

## Common intake flow

1. Recover the exact repository and default/current integration target.
2. Detect whether the request already targets an existing exact workstream through a durable locator such as branch, workstream ID, manifest or PR. If yes, recover that workstream instead of creating a duplicate. Resume its durable active intake from the recorded stage; do not replay already-completed discovery/diagnosis merely to satisfy the new-workstream sequence below.
3. For a genuinely new intake, perform the route-specific **pre-creation discovery/diagnosis** required by the Issue, Feature or Generic managed-change section below. This step is read-only and must establish only the evidence needed for durable subject/identity plus independent-versus-stacked base classification before a new base/branch is chosen.
4. Choose the exact integration target and base under **Base and dependency classification** below using that route-specific evidence.
5. Choose a stable workstream ID/branch under **Workstream identity and naming**.
6. Create the branch from the selected base. Steps 1–5 are read-only: no change-specific durable Project Workflow artifact may be authored before this branch exists.
7. Persist the first change-specific durable Project Workflow state — the workstream manifest plus `INTAKE.md` with `intake.state: active` — on that created branch before any implementation mutation.
8. Immediately after the manifest exists, establish its usable orchestration binding before any policy-dependent worker realization: through the active runtime owner and the initial-establishment rule in `workflow/codex/CODEX_ORCHESTRATION.md`, resolve the currently selected opaque policy/profile and persist `runtime_owner + policy_ref` plus optional `contract_fingerprint`. Read back the manifest. If resolution/readback fails, keep Intake active and fail closed; do not select another harness or invent a policy reference.
9. Perform the route-specific **post-creation classification/materialization** below.
10. Before setting `intake.state: complete`, require the usable read-back orchestration binding and materialize the canonical durable state required by the chosen downstream route so recovery never depends on the just-finished chat.
11. Set intake complete, persist the final intake classification/result, return to the router and continue through the normal selected route.

Branch creation itself is not implementation mutation. If branch creation succeeds but the manifest/intake record write fails, do not continue normal Intake or start implementation. Route the deterministic orphan branch to Recovery; Recovery verifies provenance/conflicting state and may idempotently complete or abandon the partial intake setup. Likewise, if Intake discovers the deterministic candidate branch already exists without a coherent matching manifest, route to Recovery rather than guessing ownership or creating a duplicate.

## Base and dependency classification

Default to the repository's normal integration target for independent work.

Use an unmerged parent workstream branch only when the new work genuinely requires parent-only state to reproduce, define or implement the change.

A parent dependency is justified by concrete evidence such as:

- the relevant behavior/interface exists only on the unmerged parent;
- the issue cannot be reproduced or fixed correctly without parent-only changes;
- the feature explicitly builds on an accepted parent-only contract.

The following are **not** sufficient by themselves:

- the parent exposed or revealed the symptom;
- likely file overlap;
- convenience;
- avoiding a future rebase.

For stacked work, record `parent_workstream`, `parent_branch`, `parent_dependency`, `base_ref` and `integration_target` in the manifest. `parent_dependency` is a concise routing/integration statement of the parent-only state the child requires; the Intake record keeps the fuller evidence/rationale.

For independent work, parent fields and `parent_dependency` remain null and the branch is created from the normal integration target/base.

Intake owns this initial base/dependency classification. Final stacked integration, parent-satisfaction and target-refresh behavior is governed by `workflow/codex_only/WORKSTREAMS.md` plus `CLOSE.md`; Intake must not pre-empt those gates.

## Generic managed-change intake

A clear natural-language request to implement, apply or adopt a **new managed repository change** without `#issue` or `#feature` enters Intake as `kind: change`.

For a genuinely new generic change, complete these **read-only** steps before Common intake flow step 4 chooses a base:

1. derive a bounded durable subject and `<slug>` from the authorized change without guessing issue-versus-feature classification;
2. discover exact matching workstream/branch/PR identity and only the source/dependency evidence needed to distinguish the normal integration target from a real parent-only stacked dependency;
3. if the deterministic `work/<slug>` candidate exists without a coherent matching manifest, fail closed to Recovery rather than claiming it or choosing a suffix merely to bypass the inconsistency.

After Common intake flow step 8 has created/recovered the neutral workstream, persisted durable active intake state and established/read back its usable orchestration binding:

4. record intake kind `change` and preserve the user's authorized bounded scope;
5. classify the smallest legal downstream route from that scope under the normal policy contracts, without reclassifying the workstream to `issue` or `feature` merely to reuse a lifecycle path;
6. materialize that route's canonical durable recovery anchor before marking intake complete, then return to the router.

Generic Intake does not bypass any normal Definition-promotion, Research, Planning, review, authorization or execution gate owned by the selected downstream route.

## Issue intake

For a genuinely new `#issue`, complete these **before Common intake flow step 4 chooses a base**:

1. Establish the problem on the intended baseline when practical. Prefer reproduction, a failing check, exact source/runtime evidence, or another concrete diagnostic signal.
2. Discover relevant active branches/PRs/workstreams only far enough to decide whether the problem/fix depends on unmerged parent-only state.
3. Classify the issue as independent versus stacked from that evidence and supply the exact base decision to the common flow. Do not create the new workstream branch before this classification.

After Common intake flow step 8 has created/recovered the issue workstream, persisted durable active intake state and established/read back its usable orchestration binding:

4. Determine whether the issue qualifies for the micro-fix path using the accepted R6 criteria:
   - root cause and intended behavior are concrete;
   - change is bounded and low strategic risk;
   - no accepted requirement/architecture/product decision must change;
   - acceptance can be stated directly;
   - no substantial migration/deployment strategy is needed.
5. If all micro-fix criteria hold, record `path: micro_fix`, persist the evidence for each qualifying criterion, and record `next_route: execution_prep:micro_fix`. The completed Intake record plus selected manifest are the durable starting state for `workflow/codex_only/MICRO_FIX.md`; do not create a Master Plan merely to leave Intake.
6. Otherwise record the smallest normal route justified by evidence:
   - Research when material evidence is still missing;
   - Project Definition when accepted product/system intent must be established/changed;
   - Planning when approved Definition remains valid but execution strategy/milestone organization is required;
   - Execution Prep only when accepted authority/plan already exists and the work is a bounded legal continuation.
7. Materialize the selected route's canonical durable starting state before marking intake complete. For `path: micro_fix`, the exact completed Intake classification/qualification record plus manifest is sufficient to route deterministically into micro-fix Execution Prep before a Task Board exists; Execution Prep owns creation of the bounded fix Card and selected workstream Task Board.
8. Return to the router.

An unrelated active workstream may continue independently. Intake must not modify that workstream merely because it exposed the symptom.

## Feature intake

For a genuinely new `#feature`, complete these **before Common intake flow step 4 chooses a base**:

1. Discover existing workstreams/PRs far enough to avoid duplicate identity and to determine whether the feature genuinely depends on parent-only state.
2. Classify the feature against the normal integration target versus a real stacked dependency and supply that exact base decision to the common flow.

After Common intake flow step 8 has created/recovered the feature workstream, persisted durable active intake state and established/read back its usable orchestration binding:

3. Preserve the existing exploratory lifecycle. Before marking intake complete, create/reconcile the exact canonical Brainstorming starting record/pointer required by the Codex-only Brainstorming contract on this workstream branch.
4. Initialize/retain Definition promotion authorization as `pending` with promotion subject `none` unless the user separately and explicitly authorizes promotion for the exact current brainstorming scope/revision under the normal router gate.
5. Do **not** interpret the `#feature` directive itself as Definition promotion authority.
6. Mark intake complete only after durable discovery state is recoverable, then return to the router. Normal Brainstorming/Research → explicit promotion → Definition → Planning semantics continue from there.

If feature discovery needs formal Research, enter it through the normal Brainstorming/Research contract after the durable exploratory starting state exists; intake does not invent a separate Research lifecycle.

## Recovery and idempotency

A fresh coordinating context can recover an active intake from:

- current workflow `main`;
- branch-local `PROJECT.md`;
- exact workstream branch;
- `WORKSTREAM.yaml`;
- manifest `intake.record`;
- relevant exact Git/PR/source/runtime evidence.

Previous chat narrative is not required.

When `intake.state: active`, resume Intake before interpreting later Task Board work for that same workstream.

When `intake.state: complete`, do not replay intake. Recover the canonical downstream artifact recorded/materialized by the completed intake and let the router select that route.

If a second chat explicitly targets the same exact branch/workstream while intake is active, it recovers that intake. It does not create a second lane inside the same workstream.

A deterministic candidate branch with a missing, malformed or identity-inconsistent manifest is not a valid reusable workstream and not an ordinary collision. Route to Recovery, preserve the branch, and resolve the partial-creation/provenance state before any change-specific write or alternate workstream creation.

If exact identity cannot be established from durable locators/evidence, do not merge two plausible workstreams based on fuzzy similarity. Preserve both and request the smallest clarification only when evidence cannot resolve the ambiguity.

## Scope boundaries

Intake owns entry/classification and the durable handoff into the selected downstream route.

It does not itself own:

- the complete micro-fix execution/review lifecycle — use `workflow/codex_only/MICRO_FIX.md` plus normal Execution Prep/Execution/Review/Recovery;
- branch-local execution/review/recovery state semantics after downstream materialization — use the normal selected-workstream modules;
- local worktree/equivalent isolation, stacked integration and target-refresh rules — `workflow/codex_only/WORKSTREAMS.md` + `CLOSE.md`;
- final user-facing handoff/template/migration/E2E closure — M05.

Intake must preserve downstream gates rather than pre-empt them.

## Foreign-policy boundary

Do not import:

- mixed-policy Capability Gate routing;
- legacy Codex orchestration as Project Workflow authority; concrete runtime worker mechanics remain owned by `codex_workflow`;
- legacy bounded-parallel lanes or scheduler state.

Codex Main remains the fixed Project Workflow coordinator after intake routes into normal `codex_only` execution; concrete Executor/Tester/Investigator realization remains owned by `codex_workflow`.
