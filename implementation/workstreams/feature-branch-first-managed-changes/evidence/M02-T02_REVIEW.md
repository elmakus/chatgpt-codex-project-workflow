# M02-T02 independent review

Date: 2026-09-20
Card: `M02-T02 — Migrate ChatGPT-only execution state and historical-default recovery`
Review subject: `775792e49d6b6a9e37cc60bdb14445269df9583a`
Verdict: **RED**

## Authority reviewed

- `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md` — M02
- `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` — REQ-BF-002..009, REQ-BF-011..014, REQ-BF-016..017 and ChatGPT-only REQ-BF-015
- ADR-BF-001, ADR-BF-002, ADR-BF-003
- `openspec/changes/branch-first-m02-chatgpt-lifecycle/`
- M01 GREEN checkpoint and M02-T01 GREEN dependency
- Card contract `implementation/workstreams/feature-branch-first-managed-changes/cards/M02-T02.md`
- Implementation evidence `implementation/workstreams/feature-branch-first-managed-changes/evidence/M02-T02.md`
- Exact reviewed source at the immutable subject

## Independent inspection

The subject correctly removes root/default state as a normal active ChatGPT-only execution context, preserves manifest ↔ Task Board binding, keeps Card/milestone review and implementation Research Task-Board-owned, retains target-refresh/terminal recovery semantics, preserves historical artifacts, and keeps ChatGPT-only lifecycle separation.

One blocking finding remains.

### F1 — historical migration does not define the exact creation base/integration topology

`workflow/chatgpt_only/RECOVERY.md#Historical root/default migration before mutation` requires Recovery to establish a neutral workstream identity and then “ensure the exact workstream branch exists” before materializing `WORKSTREAM.yaml`, but for the path where no existing branch/manifest/PR already represents the obligation it does not define:

- the exact `integration_target`;
- the exact branch creation base / manifest `base_ref`;
- whether the migrated obligation is independent or stacked, including required parent metadata when applicable.

Those values are mandatory workstream topology/provenance under `WORKSTREAMS.md`, while `INTAKE.md#Base and dependency classification` contains the normal deterministic rules for choosing them. The migration text references only Intake naming/collision rules, not base/dependency classification, and step 3 creates the branch without an exact base-selection rule.

Impact: a historical live root/default obligation with no already-existing workstream can be migrated from an incidental current ref or with inconsistent/null topology fields. That is not deterministic/fail-closed and can weaken stacked-workstream/target-refresh safety. This conflicts with M02 acceptance (“historical/default board … further mutation only after safe workstream migration”), Card acceptance 3 and 6, REQ-BF-007/012/017, and the OpenSpec migration invariant.

Required correction is bounded inside accepted authority: Recovery must recover/prove the intended integration target plus exact creation/adoption base and independent-vs-stacked dependency classification from durable root/Git/PR evidence before branch creation. If that mapping cannot be proven, fail closed. When no parent-only dependency exists and the historical obligation is target-based, use the repository’s normal integration target as the independent target/base under the same policy-local classification rules; when an existing non-target branch is adopted, preserve that exact branch/base provenance. Persist `base_ref`, `integration_target`, and parent fields consistently in the new manifest and add focused regression coverage.

## Verdict

**RED.** The exact review subject does not yet satisfy deterministic historical-default migration. The finding is a bounded L1/L2 correction inside the accepted M02/Card authority; no user/product decision is required.


---

## Re-review attempt 2

Date: 2026-09-20
Review subject: `24efef664be6db1889fbf868487192a064e9e61b`
Verdict: **RED**

The prior topology finding is corrected: exact target/base/dependency classification now precedes branch creation/adoption, ambiguity fails closed, topology is persisted, and branch readback validates it. The remaining reviewed M02-T02 contracts are coherent with the Card authority and OpenSpec.

Independent static assertion replay against exact immutable GitHub contents produced **51/52** passes. The one failure is in `test_historical_artifacts_are_preserved_but_not_active`: the test expects lowercase `do not rewrite historical evidence/handoffs solely because the state model changed`, while `REPOSITORY.md` contains the same sentence beginning with capital `Do`. Since `assertIn` is case-sensitive, the committed regression test is not GREEN as written.

No GitHub Actions/status run exists for this subject. A clean local checkout attempt could not start because DNS resolution for `github.com` failed, so no Python runner pass is claimed.

Impact: Card acceptance 9 and the required focused regression-check boundary are not GREEN for this exact subject; implementation evidence overstates that check. The workflow behavior itself is not shown defective by this finding.

Bounded correction: align the regression assertion with the authoritative text (or make it semantically robust), replay the checks, reconcile evidence, and freeze a new immutable subject. No user/product decision is required.


---

## Re-review attempt 3

Date: 2026-09-20
Review subject: `a3726bf22db1103e1a53c8d6e8256647699b6267`
Verdict: **GREEN**

### Independent inspection

- Recovered the exact Card-owned review subject from the selected workstream Task Board and validated manifest ↔ Task Board identity on `feat/branch-first-managed-changes`.
- Re-read the M02 milestone, M02-T02 Card, REQ-BF-002..009 / 011..017 authority slice, ADR-BF-001..003, M02 OpenSpec, prior RED evidence, exact reviewed source and the implementation evidence.
- Verified the prior topology RED is corrected: historical root/default migration proves `integration_target`, exact base and independent-versus-stacked dependency topology before branch creation/adoption; ambiguity fails closed; topology is persisted and read back before mutable ownership switches.
- Verified the prior regression-test RED is corrected: the historical-preservation assertion now matches the authoritative text.
- Independently replayed the committed focused static assertion set against exact immutable GitHub contents for this subject: **52/52 PASS**.
- Inspected the M02-T02 changed surface for scope/semantic coherence: active execution is workstream-only; root/default state is migration/history input only; binding mismatch does not fall back; Card/milestone review and implementation/recovery Research remain Task-Board-owned; micro-fix, target refresh, terminal target-side recovery and historical preservation remain intact; no ChatGPT-only lifecycle file imports `workflow/codex_only/`.
- The subject changes only the M02-T02 lifecycle/OpenSpec/test/evidence surfaces plus its Task Board bookkeeping. No accepted requirement, ADR or milestone strategy change is required.

No CI/Python runner pass is claimed by this review; the independent verification is exact GitHub subject readback plus connector-backed replay of the committed static contract suite.

### Verdict

**GREEN.** Exact subject `a3726bf22db1103e1a53c8d6e8256647699b6267` satisfies the M02-T02 Card acceptance and applicable M02 authority. No blocking finding remains.
