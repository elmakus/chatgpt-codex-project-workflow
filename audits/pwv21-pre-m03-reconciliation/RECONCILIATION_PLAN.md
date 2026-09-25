# PWv2.1 Pre-M03 Reconciliation Plan

## Source and scope

- Source harvest repository: `elmakus/chatgpt-codex-project-workflow`
- Source harvest branch: `audit/pwv21-pre-m03-bug-harvest`
- Exact completed harvest HEAD: `7ff23a18e6966ece83eaf8bda45c8923e49791e8`
- Original terminal items: **30**
- Confirmed material: **28**
- Rejected / no repair: **2** (`H011`, `H013`)
- Resulting semantic repair families: **17**
- Family classifications: **1 MUST_RECONCILE_BEFORE_M03 / 7 CAN_DEFER / 9 REQUIRES_CHECKPOINT_READBACK**
- Product repair performed in this reconciliation workspace: **no**

## Reconciliation rule used

PWV21-REQ-122..127 are applied as the boundary rule: classify each live finding before authority mutation; reconcile only findings that materially affect the next downstream authority/topology/semantics; keep trackers non-authoritative; never reopen correctly terminal historical Cards/Milestones merely to conform history; preserve the historical failures as regression fixtures; and do not materialize M03 until the corrected authority plus required Planning/review gates are complete. M03 is the first intended downstream live consumer of the corrected M02R semantics.

A historical or frozen-candidate persistence check is not treated as proof that the future checkpoint implementation still contains the defect. Every family whose final applicability depends on that then-current implementation is therefore classified `REQUIRES_CHECKPOINT_READBACK`.

## Repair-family summary

| Family | Members | Ownership | M03 material | Classification | Proposed corrective Card boundary |
|---|---|---|---:|---|---|
| RF001 | H001, H004, H025 | `canonical_pw_v2` | yes | `REQUIRES_CHECKPOINT_READBACK` | One narrow Card for Task Board cross-field coherence plus blocker/result/review-first routing. Do not fold review-contract redesign into this Card. |
| RF002 | H002, H022 | `canonical_pw_v2` | no | `CAN_DEFER` | One Brainstorm→Definition lifecycle Card: enforce promoted state and explicit-stop precedence at the cross-record routing boundary. |
| RF003 | H003 | `canonical_pw_v2` | no | `CAN_DEFER` | One router-precedence Card that evaluates the owning boundary before generic Research dispatch and preserves exact Research return ownership. |
| RF004 | H005, H006 | `cross_cutting` | yes | `REQUIRES_CHECKPOINT_READBACK` | One exact-acceptance-binding Card spanning implementation review and Plan Review, using the same canonical exact-authority key/readback contract rather than two unrelated ad hoc checks. |
| RF005 | H007 | `canonical_pw_v2` | yes | `REQUIRES_CHECKPOINT_READBACK` | One Plan Review state-domain Card: narrow validation or exhaustively route pending/green/red and fail closed for every other state. |
| RF006 | H008, H009, H018 | `cross_cutting` | yes | `REQUIRES_CHECKPOINT_READBACK` | One review-history identity/completeness Card: establish immutable attempt identity, durable legacy provenance, and append-only complete history readback consumed by Final observation reconciliation. |
| RF007 | H010, H020, H029 | `cross_cutting` | yes | `REQUIRES_CHECKPOINT_READBACK` | One reusable locator/readback foundation Card: resolve existence, semantic root and exact Git object identity before any consumer treats a locator/declaration as workflow proof. |
| RF008 | H012 | `authority_decision` | yes | `MUST_RECONCILE_BEFORE_M03` | Do not create an implementation Card first. Return the proof rule to Definition/Planning, accept the durable old/new-subject classification mechanism, then materialize one narrow enforcement Card if implementation work remains. |
| RF009 | H014, H016 | `canonical_pw_v2` | no | `CAN_DEFER` | One Research referential-integrity Card: exact origin↔return-target binding plus exact prior-art-result provenance consumed by Intake/Board owners. |
| RF010 | H015 | `canonical_pw_v2` | no | `CAN_DEFER` | One Intake issue-lifecycle Card: gate issue_alignment on a concrete repair subject plus completed exact diagnosis/prior-art proof. |
| RF011 | H017, H019 | `cross_cutting` | no | `CAN_DEFER` | One Close/Recovery proof-derivation Card: derive the mandatory package and cleanup proof from durable state using exact readback; remove self-attested completeness inputs from authority decisions. |
| RF012 | H021 | `canonical_pw_v2` | yes | `REQUIRES_CHECKPOINT_READBACK` | One Definition→Planning freshness Card using a durable exact authority key shared by Planning, Plan Review and router freshness checks. |
| RF013 | H023, H024 | `canonical_pw_v2` | yes | `REQUIRES_CHECKPOINT_READBACK` | One execution/result semantic-validation Card: validate the stable Card before recovered Execution and use a structured success predicate before a Result can authorize reconciliation/review/no-replay recovery. |
| RF014 | H026 | `canonical_pw_v2` | yes | `REQUIRES_CHECKPOINT_READBACK` | One JIT-terminality Card: make pending/satisfied JIT obligations part of terminal completeness and require exact consumed-by/materialized-downstream binding. |
| RF015 | H027 | `canonical_pw_v2` | no | `CAN_DEFER` | One Close-composition Card that gives the selector durable Close-completion input/readback and emits end_of_scope_stop/USER_STOP when the oracle says true end. |
| RF016 | H028 | `canonical_pw_v2` | no | `CAN_DEFER` | One delivery-integrity Card for SessionStart canonical-router verification and marker-preserving corruption tests; keep workflow semantics in the router, not the bootstrap. |
| RF017 | H030 | `canonical_pw_v2` | yes | `REQUIRES_CHECKPOINT_READBACK` | One parser-normalization Card: normalize TOML decode failures at the durable-state read boundary (or exhaustively catch them) so every selector-owned TOML surface returns deterministic Recovery. |

