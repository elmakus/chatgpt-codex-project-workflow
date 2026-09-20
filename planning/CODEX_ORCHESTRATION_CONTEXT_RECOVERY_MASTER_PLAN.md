# Master Plan — Codex orchestration recovery after context loss

Plan revision: CCOR-P2
Status: draft
Review requirement: RECOMMENDED

## Authority

- Requirements: `requirements/CODEX_ORCHESTRATION_CONTEXT_RECOVERY.md` R2
- Decision: `decisions/ADR_CODEX_ORCHESTRATION_POLICY_BINDING.md`
- Workstream: `issue-codex-compaction-routing-recovery`

## Goal

Make `codex_only` continuation recover both the current project obligation and the selected runtime-orchestration policy after context compaction/reconstruction, without duplicating `codex_workflow` internals and without a heavy workflow re-read.

The design must protect the primary same-version failure: a durable policy selection is not proof that it has been re-bound in the current coordinator context.

## Non-goals

- Implement `codex_workflow` role→harness enforcement.
- Encode Muse-specific role maps in Project Workflow.
- Persist worker/session/process/model-instance identity.
- Add a repository-global orchestration registry.
- Reintroduce a `codex_only` Context Health/FRESH user stop.
- Change `chatgpt_only` behavior.

## OpenSpec boundary

M01 is an OpenSpec candidate because it changes persistent manifest state plus reconstruction/re-bind semantics across the Project Workflow ↔ runtime boundary. Execution Prep should require the first implementation Card touching that contract to create/reconcile the JIT OpenSpec against current HEAD and the exact Card authority slice; do not freeze runtime role→harness mappings in that spec.

## M01 — Token-light orchestration recovery boundary

### Outcome

Branch-first `codex_only` workstreams durably carry only an opaque runtime-policy selection. A small conditional kernel requires a fresh current-context re-bind before the first policy-dependent dispatch after reconstruction/uncertainty and fails closed instead of falling back to a different harness. Existing project-owned review/authority/ownership/stop state remains in its current canonical owners.

### Requirement coverage

Owns CCOR-R1 through CCOR-R10.

### Planned work package A — Binding schema and kernel

1. Add `workflow/codex_only/ORCHESTRATION_KERNEL.md` as the single compact contract for:
   - durable binding fields;
   - deliberately non-durable current-context latch;
   - reconstruction/uncertainty/drift triggers;
   - bounded read set;
   - pre-dispatch re-bind/fail-closed rule;
   - canonical project-invariant pointers;
   - runtime ownership boundary.
2. Extend `workflow/codex_only/WORKSTREAM_TEMPLATE.yaml` with:
   ```yaml
   orchestration:
     runtime_owner: null
     policy_ref: null
     contract_fingerprint: null
   ```
3. Reconcile `workflow/codex_only/WORKSTREAMS.md` so this block is workstream-local routing/recovery metadata, available before Task Board creation and never mirrored globally. Define its lifecycle explicitly:
   - a newly created `codex_only` manifest may carry null orchestration fields only during initial materialization;
   - before Intake can complete for that workstream, and before any policy-dependent worker realization after the manifest exists, Main asks the runtime owner to resolve the currently selected opaque policy/profile and persists `runtime_owner + policy_ref` plus optional fingerprint;
   - a present binding with missing/unknown/contradictory required values is invalid and fails closed rather than selecting another harness.
4. Reconcile `workflow/codex_only/INTAKE.md` with that initialization rule without teaching Intake any role→harness mapping. Pre-creation read-only discovery remains branch-free; once the manifest exists, Intake cannot yield to a runtime worker path until the manifest binding is established.
5. Add a one-time branch-first schema-upgrade path in `workflow/codex_only/RECOVERY.md` for a selected pre-change manifest that has no `orchestration` block at all: resolve the current selected policy through the runtime owner, persist the new compact binding only after successful resolution, then continue. Distinguish this legacy field absence from an already-present but invalid binding, which remains fail-closed. Historical/default migration acquires the binding only after its new branch-isolated manifest exists.
6. Narrow `workflow/codex_only/STATE.md` wording that currently forbids all `profile` persistence: concrete worker/session/model-instance/runtime lifecycle identity remains forbidden, but opaque policy/profile selection is allowed only in manifest `orchestration`.

### Planned work package B — Recovery and dispatch wiring

1. Update `workflow/codex_only/RECOVERY.md` so transcript/context loss reconstructs:
   - current obligation from canonical project state;
   - manifest orchestration binding, including the one-time pre-schema migration above;
   - current-context latch as absent/uncertain until a successful runtime re-bind.
2. Update `workflow/codex_only/ROUTER.md` with a conditional kernel load/re-bind rule at reconstruction/uncertainty boundaries, not on every role transition.
3. Make `workflow/codex/CODEX_ORCHESTRATION.md` the generic pre-dispatch boundary: whenever any `codex_only` route asks the active runtime to realize or re-realize a policy-dependent worker/role, Main must satisfy the kernel binding+latch precondition first. This rule is role-agnostic and must not enumerate a concrete role→harness/model map.
4. Wire/audit every current route that can directly cause or permit runtime worker realization so it references that shared precondition rather than inventing local routing semantics:
   - Executor/member launch and retry in `workflow/codex_only/EXECUTION.md`;
   - independent Tester launch/replacement in `workflow/codex_only/REVIEW.md`;
   - independent plan-review Tester launch in `workflow/codex_only/PLAN_REVIEW.md`;
   - bounded parallel launch in `workflow/codex_only/EXECUTION_PREP.md`;
   - Investigator realization in `workflow/codex_only/RESEARCH.md`;
   - resume/replacement/re-realization paths in `workflow/codex_only/RECOVERY.md`;
   - audit `INTAKE.md`, `CLOSE.md` and other Codex-only routes for direct worker realization and add only the shared-kernel hook where such a dispatch actually exists. Routes that merely return to Router/Review/Execution must not duplicate the gate.
