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

### Concrete fixed-policy diff audit

The current policy-local files differ as follows after ignoring policy names/path prefixes:

- **Intake**: one real semantic delta exists in `codex_only`: immediately after manifest creation it establishes and reads back the durable opaque orchestration binding (`runtime_owner + policy_ref`, optional fingerprint) before Intake may complete or a policy-dependent runtime role is realized. Remaining differences are wording/path/coordinator labels.
- **Brainstorming**: no real lifecycle delta. Differences are only `fresh session` versus `fresh coordinator context` wording and one unnecessary `Codex-only workstream manifest` qualifier.
- **Promotion gate**: the complete Brainstorming → Project Definition gate in both routers is semantically identical except the policy name and policy-local Research path. This is duplicated common authority today.
- **Research**: the durable record, pointer ownership, status semantics, Return-target protocol, execution-resolution classifier, chaining and authority boundary are identical. The only real Codex addition is Investigator realization through the generic Codex pre-dispatch binding gate.
- **Definition**: no intended policy delta was found. One textual mismatch looks like stale ChatGPT-only wording: it says a completed Research obligation may be owned by `pre-execution PROJECT state`, while the current branch-first model owns pre-execution Research through selected-manifest routing. The Codex wording matches the current architecture.
- **Planning**: strategic planning semantics are identical. Differences are: (a) ChatGPT-only still lists `fresh-context boundaries only when materially useful` as possible Master Plan content, while the ChatGPT router now makes Context Health a dynamic safe-boundary check and explicitly says ordinary topology transitions are not context-health signals; (b) ChatGPT freezes plan review then stops for a fresh reviewer, whereas Codex returns to the router for Tester realization; (c) verdict-consumption wording says generic reviewer versus Tester. Difference (a) appears stale/overlapping rather than an intentional planning-semantic difference. Differences (b)/(c) are review-realization mechanics that can live outside Planning.

Existing `workflow/common/BRAINSTORMING.md`, `DEFINITION.md` and `RESEARCH.md` are older/partial common contracts. The fixed-policy copies contain later branch-first/adaptive/reconciliation behavior. Commonization should therefore **promote the current richer semantics into common**, not merely point routers at the existing common files unchanged.

The Codex orchestration contract already defines one role-agnostic pre-dispatch gate for every policy-dependent role realization. This makes the Research-specific Investigator paragraph a candidate for removal from Research entirely: common Research can remain runtime-neutral while Codex orchestration enforces the gate at dispatch.


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

### Capability-first direction

The user clarified the intended simplification direction: workflow semantics should prefer capability-dependent mechanics over product identity where the semantic obligation is the same.

For independent review, the candidate common rule is:

```text
independent review required
→ use an available independent execution context when the runtime provides one
→ otherwise persist exact review state and hand off to a fresh context
```

A failed invocation of an available independent-agent capability is not evidence that the capability is absent and must not silently downgrade to a fresh-chat fallback. Failure follows normal retry/blocker/evidence handling.

This suggests the current `chatgpt_only` / `codex_only` split should remain only where there is a genuine semantic/runtime-policy requirement, not merely because one environment realizes the same obligation with a subagent and another realizes it with a fresh context.

Accepted exploratory implications from the current user round:
- Brainstorming should not differ between fixed policies.
- Brainstorming → Definition promotion gate should not differ.
- Definition drift should be corrected and the stage treated as common.
- Research durable lifecycle should be common; Codex Investigator realization is a runtime transport concern.
- Strategic Planning should use the same common semantics; review transport belongs after plan freeze, outside Planning itself.
- Existing `workflow/common/*` must be audited as a whole before reuse: some files are current active common authority, while Brainstorming/Definition and part of Research are older/partial contracts and must not be blindly reused.
- The remaining Intake orchestration-binding step needs a separate decision: either retain it because an exact runtime orchestration policy/profile is durable project intent, or simplify/defer it if the new model only requires capability resolution at the point a capability is needed.

