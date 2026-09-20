# Requirements — Codex orchestration recovery after context loss

Status: approved
Revision: R1
Date: 2026-09-20

## Goal

Under `execution_policy: codex_only`, context compaction, coordinator replacement, resume or other context reconstruction must not cause Codex Main to forget or bypass the active orchestration/runtime policy that governs worker dispatch. Recovery must be safe even when the external runtime/workflow version did not change, and it must remain token-light.

## Requirements

### CCOR-R1 — Recover orchestration policy, not only project obligation

After coordinator context loss/reconstruction, Main MUST recover both:

1. the exact current Project Workflow obligation from its existing durable owner; and
2. the active orchestration-policy binding required to realize policy-dependent worker dispatch.

Recovering only Card/review/Task Board state is insufficient.

This requirement applies even when the external runtime/workflow version is unchanged for the entire session.

### CCOR-R2 — Durable policy binding is distinct from runtime identity

Project Workflow MUST distinguish a durable orchestration **policy binding** from concrete runtime identity.

A policy binding MAY durably contain only the compact facts needed to re-bind the active runtime contract, including an opaque runtime owner, policy/profile reference and runtime contract epoch/fingerprint when available.

Project Workflow MUST NOT persist concrete worker/session/process/model instance identity, invocation IDs, leases, worktree paths, resume tokens or other runtime lifecycle mechanics as project authority.

Existing prohibitions on concrete runtime identity remain in force; wording that currently forbids every form of `profile` persistence MUST be narrowed so it does not prohibit the policy binding required by this requirement.

### CCOR-R3 — Branch-isolated manifest owns the binding

For branch-first `codex_only` managed work, the selected `WORKSTREAM.yaml` MUST own the current orchestration-policy binding as routing/recovery metadata.

The binding MUST NOT be mirrored into root `PROJECT.md`, the Task Board, Task Cards or a repository-global mutable registry.

Historical/default state that must migrate before mutation follows existing Recovery semantics and acquires the binding only in the migrated branch-isolated workstream.

### CCOR-R4 — Token-light continuation kernel

Project Workflow MUST define a compact `codex_only` continuation/orchestration kernel that can be re-read after context reconstruction without loading the full workflow tree.

Before the first policy-dependent dispatch/transition after reconstruction or when Main cannot positively establish that the current binding is still loaded/validated, the bounded recovery set MUST be sufficient:

- project `PROJECT.md` for accepted execution policy;
- selected `WORKSTREAM.yaml` for exact workstream identity/routing plus orchestration binding;
- the small continuation kernel;
- only the canonical state record already required for the current obligation (for example the selected Task Board/review record).

The recovery rule MUST NOT require re-reading the whole Master Plan, all Task Cards, all workflow modules, all durable documents or the external `codex_workflow` repository.

### CCOR-R5 — Fail closed before policy-dependent dispatch

A Tester/Executor/other policy-dependent worker dispatch MUST NOT proceed when the orchestration binding is missing, stale, contradictory or not successfully re-bound after a reconstruction boundary.

When installed/enabled `codex_workflow` owns runtime orchestration, Main MUST use the recovered binding to re-enter that runtime policy. It MUST NOT silently fall back to an internal/native harness merely because transient routing context was lost.

If the bound runtime policy cannot be re-established for a concrete required operation, persist/route the normal concrete runtime blocker; do not silently change Project Workflow execution policy.

### CCOR-R6 — Runtime role→harness mapping remains external

Project Workflow MUST NOT duplicate the concrete role→harness/model mapping of `codex_workflow`.

The Project Workflow kernel defines only:
- that the active runtime-policy binding must be recovered/revalidated;
- which project-owned invariants must be checked before dispatch/transition;
- fail-closed behavior when re-binding cannot be proven.

The external runtime remains authoritative for interpreting the opaque policy/profile reference, selecting the concrete harness/model and enforcing its own role-routing rules.

### CCOR-R7 — Existing project invariants remain canonically owned

Context recovery MUST re-establish, from existing canonical durable owners as applicable:

- accepted `execution_policy`;
- exact current authority/review subject and its owner;
- REQUIRED/RECOMMENDED independent-review requirement and implementation/reviewer separation;
- workstream/Task Board ownership boundaries;
- deterministic continuation and real workflow stop conditions.

The continuation kernel MUST NOT duplicate full mutable state. It should point Main back to the canonical owner and state the small invariant needed before a dependent transition.

### CCOR-R8 — Version/epoch drift is an additional stale-binding case

When the runtime exposes a contract version/epoch/fingerprint, Project Workflow SHOULD persist it in the opaque binding.

If the current runtime contract no longer matches the durable binding, Main MUST treat the binding as stale, re-resolve/revalidate the selected policy/profile under the current runtime contract, and durably refresh the binding only after successful re-bind.

This drift check supplements CCOR-R1; it MUST NOT make same-version compaction safe only by accident.

### CCOR-R9 — Minimal steady-state cost

Normal deterministic continuation with an already-valid in-context binding MUST NOT repeatedly load heavy recovery material.

The new mechanism SHOULD add only:
- a small manifest binding;
- one compact static kernel;
- one bounded re-bind/revalidation at a real coordinator reconstruction/uncertainty boundary or when drift is detected.

### CCOR-R10 — Regression coverage

Repository tests MUST cover at least:

1. same-version context reconstruction followed by Tester dispatch cannot bypass the durable runtime policy binding;
2. missing/unknown binding fails closed instead of silently selecting another harness;
3. a changed runtime epoch/fingerprint requires revalidation;
4. policy binding does not permit concrete worker/session identity in project state;
5. independent-review, ownership, execution-policy and real-stop invariants remain recoverable from their canonical owners without full-tree re-read;
6. `chatgpt_only` behavior remains unchanged;
7. existing `codex_workflow` ownership of concrete role/model/harness mechanics remains explicit.

## Non-goals

- Implementing `codex_workflow` runtime-side role→harness validation.
- Encoding `muse-max` or any other named profile as a universal Project Workflow default.
- Persisting worker/session/process/model instance identity.
- Re-reading the whole workflow or project authority tree after every compaction.
- Changing the repository's accepted `chatgpt_only` execution policy.
- Weakening independent review, accepted authority, authorization or stop gates.
