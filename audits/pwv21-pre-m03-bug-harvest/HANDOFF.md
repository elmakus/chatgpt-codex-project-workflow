# Sequential Bug Harvest Handoff

## Latest technical triage

- Items completed in current batch: `H026 + H027`
- Frozen five-item batch candidate snapshot: `elmakus/project_workflow_v2@aa729e9a3b06af6e90a6884f8613629d6cd519f0`
- H026: `CONFIRMED_MATERIAL` / `persists`
- H027: `CONFIRMED_MATERIAL` / `persists`
- Evidence: `evidence/H026.md`, `evidence/H027.md`
- Next READY item: `H028`
- This batch is authorized only through H030 and remains sequential.

## Exact durable workspace state

- Repository: `elmakus/chatgpt-codex-project-workflow`
- Workspace branch: `audit/pwv21-pre-m03-bug-harvest`
- Exact branch base: `598ac506012aa22c9b126ecf23dc01fa23598d64`
- Write boundary: `audits/pwv21-pre-m03-bug-harvest/` only
- Active product workstream remains read-only: `work/pwv21-policy-kernel-brainstorming`
- Canonical workflow state mutation: forbidden
- Product repair: forbidden
- Technical triage progress: H001 through H027 terminal; H028 through H030 READY
- Completed reproduction items: 27
- READY reproduction items: 3

## Frozen candidate for this batch

H026 through H030 use `elmakus/project_workflow_v2@aa729e9a3b06af6e90a6884f8613629d6cd519f0`. Do not advance this candidate within the batch.

## Source subjects

- Canonical PWv2 aggregate exact audited subject: `4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`
- M02R-T03 shadow consumer subject: `5b76ffe03259ff141afc6bfb5b7b546041a48b41`
- M02R-T03 exact implementation subject: `180cc0af3a9b56c8c2808827bf5548b8ae040608`

These immutable subjects must not be conflated.

## Next worker obligation

Process H028 only next. H029/H030 remain untouched until their predecessor item is durably committed.

## Prohibited actions

No canonical workflow mutation, product repair, writes outside the audit workspace, active-workstream edits, PR creation, merge, or review broadening beyond H026-H030.
