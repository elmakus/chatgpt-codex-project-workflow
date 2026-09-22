# M04-T03 — target-side terminal recovery and cleanup

Date: 2026-09-22
Card: `M04-T03`
Result: **GREEN**

## Exact target

- repository: `elmakus/project_workflow_v2`
- branch: `feat/pwv2-m04-integration-close`
- predecessor: `1e482c395b04af36a97ce7c33c540653184cb26a`
- result head: `cc54b6d590474ebe32c4ade2b2879897f58c99b0`
- result tree: `da0a47f75b59bbafdb205cf15cd0365c085b51f2`
- PR: `#4`

## Implemented contract

M04-T03 adds source-ref-independent terminal recovery and bounded cleanup semantics:

- target-side recovery requires immutable merge evidence binding the exact original source head and a complete set of unique knowable recovery artifacts;
- missing unique pre-merge recovery material fails closed;
- successful closure does not require the merged source ref to survive and never recreates it for bookkeeping;
- automatic deletion of the merged source branch is accepted as normal cleanup when terminal truth is independently durable;
- surviving-branch cleanup uses optional `safe_to_delete` semantics with exact current-head revalidation;
- moved source HEAD invalidates deletion readiness;
- absence readback is required before recording a safe-to-delete ref as deleted;
- terminal-unmerged recovery preserves history without importing rejected implementation content.

Original branch/base/parent provenance remains historical identity.

## Verification

Exact local checkout verification:

- `git diff --check`: PASS;
- targeted close suite: 19/19 PASS;
- `sh scripts/test.sh`: PASS;
- state suite: 28/28 PASS;
- router suite: 38/38 PASS;
- execution contract: 4/4 PASS;
- review contract: 1/1 PASS;
- recovery contract: 2/2 PASS;
- close contract: 19/19 PASS;
- `python3 -m compileall -q tools tests`: PASS.

GitHub readback confirms exact branch head `cc54b6d590474ebe32c4ade2b2879897f58c99b0` and tree `da0a47f75b59bbafdb205cf15cd0365c085b51f2`. GitHub Actions run `35764621917` completed **success** for that exact head. No real branch deletion was performed; deterministic fixtures cover immediate auto-delete, surviving-head movement, absence readback and terminal-unmerged closure.