Historical finding for Context Health / Planning:
- `chatgpt_only` Context Health was introduced on 2026-09-18 and materially tightened on 2026-09-20 (`fa83e4e99`, anti-bounce; `0353c2bac`, router reconciliation) so topology transitions are not context-health signals.
- `codex_only/PLANNING.md` was then explicitly changed by `be7d3d7b0` on 2026-09-20 12:31 UTC to remove the planned coordinator-refresh boundary.
- `chatgpt_only/PLANNING.md` still retains the older “fresh-context boundaries only when materially useful” Master Plan bullet. That is accidental drift relative to the newer Context Health semantics, not a desired policy difference.


### User direction — runtime ownership and parallelism

The user clarified the intended target architecture:

- `codex_workflow` should own Codex runtime orchestration completely.
- The intended future `codex_workflow` has one fixed orchestration profile rather than multiple selectable compute profiles.
- Codex subagents should be launched through Codex's native subagent mechanism; the worker model may be Muse rather than an OpenAI model, but that model/harness choice remains runtime-owned by `codex_workflow`.
- Project Workflow should therefore not persist a per-workstream runtime/profile selection merely to tell `codex_workflow` which profile to use when there is only one installed/active behavior.
- Counterfactual challenge: a durable Project Workflow binding would still be justified if projects could intentionally select different orchestration profiles/owners whose identity must survive reconstruction. Under the user's one-fixed-profile target this condition no longer applies, so the current `runtime_owner + policy_ref + contract_fingerprint` workstream binding is tentatively classified as removable runtime leakage rather than durable project authority.
- Planning should describe dependency/independence and identify work that is safe/valuable to execute concurrently independent of the current runtime's ability to exploit that concurrency.
- Lack of native parallel/subagent capability must not invalidate the plan. A runtime without delegation executes the same legal dependency graph serially in deterministic order.
- A runtime with delegation may execute a compatible ready set concurrently, subject to the same dependency, write-scope, exclusive-resource and integration rules.
- Parallelism is therefore an optimization/capability realization, not a distinct project semantics branch. Only genuinely simultaneous behavior that is itself part of acceptance would create a hard capability requirement.


### User direction — no worker-role names in Project Workflow

The user refined the runtime boundary further: Project Workflow should not hardcode concrete worker-role names such as `Executor`, `Tester` or `Investigator` merely to tell Codex which worker to launch.

Target separation for the first six stages:

- Project Workflow owns the **semantic obligation and constraints**: exact Research question/return target, exact plan-review subject, whether independence is required, accepted authority and durable lifecycle state.
- Main reads that obligation plus the task/subject and asks the installed runtime workflow to realize it using the most appropriate currently available worker/capability from its own catalog.
- `codex_workflow` owns the worker catalog, role names, model/harness mapping and the decision of which concrete worker class realizes a delegable obligation.
- Project Workflow must not need to know that the selected runtime calls that worker `Investigator`, `Tester`, `Executor` or any future name.
- A semantic invariant such as independent review remains Project Workflow authority; the concrete worker chosen to satisfy that invariant is runtime authority.
- For work that does not require an independent context, Main may perform it directly when appropriate or delegate according to runtime policy; Project Workflow should not force delegation merely because a named worker role exists.

Current first-six-stage hardcoding identified on main:
- `codex_only/RESEARCH.md` explicitly names `Investigator` and contains an Investigator-realization section; this is a candidate for removal from the common Research semantics.
- `codex_only/PLANNING.md` names a Codex-managed `Tester` for plan review; common Planning should instead create the exact independent-review obligation and return to routing/transport resolution.
- `codex_only/INTAKE.md` mentions concrete Executor/Tester/Investigator realization only descriptively and as part of the current orchestration-binding design; under the one-fixed-runtime target this should not be needed in Intake.

Counterfactual challenge: Project Workflow still must encode any property that changes correctness, such as `independent context required`, exact immutable review subject, or read-only evidence boundaries. Removing worker names must not remove those semantic guarantees. The runtime may choose any catalog entry only if it satisfies the Project Workflow obligation.

Scope discipline: continue analysis only for Intake through Strategic Planning until those six stages are settled; do not advance into Execution Prep/Execution/Review/Close yet.


