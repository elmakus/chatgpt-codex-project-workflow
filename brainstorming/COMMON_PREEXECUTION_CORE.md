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


### Live test C — initiating-context capability resolution

A cleaner live test was prepared at:

`brainstorming/live-tests/CAPABILITY_PLAN_REVIEW_C.md`

It points to the same immutable review subject as A/B but changes what is being tested. The first context is explicitly the initiating/coordinating context and is forbidden from issuing the verdict itself. It receives only a runtime-neutral semantic obligation plus a capability-first realization rule.

PASS criteria for the first context:
- do not infer behavior from product identity;
- determine whether a qualifying independent execution context can actually be realized with mechanisms available in the current runtime;
- if available, realize it internally;
- if absent, preserve the same pending obligation, emit a locator-only fresh-context continuation prompt, and STOP;
- if available but invocation fails, retain pending state and route runtime failure/retry/blocker handling rather than treating the capability as absent.

This test specifically targets the capability resolver / automatic handoff generation that live test B did not test.


### Live test C — initiating ChatGPT capability resolver PASS

The initiating ChatGPT context was given only the durable pointer `brainstorming/live-tests/CAPABILITY_PLAN_REVIEW_C.md` and was not told which transport branch to choose.

Observed behavior:
- it recovered the exact obligation and immutable subject from repository state;
- it recognized that the current context was forbidden to issue GREEN/RED;
- it determined that no qualifying independent-context mechanism was available in the current runtime;
- it preserved `Review state: pending` and did not mutate the immutable subject;
- it emitted a locator-only fresh-context continuation prompt pointing back to the exact review record;
- it stopped at the user handoff boundary without issuing a verdict;
- it did not select behavior from product identity or require a concrete worker-role name.

Repository verification after the response confirmed the review record remained `pending` and the immutable subject remained unchanged.

Verdict for the first half of live test C: **PASS** for capability-first absence detection + automatic fresh-context handoff generation.

The second half (fresh context consuming the generated prompt and completing the review) remains to be run if end-to-end confirmation is desired.


### Live test C — fresh-context continuation FAIL (handoff bounce)

The second half of live test C exposed a durable-contract bug.

Observed:
- the first ChatGPT context correctly detected absence of a qualifying delegated independent context, preserved `pending`, emitted a locator-only fresh-context handoff and stopped;
- the user opened a fresh ChatGPT chat with that generated handoff;
- the fresh chat re-read the durable record and again concluded that the context receiving the record is the initiating/coordinating context forbidden from issuing a verdict;
- it therefore emitted another fresh-context handoff instead of performing the review.

This is a **handoff bounce** caused by the durable contract, not by product detection.

Root cause:
the record says:

`the context that receives this record as its current obligation is the initiating/coordinating context and MUST NOT issue the review verdict itself`

That statement is permanently true for every context that follows the durable pointer, including the intended fresh reviewer. Because the handoff prompt is explicitly non-authoritative, its statement that the new chat is fresh cannot override the durable record.

Implication:
capability-first routing needs a runtime-neutral durable distinction between:
- the context responsible for **realizing** an independent obligation; and
- the independent context that is **authorized to execute** that obligation.

The distinction must survive runtime transfer without relying on previous-chat narrative or product identity.

Candidate correction:
- keep one semantic review obligation;
- add a neutral lifecycle/ownership marker that changes durably before the handoff, e.g. `realization_state: awaiting_independent_context` or equivalent;
- an initiating context with no qualifying delegation capability transitions the record to that state, persists it, emits the locator-only handoff and stops;
- a new context recovering `awaiting_independent_context` may establish that it is a distinct context and execute the review directly, rather than trying to resolve another independent context;
- this marker must not encode `ChatGPT`, `Codex`, worker names, model names, or runtime session IDs.

The exact schema is still exploratory. The key invariant is: **a durable handoff must change enough state to distinguish "create an independent context" from "you are now the independent context", otherwise fresh-context fallback can recurse forever.**

