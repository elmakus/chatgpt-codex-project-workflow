# Design — ChatGPT-only branch-first lifecycle migration

## Pre-execution routing

The exact selected workstream manifest owns three locator-only fields:

- `routing.exploratory_scope` → active exploratory/brainstorming record;
- `routing.research_obligation` → active pre-execution Research record;
- `routing.plan_review` → active plan-review record.

The pointed artifact remains lifecycle authority. Root `PROJECT.md` is never updated to mirror these locators.

The Router validates non-null locators through `WORKSTREAMS.md` before using them. Missing, malformed, wrong-class, wrong-subject or contradictory locators fail closed to Recovery.

## Promotion

Brainstorming → Project Definition remains user-owned. Promotion authorization is read from the exact record identified by `routing.exploratory_scope`; the authorization subject must match that record's current scope/revision. The locator remains available for bounded Definition/Research recovery and is cleared only when Definition completes or the exploratory obligation is otherwise durably closed.

## Research

Pre-execution Research uses manifest `routing.research_obligation`. The Research record owns Status, Origin, Return target, reconciliation and result. Final-target reconciliation is persisted before the record is consumed and the locator cleared. Implementation/recovery Research remains Task-Board-owned and is never mirrored into the manifest pre-execution locator.

## Plan review

The review record under `planning/reviews/` remains the sole owner of plan-review state. The selected manifest `routing.plan_review` only locates the active record. A fresh review handoff may point directly to that exact record, while workstream recovery can reconstruct it from the manifest. Completed review state is preserved; the locator is cleared only after the owning Planning continuation durably reconciles the verdict.

## Execution-state migration

M02-T02 removes legacy/default as a normal live ChatGPT-only state context. Historical root/default state remains recovery input and must be migrated to an exact workstream before further managed mutation.

Recovery treats that migration as a higher-priority obligation than review, Research or execution on the historical board. Before creating or adopting a workstream branch it proves one exact migration topology from durable project/Git/PR evidence: intended `integration_target`, exact creation/adoption base, and independent-versus-stacked dependency classification. Independent migration uses the normal integration target/base with null parent fields; stacked migration is legal only with exact parent-workstream/branch evidence plus a concrete parent-only dependency. Ambiguous target/base/dependency topology fails closed.

Only after that topology is proven does Recovery recover or deterministically create one exact neutral branch-isolated workstream and materialize a manifest-bound namespaced Task Board carrying only the continuation truth required for coherent recovery. The manifest persists coherent `base_ref`, `integration_target` and parent metadata. Exact live Card/milestone review fields, implementation/recovery Research pointer, blockers, result/evidence/test pointers and required dependency results are preserved; immutable completed history may remain referenced in place and is not rewritten merely for layout.

The root/default board is read-only during migration. A partially materialized migration is recovered by the same exact identity rather than duplicated. Only after exact branch readback proves manifest ↔ Task Board identity and preservation of every live obligation does the namespaced Task Board become the sole mutable execution owner. Ambiguous source/branch/mapping state fails closed.

Long-lived legacy branches use the repository finalization migration only after active ownership is namespaced, so target-side historical/default files are not accidentally overwritten at integration. Review/Research ownership, seriality, micro-fix proportionality, target refresh and terminal recovery stay unchanged.
