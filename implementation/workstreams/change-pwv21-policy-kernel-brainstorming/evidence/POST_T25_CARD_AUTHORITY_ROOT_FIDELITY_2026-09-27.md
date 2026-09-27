# Post-T25 Close live finding — stable Card authority-root fidelity

## Trigger

After M02Q-T25 R01 and deterministic Card finalization, Close/H017 was reread against the accepted PWv2.1 product candidate `elmakus/project_workflow_v2@445eaa39542bdd272a5347fec29360b07cbe1463`.

The first fail-closed condition is the stable Card parser rejecting M02Q-T22 because `task_card.authority_refs[4]` points under the workstream evidence directory rather than an accepted authority root.

## Classification

This is a **Planning-to-Execution-Prep fidelity defect** under PWV21-REQ-122, not a new product goal or accepted-authority defect. The accepted P7/requirements/ADR authority is unchanged. The invalid entries are evidence/provenance inputs that were incorrectly serialized into the stable Card's `Authority refs` field.

PWV21-REQ-073 requires only materially affected acceptance surfaces to be revalidated. PWV21-REQ-125 preserves immutable prior Result/Review history; old exact blobs are not rewritten.

## Full current Card inventory audit

All 40 current Card contracts were inspected against the accepted `parse_task_card` authority-root rule (`requirements/`, `decisions/`, `planning/`, `workflow/`).

Exactly three current Card contracts contain an out-of-root authority ref:

1. `M02Q-T22` blob `bae478eccef547ff9ecf91f3944ec7506609bdc9`:
   `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/M02Q_MILESTONE_COMPOSITION_OBLIGATIONS_2026-09-26.md`
2. `M02Q-T23` blob `fd3810cc1847bc4fe0441d93e917d3ca41d4b1dd`:
   `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/M02Q_MILESTONE_COMPOSITION_OBLIGATIONS_2026-09-26.md`
3. `M02Q-T25` blob `73d4870bb456f937f597f3f54d3bdabd72a47b11`:
   `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/M02Q-T23_LATE_OVERSIZE_2026-09-27.md`

The other 37 current Card contracts have only accepted-root authority refs.

## Bounded correction

For each affected Card, remove only the invalid evidence-path member from `Authority refs`; preserve Included scope, Excluded scope, dependencies, acceptance, required tests/readback, review requirement and technical contract byte-for-byte otherwise.

- T22 is corrected first because H017 reaches it first. Its existing exact Result/product subject remains unchanged, but the changed acceptance surface requires a new exact Card Review attempt before T22 may again be terminal.
- T23 is a bound `returned` late-oversize handoff with no accepted GREEN result; correct only its stable contract metadata while preserving its immutable return evidence and residual binding.
- T25's R01 remains immutable historical review evidence for the old exact acceptance. After its Card correction, it requires a new fresh full-scope review attempt binding the unchanged exact Result to the corrected acceptance before T25 can again be terminal.

The corrections do not authorize M03 and do not consume OBL-M02Q-03, the historical consumed-trigger migration, or the M02Q Milestone Review.
