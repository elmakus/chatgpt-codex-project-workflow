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

### Orchestration-topology preservation — explicit user direction

The common-core refactor MUST preserve runtime/policy freedom in how a sequence of semantic obligations is realized.

The intended behavior is:

- **Codex-capable orchestration may remain one-shot across many workflow roles.**
  A coordinating context may continue through deterministic stages, delegate independent review, consume GREEN, route RED to correction, delegate the next independent recheck, and continue again without a user-facing stop whenever no real authority/runtime boundary exists.

- **Normal ChatGPT may continue deterministically after review in the same chat.**
  After a fresh independent-review chat returns GREEN, that chat leaves reviewer role and may immediately continue through post-review finalization and later deterministic routes.
  After RED, the same chat may leave reviewer role and perform a bounded authorized correction/replanning/research route when the router assigns it.

- **Independence is per exact reviewed subject, not per whole chat/session.**
  If a ChatGPT review chat performs the correction and thereby materially produces the corrected subject, it becomes a producer for that new subject and cannot independently review it. A new independent context is then required for the next review attempt.
  Likewise, a Codex runtime may reuse or replace logical runtime realizations only when independence for the exact subject remains valid.

Therefore the common semantic contract must NOT:
- require a user/chat stop after every GREEN or RED;
- require one orchestration topology for all runtimes;
- encode `fresh ChatGPT chat` or `Tester/Executor` as the semantic rule;
- prevent a capable coordinator from completing an entire deterministic chain in one user invocation.

The common layer should define durable obligations, subject independence and real-stop conditions; runtime/policy realization decides whether those obligations are handled through delegated contexts, role transitions inside one coordinating invocation, or a fresh-context handoff.

This behavior is already present in current fixed-policy contracts and is a compatibility invariant for commonization.

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


### Live test E — cross-runtime Stage-8 READY parity PASS

Both E records completed against the same immutable subject.

ChatGPT E-B:
- T01 `ready`
- T02 `ready`
- T03 `planned`
- no Execution entered
- no worker/batch/workspace selection
- commit `257159e734fa29b5e11d1e263467e7bb38770c00`

Codex E-A:
- T01 `ready`
- T02 `ready`
- T03 `planned`
- no Execution entered
- no worker/batch/workspace selection
- commit `8a5d08af2cf21bf8568613e6329336d8f17c8973`

Both durable records derive the same READY set solely from project legality/dependencies and explicitly exclude runtime scheduling capability/product identity from readiness.

Verdict: **PASS — cross-runtime Stage-8 readiness semantics are portable.**

Observed Codex runtime restarts/contention during the run did not alter the final durable result. Treat this only as incidental robustness evidence, not as a controlled recovery test.

Stage-8 working conclusion:
- common Execution Prep can own a truthful runtime-neutral READY graph;
- serial/parallel selection belongs after the Stage-8 boundary;
- Stage 9 must now define portable execution-state semantics, including clean takeover after a completed Card and safe behavior/checkpointing when concurrent work is active.


### Stage 9 audit — Execution / State (current main `7aa7512ead67a86256089d1af0171e2e655e700d`)

No Stage-9 workflow change or live test is authorized yet. This section records the current-state audit and a proposed runtime-portable direction for discussion.

#### Current ChatGPT-only execution shape

`workflow/chatgpt_only/EXECUTION.md` + `STATE.md` implement one direct serial execution loop:
- select exactly one deterministic READY Card;
- persist `ready -> in_progress`;
- persist `executor: chatgpt` plus branch/base recovery pointer;
- run Refresh Gate;
- implement in the coordinating chat;
- persist exact result/tests/evidence;
- freeze independent review when required, otherwise mark `done`;
- return to router at the durable Card boundary.

State invariant:
- exactly one Card may be `in_progress` per selected workstream Task Board;
- more than one is invalid state.

Recovery of an ordinary `in_progress` Card is intentionally simple:
- verify branch/HEAD against Task Board;
- inspect actual implementation/tests/evidence;
- run Refresh Gate;
- continue from proven durable state;
- do not blindly repeat completed steps.

This model has no durable concurrent-attempt state.

#### Current Codex-only execution shape

`workflow/codex_only/EXECUTION.md`, `STATE.md` and `RECOVERY.md` support both serial execution and a durable bounded-parallel lifecycle.

Serial path is semantically similar to ChatGPT:
- choose READY Card;
- persist `in_progress`;
- execute through runtime;
- persist result/tests/evidence;
- freeze review or finalize;
- return to router.

Codex-specific/runtime-coupled state currently includes:
- `Codex Main` as fixed coordinator;
- `implementation_owner_role: executor`;
- orchestration pre-dispatch binding;
- explicit worker-role language (`Executor`, `Tester`).

Parallel project state currently includes:
- one `parallel.current_batch`;
- stable batch IDs and lane labels;
- exact `integration_base`;
- frozen finite member order;
- batch states `prepared -> running -> integrating -> complete | blocked`;
- member states `prepared -> in_progress -> returned -> integrated | blocked`;
- exact returned and integrated result refs;
- deterministic ordered integration;
- preserved partial results;
- same-member retry or terminal reconciliation;
- post-batch review drain.

Recovery already has an important runtime-neutral property: concrete worker/session/model/worktree identity is not authority. A `returned` durable result is not rerun merely because runtime disappeared.

#### What is already naturally portable

A terminal Card is already conceptually runtime-neutral once durable truth is complete:
- `execution_status: done`;
- exact result ref;
- tests/evidence/readback;
- required review satisfied;
- dependencies can be recomputed into READY state.

Therefore a clean boundary after a completed Card should require no product-specific handoff. A different runtime can reconstruct the same Task Board and select the next legal obligation.

The current blockers to literal interchangeability are schema/provenance differences such as `executor: chatgpt` vs `implementation_owner_role: executor`, policy-specific review shapes and policy namespaces, not the underlying Card semantics.

#### Proposed common Execution ownership

Common Stage 9 should own project-level execution semantics:
- deterministic priority of already-active durable obligations before new work;
- READY -> selected/start transition;
- Refresh Gate;
- exact Card authority/scope/acceptance/tests/readback;
- durable active execution state;
- exact implementation result/evidence;
- Card review freeze boundary;
- terminal `done` semantics;
- RED correction / Research routing;
- recovery from partial durable transitions;
- cross-runtime takeover rules.

It should not own:
- product identity;
- fixed `ChatGPT` / `Codex Main` identity;
- concrete `Executor` / `Tester` names;
- model/profile/session/invocation/worktree IDs;
- runtime-specific worker lifecycle.

A neutral rule can replace `Codex Main`: the **coordinating context** is the only writer of shared Project Workflow state; delegated realizations return bounded results/evidence and do not mutate the shared Task Board/manifest/integration bookkeeping. In a non-delegating runtime, the same context may both coordinate and implement.

#### Selection after the Stage-8 READY graph

Stage 8 leaves all legally executable Cards READY.

Stage 9 asks the runtime how much of that READY set it can safely realize:
- serial-only runtime selects one;
- concurrency-capable runtime may select a compatible subset whose concurrency-safety proof is valid.

This selection is HOW, not project readiness.

However, **once work actually starts**, enough runtime-neutral durable state must be persisted to recover or transfer it. Runtime choice itself may be transient; its consequences cannot be transcript-only.

#### Candidate neutral active-execution model

Replace policy-specific serial-vs-batch semantics with a common concept such as an `active_execution` / execution set.

Conceptual shape, not yet a schema commitment:

```yaml
active_execution:
  id: X01
  state: active | reconciling | transfer_ready | complete | blocked
  base_ref: <exact durable base>
  members:
    - card_id: T01
      state: active | result_ready | reconciled | quiesced | blocked
      result_ref: null
      canonical_result_ref: null
```

Properties:
- one member is ordinary serial execution;
- two or more members represent concurrent execution;
- no worker/lane/model/session identity is required;
- member ordering may provide deterministic reconciliation order when concurrent results must be integrated;
- direct serial execution may collapse `result_ready -> reconciled` into one durable transition when result is already on the canonical workstream branch;
- delegated isolated work can preserve a separate returned/result-ready boundary before canonical reconciliation.

This is intended to preserve the useful recovery semantics of today's Codex batch without making `B01/L01/Executor/Codex Main` part of the common contract.

Open question: whether a universal execution-set wrapper is worth the overhead for one-member serial work. A lighter alternative is per-Card execution-attempt state plus an optional concurrent-group record only when >1 Card is launched. This should be decided after validation, not assumed.

#### Clean takeover after a completed Card

Target behavior:

```text
T01 done + exact result/evidence
T02 ready
no unresolved active_execution

switch runtime

new runtime reads durable state
-> does not care who executed T01
-> selects next legal obligation
```

No special user handoff should be semantically required. The next runtime reconstructs from repository truth.

Concrete provenance such as `executor: chatgpt` should disappear from required project semantics. If producer provenance is needed for independent-review proof, use neutral subject/execution provenance rather than product/worker names.

#### Takeover while a serial Card is still active

A runtime switch must not cause two contexts to mutate the same Card concurrently.

Therefore an active Card needs one of:
- completion to a terminal/durable result boundary; or
- a durable transfer/checkpoint transition that proves the previous realization has stopped/quiesced and records enough state for continuation.

A new runtime must never infer from absence of transcript that the previous realization is gone.

#### Takeover in the middle of concurrent work

The current Codex batch model already preserves useful facts: frozen base, member set/order, returned results, integrated results and blockers. The common model should preserve equivalent facts but add an explicit cross-runtime transfer boundary.

Proposed safe model:
1. current coordinating context requests/establishes a **quiescent checkpoint**;
2. every member is durably classified as one of:
   - result already durable;
   - reconciled/integrated;
   - quiesced with no accepted result yet;
   - blocked with exact evidence;
3. no old realization is allowed to continue mutating authoritative/shared/external state after the checkpoint;
4. persist `transfer_ready` (name tentative);
5. old coordinating context stops;
6. new runtime reconstructs the same active execution from durable state:
   - never reruns durable returned/reconciled results;
   - may reconcile returned results;
   - may re-realize only quiesced unresolved members under the same still-valid Card authority/base/safety constraints;
   - may choose to continue remaining unresolved work serially even if the previous runtime had executed concurrently.