## Complete Hxxx → repair-family mapping

| Finding | Mapping | Classification |
|---|---|---|
| H001 | RF001 | `REQUIRES_CHECKPOINT_READBACK` |
| H002 | RF002 | `CAN_DEFER` |
| H003 | RF003 | `CAN_DEFER` |
| H004 | RF001 | `REQUIRES_CHECKPOINT_READBACK` |
| H005 | RF004 | `REQUIRES_CHECKPOINT_READBACK` |
| H006 | RF004 | `REQUIRES_CHECKPOINT_READBACK` |
| H007 | RF005 | `REQUIRES_CHECKPOINT_READBACK` |
| H008 | RF006 | `REQUIRES_CHECKPOINT_READBACK` |
| H009 | RF006 | `REQUIRES_CHECKPOINT_READBACK` |
| H010 | RF007 | `REQUIRES_CHECKPOINT_READBACK` |
| H011 | REJECTED / NO_REPAIR | `NO_REPAIR` |
| H012 | RF008 | `MUST_RECONCILE_BEFORE_M03` |
| H013 | REJECTED / NO_REPAIR | `NO_REPAIR` |
| H014 | RF009 | `CAN_DEFER` |
| H015 | RF010 | `CAN_DEFER` |
| H016 | RF009 | `CAN_DEFER` |
| H017 | RF011 | `CAN_DEFER` |
| H018 | RF006 | `REQUIRES_CHECKPOINT_READBACK` |
| H019 | RF011 | `CAN_DEFER` |
| H020 | RF007 | `REQUIRES_CHECKPOINT_READBACK` |
| H021 | RF012 | `REQUIRES_CHECKPOINT_READBACK` |
| H022 | RF002 | `CAN_DEFER` |
| H023 | RF013 | `REQUIRES_CHECKPOINT_READBACK` |
| H024 | RF013 | `REQUIRES_CHECKPOINT_READBACK` |
| H025 | RF001 | `REQUIRES_CHECKPOINT_READBACK` |
| H026 | RF014 | `REQUIRES_CHECKPOINT_READBACK` |
| H027 | RF015 | `CAN_DEFER` |
| H028 | RF016 | `CAN_DEFER` |
| H029 | RF007 | `REQUIRES_CHECKPOINT_READBACK` |
| H030 | RF017 | `REQUIRES_CHECKPOINT_READBACK` |

Coverage check: every H001-H030 appears exactly once; all 28 confirmed findings are members of exactly one repair family; H011 and H013 remain REJECTED / NO_REPAIR.

