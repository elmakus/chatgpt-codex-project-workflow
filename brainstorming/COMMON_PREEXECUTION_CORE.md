# Brainstorm — common pre-execution workflow core

Date: `2026-09-21`
Scope ID: `common-preexecution-core`
Revision: `R1`
Status: `tentative`

## Problem / goal

The fixed policy namespaces `workflow/chatgpt_only/*` and `workflow/codex_only/*` currently duplicate most of the pre-execution lifecycle. The goal of this exploration is to determine whether that duplicated semantic contract should move back into policy-neutral `workflow/common/*`, leaving only genuine runtime/session/review differences in thin policy-specific adapters.

The scope begins with the currently discussed stages from Intake through Strategic Planning. Execution Prep, Execution, Review, Close and policy-specific orchestration are not assumed common by this scope.

## Current understanding

### Verified facts

Direct comparison of current `main` shows:

- `BRAINSTORMING.md` differs only in policy/session wording; its actual exploratory lifecycle, adaptive grilling, durable state, Research handoff and promotion readiness semantics are the same.
- `DEFINITION.md` is effectively identical; the only material-looking textual difference is pointer wording, not different Definition semantics.
- `RESEARCH.md` has one genuine Codex-only addition: Investigator realization/re-realization must pass the Codex orchestration binding gate. The durable Research lifecycle, pointer ownership, status, return-target and reconciliation semantics are otherwise shared.
- `PLANNING.md` has shared strategic-planning semantics. Policy-specific differences are concentrated around context-hygiene language and how REQUIRED/RECOMMENDED independent plan review is realized: fresh ChatGPT review boundary versus Codex-managed Tester.
- `INTAKE.md` has shared managed-change intake semantics. The genuine Codex-only difference is establishing/readback of the manifest orchestration binding before policy-dependent runtime realization.

### Existing accepted decisions

- Fixed policies remain distinct execution policies.
- `chatgpt_only` uses normal ChatGPT as the fixed executor and fresh normal ChatGPT sessions for formal independent review.
- `codex_only` uses Codex Main plus runtime-owned Executor/Tester/Investigator realization through `codex_workflow`.
- Branch-first workstream identity and manifest-owned pre-execution routing remain accepted architecture.
- A user-owned Brainstorming → Project Definition promotion gate remains part of both fixed policies.

### Assumptions to verify

- Moving shared semantics into `workflow/common/*` will reduce drift more than it increases indirection.
- A common contract can express lifecycle semantics without becoming aware of concrete ChatGPT session or Codex runtime mechanics.
- Policy adapters can be small enough that future changes naturally land once in common rather than being copied between two near-identical files.

## Ideas / alternatives considered

### Option A — keep full policy-local copies

Retain complete `chatgpt_only` and `codex_only` versions of Intake/Brainstorming/Research/Definition/Planning.

Pros:
- every policy contract is self-contained;
- no indirection while reading a route.

Cons:
- current files already demonstrate semantic duplication;
- fixes/features must be repeated;
- drift can become accidental policy divergence.

### Option B — common semantic core + thin policy adapters

Move policy-neutral lifecycle semantics into common modules. Policy namespaces keep only their true deltas and explicitly compose/reference the common contract.

Candidate factoring:
- Brainstorming: essentially all common.
- Definition: essentially all common.
- Research: common lifecycle + Codex Investigator-realization adapter.
- Planning: common strategy/audit/approval lifecycle + policy-specific review-transition/context adapter.
- Intake: common identity/base/workstream/intake lifecycle + Codex orchestration-binding hook.

Pros:
- one source of truth for identical semantics;
- policy differences become explicit and reviewable;
- much lower drift risk.

Cons:
- requires a clean composition rule to avoid readers having to mentally merge arbitrary fragments;
- a poorly designed adapter system could make routing harder to follow than duplicated files.

### Option C — only commonize Brainstorming + Definition

Extract only the two nearly identical modules and leave Research/Planning/Intake duplicated.

Pros:
- smallest refactor;
- lowest immediate risk.

Cons:
- leaves large duplicated lifecycle surfaces where differences are already localized enough to isolate;
- likely preserves the same maintenance problem in Research/Planning/Intake.

## Trade-offs / questions

The important question is not whether text is similar, but whether the same authority/lifecycle invariant is intended to stay identical across policies.

A common module should own a rule only when changing that rule should normally change both policies together.

Policy-local modules should own only mechanics whose correct behavior genuinely depends on the execution policy.

## Adaptive discovery state

### Accepted exploratory choices

| Choice | Counterfactual challenge | Stability note |
|---|---|---|
| Treat commonization as semantic-core extraction rather than blindly merging files by textual similarity. | Would keeping duplicated full files be safer because each policy remains self-contained? Yes locally, but it preserves demonstrated drift risk and obscures which differences are intentional. | Tentatively stable; still needs architecture shape decision. |

### Unresolved material decisions / dependencies

| Decision | Prerequisites | Status |
|---|---|---|
| Exact composition model: common base contract referenced by thin policy modules vs common fragments/hooks included from policy modules. | Need evaluate readability, routing/progressive-disclosure and testability. | open |
| Whether Intake belongs mostly in common or remains policy-local with extracted common intake contract. | Must preserve Codex orchestration-binding establishment without making common know Codex. | open |
| Whether Research should be one common module plus a Codex realization hook. | Need ensure Investigator runtime mechanics remain wholly outside policy-neutral state semantics. | open |
| Whether Strategic Planning should be common through plan freeze, with only review-transition handling policy-local. | Need ensure ChatGPT context-health/fresh-review behavior and Codex Tester behavior remain explicit. | open |
| Whether routers should point directly to common modules or to thin policy entry modules that import/reference common authority. | Depends on progressive disclosure and ease of recovery. | open |
| Migration/testing strategy that proves no lifecycle behavior changed accidentally. | Need map existing policy-local tests/contracts to shared invariants + adapter-specific tests. | open |

### Reopened choices

None.

## Research needed

No external research is currently required. The next useful evidence is repository-internal: routing/read-set constraints, current tests and how common modules are already composed elsewhere.

## Open questions

1. Should policy routers still route to `workflow/<policy>/BRAINSTORMING.md` etc., where those files become tiny adapters, or should they route directly to `workflow/common/BRAINSTORMING.md` when no adapter is needed?
2. For Intake and Planning, do we want one common contract with explicit policy hook points, or a common lifecycle contract plus separate short policy supplements?
3. Do we want the end state to remove duplicated policy-local files entirely when there is zero policy delta (likely Brainstorming/Definition), or preserve tiny forwarding files for namespace symmetry and discoverability?

## Outcome of this session

- Tentative conclusions: stages 2 and 5 are already effectively common; stages 3 and 6 have a common semantic core with small policy-specific edges; stage 1 has a common core but a real Codex-only orchestration-binding step. Therefore the strong candidate is **common semantic core + thin policy adapters**, not a literal wholesale merge of all six current files.
- Explicit user/product choices to promote through Project Definition: none yet.
- Research still needed: repository-internal architecture/test inspection before choosing the exact composition mechanism.
- Open questions: composition model, adapter placement, direct-common routing versus forwarding policy modules, migration/test shape.
- Next phase/action: `continue brainstorming`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`. When the selected policy requires explicit user phase promotion, only an explicit user instruction may set `Definition promotion authorization: user_authorized`, and the authorization must name the exact current `<scope-id>@<revision>`. Any material change to the exploratory scope before Definition starts creates a new revision and resets authorization to `pending`.