Verdict:
- initiating-context capability resolution: PASS;
- fresh-context continuation: FAIL;
- end-to-end ChatGPT fallback: FAIL until the durable role/lifecycle transition is specified.

This failure is useful evidence for the portability design and should be fixed before treating stage-7 commonization as settled.


### Live test D — durable handoff-state correction

A follow-up live test was prepared at:

`brainstorming/live-tests/CAPABILITY_PLAN_REVIEW_D.md`

Purpose: validate the proposed fix for the handoff bounce found in test C.

The experiment introduces a runtime-neutral durable realization state machine:

`resolve_independent_context`
→ `awaiting_independent_context`
→ `independent_context_active`
→ `satisfied`

Key invariant:
- the context that writes `awaiting_independent_context` must stop and may not execute the review;
- a later fresh context recovering `awaiting_independent_context` is no longer responsible for finding another independent context; if it satisfies the independence conditions, it becomes the reviewer and executes the obligation directly.

No product, worker, model, harness or runtime-session identity is encoded in the Project Workflow record.

This test specifically checks that a durable state transition, rather than handoff-prompt narrative, is sufficient to prevent recursive fresh-context bounce.


### Live test D — end-to-end durable handoff-state PASS

Live test D completed successfully across two normal ChatGPT contexts.

Verified sequence:
1. first context recovered `resolve_independent_context`, found no qualifying delegated independent-context mechanism, durably transitioned the record to `awaiting_independent_context`, preserved `Review state: pending`, emitted the locator-only handoff, and stopped without verdict;
2. second fresh context recovered `awaiting_independent_context` and did not bounce;
3. before judging the subject it durably transitioned to:
   - `Review state: in_progress`
   - `Realization state: independent_context_active`
   in commit `917552aa55f51ace2859b1c0baedb84ce0536799`;
4. it then independently reviewed the exact immutable subject and persisted:
   - `Review state: completed`
   - `Review verdict: RED`
   - `Realization state: satisfied`
   - concise evidence
   in commit `9e0c0915a47152feb10d93b5075d54bd4ba5de4f`;
5. the immutable subject remained unchanged with blob SHA `9f082055f79c7146dc19abbd84cd49d6d56fdf44`.

The RED is expected and matches prior independent reviews: the test subject deliberately omits the `capability present + invocation fails` case.

Conclusion:
- durable handoff-state transition fixes the recursive fresh-context bounce observed in test C;
- normal ChatGPT can implement the runtime-neutral capability-first fallback end-to-end without product-name branching or concrete worker-role names;
- a fresh context can infer from durable state that it is now the independent executor rather than another realization coordinator;
- this state-machine pattern is a strong candidate for common independent-context obligations beyond plan review.

Bounded challenge still open: determine whether `realization_state` belongs as a reusable generic common obligation primitive or whether each obligation type should own an equivalent lifecycle locally. Avoid introducing a generic abstraction unless at least one additional obligation demonstrates the same state shape.


### Stage 8 audit — Execution Prep / JIT (current main `7aa7512ead67a86256089d1af0171e2e655e700d`)

No workflow change is authorized yet. This is a current-state audit plus a proposed direction for discussion.

#### Current ChatGPT-only shape

`workflow/chatgpt_only/EXECUTION_PREP.md` contains the richer common preparation lifecycle:
- accepted-authority / approved-plan or qualified-micro-fix preconditions;
- branch-isolated workstream + manifest-bound Task Board ownership;
- full crash-safe Research return/reconciliation protocol;
- Execution Prep → Research handoff;
- qualified micro-fix materialization;
- JIT decomposition and deferred-Card triggers;
- exact authority slices / must-preserve constraints;
- bounded scope, acceptance, tests, external readback, review classification and OpenSpec;
- incremental L2/JIT refinement;
- authority/evidence/Git/handoff rules;
- automatic return to router after preparation.