5. Keep the runtime boundary explicit: Project Workflow owns durable policy selection + current-context re-bind requirement; runtime owns policy interpretation, concrete role→harness/model realization and runtime-side enforcement.
6. Reconcile `prompts/CODEX_START.md` / bundled Project Workflow skill only if required so a true recovery entry can discover the kernel through the canonical router rather than duplicating its contents.

### Planned work package C — Regression and documentation

1. Add a focused contract test (prefer a new `tests/test_codex_only_orchestration_recovery_contract.py`) proving:
   - the manifest template contains only the permitted binding fields;
   - new selected workstreams establish a usable opaque binding before post-materialization policy-dependent worker dispatch;
   - a pre-change branch-first manifest with no orchestration block takes the bounded one-time migration path, while an already-present invalid/unknown binding fails closed;
   - same-version reconstruction cannot use durable fingerprint/binding as the current-context latch;
   - reconstruction/uncertainty requires kernel re-bind before Executor, Tester, Investigator and recovery re-realization paths;
   - missing/stale/unresolvable binding fails closed and cannot silently fall back to another harness;
   - fingerprint drift forces policy re-resolution;
   - concrete worker/session/model-instance identity remains forbidden;
   - review requirement/subject, ownership, execution policy and stop conditions remain canonical-owner state;
   - concrete role→harness/model mapping remains `codex_workflow`-owned and the generic gate does not become a duplicate role map;
   - `chatgpt_only` Context Health and routing remain unchanged.
2. Keep existing `tests/test_codex_only_continuous_orchestration_contract.py` GREEN, proving the new recovery boundary does not become a user-facing hygiene stop.
3. Update README/CHANGELOG only where needed to make the new recovery boundary and responsibility split discoverable without teaching runtime-specific mappings.

### Acceptance

- A selected branch-first `codex_only` manifest can durably recover the opaque active runtime owner/policy selection with optional contract fingerprint.
- New workstreams establish that binding deterministically before post-materialization policy-dependent worker realization; pre-schema branch-first manifests have a bounded one-time Recovery migration, while already-present invalid bindings fail closed.
- No Task Board, Task Card, root `PROJECT.md` or global registry mirrors that selection.
- Current-context readiness is explicitly non-durable and cannot be inferred from durable binding/fingerprint evidence.
- After context reconstruction or uncertainty, Main must re-bind before the first policy-dependent worker realization or re-realization — including Executor, Tester, Investigator and recovery retry paths — even when the runtime fingerprint is unchanged.
- Missing/stale/unresolvable binding is fail-closed; there is no silent native/internal harness fallback.
- Runtime contract drift triggers policy re-resolution before dispatch.
- Project Workflow contains no Muse-specific or other concrete role→harness map.
- Concrete worker/session/process/model-instance identity remains outside Project Workflow state.
- Existing independent-review, ownership, authority, Task Board/workstream binding and real-stop semantics remain canonically owned and recoverable.
- The bounded recovery read set is `PROJECT.md` + selected manifest + orchestration kernel + exact current obligation state; no full-tree or external-runtime-repository re-read is required.
- `codex_only` remains continuous with no Context Health/FRESH user stop.
- `chatgpt_only` behavior is unchanged.
- Focused and repository-wide contract tests are GREEN.

### Verification strategy

- Static contract assertions over kernel, manifest template, Workstreams, Intake, State, Recovery, Router, Execution, Review, Plan Review, Execution Prep, Research, relevant Close paths and the orchestration boundary.
- Negative assertions against durable worker/session/model-instance fields and against duplicated concrete role→harness mappings.
- Same-version and changed-fingerprint reconstruction scenarios encoded as explicit contract tests.
- Existing continuous-orchestration regression suite remains GREEN.
- Run targeted tests first, then the full repository Python unittest suite.

### JIT / implementation boundary

Execution Prep should normally realize M01 as a small serial set of bounded Cards:

1. schema + kernel + JIT OpenSpec for the persistent binding/re-bind contract;
2. binding lifecycle/migration + generic recovery/dispatch wiring;
3. regression/docs.

It may merge adjacent Cards when exact write scope remains reviewable. Do not parallelize modifications that share router/kernel/state contracts merely to reduce elapsed time.

If implementation proves that safe current-context detection requires a concrete `codex_workflow` mechanism or API that Project Workflow cannot specify opaquely, preserve this plan boundary and route that dependency to the separate runtime-side issue rather than importing runtime mechanics here.

## Planning audit

- Definition completeness: GREEN.
- Requirement coverage: CCOR-R1…R10 all owned by M01.
- Primary same-version compaction case: explicitly covered.
- Version/epoch drift: additive, not substituted for the primary case.
- Responsibility boundary: Project Workflow owns durable selection/re-bind gate; runtime owns mapping/enforcement.
- Token-cost constraint: satisfied by one small manifest block + conditional kernel + current-context latch; no recurring full re-read.
- OpenSpec boundary: M01 marked as a JIT OpenSpec candidate for persistent schema/state + cross-runtime contract; no runtime role map is frozen there.
- Strategic ambiguity: none remaining.
- Migration/data risk: low but explicit; historical/default migration remains governed by existing Recovery, and pre-change branch-first manifests receive a bounded one-time orchestration-block upgrade before dispatch.
- User/deployment authorization gate: none for repository edits/tests/PR.
- Independent plan review: RECOMMENDED because this changes recovery and worker-dispatch safety semantics across the Project Workflow/runtime boundary.