If quiescence cannot be proven, fail closed rather than launch duplicate work.

This gives safe cross-runtime takeover without requiring true hot migration of runtime sessions.

#### Important external-write caveat

Repository-isolated workers are relatively easy to replace because stale returned commits can be ignored/reconciled. Material external writes are different: an old realization that might still mutate an external system cannot safely be duplicated.

Therefore cross-runtime transfer of an active Card with external side effects requires exact quiescence/idempotency/readback evidence before replacement. Runtime loss alone is not proof that an old external mutation cannot still occur.

This correctness property belongs in common Project Workflow even though the concrete cancellation mechanism is runtime-owned.

#### Review provenance cleanup

Current ChatGPT stores `executor: chatgpt`; Codex stores `implementation_owner_role: executor` and review `reviewer_role: tester`.

Target should not require those product/role names.

Common state needs only enough neutral provenance to establish:
- exact implementation subject/result;
- which execution attempt produced it;
- whether the review context is independent of that producing context.

The Stage-7 independent-context realization lifecycle can then be reused conceptually for Card review without hardcoding `Tester`.

Do not yet generalize the exact schema until the Stage-9/Review interaction is validated.

#### Proposed Stage-9 working direction

1. Commonize the serial Card lifecycle and recovery semantics.
2. Remove product/worker identity from required project state.
3. Make multiple active Cards legal only when covered by one exact durable active-execution/concurrency record.
4. Move Codex's useful returned/integrated/recovery facts into runtime-neutral execution-state terminology.
5. Allow a runtime that cannot continue concurrency to finish/recover remaining members serially after a proven transfer checkpoint.
6. Define clean Card-boundary runtime switching as ordinary recovery/continuation, not a special workflow.
7. Define active-work switching as a durable quiesce/checkpoint protocol; no blind hot takeover.
8. Keep concrete orchestration, worker choice, cancellation, resume and workspace handling runtime-owned.
9. Preserve fail-closed behavior for uncertain runtime-active/external-write state.

#### Proposed validation after user approval

Do not run yet.

A. **Completed-Card takeover test**
- one runtime executes T01 to terminal durable `done`;
- another runtime starts from only durable state;
- it must recognize T01 as complete, T02 as next READY and must not replay T01.

B. **Serial in-progress checkpoint takeover**
- first runtime starts T01 and persists a bounded checkpoint/transfer-ready state;
- second runtime resumes/continues T01 without duplicating already durable work.

C. **Mid-concurrency takeover**
- runtime A starts T01+T02 concurrently;
- one member becomes durable result, the other reaches a proven quiescent unresolved checkpoint;
- switch to a serial-only runtime;
- it must preserve/reconcile the completed member and continue only the unresolved member serially;
- T03 becomes READY only after both are terminal.

D. **Unsafe takeover negative case**
- old realization may still perform a non-idempotent external write and quiescence cannot be proven;
- new runtime must fail closed, not duplicate the operation.


### Stage 9 direction — tentatively accepted

The user tentatively accepted the proposed runtime-portable Stage-9 direction for live validation:

- common execution semantics own durable Card/result/review/recovery truth;
- Stage-8 READY remains runtime-neutral;
- runtime selects serial vs compatible concurrent realization;
- product/worker/model/session identity is not required Project Workflow state;
- completed-Card runtime switching is ordinary durable continuation;
- active-work switching requires a durable quiesce/checkpoint boundary rather than blind hot migration;
- concurrent work must preserve enough runtime-neutral durable result/reconciliation state for another runtime to take over safely;
- uncertain still-active or external-write execution fails closed rather than being duplicated;
- concrete orchestration/cancellation/resume/workspaces remain runtime-owned.

This remains Brainstorming acceptance, not Definition promotion authorization.


### Live test F — completed-Card cross-runtime takeover

Prepared durable live test:
- record: `brainstorming/live-tests/CAPABILITY_EXECUTION_F.md`
- immutable subject: `6e580867cc3090ef59efbede19d8e6fb17cb8c31:brainstorming/live-tests/CAPABILITY_EXECUTION_F_SUBJECT.md`

The test uses real isolated repository outputs:
- T01 writes `brainstorming/live-tests/execution-f/A.txt`;
- T02 depends on T01 and writes `brainstorming/live-tests/execution-f/B.txt`.

The common test contract uses a one-member runtime-neutral `Active execution` wrapper even for serial work. Each context must durably mark start, execute exactly one Card, persist its result, clear active execution, recompute readiness, and STOP at the completed-Card boundary.

Phase 1 is intended for Codex; Phase 2 for normal ChatGPT. Product identity is not part of the durable contract. PASS requires the second runtime to preserve T01 and execute only T02 from repository truth.

This first Stage-9 test does not yet test in-progress transfer or concurrent execution.


### Live test F — completed-Card cross-runtime takeover PASS

The two-runtime execution test completed successfully against one shared durable record.

Phase 1 — Codex:
- durably started T01 under one-member active execution X01;
- created only `brainstorming/live-tests/execution-f/A.txt`;
- exact T01 result commit: `8d7a8224f85eb0e8c86c48029886af7d049fda0d`;
- completion-state commit: `bf7833def24e52e3b2d71fe9215b6fcc6ca0e0e8`;
- persisted T01 `done`, T02 `ready`, `Active execution: null`;
- stopped at the completed-Card boundary.

Phase 2 — normal ChatGPT:
- recovered the same durable record with T01 already terminal;
- verified accepted T01 result instead of re-executing it;
- durably started only T02 as X02 in `ea28ea2a3d152b92c5e98e5eb4bdbab7fc2704d8`;
- created only `brainstorming/live-tests/execution-f/B.txt`;
- exact T02 result commit: `00fb4871f22e719bc4f454c0c9372c588fd968fc`;
- completion-state commit: `f85786ee4ecb82646476433cf268a4d53621dff0`;
- persisted both Cards `done` and `Active execution: null`.

Verification:
- T02 result commit changes only B.txt;
- A.txt remains exactly the T01 blob `ba78e7baacc4a3930ac0f2744d6a1db6ba9662ab`;
- final A/B contents match the immutable subject;
- no product/worker/session conversion schema was needed between runtimes.

Verdict: **PASS — a completed Card boundary is a portable cross-runtime continuation boundary.**

This validates the intended normal case:
`Codex completes Card -> durable repository truth -> ChatGPT continues next Card`.
The reverse direction remains worth one bounded counterfactual test only if implementation details differ materially; semantically the tested contract is symmetric.

#### F schema finding

The synthetic record still says top-level `Execution state: active` after both Cards are done while `Active execution: null`.

This does not invalidate the takeover result because the test contract routes from Card state + `Active execution`, but it exposes an avoidable ambiguous duplicate lifecycle.

Working direction:
- prefer one authoritative active-execution lifecycle plus Card states;
- do not keep an additional generic `Execution state` unless it has a distinct, necessary meaning with exact transitions.


### Live test G — active-Card checkpoint takeover

Prepared:
- durable record: `brainstorming/live-tests/CAPABILITY_EXECUTION_G.md`
- immutable subject: `82cac004ad0c47e4d94e766aaabf604d84e2f748:brainstorming/live-tests/CAPABILITY_EXECUTION_G_SUBJECT.md`

T01 intentionally spans two bounded units:
- Unit A creates a durable prefix and becomes the transfer checkpoint;
- Unit B completes the same Card after takeover.

Phase 1 must leave:
- T01 `in_progress`;
- execution attempt `X01`;
- `state: transfer_ready`;
- member `state: quiesced`;
- exact Unit-A `checkpoint_ref`;
- no old realization still able to mutate T01;
- then STOP.

Phase 2 must preserve X01, verify and not replay Unit A, reactivate the same execution attempt, execute only Unit B, then complete T01.

This deliberately tests that runtime/context switching does not imply a new project execution attempt.

Bounded challenge: the synthetic test can prove quiescence because it has only synchronous repository-local work. A later test must separately validate the negative case where quiescence of a detached worker or external side effect cannot be proven; that case must fail closed.


### Live test G — active-Card checkpoint takeover PASS

The repository is sufficient to verify the full test; no chat transcript is required.

Verified durable sequence:

1. `8413cdb9da798a346d3840c94bd8df904c107afb`
   - T01 `ready -> in_progress`
   - execution attempt `X01` created as `active`

2. `9625b8de23914975acc09e8a3549332c46c16287`
   - Unit A only
   - creates `execution-g/part1.txt`
   - exact content matches immutable subject

3. `91baa2ba052b29f3494b1018739419b5f9234741`
   - T01 remains `in_progress`
   - same X01 transitions `active -> transfer_ready`
   - member transitions `active -> quiesced`
   - exact checkpoint ref persisted
   - durable evidence states no delegated/detached realization was used and X01 is quiesced

4. `8e4d5ddd32025de1c773accb88d7fec0f7885046`
   - same X01 transitions back to `active`
   - checkpoint ref is preserved
   - no new project execution attempt is created

5. `19a99fbbff3f9d05f62907274f9a4fea505c3dd9`
   - Unit B only
   - creates `execution-g/part2.txt`
   - compare from checkpoint to result shows no modification to `part1.txt`

6. `d97a3607d0278702b2b83dc4b1b95d45bcfae2b4`
   - T01 becomes `done`
   - exact T01 result ref persisted
   - Active execution becomes null
   - evidence records preserved checkpoint and unchanged Unit A

Final artifacts:
- `part1.txt`: exact Unit-A content
- `part2.txt`: exact Unit-B content

Verdict: **PASS — one non-terminal repository-local Card can transfer across contexts/runtimes at a durable quiescent checkpoint while preserving the same project execution attempt.**

What this proves:
- durable `transfer_ready/quiesced` state is sufficient for takeover without prior-chat narrative;
- completed checkpoint work is not replayed;
- runtime/context switch does not require a new project execution attempt;
- Project Workflow can distinguish an unsafe active realization from a transferable quiesced one.

What this does NOT yet prove:
- cancellation/quiescence of a detached runtime worker;
- takeover while multiple concurrent members are active;
- safety for non-idempotent external side effects.

The next materially distinct validation target is concurrent takeover rather than the reverse-direction version of this same serial checkpoint test.


### Live test H — concurrent execution-set takeover

