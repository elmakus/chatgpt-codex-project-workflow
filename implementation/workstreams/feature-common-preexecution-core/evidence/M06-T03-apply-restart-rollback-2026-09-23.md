# M06-T03 — idempotent apply, readback, restart and rollback

Date: 2026-09-23
Result: GREEN

## Exact target

- Repository: `elmakus/project_workflow_v2`
- Branch: `feat/pwv2-m06-migration`
- Commit: `0f96b202ff7906cecc3d3a15f8090c6f27933681`
- Tree: `unknown`
- Draft PR: #6
- Base: `main@27b9132e173850e7d596092e023b0af7e0507472`

## Implemented apply/recovery boundary

The fixture-only migration apply now:
- requires an exact explicit authorization token bound to the converted source fingerprint;
- revalidates the conversion output fingerprint and common-V2 state before mutation;
- re-reads the current V1 fixture commit/content fingerprints before staging, so a racing/changed source fails closed;
- materializes canonical V2 output in a deterministic sibling staging directory with a migration record containing exact source/output fingerprints plus per-file hashes;
- validates staged TOML/readback before atomic promotion;
- treats an already activated destination with the same exact record/content as a verified no-op;
- rejects any destination content/fingerprint divergence instead of overwriting it;
- recovers deterministically from crashes before record creation, after record creation and after promotion;
- permits rollback only for unactivated exact staging; activated output is forward-repair-only;
- exposes destination readback that remains independent of the V1 source after activation;
- requires readback of uncertain external effects before any retry and blocks when occurrence cannot be established.

No production adoption, deployment, source mutation, history rewrite, dual-write path or ordinary V2 runtime dependency on V1 readers was added.

## Deterministic verification

Added `tests/test_migration_apply.py` covering:
- missing/wrong authorization;
- first apply + destination readback + repeated verified no-op;
- changed-source and changed-destination failure;
- crash/restart before record, after record and after promotion;
- rollback of unactivated staging and refusal to roll back activated output;
- external-effect expected/no-effect/unknown readback decisions;
- activated-destination recovery without V1 source access.

The suite is included in `sh scripts/test.sh`.

GitHub Actions on exact head:
- pull_request run `35847087543`, job `107135729086`: completed / success;
- push run `35847081707`: completed / success.

## Acceptance

M06-T03 is GREEN for the owned A06/A10/A15 apply/restart/readback slice. Rehearsal breadth, boundary documentation and cumulative migration coverage remain M06-T04/T05.
