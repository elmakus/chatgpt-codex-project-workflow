# M02-T05 — cumulative M02 acceptance evidence

Date: 2026-09-22
Card: `M02-T05`
Result before independent review: GREEN / corrected subject review pending
Target repository: `elmakus/project_workflow_v2`
Target branch: `feat/pwv2-m02-intake-definition-planning`
Frozen target commit: `89503fafa55e052e1ee48fb8252cecb6d3028728`
Frozen target tree: `a62d48b362596ab9837583d15177b3bac5a66a8b`
Target integration baseline: `main@8c955d1d9e8ba9396582753814d5b6c3283dde01`
Draft PR: `elmakus/project_workflow_v2#2`

## Acceptance surface

This evidence evaluates the exact target commit against:
- M02-T01..T05 Card contracts;
- approved PWV2-P1 M02 outcome/packages/JIT and validation mapping;
- M02-owned/supporting PWV2 requirements under frozen Definition R1;
- ADR-PWV2-003, ADR-PWV2-005 and ADR-PWV2-006;
- accepted M01 foundation/integration result;
- the S2 Execution Prep guidance;
- immutable M02-T05 R01, R02 and R03 independent-review evidence.

This is deterministic M02 acceptance only. It does not claim M03+ execution/review/Close semantics, L01-L09 live-product acceptance, migration, production adoption or custody transfer.

## Independent-review correction reconciliation

### R01

Independent R01 on `f978dda304ac9de8fe4806f6f31c530cc586e70e` was RED and remains immutable history. Its two blockers remain corrected:
1. completed/consumed Research requires explicit durable conflict accounting across the proportional source classes;
2. material Planning re-entry has exact new-cycle A/B/review/C semantics and bounded `editorial_exempt` state tied to prior exact GREEN review + satisfied C.

### R02

Independent R02 on `6ee800aa1a43b96b3cfb9891031b72d99f21f983` was RED and remains immutable history. Both blockers remain corrected:
1. concrete issue diagnosis requires exact proportional Intake-origin prior-art Research before repair alignment;
2. premium A/B/C expose the accepted best-available / fresh-independent / lighter-cheaper human-facing recommendation semantics without canonical model identity.

### R03

Independent R03 on `fdd737fd16c7aac385bf35699782eafe1722819b` was RED and remains immutable history.

R03 found that the R02 prior-art correction depended on the single current `RESEARCH.toml` continuing to contain the consumed Intake-origin diagnosis record. A later legal Brainstorming Research obligation could reuse that one slot while issue alignment remained pending, after which the router would no longer see the diagnosis proof and would incorrectly demand it again.

The bounded correction keeps the single Research slot and adds only the smallest durable fact needed by Intake:
- `INTAKE.toml` now owns `diagnosis_prior_art_subject` + `diagnosis_prior_art_result`;
- exact consumed Intake-origin diagnosis Research must be reconciled into that binding before alignment proceeds;
- the binding must match the current `repair_subject`; changing the repair subject clears/invalidates it and requires new proportional prior art;
- once reconciled, later legitimate Brainstorming/Definition Research may reuse the single current Research slot without erasing diagnosis proof;
- authorized issue state requires the exact durable prior-art binding;
- feature/change Intake rejects diagnosis-prior-art state;
- production router uses the stable Intake binding, while still requiring/reconciling exact consumed Intake Research when the binding is absent;
- deterministic regression `test_later_brainstorming_research_does_not_erase_issue_diagnosis_prior_art` proves the composed path.

No Research registry/history mechanism was introduced. No Definition/PWV2-P1 strategy or product authority changed.

## Exact Git readback

Immediately before this corrected freeze:
- target feature HEAD = `89503fafa55e052e1ee48fb8252cecb6d3028728`;
- target tree = `a62d48b362596ab9837583d15177b3bac5a66a8b`;
- target `main` remains M01 integration commit `8c955d1d9e8ba9396582753814d5b6c3283dde01`;
- feature is 80 commits ahead / 0 behind current main;
- draft PR #2 has exact base/head above, 23 changed files and is mergeable/clean;
- R03 correction delta from `fdd737f...` is 10 commits touching exactly Intake template/fixture, production router/state validation, their tests, and Intake/Research/Router/State contracts;
- the cumulative 23-file acceptance surface remains common M02 modules/templates plus production router/state validation/tests; no V1 policy directory was added.

