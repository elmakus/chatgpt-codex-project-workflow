# ChatGPT-only Planning

## Responsibility

The strategic-planning role **organizes an accepted Project Definition into an executable project strategy**.

It owns:
- Master Plan structure/revision;
- milestone sequence, outcomes and dependencies;
- stable milestone-level acceptance/checkpoints;
- requirement-to-milestone coverage;
- high-level planned work packages;
- deployment/migration/system-verification strategy inside accepted authority;
- JIT decomposition triggers;
- explicit execution boundaries/gates inherited from the accepted definition;
- planning-level risk/order decisions that do not change accepted product/system intent.

It does **not** own:
- inventing or changing product/system requirements;
- accepting strategic/high-level architecture/product choices that belong in `decisions/`;
- silently resolving an open user/product choice;
- concrete Task Card state or live implementation state.

Those belong to Project Definition or later execution roles as routed.

The strategic-planning role is not bound to a named model or reasoning level.

## Preconditions

Before planning:

- canonical requirements exist and are `approved`;
- material strategic/high-level decisions required to plan are accepted;
- unresolved research uncertainty does not materially block milestone architecture;
- no unresolved user/product choice can materially change the target definition.

If these conditions fail:
- missing/contradictory accepted intent → return to Project Definition;
- missing evidence → use the durable Research handoff below, then return to Research;
- broader option generation/comparison needed → return to Brainstorming;
- explicit user/product decision needed → real user stop.

Do not compensate for an incomplete definition by inventing strategic authority inside the plan.

## Research handoff from Planning

When Planning needs evidence before it can make a valid planning decision:

1. create one exact record under `workflow/chatgpt_only/RESEARCH.md#Durable record contract`, with `Origin role: strategic_planning`, the current plan revision/planning obligation as Origin subject, `Return target: strategic_planning:<exact subject>`, and `Return reconciliation: pending`;
2. for pre-execution Planning, set the selected workstream manifest `routing.research_obligation` to that exact record before yielding;
3. when replanning active implementation/recovery work, set Task Board `research_obligation` instead and do not mirror it into root `PROJECT.md` or manifest pre-execution routing;
4. persist record + owning pointer before returning to the router for Research.

When that record becomes `complete` for this Strategic Planning subject, follow `workflow/chatgpt_only/RESEARCH.md#Final Return-target protocol`. The target-specific reconciliation is the exact planning result: updated planning authority and, when REQUIRED/RECOMMENDED review still applies, the exact next plan revision/review boundary. Persist that result and `Return reconciliation: applied` + exact result refs in the same durable Git transition. Only then consume/clear. Recovery from `applied + complete` must not create another plan revision or review record.

## Inputs

Use:
- project `PROJECT.md`;
- approved canonical requirements;
- accepted decisions;
- only relevant verified research/evidence referenced by that definition;
- current project/source baseline when materially needed to organize execution;
- current approved Master Plan when replanning.

Read Task Board/current handoff only when planning or replanning an active project.

Do not load implementation files merely to create distant speculative design.

## Master Plan

The approved Master Plan normally lives at `planning/MASTER_PLAN.md`.

Cover as applicable:
- problem/goal and accepted target state by reference to Definition authority;
- verified execution baseline needed by the plan;
- canonical requirements/decision pointers;
- non-goals, invariants and external constraints that shape execution;
- milestones and stable checkpoint/acceptance for each;
- milestone dependencies/order;
- planned work packages at the level knowable now;
- requirement coverage;
- explicit user/deployment/live-write authorization gates;
- deployment/migration strategy;
- system verification strategy;
- idempotency/data-integrity/security strategy;
- JIT decomposition triggers where concrete execution detail is not yet knowable;
- fresh-context boundaries only when materially useful;
- relevant OpenSpec/handoff policy references when they materially shape execution.

Do not duplicate the full text of requirements/decisions when exact authority references are sufficient.

The Master Plan is not the live task tracker. Mutable execution state lives only in Task Board.

## Milestones