It also encodes runtime-specific serial behavior:
- preparation step 16 sets **exactly the next eligible Card** `ready`;
- `ChatGPT is the fixed executor`;
- no executor/capability selection;
- downstream `STATE.md` makes more than one Card `in_progress` invalid.

Its Task Card contract has no concurrency-safety metadata.

#### Current Codex-only shape

`workflow/codex_only/EXECUTION_PREP.md` shares the basic Card/JIT principles but compresses several common lifecycles (especially Research/micro-fix detail) and adds an M03 bounded-parallel scheduler layer:
- optional Card `parallel_safe`, `write_scope`, `exclusive_resources`;
- mark next executable Card(s) READY;
- normalize write/resource claims;
- greedily build a compatible READY set;
- resolve one exact integration base;
- ask runtime whether isolated mutable workspaces exist;
- freeze stable batch/lane IDs (`B01`, `L01`, ...);
- mark batch members `in_progress` before runtime launch;
- persist batch membership/base/history in Task Board;
- revalidate safety immediately before launch;
- prepared-batch abandonment/recovery semantics.

It also persists semantic role wording such as `implementation_owner_role: executor`.

#### Core semantic mismatch

Current ChatGPT `READY` partly means “the one Card this serial runtime should execute next”. Current Codex `READY` can represent several simultaneously executable Cards.

That makes readiness depend on runtime scheduling capability, which conflicts with cross-runtime portability.

Proposed invariant:

`READY = this Card is legally executable now from project authority/dependencies/prerequisites.`

Runtime selection is separate:

`SELECTED FOR EXECUTION = the current runtime chose this READY Card now.`

For example, if T01 and T02 have no dependencies and T03 depends on both, common durable state after preparation should be:
- T01 READY
- T02 READY
- T03 blocked/planned behind dependencies

A serial runtime may execute T01 then T02. A concurrency-capable runtime may execute T01+T02 concurrently. Neither runtime should rewrite project readiness merely because of its capability surface.

#### Proposed common Stage-8 ownership

A common `EXECUTION_PREP.md` should own:
- accepted authority / plan / micro-fix preconditions;
- exact selected workstream + canonical Task Board;
- Research return/handoff/reconciliation;
- JIT decomposition and durable triggers;
- Task Card creation/refinement for not-yet-started work;
- exact dependencies and authority slices;
- included/excluded scope;
- acceptance/tests/readback;
- review requirement;
- OpenSpec candidate handling;
- requirement coverage and strategic-boundary checks;
- marking **all currently executable Cards READY**;
- automatic return to routing/execution when at least one READY Card exists and no real gate intervenes.

It should not own:
- product identity;
- fixed executor names;
- concrete worker-role names;
- capability inventory by product;
- batch/lane IDs;
- worker/worktree allocation;
- concrete runtime concurrency selection;
- pre-launch runtime worker dispatch.

#### Concurrency-safety metadata proposal

Some project-level safety facts should remain portable because they are useful regardless of which runtime later executes the Card.

Candidate optional Card metadata:
- bounded repository `write_scope`;
- `exclusive_resources` for non-path conflicts.

These are correctness/ownership facts, not worker identities.

Open design choice:
- retain an explicit neutral opt-in such as `concurrency_safe: true`; or
- treat complete valid concurrency-safety metadata as the opt-in and remove the boolean.

Recommended direction for discussion: keep the metadata optional and JIT. Absence never blocks serial execution. Do not force every Card to predict scopes that are not useful/knowable. A runtime considering concurrency may use only Cards with a complete safety proof.

The current Codex-specific `parallel_safe` name and scheduler semantics need not survive as-is.

#### Batch mechanics boundary

Current Codex Execution Prep freezes `Bxx/Lxx` batches before Execution. Proposed Stage-8 commonization should remove that scheduler action from Execution Prep.

