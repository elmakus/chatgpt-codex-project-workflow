# Pre-M03 Audit Reconciliation Checkpoint — Applicability Readback

Status: **READBACK COMPLETE, INDEPENDENT REVIEW PENDING.** Fresh independent review of this synthesis is required before any corrective work.
Policy: `QUALITY_FIRST_PRE_M03`. This readback authorizes no repair, no Card, and no scope expansion.

## 1. Exact inputs

| Input | Value |
|---|---|
| Consumer HEAD | `6e47749782cac0cdf01b8e65a95ddf2d5be7c2ec` |
| Consumer Board revision | `104` (`implementation/workstreams/change-pwv21-policy-kernel-brainstorming/TASK_BOARD.toml`, `revision = 104`, read via `HEAD:` object) |
| Candidate | `elmakus/project_workflow_v2@07c724085de591c2a0bb51aaaae0ec23009880bf` |
| Audit package | `e0fdcbf5021f7b50a347edc169beaa8a01eeb58b` on `audit/pwv21-pre-m03-reconciliation` |
| Audit files (read via `git cat-file -p <audit_sha>:<path>`) | `audits/pwv21-pre-m03-reconciliation/HANDOFF.md`, `REPAIR_GROUPS.toml`, `RECONCILIATION_PLAN.md` |
| Current-state probe reports | `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/pre_m03_audit_readback/PROBE_BATCH_01.json`, `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/pre_m03_audit_readback/PROBE_BATCH_02.json`, `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/pre_m03_audit_readback/PROBE_BATCH_03.json`, `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/pre_m03_audit_readback/PROBE_BATCH_04.json` |

All four probe reports agree on the three SHAs, Board rev104, policy `QUALITY_FIRST_PRE_M03`, audit `REPAIR_GROUPS.toml` members, original technical classifications, and dependencies. Reports were reconciled against the audit TOML: 17 unique families, no duplicates, no omissions.

Historical harvest HEAD `7ff23a18e6966ece83eaf8bda45c8923e49791e8` is cited by the audit as source only; it is not used as current-state proof.

## 2. Counts and lists

- Total repair families: **17 / 17** read back.
- Current dispositions: **14 STILL_APPLICABLE**, **3 AUTHORITY_RECONCILIATION_REQUIRED**, **0 SATISFIED_BY_CURRENT_IMPLEMENTATION**, **0 NEEDS_MORE_CURRENT_EVIDENCE**.
- Original technical/downstream classifications (preserved, separate from current applicability): **1 MUST_RECONCILE_BEFORE_M03**, **7 CAN_DEFER**, **9 REQUIRES_CHECKPOINT_READBACK**.

Explicit lists:

- STILL_APPLICABLE (14): `RF001`, `RF002`, `RF003`, `RF004`, `RF005`, `RF007`, `RF009`, `RF010`, `RF012`, `RF013`, `RF014`, `RF015`, `RF016`, `RF017`.
- AUTHORITY_RECONCILIATION_REQUIRED (3): `RF006`, `RF008`, `RF011`. Defects persist, but the durable mechanism/package definition is missing (RF006/RF011) or the family is authority-first (RF008).
- SATISFIED_BY_CURRENT_IMPLEMENTATION (0): none.
- NEEDS_MORE_CURRENT_EVIDENCE (0): none — zero-evidence list is empty; every family has a current probe with observed result and code references.

Original classification map:

- MUST_RECONCILE_BEFORE_M03 (1): `RF008`.
- CAN_DEFER (7): `RF002`, `RF003`, `RF009`, `RF010`, `RF011`, `RF015`, `RF016`.
- REQUIRES_CHECKPOINT_READBACK (9): `RF001`, `RF004`, `RF005`, `RF006`, `RF007`, `RF012`, `RF013`, `RF014`, `RF017`.

Rejected/no-repair `H011`, `H013` remain rejected and are not repair families.

## 3. Dependency-aware order (currently active/authority families: all 17)

Audit `resolution_order` (topological; respects every `depends_on` edge; sequence only, not authorization):

1. `RF008`
2. `RF007`, `RF005`, `RF017`, `RF002`, `RF016`
3. `RF012`, `RF013`, `RF009`, `RF006`
4. `RF004` (after `RF007`+`RF012`), `RF003` (after `RF009`), `RF010` (after `RF009`), `RF011` (after `RF006`+`RF007`)
5. `RF001` (after `RF004`+`RF006`+`RF007`)
6. `RF014` (after `RF001`+`RF013`)
7. `RF015` (after `RF011`+`RF014`)

