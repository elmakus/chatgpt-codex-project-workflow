# M02Q-T31 F03 historical JIT consumed-proof migration — implementation evidence

## Subjects

- Immutable source Board for F03 inventory: `b4da01b7715cfa39743b7f35b6d05022ce0e5049:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/TASK_BOARD.toml@c388e19cacf687f3f02a143a7c17eb3c0a799db3`.
- T31 launch Board: `784380aea06e1b2256610d7d08bb36d11cb6690a`, revision 264.
- Pure 33-proof migration commit: `63817140f8e8adae17b8fc37a46346277d87a593`.
- Final verified state after bounded Card-parser Recovery: `8eb95db88ad799abfa8222c78e6931cff7a8c1eb`, Board revision 266.
- Corrected stable T31 Card: `37d8dbf1528d2d0b50af65639e7b5a5b6db2f277:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/cards/M02Q-T31.md@71342ffdc9f2b72eb75893ac50f427ac90657baf`.
- Accepted RF014 verifier/router subject: `elmakus/project_workflow_v2@a2bc026262e1f4a16dd06d7b1ef04d8de5a98f9f`.

## Exact migration

The immutable source Board contains 39 JIT triggers: 38 consumed, five already carrying exact consumed proof, and exactly 33 consumed triggers without proof. The 33 are exactly `after-M01-T01`, `after-M02-T01`, `after-M02R-T01..T12`, and `after-M02Q-T01..T19`.

The implementation maps them causally to:
- `after-M01-T01 → M02-T01`;
- `after-M02-T01 → M02R-T01`;
- each `after-M02R-T01..T12` to the immediately following `M02R` Card through T13;
- each `after-M02Q-T01..T19` to the immediately following `M02Q` Card through T20.

Direct immutable Card readback proved 33/33 downstream Cards declare the exact predecessor Result path+commit+blob owned by the Board. Every migrated proof uses the accepted four-key `card/path/commit/blob` schema, exact Card path, common ancestor proof commit `b4da01b7715cfa39743b7f35b6d05022ce0e5049`, and each downstream Card's exact stable blob at that commit/current bytes.

## Diff and preservation

Exact compare `784380aea06e1b2256610d7d08bb36d11cb6690a...63817140f8e8adae17b8fc37a46346277d87a593` is one commit and one changed file: `TASK_BOARD.toml`, +199/-1. The only deletion/addition replacement is Board revision 264→265; the remaining additions are the 33 nested proof tables.

Mechanical pre/post TOML comparison:
- source missing proof records at launch: 33;
- proofs added to that exact missing set: 33;
- migrated trigger core-field changes (`id/after_card/state/condition`): 0;
- pre-existing proof tables at launch: 6 (the five historical proofs plus `after-M02Q-T30 → T31`);
- changed pre-existing proof tables in the pure migration commit: 0;
- extra proof additions outside the 33-record set: 0.

The later bounded Recovery changes only T31's own parser-compatible arrow notation and rebinds `after-M02Q-T30` to the corrected T31 Card identity; see `M02Q-T31_RECOVERY_2026-09-27.md`.

## Exact verifier/readback

On Tower, clean temporary checkouts were pinned to consumer `8eb95db88ad799abfa8222c78e6931cff7a8c1eb` and product `a2bc026262e1f4a16dd06d7b1ef04d8de5a98f9f`.

- `validate_board`: PASS, Board revision 266.
- Current consumed triggers: 39.
- Current consumed triggers missing proof: 0.
- Exact accepted `verify_consumed_trigger`: PASS 39/39.
- This includes the 33 F03 migrations, all five earlier exact proofs and `after-M02Q-T30 → M02Q-T31`.
- Exact RF014 `jit_terminality_gate` verifies all consumed bindings and returns only `execution_prep` for `after-M02Q-T31`: the historical F03 barrier is gone and the separate downstream obligation remains visible.
- Full accepted product `sh scripts/test.sh`: exit 0; Python suite 1221/1221 GREEN; M01 baseline PASS.

The separately recorded legacy semicolon Evidence-refs/composed-final-serving defect is not corrected here. `after-M02Q-T31` remains waiting for that separate correction before fresh M02Q Milestone re-review; M03 remains blocked.
