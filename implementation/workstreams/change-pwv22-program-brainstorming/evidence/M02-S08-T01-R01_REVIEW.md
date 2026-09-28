# M02-S08-T01-R01 Independent Review Evidence

Verdict: RED

Exact reviewed Result: `implementation/workstreams/change-pwv22-program-brainstorming/results/M02-S08-T01.md@4f9328baf3d127eaddfb7e914b862f3dce555e4a:3faad98f9c0691e7881f01131d4caf11cbabefe8`

Exact implementation subject: `elmakus/project_workflow_v2@e291bf8daf2d88a59f043da937c24043ab5d4d7e`.

## Finding

The Card requires explicit finite exact admission and states that revoked/non-admitted work cannot become accepted. R7 requirement 54 requires an explicit finite **accepted admission fact** for the exact Cards/subjects.

The implementation's `typed_admission()` validates only the shape of an arbitrary mapping. `parallel_legal()` accepts that mapping directly and therefore has no exact accepted-admission identity or acceptance proof to verify. A caller can manufacture a well-shaped admission record and obtain parallel legality without any accepted admission fact.

Separately, `compatible_fan_in()` has no admission operand or admission check. The focused revoked-admission test covers only `admitted()`; it does not demonstrate that revoked/non-admitted work cannot enter accepted fan-in. Thus the required acceptance property is not established by the reviewed subject.

## Required correction

Bind legality/fan-in to an exact accepted finite-admission fact using the native exact-identity/acceptance primitives, reject absent/stale/unaccepted/revoked admission, and add negative tests proving fabricated/unaccepted and revoked/non-admitted subjects cannot pass the acceptance/fan-in boundary. Preserve conservative conflict serialization and exact ordered sibling compatibility.