Linear form: `RF008 → RF007 → RF005 → RF017 → RF002 → RF016 → RF012 → RF013 → RF009 → RF006 → RF004 → RF003 → RF010 → RF011 → RF001 → RF014 → RF015`.

## 4. Authority-readback rule applied

- For `RF004`/`RF005`/`RF012`: one Tester called the canonical semantic rule accepted, but a separate bounded P6 map found **no explicit M02R corrective Card authority**. Recorded below as `M02R corrective authority not established`, with owning surface noted (RF004 general review/M05; RF005 Plan Review/M05; RF012 Definition→Planning freshness/M06). No work is authorized.
- For all other STILL families: the reports' authority analysis is used conservatively (`insufficient` / `not established`; requires explicit pre-M03 authority/replan or separate authorized maintenance).
- `RF008`: no `editorial_exempt` proof is invented. Authority-first handling only.

## 5. Family readback (all 17, exactly once)

Each entry states the concrete mutation and observed output; ephemeral `/tmp` probe-script paths are provenance only, never the sole reproduction evidence.

### RF001 — Card status must not outrank durable blocker/result/review truth

- Members: `H001`, `H004`, `H025`. Technical: `REQUIRES_CHECKPOINT_READBACK`. Disposition: `STILL_APPLICABLE`. Depends on: `RF004`, `RF006`, `RF007`. Source: batch4.
- Probe mutation: disposable copies of `tests/fixtures/router/valid-project`; set `in_progress`+`human_authority` blocker; `done`+result (present file and dangling file) with no review; `ready`/`blocked`/`planned`+result; controls `in_progress`/no-blocker and `ready`/no-result; call `select_route`.
- Observed result: `in_progress`+blocker → `route/execution` (identical to no-blocker positive); active path `tools/router.py:751-873` never reads blocker; `tools/state_contract.py:863-872` permits blocker. `done`+result/no-review (present and dangling) → `route/close`; K012 `tools/policy_kernel.py:81-83` inputs `board.cards` only, `tools/router.py:934-939` reads no result/review; only narrow done-without-locator fails closed (`:850-851`). `ready`+result → `route/execution_prep` launch (`refresh_ready_card :250-303` never checks result); `blocked`+dangling → `research_handoff` ignoring dangling; `planned`+result → `execution_prep` fallback `:1030`. Positives preserved; 99 tests pass; no closing test.
- Likely future repair boundary: one narrow Card for Task Board cross-field coherence plus blocker/result/review-first routing; no review-contract redesign; after `RF004`/`RF006`/`RF007`.
- Accepted-M02R authority: insufficient — no accepted REQ or BOOT-A/B/C/D seam covers Board cross-field coherence or blocker/result/review-first routing; P6 M02R scope is review convergence, decomposition fidelity, live-validation, Worker discipline. Requires explicit pre-M03 authority/replan or separate maintenance.

### RF002 — Brainstorm owner state must govern downstream Definition entry

- Members: `H002`, `H022`. Technical: `CAN_DEFER`. Disposition: `STILL_APPLICABLE`. Depends on: none. Source: batch1.
- Probe mutation: disposable `select_route` fixtures on valid-project copy. A1: brainstorm promoted+authorized, `stop=true`, definition active. A2: same + definition green/A-due. A3 control: stop alone. B1/B2: state `active`|`ready_for_definition` + exact promotion authorization + definition active. C positive: promoted, no stop.
- Observed result: A1 → `route/definition` ("Promoted scope has active Definition work"), not stop; explicit stop shadowed by definition branch `tools/router.py:469-475` before brainstorm stop `:582-590`. A3 control correctly stops `explicit_user_stop`. B1/B2: `validate_brainstorm` ACCEPTED `active`|`ready`+authorized (`tools/state_contract.py:355-384` has no `state==promoted` gate); router `:460-466` checks only promotion_state/subject, not state, so both → `route/definition`. C positive routes definition. Suites pass (55 router + 46 state).
- Likely future repair boundary: one Brainstorm→Definition lifecycle Card: enforce `state==promoted` + exact promotion authorization at cross-record boundary (router `:458-466` + validator) and evaluate `explicit_user_stop` before downstream Definition/Planning dispatch.
- Accepted-M02R authority: insufficient — M02R owns REQ-108..114/133..137 review convergence/observation/Card sizing/Worker/live-validation; all 13 M02R Cards done at rev104; no M02R Card owns Brainstorm promotion lifecycle. Requires explicit pre-M03 authority/replan or separate maintenance.

### RF003 — Generic Research dispatch must not preempt the owning workflow boundary

