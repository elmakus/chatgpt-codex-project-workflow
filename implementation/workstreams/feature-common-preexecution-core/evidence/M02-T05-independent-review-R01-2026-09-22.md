# M02-T05 — independent review R01

Date: 2026-09-22
Card: `M02-T05`
Verdict: **RED**
Review owner: selected Task Board for `feature-common-preexecution-core`

## Exact reviewed subject

`elmakus/project_workflow_v2@commit:f978dda304ac9de8fe4806f6f31c530cc586e70e|tree:5a7557e9c7f6042af8f97a21dbce4ecd5314b49d|M02-T05-card-blob:6d11a5f70d393de21e5e8b5b09c52c50c64c08b4|acceptance-evidence-blob:27b3208111bfd65f62d45ce1f8e5f0a0293d3079`

The Card blob and cumulative-acceptance-evidence blob were read back from the control branch and match the frozen subject. The target commit/tree also match the frozen subject.

## Authority and evidence reviewed

- current Project Workflow `main`: ChatGPT-only router, independent-review/state contracts and common authority;
- selected workstream manifest + Task Board;
- M02-T05 Card and cumulative acceptance evidence;
- approved `PWV2-P1` M02 contract, §6 validation mapping and Appendix A ownership;
- `requirements/PROJECT_WORKFLOW_V2.md` R1, especially PWV2-REQ-039..050;
- ADR-PWV2-003, ADR-PWV2-005 and ADR-PWV2-006;
- accepted M01 cumulative evidence and M02-T01..T04 Card/evidence records;
- S2 Execution Prep guidance;
- exact target diff/source/templates/tests at `elmakus/project_workflow_v2@f978dda304ac9de8fe4806f6f31c530cc586e70e`.

## Independent verification

Exact clean detached checkout on Tower:

- HEAD = `f978dda304ac9de8fe4806f6f31c530cc586e70e`;
- tree = `5a7557e9c7f6042af8f97a21dbce4ecd5314b49d`;
- `sh scripts/test.sh` — PASS (state 22/22, router 25/25 plus preserved package/baseline checks);
- `python3 -m unittest discover -v` — 47/47 PASS;
- `python3 -m compileall -q tools tests` — PASS;
- `git diff --check` — PASS;
- clean working tree after validation — PASS.

GitHub readback confirms draft PR #2 is still exact head/base and mergeable. The previously recorded Actions anomaly has resolved: workflow run `35718260814` is now `completed/success`; its `test` job and repository-check step are GREEN. Combined commit statuses remain empty, so no separate combined-status check is claimed.

## Blocking finding 1 — premium re-entry/exemption contract is incomplete

Accepted authority requires a material later re-entry into Strategic Planning to repeat the full A → Planning → B → Plan Review → C block (PWV2-REQ-044 / ADR-PWV2-005), and M02-T03 explicitly includes bounded editorial/mechanical review exemptions plus deterministic A/B/C restart/re-entry fixtures.

The frozen target does not fully realize that contract:

- `workflow/PLANNING.md` states the intended cycle semantics, but `tools/state_contract.py::validate_planning` only proves that a Planning record self-asserts `premium_a = "satisfied"` and that `premium_a_subject == entry_subject`;
- Definition state carries only `premium_a = not_due|due|satisfied`; it does not durably bind the user-owned A satisfaction to the exact later planning-cycle subject that Planning claims;
- `tools/router.py` can stop on Definition A, but after A satisfaction there is no cross-owner validation proving that the exact A just satisfied is the A claimed by a new material cycle;
- the only cycle-2 fixture is a negative stale-subject rejection. There is no positive material-replan A→B→independent review→C recovery trace;
- the accepted editorial/mechanical exemption is described in prose but has no production state/route representation and no deterministic fixture. A changed frozen plan subject still requires an exact matching Plan Review through the current validator/router.

Therefore the M02-T03/M02 checkpoint claims for material replan and editorial exemption are not yet accepted.

## Blocking finding 2 — A13 Research conflict accounting is not implemented

ADR-PWV2-006, M02-T02 and the approved A13 oracle require source weighting **and explicit conflict handling/accounting** across the proportional prior-art classes.

The frozen target accounts for source classes, status and a non-empty `weight`, but not conflicts:

- `templates/RESEARCH.toml` has class/status/weight plus global finding/limitations only;
- `tools/state_contract.py::validate_research` requires all four source classes and non-empty weight, but has no required conflict/conflict-resolution field or equivalent invariant;
- `workflow/RESEARCH.md` says community popularity does not override stronger authority, but does not make conflicting evidence a durable completed-record obligation.

A Research record containing contradictory source classes can therefore validate as complete without explicitly recording that conflict. This does not satisfy the M02-T02 Card acceptance or A13's `weights/conflicts/limits` oracle.

## Verdict and corrective route

**RED.** The exact reviewed subject remains immutable and must retain this failed R01 evidence.

Both findings are bounded implementation corrections inside already accepted Definition/PWV2-P1 authority. They do not require a product/strategic decision, a Master Plan change, or new Research before correction. Router classification is therefore bounded L1/L2 corrective Execution Prep/Execution.

After correction, cumulative M02 validation must be rerun against the new exact target commit, the acceptance evidence must be refreshed, and a new immutable M02-T05 review subject must be frozen as `pending` for a fresh independent reviewer. This R01 verdict must not be reused for the corrected subject.