Prepared:
- durable record: `brainstorming/live-tests/CAPABILITY_EXECUTION_H.md`
- immutable subject: `3f18dd1483dc5bb4cd42257c47bf0187d55f9c14:brainstorming/live-tests/CAPABILITY_EXECUTION_H_SUBJECT.md`

H validates a materially distinct Stage-9 property from F/G.

Phase 1 requires actual concurrent isolated realization of:
- T01 to full completion;
- T02 only through checkpoint Unit B1.

The coordinator then reconciles both outputs into canonical durable state and freezes:
- T01 `done / reconciled`;
- T02 `in_progress / quiesced`;
- X01 `transfer_ready`;
- T03 still `planned`.

Phase 2 may run in a serial-only runtime. It must preserve T01 and B1, reactivate the same X01 only for unresolved T02, execute B2 serially, finish T02, and make T03 READY.

Important bounded interpretation:
- this tests concurrency followed by takeover after all old member realizations have already stopped/returned;
- it does not yet prove forced quiescence/cancellation of a still-live detached worker;
- it does not test external side effects.

The test fails as a concurrency validation if Phase 1 silently executes T01 and T02/B1 serially.


### Live test H — concurrent execution-set takeover PASS with concurrency-evidence caveat

The H durable record reached the intended final state:

- T01 `done`, result `2a48259a9e1bbb3086581f3d88bc169eb9fba8c5`;
- T02 `done`, result `f3630798b7bfb2002efc57e3d7051123d834c4dc`;
- T03 `ready`;
- `Active execution: null`;
- `Experiment state: completed`.

Verified durable sequence:

1. `7e0d166c92f6ea15bae5ee6aa98cb075b6b3e013`
   - T01 and T02 both `ready -> in_progress` before member work;
   - X01 created with both members active;
   - exact common base persisted.

2. Phase-1 member outputs:
   - T01 artifact/result: `2a48259a9e1bbb3086581f3d88bc169eb9fba8c5`;
   - T02 B1 checkpoint: `1ee12e95ca96fc08a4ed5719d036e3c5f32ec525`;
   - exact artifact contents match immutable subject.

3. `da1475c2e28e1277a2616eb4ba43b2707ae83abb`
   - durable evidence records that T01 and T02/B1 were realized concurrently in separate isolated mutable contexts;
   - T01 is `done / reconciled`;
   - T02 remains `in_progress / quiesced`;
   - X01 becomes `transfer_ready`;
   - T03 remains planned;
   - all old member realizations are recorded as ended before transfer.

4. `6ec6e8cf75a1e77f5efdcb0b6eb093b14b3b1b58`
   - same X01 is resumed;
   - T01 remains reconciled;
   - only T02 becomes active;
   - B1 checkpoint ref is preserved.

5. `f3630798b7bfb2002efc57e3d7051123d834c4dc`
   - Phase 2 creates only `execution-h/B.txt`.

6. `6735d7799f8abb5fa3b536f151ffa5dc6dde76e7`
   - T02 becomes done;
   - T03 becomes ready;
   - Active execution becomes null;
   - experiment becomes completed.

Preservation verification:
- compare from the transfer checkpoint through T02 result shows only the state record + new `B.txt`;
- `A.txt` was not replayed or rewritten;
- `B-prefix.txt` was not replayed or rewritten;
- T03 was not executed.

Verdict: **PASS for the designed common execution-set takeover contract.**

#### Concurrency evidence boundary exposed by H

The repository proves:
- both Cards were made active before member work;
- separate accepted member artifacts existed;
- the coordinator durably attested that their isolated realizations ran concurrently;
- canonical reconciliation and later serial takeover behaved correctly.

However, canonical Git history itself is serial and does not independently prove wall-clock overlap. In particular, the canonical B1 commit is descended from the T01 reconciliation path. This is compatible with parallel workers whose returned outputs were reconciled sequentially, but Git topology alone cannot distinguish that from serial realization.

Therefore the strongest precise claim is:
- **takeover/reconciliation semantics are independently repository-verifiable;**
- **actual concurrent realization is verified by the coordinator's durable runtime-neutral attestation, not independently reconstructible from Git topology.**

This is acceptable under H's written evidence contract, which intentionally forbids concrete worker/session/worktree identity, but it exposes a design question for the eventual common schema: whether a runtime-neutral concurrency proof stronger than coordinator attestation is worth retaining.

Possible stronger future evidence, if needed:
- preserve per-member isolated result refs derived from one frozen base before canonical reconciliation;
- still avoid concrete worker/session identity;
- treat such refs as proof of isolation/common-base execution, while recognizing that even this does not by itself prove exact wall-clock overlap.


### Live test I — unsafe takeover must fail closed

Prepared:
- durable record: `brainstorming/live-tests/CAPABILITY_EXECUTION_I.md`
- immutable subject: `be7f0d30830655c5dc16356357c035a923a48f5e:brainstorming/live-tests/CAPABILITY_EXECUTION_I_SUBJECT.md`

Initial durable state intentionally represents uncertain live work:
- T01 `in_progress`;
- X01 `active`;
- no result;
- no quiescence proof;
- takeover candidate cannot prove the old realization has stopped.

PASS requires the receiving context to preserve the active obligation and persist only a blocker:
- no T01 replay;
- no replacement X02;
- no result artifact;
- no synthetic `ready` reset;
- no assumption that missing runtime/session means the old work is dead.

This is the negative counterpart to G/H and validates the fail-closed edge of the transfer protocol.


### Live test I — unsafe takeover fail-closed PASS

Verified commit: `72b06a2f142d3818c26ab3935679910761d083b1`.

The diff changes only the durable test record:
- `Experiment state: pending -> blocked`;
- adds exact blocker evidence.

Verified final durable state:
- T01 remains `in_progress`;
- X01 remains the same `active` unresolved execution attempt;
- no result ref exists;
- no X02/replacement attempt exists;
- `brainstorming/live-tests/execution-i/result.txt` does not exist.

Verdict: **PASS — uncertain still-active work fails closed rather than being replayed or replaced.**

This completes the core Stage-9 transfer safety matrix exercised so far:
- F: completed-Card boundary takeover — PASS;
- G: active single-Card takeover at proven quiescent checkpoint — PASS;
- H: multi-member concurrent-set takeover after quiescent reconciliation — PASS, with actual-concurrency evidence limited to durable coordinator attestation;
- I: unsafe active takeover without quiescence/result proof — PASS fail-closed.

Working conclusion:
- a common runtime-neutral execution lifecycle can distinguish terminal, transferable and unsafe-active states without product identity;
- cross-runtime transfer should be ordinary recovery from durable execution state;
- `transfer_ready/quiesced` is an explicit safety boundary, not an inference from context/session disappearance;
- no new realization is legal while prior active liveness remains unresolved.


### Stage 9 concrete target contract draft — common Execution / State

Status: tentatively accepted direction refined from live tests F–I. This is still Brainstorming authority only.

#### Core separation

The target model uses two distinct state layers:

1. **Card lifecycle** answers whether project work is not started, executable, started/non-terminal, blocked or terminal.
2. **Active execution lifecycle** answers whether a concrete current realization set exists and whether it is safe to continue/transfer.

Therefore `execution_status: in_progress` MUST NOT mean "a worker/session is currently alive".

A Card may remain `in_progress` after implementation is durably reconciled while a REQUIRED/RECOMMENDED review or another non-terminal Card obligation still prevents `done`, even when `active_execution: null`.

#### Common Card lifecycle

Keep the existing project-level Card states:

```text
planned -> ready -> in_progress -> done
                     \-> blocked
planned|ready|in_progress|blocked -> superseded   # only with accepted authority
```

Stage-8 meaning remains:

`READY = legally executable now from durable project authority, dependencies, prerequisites and authorization gates.`

Starting execution moves a selected READY Card to `in_progress`.

A launched/in-progress Card MUST NOT be reset to READY merely because runtime state disappeared. The narrow exception is a provably pre-launch prepared execution that never authorized or began mutation; safe abandonment may restore ordinary READY state after durable reconciliation.

A Card becomes `done` only after the applicable Definition of Done, including required review, is satisfied.

#### One common active-execution model

Use one current execution-set concept for both serial and concurrent work.

Conceptual target schema:

```yaml
active_execution:
  id: X01
  state: prepared | active | transfer_ready
  base_ref: <exact canonical durable base>
  reconciliation_order: [T01, T02]
  members:
    - card_id: T01
      state: prepared | active | quiesced | result_ready | reconciled | blocked
      checkpoint_ref: null
      result_ref: null
      canonical_result_ref: null
      evidence: null
```

Or:

```yaml
active_execution: null
```

Rules:
- one member = ordinary serial execution;
- multiple members = bounded concurrent execution;
- `Xnn` is a project-local execution-attempt identifier, not runtime/session identity;
- one X ID survives runtime/context takeover until that project execution attempt closes;
- concrete worker/model/session/invocation/worktree identity is forbidden as required Project Workflow state;
- member set and `reconciliation_order` freeze before member mutation begins;
- `base_ref` is exact durable project/Git state against which selected work was started;
- shared Task Board/manifest/integration state has one coordinating writer; delegated realizations return bounded result/evidence and do not independently mutate common coordination state.

No separate `parallel.current_batch`, batch ID, lane ID or fixed worker-role identity is required.

#### Active-execution states

`prepared`
- exact member set is selected and durable;
- selected Cards are already `in_progress`;
- exact base/order are frozen;
- no member mutation is yet accepted as having begun;
- before launch, current safety/authority may be revalidated;
- safe abandonment back to ordinary Card READY is legal only when durable/runtime evidence proves no member mutation or side effect began.

`active`
- at least one member realization may be active, result reconciliation may be in progress, or liveness is otherwise not safe to infer;
- another runtime MUST NOT create a replacement realization merely because the old runtime/session is unavailable;
- uncertain liveness remains `active` and fails closed, as validated by test I.

`transfer_ready`
- an explicit durable safety boundary;
- every old realization has been proven quiescent/ended;
- no old member may continue mutating project or external state;
- enough durable state exists to let another runtime continue/reconcile the same X attempt;
- this is never inferred from transcript/session disappearance.

`null`
- no current implementation realization set remains;
- all member outcomes have been reconciled into ordinary Card/review/blocker state.