### Stage 7 exploration — Execution Prep / JIT refinement

Current-main comparison shows that Execution Prep has one large semantic common core plus a Codex-only parallel-batch scheduler layered into the route.

Common/project-semantic material that should remain independent of runtime identity:
- exact selected branch-isolated workstream and manifest-bound Task Board;
- Task Card creation only when scope is currently knowable, with durable JIT triggers instead of speculative placeholders;
- exact authority slice, dependencies, included/excluded scope, acceptance, tests/evidence/readback, authorization gates and review requirement;
- Research handoff/return and crash-safe reconciliation;
- qualified micro-fix materialization into one bounded Card without inventing a Master Plan/milestone;
- incremental L2/JIT refinement only for not-yet-started work within accepted authority;
- OpenSpec marking, requirement coverage, side-effect/idempotency/security/migration audit;
- Task Board as sole mutable implementation/review/Research state;
- automatic return to router when executable work is prepared.

Current Codex-only additions are primarily concurrency realization:
- optional Card fields `parallel_safe`, `write_scope`, `exclusive_resources`;
- current READY-set compatibility calculation;
- freezing a concrete batch ID/member list/lane order/integration base;
- pre-launch workspace-isolation proof and stale-batch refresh/abandon logic;
- marking batch members in progress before runtime launch.

Current ChatGPT-only differences are primarily policy restrictions rather than different preparation semantics: it forbids bounded-parallel coordination metadata and marks exactly one next eligible Card READY because the policy assumes serial execution.

Capability-first candidate architecture:
- common Execution Prep creates the same Cards and dependency graph for every runtime;
- optional project-safety metadata may describe whether concurrent mutation is safe, but must not encode worker/session/model identity;
- common Project Workflow should not freeze a concrete parallel runtime batch merely because one product supports subagents unless that batch/integration state is required for durable project correctness;
- Main/runtime may choose serial versus concurrent realization from the same READY Cards according to available capabilities;
- lack of concurrency capability leaves the Cards serial-valid and does not require a different policy-local Task Card contract.

Open decision for stage 7: whether `parallel_safe/write_scope/exclusive_resources` belong in stable Project Workflow Card contracts as project-level safety constraints, while concrete batch/lane/workspace scheduling moves to runtime orchestration; or whether even those fields should be derived dynamically by Main/runtime from Card scope. Recommendation: retain explicit project-safety metadata only when it is necessary to prove non-overlap safely; move concrete batch formation and worker/lane realization out of Project Workflow.


### Stage numbering correction

The previously discussed stage 7 was misnumbered. The intended sequence is:
- 6. Strategic Planning
- 7. Independent Plan Review
- 8. Execution Prep / JIT

Stage-8 parallelism analysis remains useful but is deferred until stage 7 is settled.

### Stage 7 exploration — Independent Plan Review

Current-main comparison shows the same Project Workflow semantics in both fixed policies:
- review requirement comes from Planning;
- one durable review record per exact immutable plan revision/subject;
- selected workstream manifest points to that active review record;
- reviewer must be independent from the author of the exact subject;
- reviewer reads the immutable plan + approved Definition/decisions/relevant evidence and does not mutate the plan while judging it;
- verdict is GREEN/RED with durable evidence;
- GREEN returns to Planning for deterministic approval/verdict consumption, then may continue to Execution Prep;
- RED returns through the router to Planning, Definition, Research, or a real user-owned stop depending on the defect;
- substantive correction creates a new plan revision and a new review subject; completed review records are never overwritten.

The current policy difference is review transport/realization only:
- ChatGPT-only requires a fresh normal ChatGPT chat because the authoring chat cannot provide an independent verdict.
- Codex-only asks runtime to realize an independent Tester and carries Codex-specific binding/runtime-loss semantics.