## Pre-M03 relevance classification

- **MUST_RECONCILE_BEFORE_M03:** H012. This is an accepted-authority/proof ambiguity on the Planning/Plan Review gate and must return to Definition/Planning before implementation chooses a proof mechanism.
- **REQUIRES_CHECKPOINT_READBACK:** H001, H004, H025, H005, H006, H007, H008, H009, H018, H010, H020, H029, H021, H023, H024, H026, H030. These findings map to M03's Git-alone recovery, portability, stale-result, review-boundary, JIT or fail-closed acceptance surfaces, but the harvest snapshots are not current-state proof.
- **CAN_DEFER:** H002, H022, H003, H014, H016, H015, H017, H019, H027, H028. These map to already-passed Brainstorm/Intake/Research surfaces or to M06/M07 runtime/Close cleanup surfaces and therefore are not made M03 blockers merely because they exist.

## Dependency order if corrective work is activated

1. **Authority first:** RF008. Resolve the editorial-exemption proof rule in Definition/Planning before any implementation Card is authored for it.
2. **Foundational truth/readback and fail-closed primitives:** RF007, RF005, RF017; RF002/RF016 may be handled independently when their deferred stages are reached.
3. **Freshness and semantic contract layers:** RF012, RF013, RF009.
4. **Review and owner binding:** RF004 after RF007+RF012; RF006 after RF007; RF003 after RF009; RF010 after RF009.
5. **Card/JIT coherence:** RF001 after RF004+RF006+RF007; RF014 after RF001+RF013.
6. **Later Close/Recovery integration:** RF011 after RF006+RF007; RF015 after RF011+RF014.

## Proposed corrective Card boundaries and proof

### RF001 — Card status must not outrank durable blocker/result/review truth

**Members:** H001, H004, H025  
**Violated invariant:** Task Board status is a derived lifecycle projection. It must not contradict or override a real blocker, a durable Card Result, or required exact review proof; durable blocker/result/review truth has routing precedence.  
**Affected surfaces:** `workflow/STATE.md`, `workflow/EXECUTION.md`, `workflow/REVIEW.md`, `TASK_BOARD`, `tools/state_contract.py::validate_board`, `tools/router.py Card routing`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** RF004, RF006, RF007  
**M03 materiality:** yes — Directly affects M03 stale-result, recovery, and no-replay parity fixtures. The harvest only proves persistence at frozen candidate snapshots, so the future M02R→M03 checkpoint must read back the then-current implementation before opening repair.  
**Classification:** `REQUIRES_CHECKPOINT_READBACK`  
**Smallest coherent corrective Card boundary:** One narrow Card for Task Board cross-field coherence plus blocker/result/review-first routing. Do not fold review-contract redesign into this Card.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- in_progress + human_authority blocker must fail closed or route the real user stop, never ordinary Execution
- done without a valid Result and required exact GREEN review must be rejected/recovered
- ready/blocked/planned + durable Result must reconcile from durable truth or fail closed, never replay implementation
- positive controls preserve ordinary READY-without-result and valid reviewed DONE flows

### RF002 — Brainstorm owner state must govern downstream Definition entry

**Members:** H002, H022  
**Violated invariant:** A durable Brainstorm explicit stop remains authoritative, and Definition may consume only the exact Brainstorm revision that is durably promoted as well as promotion-authorized.  
**Affected surfaces:** `workflow/BRAINSTORMING.md`, `workflow/DEFINITION.md`, `workflow/USER_STOP.md`, `tools/state_contract.py::validate_brainstorm`, `tools/router.py Brainstorm→Definition routing`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** none  
**M03 materiality:** no — The current PWv2.1 workstream is already past Brainstorm/Definition and REQ-125 forbids reopening correctly terminal history merely to conform it. M03 does not intentionally consume a new Brainstorm transition.  
**Classification:** `CAN_DEFER`  
**Smallest coherent corrective Card boundary:** One Brainstorm→Definition lifecycle Card: enforce promoted state and explicit-stop precedence at the cross-record routing boundary.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- explicit_user_stop plus otherwise-valid downstream Definition/Planning/Board must still stop
- active or ready_for_definition plus exact promotion authorization must not authorize Definition
- durably promoted exact revision with cleared/no stop remains a legal Definition source

