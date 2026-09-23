# M07-T08 — final production-candidate freeze and pilot rollback boundary

Date: 2026-09-23
Status: FROZEN FOR INDEPENDENT FINAL-INTEGRATION REVIEW

## Exact PWv2 candidate

- Repository: `elmakus/project_workflow_v2`
- Candidate commit: `15978113e46abc8498ceaef594461c8613fcadb8`
- Candidate tree: `f05d86d72f9bbe941583b4ccf92e2c46b5decf83`
- Candidate branch: `feat/pwv2-m07-qualification`
- PR: `elmakus/project_workflow_v2#7`
- PR state at freeze: open, draft, mergeable/clean
- PR head: exact candidate commit above
- PR base: `main@2d010a95bac89dfd561dcc3accad6c5e8a0bda7a`

No release/tag/package activation is performed before final independent review. Release/package identity is an M07-T09 post-review adoption action.

## Qualification surface

The exact candidate is covered by:
- M07-T01: A01-A17 + PWV2-REQ-001..076 + 97-row/0-OPEN salvage accounting GREEN;
- M07-T02: L03 GREEN;
- M07-T03: L04 GREEN;
- M07-T04: L06 GREEN;
- M07-T05: L07 GREEN;
- M07-T06: L08 GREEN;
- M07-T07: L09 GREEN;
- inherited M05 live evidence: L01, L02 and L05 GREEN.

Thus all mandatory A01-A17 and L01-L09 are GREEN on this candidate/compatible unchanged surfaces. Final independent integration review remains intentionally outstanding and is activated by this freeze.

## Named production pilot and authorization

Authorized pilot:
- `elmakus/orchestration-runtime`

User authorization:
- adopt PWv2 candidate `15978113e46abc8498ceaef594461c8613fcadb8` for this pilot;
- preserve rollback to the present PWv1 state.

This authorization is scoped only to this named pilot. It does not authorize wider rollout.

## Exact pre-activation PWv1 rollback snapshot

Repository: `elmakus/orchestration-runtime`

Refs:
- `main@c4130e63760d08c3656552f4a92c479239acbea3`
- `work/orchestration-prior-art-findings@636a9ec2b7760fc6a24eddb00319bfff9d583165`

Exact V1 state blobs at the workstream head:
- `PROJECT.md` -> `1528c676ab2ccfe3db78b712f0ef45aca149c9ca`
- `implementation/workstreams/change-orchestration-prior-art-findings/WORKSTREAM.yaml` -> `208d543bb389ce7e33d3866489f3ae19ee94c3be`
- `implementation/workstreams/change-orchestration-prior-art-findings/INTAKE.md` -> `ae4768b0f7406e62b1b6115ea66807797783a7cc`
- `brainstorming/ORCHESTRATION_RUNTIME_PRIOR_ART_R1.md` -> `ea3bc14673cc0cc064dd891fdd6ce3a13218342b`
- `research/ORCHESTRATION_RUNTIME_PRIOR_ART_R1.md` -> `208b5d024618e35098d334b37852a1394ec2af7d`

Recovered semantic boundary:
- workstream status: `discovery`;
- Intake: complete;
- exploratory scope points to `brainstorming/ORCHESTRATION_RUNTIME_PRIOR_ART_R1.md`;
- Brainstorming: `ready_for_definition`;
- Definition promotion authorization: `pending`;
- Definition promotion subject: `none`;
- Research: no active manifest research obligation;
- Task Board: `null`;
- accepted requirements: none;
- accepted decisions: none;
- approved plan: none;
- no implementation/review obligation exists.

This is the rollback source of truth until PWv2 destination activation occurs.

## Required migration semantics

The ordinary M06 automatic migration intentionally does not infer pre-Definition promotion state. M07 adoption must therefore explicitly reconstitute, from the immutable V1 evidence above, a V2 workstream that preserves:
- same consumer repository and branch provenance;
- exact exploratory findings as migrated evidence/provenance, not accepted Definition authority;
- `ready_for_definition` with promotion still `pending`;
- no fabricated Definition, Planning, Task Board, review verdict or implementation;
- no implicit user authorization to enter Definition.

A fresh PWv2 recovery after activation must route to the same user-owned Brainstorming -> Definition promotion gate.

## Rollback rule

Until destination activation produces new V2 live state/effects:
- V1 remains the sole live owner;
- an unaccepted migration branch/staging package may be discarded;
- user-owned bootstrap/Project Instructions may be restored to their pre-adoption V1 values.

After destination activation and any subsequent V2 live state/effect, rollback is no longer a blind reset: preserve V2 evidence, read back effects and use bounded forward correction or separately authorized reverse migration.

## Review boundary

This freeze was produced in the implementing/adoption-preparation chat and must not self-review.

The selected workstream final-integration gate is RECOMMENDED and must be reviewed by a fresh normal ChatGPT context before:
- merging/releasing PWv2 candidate;
- recording terminal V1 construction custody transfer;
- mutating the pilot's user-owned bootstrap/Project Instructions;
- activating migrated V2 state.