Capability-first target:
- common Project Workflow expresses only `independent review required for exact subject X` plus the read/evidence/immutability constraints;
- it does not name `Tester` or any concrete worker role;
- Main/runtime selects any available catalog capability that satisfies the independence constraint;
- when no independent delegated context is available, persist the exact review obligation and perform a fresh-context handoff;
- a failed invocation of an available independent-context capability is a runtime failure/retry/blocker, not evidence that capability is absent;
- a fresh ChatGPT context can perform the same common review contract directly from the durable locator, so no product-specific review semantics are required.

Counterfactual challenge: removing worker-role names must not weaken provenance. Project Workflow still needs enough durable information to prove that the verdict did not come from the author of the exact review subject. The concrete runtime worker name/ID need not be part of the project contract, but independence evidence/provenance may still need a neutral representation.


### Proposed validation — capability-parity A/B smoke

Before committing to the common/capability-first refactor, validate the design with fixture-driven semantic A/B scenarios rather than product-identity detection.

Core test principle:
- start from the **same durable Project Workflow state** and exact semantic obligation;
- run the routing decision under two mocked runtime capability surfaces;
- assert that Project Workflow semantics and durable subject/state are identical, while only the realization/transport differs.

Primary plan-review scenario:

```text
Input:
  exact immutable plan subject R1
  review requirement = RECOMMENDED
  review state = pending
  reviewer must be independent from author

A: independent_context_available = true
  → select delegated independent realization
  → no user stop
  → verdict is written to the same review record

B: independent_context_available = false
  → persist/retain the same pending review record
  → fresh-context handoff
  → STOP
  → fresh context resumes from the same durable locator
  → verdict is written to the same review record

Expected semantic equivalence after verdict:
  same review subject
  same review lifecycle
  same GREEN/RED semantics
  same evidence requirements
  same router continuation
  no product-specific worker role appears in Project Workflow state
```

Negative scenario:
- capability is reported available but delegated invocation fails;
- expected: runtime retry/blocker/error path;
- forbidden: reinterpret failure as capability absence and silently switch to fresh-context fallback.

Additional first-seven-stage regression scenarios should verify:
1. Brainstorming and Definition behave identically under both capability surfaces.
2. Research obligation is the same; runtime may delegate or Main may execute it, but durable Research semantics remain unchanged.
3. Planning creates the same immutable plan-review obligation regardless of capability.
4. Fresh-context continuation recovers from durable state without previous-chat narrative.
5. No `Tester`/`Investigator`/other runtime catalog role is required in common Project Workflow contracts.

Recommended test shape in this repository:
- add a fixture JSON/YAML matrix similar to the existing adaptive-brainstorming fixtures;
- add Python contract/state-transition tests that assert expected next obligation/stop/locator for each capability variant;
- retain static text-contract tests only as secondary guardrails;
- add one synthetic E2E smoke covering Planning → independent plan review → GREEN → Planning approval for both capability variants.

Success criterion: **semantic parity with transport variance**. If the two capability variants require different Project Workflow authority/state semantics, the commonization proposal is not yet correct.


### Capability-parity A/B smoke — result

A bounded in-session state-machine experiment was run for stage 7 using one identical durable plan-review subject under three mocked capability surfaces.

Input in all cases:
- plan revision: `R1`;
- review requirement: `RECOMMENDED`;
- review state: `pending`;
- exact immutable review subject: one fixed subject;
- reviewer must differ from the subject author.

Results:

| Case | Capability surface | Expected transport | Result |
|---|---|---|---|
| A | independent context available, invocation succeeds | delegated independent review | PASS |
| B | independent context absent | durable fresh-context handoff, then fresh review | PASS |
| C | independent context available, invocation fails | runtime failure/retry/blocker; no fallback | PASS |

For A and B, after an equivalent GREEN verdict the Project Workflow durable state was semantically identical: same plan revision, same exact review subject, same GREEN state and same evidence. Concrete reviewer transport identity was irrelevant to the durable review semantics.

For C, the failed delegated invocation preserved the original pending review subject/state and did not reinterpret the failure as capability absence or trigger a fresh-context fallback.

This smoke supports the capability-first hypothesis for stage 7: independent review semantics can be common while realization transport varies. It is not yet proof for the full workflow; later stages require their own parity scenarios.