No separate generic `Execution state` field is needed.

#### Member states

`prepared`
- selected inside X but mutation has not begun.

`active`
- member may still mutate or its liveness is uncertain.

`quiesced`
- old realization is proven unable to continue mutation;
- member is still non-terminal and may carry an exact durable `checkpoint_ref`;
- same X may later reactivate this member.

`result_ready`
- an exact durable realization result exists;
- that result is not yet the accepted canonical Card result;
- member must not be re-executed merely because runtime state disappeared.

`reconciled`
- accepted member result has been reconciled into canonical project state;
- exact `canonical_result_ref` is durable;
- this member is never replayed within this X attempt.

`blocked`
- the member realization is durably stopped/quiesced and cannot legally continue without recovery/classification;
- exact blocker evidence is required;
- do not use `blocked` to hide uncertain liveness: if an old realization may still mutate, the member remains `active` and the takeover is fail-closed.

#### Member transitions

Normal:

```text
prepared -> active
active -> result_ready -> reconciled
active -> quiesced -> active
active -> quiesced -> blocked
```

Direct canonical execution may collapse:

```text
active -> reconciled
```

when there is no separate returned-result integration boundary and exact accepted canonical result/evidence is already durable.

A bounded retry of the same member under the same X is legal only when:
- prior realization is proven quiescent;
- accepted Card authority is unchanged;
- base and safety constraints required by the Card remain valid;
- any failed/returned prior result remains durably recoverable as evidence.

Then the member may re-enter `active` without creating a new X. Successful/reconciled siblings are never replayed.

A changed Card authority/subject that constitutes new implementation work creates a later execution attempt after the current obligation is reconciled; do not mutate an old X into a different contract.

#### Starting execution from Stage 8

Precondition:
- `active_execution: null`;
- no higher-priority durable review/Research/correction/recovery obligation owns continuation;
- one or more Cards are READY.

Runtime realization selection:
- a serial runtime selects one legal READY Card;
- a concurrency-capable runtime may select a finite compatible subset for which current project-level concurrency safety is proven;
- runtime capability changes the selected subset/scheduling, not READY semantics;
- Project Workflow does not ask the user to choose between equivalent deterministic realizations.

Before member work:
1. freeze one X ID, exact `base_ref`, finite member set and reconciliation order;
2. move every selected Card `ready -> in_progress`;
3. persist `active_execution.state: prepared`;
4. read back;
5. perform current refresh/safety validation;
6. durably enter `active` before accepting member mutation as live;
7. invoke/realize through the runtime.

If a reported available runtime capability fails during invocation, do not reinterpret it as capability absence and silently change transport. Preserve/retry/block according to runtime-operation evidence.

Partial launch uncertainty is fail-closed. A stale `active` state is never proof that nothing launched.

#### Result and reconciliation semantics

Delegated/isolated realization:
- returned exact member result -> `result_ready` + exact `result_ref`;
- validate authority/scope/tests/evidence against the frozen base;
- reconcile in frozen `reconciliation_order`;
- persist exact canonical result -> `reconciled` + `canonical_result_ref`.

Direct canonical realization:
- exact accepted canonical result may move the member directly to `reconciled`.

Project Card result state always points to the accepted canonical result, never merely to an unintegrated isolated-worker result.

A durable `result_ready` member is never rerun solely because its runtime disappeared.

Scope escape, integration conflict or contradictory evidence preserves the returned result/evidence and fails closed; it does not silently widen scope or reorder siblings.

#### Closing one execution attempt

An X may be cleared only when no member remains potentially live and every member outcome has been reconciled into durable project state:
- `reconciled` result;
- or durable Card/member blocker after proven quiescence.

Then:
1. persist corresponding Card result/blocker/review boundary;
2. recompute project readiness;
3. set `active_execution: null`;
4. return to the common router.

No permanent execution-set history ledger is required by default once all necessary lineage is already carried by exact Card result, evidence, review-attempt and blocker refs. Preserve additional execution history only when a concrete recovery/review requirement proves it necessary.

#### Review boundary while an execution set is unresolved

When a member becomes `reconciled` and its Card requires independent review:
- freeze the exact immutable review subject/result as `pending`;
- the Card remains non-terminal;
- do not issue a verdict in the producing context.

For a multi-member X with unresolved members, formal review realization is deferred until that X is closed or terminally reconciled. This preserves the useful current Codex invariant that a RED correction cannot mutate production underneath unresolved sibling reconciliation.

After X is null, ordinary common review routing may consume the frozen pending attempts.

No `implementation_owner_role: executor` or `reviewer_role: tester` is required. Review must instead prove the semantic independence requirement against the exact produced subject; concrete independent-context realization belongs to runtime capability handling.

#### Completed-Card runtime switch

A terminal/reconciled Card boundary requires no special product handoff.

Target:

```text
T01 done + exact result/evidence
T02 ready
active_execution null

new runtime
-> reconstruct from durable project state
-> do not replay T01
-> select next legal obligation
```

Validated by live test F.

#### Active runtime switch

A non-terminal execution attempt can transfer only through explicit `transfer_ready`.

To set `transfer_ready`:
- every old realization is proven ended/quiescent;
- no member remains `active`;
- every completed result/checkpoint/ref needed for continuation is durable;
- no old context/worker may continue authoritative or external mutation.

Receiving runtime:
1. verifies exact X, base, member states and refs;
2. preserves every `reconciled` and `result_ready` member;
3. never replays a durable checkpoint merely due runtime switch;
4. may reactivate only unresolved `quiesced/prepared` members under the same still-valid authority;
5. may continue those remaining members serially even when the previous runtime used concurrency;
6. preserves the same X ID.

Validated for one Card by G and for a multi-member concurrent set by H.

#### Unsafe takeover

If `active_execution.state: active` and exact evidence does not prove prior realization quiescence/end or an already-accepted durable result:
- do not create a replacement X;
- do not replay the Card;
- do not reset the Card to READY;
- do not infer old realization death from missing session/runtime identity;
- persist/recover the exact blocker and fail closed.

Validated by I.

For material non-idempotent external effects, quiescence/idempotency/readback evidence is mandatory before replacement. Repository-local worker disappearance is not a general proof that external mutation stopped.

#### Multiple in-progress Cards

Remove the ChatGPT-only invariant that exactly one Card may be `in_progress`.

Multiple `in_progress` Cards are legal when each has exact durable ownership, for example:
- it is a member of the current `active_execution`; or
- implementation is already reconciled but a durable review/finalization/correction obligation keeps the Card non-terminal.

Therefore Card `in_progress` cardinality is not a runtime capability signal.

What is invalid is an `in_progress` Card whose exact owning durable obligation cannot be reconstructed.

#### Runtime-neutral concurrency safety

Stage 9 consumes, but does not invent, project-level concurrency-safety facts established/refreshed at JIT.

The exact Card schema for those facts remains a Stage-8 schema choice, but Stage 9 requires at minimum enough durable proof to establish:
- compatible mutation/write scope;
- no conflicting exclusive/shared resource;
- no hidden sequencing prerequisite;
- safe reconciliation/integration behavior;
- any external-side-effect constraints.

Absence/incompleteness of such proof means serial realization remains legal but concurrency is not.

#### Current ChatGPT-only material to remove/replace

Replace:
- `Normal ChatGPT is the fixed executor`;
- `executor: chatgpt`;
- exactly-one-`in_progress` invariant;
- execution semantics that assume implementation occurs directly inside one fixed product context;
- product-specific fresh-review stop mechanics inside Execution.

Preserve/promote:
- deterministic Card authority/Refresh Gate;
- result/tests/evidence/readback;
- Research return/handoff;
- Definition of Done;
- exact review freeze boundary;
- recovery from actual durable state.

#### Current Codex-only material to remove/translate

Remove as Project Workflow authority:
- `Codex Main` identity;
- `Executor` / `Tester` names;
- `implementation_owner_role: executor`;
- `reviewer_role: tester`;
- orchestration profile/pre-dispatch binding from common project semantics under the fixed-runtime target;
- batch IDs and lane labels as required project semantics;
- concrete worker/worktree/session lifecycle.

Translate:
- `parallel.current_batch` -> `active_execution`;
- `integration_base` -> `base_ref`;
- batch frozen member list -> X frozen member list;
- `returned` -> member `result_ready`;
- `integrated` -> member `reconciled`;
- member returned/integrated refs -> `result_ref` / `canonical_result_ref`;
- prepared/running/integrating recovery rules -> common prepared/active/result-ready/reconciliation recovery;
- post-launch terminal reconciliation -> quiesce all live members, preserve returned/reconciled refs, move unresolved Cards to exact blocked state, then clear X;
- post-batch review drain -> ordinary pending-review drain after X closes.

Preserve the safety substance:
- one shared-state writer;
- isolated mutable concurrent realizations;
- frozen base/member set/order;
- scope/resource validation;
- never replay returned/reconciled siblings;
- deterministic reconciliation;
- fail-closed partial writes/conflicts;
- review not interleaved with unresolved sibling production.

#### Stage-9 counterfactual challenge

Could the common model simply keep the current Codex batch schema and treat serial work as a one-member batch?

That would preserve recovery power, but it would also retain accidental scheduler vocabulary (`batch`, `lane`) and make every runtime appear to use Codex-style parallel orchestration. F–I show the required common semantics are smaller: exact execution set, member lifecycle, base/result/checkpoint/reconciliation refs, quiescence and transfer safety.

Conversely, could common Execution keep only Card states and discard `active_execution` entirely?

No. G–I demonstrate that `in_progress` alone cannot distinguish:
- safely transferable quiesced work;
- durable partial checkpoint work;
- returned/reconciled sibling results;
- unsafe uncertain-live work.

Therefore a runtime-neutral active-execution record is materially required for portable mid-Card/mid-set recovery.

#### Stage-9 working conclusion

Tentatively stable Stage-9 target:

```text
Stage 8:
truthful READY graph

Stage 9:
runtime selects 1..N legal READY Cards
-> common X execution set
-> prepared
-> active
-> member results/checkpoints/reconciliation
-> optional transfer_ready
-> canonical Card result/review/blocker state
-> active_execution null
```

