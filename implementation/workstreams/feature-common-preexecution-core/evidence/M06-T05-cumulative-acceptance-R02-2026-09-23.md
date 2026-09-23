# M06-T05 — cumulative M06 acceptance R02 after independent-review correction

Date: 2026-09-23
State: GREEN implementation/acceptance candidate; fresh independent review required before milestone completion.

## Prior independent review

R01 is durably RED at:
`implementation/workstreams/feature-common-preexecution-core/evidence/M06-T05-independent-review-R01-2026-09-23.md`.

R01 identified three bounded M06 defects on the former exact subject `5b3d195e61645d541821f238f5374cca7e121e58`:
1. GREEN dry-run source hashes were not re-bound to conversion input.
2. an activated V1 workstream final-integration review, including GREEN, could be omitted by conversion.
3. apply/readback could verify an activated destination while workstream-local Card/result/terminal-review-evidence locators were not materialized.

All corrections below remain inside the accepted M06 technical/plan authority. No Definition, strategy, production-adoption or custody-transfer authority changed.

## Exact corrected target

- Repository: `elmakus/project_workflow_v2`
- Branch: `feat/pwv2-m06-migration`
- Commit: `e38d92f87ff1f93fae79d9763e1127295dc3ed92`
- Tree: `05819376a634372259061d5e14e4529778d3f466`
- Draft PR: #6
- Base: `main@27b9132e173850e7d596092e023b0af7e0507472`
- PR readback: open, draft, mergeable, exact head/base.

The corrected subject is six commits ahead of the R01 subject and changes only:
`tools/v1_migration.py`, `tools/migration_apply.py`,
`tests/test_v1_migration.py`, `tests/test_migration_apply.py`,
`tests/test_migration_rehearsal.py`, and `docs/V1_MIGRATION_REHEARSAL.md`.

## R01 correction readback

### Exact dry-run -> conversion binding

`convert_dry_run()` now recomputes the exact dry-run source fingerprint and board/manifest SHA-256 identities before parsing/converting. A plan created from source A cannot convert different source B. DONE V1 Cards also fail closed unless their exact result commit and result evidence are present.

A regression explicitly creates a GREEN dry-run for one board and then changes its execution state before conversion; conversion rejects the mismatch.

### Activated workstream review preservation

Any activated manifest-owned V1 workstream review state — `pending`, `in_progress`, `red` or `green` — is now surfaced as an outstanding `workstream_review:<state>` obligation and blocks automatic conversion with `workstream_review_reconciliation_required`.

This deliberately treats the supported real-derived Codex class as recognized but not automatically convertible while its V1 final-integration review cannot be exactly reconstituted into a common V2 owner. Pending/RED/GREEN regression coverage proves the verdict is not silently discarded or treated as authorization.

### Durable local artifact materialization/readback

Fixture apply now requires an exact source-artifact resolver called with immutable `repository + commit + path` for planned Task Card/review-evidence copies. It materializes those workstream-local artifacts before promotion and creates a deterministic normalized local result record for DONE Cards.

Activation readback now requires the Task Board, every Card contract, every result/blocker, every review-attempt file and every terminal review evidence path to exist and be covered by the migration record. Missing exact source artifact access fails closed before destination activation. The source-disappearance readback remains independent after successful activation because the complete referenced package is local.

## Exact verification

On exact corrected head `e38d92f87ff1f93fae79d9763e1127295dc3ed92`:

- pull_request Actions run `35851500415`: completed / success;
- push Actions run `35851494382`: completed / success;
- pull_request job `107150009328`: completed / success;
- repository combined migration/close/delivery group: 80/80 GREEN;
- full unittest discovery: 154/154 GREEN;
- state-contract: 28/28 GREEN;
- router: 39/39 GREEN;
- execution-contract: 4/4 GREEN;
- recovery: 2/2 GREEN;
- package/bootstrap probes: PASS;
- `compileall`, `git diff --check` and clean-tree verification remain inside successful `sh scripts/test.sh`.

The existing A17 coverage authority remains `brainstorming/V1_TO_V2_COVERAGE_MATRIX.md` blob `aafd4a916ae11f8a3ff0c6edb799d8ced996a4bf`, with the previously verified 97 classified rows and no OPEN/unclassified disposition.

## Acceptance assessment

The corrected candidate satisfies the M06-T05 implementation-side acceptance package for A02/A03/A05/A06/A07/A10/A15/A17 and the M06 technical contract, including the R01 fail-closed gaps.

No real project was migrated. No permanent V1 semantic route, dual-write layer, runtime/policy/scheduler state or production adoption was added. M07 production qualification/adoption/custody transfer remains untouched.

Because this same context materially produced the R01 corrections, it is not independent of this corrected subject. M06-T05 remains non-terminal and must stop at a fresh independent review boundary after the exact subject is frozen.
