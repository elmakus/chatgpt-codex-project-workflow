# M04-T01 — integration refresh and review-coverage preservation

Date: 2026-09-22
Card: M04-T01
Result: GREEN

## Exact target

- repository: elmakus/project_workflow_v2
- branch: feat/pwv2-m04-integration-close
- base: main@29f5e1880d66949c3009afa399490a6a81bc949a
- result head: 51f3d820d18c9e99a738bda5b281b578e03afe9b
- result tree: ab631650397b5782ca883ccadc6e919c15770282
- PR: #4, open/draft, exact base/head, mergeable at readback

## Implemented contract

M04-T01 adds the common Close/integration-refresh slice:

- tools/close_contract.py defines immutable refresh snapshots, review-coverage reuse/new-subject classification, reread-before-mutation target race protection and stacked integration path selection;
- workflow/CLOSE.md states the corresponding common semantic contract;
- tests/test_close_contract.py covers A08/A09 foundations, stronger-coverage reuse, target race and both stacked dependency paths;
- scripts/test.sh includes the production close-contract test suite.

The contract treats target SHA/ancestry-only movement as insufficient reason to invalidate GREEN when covered content/behavior/acceptance is unchanged and affected compatibility is GREEN. Material covered-content/behavior/acceptance change requires a new exact review subject. A clean textual merge alone is explicitly insufficient.

## Verification

Exact local checkout verification on result content:

- git diff --check: PASS;
- sh scripts/test.sh: PASS;
- state suite: 27/27 PASS;
- router suite: 38/38 PASS;
- execution contract: 4/4 PASS;
- review contract: 1/1 PASS;
- recovery contract: 2/2 PASS;
- close contract: 8/8 PASS;
- python3 -m compileall -q tools tests: PASS.

GitHub Actions run 35759502841 for exact head 51f3d820d18c9e99a738bda5b281b578e03afe9b completed success. Its test job and repository-check step are GREEN.

Base-to-head comparison is 4 commits ahead / 0 behind and changes only:
- scripts/test.sh
- tests/test_close_contract.py
- tools/close_contract.py
- workflow/CLOSE.md

No external write/tracker-close implementation, terminal package/branch cleanup, fork release implementation, M05 delivery behavior, production adoption or custody transfer is claimed by T01.
