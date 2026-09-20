# Requirements — Codex orchestration recovery after context loss

Status: approved
Revision: R2
Date: 2026-09-20

## Goal

Under `execution_policy: codex_only`, context compaction, coordinator replacement, resume or other context reconstruction must not cause Codex Main to forget or bypass the active orchestration/runtime policy that governs worker dispatch. Recovery must be safe even when the external runtime/workflow version did not change, and it must remain token-light.

## Requirements

### CCOR-R1 — Recover orchestration policy, not only project obligation

After coordinator context loss/reconstruction, Main MUST recover both:

1. the exact current Project Workflow obligation from its existing durable owner; and
2. the active orchestration-policy binding required to realize policy-dependent worker dispatch.

Recovering only Card/review/Task Board state is insufficient. This requirement applies even when the external runtime/workflow version is unchanged for the entire session.

### CCOR-R2 — Durable policy binding is distinct from runtime identity

Project Workflow MUST distinguish a durable orchestration **policy binding** from concrete runtime identity.

A binding MAY contain only compact facts needed to re-bind the active runtime contract: an opaque runtime owner, policy/profile reference and runtime contract epoch/fingerprint when available.

Project Workflow MUST NOT persist concrete worker/session/process/model-instance identity, invocation IDs, leases, worktree paths, resume tokens or other runtime lifecycle mechanics as project authority.

Existing prohibitions on concrete runtime identity remain in force; wording that currently forbids every form of `profile` persistence MUST be narrowed so it does not prohibit durable policy/profile **selection**.

### CCOR-R3 — Branch-isolated manifest owns the binding

For branch-first `codex_only` managed work, selected `WORKSTREAM.yaml` MUST own the current orchestration-policy binding as routing/recovery metadata.

The binding MUST NOT be mirrored into root `PROJECT.md`, Task Board, Task Cards or a repository-global mutable registry.

Historical/default state follows existing Recovery migration semantics and acquires the binding only in the migrated branch-isolated workstream.

### CCOR-R4 — Current-context readiness is deliberately non-durable

Successful durable policy resolution MUST NOT be treated as proof that the policy is loaded in the current coordinator context.

The continuation contract MUST maintain a conceptual non-durable **current-context binding latch** after successful runtime re-bind. The latch:

- exists only as current coordinator context state;
- is never serialized as project authority or tied to a worker/session identifier;
- MUST be treated as absent whenever Main reconstructs from durable state or cannot positively establish that the binding was re-established in the current context;
- MUST NOT be inferred from a matching durable fingerprint or previous durable binding evidence.

An absent/uncertain latch forces the bounded re-bind in CCOR-R5. This is what makes same-version compaction safe.

### CCOR-R5 — Token-light continuation kernel and fail-closed re-bind

Project Workflow MUST define a compact `codex_only` orchestration continuation kernel that can be re-read after context reconstruction without loading the full workflow tree.

Before the first policy-dependent dispatch/transition when the current-context latch is absent/uncertain, the bounded recovery set MUST be sufficient:

- project `PROJECT.md` for accepted execution policy;
- selected `WORKSTREAM.yaml` for exact workstream identity/routing plus orchestration binding;
- the small continuation kernel;
- only the canonical state record already required for the current obligation.

Main MUST re-bind the durable policy through its runtime owner and establish the current-context latch before Tester/Executor/other policy-dependent worker dispatch.

A missing, stale, contradictory or unresolvable binding fails closed. When installed/enabled `codex_workflow` owns runtime orchestration, Main MUST NOT silently fall back to an internal/native harness merely because transient routing context was lost.

If the bound runtime policy cannot be re-established for a concrete required operation, persist/route the normal concrete runtime blocker; do not silently change Project Workflow execution policy.

The recovery rule MUST NOT require re-reading the whole Master Plan, all Task Cards, all workflow modules, all durable documents or the external `codex_workflow` repository.

### CCOR-R6 — Runtime role→harness mapping remains external

Project Workflow MUST NOT duplicate the concrete role→harness/model mapping of `codex_workflow`.

The Project Workflow kernel defines only:
- recovery/revalidation of the active runtime-policy binding;
- the current-context latch rule;
- project-owned invariants checked before dispatch/transition;
- fail-closed behavior when re-binding cannot be proven.

The external runtime remains authoritative for interpreting the opaque policy/profile reference, selecting concrete harness/model routing and enforcing its own role-routing rules.

### CCOR-R7 — Existing project invariants remain canonically owned

Context recovery MUST re-establish, from existing canonical durable owners as applicable:

- accepted `execution_policy`;
- exact current authority/review subject and its owner;
- REQUIRED/RECOMMENDED independent-review requirement and implementation/reviewer separation;
- workstream/Task Board ownership boundaries;
- deterministic continuation and real workflow stop conditions.

The continuation kernel MUST NOT duplicate full mutable state. It points Main back to the canonical owner and states only the small invariant needed before a dependent transition.

### CCOR-R8 — Version/epoch drift is an additional stale-binding case

When the runtime exposes a contract version/epoch/fingerprint, Project Workflow SHOULD persist it in the opaque binding.

If the current runtime contract no longer matches the durable binding, Main MUST treat the binding as stale, re-resolve/revalidate the selected policy/profile under the current runtime contract, and durably refresh the binding only after successful resolution.

This drift check supplements CCOR-R1/CCOR-R4. A matching fingerprint MUST NOT substitute for current-context re-bind after reconstruction.

### CCOR-R9 — Minimal steady-state cost

Normal deterministic continuation with an established current-context latch MUST NOT repeatedly load heavy recovery material.

The new mechanism SHOULD add only:
- a small manifest binding;
- one compact static kernel;
- one bounded re-bind at a real coordinator reconstruction/uncertainty boundary or when drift is detected.

### CCOR-R10 — Regression coverage

Repository tests MUST cover at least:

1. same-version context reconstruction followed by Tester dispatch cannot bypass the durable runtime policy binding;
2. durable binding/fingerprint alone cannot satisfy the current-context latch;
3. missing/unknown binding fails closed instead of silently selecting another harness;
4. a changed runtime epoch/fingerprint requires policy re-resolution;
5. policy binding does not permit concrete worker/session/model-instance identity in project state;
6. independent-review, ownership, execution-policy and real-stop invariants remain recoverable from canonical owners without full-tree re-read;
7. `chatgpt_only` behavior remains unchanged;
8. existing `codex_workflow` ownership of concrete role/model/harness mechanics remains explicit.

## Non-goals

- Implementing `codex_workflow` runtime-side role→harness validation.
- Encoding `muse-max` or any other named profile as a universal Project Workflow default.
- Persisting worker/session/process/model-instance identity or a durable context/session latch.
- Re-reading the whole workflow or project authority tree after every compaction.
- Changing the repository's accepted `chatgpt_only` execution policy.
- Weakening independent review, accepted authority, authorization or stop gates.