The same contract supports:
- direct serial ChatGPT-style execution;
- delegated serial execution;
- concurrent Codex-style execution;
- crash recovery;
- completed-Card runtime switching;
- active-Card switching through quiescent checkpoint;
- concurrent-to-serial takeover;
- fail-closed unsafe liveness.

No Definition promotion is authorized by this conclusion.


### Post-implementation Independent Review audit — current main `7aa7512ead67a86256089d1af0171e2e655e700d`

No review workflow change or live test is authorized yet. This section records the current-state audit and a proposed common target for discussion.

#### Current common semantics already shared

Both fixed-policy review routes already agree on the important project-level rules:

- REQUIRED and RECOMMENDED reviews are real completion gates once activated;
- one review judges one exact immutable subject;
- the reviewer must be independent from production of that exact subject;
- reviewer must not repair/mutate the subject while judging it;
- verdict is GREEN or RED with durable evidence;
- GREEN does not itself mark a Card `done`; Execution performs deterministic finalization after verifying the result still equals the GREEN subject;
- RED preserves the reviewed subject/evidence and routes deterministic correction according to authority:
  - bounded L1/L2 implementation correction -> Execution Prep/Execution;
  - plan-only correction -> Planning;
  - accepted authority change -> Definition;
  - missing evidence -> Research;
  - unresolved user/authorization/runtime-input gate -> real stop;
- a changed corrected result is a new immutable review subject;
- runtime/reviewer loss must not invent a new project review attempt when subject is unchanged;
- workstream final-integration review is a distinct gate from Card/milestone review and may reuse an already-independent stronger verdict only when exact subject + complete acceptance coverage are proven.

These are common Project Workflow semantics, not product behavior.

#### Current ChatGPT-only realization

`workflow/chatgpt_only/REVIEW.md` hardcodes:
- a fresh normal ChatGPT chat as reviewer;
- implementing chat cannot review its own subject;
- fresh-review handoff/STOP when a new independent reviewer is required.

Card/milestone review state is flat:

```yaml
review_state: pending | in_progress | green | red
review_subject: <exact subject>
review_evidence: <pointer>
```

This expresses the current attempt but has no explicit append-only attempt ledger.

The current ChatGPT state contract says a corrected subject receives a new review, but the flat mutable fields do not themselves preserve prior RED/GREEN attempt lineage.

#### Current Codex-only realization

`workflow/codex_only/REVIEW.md` hardcodes:
- `Codex Main` as state writer;
- independent `Tester` as reviewer role;
- `Executor` as implementation owner;
- orchestration pre-dispatch binding.

Card/milestone review state is richer and append-only:

```yaml
review:
  requirement: REQUIRED
  current_attempt: R01
  attempts:
    - id: R01
      state: pending
      subject: <exact immutable subject>
      reviewer_role: tester
      evidence: null
```

Useful semantics:
- stable attempt IDs;
- one immutable subject per attempt;
- prior attempts append-only;
- corrected result appends a new attempt;
- reviewer replacement for the unchanged subject does not create a new attempt;
- terminal verdict requires durable evidence.

The worker-role fields are runtime leakage, but the append-only attempt model is stronger project semantics and should not be lost.

#### Workstream final-integration drift

Both current workstream manifests use a flat final-review gate:

```yaml
review:
  requirement: ...
  state: pending | in_progress | green | red | null
  subject: ...
  evidence: ...
  covered_by: ...
```

This is sufficient for one current gate but is weaker than the Codex Card/milestone attempt ledger when a final review is RED, correction produces a changed integrated subject, and the next review must preserve earlier verdict lineage.

Working direction: final-integration review should also preserve append-only gate-attempt history rather than overwrite the prior subject/evidence.

#### Proposed common review owner model

Every post-implementation review owner should use the same append-only project semantics:
- Card;
- milestone/checkpoint;
- workstream final-integration gate.

Conceptual common shape:

```yaml
review:
  requirement: REQUIRED | RECOMMENDED | none
  current_attempt: R02
  attempts:
    - id: R01
      mode: independent_review
      state: red
      subject: <immutable subject 1>
      evidence: <exact durable evidence>
      independence:
        requirement: independent_context
        realization_state: satisfied
        evidence: <runtime-neutral verification>
      covered_by: null

    - id: R02
      mode: independent_review
      state: pending
      subject: <immutable subject 2>
      evidence: null
      independence:
        requirement: independent_context
        realization_state: resolve_independent_context
        evidence: null
      covered_by: null
```

For exact stronger-coverage reuse at the distinct workstream final-integration gate, an append-only terminal entry may use:

```yaml
mode: coverage_reuse
state: green
subject: <exact final integrated subject>
covered_by: <exact prior independent GREEN verdict>
evidence: <proof of identical subject + complete acceptance coverage>
```

No independent-context realization occurs for `coverage_reuse`; the evidence proves why a new review was unnecessary.

This keeps one history model without pretending coverage reuse is a newly executed review.

#### Review-attempt invariants

Target common invariants:

- attempt IDs are stable and never reused;
- one attempt covers exactly one immutable subject;
- `current_attempt` points to an existing attempt or is null;
- at most one attempt for an owner is non-terminal;
- prior attempts are append-only;
- `green | red` requires durable evidence;
- a verdict can only apply if its subject still exactly matches the reviewed durable result;
- changed implementation/accepted subject creates a new attempt;
- reviewer/context replacement for the unchanged subject stays in the same attempt;
- no review attempt may mutate the subject while judging it;
- no concrete product/worker/model/session identifier is required project state.

This should replace the ChatGPT flat review fields rather than preserve two incompatible state shapes.

#### Independence as a semantic obligation, not a worker name

Common Project Workflow should encode:

`independent context required for this exact subject`

It should not encode:
- `fresh ChatGPT`;
- `Tester`;
- `Executor`;
- `Codex Main`.

The Stage-7 capability-first realization lifecycle is a good candidate for review attempts:

```text
resolve_independent_context
-> awaiting_independent_context
-> independent_context_active
-> satisfied
```

Interpretation:
- `resolve_independent_context`: review exists, realization method not yet resolved;
- if runtime has a qualifying independent delegated context, use it;
- if not, persist `awaiting_independent_context`, emit locator-only fresh-context handoff and STOP;
- receiving fresh context moves to `independent_context_active` rather than bouncing again;
- terminal verdict sets realization to `satisfied`.

If a reported available independent-context capability fails to invoke, that is runtime failure/retry/blocker evidence. It MUST NOT be reinterpreted as capability absence and silently downgraded to another transport.

#### Independence proof

Project Workflow needs durable proof that the semantic independence requirement was satisfied, but it does not need concrete session/worker identity.

For an exact implementation subject:
- the producing context must never review that same subject;
- when multiple runtime realizations contributed to the subject, the selected reviewer must be independent from all production realizations that materially contributed;
- runtime owns the concrete identity comparison/mechanism;
- Project Workflow persists only runtime-neutral evidence/attestation that independence was verified for the exact subject.

For fresh-context fallback, the durable `awaiting_independent_context -> independent_context_active` handoff state provides the same anti-bounce/recovery property validated in Stage 7.

The independence evidence is tied to the immutable subject; changing subject invalidates it.

#### Interaction with Stage 9 active_execution

When one member of a multi-member X becomes `reconciled` and requires review:
- freeze its exact pending review attempt immediately after canonical result is durable;
- keep the Card non-terminal;
- while the same `active_execution` still has unresolved sibling production, do **not** start formal review;
- close/terminally reconcile X first;
- then route pending reviews deterministically.

This preserves the useful current Codex rule without any `batch`/`Tester` vocabulary and prevents RED repair from changing canonical production while sibling reconciliation is unfinished.

For serial/direct execution with `active_execution: null` after reconciliation, the pending review obligation may be resolved immediately by the capability-first independent-context resolver.

#### GREEN

For a Card-completion attempt:
1. persist GREEN/evidence;
2. independence realization becomes satisfied;
3. review role ends;
4. router sends the Card to Execution finalization;
5. Execution verifies current canonical result still equals GREEN subject;
6. if equal and DoD is satisfied -> Card `done`;
7. if result changed -> GREEN does not cover it; freeze a new attempt when review still applies.

For workstream final-integration GREEN:
- preserve attempt/history;
- continue Close/integration only while exact covered subject/acceptance remains valid.

A reviewer verdict is not itself a reason for a user-facing stop.

#### RED

For RED:
1. persist verdict/evidence append-only;
2. reviewer role ends and never repairs the subject while still reviewer;
3. classify correction from durable authority/evidence;
4. route deterministic correction;
5. preserve prior RED attempt unchanged;
6. when corrected canonical result exists, append a new pending attempt with a new immutable subject;
7. resolve independence again for that new subject.

The same chat/context that performs the correction is disqualified from reviewing the corrected subject; the common independent-context resolver handles the next review.

#### Runtime loss and recovery

For `pending`:
- resume independent-context realization for the same attempt/subject.

For `in_progress` with no complete durable verdict:
- runtime may resume/replace reviewer realization;
- reviewer performs the full review of the same immutable subject;
- do not create a new project attempt.

For durable verdict evidence whose attempt state is stale:
- verify evidence exactly matches attempt + subject;
- reconcile state to GREEN/RED;
- do not rerun review merely to repair bookkeeping.

For GREEN/RED:
- never replay verdict because the reviewer/runtime disappeared.

#### Proposed removals

From ChatGPT-only review semantics:
- fixed requirement that the reviewer is a normal ChatGPT product session;
- product-specific fresh-review wording inside semantic review contract;
- flat mutable Card/milestone review state.

From Codex-only review semantics:
- `Codex Main`;
- `Tester`;
- `Executor`;
- `reviewer_role: tester`;
- `implementation_owner_role: executor`;
- orchestration pre-dispatch binding as Project Workflow review semantics.

Preserve/promote from both:
- exact owner and immutable subject;
- same authority/acceptance surface;
- independence requirement;
- no reviewer repair;
- append-only attempt lineage;
- durable verdict/evidence;
- GREEN finalization;
- RED classification/correction;
- runtime-loss recovery;
- workstream exact-coverage reuse.

#### Counterfactual challenge — do we really need append-only attempts everywhere?

A smaller common schema could keep ChatGPT's flat current review state and rely on evidence files/Git history for previous RED/GREEN verdicts.

