# M02-T05 — cumulative M02 acceptance evidence

Date: 2026-09-22
Card: `M02-T05`
Result before independent review: GREEN / corrected subject review pending
Target repository: `elmakus/project_workflow_v2`
Target branch: `feat/pwv2-m02-intake-definition-planning`
Frozen target commit: `fdd737fd16c7aac385bf35699782eafe1722819b`
Frozen target tree: `dc21a3986cc0fbbec7e2d299570d0dca3181d970`
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
- immutable M02-T05 R01 and R02 independent-review evidence.

This is deterministic M02 acceptance only. It does not claim M03+ execution/review/Close semantics, L01-L09 live-product acceptance, migration, production adoption or custody transfer.

## Independent-review correction reconciliation

### R01

Independent R01 on `f978dda304ac9de8fe4806f6f31c530cc586e70e` was RED and remains immutable history. Its two blockers remain corrected:
1. completed/consumed Research requires explicit durable conflict accounting across the proportional source classes;
2. material Planning re-entry has exact new-cycle A/B/review/C semantics and bounded `editorial_exempt` state tied to prior exact GREEN review + satisfied C.

### R02

Independent R02 on `6ee800aa1a43b96b3cfb9891031b72d99f21f983` was RED and remains immutable history. Both new blockers were corrected inside already accepted M02 authority:

1. **Mandatory prior-art for concrete issue diagnosis**
   - `workflow/INTAKE.md` now requires a concrete current issue `repair_subject` to materialize proportional Research with `origin_role = intake`, exact `origin_subject = repair_subject`, and `return_target = intake`;
   - alignment cannot proceed until that exact Research result is applied and consumed;
   - changed repair subject makes the previous diagnosis Research stale;
   - `tools/router.py` production routing enforces the exact consumed Research binding before alignment/completion can advance;
   - deterministic fixtures prove missing or stale diagnosis Research routes back to Intake and exact consumed Research permits the normal alignment stop/continuation.

2. **Premium A/B/C human-facing recommendation semantics**
   - initial and re-entry A stops explicitly recommend the best available model/context for Strategic Planning without making model identity canonical;
   - B explicitly requires a fresh independent best-available review context;
   - C explicitly recommends switching to a lighter/cheaper model/context before Execution Prep;
   - `DEFINITION.md`, `PLANNING.md`, `ROUTER.md` and production router reasons carry the same semantics;
   - deterministic router fixtures assert A/B/C recommendation text.

No Definition/PWV2-P1 strategy or product authority changed.

## Exact Git readback

Immediately before this corrected freeze:
- target feature HEAD = `fdd737fd16c7aac385bf35699782eafe1722819b`;
- target tree = `dc21a3986cc0fbbec7e2d299570d0dca3181d970`;
- target `main` remains M01 integration commit `8c955d1d9e8ba9396582753814d5b6c3283dde01`;
- feature is 70 commits ahead / 0 behind current main;
- draft PR #2 has exact base/head above, 23 changed files and is mergeable;
- the 23-file acceptance surface remains common M02 modules/templates plus production router/state validation/tests; no V1 policy directory was added.

## Cumulative deterministic validation

GitHub Actions PR run `35722629802` checked the refreshed PR merge subject containing target head `fdd737fd16c7aac385bf35699782eafe1722819b` and completed successfully.

`sh scripts/test.sh` — GREEN:
- preserved M01 package/bootstrap probe;
- production state-contract suite **23/23 PASS**;
- production bundle validation PASS;
- production router suite **27/27 PASS**;
- router CLI smoke PASS;
- M01 baseline checks PASS.

The router suite now includes `test_issue_diagnosis_requires_exact_consumed_prior_art_research` plus A/B/C recommendation assertions. The tests import production `tools/state_contract.py` and `tools/router.py`; there is no parallel test-only workflow interpreter.

No separate combined-status PASS is claimed because GitHub combined commit statuses contain no status records.

## M02 semantic acceptance

### Intake / alignment / mandatory diagnosis prior art

GREEN fixtures prove symptom/marker alone never authorizes repair; a later question/concern/alternative is a response but not authorization; exact authorization is bound to the current repair subject; stale alignment fails closed; micro-fix candidacy requires exact alignment; and a concrete issue diagnosis cannot reach alignment/completion without exact consumed proportional prior-art Research for the current repair subject.

### Brainstorming / Research / Definition — A13

GREEN fixtures prove intrinsic adaptive exploration without an active `#grill`; exact revision-bound Definition promotion; GREEN challenge audit; Research exact origin/return and once-only reconciliation; mandatory proportional accounting for official/upstream, project/runtime, tracker/discussion and practitioner/community source classes with explicit status/weight and explicit conflict accounting; Definition exact promoted subject and premium stop A.

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
- Actions run `35722629802` is `completed/success`;
- job `test` is GREEN;
- repository-check step is GREEN;
- combined commit statuses contain no separate status records;
- draft PR #2 reports exact corrected head/base and mergeable.

This does not waive the later pre-merge refresh/readback required by Close.

## Corrected review freeze

The correcting context found no remaining deterministic M02 acceptance failure after the exact corrected commit above.

The next immutable independent-review subject combines:
- exact corrected target commit/tree;
- unchanged exact M02-T05 Card blob;
- this refreshed exact acceptance-evidence blob once persisted.

M02-T05 remains non-terminal. R01 and R02 RED remain historical evidence and do not apply to the corrected subject. Because this chat implemented the R02 correction, it must not independently review the new subject; a fresh independent reviewer is required before Card finalization and M02 Close/integration.

No production adoption, migration or custody transfer is authorized.
