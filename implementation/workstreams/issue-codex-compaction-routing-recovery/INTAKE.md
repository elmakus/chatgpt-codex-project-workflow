# Intake — Codex compaction routing recovery

- Workstream ID: `issue-codex-compaction-routing-recovery`
- Kind: `issue`
- Branch: `fix/codex-compaction-routing-recovery`
- Integration target: `main`
- Base: `aa35886be2ec1b2ac58e600cd633dc214dc65096`
- Classification: independent
- Parent workstream: none
- Status: active

## Operator intent

Diagnose and repair loss or non-respect of critical orchestration policy after Codex context compaction/resume. The motivating incident had an active `muse-max` compute profile before compaction, correctly routed Tester/Executor work through Muse, then dispatched a fresh independent Tester through an internal `spawn_agent(...)` harness after compaction until the user forced Main to re-read the runtime contract.

The primary requirement is independent of workflow version drift: the same failure must be prevented even when the external `codex_workflow` version is unchanged for the entire session. Version/epoch drift remains an additional stale-policy case.

The solution must remain token-light. Recovery must not require re-reading the whole workflow, Master Plan, Task Board and delegation/runtime contracts after every compaction.

## Pre-creation discovery

Current `main` evidence:

- Root `PROJECT.md` selects this repository's own `execution_policy: chatgpt_only`; this issue is therefore managed through ChatGPT-only branch-first Intake even though the affected contract is the `codex_only` policy.
- No matching active branch, PR or GitHub issue was found for compaction/routing/policy recovery. Repository branch discovery showed only `main`, so this workstream is independent and based on the normal integration target.
- `requirements/CODEX_ONLY_CONTINUOUS_ORCHESTRATION.md` COCO-R4 requires coordinator/session/runtime interruption or replacement to be recoverable from current workflow authority plus durable project state, while concrete worker/session/model/resume mechanics remain runtime-owned.
- `workflow/codex_only/RECOVERY.md` promises recovery after transcript/context loss from durable project state.
- `workflow/codex_only/STATE.md` explicitly states that runtime worker identity/lifecycle is not Project Workflow state and forbids persisting worker/session/model/profile/invocation/resume identity.
- `prompts/CODEX_START.md` and `workflow/codex/CODEX_ORCHESTRATION.md` delegate internal worker/reviewer/model routing and runtime recovery to installed `codex_workflow`.
- `skills/project-workflow/SKILL.md` is intentionally thin: after entry/recovery it resolves `PROJECT.md`, the canonical router and only the currently required route modules/state.

## Root-cause diagnosis

The current contracts recover **project obligation state** but do not define a minimal durable/recoverable representation of the **active orchestration-policy selection** that Main must respect when realizing the next worker dispatch.

This creates two different recoverability domains:

1. Project Workflow can recover what obligation is current: selected workstream, Task Board/Card, exact review subject, authority, evidence, ownership and stop conditions.
2. Internal runtime policy determines how that obligation is realized: active compute/orchestration profile and its role→harness routing.

Project Workflow currently treats the second domain too coarsely as entirely runtime-owned and, at the same time, states that concrete `profile` identity must not be persisted in Project Workflow state. After context loss, Main can therefore reconstruct the next Tester/Executor obligation correctly while lacking a compact durable fact that the active runtime policy is still `muse-max` (or another selected policy handle) and must be re-bound before the first policy-dependent dispatch.

The observed failure is consequently possible without any workflow-version change. Version drift only makes the same missing revalidation problem more visible.

## Responsibility boundary

This workstream must not duplicate `codex_workflow`'s runtime-side enforcement. A separate runtime issue may validate/fail closed on illegal role→harness dispatch.

Project Workflow should own the project/orchestrator side of the boundary:

- identify which orchestration-policy facts are correctness-critical across compaction/resume;
- require a cheap recovery/revalidation step before the first policy-dependent dispatch/transition after context loss or coordinator replacement;
- keep project-owned review/ownership/authority/stop invariants recoverable from their existing durable owners;
- distinguish durable **policy selection / contract binding** from forbidden concrete worker/session/process identity;
- define behavior for external workflow/policy epoch drift without making drift the primary problem;
- keep the steady-state token cost small.

## Candidate design direction to validate in Definition/Planning

Prefer a compact orchestration continuation kernel/checkpoint rather than re-reading full workflow trees. The kernel may contain an opaque runtime-policy binding such as runtime owner + selected policy/profile handle + contract epoch/fingerprint, plus small Project Workflow invariants/pointers needed to force route revalidation before dispatch.

The exact storage/schema is not accepted yet. Definition must decide whether this kernel belongs in branch-isolated workstream routing state, another small durable project artifact, or a runtime-provided checkpoint that Project Workflow requires but does not interpret beyond an opaque binding.

The contract must not persist concrete worker/session/process identity, worker leases, invocation IDs or other `codex_workflow` mechanics.

## Similar invariant exposure

The same compaction class can affect any invariant that Main previously held only in transient context. Definition/planning must explicitly cover:

- independent review requirement and exact independence boundary;
- implementation/reviewer ownership separation;
- real workflow stop conditions and deterministic continuation;
- active execution policy;
- current authority/review subject and owning durable pointer.

Project Workflow already durably owns most of these through PROJECT/manifest/Task Board/review records; the missing requirement is to re-bind/revalidate the small critical set before a dependent transition, rather than assume transient Main memory remains valid.

## Path classification

This is **not** a micro-fix.

The issue changes accepted architecture around the Project Workflow ↔ `codex_workflow` boundary and may require revising the existing rule that model/profile information is never Project Workflow state. It therefore routes to **Project Definition**.

Next route: `project_definition`.

## Scope boundaries

Included:
- `codex_only` compaction/resume/continuation recovery semantics;
- minimal durable/recoverable orchestration-policy binding;
- pre-dispatch/pre-transition revalidation semantics;
- interaction with project-owned review/ownership/authority/stop invariants;
- version/epoch drift as an additional stale-policy case;
- token-light regression coverage and documentation.

Excluded:
- implementing `codex_workflow` role→harness enforcement;
- storing concrete worker/session/process/invocation identity in Project Workflow state;
- full workflow re-read after every compaction;
- changing this repository's accepted `chatgpt_only` execution policy;
- weakening independent review, authority, authorization or stop gates.
