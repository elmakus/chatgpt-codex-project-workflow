# M06-T05 — cumulative M06 acceptance and immutable review freeze

Date: 2026-09-23
State: GREEN implementation/acceptance candidate; independent review required before milestone completion.

## Exact integrated target

- Repository: `elmakus/project_workflow_v2`
- Branch: `feat/pwv2-m06-migration`
- Commit: `5b3d195e61645d541821f238f5374cca7e121e58`
- Tree: `82b7a601c3fe21f8f11219b0f5b0cf02e5ee3386`
- Draft PR: #6
- Base: `main@27b9132e173850e7d596092e023b0af7e0507472`
- PR readback: open, draft, mergeable/clean, exact head/base.

## Integrated M06 result

M06 is bounded to migration tooling and disposable rehearsal.

- T01: finite real-derived V1 readers, exact source identity, deterministic mutation-free dry run, unknown/racing/parallel-active inputs fail closed.
- T02: safe semantic conversion into common V2 workstream/Task Board/review/result owners; terminal review proof is reused only when exact and semantically independent; otherwise a durable blocker is created.
- T03: explicitly authorized fixture-only apply with exact source/output fingerprints, staging/readback/promotion, verified repeated no-op, changed-source/destination conflicts, crash restart, unactivated rollback and forward-repair-only activated history.
- T04: disposable rehearsal and boundary documentation, including nested V1 manifest validation, pre-execution/Research/Plan-Review/premium-equivalent fail-closed reconstitution, stacked dependency reconciliation, active/result/review/legacy-root coverage and ordinary-router isolation.
- T05 cumulative correction: exact pending/in-progress migrated review attempts are blocking just like RED until GREEN; regression added.
- T05 cumulative idempotency: repeated semantic conversion of the same exact source/proof returns identical bundle and output fingerprint.

No permanent V1 semantic route, dual-write compatibility layer, runtime/policy/scheduler state or production adoption was added. Real-project migration remains optional and separately authorized; M07 production qualification/adoption/custody transfer remains untouched.

## Acceptance matrix

The exact integrated checks cover the M06-owned migration slice of:
- A02 — no legacy semantic routing dependency;
- A03 — exact workstream/manifest/Task Board/branch binding;
- A05 — completed result is reconciled, not replayed;
- A06 — uncertain external effect readback before retry;
- A07 — exact append-only review attempt semantics, including RED and pending/in-progress blocking;
- A10 — activated destination remains self-verifying after source disappearance;
- A15 — representative finite V1 fixtures convert/apply or fail closed explicitly;
- A17 — accepted V1→V2 disposition remains documented and migration-only code stays outside ordinary routing.

Required fail-closed cases are represented: unknown/nested schema, ambiguous/insufficient review subject proof, racing source, parallel-active Cards, unresolved pre-execution state, unresolved stacked dependency, changed destination and uncertain external effect.

## Exact verification

`sh scripts/test.sh` on this exact target runs:
- all named repository contract/delivery/migration suites;
- full `python3 -m unittest discover -s tests -p 'test_*.py'`;
- `python3 -m compileall -q tools tests`;
- `git diff --check`;
- clean-tree verification after bytecode cleanup.

Exact-head GitHub Actions:
- pull_request run `35848155642`, job `107139204326`: completed / success;
- push run `35848149974`, job `107139185943`: completed / success.

The accepted migration boundary documentation is `docs/V1_MIGRATION_REHEARSAL.md`.

## Review freeze inputs

Review target:
- exact target commit/tree above;
- M06-T05 Task Card blob;
- this cumulative acceptance evidence blob.

A fresh independent reviewer must verify the frozen exact subject before M06 may become terminal GREEN.
