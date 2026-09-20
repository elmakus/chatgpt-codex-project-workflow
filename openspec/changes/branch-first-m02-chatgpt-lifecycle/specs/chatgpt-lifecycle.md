# Specification — ChatGPT-only branch-first lifecycle

## Pre-execution locator ownership

For durable ChatGPT-only managed work, active exploratory, pre-execution Research and plan-review routing MUST use the exact selected workstream manifest `routing.*` locators. Root `PROJECT.md` MUST NOT own or mirror those active locators.

A non-null locator MUST be validated as the expected artifact class and exact selected workstream/authority subject before use. Invalid or contradictory locator state MUST route to Recovery.

## Definition promotion

The first Brainstorming → Project Definition transition MUST remain explicitly user-owned. The exact exploratory record MUST be resolved through `routing.exploratory_scope`; durable authorization is valid only for the exact current promotion subject/revision.

## Pre-execution Research

Brainstorming, Project Definition, Strategic Planning and pre-execution Plan Review Research MUST use manifest `routing.research_obligation`. The Research record MUST remain sole owner of Status, Origin, Return target, reconciliation and result. The locator MUST remain until final-target reconciliation is durable, then be cleared with/after consumption. Implementation/recovery Research MUST remain selected-Task-Board-owned.

## Plan review

A REQUIRED/RECOMMENDED pre-execution plan review MUST keep lifecycle state in its exact `planning/reviews/<revision>.md` record and set selected manifest `routing.plan_review` to that record. The manifest MUST NOT mirror review verdict fields. Recovery MUST prefer the exact manifest locator over transcript/global inference.

## Historical execution state

New or continued managed ChatGPT-only execution MUST NOT use root `implementation/TASK_BOARD.yaml` as a normal mutable context. Historical root/default state MAY be read only to recover/migrate an exact obligation and MUST transition to a branch-isolated workstream before further mutation.

Migration MUST recover or deterministically create exactly one workstream identity, create/reconcile its manifest-bound namespaced Task Board before resuming the obligation, preserve exact live review/Research/result/evidence/dependency truth, and validate manifest ↔ Task Board binding by branch readback before the namespaced board becomes mutable authority. The historical root/default board MUST remain non-mutable migration/history input during this transition. Partial or ambiguous migration MUST fail closed and MUST NOT create a duplicate lane.

Completed historical artifacts MUST NOT be deleted or rewritten solely for topology normalization. A long-lived legacy branch MAY reconcile root historical files against the integration target only after active ownership has migrated, and only as final-integration conflict/history preservation rather than as live execution.

## Safety preservation

The migration MUST preserve exact-subject independent review, implementation Research ownership, seriality, micro-fix proportionality, target refresh, terminal target-side package and source-branch-deletion recovery semantics.
