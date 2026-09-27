# M02Q-T32 Execution Prep — legacy semicolon H017 Close composition

## Durable entry

- JIT owner: `after-M02Q-T31` after exact DONE/GREEN `M02Q-T31`.
- Consumer pre-materialization state: `elmakus/chatgpt-codex-project-workflow@bd3671fa0a4ba5bd27cc44c642cee786260b4431`, Task Board revision 270.
- Stable T32 Card: `3503ac925e32c4cda99a3e6b1c78184b17e41926:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/cards/M02Q-T32.md@f233d397732fa43953fbabdd416ce8227d8e484b`.
- Product start subject: `elmakus/project_workflow_v2@a2bc026262e1f4a16dd06d7b1ef04d8de5a98f9f`.
- Accepted legacy Result compatibility foundation: M02Q-T26 Result `04226fefd1e9e8d8a36d7d3239cba4396d4f0e12:dbe627dfbe342c2887facd325ba6b02ab910ff0c`.

## Exact RED-before

Direct H017 derivation on the exact current consumer checkout with the exact product start subject fails:

`CloseContractError: recovery package evidence '...M02R-T01_IMPLEMENTATION...; ...M02R-T01_REPAIR_R01...; ...M02R-T01_REPAIR_R02...' is dangling`.

The failure is causal and narrow. Ordinary DONE serving already calls `verify_legacy_result_migration`, whose accepted compatibility path splits historical semicolon evidence only after exact legacy proof succeeds. H017 `derive_recovery_package_from_board` instead calls raw `parse_card_result` and appends its comma-only `evidence_refs` directly into recovery-package evidence closure. The preserved M02R-T01/M02R-T02 historical Results therefore become one impossible path during H017 final serving.

## Boundary

T32 composes H017 with the already accepted legacy Result adapter for proved statusless historical DONE Results only. It does not alter historical bytes, migration schema, ordinary structured/current Result behavior, JIT proof state, review-acceptance compatibility, broader Close semantics, milestone review or M03.

One independently useful/falsifiable outcome exists: exact H017 recovery-package serving must consume individually validated evidence refs for a proved legacy statusless Result while all non-legacy behavior remains unchanged. A single Card is therefore coherent; splitting code and regression evidence would create no independently useful second outcome.

## Launch checks

- Exact T31 dependency Result is DONE and immutable at `911de5697453fe77e1d906082ad471da78910417:6de68dd209e3f7ae737b6ca0d6b745f88a4b57fb`.
- Exact T26 dependency Result is DONE and immutable at `04226fefd1e9e8d8a36d7d3239cba4396d4f0e12:dbe627dfbe342c2887facd325ba6b02ab910ff0c`.
- Product branch `work/pwv21-policy-kernel` is still exactly `a2bc026262e1f4a16dd06d7b1ef04d8de5a98f9f`.
- Fresh independent Card Review remains required after implementation.
