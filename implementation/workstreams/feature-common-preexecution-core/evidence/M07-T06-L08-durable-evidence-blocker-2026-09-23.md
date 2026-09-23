# M07-T06 — L08 durable-evidence correction blocker

Date: 2026-09-23
Status: BLOCKED

Origin: independent workstream final-integration review R01 RED:
`implementation/workstreams/feature-common-preexecution-core/evidence/M07-final-integration-independent-review-R01-2026-09-23.md`.

## Exact affected authority

- Card: `implementation/workstreams/feature-common-preexecution-core/cards/M07-T06.md`
- PWv2 candidate: `elmakus/project_workflow_v2@15978113e46abc8498ceaef594461c8613fcadb8`
- Disposable consumer: `elmakus/test-pwv2`
- Durable consumer branch to recover: `feat/m07-l08-topology-n`

## Blocker

The prior M07-T06 report names a qualifying local RED -> delegated correction -> GREEN -> finalization sequence, but the exact final Git objects are no longer present on the durable GitHub branch or in the surviving local fixture. The durable GitHub branch remains at S1 BAD / R01 pending.

A bounded correction requires an actual capable top-level runtime with genuine delegated model contexts. The current ChatGPT execution surface can inspect the workstation and exact Codex installation, but attempts to start a nested `codex exec` model run are blocked by the current runtime/tool safety boundary before the process starts. No synthetic/direct substitute is legal under M07-T06.

## Smallest required recovery

Re-execute M07-T06 from the durable consumer branch using the exact frozen PWv2 candidate and a genuinely capable Codex runtime. Preserve the resulting exact Git history/state durably on the consumer branch (or another immutable repository ref explicitly reconciled into the Card evidence) so a fresh independent final-integration reviewer can read back:
- S1 immutable RED history;
- bounded delegated S2 correction to exactly `topology-n: GOOD\n`;
- independent GREEN on exact S2;
- same-top-level-invocation Card finalization;
- final Task Board/result/review records.

After that, reconcile M07-T06 evidence, produce a new M07-T08 freeze blob / manifest review subject, and request a fresh independent workstream final-integration review. R01 RED remains immutable history.
