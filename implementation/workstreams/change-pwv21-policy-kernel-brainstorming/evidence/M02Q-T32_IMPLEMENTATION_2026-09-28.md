# M02Q-T32 implementation — legacy semicolon H017 Close composition

## Exact subjects

- Consumer launch state: `elmakus/chatgpt-codex-project-workflow@fb9a4fd0f04a126feb4a1ec4876c3289b77faa40`, Task Board revision 272, Card `M02Q-T32` in progress.
- Product start subject: `elmakus/project_workflow_v2@a2bc026262e1f4a16dd06d7b1ef04d8de5a98f9f`.
- Product implementation commit: `b1a52afd51fbf9b5e480bbed52b70ede3fec0119` (`tools/close_contract.py`).
- Product regression commit / final subject: `5352386e4328c967543c1b6cce6ebf80d54b4b88`.
- Final product tree: `f24aa33e9630d19cc122ddd99584ae3890345134`.
- Final blobs:
  - `tools/close_contract.py@8b9192d26ca0877d6067a19e36b9314a4df0feaf`
  - `tests/test_close_contract.py@eab52ff6b6dc890a7e72fce569d983833cc2f6d0`

## Implemented correction

H017 `derive_recovery_package_from_board` keeps ordinary structured/current Result parsing unchanged. When a Result is statusless legacy data, H017 now checks the Board for the existing exact `legacy_result_migrations` proof and, when present, invokes the already accepted `verify_legacy_result_migration` compatibility path before collecting evidence refs. The adapted Result therefore supplies individually normalized historical semicolon evidence refs only after full legacy provenance verification. Duplicate, invalid, stale or incoherent legacy proof remains fail-closed as a Close-contract error.

No historical consumer Result, Review, Task Card or evidence bytes were rewritten. The legacy migration schema, current structured Result path, review-acceptance compatibility, JIT proof state, fresh milestone review and M03 were not broadened or absorbed.

## RED-before / GREEN-after

Exact RED-before on consumer `bd3671fa0a4ba5bd27cc44c642cee786260b4431` plus product `a2bc026262e1f4a16dd06d7b1ef04d8de5a98f9f` reproduced the defect:

`CloseContractError: recovery package evidence '...M02R-T01_IMPLEMENTATION...; ...M02R-T01_REPAIR_R01...; ...M02R-T01_REPAIR_R02...' is dangling`

The raw H017 path treated the preserved semicolon serialization as one Git locator.

On final product `5352386e4328c967543c1b6cce6ebf80d54b4b88` with exact current consumer `fb9a4fd0f04a126feb4a1ec4876c3289b77faa40`, the same composed H017 derivation succeeds:

- recovery package locators: **373**
- package digest: `sha256:5579b5fea0c4bfe07057b01b3b45005b13888b00003c8d0bdab9015e014dbd1c`

## Tests and remote readback

- Focused H017 + legacy provenance: **18/18 GREEN**, including the new verified-adapter positive seam and invalid-adapter fail-closed regression.
- Clean exact-head full product gate: **1223/1223 GREEN**.
- `M01 baseline checks: PASS`.
- `scripts/test.sh`: exit 0 on clean exact product HEAD.
- GitHub Actions final-head run `36355277678` (`test`, run 824): completed **success**.
- Remote branch exact final product HEAD: `5352386e4328c967543c1b6cce6ebf80d54b4b88`.

Fresh independent Card Review remains required before T32 may be finalized.