Execution Prep should end with a truthful READY set plus optional concurrency-safety facts. The current runtime decides how many READY Cards to select.

Exact durable state needed after actual concurrent execution starts (integration base, concurrent attempts, partial results, recovery) belongs to the Stage-9 Execution/State audit; do not prematurely classify all of it as runtime-only because some may be required for crash recovery and cross-runtime takeover.

#### Existing common semantics to prefer

The ChatGPT-only Execution Prep currently has the more complete common JIT/Research/micro-fix lifecycle and should be the semantic baseline for commonization. The Codex-only parallel-safety ideas should be selectively merged into that baseline rather than replacing it.

Task Card commonization should similarly start from the richer ChatGPT Card authority/JIT contract and add only runtime-neutral optional concurrency-safety facts from Codex.

#### Downstream issues intentionally deferred to Stage 9

The following are visible now but should not be solved as part of Stage 8:
- ChatGPT `executor: chatgpt` provenance;
- Codex `implementation_owner_role: executor`;
- whether multiple `in_progress` Cards are common-valid state;
- exact durable concurrent-attempt/batch/integration provenance;
- takeover while runtime workers are actively executing;
- runtime-specific recovery/resume state.

Those belong to Execution/State because they arise only after a READY Card is actually selected/launched.


### Stage 8 direction — tentatively accepted

The user tentatively accepted the Stage-8 direction for further validation:

- common Execution Prep owns project-legality/JIT preparation, not runtime scheduling;
- `READY` means a Card is legally executable now from project authority/dependencies/prerequisites;
- all currently executable Cards may be READY simultaneously;
- runtime selection/concurrency is deferred to Execution;
- ChatGPT serial capability must not suppress otherwise-legal READY state;
- Codex parallel capability must not change Project Workflow readiness semantics;
- optional runtime-neutral concurrency-safety facts may remain on Cards, while concrete batch/lane/worker/workspace mechanics are not Stage-8 preparation state;
- exact concurrent-attempt/recovery state remains deferred to the Stage-9 audit.

This is still Brainstorming acceptance, not Definition promotion authorization.


### Live test E — Stage-8 READY parity

Prepared two equivalent live records:
- `brainstorming/live-tests/CAPABILITY_EXECUTION_PREP_E_A.md`
- `brainstorming/live-tests/CAPABILITY_EXECUTION_PREP_E_B.md`

Both point to the same immutable synthetic milestone subject:
`bb1bf611bdd883567d642c020c4fd35feecdf88a:brainstorming/live-tests/CAPABILITY_EXECUTION_PREP_E_SUBJECT.md`

Synthetic graph:
- T01: no dependencies;
- T02: no dependencies;
- T03: depends on T01 + T02.

The live test is intentionally bounded to Execution Prep. It forbids Card execution, worker selection and batch/lane creation.

Target property:
- both runtimes must derive readiness solely from project legality;
- expected READY set is T01 + T02;
- T03 remains non-READY until both dependencies are done;
- runtime serial/parallel capability must not alter the READY set.

A/B records are separate only so each runtime can mutate its own durable result without racing the other.

Counterfactual challenge: if a runtime marks only one of T01/T02 READY because it intends to execute serially, that is evidence that scheduling remains incorrectly encoded in Stage-8 project state. If it creates a batch or starts work, it has crossed the intended Stage-8/Stage-9 boundary.


### Live test E-B — ChatGPT Stage-8 readiness result

ChatGPT completed the E-B Stage-8-only reconciliation and persisted commit `257159e734fa29b5e11d1e263467e7bb38770c00`.

Verified durable result:
- T01: `ready`
- T02: `ready`
- T03: `planned`
- Preparation state: `completed`

The record explicitly states that runtime scheduling capability/product identity were not used and no Execution worker/batch/workspace action was taken.

Verdict for ChatGPT side only: **PASS**.

Cross-runtime READY parity remains pending until E-A completes in Codex.


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
