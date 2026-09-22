# M02-T05 — independent review R03

Date: 2026-09-22
Card: `M02-T05`
Verdict: **RED**
Review owner: selected Task Board for `feature-common-preexecution-core`

## Exact reviewed subject

`elmakus/project_workflow_v2@commit:fdd737fd16c7aac385bf35699782eafe1722819b|tree:dc21a3986cc0fbbec7e2d299570d0dca3181d970|M02-T05-card-blob:6d11a5f70d393de21e5e8b5b09c52c50c64c08b4|acceptance-evidence-blob:431c9175a1f0ec77a064453b6bd82f23cac06ad2`

The target commit/tree, Card blob and cumulative-acceptance-evidence blob were read back independently and match the frozen subject.

## Authority and evidence reviewed

- current Project Workflow `main`: ChatGPT-only router, state, workstream and independent-review contracts plus common authority;
- selected workstream manifest + Task Board;
- M02-T05 Card and corrected cumulative acceptance evidence;
- immutable M02-T05 R01 and R02 RED evidence;
- approved `PWV2-P1` M02.P1-P4 contract, checkpoint and §6 validation mapping;
- `requirements/PROJECT_WORKFLOW_V2.md` M02-owned requirements, especially PWV2-REQ-048..050 and PWV2-REQ-053..055;
- ADR-PWV2-003, ADR-PWV2-005 and ADR-PWV2-006;
- S2 Execution Prep guidance;
- exact target source/templates/tests at `elmakus/project_workflow_v2@fdd737fd16c7aac385bf35699782eafe1722819b`.

## Independent verification

Exact GitHub readback proves:
- target commit = `fdd737fd16c7aac385bf35699782eafe1722819b`;
- target tree = `dc21a3986cc0fbbec7e2d299570d0dca3181d970`;
- feature is 70 commits ahead / 0 behind `main@8c955d1d9e8ba9396582753814d5b6c3283dde01`;
- draft PR #2 has the exact frozen head/base, 23 changed files and is mergeable;
- Actions run `35722629802` is completed/success and its `test` job / repository-check step are GREEN;
- combined commit statuses contain no separate status records, so no separate combined-status PASS is claimed.

The R02 corrections are materially present: exact consumed Intake-origin prior-art Research is required before issue alignment, and premium A/B/C carry the accepted human-facing context recommendations.

## Blocking finding — single-slot Research invalidates a legal issue-alignment continuation

The R02 diagnosis-prior-art correction is not composable with the already-accepted Brainstorming/Research path while issue alignment is still active.

Exact frozen behavior:

1. Workstream validation permits only one Research locator and binds it to the single exact path `implementation/workstreams/<id>/RESEARCH.toml`.
2. For any issue Intake with a non-empty `repair_subject`, `tools/router.py` requires the **currently loaded** Research record to be `state = consumed`, `origin_role = intake`, exact `origin_subject = repair_subject`, `return_target = intake`, and applied with a non-empty result.
3. The same router correctly sends a post-diagnosis user `question | concern | alternative` to Brainstorming while Intake remains active/pending.
4. Accepted M02 authority then allows/obliges Brainstorming to use Research for agent-findable facts (PWV2-REQ-048..050 / M02.P2). That later Research must reuse the same single `RESEARCH.toml` slot because no second/history Research locator/path is legal.
5. After that Brainstorming Research is applied and consumed, routing falls through to the still-active issue Intake. The current Research now has `origin_role = brainstorming`, so the exact-diagnosis check fails and routes back to Intake demanding the diagnosis prior-art Research again.
6. No target contract defines an archive/rebind mechanism that preserves a stable consumed diagnosis-prior-art binding on Intake while allowing the one Research slot to serve the later legal obligation. The exact tree contains no Research history/evidence mechanism beyond the single template/contract.

This means a legal M02 path — issue diagnosis prior art → user question/concern → Brainstorming → additional factual Research → consumed return while alignment is still pending — cannot retain both obligations coherently. The isolated fixtures pass, but the composed lifecycle required by the accepted authority is not covered.

This violates the M02.P1/P2 composition behind PWV2-REQ-048..050 and PWV2-REQ-055, and makes the R02 fix non-durable across a subsequent legal Research obligation.

## Verdict and corrective route

**RED.** This subject remains immutable and R03 evidence applies only to it. R01/R02 history remains immutable.

The correction is bounded L1/L2 implementation work inside accepted Definition/PWV2-P1 authority. It does not require a product decision, Definition change, Master Plan change or new factual Research.

Prefer the smallest durable fix: once exact consumed Intake-origin diagnosis Research is reconciled, persist an Intake-owned exact prior-art binding/result sufficient to prove that exact `repair_subject` was checked. Router validation can then rely on that stable Intake-owned fact after later Research legitimately reuses the single Research slot. Avoid adding a generalized Research registry/history unless current authority proves it necessary.

Add a deterministic composed fixture covering:
`issue prior-art consumed → question/concern → Brainstorming Research active/complete/consumed → return to still-pending issue alignment`.

Then rerun cumulative M02 validation, refresh acceptance evidence and freeze a new immutable M02-T05 subject for a fresh independent reviewer.
