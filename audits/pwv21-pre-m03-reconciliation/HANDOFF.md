# PWv2.1 Pre-M03 Reconciliation Handoff

## Completed reconciliation package

- Exact source harvest HEAD: `7ff23a18e6966ece83eaf8bda45c8923e49791e8`
- Source terminal population: 30 = 28 CONFIRMED_MATERIAL + 2 REJECTED + 0 NEEDS_MORE_EVIDENCE
- Repair families: 17
- Technical/downstream-relevance classifications: 1 MUST_RECONCILE_BEFORE_M03 / 7 CAN_DEFER / 9 REQUIRES_CHECKPOINT_READBACK
- Complete H001-H030 mapping: yes
- H011 and H013 preserved as REJECTED / NO_REPAIR
- User-selected resolution policy: `QUALITY_FIRST_PRE_M03`
- User resolution target: `resolve_before_m03_if_still_applicable`
- Checkpoint applicability readback under the quality-first policy: 17 / 17 repair families
- Authority-first families: 1 (`RF008`)
- Product repair performed: no

## Quality-first pre-M03 boundary

Technical relevance classification and user-selected resolution policy are separate dimensions. The prior labels remain semantic/downstream-relevance metadata and are not rewritten to pretend that all families are intrinsically M03 blockers.

At the future reconciliation checkpoint, read back the exact then-current candidate for all 17 repair families. For each family, determine whether the defect still exists. If it is already corrected, record it as satisfied by current implementation. If it is still applicable, determine whether accepted M02R authority already authorizes the corrective work. When it does, propose the smallest coherent corrective Card in dependency order. When it does not, require explicit pre-M03 authority/replan or a separate authorized maintenance workstream. Do not silently broaden M02R.

Still-applicable families are the user's target for resolution before M03, subject to accepted authority. RF008 remains authority-first: if still applicable, return to accepted Definition/Planning and accept the proof mechanism before implementation selects or enforces one.

No corrective implementation Cards have been created. Product repair has not started.

## Quality-first dependency order

RF008 → {RF007, RF005, RF017, RF002, RF016} → {RF012, RF013, RF009, RF006} → {RF004, RF003, RF010, RF011} → RF001 → RF014 → RF015

Respect each family's explicit `depends_on` edges; the grouped order above is a compact topological resolution sequence, not an authorization to repair.

## Workspace boundary

This branch contains reconciliation-policy evidence only under `audits/pwv21-pre-m03-reconciliation/`. It contains no product implementation repair, no canonical workflow-state change, no active PWv2.1 workstream mutation, no corrective Card creation, no PR creation and no merge.
