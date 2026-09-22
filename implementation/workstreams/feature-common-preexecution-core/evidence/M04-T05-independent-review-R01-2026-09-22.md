# M04-T05 — independent review R01

Date: 2026-09-22
Card: `M04-T05`
Verdict: **RED**
Review owner: selected workstream Task Board
Review subject: `elmakus/project_workflow_v2@commit:f40250fa2fe88477df3f03c26adfeb2d8024581b|tree:90d5ebb7480dbc2eeab633a518bce221f09c7a45|M04-T05-card-blob:61ae9578d0df1eb7dbb4f0030d638fa846e2f6aa|acceptance-evidence-blob:759e02b5da46478672a1e45dd6121278ced61aa6`

## Independence

This review was performed from the frozen durable subject by a fresh reviewer context that did not materially produce or repair the reviewed target subject. Runtime/model/session identity is intentionally not canonical independence evidence.

## Authority and evidence reviewed

- `PWV2-P1` M04 contract, including P1-P4 and A06/A08/A09/A10/A16 acceptance.
- `requirements/PROJECT_WORKFLOW_V2.md` R1 M04-owned/supporting requirements.
- ADR-PWV2-003 and ADR-PWV2-005.
- Trigger-only fork-lineage authority: `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` and `requirements/FORK_RELEASE_VERSIONING.md` R1.
- Accepted M04-T01..T04 contracts/evidence and M04-T05 cumulative acceptance evidence.
- Exact target `elmakus/project_workflow_v2@f40250fa2fe88477df3f03c26adfeb2d8024581b`, tree `90d5ebb7480dbc2eeab633a518bce221f09c7a45`, including production Close/router/fork-lineage/state helpers and deterministic tests.
- PR #4 exact head/base and exact-head GitHub Actions push run `35768949267` plus PR run `35768955381`, both completed successfully.

## Blocking finding

### Fork-lineage helper does not validate the required exact upstream commit SHA

Accepted M04.P4 and M04-T04 require a durably declared downstream-fork release to carry the accepted upstream repository/tag/**SHA**. ADR-FRV-001 states that every canonical downstream release records the exact upstream repository, tag/version and upstream commit SHA. FRV-REQ-005 and its acceptance criterion likewise require exact upstream repo/tag/SHA provenance.

On the frozen subject, `tools/fork_release_contract.py::UpstreamLineage.__post_init__` rejects an empty repository/commit and validates the tag, but accepts any non-empty commit string. For example, a lineage with `commit="not-a-sha"` passes construction and can activate `module_for_operation("downstream_fork_release", ...)`. The deterministic fork tests use a 40-hex value but contain no negative malformed-SHA fixture.

This violates the exact-lineage/fail-closed boundary: malformed upstream commit provenance can be accepted as the durable trigger for the optional publication lineage module.

Required bounded correction:
- validate the upstream commit as an exact Git commit SHA identity used by this contract (40 hexadecimal characters, consistently with the repository's existing exact-SHA contracts);
- add a negative deterministic test proving malformed/non-SHA commit identity is rejected before the fork-release module can activate;
- rerun cumulative M04 verification and freeze a new immutable M04-T05 subject/evidence. Preserve this R01 as immutable RED history.

## Other reviewed M04 findings

No additional blocking defect was found in the reviewed M04 surface. The frozen subject otherwise preserves moving-target semantic refresh/re-review rules, target-race reread, external-effect readback-before-retry, final tracker closure boundaries, target-side/source-ref-independent recovery, exact-head cleanup, terminal-unmerged history separation, ordinary-Close negative fork-module loading, numeric private lanes/order, historical immutability, latest-alias identity, and true end-of-scope semantics without implicit deployment/release authorization.

## Verification/readback

- exact target branch HEAD: `f40250fa2fe88477df3f03c26adfeb2d8024581b`;
- exact target tree: `90d5ebb7480dbc2eeab633a518bce221f09c7a45`;
- PR #4: open draft, base `main@29f5e1880d66949c3009afa399490a6a81bc949a`, exact frozen head, mergeable/clean at review readback;
- compare: 9 commits ahead / 0 behind, 16 changed files;
- Actions push `35768949267`: exact head/tree, completed success;
- Actions PR `35768955381`: exact head, completed success; repository-check job GREEN;
- cumulative acceptance evidence records 102/102 full unittest discovery plus compileall/diff/check/clean-tree as GREEN.

The GREEN automated runs do not close the malformed-SHA gap because the current tests never exercise it.

## Verdict

**RED.** The exact frozen R01 subject does not fully satisfy the accepted M04 fork-lineage provenance contract. The defect is bounded implementation/test work inside already accepted authority; no requirements or planning change is required.
