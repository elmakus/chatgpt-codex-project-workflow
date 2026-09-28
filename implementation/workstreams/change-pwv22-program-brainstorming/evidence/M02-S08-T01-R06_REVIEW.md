# M02-S08-T01-R06 Independent Review Evidence

Verdict: RED

Exact reviewed Result: `implementation/workstreams/change-pwv22-program-brainstorming/results/M02-S08-T01.md@edf9ece7241e25c6832d29a8be2458896a50662e:f8ff5c82f94a96b8deae64bf4d3f8a28912a0465`

Exact implementation subject: `elmakus/project_workflow_v2@1348a6b7c1649c151e5f216520dbf67aafb096e5`; `tools/pwv22_parallel.py` blob `1f3a1e155ecfbf3792ef90d0627e02b027778605`; `tests/test_pwv22_parallel.py` blob `dc527b38c201ada9c1536fd7a3f6b9b4a755eae4`.

## Finding

The R05 repair removes the self-referential Git locator and makes the admission artifact durably hashable, but the finite admission still binds only bare Card IDs. `typed_admission()` persists `cards: [str]`, and `parallel_legal()` / `compatible_fan_in()` authorize by testing only whether a caller-supplied `card_id` occurs in that list.

That means an admission accepted for Card ID `a` remains usable after the material Card/subject represented by `a` changes, because no exact subject locator is part of the admitted member and no subject equality is checked at use. Requirement 54 requires explicit finite accepted admission for the exact Cards/subjects involved; the Card likewise requires explicit finite exact admission. Bare stable IDs do not provide that exact-subject fence.

The focused tests prove exact identity of the admission artifact itself, but none changes a Card subject under the same Card ID and proves the old admission is rejected.

## Required correction

Make every admitted member bind the Card ID to an exact immutable subject identity (or an equivalent deterministic exact-subject representation), and require the presented work/fan-in operands to match that admitted subject. A changed subject under the same Card ID must fail closed until a new finite admission is durably accepted. Add focused stale-subject tests while preserving the R03-R05 protections, overlap/uncertainty serialization, one-mutator rule, exact ordered sibling Results and compatibility rejection.
