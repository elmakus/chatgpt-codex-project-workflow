# M01 — final integration refresh and acceptance evidence

Date: 2026-09-20
Workstream: `issue-fork-release-versioning`
Integration target: `main`

## Refreshed exact state

- Original implementation/review baseline: `main@f3cdb60367da3e978397409b51c37faa181d613f`.
- Current integration target after concurrent workstream integration and its target-side closure: `main@a52fae6c38944f69c4ec38dc6e77457935146f26`.
- Target movement was reconciled by a normal merge into the workstream; exact reconciliation commit on the workstream branch: `8fad2acd3a31ccb53012e2f67f3fd8b8df706343`.
- Reconciled Git tree: `d8dc7a0ee6f83d98beb63c3551f38b794833b762`; it exactly matched the independently constructed/tested local merge tree.
- The reconciliation had no textual conflicts. The overlapping files were `README.md`, `workflow/chatgpt_only/CLOSE.md`, and `workflow/codex_only/CLOSE.md`; current-main branch-first semantics remain intact and the FRV additions remain the same bounded additions reviewed for M01-T01.
- After reconciliation, GitHub compare reports the workstream `behind_by: 0`; the diff from current `main` contains only the 23 FRV-owned files/surfaces.
- Independently reviewed immutable workstream content/behavior subject remains `cec373fbfe38ffb1602a17f87f222e244e1f1657`.
- Full repository discovery on the reconciled tree: **62/62 passed**.
- The target movement and merge changed ancestry/compatibility context only; they did not change FRV-owned behavior, accepted authority, OpenSpec, tests, or the M01 acceptance surface.

## Integrated milestone acceptance

**GREEN** for M01 — Canonical fork-release contract and publication enforcement.

M01 contains one implementation Card, `M01-T01`, which owns FRV-REQ-001..012 and the full milestone outcome. The Card is terminal with independent review GREEN for the exact immutable subject above.

Acceptance was checked against:
- `requirements/FORK_RELEASE_VERSIONING.md` R1 / FRV-REQ-001..012;
- `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` / ADR-FRV-001;
- `planning/FORK_RELEASE_VERSIONING_MASTER_PLAN.md` / FRV-P2 / M01;
- the M01-T01 Card acceptance and required checks;
- the JIT OpenSpec under `openspec/changes/fork-release-versioning/`;
- implementation and independent review evidence;
- compatibility against current `main@a52fae6c38944f69c4ec38dc6e77457935146f26`.

The accepted result has one common policy-neutral fork-release contract, all three supported publication surfaces defer to it without duplicating the lineage algorithm, canonical `v<upstream>-private.N` semantics and migration/provenance rules are covered, historical release mutation/upstream-sync are excluded, and the repository-local auto-patch workflow remains outside this Card.

No unresolved Card, Research obligation, blocker, stacked dependency, strategic decision, deployment/live-write authorization gate, target compatibility defect, or behavioral acceptance defect remains.

## Distinct workstream final-integration review coverage

The manifest final-integration gate is RECOMMENDED and distinct from the Card review lifecycle.

Coverage reuse remains valid after target refresh because:
1. this workstream has one implementation Card only;
2. M01-T01 owns the complete M01/workstream behavior and requirement surface;
3. its independent review checked the full authority slice, OpenSpec coherence, all three publication integrations, migration/provenance/non-goal boundaries, and regression coverage;
4. the immutable workstream-owned content/behavior subject remains exactly `cec373fbfe38ffb1602a17f87f222e244e1f1657`;
5. target reconciliation changed ancestry/context only; the reconciled FRV diff is behaviorally identical to the reviewed subject;
6. compatibility against the moved target is GREEN with no textual conflict and **62/62** full-suite verification.

Therefore the distinct manifest gate remains GREEN with `covered_by` pointing to the exact independent M01-T01 review evidence. This is coverage reuse, not a second review verdict.

## Pre-merge condition

Immediately before merge, re-read `main`, PR #40 and the exact PR head. If the target or covered workstream behavior changes again, rerun the integration refresh and invalidate coverage only when the covered behavior/acceptance surface materially changes.
