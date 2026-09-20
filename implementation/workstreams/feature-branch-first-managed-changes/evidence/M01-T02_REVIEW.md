# M01-T02 independent review

Date: 2026-09-20
Card: `M01-T02 — Add generic natural-language managed-change entry`
Review subject: `4ec2c68b68c282a10f8c5275799d8bcabec1be95`
Verdict: **GREEN**

## Authority reviewed

- `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md` — M01
- `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` — REQ-BF-001..007, REQ-BF-011, REQ-BF-015..017
- ADR-BF-001 and ADR-BF-003
- `openspec/changes/branch-first-m01-state-entry/`
- dependency M01-T01 independent GREEN evidence
- Card contract `implementation/workstreams/feature-branch-first-managed-changes/cards/M01-T02.md`

## Independent inspection

The exact immutable subject was read directly from repository state. The review did not use the implementing-chat narrative as evidence.

The contracted production delta from the M01-T01 reviewed subject to this subject was inspected for both fixed-policy Router/Intake/Workstreams namespaces, and the resulting files were read back at the exact review subject. Commits after the review subject changed only the Task Board review lifecycle; no reviewed production file drifted before this verdict.

No blocking findings.

Acceptance checks:

1. GREEN — both fixed-policy routers recognize clear natural-language authorization for a new managed repository change and route to Intake before change-specific durable writes.
2. GREEN — read-only inspect/compare/analyze remains branch-free and does not trigger generic Intake.
3. GREEN — generic identity is neutral and identical in both policies: `change-<slug>` + `work/<slug>`.
4. GREEN — exact existing branch/manifest/PR identity is recovered rather than duplicated.
5. GREEN — coherently different durable work uses the smallest available shared numeric suffix for both workstream ID and branch.
6. GREEN — deterministic candidate branches with missing/malformed/identity-inconsistent manifests fail closed to Recovery instead of being claimed, overwritten or silently bypassed by suffixing.
7. GREEN — Intake explicitly makes pre-creation steps read-only, creates the branch first, then persists the first change-specific durable Project Workflow state on that branch.
8. GREEN — `#issue` / `#feature` remain explicit shortcuts, and an explicit marker retains precedence over ordinary implementation language.
9. GREEN — generic Intake does not reclassify the workstream to issue/feature merely to reuse a lifecycle path and does not bypass normal downstream gates.
10. GREEN — equivalent semantics exist in `workflow/chatgpt_only/*` and `workflow/codex_only/*` without cross-policy lifecycle imports.
11. GREEN — OpenSpec task 3 is complete and coherent with the implemented entry/naming/recovery contract.
12. GREEN — scope remains bounded; full downstream pointer migration, root/default cutover and documentation/dogfood closure remain outside M01-T02 as contracted.

## Verification notes

- Exact subject readback: GREEN.
- Focused static/scenario contract inspection: GREEN.
- GitHub reported no status checks or workflow runs for the exact subject; no CI result is claimed.
- No repository test runner is claimed by this review.

## Verdict

**GREEN.** The exact review subject satisfies the M01-T02 Card contract and its applicable authority slice. The Card may proceed to deterministic post-review finalization.
