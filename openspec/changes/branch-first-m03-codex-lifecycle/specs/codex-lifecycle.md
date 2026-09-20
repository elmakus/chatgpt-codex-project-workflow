# Specification — Codex-only branch-first lifecycle

## Pre-execution locator ownership

For durable Codex-only managed work, active exploratory, pre-execution Research and plan-review routing MUST use the exact selected workstream manifest `routing.*` locators. Root `PROJECT.md` MUST NOT own or mirror those active locators.

A non-null locator MUST be validated as the expected artifact class and exact selected workstream/authority subject before use. Invalid, stale or contradictory locator state MUST route to Recovery rather than global/transcript inference.

## Definition promotion

The first Brainstorming → Project Definition transition MUST remain explicitly user-owned. The exact exploratory record MUST be resolved through `routing.exploratory_scope`; durable authorization is valid only for the exact current promotion subject/revision.

## Pre-execution Research

Brainstorming, Project Definition, Strategic Planning and pre-execution Plan Review Research MUST use manifest `routing.research_obligation`. The Research record MUST remain sole owner of Status, Origin, Return target, reconciliation and result. The locator MUST remain until final-target reconciliation is durable and the record is consumed.

Implementation/recovery Research MUST remain selected-Task-Board-owned and MUST NOT be mirrored into root `PROJECT.md` or manifest pre-execution routing.

## Plan review

A REQUIRED/RECOMMENDED pre-execution plan review MUST keep lifecycle state in its exact `planning/reviews/<revision>.md` record and set selected manifest `routing.plan_review` to that record.

Codex Main MUST validate the locator before review, remain sole durable shared-state writer and persist the verdict returned by a Tester independent from the plan author. The Tester MUST NOT clear the locator. Planning MUST consume the exact verdict and clear/repoint the locator only with the corresponding durable approval/correction transition.

## Ownership and policy separation

Codex Main MUST remain the sole shared Project Workflow Task Board/integration-state writer. Runtime worker/session/model/profile/invocation/worktree identity MUST NOT become required durable project state.

Card/milestone review attempts MUST remain Task-Board-owned; workstream final-integration review MUST remain manifest-owned. Existing bounded batch and post-batch review-drain semantics MUST remain unchanged.

Codex-only lifecycle contracts MUST NOT import `workflow/chatgpt_only/*` lifecycle modules.
