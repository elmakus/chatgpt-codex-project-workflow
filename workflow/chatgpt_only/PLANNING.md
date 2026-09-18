# ChatGPT-only Planning

## Responsibility

The strategic-planning role owns:
- problem definition;
- verified baseline;
- authoritative requirements;
- accepted architecture/decisions;
- global invariants;
- milestone outcomes;
- requirement coverage;
- explicit user/deployment/live-write authorization gates.

Implementation detail that depends on current source/runtime is reconciled later through execution preparation and Refresh Gate. Do not freeze distant code-dependent detail prematurely.

## Inputs

Use:
- project `PROJECT.md`;
- canonical requirements;
- accepted decisions;
- relevant verified research;
- current project/source baseline when needed.

## Master Plan

The approved Master Plan normally lives at `planning/MASTER_PLAN.md`.

Cover as applicable:
- problem/goal;
- verified current state;
- target state;
- authoritative requirements;
- frozen architecture decisions;
- non-goals;
- global invariants/external constraints;
- known source seams;
- milestones and checkpoint/acceptance for each;
- milestone dependencies;
- explicit user/authorization gates;
- requirement coverage;
- deployment/migration strategy;
- system verification;
- idempotency/data-integrity/security constraints;
- JIT decomposition triggers where detail is not yet knowable.

The Master Plan is not the live task tracker. Mutable execution state lives only in Task Board.

An approved Master Plan milestone subsection is the default milestone contract. Create a separate `implementation/milestones/MXX.md` only when JIT preparation needs material execution/acceptance detail not already present.

## Milestones

A milestone is a stable integrated/testable checkpoint, not a small implementation task.

Define stable outcome and acceptance without pretending distant implementation interfaces are already known.

Planner quality must survive decomposition. Persist material rationale, invariants, failure semantics, rejected-path constraints and other implementation-shaping intent in durable authority.

An approved milestone sequence authorizes execution of that approved scope, but never bypasses an explicit user/deployment/live-write gate.

After a GREEN milestone, ChatGPT may continue automatically into the next already-approved milestone when prerequisites/reviews are satisfied and no strategic or authorization gate intervenes.

## Deferred decomposition

Freeze only what is knowable and strategically important.

A future milestone may remain less detailed when correct Task Card decomposition materially depends on predecessor evidence. It must still define:
- outcome that must become true;
- requirement ownership;
- dependencies;
- applicable invariants/accepted decisions;
- knowable outcome-level acceptance;
- explicit gates;
- exact durable evidence/JIT trigger after which decomposition becomes knowable.

Do not invent placeholder cards merely to make the plan look complete.

## Delegated planning authority

Decision classes:

- **L1 — execution detail:** choices inside an accepted Task Card/milestone contract.
- **L2 — JIT decomposition/refinement:** create/split/merge/reorder/replace not-yet-started cards; complete JIT milestone detail; refine technical tests/acceptance/interfaces from durable predecessor evidence.
- **L3 — strategic replan:** change to requirements, accepted/frozen architecture or decisions, global invariants, milestone outcome, product/external behavior contract, or explicit authorization boundary.

L1/L2 may proceed without returning to the original planning session. L3 returns to strategic authority/user decision.

Never hide an already-known strategic ambiguity as deferred implementation detail.

## Requirement coverage

Every authoritative requirement must have:
- an owner milestone;
- at least one implementation Task Card before execution of that requirement;
- relevant OpenSpec when the behavior/API/schema/state/security/cross-package contract warrants it.

A coverage matrix may point to a JIT trigger instead of speculative future Card IDs.

## Pre-implementation audit

Before execution preparation, audit:
- false assumptions;
- high-risk gaps;
- milestone boundaries;
- task sizing/dependencies;
- missing acceptance/tests;
- requirement coverage;
- data integrity/idempotency/security;
- migration;
- OpenSpec boundaries;
- overengineering.

Resolve material gaps or record an explicit blocker.

## Distant work

Near-term cards may be detailed. Distant work stays functionally specific without freezing nonexistent interfaces.

Any Card whose assumptions can drift before execution requires a fresh Refresh Gate at start.
