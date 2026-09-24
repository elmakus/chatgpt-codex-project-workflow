# M02-T01 implementation evidence

Date: 2026-09-24
Card: `M02-T01`
Target repository: `elmakus/project_workflow_v2`
Target branch: `work/pwv21-policy-kernel`
Accepted M01 base: `a92c2c5f0eefd9d0bcd9fb75be4624b3719fff02`
Implementation subject: `5d0da25d9d08740a56591ba3738c6ab3dc9451ba`

## Implemented M02 surface

- Added closed, versioned transport-neutral JSON contracts:
  - `schemas/EXECUTION_OBLIGATION.schema.json`
  - `schemas/EXECUTION_RESULT.schema.json`
- Added executable contract implementation in `tools/obligation_contract.py`.
- Activated the reserved M02 kernel seams in `tools/policy_kernel.py`:
  - `compile_obligations()`
  - `validate_results()`
  - `reconcile()`
- Added `workflow/EXECUTION_CONTRACTS.md` and bound the typed boundary into `workflow/EXECUTION.md`.
- Added golden obligation/result fixtures and `tests/test_obligation_contract.py`.
- Added `scripts/test-obligation-contract.sh` and wired it into the full repository `scripts/test.sh`.

## Acceptance readback

The exact final subject was compared against the accepted M01 base. It is 24 commits ahead and 0 behind, with the M02 change set limited to the typed-contract schemas, implementation, kernel seam activation, tests/fixtures, test gate and Execution documentation.

The final implementation provides:

- deterministic canonical JSON and content-derived `obligation_id`;
- freshness material restricted to the exact subject, selected authority refs, prerequisites, constraints, completion requirements, typed mutation conditions and explicitly supplied determining canonical inputs;
- negative coverage proving unrelated unselected repository noise does not change the fingerprint while a material selected input does;
- exact authority locators requiring repository + 40-hex commit + repo-relative path + 40-hex Git blob, with materialized content re-hashed before bundling;
- bounded authority bundles containing only selected sources;
- closed schema version 1 with fail-closed unsupported-version validation;
- explicit rejection of runtime/provider/model/worker/session/retry/worktree/Paseo/invocation/scheduler telemetry keys in canonical obligation/result payloads and golden fixtures;
- exact result-to-obligation and original-freshness binding validation;
- stale-result classification: unchanged -> `accept`; stale without proof -> `reexecute`; stale with exact old/new fingerprints plus positive safety proof -> explicit `reuse`, `rebase` or `reconcile`;
- typed canonical mutation equality preconditions/postconditions with coordinator-side verification/readback helpers; no canonical writer exists in the transport contract;
- external-effect recovery delegated to the existing exact-target readback oracle so uncertain occurrence fails closed without blind retry;
- kernel compilation restricted to an already registered M01 rule ID, preserving the single mechanical-rule vocabulary.

## Verification

GitHub Actions workflow `test`, run #366 / ID `35937158427`, was read back for exact head `5d0da25d9d08740a56591ba3738c6ab3dc9451ba`:

- workflow status: `completed`;
- workflow conclusion: `success`;
- job `test`: `success`;
- step `Run repository checks`: `success`.

The repository gate includes the dedicated M02 typed-contract suite and the complete existing baseline through `scripts/test.sh`.

Implementation acceptance: GREEN; independent Card review remains required.