### RF003 — Generic Research dispatch must not preempt the owning workflow boundary

**Members:** H003  
**Violated invariant:** Research is non-authoritative and must return to its exact owner; generic Research routing cannot outrun a higher-precedence explicit/premium stop, Intake obligation, result reconciliation, or Board-owned continuation.  
**Affected surfaces:** `workflow/RESEARCH.md`, `workflow/ROUTER.md`, `workflow/INTAKE.md`, `workflow/DEFINITION.md`, `Task Board Research continuation`, `tools/router.py`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** RF009  
**M03 materiality:** no — P6 M03 does not require a Research transition as part of its defined JIT/acceptance surface. Keep as durable regression debt unless the future checkpoint discovers that M03 itself has acquired a Research dependency.  
**Classification:** `CAN_DEFER`  
**Smallest coherent corrective Card boundary:** One router-precedence Card that evaluates the owning boundary before generic Research dispatch and preserves exact Research return ownership.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- active Research plus due premium/explicit stop must honor the owner stop
- unrelated Research must not bypass Intake diagnosis/alignment ownership
- Board-bound Research must return to its exact owning continuation
- ordinary active Research remains routable when no higher-precedence owner boundary exists

### RF004 — GREEN review must bind the exact current acceptance authority

**Members:** H005, H006  
**Violated invariant:** A GREEN review is reusable only for the exact current acceptance surface: implementation review must bind the selected stable Task Card contract, and Plan Review must bind the current Definition/requirements/decisions authority rather than any merely well-shaped path.  
**Affected surfaces:** `workflow/REVIEW.md`, `workflow/PLAN_REVIEW.md`, `templates/TASK_CARD.md`, `DEFINITION.toml`, `PLANNING.toml`, `tools/state_contract.py review validators`, `tools/router.py review consumption`  
**Likely ownership:** `cross_cutting`  
**Dependencies:** RF007, RF012  
**M03 materiality:** yes — M03 is the first authority-level dogfood and explicitly exercises fresh-review boundaries/shadow replay. Final applicability still depends on the then-current candidate implementation, so read back before creating corrective work.  
**Classification:** `REQUIRES_CHECKPOINT_READBACK`  
**Smallest coherent corrective Card boundary:** One exact-acceptance-binding Card spanning implementation review and Plan Review, using the same canonical exact-authority key/readback contract rather than two unrelated ad hoc checks.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- same Card ID at an alternate acceptance path must not inherit GREEN
- same-path Task Card acceptance/test mutation must stale prior GREEN
- Plan Review acceptance path outside the current Definition authority set must reject
- exact current Task Card and exact current Definition authority positive cases remain GREEN-consumable

### RF005 — Plan Review verdict domain must be closed and exhaustively routed

**Members:** H007  
**Violated invariant:** Only canonical Plan Review lifecycle verdicts may be consumed, and RED semantics may be assigned only to an explicit RED terminal verdict; unsupported shared-review states must not fall through as RED.  
**Affected surfaces:** `workflow/PLAN_REVIEW.md`, `tools/state_contract.py::validate_plan_review`, `shared review validator`, `policy/mechanical_policy.json`, `tools/router.py Planning correction path`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** none  
**M03 materiality:** yes — A pre-M03 reconciliation may itself require Planning/Plan Review, and M03 exercises review boundaries. Because the active implementation may have changed since the harvest snapshot, this is a checkpoint-readback item.  
**Classification:** `REQUIRES_CHECKPOINT_READBACK`  
**Smallest coherent corrective Card boundary:** One Plan Review state-domain Card: narrow validation or exhaustively route pending/green/red and fail closed for every other state.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- pending routes to Plan Review
- green routes to GREEN consumption
- red routes to RED correction
- in_progress or any unsupported verdict never receives RED authority and fails closed or follows an explicitly authorized active-review path

### RF006 — Review history must be immutable, provenance-backed, and complete

