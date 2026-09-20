# ADR — Persist a compact orchestration-policy binding for Codex recovery

Status: accepted
Date: 2026-09-20
Amended: 2026-09-20 — separate durable policy binding from non-durable current-context readiness

## Context

Current `codex_only` contracts make durable Project Workflow state sufficient to recover the next project obligation after coordinator/session/context loss. They intentionally keep concrete worker/session/model/profile lifecycle outside Project Workflow and delegate internal orchestration to `codex_workflow`.

That separation is too coarse for context recovery.

The project can durably know that the next obligation is an independent Tester review of one exact subject while Main no longer retains the transient fact that the active runtime policy was `muse-max` and that Tester dispatch must be realized through the Muse-backed runtime. Main can therefore recover **what** to do and still select the wrong harness for **how** to do it.

The failure exists without any workflow-version change. Runtime version/epoch drift is only an additional reason to revalidate the binding.

A full re-read of Project Workflow, Master Plan, Task Board, delegation/runtime contracts and external runtime source after every compaction would be safe but too expensive.

## Decision

Introduce a three-part, token-light recovery boundary for branch-first `codex_only` work.

### 1. Manifest-owned opaque orchestration binding

Selected branch-isolated `WORKSTREAM.yaml` owns a compact `orchestration` block representing the runtime policy that Main must re-bind before policy-dependent worker dispatch.

Normative shape:

```yaml
orchestration:
  runtime_owner: null
  policy_ref: null
  contract_fingerprint: null
```

- `runtime_owner` — opaque owner identifier such as `codex_workflow`;
- `policy_ref` — opaque selected orchestration/compute-policy reference such as a runtime profile name;
- `contract_fingerprint` — optional runtime-supplied version/epoch/fingerprint for stale-binding detection.

The exact role→harness/model mapping is not stored here. Concrete worker/session/process/model-instance identity remains forbidden.

When no stable fingerprint exists, the field may be null; reconstruction still requires a fresh re-bind of `runtime_owner + policy_ref`.

### 2. Non-durable current-context binding latch

A successful runtime re-bind establishes a conceptual `current_context_binding_valid` latch only for the current coordinator context.

The latch is intentionally **not durable** and carries no session/worker ID. Durable policy selection and a matching fingerprint never imply that the latch is present.

Whenever Main reconstructs from repository state, resumes after known context loss/compaction, or cannot positively establish that the current context already performed the re-bind, the latch is treated as absent. The next policy-dependent dispatch must re-bind first.

This split closes the same-version compaction failure: durable state tells Main **which policy to restore**, while absence of the transient latch tells Main **that restoration is still required now**.

### 3. Small Codex-only orchestration continuation kernel

Add one small static `workflow/codex_only/ORCHESTRATION_KERNEL.md` contract.

At a coordinator reconstruction/uncertainty boundary Main reads only:

1. root `PROJECT.md`;
2. selected `WORKSTREAM.yaml`;
3. `ORCHESTRATION_KERNEL.md`;
4. the exact canonical state record already required by the current obligation.

Before first policy-dependent dispatch, Main re-binds the manifest policy through the runtime owner and establishes the non-durable latch. Missing/stale/unresolvable binding fails closed to the normal runtime-blocker path. Main must not silently fall back to another worker harness.

After successful re-bind, ordinary continuation proceeds without repeatedly loading the kernel while the current-context latch remains positively established.

## Why the manifest owns the binding

The binding is workstream-local routing/recovery state:

- it is needed before a Task Board may exist;
- it survives Card/review transitions and coordinator replacement;
- it can differ between independent workstreams;
- root `PROJECT.md` would create a mutable global routing mirror;
- Task Board alone is too late for pre-execution recovery;
- transient runtime context alone reproduces the original failure.

## Canonical project invariants are not copied into the binding

The kernel is not a second state database. It requires Main to re-check existing canonical owners for:
- accepted execution policy;
- exact review subject/requirement;
- implementation/reviewer ownership separation;
- workstream/Task Board binding;
- deterministic continuation versus real stop.

Only the small runtime policy selection is new durable state.

## Runtime boundary

Project Workflow is authoritative for requiring/recovering the binding, current-context re-bind gate and fail-closed dispatch boundary.

`codex_workflow` or another active runtime remains authoritative for:
- interpreting `policy_ref`;
- concrete role→harness/model routing;
- worker/session lifecycle;
- runtime-side fail-closed validation;
- concrete resume/replacement mechanics.

This complements rather than duplicates runtime-side enforcement.

## Drift behavior

When `contract_fingerprint` is available and differs from the current runtime contract, the durable binding is stale. Main re-resolves the same selected policy under the current contract and refreshes the compact binding only after successful resolution.

A matching fingerprint never removes the same-version reconstruction requirement: after context loss the current-context latch is absent/uncertain and Main still re-binds.

## Consequences

- Context compaction cannot be treated as harmless solely because project Task Board/review state and a prior binding are durable.
- The steady-state cost remains small: one manifest block, one compact conditional kernel and one non-durable latch.
- Blanket wording that `profile` is never durable state must be narrowed to distinguish policy/profile **selection** from concrete model/worker/session **identity**.
- Existing canonical state owners remain unchanged.
- A separate `codex_workflow` issue can independently enforce role→harness routing at runtime.