- Members: `H003`. Technical: `CAN_DEFER`. Disposition: `STILL_APPLICABLE`. Depends on: `RF009`. Source: batch1.
- Probe mutation: disposable `select_route` fixtures. A: active Research + brainstorm explicit stop. B: active unrelated Research (`brainstorming/scope-a@1`) + issue Intake `concrete repair:v2` without prior-art binding. C: active Research + promoted brainstorm + definition green/A-due. D/E positive controls.
- Observed result: all three → `route/research` ("Active Research owns next factual obligation"); research-first branch `tools/router.py:342-366` runs before intake `:368`, brainstorm/definition `:449-483`, premium gates. Thus active Research preempts explicit stop, Intake obligation, and premium_A. Positives pass: lone active → research; complete → exact return owner brainstorming. Suites OK.
- Likely future repair boundary: one router-precedence Card after `RF009`: evaluate owning boundary (explicit/premium stop, Intake obligation, result reconciliation, Board continuation) before generic Research dispatch; preserve exact return ownership.
- Accepted-M02R authority: insufficient — M02R scope contains no Research precedence/return-ownership correction; terminal at rev104. Requires explicit pre-M03 authority/replan or separate maintenance after `RF009`.

### RF004 — GREEN review must bind the exact current acceptance authority

- Members: `H005`, `H006`. Technical: `REQUIRES_CHECKPOINT_READBACK`. Disposition: `STILL_APPLICABLE`. Depends on: `RF007`, `RF012`. Source: batch2.
- Probe mutation: harvest validator repros rerun on current candidate + new router probes with disposable fixtures. H005: alternate `cards/archive/M01-T01.md` vs selected `cards/M01-T01.md`; router alternate-acceptance GREEN vs exact-acceptance control + result-subject-mismatch control. H006: acceptance `workflow/ROUTER.md` vs Definition `{requirements,decisions}/current.md`; router unrelated-acceptance GREEN vs baseline.
- Observed result: H005 PERSISTS — harvest repro ACCEPTED; router alternate-GREEN → `route/post_review_finalization` identical to exact control, while result-subject-mismatch correctly freezes (`review_freeze`). Cause: task_card locator has no commit/blob (`tools/state_contract.py:211-214`); review acceptance checks only path stem (`:1031-1035`); `parse_task_card` drops acceptance/tests text (`:762-768`); router compares only result subject (`tools/router.py:796-806`). Same-path mutation proven by structural absence. H006 PERSISTS — harvest ACCEPTED; router unrelated-GREEN consumed identically to baseline (GREEN-consumption); `validate_plan_review(data,workstream_id,planning)` takes no Definition (`:594`); router passes none (`:517`); authority acceptance is root-shaped only (`:1025-1026`, `:249-251`).
- Likely future repair boundary: one exact-acceptance-binding Card spanning implementation review and Plan Review with a shared canonical exact-authority key/readback contract; after `RF007`+`RF012`.
- Accepted-M02R authority: **M02R corrective authority not established** — Tester judged the canonical semantic rule accepted (`workflow/REVIEW.md` exact subject+acceptance; `workflow/PLAN_REVIEW.md` judges against accepted Definition; M02R-T01 acceptance; REQ-108), but the separate bounded P6 map found no explicit M02R corrective Card authority; RF004 belongs to general review/M05. Do not authorize work; requires explicit pre-M03 authority/replan or separate maintenance.

### RF005 — Plan Review verdict domain must be closed and exhaustively routed

- Members: `H007`. Technical: `REQUIRES_CHECKPOINT_READBACK`. Disposition: `STILL_APPLICABLE`. Depends on: none. Source: batch2.
- Probe mutation: router probe with disposable fixtures: frozen Planning + premium-B satisfied; verdict varied `pending`/`green`/`red`/`in_progress`.
- Observed result: `in_progress` (validator-legal via shared `validate_review` domain `tools/state_contract.py:1011`; `validate_plan_review` does not narrow it, `:614-618`) → `route/planning` with reason "RED Plan Review returns to Planning for correction classification", identical to true-RED handling. Controls correct: `pending`→`route/plan_review` (K006), `green`→`route/planning` GREEN-consumption (K007), `red`→`route/planning` RED-correction. Root cause: router frozen branch falls through to unconditional RED reason after K006/K007 miss (`tools/router.py:547-551`); policy predicates cover only pending/green (`tools/policy_kernel.py`). Approved-branch path already fails closed for non-green (`:564`); defect is frozen-branch-specific.
- Likely future repair boundary: one Plan Review state-domain Card: narrow validation to `pending`/`green`/`red` or exhaustively route all three and fail closed for every other state.
- Accepted-M02R authority: **M02R corrective authority not established** — Tester judged the canonical lifecycle accepted (`workflow/PLAN_REVIEW.md` pending/green/red), but the P6 map found no explicit M02R corrective Card authority; RF005 belongs to Plan Review/M05. Prospective-only if later authorized (M02 terminal GREEN, REQ-125). Do not authorize work.

