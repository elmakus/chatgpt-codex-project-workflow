# Master Plan — Codex orchestration recovery after context loss

Plan revision: CCOR-P1
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
3. Reconcile `workflow/codex_only/WORKSTREAMS.md` so this block is workstream-local routing/recovery metadata, available before Task Board creation and never mirrored globally.
4. Narrow `workflow/codex_only/STATE.md` wording that currently forbids all `profile` persistence: concrete worker/session/model-instance/runtime lifecycle identity remains forbidden, but opaque policy/profile selection is allowed only in manifest `orchestration`.

### Planned work package B — Recovery and dispatch wiring

1. Update `workflow/codex_only/RECOVERY.md` so transcript/context loss reconstructs:
   - current obligation from canonical project state;
   - manifest orchestration binding;
   - current-context latch as absent/uncertain until a successful runtime re-bind.
2. Update `workflow/codex_only/ROUTER.md` with a conditional kernel load/re-bind rule at reconstruction/uncertainty boundaries, not on every role transition.
3. Gate every actual Codex-managed worker dispatch path through the kernel without copying runtime role maps:
   - Executor/worker launch in `workflow/codex_only/EXECUTION.md`;
   - independent Tester launch/replacement in `workflow/codex_only/REVIEW.md`;
   - independent plan-review Tester launch in `workflow/codex_only/PLAN_REVIEW.md`;
   - bounded parallel runtime launch in `workflow/codex_only/EXECUTION_PREP.md`.
4. Keep `workflow/codex/CODEX_ORCHESTRATION.md` authoritative for the Project Workflow ↔ `codex_workflow` boundary, but make explicit that Project Workflow owns durable policy selection + current-context re-bind requirement while runtime owns policy interpretation and concrete role→harness/model realization.
5. Reconcile `prompts/CODEX_START.md` / bundled Project Workflow skill only if required so a true recovery entry can discover the kernel through the canonical router rather than duplicating its contents.

### Planned work package C — Regression and documentation

1. Add a focused contract test (prefer a new `tests/test_codex_only_orchestration_recovery_contract.py`) proving:
   - the manifest template contains only the permitted binding fields;
   - same-version reconstruction cannot use durable fingerprint/binding as the current-context latch;
   - reconstruction/uncertainty requires kernel re-bind before Tester/Executor dispatch;
   - missing/stale/unresolvable binding fails closed and cannot silently fall back to another harness;
   - fingerprint drift forces policy re-resolution;
   - concrete worker/session/model-instance identity remains forbidden;
   - review requirement/subject, ownership, execution policy and stop conditions remain canonical-owner state;
   - concrete role→harness/model mapping remains `codex_workflow`-owned;
   - `chatgpt_only` Context Health and routing remain unchanged.
2. Keep existing `tests/test_codex_only_continuous_orchestration_contract.py` GREEN, proving the new recovery boundary does not become a user-facing hygiene stop.
3. Update README/CHANGELOG only where needed to make the new recovery boundary and responsibility split discoverable without teaching runtime-specific mappings.

### Acceptance

- A selected branch-first `codex_only` manifest can durably recover the opaque active runtime owner/policy selection with optional contract fingerprint.
- No Task Board, Task Card, root `PROJECT.md` or global registry mirrors that selection.
- Current-context readiness is explicitly non-durable and cannot be inferred from durable binding/fingerprint evidence.
- After context reconstruction or uncertainty, Main must re-bind before the first Executor/Tester/parallel worker dispatch even when the runtime fingerprint is unchanged.
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

- Static contract assertions over kernel, manifest template, Workstreams, State, Recovery, Router, Execution, Review, Plan Review, Execution Prep and orchestration boundary.
- Negative assertions against durable worker/session/model-instance fields and against duplicated concrete role→harness mappings.
- Same-version and changed-fingerprint reconstruction scenarios encoded as explicit contract tests.
- Existing continuous-orchestration regression suite remains GREEN.
- Run targeted tests first, then the full repository Python unittest suite.

### JIT / implementation boundary

Execution Prep should normally realize M01 as a small serial set of bounded Cards:

1. schema + kernel;
2. recovery/dispatch wiring;
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
- Strategic ambiguity: none remaining.
- Migration/data risk: low; workflow-contract/schema evolution only, with historical/default migration governed by existing Recovery.
- User/deployment authorization gate: none for repository edits/tests/PR.
- Independent plan review: RECOMMENDED because this changes recovery and worker-dispatch safety semantics across the Project Workflow/runtime boundary.