A milestone is a stable integrated/testable checkpoint, not a small implementation task.

Each milestone should define:
- outcome/state that must become true;
- requirement ownership;
- dependencies;
- stable acceptance/checkpoint;
- applicable inherited invariants/decisions;
- explicit boundary/authorization gates;
- planned work packages when knowable;
- JIT trigger for detail that genuinely depends on predecessor evidence.

Milestone boundaries and ordering are planning decisions as long as they remain inside the accepted Project Definition.

If planning reveals that a required milestone outcome would require changing accepted product/system intent, frozen strategic decisions, global invariants or authorization boundaries, return to Project Definition instead of changing them here.

An approved Master Plan milestone subsection is the default milestone contract. Create a separate `implementation/milestones/MXX.md` only when JIT execution preparation needs material execution/acceptance detail not already present.

## Planned work packages versus Task Cards

Planning may decompose a milestone into **planned work packages/tasks** when that improves clarity and requirement coverage.

These are planning structure, not executable Task Cards.

Do not assign live state, result pointers or executor metadata to planned work packages.

`EXECUTION_PREP.md` owns conversion of currently knowable work into concrete Task Cards and may split/merge/reorder not-yet-started Cards through delegated L2/JIT authority without strategic replanning.

If exact Card scope depends on predecessor evidence, record the JIT trigger instead of inventing a placeholder Card.

## Deferred decomposition

Freeze only what is knowable and strategically important.

For deferred work preserve enough authority to prevent downstream invention:
- intended outcome;
- requirement ownership;
- dependencies;
- inherited constraints/decisions;
- knowable outcome-level acceptance;
- explicit gates;
- exact durable evidence/result that will make decomposition knowable.

Distant implementation interfaces must not be frozen merely to make the plan look complete.

## Planning authority and escalation

Within an accepted Project Definition, Planning may decide:
- milestone partition/order;
- dependency structure;
- execution strategy/sequence;
- planned work-package grouping;
- verification/migration sequencing;
- JIT boundaries;
- planning-level risk controls.

Downstream roles may decide:
- **L1 — execution detail:** implementation choices inside an accepted Card/milestone;
- **L2 — JIT decomposition/refinement:** create/split/merge/reorder/replace not-yet-started Cards and refine technical acceptance/interfaces from durable predecessor evidence.

Return to Planning when evidence requires changing the approved execution strategy, milestone structure/order or future milestone outcomes **without changing accepted Project Definition**.

Return to Project Definition when evidence requires changing:
- requirements;
- accepted strategic/high-level decisions;
- global product/system invariants;
- product/external behavior contract;
- explicit authorization boundary;
- another accepted target-state property.

Never hide known strategic ambiguity as deferred implementation detail.

## Requirement coverage

Every authoritative requirement must:
- map to at least one owner milestone in the Master Plan;
- have an execution path expressed as a planned work package or durable JIT trigger;
- receive at least one concrete Task Card from Execution Prep before implementation of that requirement;
- reference OpenSpec when the behavior/API/schema/state/security/cross-package contract warrants it.

The Master Plan does not need speculative future Task Card IDs.

## Pre-implementation planning audit

Before plan review/approval, the planner performs its own audit:
- false assumptions and P0/P1 risks;
- consistency with approved requirements/decisions;
- milestone boundaries/order;
- dependency completeness;
- missing outcome-level acceptance;
- requirement coverage;
- data integrity/idempotency/security;
- migration/rollback;
- system verification;
- explicit authorization gates;
- OpenSpec boundaries;
- overengineering or premature implementation detail;
- unresolved questions that should have routed back to Definition/Research.

Apply the policy-neutral `workflow/common/AUTHORITY.md#YAGNI--proportional-design` invariant during this audit. For each material increase in solution complexity, ask which current requirement, accepted constraint, verified evidence, existing contract or demonstrated current reuse justifies it; hypothetical future need alone is insufficient.

Resolve deterministic planning defects directly.