### Primary design goal — runtime portability at any workflow boundary

The user clarified the overarching goal: one Project Workflow task/workstream must remain portable between normal ChatGPT and Codex at arbitrary durable boundaries, without changing project semantics or requiring a policy rewrite.

Intended usage includes, for example:
- start Brainstorming in ChatGPT;
- continue Research in Codex;
- return to ChatGPT for Definition/Planning/JIT preparation;
- move implementation to Codex;
- later move remaining implementation back to ChatGPT;
- continue from the same durable project/workstream state each time.

Therefore Project Workflow should describe **semantic obligations, authority, durable state and correctness constraints**, not product identity or concrete worker catalogs.

Runtime realization is capability-dependent:
- when independent context is required and native/delegated independent execution is available, the runtime may realize it internally;
- when independent context is required but unavailable, preserve the same obligation and produce a fresh-context handoff;
- when multiple ready obligations are concurrency-safe and runtime can execute concurrently, it may do so;
- when concurrency is unavailable, the same legal obligations execute serially;
- lack of a capability changes transport/scheduling, not the underlying Project Workflow meaning;
- available-capability invocation failure is not capability absence and follows normal runtime failure/retry/blocker handling.

The durable state must be sufficient for another supported runtime to take over without relying on previous-chat narrative, worker names, session IDs, model identities or runtime-specific orchestration metadata.

Counterfactual challenge: runtime-neutral portability must not erase real correctness requirements. If an obligation genuinely requires a property such as reviewer independence, isolated mutable ownership, atomic external operation, or simultaneous behavior as part of acceptance, Project Workflow must persist that property explicitly. The receiving runtime may choose how to realize it, but may not weaken it merely because a capability is unavailable.

This portability goal is now the main architectural criterion for evaluating commonization and capability-dependent mechanics.


### Live test B — ChatGPT fresh-context result

The live ChatGPT branch of the capability-first experiment completed from a fresh independent chat using only the runtime-neutral durable obligation in `brainstorming/live-tests/CAPABILITY_PLAN_REVIEW_B.md`.

Observed behavior:
- the user manually opened a fresh ChatGPT chat and supplied the locator prompt;
- that fresh chat recovered the exact immutable subject from the durable review record;
- it did not require a concrete worker-role name, model, product-specific reviewer contract or previous-chat narrative;
- it preserved the immutable subject unchanged;
- it wrote the verdict/evidence back to the same review record;
- verdict was **RED** because the deliberate plan omission for `capability available + invocation fails` is a material correctness gap.

Correct interpretation: this proves **fresh-context consumption/recovery portability**, not automatic capability resolution or automatic handoff generation. The initiating ChatGPT context was not tested for the decision `independent context required + no native delegation capability → generate fresh-context handoff and stop`; the user manually created that fresh context. The RED still demonstrates that the fresh context independently evaluated the runtime-neutral obligation.

A/B comparison remains open until the Codex live branch completes.


### Live A/B conclusion — ChatGPT vs Codex

Both live branches completed against the same immutable subject `dcdc80769c0b64d4444aa330285a780f8483ec5c:brainstorming/live-tests/CAPABILITY_PLAN_R1.md`.

Observed common behavior:
- neither initiating context issued the independent verdict itself;
- neither durable obligation named a required worker role;
- ChatGPT satisfied independence through a fresh-chat boundary;
- Codex satisfied independence by selecting a separate runtime worker internally;
- both reviewers independently returned **RED** for the same material defect: the subject leaves `capability available + invocation fails` undefined;
- both preserved the immutable subject.

This is strong live evidence for the core portability hypothesis: the same runtime-neutral semantic obligation can be realized by different runtimes while preserving the same substantive review result.

The live test also exposed two serialization/provenance differences that must be resolved before claiming full durable-state parity:
1. ChatGPT persisted `Review state: RED`, while Codex persisted `Review state: completed` plus a separate `Review verdict: RED`. A common review contract must define one canonical lifecycle schema so takeover does not depend on runtime-specific interpretation.
2. Codex additionally persisted concrete runtime provenance (`Reviewer: fresh logical Muse Tester...`, invocation UUID). That was not required by the runtime-neutral obligation. Under the target architecture, Project Workflow should persist only neutral provenance needed to prove independence/correctness; concrete worker/session/invocation identity should remain runtime-owned unless a specific audit requirement justifies it.