### RF006 — Review history must be immutable, provenance-backed, and complete

- Members: `H008`, `H009`, `H018`. Technical: `REQUIRES_CHECKPOINT_READBACK`. Disposition: `AUTHORITY_RECONCILIATION_REQUIRED`. Depends on: `RF007`. Source: batch2.
- Probe mutation: validator/locator probes + close-gate fixture probe + test-suite review. H008: newly authored legacy-shaped R01 RED (no `review_kind`/`findings`/`severity`) vs explicit-RED controls (no findings / no severity). H009: `[R01 RED]` vs same-ID rewritten `[R01 GREEN]`; `review_attempt` locator with bogus commit/blob keys. H018: close gate on truncated board (`review_attempts=[]`) with durable R01 + open O1 on disk vs listed-board control omitting O1.
- Observed result: H008 PERSISTS — newly authored legacy-shaped ACCEPTED as initial legacy prefix (`tools/state_contract.py:1273-1279`, no provenance input `:1235-1243`); explicit-RED controls correctly rejected. Live impact: accepted consumer reviews M02R-T01..T07 (incl. M02R-T03 R01 RED/R02 GREEN) are legacy-shaped yet DONE — Board DONE must not imply closure. H009 PERSISTS — both `[R01 RED]` and rewritten `[R01 GREEN]` validate (current-list-only, no prior comparison); `review_attempt` locator is path-only (`:228-232`), bogus keys ignored; router reads current bytes only (`tools/router.py:768-770`). H018 PERSISTS — close gate completes (`final_observation_reconciliation_complete`) on truncated board while durable open O1 exists; listed-board control correctly rejects empty proposal. Gate enumerates only current locators (`tools/close_contract.py:563-581`); test `test_board_gate_accepts_proven_empty_history_and_reviewed_cleanup` (`test_close_contract.py:836`) encodes vacuous completion.
- Likely future repair boundary: one review-history identity/completeness Card (immutable attempt identity, durable legacy provenance, append-only complete readback consumed by Final reconciliation) AFTER Definition/Planning accepts the legacy cutoff/provenance representation, and after `RF007`.
- Accepted-M02R authority: authority reconciliation required — accepted authority (REQ-097..102, REQ-125, P6, Definition R3, M02R-T01..T03) defines no durable legacy cutoff/provenance representation distinguishing genuinely historical attempts from newly authored legacy-shaped ones; REQ-097 requires ambiguous legacy state to fail closed (current code violates it); REQ-098 conditions historical validity on subject/evidence proof. Per audit `authority_ambiguity`, the cutoff/provenance choice must return to Definition/Planning; implementation must not invent it. Defects persist but the durable mechanism is missing.

### RF007 — A locator is not proof until the actual target is resolved and identity-checked

- Members: `H010`, `H020`, `H029`. Technical: `REQUIRES_CHECKPOINT_READBACK`. Disposition: `STILL_APPLICABLE`. Depends on: none. Source: batch3.
- Probe mutation: disposable `/tmp` fixture copies of `tests/fixtures/router/valid-project` on exact candidate `07c7240`. H010: dangling `evidence/DOES-NOT-EXIST.md` result + dangling locator + `#O1` observation. H020: same-path byte mutation with unchanged declared `(path,commit,blob)` tuple through `refresh_ready_card`. H029: `workflow/ALIAS.md` symlink to `../untrusted/ISSUE_TEXT.md` + backslash-traversal string.
- Observed result: H010 — `parse_card_result` accepts dangling (`tools/execution_contract.py:70-82`, existence never checked); router active-result branch never dereferences evidence refs (`tools/router.py:758-777`); `validate_observation_provenance` accepts dangling locator + `#O1` on string binding only (`tools/review_contract.py:553-585`). H020 — `refresh_ready_card` compares declared tuples only and reads live bytes without Git resolve/hash (`tools/router.py:278-297`); same-path byte mutation with unchanged tuple still → `execution_prep`; existing stale test mutates metadata+bytes together so still misses it. H029 — `validate_locator` passes `workflow/ALIAS.md`; `Reads._read_path` follows symlink to `../untrusted/ISSUE_TEXT.md`, checks broad root only, records raw `owner:raw` (`tools/router.py:95-105`); `_safe_relative_path` uses `PurePosixPath` and passes backslash traversal on POSIX (`tools/state_contract.py:189-194`).
- Likely future repair boundary: one reusable locator/readback foundation Card: resolve existence, semantic root, and exact Git object identity before any consumer treats a locator/declaration as workflow proof.
- Accepted-M02R authority: M02R corrective authority not established (report: insufficient/false) — no M02R Card owns the locator/readback foundation. Requires explicit pre-M03 authority/replan or separate maintenance.

