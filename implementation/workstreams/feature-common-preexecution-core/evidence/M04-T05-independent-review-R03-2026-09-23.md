# M04-T05 — independent review R03

Date: 2026-09-23
Card: `M04-T05`
Verdict: **GREEN**
Review owner: selected workstream Task Board
Review subject: `elmakus/project_workflow_v2@commit:013c4b405875a356f863b9b381d60faa0ad8935a|tree:7367d38d41240730530ec3b16174ca7db2738807|M04-T05-card-blob:61ae9578d0df1eb7dbb4f0030d638fa846e2f6aa|acceptance-evidence-blob:9cbe9998860fe74517c387d9c1fed713c872deb0`

## Review purpose and independence

This is a retrospective independent revalidation of the already-frozen M04-T05 subject after the user reported an independence/provenance problem with the prior R02 review.

This reviewer context did not implement or repair the frozen target subject. The verdict below was reconstructed from durable repository authority, the exact immutable reviewed subject, the actual M04 diff/source, acceptance evidence and GitHub readback. The prior R02 record was read only as historical/provenance context and is not used as the basis for this verdict. R01 RED and R02 remain immutable history.

Because M04 was already terminal and downstream M05 execution had begun before this revalidation request, no transient `done + review_state: in_progress` state was written. The exact subject was not mutated while judging it; this R03 terminal record is appended and the Task Board canonical review-evidence pointer is updated only after the verdict.

## Authority and acceptance reviewed

- `planning/PROJECT_WORKFLOW_V2_MASTER_PLAN.md` revision `PWV2-P1`, M04.P1-P4, M04 checkpoint/JIT and A06/A08/A09/A10/A16.
- `requirements/PROJECT_WORKFLOW_V2.md` R1, especially PWV2-REQ-032..038, 051, 056..066, 068, 070 and 073.
- `decisions/ADR_PROJECT_WORKFLOW_V2_MANAGED_CHANGE_LIFECYCLE.md` (ADR-PWV2-003).
- `decisions/ADR_PROJECT_WORKFLOW_V2_REVIEW_AND_PREMIUM_PLANNING.md` (ADR-PWV2-005).
- Trigger-only fork lineage authority in `decisions/ADR_FORK_RELEASE_VERSION_LINEAGE.md` and `requirements/FORK_RELEASE_VERSIONING.md` R1.
- M04-T01..T04 contracts/evidence and the accepted M03 cumulative baseline.
- Exact M04-T05 Card and cumulative R02 acceptance evidence identified by the frozen blob SHAs.
- Actual target source/diff at `elmakus/project_workflow_v2@013c4b405875a356f863b9b381d60faa0ad8935a`.

## Exact-subject readback

Independent GitHub readback confirms:

- M04-T05 Card blob = `61ae9578d0df1eb7dbb4f0030d638fa846e2f6aa`;
- cumulative acceptance blob = `9cbe9998860fe74517c387d9c1fed713c872deb0`;
- reviewed target commit = `013c4b405875a356f863b9b381d60faa0ad8935a`;
- reviewed target tree = `7367d38d41240730530ec3b16174ca7db2738807`;
- the R01 correction is exactly one commit after `f40250fa2fe88477df3f03c26adfeb2d8024581b` and changes only `tools/fork_release_contract.py` plus `tests/test_fork_release_contract.py`;
- PR #4 later merged that exact reviewed head to `main`, producing merge result `674fb970913c393cfc6ed82a5ef67dda8b8713b7`.

The complete M03-accepted-head to M04-frozen-head delta is 11 commits / 16 files, limited to common Close, tracker/external-effect, recovery/cleanup, fork-lineage, router/state support and deterministic tests/scripts. No runtime-specific policy tree, scheduler, Context Health lifecycle or V1 semantic route was introduced by the M04 delta.

## Independent semantic review

### M04.P1 — moving-target refresh and review coverage

`workflow/CLOSE.md` and `tools/close_contract.py` correctly distinguish target SHA movement from material content/behavior/acceptance change. GREEN reuse requires unchanged covered semantics plus affected compatibility GREEN; new required acceptance, changed content or changed behavior produces a new review subject. A target movement after refresh fails the pre-mutation check. Stacked integration does not depend on parent-branch survival and does not bypass a genuine unaccepted parent-only dependency.

No blocking defect found.

### M04.P2 — external effects and tracker closure

The external-effect oracle requires exact-object readback before retry. Pending effects route to readback; unresolved/uncertain occurrence fails closed; only verified no-effect permits retry; verified expected effect reconciles without replay.

Tracker closing linkage is available only for a linked tracker on a final scope-completing default-branch integration. Early Issue closure is reconciliation evidence rather than approval; explicit fallback close requires durable accepted completion and unavailable/disabled automatic closure. Tracker state remains bookkeeping and does not authorize implementation.

No blocking defect found.

### M04.P3 — terminal recovery and cleanup

Target-side recovery binds the original source provenance to the exact merged source head, requires immutable merge evidence and fails closed when required unique recovery artifacts are missing. Recovery does not require the source ref to survive.

Automatic merged-head deletion is treated as valid normal cleanup. A surviving `safe_to_delete` ref requires exact-head revalidation before deletion and absence readback before terminal deleted state. Terminal-unmerged closure rejects importing rejected implementation content into the integration target.

No blocking defect found.

### M04.P4 — trigger-only fork lineage and end of scope

The optional fork module is selected only for the exact `downstream_fork_release` operation and requires complete accepted lineage. Ordinary Close does not load the fork module.

The R01 blocking defect is closed on this subject: `UpstreamLineage` now requires the upstream commit to match exact lowercase 40-hex Git SHA syntax before the fork-release module can activate, with deterministic rejection of empty, non-SHA, uppercase, 39-character and 41-character identities.

Private release lanes are baseline-local and numeric, cross-baseline ordering is numeric, historical tags are declared immutable, synthetic `vlatest` is rejected, and an optional native latest alias must point to the same accepted canonical artifact. The module does not authorize sync, tag creation/movement, release publication or deployment.

Close reaches end-of-approved-scope only after durable completion with no already-authorized obligation remaining; deployment/live-write status alone does not manufacture a human gate.

No blocking defect found.

Actual tag/release/deployment mutation is explicitly outside M04-T05 scope. Its later real-surface qualification therefore is not treated as an M04 acceptance defect.

## Verification/readback

For the exact reviewed head/tree:

- GitHub Actions push run `35773744806`: completed **success**, exact head `013c4b405875a356f863b9b381d60faa0ad8935a`, tree `7367d38d41240730530ec3b16174ca7db2738807`;
- GitHub Actions pull-request run `35773750088`: completed **success** for PR #4 with the same reviewed head;
- repository-check job completed success and executed `sh scripts/test.sh`;
- logged component suites: state 28/28, router 39/39, execution 4/4, review 1/1, recovery 2/2, Close + fork-lineage 29/29;
- cumulative acceptance additionally records full unittest discovery 103/103, compileall, diff-check and clean-tree verification.

The automated evidence is consistent with the independently inspected implementation and acceptance authority.

## Verdict

**GREEN.** No blocking defect was found in the exact frozen M04-T05 subject. The R01 exact-upstream-SHA defect is correctly repaired, and the reviewed subject satisfies the accepted M04 integration/Close, external-effect/tracker, terminal-recovery, trigger-only fork-lineage and end-of-scope contracts.

R01 remains immutable RED history. R02 remains historical evidence but is not relied on for this revalidation. This R03 is the independent confirmation for the unchanged exact M04-T05 subject.