Rejected as the working direction because:
- RED -> correction -> recheck is a first-class lifecycle, not forensic Git archaeology;
- cross-runtime recovery should know current vs historical verdicts directly from canonical state;
- workstream final-review correction has the same lineage problem as Card review;
- current Codex state already demonstrates a compact append-only solution.

Therefore append-only attempt history is tentatively preferred for all post-implementation review owners.

#### Proposed validation after user approval

Do not run yet.

**J — cross-runtime GREEN review**
- runtime/context A produces a durable reviewable Card subject and freezes R01 pending with `resolve_independent_context`;
- another qualifying independent context reviews exactly R01 and persists GREEN;
- a later context/runtime finalizes the Card without replaying implementation or review;
- no product/worker name enters review state.

**K — RED -> repair -> R02 recheck**
- R01 reviews subject S1 and returns RED;
- bounded correction produces S2;
- R01 remains immutable RED;
- R02 is appended for S2;
- producing correction context cannot self-review S2;
- independent R02 returns GREEN;
- final state preserves both attempts.

A separate coverage-reuse test is only needed if manifest final-integration schema remains materially uncertain after J/K.


### Live review tests J/K prepared

Prepared test J:
- durable record: `brainstorming/live-tests/CAPABILITY_REVIEW_J.md`
- immutable authority: `dbe81191afb840e096ef0aadde9b922ee5ccf5da:brainstorming/live-tests/CAPABILITY_REVIEW_J_SUBJECT.md`
- exact implementation result: `a23712266f36ae70cda129a9b3242c6391b50b49:brainstorming/live-tests/review-j/result.txt`

J validates:
- capability-first realization of one independent R01 review without product/worker identity;
- durable GREEN;
- later cross-runtime/context Card finalization from that GREEN without replaying implementation or review;
- one immutable attempt remains sufficient when subject did not change.

Prepared test K:
- durable record: `brainstorming/live-tests/CAPABILITY_REVIEW_K.md`
- immutable authority: `569a439b3ffa75a8fa7d0fd6947e89d4bde1d0cd:brainstorming/live-tests/CAPABILITY_REVIEW_K_SUBJECT.md`
- intentionally defective S1: `f72d08ae5d4aa8faf06dcedb586bc1618887200c:brainstorming/live-tests/review-k/result.txt`

K validates:
- R01 independently detects S1 defect and becomes immutable RED;
- bounded correction produces distinct S2;
- correction appends R02 instead of replacing R01;
- correction-producing context cannot issue the R02 verdict;
- later independent R02 reviews exact S2 GREEN;
- both review attempts remain durable and addressable.

Both tests reuse the capability-first independence lifecycle from Stage 7:
`resolve_independent_context -> awaiting_independent_context | independent_context_active -> satisfied`.

Test-specific STOP boundaries are intentional observability points. They do not imply that the eventual production router must stop after every GREEN/RED transition when deterministic continuation is otherwise legal.


### Live review test J — cross-runtime GREEN + finalization PASS

Verified durable sequence:

1. Codex-side independent review completed R01 GREEN at
   `c7a01744688301fb5c755143aa946f1a2c9892e7`.
   - Experiment `pending_review -> reviewed`.
   - R01 `in_progress -> green`.
   - exact immutable subject remained
     `a23712266f36ae70cda129a9b3242c6391b50b49:brainstorming/live-tests/review-j/result.txt`.
   - durable GREEN evidence was recorded.
   - `independence.realization_state -> satisfied`.
   - no reviewed-subject mutation occurred.

2. Later ChatGPT context finalized the same Card at
   `044aab4f8b78bdfe5450aad64c3d9fe6d48b9edd`.
   - Experiment `reviewed -> completed`.
   - T01 `in_progress -> done`.
   - T01 result ref remained unchanged.
   - R01 remained the only attempt and stayed GREEN.
   - no implementation replay;
   - no review replay;
   - review history/evidence unchanged.

Verdict: **PASS — a runtime-neutral independent GREEN verdict can be consumed by a later different runtime/context for deterministic Card finalization without replay.**

This validates:
- product-neutral independent-context review semantics;
- one unchanged subject stays in one review attempt;
- terminal review evidence survives runtime/context change;
- Card finalization is a separate deterministic continuation from verdict production.


### Live review test K — Phase 1/2 verified, Phase 3 still pending

Verified Phase 1:

- `6596a4bcf5c130813c54fd3b012de41c5b23015b`
  - R01 `pending -> in_progress`;
  - independence realization `resolve_independent_context -> independent_context_active`.

- `20451f05b064a0fd075962b989fe6e453b8c77fd`
  - experiment `pending_r01 -> r01_red`;
  - R01 `in_progress -> red`;
  - exact immutable S1 subject preserved;
  - RED evidence correctly identifies `review-k: BAD\n` versus required `review-k: GOOD\n`;
  - independence becomes `satisfied`.

Verified Phase 2:

- `073f6d569c44d609de5eee3bf2bf1e550ca74938`
  - only authorized file `brainstorming/live-tests/review-k/result.txt` changes;
  - exact correction is `BAD -> GOOD`;
  - this commit is canonical S2.

- `c3d5f593b22dbf2150c02a300421ce7534280ce2`
  - T01 result ref advances from exact S1 to exact S2;
  - `current_attempt: R01 -> R02`;
  - R01 remains immutable RED with its original subject/evidence;
  - R02 is appended as a distinct pending attempt for exact S2;
  - R02 independence starts at `resolve_independent_context`;
  - experiment becomes `pending_r02`.

Current remote durable state is still `pending_r02`. No later durable R02 GREEN transition is present yet, so K cannot yet receive a full PASS.

#### Runtime-role leakage finding

The intermediate Phase-1 commit `6596a4bc...` persisted independence evidence containing the phrase `delegated Tester context`.

The later terminal R01 evidence no longer requires or names a concrete worker role, so the current canonical review record is runtime-neutral. However, Git history proves that current runtime behavior can still leak a concrete worker-role label into a transient durable Project Workflow state transition.

This does not invalidate the RED/correction/append-only semantics already verified, but it is evidence that the eventual common contract should explicitly prohibit concrete runtime-role names not only in the final schema but also in intermediate durable evidence/state.


#### K race-condition finding — losing correction context is not an independent R02 reviewer

A second Codex context also executed Phase 2 locally from the stale `r01_red` state and produced an equivalent S2/R02 transition. Its push was rejected because the remote branch had already advanced to the equivalent canonical Phase-2 state created by the ChatGPT correction context.

The Codex context then refreshed/reset to remote `c3d5f593b22dbf2150c02a300421ce7534280ce2` and stopped before R02.

This is the correct independence outcome.

Reason:
- independence is determined by what a context/realization materially did, not by which competing equivalent commit became canonical;
- a context that independently produced the correction S2 is a production/correction context for that exact reviewed subject, even if its own write lost a CAS/push race;
- therefore that same context is disqualified from issuing R02;
- observing that remote already contains an equivalent S2 does not retroactively make the losing producer independent.

This exposes a useful common review invariant:

> A context/realization that materially produced, repaired or transformed the exact reviewed subject is disqualified from independently reviewing that subject, regardless of whether its local result became the canonical durable commit.

Canonical state remains correctly at:
- R01 immutable RED for S1;
- R02 pending for canonical S2 `073f6d569c44d609de5eee3bf2bf1e550ca74938`;
- `Experiment state: pending_r02`.

A genuinely fresh context that did not perform the S2 correction is still required for Phase 3.


### Authoritative-state refresh gate — cross-context/recovery entry

The K correction race exposed a distinct portability requirement:

`fresh context != fresh durable repository state`.

A newly opened context can be perfectly independent from prior chat history while still routing from a stale local checkout/worktree. Therefore common Project Workflow recovery/entry must establish current authoritative durable state **before** selecting the next legal obligation.

Target rule:

```text
new context / takeover / recovery entry
-> resolve exact selected workstream + authoritative branch/ref
-> refresh the authoritative durable source
-> establish exact current authoritative head
-> reconcile/validate local checkout against that head
-> read canonical durable workflow state from that head
-> only then select the legal pending obligation
```

For a remote-backed Git workstream:
- fetch/refresh the exact authoritative branch/ref before routing when that ref may have advanced outside the current context;
- do not infer current workflow state from an unrefreshed local worktree merely because the chat/context itself is fresh;
- if local state is behind/diverged from authoritative durable state, do not execute the phase implied only by stale local state;
- if local uncommitted/unpushed state represents an unresolved owned attempt, reconcile that ownership first rather than discarding or replaying it blindly;
- if safe reconciliation cannot be proven, fail closed to Recovery.

Before publishing a mutable transition, preserve the existing optimistic-concurrency/CAS behavior:
- write from the exact expected durable base;
- if push/update is rejected because the authoritative branch advanced, refresh authoritative state and **reroute from the new durable state**;
- do not blindly retry the stale phase.

The K race demonstrates why both layers are needed:
1. **pre-routing freshness** prevents unnecessary duplicate phase execution;
2. **expected-base/CAS publication** remains the final protection against concurrent advancement.

This gate applies at cross-context/takeover/recovery entry or whenever the selected authoritative state may have advanced externally. It does not require a redundant remote refresh before every deterministic role transition performed by the same coordinating context when that context still owns the exact current durable head and no competing writer is permitted.

The gate is common workflow correctness, not a Codex-specific fix.

### Live review test K — lifecycle PASS, runtime-neutral evidence defect exposed

Phase 3 is now durable at:

`729c17e48b688e00394f0428bf62259fe6e5839d`

Verified final lifecycle:
- experiment `pending_r02 -> completed`;
- R02 `pending -> green`;
- exact S2 subject remains
  `073f6d569c44d609de5eee3bf2bf1e550ca74938:brainstorming/live-tests/review-k/result.txt`;
- R01 remains immutable RED for S1;
- T01 remains `in_progress` as intended by this test;
- Phase 3 did not finalize the Card.

Therefore the **review lifecycle objective passes**:
```text
R01 RED(S1)
-> bounded correction S2
-> append R02(S2)
-> independent R02 GREEN
```

The append-only attempt model and correction-context self-review prohibition are validated.

