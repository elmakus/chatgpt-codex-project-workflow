# M07-T01 — full automated qualification and acceptance-gap reconciliation

Date: 2026-09-23
Result: GREEN for the automated M07.P1 slice. This evidence does **not** claim first-production acceptance; the mandatory real-surface ledger below remains open.

## Exact candidate and repository readback

Target repository: `elmakus/project_workflow_v2`
Target branch: `feat/pwv2-m07-qualification`
Exact candidate commit: `15978113e46abc8498ceaef594461c8613fcadb8`
Exact candidate tree: `f05d86d72f9bbe941583b4ccf92e2c46b5decf83`
M06 baseline / PR base: `main@2d010a95bac89dfd561dcc3accad6c5e8a0bda7a`
PR: `elmakus/project_workflow_v2#7`, open/draft/mergeable, exact head/base read back.

Baseline -> candidate is exactly two commits and two added files:
- `tools/adoption_contract.py`
- `tests/test_adoption_contract.py`

No existing workflow, delivery, migration or package file changed in this slice. Therefore prior exact M01-M06 deterministic/live evidence is compatible unless a live scenario below is independently required by PWV2-P2 for final M07 qualification.

## Exact automated verification

GitHub Actions on the exact candidate:
- push run `35858945879`, job `107174118383`: completed/success;
- pull-request run `35858978373`, job `107174227215`: completed/success.

The PR-run log proves:
- package bootstrap shell probes: PASS;
- state suite: 28/28;
- router suite: 39/39;
- execution suite: 4/4;
- review suite: PASS;
- recovery suite: 2/2;
- selected close/fork/delivery/migration group: 80/80;
- full unittest discovery: 161/161;
- compileall, diff-check and clean-tree checks completed within successful `scripts/test.sh`;
- repository baseline checks: PASS.

The one deterministic gap found during M07.P1 was the accepted §4/§8 **interrupted construction-custody transfer** contract. The candidate now contains a production helper plus seven focused regressions proving: explicit adoption authorization, verified-package staging while V1 remains sole owner, exact terminal-handoff binding, interruption recovery without reactivating V1, exactly one final live owner, rejection of dual mutable ownership, and rejection of destination activation before the terminal handoff.

## A01-A17 reconciliation

| ID | Implemented acceptance evidence on/compatible with this candidate |
| --- | --- |
| A01 | `tests/test_chatgpt_delivery.py`, `tests/test_codex_delivery.py`; M05-T01/T02/T03/T05 + M05 target-integration evidence. Thin bootstrap/read sets and package-root containment are exercised directly. |
| A02 | `tests/test_state_contract.py` prohibited state keys; `tests/test_router.py` legacy-policy/binding negatives; M06 migration regressions. New normal state rejects V1 policy/runtime/scheduler/Context-Health surfaces. |
| A03 | state/router wrong workstream, branch, class, missing/cross-workstream/path-escape tests; M01 state/router acceptance. |
| A04 | state one-active-Card enforcement plus execution delegated/direct semantic-result tests. Runtime topology never becomes extra Cards/shared writers. |
| A05 | router durable-result reconciliation-without-replay; M06 apply/restart/source-disappearance recovery. |
| A06 | close external-effect readback-before-retry and uncertain fail-closed cases; M06 apply uncertain-effect regression. |
| A07 | state exact review + append-only history; router changed-result/new-attempt cases; M06 RED->GREEN/pending review preservation. |
| A08 | close target-SHA movement and stronger-coverage reuse tests with affected compatibility GREEN. |
| A09 | close changed content/behavior/new acceptance tests require new review subject. |
| A10 | close target-side recovery/auto-delete/exact-head cleanup/absence-readback tests; actual M05 and M06 target integrations both recovered after GitHub auto-deleted the merged source branch. |
| A11 | stable Task Card parser + JIT trigger tests; router technical-contract/JIT-refinement cases. |
| A12 | prohibited canonical complexity/state fields; selective technical-contract loading and accepted YAGNI authority from M01/M03 evidence. |
| A13 | state Research regression requires proportional official/upstream, project/runtime, tracker/discussion and practitioner/community accounting with weight/conflict/limitations; M02-T02 evidence. |
| A14 | tracker state/correlation validation plus router duplicate/ambiguity/create-readback cases; M02/M04 tracker evidence. |
| A15 | complete `test_v1_migration.py`, `test_migration_apply.py`, `test_migration_rehearsal.py`; M06-T01..T05 and rehearsal evidence. |
| A16 | `test_fork_release_contract.py` proves trigger-only loading, numeric lanes/tuples, immutable history and exact optional alias artifact identity. |
| A17 | accepted `brainstorming/V1_TO_V2_COVERAGE_MATRIX.md` at blob `aafd4a916ae11f8a3ff0c6edb799d8ced996a4bf`: 97 rows classified, 0 OPEN; M06-T04/T05 regression. Candidate changes only custody helper/test, so the matrix-owned production surfaces are unchanged. |

## Supplemental deterministic cases