Therefore the live test verdict on the architecture is:
- **capability-first semantic portability: supported by live evidence;**
- **full durable-state interchangeability: not yet complete until canonical verdict/provenance serialization is defined.**

Recommended next bounded test after correcting the deliberate subject defect and canonical record schema: repeat the same A/B review expecting GREEN and compare the resulting durable records field-for-field after excluding transport-only runtime logs.


### Live-test interpretation correction

The first A/B live test must not be overclaimed.

What was actually tested:
- ChatGPT B: a manually created fresh ChatGPT chat could recover and execute the runtime-neutral review obligation.
- Codex A: Codex Main/runtime could realize the independent-review obligation through its installed orchestration without the Project Workflow record naming a worker role.

What was **not** tested on ChatGPT B:
- whether the initiating ChatGPT context independently detects that it lacks a qualifying delegated independent-context capability;
- whether it automatically chooses the fresh-context fallback;
- whether it emits the correct durable handoff/STOP without the user pre-creating the fresh chat.

Therefore ChatGPT B is evidence for **handoff target recoverability**, not evidence for the proposed capability resolver.

Codex A also reflects the currently installed legacy `codex_workflow` behavior: it selected a Muse exec-backed worker. This validates runtime-owned realization/no Project Workflow worker-name requirement, but does not validate the intended future native-Codex-subagent implementation. That mechanism must be retested after `codex_workflow` is updated.

Corrected next live test:
1. create one pending runtime-neutral independent-review obligation;
2. remain in the initiating ChatGPT context;
3. instruct it only to continue the obligation under the capability-first rule, without manually opening a fresh chat and without telling it which transport to use;
4. PASS requires the initiating ChatGPT context to determine that no qualifying native/delegated independent context is available, preserve the pending durable obligation, generate a locator-only fresh-context handoff, and STOP without issuing the verdict itself;
5. then run that generated handoff in a fresh chat and verify recovery/verdict;
6. after the future `codex_workflow` native-subagent change, run the same initiating-context test in Codex and require internal independent realization without a user handoff.


## Research needed

No external research is currently required. The next useful evidence is repository-internal: routing/read-set constraints, current tests and how common modules are already composed elsewhere.

## Open questions

1. Should policy routers still route to `workflow/<policy>/BRAINSTORMING.md` etc., where those files become tiny adapters, or should they route directly to `workflow/common/BRAINSTORMING.md` when no adapter is needed?
2. For Intake and Planning, do we want one common contract with explicit policy hook points, or a common lifecycle contract plus separate short policy supplements?
3. Do we want the end state to remove duplicated policy-local files entirely when there is zero policy delta (likely Brainstorming/Definition), or preserve tiny forwarding files for namespace symmetry and discoverability?

## Outcome of this session

- Tentative conclusions: Brainstorming, the promotion gate and Definition should be fully common. Research can likely be fully common because Codex Investigator dispatch is already governed by the generic orchestration boundary. Planning can likely be fully common if review realization and Context Health remain router/review concerns. Intake has one real Codex-only orchestration-binding establishment step; this is the only stage in 1–6 that still clearly needs a policy-specific hook unless binding establishment is deliberately moved/lazily deferred.
- Explicit user/product choices to promote through Project Definition: none yet.
- Research still needed: repository-internal architecture/test inspection before choosing the exact composition mechanism.
- Open questions: composition model, adapter placement, direct-common routing versus forwarding policy modules, migration/test shape.
- Next phase/action: `continue brainstorming`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`. When the selected policy requires explicit user phase promotion, only an explicit user instruction may set `Definition promotion authorization: user_authorized`, and the authorization must name the exact current `<scope-id>@<revision>`. Any material change to the exploratory scope before Definition starts creates a new revision and resets authorization to `pending`.