**Members:** H008, H009, H018  
**Violated invariant:** Review history is append-only durable truth: terminal attempts cannot be rewritten, legacy treatment must be proven by durable historicity rather than schema shape, and current Board locators cannot truncate previously durable attempts/observations from canonical history.  
**Affected surfaces:** `workflow/REVIEW.md`, `Task Board review_attempts`, `tools/state_contract.py::validate_review_history`, `tools/router.py review loading`, `tools/close_contract.py observation reconciliation`, `M02R review/observation closure`  
**Likely ownership:** `cross_cutting`  
**Dependencies:** RF007  
**M03 materiality:** yes — M02R review convergence and durable observation closure are explicit prerequisites for M03 dogfood. Persistence was proved only at frozen candidate snapshots, so the future checkpoint must verify the current history implementation before repair.  
**Classification:** `REQUIRES_CHECKPOINT_READBACK`  
**Smallest coherent corrective Card boundary:** One review-history identity/completeness Card: establish immutable attempt identity, durable legacy provenance, and append-only complete history readback consumed by Final observation reconciliation.  
**Authority ambiguity:** If accepted authority does not already define a durable legacy cutoff/provenance representation, that choice must return to Definition/Planning; implementation must not invent a historical cutoff.

Regression/evidence that should prove repair:
- newly authored legacy-shaped R01 RED cannot manufacture historical exemption
- terminal R01 RED rewritten in place to GREEN is rejected; R01 RED + appended valid R02 GREEN is legal
- removing a previously durable R01 locator from the current Board cannot make its open observation disappear
- genuinely migrated historical attempt with authorized durable provenance remains compatible

### RF007 — A locator is not proof until the actual target is resolved and identity-checked

**Members:** H010, H020, H029  
**Violated invariant:** Workflow proof locators must resolve to real bytes that still satisfy their semantic class/workstream confinement and, when an immutable Git subject is declared, match the exact repository/commit/path/blob identity actually consumed.  
**Affected surfaces:** `locator validation`, `tools/router.py Reads`, `tools/execution_contract.py evidence refs`, `READY dependency refresh`, `Git exact-subject readback`, `filesystem semantic-root confinement`  
**Likely ownership:** `cross_cutting`  
**Dependencies:** none  
**M03 materiality:** yes — This is directly on M03's Git-alone recovery, portability, stale-result and evidence-locking acceptance path. The future checkpoint must test the then-current resolver/readback behavior rather than assume the older snapshot still applies.  
**Classification:** `REQUIRES_CHECKPOINT_READBACK`  
**Smallest coherent corrective Card boundary:** One reusable locator/readback foundation Card: resolve existence, semantic root and exact Git object identity before any consumer treats a locator/declaration as workflow proof.  
**Authority ambiguity:** none; the serialization/helper choice may remain an implementation detail under accepted exact-subject and fail-closed semantics.

Regression/evidence that should prove repair:
- dangling result/review/observation evidence locator fails before consumption
- same-path dependency bytes changed while commit/blob declarations stay unchanged fails READY refresh
- authority/Card symlink resolving outside its declared semantic root fails before bytes are consumed
- Windows-style backslash traversal is rejected under supported host semantics
- positive exact target/readback cases remain accepted

### RF008 — editorial_exempt needs authority-owned proof, not self-attestation

**Members:** H012  
**Violated invariant:** Plan Review may be skipped only for a genuinely editorial/mechanical change that preserves strategy, milestone structure, requirement coverage and accepted gates, with proof bound to the exact prior and changed plan subjects.  
**Affected surfaces:** `workflow/PLANNING.md`, `workflow/PLAN_REVIEW.md`, `Planning authority`, `editorial_exempt validation`  
**Likely ownership:** `authority_decision`  
**Dependencies:** none  
**M03 materiality:** yes — REQ-127 requires corrected authority and Planning/review gates before M03 is materialized. This is therefore the one unconditional pre-M03 authority reconciliation family in this package.  
**Classification:** `MUST_RECONCILE_BEFORE_M03`  
**Smallest coherent corrective Card boundary:** Do not create an implementation Card first. Return the proof rule to Definition/Planning, accept the durable old/new-subject classification mechanism, then materialize one narrow enforcement Card if implementation work remains.  
**Authority ambiguity:** Authority ambiguity is material: the accepted semantics define what may be exempt but do not select the durable proof mechanism. That mechanism must be accepted by Definition/Planning rather than silently chosen by implementation.

Regression/evidence that should prove repair:
- pure editorial change with accepted durable classification bound to exact old/new subjects may reuse the prior review
- strategy/milestone/requirement/gate change must force a new material Planning/Plan Review cycle
- new plan blob plus only self-authored 'wording only' prose must fail closed
- stale or unbound exemption proof must fail closed

