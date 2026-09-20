# ADR — Persist a compact orchestration-policy binding for Codex recovery

Status: accepted
Date: 2026-09-20

## Context

Current `codex_only` contracts make durable Project Workflow state sufficient to recover the next project obligation after coordinator/session/context loss. They intentionally keep concrete worker/session/model/profile lifecycle outside Project Workflow and delegate internal orchestration to `codex_workflow`.

That separation is too coarse for context recovery.

The project can durably know that the next obligation is, for example, an independent Tester review of one exact subject while Main no longer retains the transient fact that the active runtime policy was `muse-max` and that Tester dispatch must be realized through the Muse-backed runtime. In that state Main can recover **what** to do and still select the wrong harness for **how** to do it.

The failure exists without any workflow-version change. Runtime version/epoch drift is only an additional reason to revalidate the binding.

A full re-read of Project Workflow, Master Plan, Task Board, delegation/runtime contracts and external runtime source after every compaction would be safe but too expensive in context and latency.

## Decision

Introduce a two-part, token-light recovery boundary for branch-first `codex_only` work.

### 1. Manifest-owned opaque orchestration binding

The selected branch-isolated `WORKSTREAM.yaml` owns a compact `orchestration` block representing the runtime policy that Main must re-bind before policy-dependent worker dispatch.

The block is routing/recovery metadata, not worker lifecycle state. Its normative shape is:

```yaml
orchestration:
  runtime_owner: null
  policy_ref: null
  contract_fingerprint: null
  validation: null
```

Semantics:

- `runtime_owner` — opaque owner identifier such as `codex_workflow` or another active runtime owner;
- `policy_ref` — opaque selected orchestration/compute-policy reference such as a runtime profile name;
- `contract_fingerprint` — optional runtime-supplied version/epoch/fingerprint used to detect stale bindings;
- `validation` — compact durable evidence/pointer that the binding was successfully resolved for the current runtime contract.

The exact role→harness/model mapping is **not** stored here. Concrete worker/session/process identity remains forbidden.

When the active runtime does not expose a stable fingerprint, the field may be null; reconstruction still requires a fresh re-bind of the same `runtime_owner + policy_ref`.

### 2. Small Codex-only orchestration continuation kernel

Add one small static `workflow/codex_only/ORCHESTRATION_KERNEL.md` contract.

At a coordinator reconstruction boundary — including context loss/compaction when Main can no longer positively establish that the active binding is loaded and validated — Main reads only:

1. root `PROJECT.md`;
2. selected `WORKSTREAM.yaml`;
3. `ORCHESTRATION_KERNEL.md`;
4. the exact canonical state record already required by the current obligation.

Before the first policy-dependent dispatch, Main re-binds the manifest policy through the runtime owner. A missing/stale/unresolvable binding fails closed to the normal runtime-blocker path. Main must not silently fall back to another worker harness.

After successful re-bind, ordinary continuation proceeds without repeatedly loading the kernel until another reconstruction/uncertainty/drift boundary occurs.

## Why the manifest owns the binding

The binding is workstream-local routing/recovery state:

- it is needed before a Task Board may exist;
- it must survive Card/review transitions and coordinator replacement;
- it can differ between independent workstreams;
- storing it in root `PROJECT.md` would create a mutable global routing mirror and cross-workstream contention;
- storing it only in Task Board would fail pre-execution recovery;
- storing it only in transient runtime context reproduces the original failure.

## Canonical project invariants are not copied into the binding

The kernel does not become a second state database.

It requires Main to re-check the existing canonical owner for:
- accepted execution policy;
- exact review subject/requirement;
- implementation/reviewer ownership separation;
- workstream/Task Board binding;
- deterministic continuation versus real stop.

Only the small runtime policy binding is new durable state.

## Runtime boundary

Project Workflow remains authoritative for requiring/recovering the binding and for deciding that dispatch may not proceed without successful re-bind.

`codex_workflow` or another active runtime remains authoritative for:
- interpreting `policy_ref`;
- resolving concrete role→harness/model routing;
- worker/session lifecycle;
- runtime-side fail-closed validation;
- concrete resume/replacement mechanics.

This ADR therefore complements, rather than duplicates, runtime-side enforcement.

## Drift behavior

When `contract_fingerprint` is available and differs from the current runtime contract, the old validation is stale.

Main must re-resolve the same selected policy under the current contract. If successful it refreshes the compact binding/validation evidence; if not, it routes the normal concrete runtime blocker.

A matching fingerprint never removes the same-version reconstruction requirement: after context loss Main still re-binds because transient routing state may have been lost.

## Consequences

- Context compaction can no longer be treated as harmless solely because project Task Board/review state is durable.
- The steady-state context cost remains small: one manifest block plus one compact conditional kernel.
- Project Workflow's former blanket wording that `profile` is never durable state must be narrowed to distinguish policy/profile **selection** from concrete model/worker/session **identity**.
- Existing canonical state owners remain unchanged.
- The design provides an explicit integration point for the separate `codex_workflow` issue to enforce role→harness routing at runtime.