### RF008 — editorial_exempt needs authority-owned proof, not self-attestation

- Members: `H012`. Technical: `MUST_RECONCILE_BEFORE_M03`. Disposition: `AUTHORITY_RECONCILIATION_REQUIRED`. Depends on: none. Source: batch1. Authority-first family.
- Probe mutation: authority-first readback; no proof mechanism designed. Code: disposable no-board fixture with green Definition + planning `approved editorial_exempt` with basis `wording only` (changed blob `c*40`, base `b*40`) + prior GREEN plan_review; variants `mechanical fix`, empty basis, stale base. Authority search: grep of consumer requirements/decisions/P6 and candidate requirements for a durable proof mechanism.
- Observed result: `validate_planning` ACCEPTED self-attested `wording only` and `mechanical fix` (`tools/state_contract.py:522-526` requires only non-empty basis+base); router `tools/router.py:553-562` → `route/execution_prep` without new Stage-6 review. Empty basis and stale base correctly fail closed to recovery, proving only shape/binding is enforced, not editorial-vs-material proof. Authority search: PWV2-REQ-039 + `PLANNING`/`PLAN_REVIEW` prose only; zero hits for a durable classification/proof mechanism in consumer `PWV21_POLICY_KERNEL` requirements/decisions/P6. Ambiguity persists. No `editorial_exempt` proof invented.
- Likely future repair boundary: no implementation Card first. Return the proof rule to Definition/Planning, accept the durable old/new-subject classification mechanism, then materialize one narrow enforcement Card if work remains.
- Accepted-M02R authority: authority reconciliation required, authority-first — accepted semantics define what may be exempt but select no durable mechanism. Must return to Definition/Planning before any implementation Card; do not broaden M02R silently.

### RF009 — Research provenance and return ownership must be exact

- Members: `H014`, `H016`. Technical: `CAN_DEFER`. Disposition: `STILL_APPLICABLE`. Depends on: `RF007`. Source: batch1.
- Probe mutation: disposable `select_route` + validator fixtures. A1/A2/A3: complete Research with mismatched origin/return (`intake`→`brainstorming`; `definition`→`intake`; nonexistent `scope@99`). B: forged Intake binding `repair:v9/forged-string` with no Research. B2: forged binding mismatched vs consumed real result. C: exact-binding control.
- Observed result: `validate_research` ACCEPTED all mismatches (`tools/state_contract.py:387-448` checks only non-empty `origin_subject` + allowed `return_target` set, no existence/cross-record binding); router `:351-366` routed each to the declared `return_target`, never recovery. `validate_intake` ACCEPTED forged binding (`:324-328` checks only `subject==repair` + non-empty string, no Research readback); router `:372-399` accepts stable binding without verifying consumed Research, so both forged cases → `stop/issue_alignment` identical to exact control. Exact control correctly stops.
- Likely future repair boundary: one Research referential-integrity Card after `RF007`: exact origin↔return-target binding + exact prior-art-result provenance consumed by Intake/Board owners.
- Accepted-M02R authority: insufficient — M02R owns no Research referential-integrity/provenance correction and is terminal at rev104. Requires explicit pre-M03 authority/replan or separate maintenance in order `RF007`→`RF009`.

### RF010 — Issue alignment cannot precede a concrete repair subject

- Members: `H015`. Technical: `CAN_DEFER`. Disposition: `STILL_APPLICABLE`. Depends on: `RF009`. Source: batch1.
- Probe mutation: disposable `select_route` fixtures. A: issue `pending`, response `none`, empty `repair_subject`. B: concrete `repair:v2` without prior-art proof. C: concrete + exact prior-art binding + matching consumed Research.
- Observed result: A → `stop/issue_alignment` with empty subject: router guard `tools/router.py:372` (`if kind==issue and repair_subject`) skips the prior-art gate when empty, then `:400-408` unconditionally stops on `pending`+`none`; validator `tools/state_contract.py:329-332` permits `pending` with empty `repair_subject`. B correctly routes `intake` (concrete diagnosis must materialize prior-art); C correctly stops. Only the empty-subject path is defective; family remains applicable.
- Likely future repair boundary: one Intake issue-lifecycle Card after `RF009`: gate `issue_alignment` on a concrete `repair_subject` plus completed exact diagnosis/prior-art proof; empty subject stays in Intake diagnosis.
- Accepted-M02R authority: insufficient — M02R owns no Intake issue-lifecycle/alignment-gate correction and is terminal at rev104. Requires explicit pre-M03 authority/replan or separate maintenance after `RF009`.

