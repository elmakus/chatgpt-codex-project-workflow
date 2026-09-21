# Cross-cutting audit — common-preexecution-core@R1

Date: 2026-09-21
Status: Brainstorming evidence
Production authority: none
Audited baseline: current `main`
Audited areas: ROUTER / RECOVERY / WORKSTREAMS / CLOSE / state+templates / contract tests

## Executive finding

The current fixed-policy trees contain substantially more duplicated project semantics than genuine policy semantics.

The target V2 should use **one common semantic router/state machine plus thin runtime/surface realization adapters**.

Runtime/product identity must not select a different Project Workflow lifecycle schema.

The same durable workstream must remain recoverable/continuable across supported runtimes at safe boundaries.

## 1. Router audit

### Common semantics already duplicated

Both fixed routers implement the same high-level durable routing priorities:

- resolve exact branch-isolated workstream before mutable state;
- validate manifest ↔ Task Board binding;
- resume active Intake;
- prioritize active review obligations;
- preserve implementation/recovery Research ownership;
- classify RED before unrelated work;
- finalize exact GREEN subjects deterministically;
- enforce final-integration review before Close;
- recover post-merge/terminal workstream state;
- preserve pre-execution Research / plan-review / exploratory locators;
- continue deterministic authorized work until a real stop.

The current duplicated router trees are therefore not justified as two semantic routers.

### Genuine surface/runtime differences

ChatGPT currently adds:
- context-health evaluation at safe boundaries;
- fresh normal-ChatGPT handoff when independent context cannot be realized inside the current chat;
- a user-facing STOP when the current chat produced the exact subject that now needs independent review.

Codex currently adds:
- runtime delegation through `codex_workflow`;
- no Project Workflow context-hygiene stop;
- current orchestration binding/re-bind machinery.

Only the first two categories are realization/topology differences. The durable routing priority is common.

### Target

Create one common semantic router.

Runtime/surface adapters may influence only:
- how an independent-context obligation is realized;
- how execution work is directly performed/delegated/parallelized;
- whether a non-semantic context-hygiene handoff is desirable;
- user-facing handoff mechanics.

They must not own a separate obligation ordering or Project Workflow state model.

## 2. Recovery audit

### Common recovery semantics

Both policies already share:
- branch-first workstream identity;
- historical root/default migration-before-mutation;
- manifest/Task Board binding validation;
- review and Research recovery;
- RED/GREEN deterministic reconciliation;
- terminal target-side package recovery;
- fail-closed behavior for inconsistent durable state.

### Current divergence

ChatGPT recovery assumes one serial in-progress Card.

Codex recovery has a detailed policy-local batch state machine and concrete role vocabulary.

The proposed common `active_execution` primitive subsumes both:
- one member = ordinary serial execution;
- multiple members = bounded concurrent execution;
- runtime capability decides realization;
- durable member states define safe continuation/takeover.

Target common execution-set shape remains:

```yaml
active_execution:
  id: X01
  state: prepared | active | transfer_ready
  base_ref: <exact durable base>
  reconciliation_order: [T01, T02]
  members:
    - card_id: T01
      state: prepared | active | quiesced | result_ready | reconciled | blocked
      checkpoint_ref: null
      result_ref: null
      canonical_result_ref: null
      evidence: null
```

Concrete worker/session/model/worktree identity is forbidden canonical state.

### Authoritative-state entry gate

Live test L plus this audit support making the following common precondition mandatory on new-context/takeover/recovery entry:

```text
resolve exact workstream + authoritative branch/ref
-> refresh authoritative durable source
-> establish exact current authoritative head
-> reconcile/validate local state
-> read canonical durable workflow state
-> route
```

Expected-base/CAS remains the publication guard.

No stronger lease/fencing primitive is currently justified. Explicit quiescence/transfer state + authoritative refresh + expected-base/CAS is sufficient for the currently evidenced failure modes. Reopen only if V2 implementation/recovery testing demonstrates a concrete gap.

### Codex orchestration binding

The durable manifest `orchestration.runtime_owner/policy_ref/contract_fingerprint` and current-context latch are V1 runtime-policy machinery.

Under the accepted one-fixed-runtime/capability-first target:
- remove this block from V2 Project Workflow durable state;
- runtime ownership/profile/model/worker catalog stays runtime-owned;
- if a concrete required capability cannot be realized, persist the semantic blocker/obligation rather than a runtime policy selection;
- future need for multiple intentionally selectable runtime profiles would require a new accepted design decision.

## 3. Workstreams audit

### Common workstream semantics

