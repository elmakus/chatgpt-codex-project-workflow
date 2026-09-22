# M04-T02 — external effects and final tracker lifecycle

Date: 2026-09-22
Card: `M04-T02`
Result: **GREEN**

## Exact target

- repository: `elmakus/project_workflow_v2`
- branch: `feat/pwv2-m04-integration-close`
- predecessor: `51f3d820d18c9e99a738bda5b281b578e03afe9b`
- result head: `1e482c395b04af36a97ce7c33c540653184cb26a`
- result tree: `40ec062eedfcfb37b3064a8531d10141f5c52a99`
- PR: `#4`, open/draft, exact head/base at readback

## Implemented contract

M04-T02 adds the common external-effect and final GitHub tracker lifecycle:

- external-effect state now separates readback status from the concrete observed effect;
- pending effects require exact-object readback before any retry decision;
- unresolved/uncertain occurrence fails closed without replay;
- verified no-effect permits retry, verified expected-effect reconciles without replay, and unexpected-effect routes reconciliation;
- tracker linkage is reference-only for intermediate or non-default integrations;
- closing linkage is selected only for the accepted scope-completing default-branch PR;
- post-completion Issue readback distinguishes verified closure, unexpected early closure, missing expected automatic closure and accepted-completion-only explicit fallback close;
- Issue/tracker state remains bookkeeping and never grants workflow authorization.

No real Issue mutation was performed by deterministic tests.

## Verification

Exact local checkout verification on result content:

- `git diff --check`: PASS;
- targeted state + close suites: 41/41 PASS;
- `sh scripts/test.sh`: PASS;
- state suite: 28/28 PASS;
- router suite: 38/38 PASS;
- execution contract: 4/4 PASS;
- review contract: 1/1 PASS;
- recovery contract: 2/2 PASS;
- close contract: 13/13 PASS;
- `python3 -m compileall -q tools tests`: PASS;
- clean local working tree after commit/push: PASS.

GitHub readback confirms branch head `1e482c395b04af36a97ce7c33c540653184cb26a` with tree `40ec062eedfcfb37b3064a8531d10141f5c52a99`, PR #4 head at the same commit and base `main`. GitHub Actions run `35763906839` completed **success** for the exact result head.

Predecessor-to-result comparison is exactly one commit ahead / zero behind with eight M04-T02 files changed. M04-T03 terminal recovery/cleanup and M04-T04 fork/end-of-scope semantics remain deferred.
