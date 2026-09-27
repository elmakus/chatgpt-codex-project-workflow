# M02Q-T26 implementation evidence — OBL-M02Q-03 legacy Result compatibility

## Exact product subject

- Repository: `elmakus/project_workflow_v2`
- Branch: `work/pwv21-policy-kernel`
- Parent candidate: `445eaa39542bdd272a5347fec29360b07cbe1463`
- Implementation commit: `9ba60dcc3eb5f4fab11e37b8b9d9c5d8462ea6f4`
- Changed files: `tools/legacy_result_provenance.py`, `tools/router.py`, `tools/state_contract.py`, `tests/test_legacy_result_provenance.py`, `tests/test_router.py`, `workflow/EXECUTION.md`, `workflow/STATE.md`.

The product adds an explicit Board-level `legacy_result_migrations` proof for immutable statusless historical Results. Normal/current structured Result serving remains unchanged and fail-closed. Compatibility requires exact immutable source repository/commit/path/blob/workstream/Card proof, prior DONE/source-Board durability, unchanged current Result bytes, and the ordinary independent GREEN review of the exact Result subject. Only inside that proved legacy path may historical semicolon-separated evidence refs and path-only historical Card acceptance be exact-derived from immutable Git state.

No consumer historical Result file was rewritten and no consumer migration proof record was added by this Card.

## Verification

Focused regression after implementation: **197/197 GREEN**. After the direct-script portability correction, the affected state/router/provenance subset remained GREEN.

Canonical full product gate on the committed clean tree:

- `PATH=/tmp/pwv21-test-venv/bin:$PATH bash scripts/test.sh`
- **1203/1203 tests GREEN**
- `M01 baseline checks: PASS`
- `git diff --check`: GREEN
- clean-tree gate: GREEN
- process exit: **0**

GitHub remote readback confirms branch `work/pwv21-policy-kernel` points to exact commit `9ba60dcc3eb5f4fab11e37b8b9d9c5d8462ea6f4`. GitHub Actions workflow run `36295197631` completed with conclusion **success**.

## Real-consumer compatibility readback

A temporary exact consumer simulation used the preserved current Board history and generated migration proofs for exactly the **23** DONE statusless legacy Results without changing their Result bytes. The committed T26 product served all 23, including M02R-T01/T02 semicolon evidence serialization and the corresponding path-only historical acceptance.

After those 23 were served, canonical routing advanced to the next separate residual at structured Result Card **M02Q-T09**, whose historical review acceptance is path-only. That residual is outside T26 scope and remains fail-closed instead of being silently generalized into this compatibility mechanism.

## Outcome

OBL-M02Q-03 product-side compatibility mechanism is implemented and verified. The separately allocated consumer-side 23-record append-only migration remains on `after-M02Q-T26` and must not be materialized until this Card has a fresh independent GREEN Card Review. M03 remains unmaterialized.