### RF009 — Research provenance and return ownership must be exact

**Members:** H014, H016  
**Violated invariant:** A Research result must be durably bound to its exact origin role/subject and exact return owner, and Intake prior-art completion must reference the actual consumed/applied Research result rather than an arbitrary non-empty string.  
**Affected surfaces:** `workflow/RESEARCH.md`, `workflow/INTAKE.md`, `RESEARCH.toml`, `INTAKE.toml`, `Task Board Research ownership`, `tools/state_contract.py`, `tools/router.py`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** RF007  
**M03 materiality:** no — The accepted M03 plan does not require Research as part of its materialization or acceptance path. Preserve these failures as regression debt and reconcile before the first downstream stage that actually consumes the affected Research flows.  
**Classification:** `CAN_DEFER`  
**Smallest coherent corrective Card boundary:** One Research referential-integrity Card: exact origin↔return-target binding plus exact prior-art-result provenance consumed by Intake/Board owners.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- origin subject and return target pointing at a different/nonexistent Card fails closed
- forged diagnosis_prior_art_result without matching applied Research result is rejected
- completed Research returns only to the exact durable owner and exact result binding

### RF010 — Issue alignment cannot precede a concrete repair subject

**Members:** H015  
**Violated invariant:** Issue Intake remains diagnosis-owned until a concrete repair outcome/subject exists and required pre-repair diagnosis obligations are complete; an empty repair subject cannot become a human alignment stop.  
**Affected surfaces:** `workflow/INTAKE.md`, `INTAKE.toml`, `tools/router.py issue_alignment`, `workflow/USER_STOP.md`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** RF009  
**M03 materiality:** no — M03 is continuation of an already-defined change workstream, not a new issue-intake flow. REQ-123 therefore does not make this an M03 blocker.  
**Classification:** `CAN_DEFER`  
**Smallest coherent corrective Card boundary:** One Intake issue-lifecycle Card: gate issue_alignment on a concrete repair subject plus completed exact diagnosis/prior-art proof.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- pending issue alignment with empty repair_subject remains in Intake diagnosis and does not stop the user
- concrete repair subject with incomplete prior-art proof remains in Intake
- concrete subject plus completed exact diagnosis proof may reach the authorized alignment stop

### RF011 — Recovery/cleanup completion proof must be derived, not caller-attested

**Members:** H017, H019  
**Violated invariant:** Recovery and Final cleanup completeness must be established from the canonical mandatory durable package and exact cleanup subject/evidence/independent review, never from caller-supplied empty required sets, shape-only identities, non-empty strings or booleans.  
**Affected surfaces:** `workflow/RECOVERY.md`, `workflow/CLOSE.md`, `tools/close_contract.py recovery verification`, `cleanup-work validation`, `Final reconciliation`  
**Likely ownership:** `cross_cutting`  
**Dependencies:** RF006, RF007  
**M03 materiality:** no — These findings sit on source-ref cleanup/Final completion surfaces planned for M07, not M03's disposable runtime/helper-state recovery. They should not block M03 merely because they exist.  
**Classification:** `CAN_DEFER`  
**Smallest coherent corrective Card boundary:** One Close/Recovery proof-derivation Card: derive the mandatory package and cleanup proof from durable state using exact readback; remove self-attested completeness inputs from authority decisions.  
**Authority ambiguity:** If the accepted recovery authority does not fully enumerate the mandatory source-ref-independent package, that package definition must return to Definition/Planning before implementation fills the gap.

Regression/evidence that should prove repair:
- required_artifacts=[] and present_artifacts=[] cannot certify source-ref-independent recovery
- fabricated 40-hex cleanup subject, dangling evidence and independent_review_green=true cannot unblock Final
- real cleanup subject + real evidence + exact independent GREEN review + correct candidate coverage succeeds

### RF012 — Planning must be fresh to the current Definition authority

