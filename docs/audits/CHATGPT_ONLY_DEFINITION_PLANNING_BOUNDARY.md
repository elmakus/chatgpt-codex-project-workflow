# Audit — Project Definition / Planning Boundary

Date: 2026-09-18  
Base: `main@a6ac7fdd431fb80ebd095313e3ed89f11be560ef`  
Audited branch: `refactor/definition-planning-boundary@58c45994358808596978480ece0ad1357ab41c16`

Verdict: **GREEN**

## Target lifecycle

```text
BRAINSTORMING ↔ RESEARCH
        ↓
PROJECT DEFINITION
        ↓
PLANNING
        ↓
EXECUTION PREP
        ↓
EXECUTION
```

The purpose of the refactor is to prevent Planning from simultaneously deciding what the project should be and how execution should be organized.

## Role ownership

### Brainstorming

Owns:
- ideas;
- alternatives;
- tentative hypotheses;
- open questions.

Does not produce accepted requirements/decisions by itself.

Exit:
- evidence needed → Research;
- enough evidence/accepted user intent to formalize target state → Project Definition.

### Research

Owns:
- verified facts/evidence;
- current-state findings;
- assumptions/uncertainties;
- alternatives/recommendations when requested.

Does not promote itself directly into accepted requirements/decisions/plan authority.

Exit:
- findings ready to shape target state → Project Definition.

### Project Definition

Canonical module:
`workflow/common/DEFINITION.md`

Owns promotion into:
- `requirements/`;
- `decisions/`;
- unresolved product/strategic questions;
- high-level PROJECT pointers/status where material.

Definition answers WHAT must become/remain true plus strategic/high-level HOW that must be accepted before planning.

Definition does not own:
- milestone sequencing;
- work-package decomposition;
- Task Cards;
- live execution state.

Definition Complete requires:
- explicit target state;
- material MUST requirements;
- constraints/non-goals/invariants;
- acceptance-level outcomes;
- accepted strategic/high-level decisions needed before planning;
- no material unresolved user/product choice;
- coherent approved canonical requirements.

Transitions:
- missing evidence → Research;
- more option generation → Brainstorming;
- unresolved user/product authority → real user stop;
- Definition Complete GREEN → Planning.

### Planning

Canonical module:
`workflow/chatgpt_only/PLANNING.md`

Consumes:
- approved canonical requirements;
- accepted decisions;
- referenced verified evidence;
- only baseline/source context materially needed for execution organization.

Owns:
- Master Plan revision;
- milestone sequence/outcomes/dependencies;
- stable outcome-level acceptance/checkpoints;
- requirement-to-milestone coverage;
- planned work packages;
- migration/deployment/system-verification strategy inside accepted Definition;
- JIT decomposition triggers;
- inherited execution/authorization gates.

Does not own:
- changing accepted requirements;
- accepting missing product/architecture choices;
- concrete Task Card state.

### Execution Prep

Owns conversion of currently knowable planned work into concrete Task Cards + Task Board state.

It may perform delegated L2/JIT split/merge/reorder/refinement of not-yet-started Cards inside accepted Definition + approved Plan.

## Planned work packages versus Task Cards

Master Plan may include planned work packages/tasks for clarity and coverage.

They are not executable Task Cards and carry no live status/result/executor state.

Exact Card IDs are not required at plan approval when real scope depends on predecessor evidence.

Execution Prep creates Cards just-in-time before implementation.

## Requirement ownership timing

Project Definition no longer has to know future milestone IDs.

During Definition:
`Owner milestone = unassigned` is valid.

Planning assigns:
- owner milestone;
- planned work package or durable JIT trigger.

Execution Prep assigns:
- concrete Task Card before implementation.

This removes the previous circular dependency where requirements were expected to know milestone ownership before Planning had run.

## Strategic escalation split

When downstream evidence invalidates accepted authority:

- requirements / strategic decisions / global product-system invariants / product-external behavior / authorization boundary → **Project Definition**;
- milestone structure/order/outcome or execution strategy while Definition remains valid → **Planning**;
- missing evidence needed to decide either → **Research**.

Execution Prep now returns above L1/L2 authority to the router for this classification.

## Plan approval

Planning may mark Master Plan approved only when:
- Definition Complete remains GREEN;
- planning audit is GREEN;
- requirement coverage exists at milestone + work-package-or-JIT level;
- no Definition-owned choice is hidden inside the plan;
- gates are explicit;
- execution can begin without inventing strategic authority.

If current scope already authorizes implementation:
`PLANNING → ROUTER → EXECUTION_PREP`

If user requested planning only:
planning completion is end of approved scope.

## Pre-implementation audit

Planner audit covers:
- false assumptions / P0/P1;
- Definition consistency;
- milestone boundaries/order;
- dependencies;
- outcome-level acceptance;
- coverage;
- data integrity/idempotency/security;
- migration/rollback;
- system verification;
- authorization gates;
- OpenSpec boundaries;
- overengineering/premature detail;
- unresolved questions that belong in Definition/Research.

A separate independent plan review is not an implicit default lifecycle gate. If user/project authority explicitly requires one, the exact plan revision must be frozen and the planner may not pretend to independently review its own subject.

## Template audit

GREEN:
- `templates/REQUIREMENTS.md` permits unassigned milestone during Definition;
- `templates/DECISION.md` permits milestone/Card linkage to remain none until later roles;
- `templates/MASTER_PLAN.md` states Planning consumes approved Definition;
- Master Plan uses planned work package/JIT trigger instead of speculative Task Card IDs;
- Master Plan workflow references point only to active common/chatgpt_only modules;
- Brainstorm and Research templates route authority promotion through Definition.

## Router audit

GREEN:
- explicit Project Definition route exists;
- Planning route requires approved requirements/accepted decisions;
- incomplete Definition returns to Definition instead of silent planner decisions;
- Strategic Blocker classifies to Definition vs Planning vs Research;
- role-transition example includes Research → Definition → Planning → Execution Prep.

## Static checks

PASS:
- Definition persists to existing requirements/decisions instead of adding duplicate authority;
- Definition does not own milestones;
- Definition Complete gate exists;
- Brainstorming routes to Definition;
- Research routes to Definition;
- Planning requires approved requirements;
- Planning explicitly does not own product/system requirements;
- planned work packages are distinct from executable Task Cards;
- Planning returns to Execution Prep after approval when implementation is authorized;
- replanning ownership is split from Definition ownership;
- Execution Prep strategic escalation routes to Definition/Planning/Research;
- requirements milestone ownership may remain unassigned during Definition;
- Master Plan contains no legacy workflow path references.

## Final verdict

**GREEN.** The workflow now has a distinct accepted Project Definition layer between exploration/evidence and execution planning. Planning is reduced to execution organization, and Execution Prep remains the owner of concrete Task Cards.
