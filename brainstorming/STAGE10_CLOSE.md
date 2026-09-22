# Stage 10 Brainstorming — Close / Publication / Integration

Date: 2026-09-22
Scope: common-preexecution-core@R1
Status: active analysis
Production authority: none
Baseline: current main fixed-policy CLOSE/WORKSTREAMS contracts

## Purpose

Merge the proven ChatGPT-only and Codex-only close/integration semantics into one runtime-neutral contract.

This stage owns what happens after implementation/review is accepted:
- milestone close;
- integration-target refresh;
- final-integration review reuse/freeze;
- publication/PR verification;
- durable workstream closure;
- source-branch cleanup;
- transition to the next approved milestone/workstream obligation.

Do not turn Close into another orchestration engine.

## Current V1 common core

Both fixed-policy branches already share most of the important close semantics:

- all required Cards/reviews must be terminal/GREEN before normal close;
- integrated milestone acceptance checks the approved outcome, tests, evidence, relevant constraints and external readback;
- RED creates bounded corrective work rather than silently closing;
- branch-isolated final integration refreshes the current target before merge/publication;
- stacked-parent dependencies must be satisfied before child integration;
- material target movement is reconciled with the smallest authorized technical change;
- affected verification is rerun after reconciliation;
- final-integration review coverage is decided **after** refresh;
- target movement alone does not invalidate an existing GREEN when exact covered content/behavior + acceptance surface are unchanged and compatibility remains GREEN;
- material change to the covered subject creates a new exact review subject/attempt;
- successful external publication/merge must be verified/read back;
- final target must retain enough durable workstream history for recovery before the source branch may disappear;
- Close returns to normal routing/automatic continuation when no real stop remains.

The main V1 divergence is branch cleanup realization and some policy-specific review/runtime wording.

## Integration refresh

Before actual final integration/publication:

1. resolve exact selected workstream and target;
2. establish current target truth;
3. satisfy parent/stacked dependency topology;
4. compare against the last validated/reconciled target baseline;
5. if materially changed, perform the smallest authorized reconciliation;
6. rerun affected verification;
7. only then decide whether existing independent GREEN coverage still applies or a new final-integration review subject is needed;
8. immediately before merge/publication, re-read target again if it may have moved.

This is common correctness, not runtime-specific behavior.

## Final-integration review

Stage 9 resolves one generic append-only review-attempt model.

Close therefore does not own a second special review state machine.

For REQUIRED/RECOMMENDED final-integration review:
- reuse exact stronger existing independent GREEN when complete coverage is proven after refresh; or
- freeze the exact refreshed integrated subject and route the generic review obligation;
- RED routes bounded correction and later creates a new exact subject/attempt;
- only GREEN/valid coverage permits final integration.

## Durable closure package

A workstream is not durably closed merely because code merged.

Before the source workstream branch may disappear, the integration target (or another accepted durable target-side location) must retain the recovery-relevant workstream package, including the exact terminal lifecycle/result/review evidence needed to reconstruct completed truth without the source branch.

If merge result metadata can only be known after the merge:
- perform the smallest closure-only target-side reconciliation;
- do not change the accepted implementation subject merely to write lifecycle bookkeeping;
- read back and verify the target-side closure package.

The same principle applies to intentionally terminal-unmerged/superseded workstreams: preserve lifecycle/history without publishing rejected implementation content.

## Branch cleanup — current V1 divergence

Current ChatGPT-only can persist a fallback cleanup obligation such as exact `safe_to_delete` state when it cannot physically delete the source ref.

Current Codex-only expects capable Main/runtime to delete the exact branch and verify its absence, without a separate cleanup lifecycle.

Earlier cross-cutting Brainstorming direction:

1. first prove common terminal safety and durable target-side recovery package;
2. if branch is already absent, cleanup is complete;
3. if current runtime can safely delete it, verify exact ref/head, delete exact branch, verify absence;
4. if deletion capability is unavailable, persist a minimal exact cleanup fallback for a later capable context;
5. later cleanup must revalidate the exact ref/head before deleting;
6. never invent alias/delete-marker refs;
7. cleanup state is workstream lifecycle fallback, not runtime identity.

This needs final Stage-10 grilling because the user prefers keeping V2 small.

## Publication / external write

Publication, PR merge, release/cutover or other external mutation follows the ordinary execution safety rule:

```text
ACTION -> READBACK -> VERIFY EXPECTED STATE -> EVIDENCE
```

Do not invent a user confirmation merely because an operation is deployment/live write.

If accepted authority explicitly contains an authorization gate, honor it.

Independent review may occur at the last useful reversible checkpoint for difficult-to-reverse/high-risk writes per Stage 9.

## Main/worker boundary during Close

Main/coordinator owns:
- integration refresh reasoning;
- exact review coverage decision;
- deterministic Git/PR/workflow-state reconciliation;
- publication/readback orchestration;
- Task Board/manifest/terminal package state;
- branch cleanup coordination.

When qualifying workers exist:
- behavioral/code reconciliation that requires implementation judgment is delegated;
- Main may perform deterministic/mechanical Git/workflow operations and lightweight checks;
- runtime-specific worker/tool/session details remain outside Project Workflow.

## Automatic continuation

Close should not stop merely to announce success.

After durable milestone/workstream closure:
- return to the common router;
- advance to the next already-approved legal obligation when dependencies/reviews/gates allow it;
- stop only for a real unresolved user/product authority, explicit accepted authorization gate, or concrete unremediable access/runtime/input blocker.

Detailed Stage 11 analysis will own the broader continuation topology.

## Current open material questions

1. After final merge/closure, should Project Workflow always attempt to delete the source workstream branch automatically when current capability supports it?
2. If the current runtime cannot delete the exact safe branch, should we keep a tiny durable `safe_to_delete` fallback for later cleanup, or simply leave the branch with no Project Workflow cleanup state?
3. For a normal completed workstream, should Close always persist/read back the durable target-side recovery package before considering the workstream done, even when repository hosting already auto-deletes the source branch?
4. Should deterministic closure-only bookkeeping after merge be allowed without opening a new implementation/review subject, provided it cannot change accepted behavior/content?

These are Brainstorming questions, not accepted Definition decisions.