### RF011 — Recovery/cleanup completion proof must be derived, not caller-attested

- Members: `H017`, `H019`. Technical: `CAN_DEFER`. Disposition: `AUTHORITY_RECONCILIATION_REQUIRED`. Depends on: `RF006`, `RF007`. Source: batch3.
- Probe mutation: H017: `verify_target_side_recovery` with `required=present=frozenset()` fed to `cleanup_branch_action`. H019: `validate_cleanup_work` with fabricated 40-hex commit/blob, dangling evidence string, boolean `independent_review_green`/`speculative`/new-scope flags; plus repo positive-test review. Authority search over candidate `workflow/requirements/planning` + consumer HEAD for an exact package enumeration.
- Observed result: H017 reproduces — empty sets → `source_ref_independent_recovery` (`tools/close_contract.py:179-202`, no mandatory minimum) → `delete_exact_ref`. H019 reproduces — fabricated inputs ACCEPTED (`:251-318`); repo positive test `test_cleanup_work_requires_exact_subject_tests_and_independent_review` still encodes `a*40`/`b*40` acceptance. Package definition genuinely missing as an exact enumeration: `CLOSE.md:61` and `WORKSTREAMS.md:27` list prose categories only; no exact artifact set or per-class completeness rule exists in candidate `workflow/requirements/planning` or consumer accepted Definition/P6. Defects persist but the durable package definition is missing.
- Likely future repair boundary: blocked until Definition/Planning accepts the exact mandatory source-ref-independent package enumeration; then one Close/Recovery proof-derivation Card (derive mandatory package + cleanup proof from durable state via exact readback; H019 readback portion implementable once `RF007` lands).
- Accepted-M02R authority: authority reconciliation required — per audit `authority_ambiguity`, the package definition must return to Definition/Planning; implementation must not invent it.

### RF012 — Planning must be fresh to the current Definition authority

- Members: `H021`. Technical: `REQUIRES_CHECKPOINT_READBACK`. Disposition: `STILL_APPLICABLE`. Depends on: `RF007`. Source: batch2.
- Probe mutation: router probe with disposable fixtures: approved Planning + GREEN Plan Review + satisfied C + live board; Definition varied `R1`→`R2` and requirements/decisions swapped under `R1`.
- Observed result: baseline R1 → `route/execution M01-T04`; R2 mutant (Planning/`entry_subject`/premium/review untouched) → identically `route/execution M01-T04` instead of failing closed/re-entering Planning; changed-requirements/decisions-under-R1 mutant also executes. Structural cause: `validate_planning(data,workstream_id)` takes no Definition and binds `entry_subject` only to `premium_a_subject` (`tools/state_contract.py:543`); router loads Definition and Planning separately and never compares `planning.entry_subject` to definition revision/authority (`:485-522`); no freshness predicate in mechanical policy.
- Likely future repair boundary: one Definition→Planning freshness Card using a durable exact authority key shared by Planning, Plan Review, and router freshness checks; after `RF007`.
- Accepted-M02R authority: **M02R corrective authority not established** — Tester judged Planning-derives-from-current-Definition accepted (`workflow/PLANNING.md`; H021 serialization is an implementation detail), but the P6 map found no explicit M02R corrective Card authority; RF012 belongs to Definition→Planning freshness/M06. Prospective-only if later authorized (M02 terminal GREEN, REQ-125). Do not authorize work.

### RF013 — Execution authority and Card Result require semantic validity, not mere presence