The following are policy-neutral and should have one common contract:
- stable workstream identity and branch provenance;
- Intake lifecycle pointer;
- locator-only exploratory / pre-execution Research / plan-review routing;
- manifest ↔ Task Board binding;
- no mutable global registry;
- stacked dependency semantics;
- integration refresh;
- final-target durable package;
- terminal recovery after source branch deletion;
- workstream final-integration review ownership.

### Branch cleanup reconciliation

V1 contains two intentionally different historical solutions:

- ChatGPT persists optional `branch_cleanup: safe_to_delete | deleted` because its connector may not be able to delete refs.
- Codex deliberately avoids a cleanup lifecycle when authenticated `gh` can delete the exact terminal-unmerged branch directly and recovery can derive cleanup from terminal durable state + branch existence.

V2 should preserve both behaviors through one capability-first common rule:

1. terminal safety and target-side durable recovery package are common prerequisites;
2. if the source branch is already absent, cleanup is complete;
3. if the branch survives and the active runtime can safely delete it:
   - re-read exact branch HEAD;
   - verify terminal-safety evidence;
   - delete the exact manifest branch;
   - read back absence;
4. if physical deletion is currently unavailable:
   - persist optional common fallback `branch_cleanup.state: safe_to_delete` with exact ref, verified HEAD and terminal-safety evidence;
   - a later cleanup-capable context may delete only if current HEAD still matches; otherwise revalidate;
5. never create alias/delete-marker refs;
6. cleanup state is workstream lifecycle state, never worker/session state.

This preserves both previously accepted behaviors without policy-specific workflow trees.

## 4. Review model audit

### Card/milestone drift

ChatGPT active Task Board still uses single mutable:
- `review_state`
- `review_subject`
- `review_evidence`.

Codex already uses append-only attempts but persists semantic role labels such as `implementation_owner_role: executor` and `reviewer_role: tester`.

Live tests J/K/M support one neutral append-only model with no concrete role names.

### Workstream final-integration drift

Both manifest templates still use one mutable:
- `review.state`
- `review.subject`
- `review.evidence`
- `review.covered_by`.

This must be reconciled with the append-only model rather than retained as a second lifecycle.

### Target generic review gate

Use the same attempt structure for Card, milestone and workstream final-integration gates:

```yaml
review:
  requirement: REQUIRED | RECOMMENDED | none
  current_attempt: R02
  attempts:
    - id: R01
      mode: independent_review | coverage_reuse
      state: pending | in_progress | green | red
      subject: <exact immutable reviewed subject>
      evidence: <semantic-only evidence>
      independence:
        requirement: independent_context
        realization_state: resolve_independent_context | awaiting_independent_context | independent_context_active | satisfied
        evidence: <semantic-only evidence>
      covered_by: null
```

Rules:
- one attempt = one immutable subject;
- changed subject appends a new attempt;
- prior attempts remain immutable/addressable;
- `independent_review` uses the normal independent-context lifecycle;
- `coverage_reuse` is legal only for final-integration gates and is created as a terminal GREEN attempt when an exact stronger prior independent verdict covers the identical final subject + acceptance surface;
- a coverage-reuse attempt stores exact `covered_by` and semantic coverage evidence; it does not pretend to run a new reviewer and does not need a new independent-context realization;
- target movement alone does not append a new review attempt when workstream-owned content/behavior and acceptance surface are unchanged and refreshed compatibility verification remains GREEN;
- integration-target refresh evidence stays separate from immutable review-attempt history.

Concrete product/worker/model/session/invocation/worktree identity is forbidden canonical review evidence.

## 5. Close audit

Milestone/workstream Close is predominantly common:
- acceptance;
- integration refresh;
- final-review freeze/reuse;
- publication/PR verification;
- target-side closure package;
- branch provenance;
- automatic next approved milestone;
- explicit deployment/live-write gates.

Policy-specific lines about `Tester`, fresh ChatGPT review stops or Codex pre-dispatch gates are realization mechanics and move out of common Close.

Common Close should:
1. freeze/consume semantic review obligations;
2. return to the common router;
3. let the realization adapter satisfy independent-context needs;
4. continue automatically after GREEN when no real stop exists.

## 6. Template/schema audit

### V1 problem

There are currently two active workstream Task Board schemas:
- ChatGPT serial/single-review-state shape;
- Codex append-only-review + parallel batch shape.

There are also two workstream manifest templates, with Codex-only orchestration binding and ChatGPT-only cleanup fallback.

### V2 target

One common `WORKSTREAM_TEMPLATE.yaml`:
- identity/provenance;
- parent dependency;
- Intake;
- routing locators;
- Task Board locator;
- accepted authority refs;
- generic append-only final-integration review gate;
- optional capability-fallback branch cleanup;
- PR/result.