**Members:** H021  
**Violated invariant:** An approved Planning/Plan Review/premium chain may be reused only when its entry authority exactly matches the current Definition revision and accepted requirements/decision authority; upstream Definition change makes the old cycle stale.  
**Affected surfaces:** `DEFINITION.toml`, `PLANNING.toml`, `PLAN_REVIEW.toml`, `tools/state_contract.py Definition/Planning validators`, `tools/router.py Planning entry/freshness`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** RF007  
**M03 materiality:** yes — M03 materialization must be governed by the corrected current Definition/Planning authority. The future checkpoint must verify whether the current candidate already has this freshness binding.  
**Classification:** `REQUIRES_CHECKPOINT_READBACK`  
**Smallest coherent corrective Card boundary:** One Definition→Planning freshness Card using a durable exact authority key shared by Planning, Plan Review and router freshness checks.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- valid R1 Definition + approved R1 Planning baseline remains executable
- change only current Definition to R2 while old Planning stays internally valid -> fail closed/re-enter Planning
- change accepted requirements/decision authority under the current Definition key -> stale old Planning
- new Planning/review/premium cycle bound to the new exact Definition authority becomes legal

### RF013 — Execution authority and Card Result require semantic validity, not mere presence

**Members:** H023, H024  
**Violated invariant:** Execution may start only from a valid stable Task Card contract, and a durable Card Result may become recovery truth only after semantically successful tests/readback and the rest of the accepted result contract; readability or non-empty prose is insufficient.  
**Affected surfaces:** `templates/TASK_CARD.md`, `templates/CARD_RESULT.md`, `tools/state_contract.py::parse_task_card`, `tools/execution_contract.py::parse_card_result`, `workflow/EXECUTION.md`, `workflow/EXECUTION_PREP.md`, `tools/router.py active/result branches`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** RF007  
**M03 materiality:** yes — M03 explicitly revalidates M01/M02 outputs, exercises stale results and helper-less recovery, and requires Git state alone to reconstruct the legal continuation. Current implementation applicability must be read back.  
**Classification:** `REQUIRES_CHECKPOINT_READBACK`  
**Smallest coherent corrective Card boundary:** One execution/result semantic-validation Card: validate the stable Card before recovered Execution and use a structured success predicate before a Result can authorize reconciliation/review/no-replay recovery.  
**Authority ambiguity:** No policy change is required if a machine-readable success representation can be introduced without changing accepted semantics; do not use substring heuristics as a substitute for a structured contract.

Regression/evidence that should prove repair:
- active result-less malformed/truncated Task Card routes Recovery, never Execution
- Card Result with explicit failed tests/readback cannot route result_reconciliation/review/finalization
- complete stable Card + successful structured result preserves normal Execution and result reconciliation
- retain separate exact-subject/evidence-readback regressions from RF007

### RF014 — JIT lifecycle must participate in terminality and prove materialization

**Members:** H026  
**Violated invariant:** A satisfied JIT trigger is an already-authorized Execution Prep obligation and therefore prevents Close; a consumed trigger must carry exact proof of the downstream Card/materialization that consumed it.  
**Affected surfaces:** `workflow/EXECUTION_PREP.md`, `Task Board JIT records`, `tools/state_contract.py::validate_board`, `policy/mechanical_policy.json PWV21-K012`, `tools/policy_kernel.py board_all_cards_done`, `tools/router.py terminal dispatch`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** RF001, RF013  
**M03 materiality:** yes — M03 is explicitly the first downstream JIT dogfood of the R2+R3 decomposition rules, so this family materially affects the M02R→M03 boundary if it still exists. Read back the then-current candidate before repair.  
**Classification:** `REQUIRES_CHECKPOINT_READBACK`  
**Smallest coherent corrective Card boundary:** One JIT-terminality Card: make pending/satisfied JIT obligations part of terminal completeness and require exact consumed-by/materialized-downstream binding.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- all current Cards DONE + satisfied trigger + no downstream Card must not route Close
- consumed trigger without exact downstream materialization evidence fails closed
- exact consumed-by binding plus terminal downstream Cards restores Close eligibility
- all-DONE with no pending JIT obligation remains a valid Close candidate

### RF015 — Close continuation must be connected to the production selector