However, R02 durable independence evidence contains concrete runtime telemetry:
- the role label `tester`;
- a concrete session UUID;
- a concrete invocation UUID.

This violates the intended stronger runtime-neutral Project Workflow boundary even though the schema itself did not require those fields.

Therefore the precise K result is:

- **append-only review / RED-repair-recheck semantics: PASS**;
- **strict runtime-neutral durable evidence: FAIL / defect exposed**.

The common contract should be strengthened from:

`runtime identity is not required project state`

to:

`concrete runtime worker/role/model/session/invocation/worktree identity MUST NOT be persisted in canonical Project Workflow state or canonical review evidence merely to prove independence`.

Allowed canonical independence evidence should state only semantic facts needed for project recovery, for example:
- `independence: verified`;
- the exact immutable subject;
- that the reviewer did not materially produce/repair that subject;
- that review was read-only with respect to the subject.

Concrete runtime telemetry may remain in runtime-owned logs when useful for diagnostics, but it is not Project Workflow authority and must not be copied into canonical review state.

This also strengthens the earlier K race invariant:
- a context that materially produced/repaired S2 is disqualified from R02 regardless of whether its competing local commit became canonical;
- this semantic fact may be attested without persisting the context/session identity itself.


### Live-test harness contamination finding — current Project Workflow still wraps the experiment

The live-test prompts begin with:

`Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow`

while the repository bootstrap still says current workflow `main` is authoritative and routes into the existing fixed-policy modules. Therefore the live tests are not executing the proposed common contract in a vacuum.

Current old-policy behavior can influence the experiment before/around the synthetic record.

Verified examples from current `main`:
- root `CHATGPT.md` says current workflow `main` is authoritative and routes through the selected fixed-policy namespace;
- `workflow/codex_only/REVIEW.md` explicitly uses `Codex Main`, `Tester`, `Executor`, semantic reviewer-role terminology and the old orchestration gate;
- current Recovery does not yet impose the newly proposed mandatory authoritative-remote refresh before routing a fresh/takeover context.

Consequences for interpreting J/K and earlier live tests:

1. **Runtime-role/evidence leakage**
   - the appearance of `Tester` and concrete session/invocation telemetry in K is likely influenced by the currently active Codex-only review/runtime contract;
   - it is evidence that the old workflow/harness can contaminate canonical live-test evidence;
   - it is NOT clean evidence that the proposed common review contract itself would choose those fields if implemented natively.

2. **Stale local durable state on fresh context**
   - a new chat being fresh does not imply its checkout was refreshed;
   - current old workflow does not contain the new explicit pre-routing authoritative-state refresh gate;
   - therefore the K duplicate Phase-2 attempt is evidence of a gap in the currently active wrapper/recovery behavior and motivates the new common gate, but must not be described as a failure of the not-yet-implemented common contract.

3. **What remains valid**
   - the durable state-machine transitions exercised by the synthetic records remain useful evidence because each test record explicitly constrained legal phases and STOP boundaries;
   - F/G/H/I/J/K still demonstrate whether agents can consume those runtime-neutral states correctly once they read the intended record;
   - incidental old-policy vocabulary/telemetry must be separated from the semantic state-transition result.

#### Stronger isolation rule for future live tests

Future capability-first live-test prompts should explicitly establish an experimental authority boundary:

- use the installed/current Project Workflow only for safe repository/bootstrap mechanics;
- for the tested obligation, the exact durable live-test record is the authoritative semantic contract;
- when an existing `workflow/chatgpt_only/*` or `workflow/codex_only/*` rule conflicts with the live-test record's synthetic common contract, the live-test record wins **for that isolated experiment only**;
- do not import fixed-policy worker names, product identity, state schema or review/execution realization rules unless the live-test record explicitly references them;
- normal repository safety, branch ownership, Git integrity and explicit STOP boundaries still apply.

Suggested prompt prefix:

```text
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow do bezpiecznego bootstrapu repozytorium i operacji Git.
To izolowany live test projektowanego common contractu. Dla testowanej obligation exact durable live-test record jest nadrzędnym kontraktem semantycznym i zastępuje sprzeczne reguły z workflow/chatgpt_only/* lub workflow/codex_only/* wyłącznie w granicach tego eksperymentu. Nie importuj z fixed-policy modules nazw produktów/workerów, state shape ani realization behavior, jeśli durable record ich jawnie nie wymaga.
```

This does not promote the proposed common contract to production authority. It is only test-harness isolation so the experiment measures the candidate semantics rather than current fixed-policy implementation.

#### Reclassification of K evidence defect

The K runtime-neutral evidence finding should therefore be read as:

- append-only RED -> repair -> R02 GREEN lifecycle: **PASS**;
- clean isolation from old fixed-policy runtime vocabulary: **not proven by the current harness**;
- observed `tester/session/invocation` telemetry: **old-workflow/harness contamination exposed**, not a definitive failure of the proposed common contract.

The target common contract should still forbid such telemetry in canonical Project Workflow state, because that remains the desired architecture boundary.



### Live-test harness hardening complete; L PASS; M prepared

The isolated harness remains durable at:

`c427bafb31c3f6c79544be3a89300b02503aa7f9:brainstorming/live-tests/ISOLATED_COMMON_CONTRACT_HARNESS.md`

#### Live test L — authoritative-state refresh PASS

L completed durably at:

`b10eaa864b2a58831868e8b6efbea29bd0164c1e`

Verified from repository truth:
- the probe started from exact stale snapshot `2e52d793c597da27dc1000b126cf60cb90a8a491`;
- it refreshed authoritative state before selecting the obligation;
- refreshed routing selected `L-FRESH`;
- stale `L-STALE` was neither executed nor published;
- no push/CAS rejection was needed to discover freshness;
- exact result is `L: FRESH\n`;
- the completion commit changed only the L record and its result fixture;
- persisted evidence contains semantic/Git correctness facts and no concrete runtime identity telemetry.

Verdict: **PASS — authoritative-state refresh before routing prevents stale-phase execution and complements expected-base/CAS publication safety.**

This supports the common entry/recovery invariant:

```text
new context / takeover / recovery
-> resolve exact authoritative branch/ref
-> refresh authoritative durable source
-> establish current authoritative head
-> reconcile/validate local state
-> read canonical durable state
-> route
```

#### Live test M — clean independent-review evidence PASS

M completed durably at:

`9435ebd56d9628588e64cde22efc631e1463dca0`

Verified from repository truth:
- R01 is GREEN for exact immutable subject `788ceee02a19d6e03d336b6f28b524691f09250d:brainstorming/live-tests/review-m/result.txt`;
- authority and subject remain unchanged;
- the verdict commit changed only `CAPABILITY_REVIEW_M.md`;
- canonical evidence uses exactly the normalized semantic-only shape required by the experiment;
- no concrete product/worker/model/session/invocation/workspace/worktree identity is present.

Verdict: **PASS — independent review can be realized under the isolated common harness without runtime telemetry leaking into canonical Project Workflow evidence.**

This closes the clean-evidence defect exposed by the contaminated K harness as a candidate common-contract capability.

#### Orchestration-topology continuity test N deferred until V2

One shared semantic authority:

`43aef1d58367d2cfea1f561c58eee7791322c203:brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_AUTHORITY.md`

Two realization variants are retained as post-implementation V2 validation scenarios:

1. **N-CAPABLE**
   - record: `brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_CAPABLE.md`;
   - starts with R01 pending for BAD S1;
   - success requires one capable coordinating invocation to perform:
     `R01 RED -> correction S2 -> R02 independent GREEN -> deterministic finalization`
     without artificial user-facing stops.

2. **N-CHATGPT**
   - record: `brainstorming/live-tests/ORCHESTRATION_TOPOLOGY_N_CHATGPT.md`;
   - starts in `awaiting_independent_context` for R01;
   - first fresh ChatGPT review chat must:
     `R01 RED -> same-chat correction S2 -> freeze R02 -> STOP only at new fresh-review boundary`;
   - second fresh ChatGPT review chat must:
     `R02 GREEN -> same-chat deterministic finalization -> completed`;
   - stopping immediately after RED or GREEN is a test failure.

These tests are intentionally **not executed against V1**. The user chose to defer them until V2/common-core exists far enough that the tested contexts can exercise the new implementation directly rather than be influenced by current fixed-policy wrappers.

The required behavior remains a compatibility invariant, but N is no longer a prerequisite for completing current Brainstorming or entering Definition. It becomes part of the V2 implementation/validation plan.

The clean-room harness prepared for N is retained as experimental test infrastructure only; it does not change production authority.

No production workflow module has been changed.

### Cross-cutting audit complete — target V2 architecture resolved

The cross-cutting audit is durable at:

`brainstorming/CROSS_CUTTING_AUDIT_COMMON_PREEXECUTION_CORE.md`

The audit covered current V1:
- `ROUTER`;
- `RECOVERY`;
- `WORKSTREAMS`;
- `CLOSE`;
- active workstream/Task Board templates;
- branch-first, context-health and Codex orchestration regression tests.

Brainstorming conclusion:

1. **One common semantic router/state machine.**
   Durable obligation ordering, authority, recovery, review and workstream lifecycle move to common contracts.

2. **Thin runtime/surface adapters only.**
   ChatGPT context-health/fresh-chat mechanics and Codex runtime delegation remain realization concerns. They must not redefine Project Workflow semantics or state schema.

3. **One common Task Board schema.**
   Replace ChatGPT single-review-state and Codex batch-specific project schema divergence with:
   - generic append-only review attempts;
   - neutral `active_execution`;
   - no product/worker/model/session/worktree identity.

4. **One common workstream manifest.**
   Remove V1 Codex durable `orchestration` binding for new V2 work under the one-fixed-runtime/capability-first target.
   Keep project identity/routing/authority/final-review/result state only.

5. **One generic review model for Card, milestone and final integration.**
   Workstream final-integration review no longer keeps a separate mutable `state/subject/evidence/covered_by` lifecycle.
   It uses the same append-only attempt history, with `mode: independent_review | coverage_reuse`.
   Exact coverage reuse becomes a terminal GREEN attempt referencing the stronger prior independent verdict.

