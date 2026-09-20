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

M03-T02 removes root/default as a normal live Codex-only execution context. Historical root/default state remains read-only recovery input and must migrate to one exact branch-isolated workstream before further managed mutation.

Migration outranks review, Research, batch recovery and execution on the historical board. Before creating or adopting a workstream branch, Recovery proves one exact topology from durable project/Git/PR evidence: intended `integration_target`, exact creation/adoption base and independent-versus-stacked dependency classification using the policy-local Intake rules. Independent migration uses the normal target/base with null parent fields; stacked migration is legal only with exact parent-workstream/branch evidence plus a concrete parent-only dependency. Ambiguous target/base/dependency topology fails closed.

After topology proof, Recovery reuses or deterministically creates one neutral workstream identity, materializes a coherent manifest-bound namespaced Task Board, and preserves only exact continuation truth needed for recovery: plan/milestone identity, live Cards/dependencies, semantic implementation owner, append-only Card/milestone review attempts, implementation Research pointer, results/evidence/blockers and the complete current batch/history lineage needed to preserve frozen base/member order/returned/integrated refs/post-batch review drain. Runtime worker/session/model/profile/invocation/worktree identity is not migrated because it is non-authoritative.

The historical root board remains unmodified. Partial migration recovers the same deterministic identity and topology rather than creating a duplicate lane. Exact branch readback must prove manifest ↔ Task Board binding, persisted topology and preservation of every live review/Research/result/dependency/batch obligation before mutable ownership switches to the namespaced board.

Long-lived legacy branches use repository finalization migration only after active ownership is namespaced, so independently evolved target-side historical/default files are not overwritten. Micro-fix proportionality, Codex Main sole-writer ownership, exact-subject Tester independence, bounded batch semantics, target refresh, terminal target-side package and source-branch-deletion recovery remain unchanged.