## Cumulative deterministic validation

GitHub Actions PR run `35725824309` checked exact target head `89503fafa55e052e1ee48fb8252cecb6d3028728` and completed successfully. Job `test` and the repository-check step are GREEN.

`sh scripts/test.sh` — GREEN:
- preserved M01 package/bootstrap probe;
- production state-contract suite **23/23 PASS**;
- production bundle validation PASS;
- production router suite **28/28 PASS**;
- router CLI smoke PASS;
- M01 baseline checks PASS.

A separate clean detached checkout on Tower at the same exact commit/tree verified:
- `sh scripts/test.sh` — PASS;
- `python3 -m unittest discover -v` — **51/51 PASS**;
- `python3 -m compileall -q tools tests` — PASS;
- `git diff --check` — PASS;
- clean working tree after validation — PASS.

The tests import production `tools/state_contract.py` and `tools/router.py`; there is no parallel test-only workflow interpreter.

No separate combined-status PASS is claimed because GitHub combined commit statuses contain no status records.

## M02 semantic acceptance

### Intake / alignment / mandatory diagnosis prior art

GREEN fixtures prove symptom/marker alone never authorizes repair; a later question/concern/alternative is a response but not authorization; exact authorization is bound to the current repair subject; stale alignment fails closed; micro-fix candidacy requires exact alignment; concrete issue diagnosis requires exact consumed proportional prior-art Research; that result is durably reconciled into Intake before alignment; and a later legal Brainstorming Research obligation cannot erase the diagnosis prior-art proof while issue alignment is still pending.

### Brainstorming / Research / Definition — A13

GREEN fixtures prove intrinsic adaptive exploration without an active `#grill`; exact revision-bound Definition promotion; GREEN challenge audit; Research exact origin/return and once-only reconciliation; mandatory proportional accounting for official/upstream, project/runtime, tracker/discussion and practitioner/community source classes with explicit status/weight and explicit conflict accounting; single current Research-slot reuse after exact return-owner reconciliation; Definition exact promoted subject and premium stop A.

### Strategic Planning / Plan Review / premium A/B/C

GREEN fixtures prove material planning-cycle identity; stale A rejection after cycle movement; positive new-cycle A stop/satisfaction; GREEN planner audit before freeze; immutable plan Git subject; B fresh independent best-available-context boundary; exact independent Plan Review subject/revision/cycle; GREEN consumption before C; C before Execution Prep; full material replan A/B/review/C trace; bounded editorial/mechanical review omission only with preserved prior exact GREEN+C basis; and the required human-facing best-available recommendation at A plus lighter/cheaper recommendation at C.

### GitHub tracker — A14

GREEN fixtures prove discovery/dedup before create, interrupted create readback before retry, exact linked Issue correlation, ambiguous duplicate recovery, capability-unavailable state, reserved final-PR pointer and rejection of tracker-carried repair/requirements/plan authorization.

## DROP / boundary regression

Production validation and repository checks continue to reject or omit:
- execution-policy selection;
- runtime/model/session/worker identity as canonical authority;
- V1 ChatGPT/Codex/legacy semantic trees;
- Context Health/FRESH lifecycle;
- Project-Card lane/batch/scheduler state;
- automatic issue repair from marker/symptom;
- tracker content as authority;
- planner-performed/internal Stage-6 independent review.

M03+ execution/delegation/final-review behavior remains explicitly unavailable rather than guessed.

## GitHub Actions / PR readback

For this corrected frozen target:
- Actions PR run `35725824309` is `completed/success`;
- job `test` is GREEN;
- repository-check step is GREEN;
- combined commit statuses contain no separate status records;
- draft PR #2 reports exact corrected head/base, 23 changed files and mergeable/clean.

This does not waive the later pre-merge refresh/readback required by Close.

## Corrected review freeze

The correcting context found no remaining deterministic M02 acceptance failure after the exact corrected commit above.

The next immutable independent-review subject combines:
- exact corrected target commit/tree;
- unchanged exact M02-T05 Card blob;
- this refreshed exact acceptance-evidence blob once persisted.

M02-T05 remains non-terminal. R01, R02 and R03 RED remain historical evidence and do not apply to the corrected subject. Because this chat implemented the R03 correction, it must not independently review the new subject; a fresh independent reviewer is required before Card finalization and M02 Close/integration.

No production adoption, migration or custody transfer is authorized.