- Members: `H023`, `H024`. Technical: `REQUIRES_CHECKPOINT_READBACK`. Disposition: `STILL_APPLICABLE`. Depends on: `RF007`. Source: batch3.
- Probe mutation: disposable `/tmp` fixture copies. H023: Card Result with Tests/readback summary `FAILED: acceptance test failed` through `parse_card_result` + router active-result branch with review `none`. H024: default active/result-less fixture card (2-line `cards/M01-T04.md`) through `select_route` vs `parse_task_card`.
- Observed result: H023 — `parse_card_result` accepts the FAILED string as non-empty (`tools/execution_contract.py:63-65,84-88`, no success predicate); router active-result branch with review `none` → `route/result_reconciliation`, calling it "valid semantic result" (`tools/router.py:772-777`). H024 — the same 2-line card → `route/execution` while `parse_task_card` rejects the same file (missing stable fields); active/no-result branch reads but never parses the Card (`:757,867-873`).
- Likely future repair boundary: one execution/result semantic-validation Card: validate the stable Card before recovered Execution; use a structured success predicate before a Result can authorize reconciliation/review/no-replay recovery (no substring heuristics).
- Accepted-M02R authority: M02R corrective authority not established (report: insufficient/false). Requires explicit pre-M03 authority/replan or separate maintenance after `RF007`.

### RF014 — JIT lifecycle must participate in terminality and prove materialization

- Members: `H026`. Technical: `REQUIRES_CHECKPOINT_READBACK`. Disposition: `STILL_APPLICABLE`. Depends on: `RF001`, `RF013`. Source: batch4.
- Probe mutation: `all-DONE`+satisfied ordinary trigger with no downstream Card; `all-DONE`+consumed trigger with no downstream evidence; `validate_board` direct; positive `all-DONE`/no-JIT.
- Observed result: both `all-DONE`+satisfied and `all-DONE`+consumed (no downstream) → `route/close`, identical to the no-JIT positive; K012 (`tools/policy_kernel.py:81-83`, `mechanical_policy.json` inputs `board.cards` only) fires at `tools/router.py:934-939` before JIT holds at `957-1028`, which cover only live-finding/live-consumer gates; `validate_board` (`tools/state_contract.py:891-905`) requires only DONE predecessor/bound-handoff, no consumed-by/downstream binding; no `consumed_by` field validated anywhere (grep). Consumer Board rev104 itself carries 14 consumed triggers with prose-only condition keys, tolerated as terminal history under REQ-125. No closing test.
- Likely future repair boundary: one JIT-terminality Card: pending/satisfied JIT obligations part of terminal completeness; exact consumed-by/materialized-downstream binding; after `RF001`+`RF013`.
- Accepted-M02R authority: insufficient — REQ-123/REQ-127 authorize only affected-JIT (live-finding) and intentional live-consumer holds, both implemented; ordinary satisfied-JIT terminality and consumed-by materialization proof have no accepted requirement or BOOT seam. Requires explicit pre-M03 authority/replan or separate maintenance.

### RF015 — Close continuation must be connected to the production selector

- Members: `H027`. Technical: `CAN_DEFER`. Disposition: `STILL_APPLICABLE`. Depends on: `RF011`, `RF014`. Source: batch4.
- Probe mutation: first `all-DONE` entry; immediate re-entry on the same board; `close_continuation` unit oracle; static grep for production callers and `end_of_scope_stop` in `tools/router.py`.
- Observed result: first `all-DONE` → `route/close` (positive holds); re-entry → `route/close` again, never `stop`/`end_of_scope_stop`. Oracle `close_continuation` (`tools/close_contract.py:606-632`) correctly returns `end_of_scope_stop`/`authorization_stop` and is unit-tested (`test_close_contract.py:327-375`), but grep proves zero production callers and zero `end_of_scope_stop` references in `tools/router.py`; `ROUTER.md:64-65` and `CLOSE.md:93` claim the continuation the selector never implements.
- Likely future repair boundary: one Close-composition Card: selector durable Close-completion input/readback emitting `end_of_scope_stop`/`USER_STOP` at true end; after `RF011`+`RF014`. Technical label `CAN_DEFER` preserved (M07 surface).
- Accepted-M02R authority: insufficient — P6 places close continuation semantics in M07 (P6 line 152); no M02R requirement authorizes Close-composition/selector wiring. Requires explicit pre-M03 authority/replan or separate maintenance.

### RF016 — SessionStart must verify canonical router integrity beyond marker strings

