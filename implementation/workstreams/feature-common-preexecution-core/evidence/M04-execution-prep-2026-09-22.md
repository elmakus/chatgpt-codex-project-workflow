# M04 Execution Prep — 2026-09-22

Workstream: feature-common-preexecution-core
Plan: PWV2-P1
Milestone: M04 — Integration, tracker closure, publication and terminal recovery
Target repository: elmakus/project_workflow_v2
Target branch: feat/pwv2-m04-integration-close
Creation base: main@29f5e1880d66949c3009afa399490a6a81bc949a

## Preconditions

- M03 is GREEN and integrated through target PR #3.
- Target M03 merge tree is identical to the reviewed M03 tree.
- Frozen Definition R1, ADR-PWV2-003/005 and approved PWV2-P1 remain valid.
- M04 introduces no unresolved product/strategy choice; current target state makes the four approved packages contractible.
- Construction custody remains in the V1 control workstream.

## JIT decomposition

Five bounded Cards are now contractible:

1. M04-T01 — integration refresh and review-coverage preservation.
2. M04-T02 — external effects and final tracker lifecycle.
3. M04-T03 — target-side terminal recovery and cleanup.
4. M04-T04 — trigger-only fork lineage and end-of-scope semantics.
5. M04-T05 — cumulative M04 acceptance and immutable review freeze.

T01..T04 are individually review-free and covered by cumulative exact-subject independent review in T05. No OpenSpec/technical-contract artifact is created: the Card contracts and accepted M04 plan already define the required behavior precisely.

## JIT boundaries

- actual target movement selects affected compatibility checks at Close time rather than creating a general merge engine;
- actual external-operation support selects readback implementation while deterministic helpers remain provider-neutral;
- fork lineage is implemented as trigger-only semantics and does not authorize a real release;
- M05 delivery/plugin work remains excluded.

## Next legal obligation

M04-T01 is READY from integrated M03 main@29f5e1880d66949c3009afa399490a6a81bc949a. A target implementation branch can now be created from that exact base and execution may continue automatically.