All additional deterministic cases explicitly required by PWV2-P2 §6.1 are represented:
- issue alignment/promotion and read-only diagnosis boundary: state/router Intake tests + M02 evidence;
- premium A/B/C and material replan: state/router planning/plan-review tests + M02/M05 P2 evidence;
- end-of-scope versus role completion: close/router continuation tests;
- authorization before live writes: close explicit-authorization-gate tests;
- stacked dependencies: close stacked-path tests + M06 rehearsal preservation;
- source-head movement before cleanup: exact-head `safe_to_delete` regression;
- Research return crash points / once-only reconciliation: state `pending/applied/consumed` validation, router implementation-Research return/cleanup cases and `workflow/RESEARCH.md` consume-only contract;
- package missing authority/trust/path containment: Codex missing/malformed router, root mismatch and path-escape tests;
- custody-transfer interruption: new `tools/adoption_contract.py` + seven `tests/test_adoption_contract.py` cases on this exact candidate.

No second test-only workflow interpreter was introduced.

## PWV2-REQ-001..076 concrete evidence map

Evidence groups used below:
- **CORE** — M01 cumulative/integration evidence + current state/router tests.
- **PREEXEC** — M02 cumulative/integration evidence + current Intake/Brainstorming/Research/Definition/Planning/tracker state/router tests.
- **EXEC** — M03 cumulative/integration evidence + current execution/review/recovery/state/router tests.
- **CLOSE** — M04 cumulative/integration evidence + current close/fork tests + actual M05/M06 integration readback.
- **DELIVERY** — M05-T01..T05/integration evidence + current ChatGPT/Codex delivery tests.
- **MIG** — M06-T01..T05/integration evidence + current migration suites.
- **M07-AUTO** — this exact candidate, the two successful Actions runs and custody/adoption regressions.

| Requirements | Concrete evidence |
| --- | --- |
| 001-004 | CORE |
| 005 | EXEC + DELIVERY; mandatory full live L06 remains in the real-surface ledger |
| 006 | CORE + EXEC |
| 007-016 | DELIVERY + CORE; full ordinary model-backed L04 continuation remains separately mandatory where noted by PWV2-P2 |
| 017-023 | CORE + EXEC + CLOSE |
| 024-027 | EXEC; actual capable topology remains additionally required by L08 before production acceptance |
| 028-031 | EXEC |
| 032-033 | CLOSE + MIG |
| 034-038 | EXEC + CLOSE; final exact M07 integration review remains a later M07 gate |
| 039-045 | PREEXEC; actual premium-context L07 remains mandatory |
| 046-050 | PREEXEC |
| 051-052 | CORE + EXEC |
| 053-058 | PREEXEC + M05 real L01/L02 evidence |
| 059-060 | CLOSE deterministic contract; full real L03 final-PR/default-branch tracker close/readback remains mandatory |
| 061-066 | CLOSE + MIG |
| 067-071 | CORE + EXEC + CLOSE + DELIVERY; live L07/L09 observations remain where PWV2-P2 explicitly requires them |
| 072 | MIG |
| 073 | CLOSE |
| 074 | M07-AUTO + all groups above; every deterministic suite is automated and GREEN |
| 075 | EXEC semantic/topology contracts exist, but mandatory actual V2 L08 + L09 remain open and cannot be replaced by automation |
| 076 | MIG + A17 97-row/0-OPEN reconciliation |

This mapping contains an actual implementation/test/evidence owner for every requirement; no requirement uses the Master Plan alone as acceptance evidence. Where PWV2-P2 independently mandates an actual product/runtime observation, the deterministic implementation evidence is explicitly **not** promoted into a live PASS.

## V1 salvage / DROP reconciliation

M06's exact A17 evidence reconciled all 97 accepted source rows with zero OPEN rows, including the standalone explicit-drop checklist. The current M07 candidate changes neither `workflow/`, delivery bootstrap nor migration semantics, so that exact row-by-row disposition remains compatible. The current full test run also re-executes the negative state/router/delivery/migration surfaces that prevent dropped V1 semantics from becoming positive normal routes.

## Real-surface obligations still mandatory

The following are intentionally **not GREEN** from M07-T01 and block first-production acceptance until executed against the exact compatible/final candidate:

1. **L03 full** — final scope-completing default-branch PR/tracker linkage, post-merge Issue readback and accepted-completion-only fallback close.
2. **L04 full ordinary model-backed completion** — actual installed `$pw:project_workflow_v2` semantic continuation beyond the already-GREEN M05 delivery/bootstrap mechanics.
3. **L06** — same workstream ChatGPT -> Codex -> ChatGPT with no state conversion and completed-result reuse.
4. **L07** — actual premium A -> best-context Planning -> B fresh review -> GREEN -> C lighter-context path, including recovery at gates.
5. **L08** — actual V2 N-CAPABLE RED S1 -> bounded delegated correction S2 -> independent GREEN -> same-invocation finalization.
6. **L09** — actual V2 N-CHATGPT: fresh reviewer RED -> same-chat authorized correction -> freeze S2 -> new fresh-context stop -> GREEN -> same-chat finalization.

L01, L02 and L05 were already GREEN in M05. The only candidate changes since the integrated M06 baseline are the isolated custody helper and its tests, so those M05 live observations are compatibility-reused without claiming any of the still-missing L03/L04/L06-L09 portions.

## M07-T01 verdict

GREEN. The automated M07.P1 acceptance surface has no remaining identified deterministic gap on `15978113e46abc8498ceaef594461c8613fcadb8` / tree `f05d86d72f9bbe941583b4ccf92e2c46b5decf83`. The next legal work is JIT live qualification from the explicit real-surface ledger. Production adoption/custody mutation remains unauthorized and untouched.