- Members: `H028`. Technical: `CAN_DEFER`. Disposition: `STILL_APPLICABLE`. Depends on: none. Source: batch4.
- Probe mutation: `hooks/session-start.py canonical_router` with a two-marker-only `ROUTER.md`; marker-preserving contradictory/truncated `ROUTER.md`; positive untouched candidate root; digest/manifest grep.
- Observed result: two-marker-only file ENABLED (returns path, should BLOCK); marker-preserving contradictory/truncated file ENABLED (should BLOCK); `canonical_router` (`hooks/session-start.py:34-53`) checks only `ROUTER_HEADER`+`ROUTER_SELECTOR` substring presence; no digest/manifest/hash reference in file (grep NONE); positive untouched candidate root ENABLED. Existing tests (`test_codex_delivery.py:126-142`) cover only missing/markerless/escape cases, no marker-preserving corruption test.
- Likely future repair boundary: one delivery-integrity Card for SessionStart canonical-router verification + marker-preserving corruption tests; keep workflow semantics in the router, not the bootstrap.
- Accepted-M02R authority: insufficient — SessionStart delivery integrity is an M06 runtime/handoff surface; no M02R requirement or BOOT seam authorizes it. Requires explicit pre-M03 authority/replan or separate maintenance. Technical label `CAN_DEFER` preserved.

### RF017 — Malformed durable TOML must deterministically route Recovery

- Members: `H030`. Technical: `REQUIRES_CHECKPOINT_READBACK`. Disposition: `STILL_APPLICABLE`. Depends on: none. Source: batch3.
- Probe mutation: malformed `TASK_BOARD.toml` and `WORKSTREAM.toml` (`revision = [`) through `select_route`; controls: valid TOML and semantic-invalid TOML.
- Observed result: malformed → uncaught `tomllib.TOMLDecodeError` out of `select_route` instead of `recovery_boundary`; `read_toml`/`read_project` do not normalize (`tools/state_contract.py:159-174`); selector catches `(OSError,ValidationError[,KeyError])` only (`tools/router.py:313,665,867,883,918`); only the `state_contract` CLI catches `TOMLDecodeError` (`:1523`). Controls: valid TOML routes normally; semantic-invalid TOML still returns recovery via `ValidationError`; no router malformed-TOML test exists.
- Likely future repair boundary: one parser-normalization Card: normalize TOML decode failures at the durable-state read boundary (or exhaustively catch) so every selector-owned TOML surface returns deterministic Recovery.
- Accepted-M02R authority: M02R corrective authority not established (report: insufficient/false). Requires explicit pre-M03 authority/replan or separate maintenance.

## 6. Explicit non-events

- No corrective implementation was performed.
- No corrective Card was created.
- No M02R Milestone Review was performed.
- No M03 was materialized.
- No audit-branch mutation was performed (audit files were read read-only via Git object).
- No historical rewrite was performed; correctly terminal history remains terminal under REQ-125.
- This checkpoint readback is awaiting a **fresh independent review of the synthesized applicability readback** before corrective work; the four probe reports were independent, but this synthesis itself has not yet been independently reviewed.

## 7. Limitations

- Candidate behavior was established by the four probe reports against disposable fixtures on the exact candidate SHA; this synthesis did not re-execute probes or replay the full consumer workstream.
- Board-coupled `plan_gate_passed_with_board`, Board `execution_prep`/`execution` Research return variants, and live-Board editorial paths were probed only as stated per family; several families note workstream-level dispatch only.
- RF006 router end-to-end rewrite flip follows deterministically from cited control flow but was not separately executed; legacy-vs-historical determination for already-terminal consumer reviews is Main-owned.
- RF007 Windows backslash vector confirmed at the lexical layer only (platform-conditional); Git-identity negative cases follow from the same missing-resolve path without separate execution.
- Authority searches covered the stated consumer/candidate authority roots; they did not re-read every M02R evidence file.
- Same-path Card-content mutation (RF004) was proven by structural code absence plus an alternate-path router probe, not a dedicated same-path router run.

## 8. Sources

- Consumer HEAD object: `6e47749782cac0cdf01b8e65a95ddf2d5be7c2ec` (verified via `git rev-parse HEAD`; Board `revision = 104` via `HEAD:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/TASK_BOARD.toml`).
- Audit commit object: `e0fdcbf5021f7b50a347edc169beaa8a01eeb58b` (`audit: persist quality-first pre-M03 reconciliation policy`, `origin/audit/pwv21-pre-m03-reconciliation`).
- Candidate SHA verified by local exact-head readback and consistently reported by all four probe JSONs: `07c724085de591c2a0bb51aaaae0ec23009880bf` (`elmakus/project_workflow_v2`).
- Probe JSONs: `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/pre_m03_audit_readback/PROBE_BATCH_01.json` (RF002, RF003, RF008, RF009, RF010), `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/pre_m03_audit_readback/PROBE_BATCH_02.json` (RF004, RF005, RF006, RF012), `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/pre_m03_audit_readback/PROBE_BATCH_03.json` (RF007, RF011, RF013, RF017), `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/pre_m03_audit_readback/PROBE_BATCH_04.json` (RF001, RF014, RF015, RF016).
