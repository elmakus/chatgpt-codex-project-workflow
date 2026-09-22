# Stage 9 Brainstorming — Independent Implementation Review

Date: 2026-09-21
Scope: common-preexecution-core@R1
Status: resolved
Production authority: none
Baseline: current main fixed-policy review contracts + live review evidence J/K/L/M

## Purpose

Merge ChatGPT-only fresh-context review and Codex-only Tester review into one runtime-neutral independent-review semantic contract.

Primary rule:

> Project Workflow defines what independence means and what durable review state/evidence must exist. The active runtime decides how to realize an independent context.

Do not duplicate runtime worker/session/model mechanics in Project Workflow.

## Current V1 common core

Both fixed-policy branches already agree on the important semantics:

- review is attached to one exact immutable subject;
- REQUIRED and RECOMMENDED use the same independence mechanics once activated;
- review state is durable and recoverable;
- reviewer inspects exact authority, acceptance, actual result/source and evidence;
- reviewer must not mutate the subject while judging it;
- GREEN and RED require durable evidence;
- changed implementation after RED is a new exact subject and a new review attempt;
- prior attempts remain immutable/append-only;
- a reviewer/runtime replacement for the same unchanged subject does not create a new attempt;
- a GREEN verdict can be consumed later for deterministic finalization without replaying review;
- RED is not automatically a user stop; bounded correction routes back through the normal workflow.

The primary V1 difference is realization:
- ChatGPT-only requires a fresh normal ChatGPT context;
- Codex-only delegates to an independent Tester worker/session.

That realization difference should not define two Project Workflow state machines.

## Candidate common review attempt

Conceptual shape:

```yaml
review:
  requirement: REQUIRED | RECOMMENDED | none
  current_attempt: R02
  attempts:
    - id: R01
      mode: independent_review | coverage_reuse
      state: pending | in_progress | green | red
      subject: <exact immutable reviewed subject>
      evidence: <semantic-only evidence>
      independence:
        requirement: independent_context
        realization_state: resolve_independent_context | awaiting_independent_context | independent_context_active | satisfied
        evidence: <semantic-only evidence>
      covered_by: null
```

Exact field names are not yet Definition authority.

## Independence semantics

A context/realization is not independent for an exact subject if it materially produced, repaired or transformed that subject.

This remains true even when:
- its competing local correction did not become canonical;
- its publication lost a CAS/push race;
- another equivalent correction became the durable result.

Independence is per exact reviewed subject, not a permanent property of the whole chat/session.

A context that reviewed one subject may later be routed to deterministic continuation. If it then implements a new changed subject, it becomes a producer for that new subject and cannot independently review that new subject.

## Runtime-neutral realization

When qualifying delegated independent-review capability exists:
- Main resolves/delegates the independent review through the runtime;
- concrete worker/model/session/invocation identity stays runtime-owned;
- canonical Project Workflow evidence records only semantic independence facts.

When the current runtime cannot realize an independent reviewer internally:
- persist the same pending review obligation;
- route to a fresh independent context using the available surface mechanism;
- after the verdict, return to the same common router.

Failure to invoke an available independent-review capability is runtime failure, not capability absence.

## Main/reviewer ownership

Reviewer:
- reads exact subject/authority/evidence;
- judges it independently;
- returns/persists verdict evidence through the owning review path;
- does not implement production correction while acting as reviewer.

Main/coordinating context:
- owns routing and shared Project Workflow state;
- freezes exact review subject;
- resolves independent-review realization;
- consumes GREEN;
- classifies RED and delegates/routes correction;
- does not manufacture a verdict for a subject it produced.

## GREEN

GREEN:
- is durable for the exact immutable subject;
- is not replayed because reviewer/session/runtime disappeared;
- returns to the common router;
- deterministic finalization may continue immediately when legal;
- no artificial user stop is required merely to report GREEN.

Live J validated:
- independent GREEN in one runtime/context;
- later finalization in another context/runtime;
- no implementation replay;
- no review replay;
- unchanged subject remains one attempt.

## RED -> repair -> new review

RED:
- remains immutable evidence for the failed subject;
- does not itself require a user stop when correction is bounded and authorized;
- routes correction through Execution Prep/Execution, Planning, Definition or Research according to the actual authority change;
- corrected result is a new immutable subject and appends a new attempt;
- correction-producing context cannot issue the independent verdict for that corrected subject.

Live K validated the lifecycle:

```text
R01 RED(S1)
-> bounded correction S2
-> append R02(S2)
-> independent R02 GREEN
```

R01 remains immutable.

## Semantic-only evidence

Canonical review evidence must not persist concrete runtime telemetry merely to prove independence:
- no worker role label;
- no model identity;
- no session UUID;
- no invocation UUID;
- no worktree/workspace identity.

Allowed evidence states semantic facts such as:
- exact immutable subject;
- reviewer did not materially produce/repair that subject;
- review was read-only with respect to the subject;
- independence requirement satisfied;
- concise GREEN/RED findings.

K exposed telemetry leakage in an experimental runtime path.
M validated the clean semantic-only evidence shape.

## Authoritative refresh

Fresh context does not guarantee fresh repository state.

Before a new review/recovery context selects its obligation:
- resolve exact authoritative workstream/ref;
- refresh authoritative durable state when it may have advanced elsewhere;
- establish current authoritative head;
- reconcile local state;
- read canonical review state;
- only then route.

Expected-base/CAS remains the publication guard.

Live L validated this behavior.

## Review continuity topology

The common semantic contract should allow both:

### Capable coordinator/runtime

A capable Main may perform a deterministic chain without artificial user stops:

```text
review R01
-> RED
-> route/delegate bounded correction
-> create R02
-> delegate a genuinely independent R02 reviewer
-> GREEN
-> deterministic finalization
```

The same Main coordinates the chain, but the implementation and independent verdict contexts remain semantically distinct where required.

### Fresh-context-only realization

A fresh ChatGPT review context may:
- produce R01 RED;
- after leaving reviewer role, perform/coordinate bounded correction if routed there;
- freeze the new R02 subject;
- then stop only because the new exact subject requires another independent context.

A fresh reviewer that produces GREEN may continue deterministic finalization in the same chat.

These topology scenarios remain deferred V2 validation (N-CAPABLE / N-CHATGPT), not a current Brainstorming blocker.

## Interaction with Stage 8 serial execution

Stage 8 now allows exactly one active Project Workflow Card per selected workstream.

Therefore old Codex rules that deferred review while sibling parallel Cards were unresolved are not part of target V2.

For a reviewable Card:
- implementation result becomes canonical through Main validation/reconciliation;
- exact review subject is frozen;
- Card remains non-terminal while REQUIRED/RECOMMENDED review is pending;
- review may proceed immediately; there is no parallel-group drain to wait for.

## Coverage reuse

A stronger existing independent GREEN verdict may be reused for a later final-integration gate only when:
- exact reviewed subject/accepted result is identical or exact coverage is proven;
- the acceptance surface required by the later gate is fully covered;
- no relevant refreshed/integrated change invalidates coverage.

Coverage reuse should use the same generic attempt/history model rather than a second special review lifecycle.

## Current open material questions

1. Should RECOMMENDED continue to be a real blocking gate once activated, exactly like REQUIRED, with the only difference being why it was requested?
2. After RED, may the same context that just acted as independent reviewer become the Main/coordinator for bounded correction, provided it does not itself issue the next independent verdict for the changed subject?
3. Should one generic append-only review model be used for Card, milestone and final-integration review, instead of keeping final-integration review as a separate mutable lifecycle?
4. For review evidence, is concise semantic evidence enough, with detailed runtime diagnostics kept only in runtime-owned logs?

These are Brainstorming questions, not accepted Definition decisions.


## Grilling decisions — common review model

User accepted:

1. Once `RECOMMENDED` review is part of the accepted contract and activated, it is a real blocking gate just like `REQUIRED`. The distinction records why the gate exists, not whether it may be skipped.
2. After an independent reviewer produces RED, that same chat/context may leave reviewer role, return through the router and act as Main/coordinator for bounded correction when legally routed there. If it materially produces/repairs the changed subject S2, it is disqualified from independently reviewing S2.
3. Card review, milestone review and workstream final-integration review should use one generic append-only attempt model rather than separate mutable review state machines. Ownership/subject differ; lifecycle semantics do not.
4. Canonical Project Workflow review evidence remains concise and semantic. Concrete model/worker/session/invocation/worktree/runtime telemetry stays runtime-owned and is not persisted merely to prove independence.

These decisions preserve the proven ChatGPT-only/Codex-only review semantics while removing product-specific realization details.


## Grilling decisions — review frequency and coverage reuse

User accepted:

1. Normal intake-created issue/feature workstreams that change code, runtime configuration, external behavior or system behavior retain at least one independent final-integration review gate. Use `REQUIRED` when existing risk authority warrants it; otherwise at least `RECOMMENDED`.
2. Card/milestone review is not automatic for every Card. Activate it only when the accepted contract/risk/checkpoint gives a concrete reason for independent review.
3. Do not duplicate review when an already-independent GREEN verdict proves exact coverage of the final integrated subject and the entire later acceptance surface. Reuse that stronger coverage through the same generic review history model.
4. For difficult-to-reverse/high-risk external writes, place independent review at the last useful reversible checkpoint when practical, then perform the authorized write and required post-write readback/verification. This is a review boundary, not an automatic user-approval gate.

Target review frequency therefore remains proportional:
- ordinary Cards: no automatic independent review;
- material/high-risk/checkpoint Cards: independent review when classified;
- normal behavioral/code workstream: at least one final-integration independent review unless exact stronger coverage is proven.


## Stage 9 completion audit

After grilling and comparison with current fixed-policy contracts:

- one generic append-only review-attempt model is sufficient for Card, milestone and final-integration review;
- REQUIRED and activated RECOMMENDED use identical blocking/independence mechanics;
- review remains proportional: no automatic independent review for every Card;
- normal behavioral/code workstreams retain at least one final-integration independent review unless exact stronger coverage is proven;
- independence is exact-subject semantic independence, not product/session identity;
- a RED reviewer may later coordinate bounded correction after leaving reviewer role, but cannot independently review a changed subject it materially produced/repaired;
- GREEN is durable and reusable across contexts/runtimes without replay;
- exact stronger GREEN coverage may satisfy a later final-integration gate when subject + acceptance coverage are proven;
- canonical evidence remains semantic-only;
- authoritative refresh + CAS protect review routing/publication;
- Stage-8 serial Project-Card execution removes old Codex batch-review deferral requirements;
- high-risk external writes may be reviewed at the last useful reversible checkpoint, followed by write + readback, without inventing a user-approval gate.

Counterfactual challenge:
- keeping separate mutable final-integration review state would duplicate lifecycle semantics without adding correctness;
- keeping Tester/fresh-ChatGPT identity in canonical review state would couple semantics to runtime realization;
- automatically reviewing every Card would add cost without corresponding risk evidence;
- allowing a correction producer to review its own changed subject would violate the validated independence invariant.

No remaining Stage-9 semantic decision is open.

Stage 9 is resolved at Brainstorming level.