No durable runtime-policy binding.

One common `WORKSTREAM_TASK_BOARD_TEMPLATE.yaml`:
- workstream binding;
- plan/milestone state;
- implementation/recovery Research pointer;
- Cards/milestones with generic append-only review attempts;
- neutral `active_execution`;
- no product/worker/model/session/worktree identity.

Legacy policy-local templates remain read-only migration input until migration support can be removed.

## 7. Test audit

Current tests encode V1 policy duplication and must not simply be copied into V2.

### Convert to common semantic tests

Merge/rewrite coverage currently split across:
- `test_chatgpt_only_branch_first_execution_state_contract.py`
- `test_codex_only_branch_first_execution_state_contract.py`
- `test_codex_only_branch_first_preexecution_contract.py`
- `test_branch_first_integrated_closure_contract.py`

into common tests for:
- branch-first manifest/Task Board ownership;
- common locator lifecycle;
- authoritative refresh before routing;
- generic append-only review attempts;
- final-integration coverage-reuse attempts;
- active_execution serial + multi-member recovery;
- target refresh;
- terminal durable package;
- capability-first branch cleanup fallback.

### Keep thin realization/surface tests

Keep/rewrite small adapter tests for:
- ChatGPT context-health and fresh-context handoff behavior;
- Codex/runtime delegation boundary and no Project Workflow-owned worker catalog;
- capability-first independent-context realization.

`test_codex_only_orchestration_recovery_contract.py` currently locks the durable orchestration binding and should be replaced with tests proving the opposite V2 boundary: no runtime-policy binding in Project Workflow state and runtime reconstruction remains outside common state.

`test_codex_only_continuous_orchestration_contract.py` expresses an important compatibility behavior but should move to V2 topology validation together with deferred N-CAPABLE/N-CHATGPT rather than serve as proof of the new implementation before V2 exists.

### Required V2 validation scenarios

Carry forward:
- L — authoritative stale-state refresh;
- M — semantic-only independent review evidence;
- N-CAPABLE — one-shot deterministic orchestration;
- N-CHATGPT — RED same-chat correction / fresh re-review / GREEN same-chat continuation;
- cross-runtime takeover matrix F/G/H/I/J;
- cleanup with delete capability;
- cleanup fallback without delete capability;
- final-integration exact coverage reuse;
- target movement preserving GREEN only when subject/acceptance remain unchanged.

## 8. Composition decision

Chosen Brainstorming direction:

### One semantic core, not policy-local forwarders per stage

Direct semantic authority lives in `workflow/common/*`.

Do not keep near-complete `chatgpt_only/*` and `codex_only/*` forwarders for every lifecycle stage.

Retain only thin runtime/surface integration contracts where behavior genuinely differs, for example:
- ChatGPT context-health / fresh-chat user handoff surface;
- Codex runtime orchestration bridge;
- generic capability-realization contract.

These adapters may realize obligations but may not redefine lifecycle semantics, route priority or state schema.

### Execution-policy migration

V2 new work should not require a durable `execution_policy: chatgpt_only | codex_only` to choose Project Workflow semantics.

The active runtime/surface realizes the same common obligations according to available capabilities.

This is required for the target property that one durable workstream can move between supported runtimes at safe boundaries without a policy migration.

Existing project `execution_policy` remains readable migration input during V2 transition but should not select a different semantic state machine.

## 9. Migration shape

Recommended staged migration:

1. Define common V2 schemas/contracts without switching production routing.
2. Add common state migration/readers for existing ChatGPT/Codex workstream manifests and Task Boards.
3. Convert pre-execution semantic modules to common.
4. Convert review/state/execution-prep/recovery semantics to the common attempt + active_execution model.
5. Convert Workstreams/Close to common, including cleanup capability fallback.
6. Switch root routing to common semantic router + thin runtime/surface adapters.
7. Run V2 validation matrix, including deferred N.
8. Only after parity is proven, retire policy-local semantic copies and old orchestration-binding state for new work.
9. Preserve bounded legacy read/migration support until all active workstreams are migrated/terminal.

Do not perform an in-place blind schema rewrite of active work without exact migration/recovery evidence.

## 10. Material questions after audit

No material architecture question remains from the audited surfaces.

The following are implementation-detail choices for Definition/Planning rather than unresolved Brainstorming product choices:
- exact filenames/module split inside `workflow/common/*`;
- exact migration helper/test file names;
- exact normalized evidence key names, provided the semantic-only boundary is preserved.

Deferred N remains post-implementation V2 validation and does not block Definition readiness.