If a material gap belongs to Project Definition or requires user/product authority, route there instead of approving around it.

## Independent plan review

Preserve the workflow rule: perform an independent plan review when practical.

Classify the Master Plan:
- `REQUIRED` when project/user authority explicitly requires independent plan review;
- `RECOMMENDED` for a new or materially revised Master Plan when independent review is practical;
- `none` for trivial/editorial plan changes that do not alter execution strategy, milestone structure, requirement coverage or accepted gates, or when independent review is concretely impractical and no project/user authority requires it. For a nontrivial `none`, record the concrete reason in the planning audit; convenience alone is not enough.

Record the classification in the Master Plan.

For REQUIRED/RECOMMENDED review, one review record corresponds to one exact plan revision/subject. Any substantive correction after a verdict must create a new plan revision before opening the next review attempt; do not reuse a completed review record for a different subject.

For REQUIRED/RECOMMENDED review:
1. keep the plan `Status: draft`;
2. freeze the exact reviewed plan subject;
3. create the separate `planning/reviews/<plan-revision>.md` record as `pending`;
4. set the selected workstream manifest `routing.plan_review` to that exact review record in the same durable handoff boundary; the manifest remains locator-only;
5. return to the router and stop at the fresh independent-plan-review boundary.

Use `workflow/chatgpt_only/PLAN_REVIEW.md` for the independent review lifecycle.

The chat that authored the exact plan subject cannot issue its independent verdict.

## Plan approval

Mark the Master Plan `approved` only when:
- Preconditions still hold;
- the planner's own planning audit is GREEN;
- REQUIRED/RECOMMENDED independent plan review is GREEN, or review classification is `none`;
- after GREEN, the approved plan body still matches the exact reviewed subject; only deterministic lifecycle metadata may change without opening a new review subject;
- requirement coverage is complete at milestone/work-package-or-JIT level;
- no unresolved Definition-owned choice is hidden in the plan;
- explicit gates are represented;
- execution can begin without inventing strategic authority.

Plan approval means **execution organization is accepted inside the already-approved Project Definition**. It does not redefine product/system intent.

For a branch-isolated REQUIRED/RECOMMENDED plan review, keep manifest `routing.plan_review` pointed through the independent verdict. Planning owns verdict consumption: after verifying the exact GREEN record/subject and durably approving that plan revision, clear `routing.plan_review`. A RED record stays pointed until Planning durably creates the corrected revision and either repoints the locator to its new pending review record or resolves the review lifecycle under accepted authority. Never clear the locator merely because a reviewer role ended.

## Route transition

Planning is a bounded role.

After an approved plan is persisted:
1. update `PROJECT.md` plan pointer/high-level status when material;
2. return to `workflow/chatgpt_only/ROUTER.md`;
3. if the current user/project scope already authorizes implementation, the next normal route is Execution Preparation;
4. if the user requested planning only, approved scope ends here and the normal user-stop contract applies.

Do not create Task Board/Card state merely to announce that planning is complete.

## Replanning active work

When replanning an active project:
- preserve completed historical evidence/results;
- read only active Task Board/handoff/source state needed to understand the affected future scope;
- change only not-yet-accepted future plan authority unless explicit recovery requires otherwise;
- record the new Master Plan revision and superseded planning assumptions;
- return through the router so Execution Prep/Recovery can reconcile downstream contracts/state.

If the trigger actually changes Project Definition, Definition must be reconciled first.

## Competing research/prototype paths

When genuinely independent alternatives need experimentation, Planning may identify the need, but Research/experimental evidence remains separate from accepted plan authority.

Path A / Path B branches may start from the same stable checkpoint when useful. Each produces independent findings/evidence/prototype results.

A production plan may use A/B/Hybrid only after the relevant strategic choice is accepted through Project Definition.

Experimental code is not merged merely because it exists.

## Distant work

Distant work stays functionally specific without freezing nonexistent interfaces.

Execution Prep + Refresh Gate reconcile implementation detail against the actual source/runtime when the work becomes current.
