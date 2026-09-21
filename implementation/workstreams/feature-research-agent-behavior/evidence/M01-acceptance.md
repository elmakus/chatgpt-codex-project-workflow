# M01 integrated acceptance — Research agent behavior

Date: `2026-09-21`
Milestone: `M01`
Verdict: **GREEN / integration-ready subject**

## Accepted implementation subject

- Behavioral implementation/result subject: `25ac000cac86c7421c3632f216be1074f61f64ce`.
- M01 contains one required Card, `M01-T01`, which is terminal `done` with independent review GREEN.
- The only commit between the tested implementation head `067d32c07f669df99c2acf3b4d1e0d3eb47613aa` and the reviewed subject adds implementation evidence only.

## Acceptance checked

- Approved outcome and RAB-REQ-001..010 are satisfied by the shared Research contract, both policy-local Research modules, the corrected shared template, JIT OpenSpec and focused regression coverage.
- ADR-RAB-001 boundaries remain intact: Research is evidence rather than accepted authority, proportional prior-art discovery is bounded, stronger evidence keeps precedence, and concrete Codex Investigator realization remains owned by `codex_workflow`.
- OpenSpec tasks are complete and consistent with the accepted behavior.
- Implementation evidence records targeted/relevant 28/28 and full repository 97/97 GREEN plus diff/conflict checks.
- Independent Card review is GREEN and found no acceptance mismatch or P0/P1 blocker.
- No migration, deployment, live-write or external-state cutover is part of M01.
- Current integration target `main` remains at the workstream base `13e27863cb11ec9e223ee2af191f79fe6b8d559d`; no target-drift reconciliation is required before final integration.

## Result

M01 intended final behavior is accepted. Remaining work is publication/final-target integration and merge-result-dependent closure bookkeeping; those operations must not change the accepted behavioral subject without reopening review coverage.
