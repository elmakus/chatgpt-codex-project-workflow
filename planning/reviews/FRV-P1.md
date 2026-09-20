# Independent Plan Review — FRV-P1

Plan revision: `FRV-P1`
Review requirement: `RECOMMENDED`
Review state: `red`
Review subject: `planning/FORK_RELEASE_VERSIONING_MASTER_PLAN.md@blob:6f8939a2957caf3a0043d91d919dd50667e73b54`
Review subject commit: `81d91b3a4e07cfbb20361356c2127da1ce37e958`
Review evidence: `RED — exact frozen plan blob 6f8939a2957caf3a0043d91d919dd50667e73b54 is recoverable and otherwise preserves approved FRV R1 / ADR-FRV-001 lineage, provenance, migration, policy-surface coverage and authorization boundaries. The blocking plan-only defect is the OpenSpec boundary: FRV-P1 says no OpenSpec is required by default because the scope changes workflow contracts rather than a runtime API/schema, while current workflow/common/OPENSPEC.md explicitly treats new/changed behavior contracts and migrations/external side-effect semantics as normally justified OpenSpec surfaces. M01 introduces a new canonical release-selection behavior contract and migration/publication semantics across three publication routes. Planning must create a new revision that marks this M01 behavior surface as an OpenSpec candidate/required JIT contract and carries its verification/reconciliation into Execution Prep. Definition remains valid; no Research or user/product authority blocker found.`

## Scope

Independently review the exact immutable FRV-P1 draft against `requirements/FORK_RELEASE_VERSIONING.md` R1, `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md`, the completed intake record, and relevant current publication/routing authority.

Verify in particular that the plan preserves the accepted upstream-anchored `v<upstream>-private.<N>` lineage model, exact upstream repo/tag/SHA provenance, immutable legacy releases, first-migration `private.1`, per-baseline `max(N)+1`, reset on an accepted upstream-baseline change, explicit non-max-SemVer mixed-tag resolution, independence of GitHub prerelease quality state, one policy-neutral semantic source, complete publication-route coverage, deterministic regression coverage, and no silent historical release mutation or upstream-sync policy.

Do not mutate the reviewed Master Plan while judging it.

## Return contract

Persist GREEN/RED evidence in this record, set `Review state`, then return to the ChatGPT-only router. GREEN returns to Planning for deterministic approval of the unchanged reviewed plan and normal continuation into Execution Prep. RED routes through the standard plan-review correction contract.
