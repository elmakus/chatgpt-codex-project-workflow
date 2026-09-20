# Codex-only Orchestration Continuation Kernel

This is the compact Project Workflow recovery contract for the **runtime-policy binding boundary** under `execution_policy: codex_only`.

It is intentionally small. It does not replace the normal route module, Task Board, review record, requirements/decisions or `codex_workflow` runtime instructions.

## 1. Durable binding

For branch-first managed work, the selected `WORKSTREAM.yaml` owns:

```yaml
orchestration:
  runtime_owner: <opaque-owner>
  policy_ref: <opaque-policy-or-profile-ref>
  contract_fingerprint: <opaque-runtime-contract-fingerprint-or-null>
```

A usable established binding requires `runtime_owner` and `policy_ref`. The fingerprint is optional.

The binding is policy **selection**, not concrete runtime identity. Never persist worker/session/process/model-instance/invocation/lease/resume/worktree identity or a concrete role→harness/model map here or elsewhere in Project Workflow state.

Do not mirror this binding into root `PROJECT.md`, Task Board, Task Cards or a repository-global registry.

## 2. Current-context binding latch

After the active runtime successfully resolves/re-binds the manifest `runtime_owner + policy_ref`, Main may treat a conceptual `current_context_binding_valid` latch as established **only in the current coordinator context**.

The latch:
- is non-durable and is never serialized;
- carries no worker/session/model identity;
- is absent/uncertain after known transcript/context loss or compaction, coordinator replacement, repository-only recovery, or whenever Main cannot positively establish that this current context already completed re-bind;
- is never inferred from the existence of a durable binding or from a matching `contract_fingerprint`.

Therefore same-version context reconstruction still requires re-bind before the first policy-dependent runtime realization.

## 3. Bounded reconstruction read set

At a reconstruction/uncertainty boundary, recover only:

1. root `PROJECT.md` for the accepted execution policy;
2. the exact selected branch-isolated `WORKSTREAM.yaml` for workstream identity/routing plus the orchestration binding;
3. this kernel;
4. only the exact canonical state record already required by the current obligation.

Then follow the canonical router/owning route. Do not load the whole Master Plan, all Task Cards, all workflow modules, every durable document or the external `codex_workflow` repository merely to recover the orchestration binding.

The current obligation still comes from its existing canonical owner. This kernel does not duplicate mutable review/Card/milestone state.

## 4. Pre-dispatch re-bind gate

Before any `codex_only` route asks the active runtime to **realize or re-realize a policy-dependent worker/role**, require:

1. a valid selected manifest orchestration binding;
2. no unresolved runtime-contract drift;
3. a positively established current-context binding latch.

If the latch is absent/uncertain, Main asks `runtime_owner` to resolve/re-bind the opaque `policy_ref` under the current runtime contract. Only successful re-bind establishes the latch for this coordinator context.

This gate is role-agnostic. Project Workflow does not enumerate or infer which concrete harness/model implements Executor, Tester, Investigator or any other runtime role.

## 5. Drift

When the runtime exposes a contract version/epoch/fingerprint and the current value differs from durable `contract_fingerprint`:

1. treat the durable binding as stale;
2. re-resolve the same selected opaque policy/profile through `runtime_owner` under the current runtime contract;
3. refresh the manifest binding/fingerprint only after successful resolution;
4. establish the non-durable current-context latch from that successful re-bind.

A matching fingerprint only means no detected contract drift. It never proves the current-context latch.

## 6. Fail-closed behavior

A missing, stale, contradictory or unresolvable binding does not authorize another harness.

When installed/enabled `codex_workflow` owns runtime orchestration, Main must not silently fall back to native/internal worker realization because transient routing context was lost.

If the bound policy cannot be re-established for a concrete required operation:
- preserve the accepted Project Workflow `execution_policy`;
- persist/route the normal concrete runtime blocker through the owning route/state;
- request user input only when the ordinary blocker contract actually reaches a real user-owned input/access/authorization boundary.

Schema-age handling is distinct:
- selected pre-schema branch-first manifests with **no `orchestration` block** use the bounded one-time Recovery upgrade defined by `RECOVERY.md`;
- a manifest where the block exists but required values are invalid does not get silently reclassified as legacy schema absence.

## 7. Canonical project invariants

Before a dependent transition, recover project invariants from their existing owners rather than copying them into this kernel/binding:

- accepted `execution_policy` → project `PROJECT.md`;
- exact current workstream/routing owner → selected `WORKSTREAM.yaml`;
- Card/milestone execution and implementation-owned Research → selected manifest-bound Task Board when implementation exists;
- plan review / Card review / milestone review / workstream final-integration review → their existing exact review owner and immutable subject;
- implementation/reviewer separation → the applicable stable contract + review state;
- deterministic continuation versus real stop → the current policy router and owning route.

## 8. Steady-state cost and runtime boundary

With a positively established current-context latch and no drift/uncertainty signal, ordinary deterministic continuation does not repeatedly load this recovery material.

Project Workflow owns:
- durable opaque policy selection;
- current-context re-bind requirement;
- canonical project-invariant checks;
- fail-closed project continuation semantics.

The installed/enabled runtime owns:
- interpretation of `policy_ref`;
- concrete role→harness/model/reasoning selection;
- worker/session lifecycle;
- runtime resume/replacement;
- runtime-side enforcement.

Do not duplicate those runtime mechanics here.
