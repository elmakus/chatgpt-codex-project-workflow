# Sequential Bug Harvest Handoff


## Latest technical triage

- Batch in progress: `H022 + H023 + H024 + H025`
- Frozen batch candidate snapshot: `elmakus/project_workflow_v2@aa729e9a3b06af6e90a6884f8613629d6cd519f0`
- H022 verdict: `CONFIRMED_MATERIAL`
- H022 current-candidate status: `persists`
- H022 evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H022.md`
- H023 verdict: `CONFIRMED_MATERIAL`
- H023 current-candidate status: `persists`
- H023 evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H023.md`
- Next READY item: `H024`
- Current authorization continues sequentially with H024, then H025 only. Do not process H026 or later.

## What was completed

The first-stage out-of-band workspace was initialized from the exact active-workstream HEAD captured before branch creation. Both persisted aggregate reports were normalized without performing a broad new product audit, without repairing product code, and without mutating canonical Project Workflow state.

All 27 PWv2 aggregate classes and all 4 M02R-T03 shadow aggregate classes were ingested. One clear semantic family was merged as **CROSS-SOURCE OVERLAP**: PWV2:C003 with M02R-T03:C02 (durable evidence locators accepted without proving the referenced artifact exists). This leaves 30 normalized harvest candidates. H001 through H023 have now been independently triaged and persisted. H022 and H023 are each `confirmed_material` / `reproduced` / `pending_repair`. H024 and H025 remain authorized and READY; H026+ remain untouched by this batch.

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
- READY reproduction items: 7
- Completed reproduction items: 23
- First READY item: `H024`

## Next worker obligation

The next READY item is **H024**. Continue this authorized batch sequentially with H024, then H025. Do not process H026 or anything later.

The `aa729e9a3b06af6e90a6884f8613629d6cd519f0` candidate SHA is the immutable snapshot for the entire H022+H023+H024+H025 batch.

## Prohibited next-worker actions

- no canonical workflow mutation;
- no candidate product repair;
- no rewriting source audit reports;
- no skipping a candidate because it was found by only one reviewer;
- no mass verdicting without reproduction;
- no writes outside `audits/pwv21-pre-m03-bug-harvest/`;
- no writes to `work/pwv21-policy-kernel-brainstorming`.
