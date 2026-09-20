# M01-T01 Implementation Evidence — 2026-09-20

## Subject

- Card: `M01-T01 — Make Codex-only orchestration continuous`
- Implementation start boundary: `8309c840b490d67330476a67119ac6faedc19a36`
- Exact immutable implementation subject: `291e4628444c97bbb4ab645108d94161eaf036e8`
- Integration target baseline at Refresh Gate: `main@ce3cf3fc80b923ad26b77d9ac66fb3db5ad31f5f`
- Refresh result: GREEN — integration target remained at the workstream base; no target drift required reconciliation.

## Authority

- `planning/CODEX_ONLY_CONTINUOUS_ORCHESTRATION_MASTER_PLAN.md@COCO-P2` — approved after independent GREEN plan review.
- `requirements/CODEX_ONLY_CONTINUOUS_ORCHESTRATION.md` R1 / COCO-R1…COCO-R7.
- `decisions/ADR_CODEX_ONLY_CONTINUOUS_MAIN_ORCHESTRATION.md`.
- `decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md`.
- Stable Card contract: `implementation/workstreams/change-codex-only-continuous-orchestration/cards/M01-T01.md`.

## Implemented scope

- Removed the normal `codex_only` Context Health/FRESH coordinator-hygiene stop and its Router dispatch.
- Removed `workflow/codex_only/CONTEXT_HEALTH.md`.
- Removed the Planning allowance for coordinating-context refresh boundaries and explicitly prohibited planned coordinator hygiene checkpoints.
- Clarified durable Recovery and the Project Workflow / `codex_workflow` runtime replacement boundary.
- Preserved existing Close automatic-next-milestone and independent Tester continuation semantics.
- Documented the `chatgpt_only` versus `codex_only` distinction in README/CHANGELOG.
- Added `tests/test_codex_only_continuous_orchestration_contract.py`.

## Exact implementation range

GitHub compare `8309c840b490d67330476a67119ac6faedc19a36..291e4628444c97bbb4ab645108d94161eaf036e8` is linear and contains exactly these eight files:

- `CHANGELOG.md`
- `README.md`
- `tests/test_codex_only_continuous_orchestration_contract.py`
- `workflow/codex/CODEX_ORCHESTRATION.md`
- `workflow/codex_only/CONTEXT_HEALTH.md` — removed
- `workflow/codex_only/PLANNING.md`
- `workflow/codex_only/RECOVERY.md`
- `workflow/codex_only/ROUTER.md`

No `workflow/chatgpt_only/*` file and no existing ChatGPT-only Context Health regression test changed.

## Verification on exact subject

The checkout was reset to exact remote subject `291e4628444c97bbb4ab645108d94161eaf036e8` before final verification.

- Dedicated continuous-orchestration contract: **7/7 GREEN**.
- Full repository Python unittest suite: **77/77 GREEN**.
- `git diff --check ce3cf3fc80b923ad26b77d9ac66fb3db5ad31f5f..291e4628444c97bbb4ab645108d94161eaf036e8`: **GREEN**.
- `git diff --name-only ce3cf3fc80b923ad26b77d9ac66fb3db5ad31f5f..291e4628444c97bbb4ab645108d94161eaf036e8 -- workflow/chatgpt_only tests/test_chatgpt_only_context_health_contract.py`: **empty / unchanged**.
- Dedicated contract proves the `codex_only` Context Health file/router dispatch is absent, Planning cannot schedule the old refresh boundary, Close still permits automatic next-milestone continuation, Recovery replaces hygiene handoffs, runtime ownership remains with `codex_workflow`, and ChatGPT-only Context Health surfaces remain present.

## Acceptance / review boundary

M01-T01 implementation acceptance is GREEN pending its contracted independent review. The Card remains non-terminal because its `RECOMMENDED` independent-review gate must review the exact immutable subject `291e4628444c97bbb4ab645108d94161eaf036e8`.

This evidence is implementation-owned and does not constitute an independent review verdict.
