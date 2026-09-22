# M02-T05 — independent review R02

Date: 2026-09-22
Card: `M02-T05`
Verdict: **RED**
Review owner: selected Task Board for `feature-common-preexecution-core`

## Exact reviewed subject

`elmakus/project_workflow_v2@commit:6ee800aa1a43b96b3cfb9891031b72d99f21f983|tree:8514a0ac31831a1419f16138ad4e6e99b1e2c840|M02-T05-card-blob:6d11a5f70d393de21e5e8b5b09c52c50c64c08b4|acceptance-evidence-blob:eed718f4821a4dcc4aba711ec26b4bd0e0674368`

The target commit/tree, Card blob and cumulative-acceptance-evidence blob were independently read back and match the frozen subject. Draft PR `elmakus/project_workflow_v2#2` has exact head `6ee800aa1a43b96b3cfb9891031b72d99f21f983`, base `main@8c955d1d9e8ba9396582753814d5b6c3283dde01`, remains draft/open and mergeable.

## Authority and evidence reviewed

- current Project Workflow `main`: ChatGPT-only router, independent-review/state contracts and common authority;
- selected workstream manifest + Task Board;
- M02-T05 Card and corrected cumulative acceptance evidence;
- prior immutable M02-T05 R01 RED evidence and its claimed correction reconciliation;
- approved `PWV2-P1` M02.P1-P4 contract, checkpoint and requirement mapping;
- `requirements/PROJECT_WORKFLOW_V2.md` R1, including PWV2-REQ-039..050, 053..058 and 067..071;
- ADR-PWV2-003, ADR-PWV2-005 and ADR-PWV2-006;
- accepted M02-T01..T04 Card/evidence records;
- exact target source/templates/tests and R01→R02 correction delta at `elmakus/project_workflow_v2@6ee800aa1a43b96b3cfb9891031b72d99f21f983`;
- exact GitHub Actions / PR / commit readback.

## Independent verification

Exact GitHub readback proves:
- target commit = `6ee800aa1a43b96b3cfb9891031b72d99f21f983`;
- target tree = `8514a0ac31831a1419f16138ad4e6e99b1e2c840`;
- feature is 63 commits ahead / 0 behind the M01 integration baseline;
- PR #2 has 23 changed files and exact head/base above;
- Actions run `35721133467` is completed/success and job `test` / repository checks are GREEN;
- combined commit statuses are empty, so no separate combined-status PASS is claimed.

The R01 corrections are materially present in production code, not only tests:
- completed/consumed Research now requires non-empty durable `conflicts`, all proportional source classes and explicit weights;
- Planning now represents material re-entry with exact cycle-bound A state, routes A before resumed planning, preserves exact B/review/C binding and has a bounded `editorial_exempt` mode tied to a prior exact GREEN-reviewed subject and satisfied C;
- deterministic positive and negative tests cover these corrected paths.

## Blocking finding 1 — issue diagnosis can bypass mandatory prior-art Research

Accepted authority is broader than the M02-T01 local acceptance wording:

- PWV2-REQ-049 and ADR-PWV2-006 require **every Research/diagnosis** to perform a mandatory-but-proportional prior-art check across relevant official/upstream, project/runtime, tracker/discussion and practitioner/community sources, with source weight/conflict handling.
- M02.P1 performs read-only `#issue` diagnosis before repair alignment; M02.P2 supplies the Research mechanism and allows Research to return to Intake.

The frozen target does not require that prior-art obligation before a diagnosed issue can reach alignment/completion:

- `workflow/INTAKE.md` says “read-only diagnosis first” but does not require proportional prior-art Research (or an equivalent exact prior-art result) before presenting/authorizing a repair;
- `tools/state_contract.py::validate_intake` validates diagnosis revision, repair subject and user alignment but carries no binding to a completed diagnosis Research result;
- `tools/router.py` correctly prioritizes a Research locator when one exists, but it does not require one for an issue diagnosis;
- the production router test `test_completed_preboard_intake_routes_without_manufacturing_board` demonstrates a completed authorized issue with `diagnosis_revision = 2` and a repair subject proceeding directly toward Execution Prep with no Research locator/prior-art result.

Therefore a legal M02 state can satisfy issue alignment while skipping the mandatory prior-art check required for diagnosis. This violates PWV2-REQ-049 / ADR-PWV2-006.

## Blocking finding 2 — premium A/C omit required human-facing context recommendations

PWV2-P1 M02.P3 and accepted requirements specify not only durable stops but their human-facing recommendation semantics:

- PWV2-REQ-041: Strategic Planning must use the best available model/context **as a human-facing recommendation**, without hard-coding a product model name;
- PWV2-REQ-043: after GREEN Plan Review, premium stop C must occur before Execution Prep **with a recommendation to switch to a lighter/cheaper model**;
- M02.P3 restates A as “recommend best available context” and C as “recommend a lighter/cheaper context”; B requires a fresh independent best-context reviewer.

The frozen target implements the gate ordering but not the full A/C recommendation contract:
- `workflow/PLANNING.md` defines A/B/C state/order but contains no best-available-context recommendation at A and no lighter/cheaper recommendation at C;
- `workflow/ROUTER.md` lists A/B/C stop routes but omits those A/C human-facing recommendation semantics;
- `tools/router.py` returns A/C stop reasons that only identify the gate; they do not carry the required recommendation;
- the M02-T03 deterministic fixtures assert stop identity/order but do not assert these recommendation semantics.

`workflow/PLAN_REVIEW.md` does correctly state that Stage-6 review requires a fresh independent best-available context, so the B independence/best-context contract is present. The blocker is specifically the missing A and C human-facing recommendations.

## Verdict and corrective route

**RED.** The exact reviewed subject remains immutable and this R02 evidence applies only to that subject. Prior R01 RED history also remains immutable.

Both findings are bounded implementation/acceptance corrections inside already accepted R1 / PWV2-P1 authority. They do not require a product decision, Definition change, Master Plan change or new factual Research before correction.

Corrective route: bounded L1/L2 Execution Prep / Execution. The correction should:
1. make proportional prior-art Research (or an equivalently exact Research result using the existing Research contract) mandatory for a concrete `#issue` diagnosis before repair alignment can complete/proceed, with deterministic fail-closed and positive recovery fixtures;
2. make premium A and C user-facing contracts explicitly carry the accepted model/context recommendations without canonical product-model identity, with deterministic assertions;
3. rerun cumulative M02 validation against the new exact target commit;
4. refresh M02-T05 acceptance evidence and freeze a new immutable review subject as `pending` for a fresh independent reviewer.

This reviewer context must not review the corrected subject after implementing any part of it.

## Reviewer-state bookkeeping note

While entering `review_state: in_progress`, this reviewer made a transient control-Task-Board serialization error that duplicated the M02-T05 block. It was detected by immediate readback and repaired on the control branch before subject judgment continued. The current selected Task Board has one unambiguous M02-T05 record, the frozen reviewed subject never changed, and this bookkeeping incident did not mutate `elmakus/project_workflow_v2` or the reviewed subject.