6. **Authoritative-state freshness is common correctness.**
   New-context/takeover/recovery entry must refresh the exact authoritative branch/ref before routing.
   Expected-base/CAS remains publication protection.
   No stronger lease/fencing primitive is currently justified beyond authoritative refresh + explicit execution quiescence/transfer + CAS.

7. **Branch cleanup becomes capability-first common behavior.**
   - already absent branch -> cleanup complete;
   - deletion capability available -> verify exact ref/head, delete, read back;
   - deletion unavailable -> persist optional exact `safe_to_delete` fallback for a later capable context.
   This reconciles the previously different ChatGPT/Codex cleanup contracts without policy-specific lifecycle trees.

8. **V2 routing is runtime-portable.**
   New V2 work should not require durable `execution_policy: chatgpt_only | codex_only` to choose a different semantic state machine.
   Existing execution-policy values remain migration input during transition.
   The active runtime realizes common obligations according to available capabilities.

9. **Migration is staged, not an in-place blind rewrite.**
   Build common schemas/readers first, migrate semantic modules, switch routing only after parity evidence, then retire policy-local semantic copies.

Deferred N-CAPABLE/N-CHATGPT remain required V2 implementation-validation scenarios, not pre-Definition Brainstorming evidence.

No production workflow module has been changed by this audit.

### Conservative commonization principle — explicit user direction

V2 is a merge/commonization of two already-working fixed-policy workflows, not permission to redesign the lifecycle into a larger generic system.

Especially:
- preserve proven `chatgpt_only` behavior unless a concrete portability/commonization requirement requires change;
- absorb useful Codex-only capability without importing Codex runtime machinery into Project Workflow semantics;
- prefer deletion of duplicated policy wording over adding new abstraction layers;
- any new common state/primitive must justify itself by a real cross-runtime correctness or recovery need;
- avoid turning the common layer into a larger contract than the two working branches it replaces.

### Stage 7 — Execution Prep / JIT — resolved

Detailed stage record:

`brainstorming/STAGE7_EXECUTION_PREP.md`

Current resolved direction:
- preserve the proven planned-work/JIT preparation model;
- materialize all currently knowable useful Cards;
- retain JIT triggers only for detail genuinely dependent on predecessor evidence;
- Main re-evaluates predecessor results rather than blindly flipping readiness;
- not-yet-started Cards remain refinable within existing L2 authority;
- READY remains semantic/project state, not worker assignment;
- no Project-Card concurrency metadata is required because Stage 8 later removed concurrent Card execution;
- launch-time refresh belongs to Execution.

Earlier Stage-7 exploration of `parallel_safe`, `write_scope`, `exclusive_resources` and concurrent execution-set selection is superseded by the later explicit no-parallel Project-Card decision.

### Seriality boundary — Project Cards only

The user's no-parallel decision applies only to Project Workflow Card concurrency.

- one Project Workflow Card active per selected workstream;
- runtime/internal worker topology for that Card is unrestricted by Project Workflow;
- internal subagents may be sequential or concurrent;
- Project Workflow does not model, count or schedule them;
- runtime internals must not create extra Project Workflow Cards or competing shared-state writers.

### User direction — remove Project Workflow parallel Card execution

The target V2 no longer includes bounded parallel execution of multiple Cards.

Consequences:
- exactly one Card may be `in_progress` per selected workstream;
- common execution preserves the proven ChatGPT-only serial lifecycle;
- Codex-only batch/lane/multi-member reconciliation machinery is not migrated into V2;
- earlier exploratory conclusions about Card-level concurrency metadata and multi-member `active_execution` are superseded;
- single-Card delegation remains allowed as runtime realization;
- Main remains the sole shared Project Workflow state writer and reasoning coordinator.

This is a deliberate simplification, not a temporary runtime limitation.

### Main delegation rule — clarified during Stage 8

For runtimes with qualifying implementation-worker capability:
- Main is the reasoning/orchestration owner, not the implementation worker;
- Card implementation is delegated;
- Main owns JIT decisions, authority, validation, integration, review routing and recovery;
- disappearance/failure of one worker does not authorize Main to implement the Card when delegated capability still exists;
- available-capability invocation failure follows runtime retry/blocker/recovery, not capability-absence fallback.

For runtimes that genuinely lack delegated implementation capability, the common workflow may allow the coordinating context to implement directly so runtime portability is preserved.

The stricter concrete worker-routing prohibition belongs to runtime orchestration (for example `codex_workflow`), while Project Workflow keeps only this capability-first semantic boundary.

### Stage 8 Main/worker boundary — accepted

For runtimes with qualifying implementation workers:
- Main reasons, routes, delegates, validates, reconciles and owns Project Workflow state;
- workers implement the active Card;
- worker completion is not Card completion;
- Main does not implement or make even small semantic/code fixes itself; corrections are delegated;
- worker-provided test/evidence may be accepted without automatic full rerun when sufficient;
- no ordinary `returned` Card state is added; the Card remains `in_progress` through Main validation/reconciliation;
- interrupted returned work is recovered from durable evidence before any re-execution;
- uncertain external side effects require readback before retry;
- no dedicated `transfer_ready` Card state is needed for runtime switching.

### Stage 8 — Execution — resolved

Detailed stage record:

`brainstorming/STAGE8_EXECUTION.md`

Stage 8 starts from a conservative merge of the two working execution paths:
- preserve the simple ChatGPT-only serial Card lifecycle;
- preserve Codex-only useful single-Card delegation/result-recovery behavior, while dropping bounded-parallel Card execution;
- Main/coordinator remains the reasoning owner and sole shared Project Workflow state writer;
- workers/subagents are bounded realizations, not competing coordinators;
- runtime capability may change how the one active Card is realized, not Card authority or READY meaning;
- runtime/model/session/worktree identity remains outside canonical Project Workflow state.

The previous universal `active_execution` / parallel execution-set direction is superseded. Stage 8 resolves to one active Project Workflow Card per selected workstream, with single-Card delegation/recovery and no extra ordinary execution wrapper.

### Supersession note for historical execution experiments

Earlier sections in this file that tentatively accepted Project-Card parallelism, multi-member `active_execution`, `prepared/transfer_ready`, batch/lane replacement semantics, or concurrency-safety Card metadata are **historical Brainstorming evidence only**.

They are superseded by the later explicit decisions recorded under Stage 7/8:
- exactly one Project Workflow Card is actively executing per selected workstream;
- no Project Workflow parallel Card execution;
- no universal `active_execution`, ordinary `returned`, or `transfer_ready` Card lifecycle state;
- runtime-internal subagent/concurrency topology is outside Project Workflow.

Do not use the older experimental sections as the current V2 target.

### Stage 9 review decisions — accepted

- activated `RECOMMENDED` review is a real blocking gate just like `REQUIRED`;
- reviewer that produced RED may later coordinate bounded correction after leaving reviewer role;
- if that context materially produces/repairs the changed subject, it cannot independently review that changed subject;
- Card, milestone and workstream final-integration review use one generic append-only review-attempt lifecycle;
- canonical review evidence is semantic-only; runtime telemetry remains runtime-owned.

### Stage 9 review-frequency decisions — accepted

- normal code/behavior/runtime-configuration workstreams retain at least one final-integration independent review gate;
- Card/milestone review is classified proportionally and is not automatic for every Card;
- exact stronger existing GREEN coverage is reused instead of performing duplicate final review;
- difficult-to-reverse external writes are reviewed at the last useful reversible checkpoint when practical, followed by write + readback;
- this review boundary does not invent a separate user-approval gate.

### Stage 9 — Independent Implementation Review — resolved

Detailed stage record:

`brainstorming/STAGE9_REVIEW.md`

Current baseline:
- one immutable exact subject per review attempt;
- append-only attempts across changed subjects;
- independence is semantic and subject-specific;
- context that materially produced/repaired the subject cannot independently review it;
- concrete runtime/product/worker/model/session/invocation/worktree identity is not canonical review evidence;
- GREEN may be consumed across runtime/context without replay;
- RED routes bounded correction without automatic user stop;
- fresh-context and delegated-review realizations are two ways to satisfy the same common independence obligation;
- old parallel-review deferral is superseded by the Stage-8 serial Project-Card decision.

### Stage 10 — Close / Publication / Integration — active analysis

Detailed stage record:

`brainstorming/STAGE10_CLOSE.md`

Current baseline:
- integration-target refresh and affected verification are common correctness;
- final-integration review uses the Stage-9 generic attempt model after refresh;
- merge/publication requires readback;
- workstream closure must remain recoverable after source-branch disappearance;
- deterministic closure bookkeeping may be distinct from behavioral implementation;
- branch cleanup realization is the main remaining ChatGPT/Codex divergence to grill.

## Current checkpoint / handoff

The current compact handoff is:

`implementation/workstreams/feature-common-preexecution-core/handoffs/BRAINSTORMING_READY_2026-09-21.md`

This Brainstorming record remains canonical exploratory authority.

The handoff records the resolved target V2 architecture, migration direction, evidence checkpoint and exact user-owned Definition promotion gate.

## Research needed

No external or repository-internal Research obligation remains before Definition.

Deferred N topology tests are post-implementation V2 validation, not missing Brainstorming evidence.

## Open material questions

Stage-by-stage reconciliation is still active. The cross-cutting audit is provisional architecture evidence, not Brainstorming completion authority.

Current focus: Stage 10 — Close / Publication / Integration. Stages 7, 8 and 9 are resolved after grilling.

## Next bounded work

Continue Stage 10 — Close / Publication / Integration grilling, focusing on durable target-side closure and branch-cleanup fallback.

Do not return to the Definition promotion gate until the remaining lifecycle stages have been reviewed individually and then reconciled cross-cutting.

## Outcome of this session

- Brainstorming status is `tentative`; the previous ready-for-definition conclusion was reopened because the lifecycle still needs stage-by-stage review.
- Scope remains `common-preexecution-core@R1`.
- Cross-cutting audit is complete.
- Target V2 common-core architecture and migration direction are resolved at Brainstorming level.
- Definition promotion authorization remains `pending`.
- Definition promotion subject remains `none`.
- Deferred N remains a V2 implementation-validation obligation, not a Brainstorming blocker.
- No production workflow module has been changed.
- Current phase/action: Stage 10 — Close / Publication / Integration analysis.

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`. Only explicit user authorization may promote the current exploratory scope into Definition.
