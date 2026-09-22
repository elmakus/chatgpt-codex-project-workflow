# M02-T05 — independent review R04

Date: 2026-09-22
Card: `M02-T05`
Verdict: **GREEN**
Review owner: selected Task Board for `feature-common-preexecution-core`

## Exact reviewed subject

`elmakus/project_workflow_v2@commit:89503fafa55e052e1ee48fb8252cecb6d3028728|tree:a62d48b362596ab9837583d15177b3bac5a66a8b|M02-T05-card-blob:6d11a5f70d393de21e5e8b5b09c52c50c64c08b4|acceptance-evidence-blob:ee0d2d21bb3c9f7f32b4ca4d9156ea5a696b51cb`

The exact target branch HEAD, commit/tree, Task Card blob and cumulative acceptance-evidence blob match the frozen subject.

## Authority and evidence reviewed

- current Project Workflow `main`: common authority plus ChatGPT-only router/state/workstream/independent-review contracts;
- selected `feature-common-preexecution-core` manifest and Task Board;
- exact M02-T05 Card and cumulative acceptance evidence;
- immutable M02-T05 R01, R02 and R03 RED evidence and the correction chain they require;
- approved `PWV2-P1` M02 outcome/packages/checkpoint and §6 validation mapping;
- `requirements/PROJECT_WORKFLOW_V2.md` R1 M02-owned/supporting requirements, including PWV2-REQ-039..050, 053..058 and 067..071;
- ADR-PWV2-003, ADR-PWV2-005 and ADR-PWV2-006;
- accepted M02-T01..T04 evidence plus M01 integrated baseline;
- exact target source/templates/tests and the R03→R04 correction delta at `elmakus/project_workflow_v2@89503fafa55e052e1ee48fb8252cecb6d3028728`;
- exact GitHub PR/Actions/readback for the frozen target.

## Independent verification

Exact GitHub readback confirms:
- target feature branch HEAD = `89503fafa55e052e1ee48fb8252cecb6d3028728`;
- target tree = `a62d48b362596ab9837583d15177b3bac5a66a8b`;
- draft PR #2 is open, targets `main`, has the frozen feature head, 23 changed files and is mergeable;
- Actions run `35725824309` for the exact frozen head is `completed/success`;
- job `test` and its repository-check step are GREEN;
- job logs execute `sh scripts/test.sh` and show production state-contract **23/23 PASS**, production router **28/28 PASS**, package-probe PASS and M01 baseline PASS;
- the exact target tree contains no V1 fixed-policy directory, Context Health lifecycle, scheduler/lane/batch tree or other prohibited normal-policy namespace.

No separate combined-status PASS is claimed; the acceptance record correctly keeps that limitation explicit.

## Review findings

### R03 blocker is closed

The R03 correction is present in production semantics, not only fixtures:

- Intake now owns an exact durable `diagnosis_prior_art_subject` + `diagnosis_prior_art_result` binding;
- a concrete issue repair subject without that stable binding must first materialize/consume exact Intake-origin proportional Research, then route through Intake to persist the binding before alignment;
- authorized issue state requires the binding to match the current repair subject;
- changing the repair subject makes the prior binding stale, while feature/change Intake rejects diagnosis-prior-art state;
- legitimate later Brainstorming/Definition Research can reuse the single current Research slot without erasing diagnosis proof;
- the composed production-router regression `test_later_brainstorming_research_does_not_erase_issue_diagnosis_prior_art` is present and GREEN.

This is the bounded correction R03 requested and does not introduce a speculative Research registry/history mechanism.

### R01/R02 corrections remain satisfied

The exact frozen target retains the prior accepted corrections:
- completed/consumed Research requires all proportional source classes, explicit source weights and explicit conflict accounting;
- material planning re-entry has a new exact A/B/Plan-Review/C cycle and stale-cycle rejection;
- the bounded editorial/mechanical exemption is tied to prior exact GREEN review plus satisfied C and a semantic exemption basis;
- concrete issue diagnosis requires proportional prior-art Research before repair alignment can proceed;
- premium A and C carry the required best-available and lighter/cheaper human-facing recommendations without making model identity canonical.

### Remaining M02 acceptance surface

The reviewed production contracts/tests also retain:
- intrinsic Brainstorming with thematic/numbered recommendations, agent-owned Research, final challenge and exact Definition promotion;
- exact Research origin/return and once-only reconciliation;
- GitHub Issue discovery/dedup, uncertain-create readback, exact correlation, ambiguous recovery and tracker-as-bookkeeping-only semantics;
- progressive disclosure and runtime-neutral routing/state;
- explicit fail-closed boundary for M03+ execution/finalization semantics rather than guessed implementation.

No M03+ semantics, L01-L09 live acceptance, migration/adoption or custody-transfer claim is made by this verdict.

## Verdict

**GREEN.** The exact immutable R04 subject satisfies the M02-T05 Card contract and the applicable accepted M02 authority. R01, R02 and R03 remain immutable RED history for their older subjects; they do not apply to the corrected R04 subject.

The independent-review role is complete. Per the current ChatGPT-only router/state contract, M02-T05 remains non-terminal until deterministic Post-review Card finalization, after which M02 Close may integrate the accepted M02 target through its PR.