**Members:** H027  
**Violated invariant:** All Cards DONE routes into Close, but durable approved-scope completion with no next authorized obligation must subsequently produce the real end_of_scope_stop through the production selector and USER_STOP contract rather than loop on Close forever.  
**Affected surfaces:** `workflow/CLOSE.md`, `workflow/ROUTER.md`, `tools/close_contract.py::close_continuation`, `tools/router.py terminal dispatch`, `workflow/USER_STOP.md`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** RF011, RF014  
**M03 materiality:** no — P6 places full Close integration in M07. This should remain regression debt unless an earlier milestone explicitly begins consuming true-end Close semantics.  
**Classification:** `CAN_DEFER`  
**Smallest coherent corrective Card boundary:** One Close-composition Card that gives the selector durable Close-completion input/readback and emits end_of_scope_stop/USER_STOP when the oracle says true end.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- first all-DONE entry routes Close
- after canonical durable Close-completion evidence, re-entry emits stop/end_of_scope_stop and reads USER_STOP
- remaining authorized obligation continues deterministically
- explicit authorization gate produces authorization stop rather than end-of-scope stop

### RF016 — SessionStart must verify canonical router integrity beyond marker strings

**Members:** H028  
**Violated invariant:** The runtime bootstrap may advertise an installed router as canonical only when the installed authority bytes/package identity are valid; preserving two marker strings cannot make semantically destroyed or stale content canonical.  
**Affected surfaces:** `hooks/session-start.py::canonical_router`, `skills/project_workflow_v2/SKILL.md`, `workflow/ROUTER.md delivery`, `SessionStart tests/package integrity`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** none  
**M03 materiality:** no — This is primarily the M06 runtime/handoff delivery surface. M03 acceptance intentionally reconstructs from canonical Git/contracts and does not require SessionStart package certification.  
**Classification:** `CAN_DEFER`  
**Smallest coherent corrective Card boundary:** One delivery-integrity Card for SessionStart canonical-router verification and marker-preserving corruption tests; keep workflow semantics in the router, not the bootstrap.  
**Authority ambiguity:** none; the integrity mechanism is an implementation choice as long as malformed/stale authority fails closed.

Regression/evidence that should prove repair:
- two-marker-only ROUTER.md must produce blocking package error
- marker-preserving contradictory/truncated router must fail
- if digest/manifest identity is used, one-byte mutation fails
- untouched valid installed package remains enabled

### RF017 — Malformed durable TOML must deterministically route Recovery

**Members:** H030  
**Violated invariant:** Syntactically invalid durable workflow state is an invalid binding and must fail closed to Recovery; parser exceptions must never escape the production selector as uncontrolled runtime errors.  
**Affected surfaces:** `tools/state_contract.py::read_toml/read_project`, `tools/router.py exception boundaries`, `workflow/RECOVERY.md`, `all selector-read TOML records`  
**Likely ownership:** `canonical_pw_v2`  
**Dependencies:** none  
**M03 materiality:** yes — M03 requires parity disagreements/invalid canonical state to fail closed to Recovery. Whether this still needs repair must be established against the future current implementation.  
**Classification:** `REQUIRES_CHECKPOINT_READBACK`  
**Smallest coherent corrective Card boundary:** One parser-normalization Card: normalize TOML decode failures at the durable-state read boundary (or exhaustively catch them) so every selector-owned TOML surface returns deterministic Recovery.  
**Authority ambiguity:** none

Regression/evidence that should prove repair:
- malformed WORKSTREAM/Intake/Research/Definition/Planning/Plan Review/TASK_BOARD/review/blocker TOML each returns recovery_boundary instead of raising
- semantic-invalid but syntactically valid TOML keeps the existing ValidationError recovery behavior
- valid TOML control paths are unchanged

## Explicit checkpoint-readback list

H001, H004, H025, H005, H006, H007, H008, H009, H018, H010, H020, H029, H021, H023, H024, H026, H030

At the future audit-reconciliation checkpoint, these families must be checked against the exact then-current PWv2.1 candidate HEAD and current accepted authority. Re-run or reconstruct the smallest negative regression for each family, record whether the class is still applicable, already closed, or partially closed, and only then materialize corrective Cards through the normal workflow. Do not infer persistence from the harvest's older candidate SHAs.

## Historical preservation

H011 and H013 remain terminal rejected findings with no repair authorization. Correctly terminal historical Cards, reviews and milestones are not reopened or rewritten. Historical failures may be replayed only as immutable regression evidence. No corrective Card, PR, merge, product implementation change, canonical workflow-state mutation, or active PWv2.1 workstream mutation was performed by this reconciliation stage.
