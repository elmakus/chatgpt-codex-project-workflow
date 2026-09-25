# Sequential Bug Harvest Handoff


## Latest technical triage

- Candidate: `H002`
- Verdict: `CONFIRMED_MATERIAL`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H002.md`
- Original subject tested: `elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`
- Current candidate snapshot tested: `elmakus/project_workflow_v2@8a24fb66c447e7a5dc22d2f398d13ddb54ebf481`
- Current candidate status: `persists`
- Next READY item: `H003`
- Next worker obligation: reproduce or reject **H003 only** against its exact audited subject, perform its required current-candidate check, and persist only H003 harvest evidence/state. Do not advance any later queue item.

## What was completed

The first-stage out-of-band workspace was initialized from the exact active-workstream HEAD captured before branch creation. Both persisted aggregate reports were normalized without performing a broad new product audit, without repairing product code, and without mutating canonical Project Workflow state.

All 27 PWv2 aggregate classes and all 4 M02R-T03 shadow aggregate classes were ingested. One clear semantic family was merged as **CROSS-SOURCE OVERLAP**: PWV2:C003 with M02R-T03:C02 (durable evidence locators accepted without proving the referenced artifact exists). This leaves 30 normalized harvest candidates. H001 and H002 have now been independently triaged as `confirmed_material` / `reproduced` / `pending_repair`; H003+ remain untouched.

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
- READY reproduction items: 28
- Completed reproduction items: 2
- First READY item: `H003`

## Next worker obligation

The next worker must reproduce or reject **H003 only**. It must read this handoff and queue first, verify H003 is still the first READY item, work against H003's exact audited subject, perform the required current-candidate check, persist only H003 harvest evidence/state, and make no product repair or canonical workflow mutation.

## Prohibited next-worker actions

- no canonical workflow mutation;
- no candidate product repair;
- no rewriting source audit reports;
- no skipping a candidate because it was found by only one reviewer;
- no mass verdicting without reproduction;
- no writes outside `audits/pwv21-pre-m03-bug-harvest/`;
- no writes to `work/pwv21-policy-kernel-brainstorming`.
