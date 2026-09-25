# Sequential Bug Harvest Handoff


## Latest technical triage

- Batch completed: `H003 + H004`
- Batch candidate snapshot: `elmakus/project_workflow_v2@31764d82911de523e36d2de5c5d98ce7c3cedb18`
- Original PWv2 subject for both candidates: `elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`
- H003 verdict: `CONFIRMED_MATERIAL`
- H003 evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H003.md`
- H003 current-candidate status: `persists`
- H003 checkpoint commit: `806b429e05faab7943101769c63475a3fa25b65d`
- H004 verdict: `CONFIRMED_MATERIAL`
- H004 evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H004.md`
- H004 current-candidate status: `persists`
- Next READY item: `H005`
- Next worker obligation: begin from `H005` and process only the next explicitly authorized batch. Do not infer authorization for later candidates from this handoff.

## What was completed

The first-stage out-of-band workspace was initialized from the exact active-workstream HEAD captured before branch creation. Both persisted aggregate reports were normalized without performing a broad new product audit, without repairing product code, and without mutating canonical Project Workflow state.

All 27 PWv2 aggregate classes and all 4 M02R-T03 shadow aggregate classes were ingested. One clear semantic family was merged as **CROSS-SOURCE OVERLAP**: PWV2:C003 with M02R-T03:C02 (durable evidence locators accepted without proving the referenced artifact exists). This leaves 30 normalized harvest candidates. H001 through H004 have now been independently triaged and persisted; H003 and H004 are both `confirmed_material` / `reproduced` / `pending_repair`. H005+ remain untouched by this batch.

## Exact durable workspace state

- Repository: `elmakus/chatgpt-codex-project-workflow`
- Workspace branch: `audit/pwv21-pre-m03-bug-harvest`
- Exact branch base: `598ac506012aa22c9b126ecf23dc01fa23598d64`
- Write boundary: `audits/pwv21-pre-m03-bug-harvest/` only
- Active product workstream branch remains read-only: `work/pwv21-policy-kernel-brainstorming`
- Canonical workflow state mutation: forbidden
- Product repair in this workspace: forbidden
- Stage: `source_normalization`
- Stage complete: `false`
- The branch HEAD containing this file is the durable triage snapshot for the next sequential worker.

## Sources ingested

1. Canonical PWv2 swarm aggregate:
   - `elmakus/project_workflow_v2`
   - aggregate branch `audit/pwv2-swarm-aggregate-1m60eainl90lrd0cfqufekjn`
   - exact audited subject `4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`
   - 34 completed valid independent audits, 164 original material findings, 27 candidate classes.

2. M02R-T03 shadow aggregate:
   - `elmakus/chatgpt-codex-project-workflow`
   - aggregate branch `audit/m02r-t03-shadow-aggregate-q9m2x7v4k8p1c6n3r5t0w2za`
   - exact consumer commit `5b76ffe03259ff141afc6bfb5b7b546041a48b41`
   - exact result blob `b357ba85d4975540f3ae87b05e73e3fcf8e0471a`
   - exact PWv2.1 implementation `elmakus/project_workflow_v2@180cc0af3a9b56c8c2808827bf5548b8ae040608`
   - 4 independent shadow reviews, 12 original material findings, 4 candidate classes.

These immutable subjects are different and must not be conflated.

## Candidate count

- PWv2 source classes ingested: 27
- M02R-T03 shadow classes ingested: 4
- Cross-source merged semantic families: 1
- Normalized harvest candidates: 30
- READY reproduction items: 26
- Completed reproduction items: 4
- First READY item: `H005`

## Next worker obligation

The next READY item is **H005**. A later worker must read this handoff and queue first, verify H005 is still the first READY item, and then process only the candidate set explicitly authorized in that later worker's batch instruction. It must not treat this handoff as authorization to advance H006 or later.

The `31764d82911de523e36d2de5c5d98ce7c3cedb18` candidate SHA was frozen for the completed H003+H004 batch only; a later batch must resolve its own candidate snapshot according to its authorization instead of silently reusing this one.

## Prohibited next-worker actions

- no canonical workflow mutation;
- no candidate product repair;
- no rewriting source audit reports;
- no skipping a candidate because it was found by only one reviewer;
- no mass verdicting without reproduction;
- no writes outside `audits/pwv21-pre-m03-bug-harvest/`;
- no writes to `work/pwv21-policy-kernel-brainstorming`.
