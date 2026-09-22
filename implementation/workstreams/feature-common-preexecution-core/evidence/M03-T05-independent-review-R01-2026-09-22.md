# M03-T05 — independent review R01

Date: 2026-09-22
Card: `M03-T05`
Verdict: **RED / NOT READY**
Review owner: selected workstream Task Board
Review subject: `elmakus/project_workflow_v2@commit:1d9aa10721d7eb5764dec9bfae857715bd555a34|tree:4402bbb83461564717ced5ddcdf96eb6ba31e9e8|M03-T05-card-blob:4043f600450f0754af0874ea64ee104edc263ee6|acceptance-evidence-blob:9c671b9267280e1cb5c385fb6ba5260231d59a8c`

## Independence

This review was performed from the frozen durable subject by a fresh reviewer context that did not materially produce or repair the reviewed target subject. Runtime/model/session identity is intentionally not used as canonical independence evidence.

## Authority and evidence reviewed

- `planning/PROJECT_WORKFLOW_V2_MASTER_PLAN.md` revision `PWV2-P1`, complete M03 contract and §6 validation mapping.
- `requirements/PROJECT_WORKFLOW_V2.md` R1, including M03-owned/supporting PWV2-REQ-021..038, 051..052 and 067..071.
- ADR-PWV2-004, ADR-PWV2-005 and ADR-PWV2-006.
- M03-T01..T04 Card contracts/results/evidence, M02 handoff, and the Pi compatibility reconciliation referenced by M03-T05.
- Exact target `elmakus/project_workflow_v2@1d9aa10721d7eb5764dec9bfae857715bd555a34`, tree `4402bbb83461564717ced5ddcdf96eb6ba31e9e8`, cumulative M03 diff, production modules/helpers/templates/tests, and PR #3 readback.

The claimed baseline is reproducible: GitHub Actions run `35751124535` is GREEN on the exact target commit; independent detached-checkout validation also passed `sh scripts/test.sh`, full `unittest` discovery (72/72), `compileall`, `git diff --check`, and clean-tree verification.

## Blocking finding F1 — predecessor dependency is path-bound, not exact-result-bound

M03.P1 and M03-T01 require stable Cards to carry **exact completed-result dependencies**, and launch refresh must reject stale dependency/result state before execution. The production implementation does not preserve that invariant.

`tools/state_contract.py::parse_task_card` parses each `Dependencies:` entry only as a workstream-local `results/*.md` path. `tools/router.py::refresh_ready_card` then constructs the set of DONE predecessor dependencies from only `item["result"]["path"]` and accepts the Card when that path matches. The predecessor result locator's immutable `commit` and `blob` identity is not part of the Card dependency and is not compared during launch refresh.

An adversarial reproduction against the frozen target showed:

1. READY Card depends on `implementation/workstreams/sample-workstream/results/M01-T03.md`.
2. DONE predecessor initially points to that path with one exact commit/blob identity; launch routes to `execution_prep`.
3. The predecessor result is materially replaced under the **same path** and its exact commit/blob locator is changed.
4. Without changing the downstream Card, launch still routes to `execution_prep` with “READY Card passed launch refresh”.

Therefore a Card prepared from predecessor result S1 can execute after the predecessor has become S2 without a stale-input failure, JIT refresh, or explicit rebinding. This contradicts the M03.P1 exact-dependency/launch-refresh contract and M03-T01 acceptance (“stale/missing dependency or authority state fails closed before launch”). It also makes the M03-T01 evidence claim that exact result dependencies are validated stronger than the implementation actually proves.

The existing `test_ready_card_stale_dependency_fails_closed_before_launch` covers only a dependency path that is no longer a DONE predecessor result. It does not cover same-path immutable-result replacement, so the normal suite remains GREEN while this contract violation survives.

## Corrective classification

This is bounded L1/L2 M03 implementation work. No accepted requirement, ADR, Strategic Plan, Pi/Codex boundary or product decision needs to change, and no additional Research is required.

The corrected implementation must, at minimum:
- bind every Card predecessor dependency to immutable result identity, not path alone;
- compare the Card-bound dependency identity with the current DONE predecessor result during launch refresh;
- fail closed when the predecessor result changes under the same path;
- add deterministic regression coverage for the same-path changed-result case while preserving simple Card-only/YAGNI behavior and runtime-neutral state.

## Verdict

**RED.** The frozen M03-T05 subject does not satisfy the exact predecessor-dependency and stale launch-refresh acceptance contract. All other checked baseline suites/readbacks being GREEN does not waive this semantic defect.
