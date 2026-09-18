# M01-T01 Independent Review — Attempt 1

Card: `M01-T01`
Verdict: `RED`
Reviewed subject: `0f24c9053a4e41346b0e14a9d043421057a99767`
Implementation base inspected: `fcce41f9a5828c8cac526e1c615a97a2c5494910`
Workflow-main baseline verified: `03035876f3283d33e8a10ff43265f5be21a27a06`

## Authority checked

- `implementation/cards/M01-T01.md`
- `planning/CHATGPT_ONLY_MULTI_WORKSTREAM_MASTER_PLAN.md#M01--workstream-state-model-and-routing-foundation`
- requirements R1, R2, R3, R12, R14, R15 in `requirements/CHATGPT_ONLY_MULTI_WORKSTREAM_INTAKE.md`
- accepted `decisions/ADR_CHATGPT_ONLY_BRANCH_ISOLATED_WORKSTREAMS.md`
- GREEN plan review `planning/reviews/MW-R1.md`
- implementation evidence `implementation/evidence/M01-T01.md`

## Checks reproduced

- full implementation diff `fcce41f9...0f24c905` inspected across all 15 changed/added files;
- `git diff --check` passed;
- active ChatGPT-only/common wording audit found no remaining repository-global seriality claim in the M01 state/routing surfaces;
- no mixed/Codex/legacy parallel-lane mechanism was introduced;
- legacy/default Task Board fallback and workstream-local one-`in_progress` semantics are explicit.

## Blocking finding

The new manifest → Task Board resolution does not validate that the selected Task Board actually belongs to the selected manifest/workstream.

`WORKSTREAM_TASK_BOARD_TEMPLATE.yaml` introduces `workstream_id` and `execution_ref.branch`, but no active contract consumes either as a binding invariant. `WORKSTREAMS.md` validates the manifest branch and then reads `manifest.task_board` without requiring:
- Task Board `workstream_id == WORKSTREAM.id`;
- Task Board `execution_ref.branch == WORKSTREAM.branch`;
- a non-null/existing Task Board whenever the selected workstream has implementation/review/recovery state.

Therefore a manifest for workstream A can accidentally point at workstream B's Task Board and the current resolution algorithm can treat B's mutable Card/review state as A's. That violates R2's distinct mutable workstream-state requirement and weakens R12 recovery correctness; it also undermines the M01 acceptance claim that one exact workstream Task Board is deterministically resolved before implementation/review/recovery routing.

## Corrective classification

Bounded L1/L2 implementation correction inside already accepted M01 authority.

Required correction: make manifest/Task-Board binding validation normative in the workstream/state resolution contract, including exact ID + branch agreement and invalid-state handling for missing/null/mismatched selected boards. Preserve legacy/default fallback and avoid any global registry.
