# Design — Codex-only branch-first lifecycle migration

## Pre-execution routing

The exact selected Codex-only workstream manifest owns three locator-only fields:

- `routing.exploratory_scope` → active exploratory/brainstorming record;
- `routing.research_obligation` → active pre-execution Research record;
- `routing.plan_review` → active plan-review record.

The pointed artifact remains lifecycle authority. Root `PROJECT.md` is integrated project authority/navigation only and is never updated to mirror these locators.

The Router validates every non-null locator through `WORKSTREAMS.md` before use. Missing, malformed, wrong-class, wrong-subject, wrong-workstream or contradictory locator state fails closed to Recovery.

## Promotion

Brainstorming → Project Definition remains user-owned. Promotion authorization is read from the exact record identified by `routing.exploratory_scope`; the authorization subject must match that record's current scope/revision. The locator remains available for bounded Definition/Research recovery and is cleared only after Definition completes or the exploratory obligation is otherwise durably closed.

## Research

Pre-execution Research uses manifest `routing.research_obligation`. The Research record owns Status, Origin, Return target, reconciliation and result. Final-target reconciliation is persisted before the record is consumed and the locator cleared.

Execution Prep / implementation / recovery Research remains selected-Task-Board-owned and is never mirrored into manifest pre-execution routing or root `PROJECT.md`.

## Plan review

The review record under `planning/reviews/` remains sole owner of plan-review state. Selected manifest `routing.plan_review` only locates the active record.

Codex Main validates the locator/record/subject and remains the sole durable review-state writer. Runtime realizes an independent Tester for the exact immutable plan subject. The Tester never clears the locator. Planning consumes GREEN/RED and clears or repoints the locator only after the corresponding planning transition is durable.

## Codex ownership preservation

This routing migration does not change execution orchestration:
- Codex Main remains sole shared Task Board/integration-state writer;
- concrete Executor/Tester/Investigator identity and worktree paths remain runtime-owned and non-authoritative;
- Card/milestone review attempts remain Task-Board-owned;
- manifest `review` remains final-integration-review-only;
- serial-default and bounded batch/post-batch review-drain semantics remain unchanged.

## Execution-state migration

Historical/default execution-state migration is owned by M03-T02. M03-T01 changes only the minimum routing boundary needed so pre-execution continuation is already workstream-local and fail-closed.
