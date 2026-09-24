# M02R-T03 Shadow Review

## Original independent verdict

FINDINGS FOUND

## Original material findings

### 1. A brand-new RED can impersonate a legacy review and bypass load-bearing evidence

- **Affected requirement/contract:** PWV21-REQ-133 and the M02R-T03 acceptance requiring concrete materially load-bearing evidence for any RED.
- **ELI10 explanation:** Old reviews are allowed to use the old rules. The validator asks only whether a review looks old. A brand-new review can use the old format and receive the legacy exception.
- **Concrete counterexample/reproduction:** A newly created terminal R01 can carry the exact current Card/result subject, valid independence and terminal evidence, but set `verdict = "red"` while omitting `review_kind`, `material_finding_ids`, and `finding_severity`. While it remains in the initial legacy prefix, `validate_review_history()` accepts that old-shaped terminal record. The new PWv2.1 RED severity gate is therefore not applied.
- **Why load-bearing:** Such a RED can block GREEN and drive correction/recovery without any concrete load-bearing finding or evidence, which is the behavior REQ-133 forbids.
- **Original classification:** Recurrence/incomplete closure of the already-known evidence-free-RED semantic class, via a new legacy-impersonation vector.

### 2. Observation provenance can still terminate at a nonexistent evidence artifact

- **Affected requirement/contract:** PWV21-REQ-134, the M02R-T03 durable provenance/origin-binding requirement, and fail-closed handling of dangling references.
- **ELI10 explanation:** The repair checks that two road signs point to the same house, but it never checks that the house actually exists.
- **Concrete counterexample/reproduction:** A terminal attempt can declare an `evidence_path` such as `implementation/workstreams/ws/evidence/DOES_NOT_EXIST.md` and an observation evidence locator `implementation/workstreams/ws/evidence/DOES_NOT_EXIST.md#O1`. The two strings bind correctly, so provenance validation succeeds. The board-bound Final gate reads the review-attempt TOML but does not read or Git-verify the referenced review evidence artifact itself.
- **Why load-bearing:** REQ-134 requires every non-load-bearing observation to remain durably traceable to its originating review evidence. A self-consistent pair of dangling strings is not durable traceability.
- **Original classification:** Recurrence/incomplete closure of the already-known observation-provenance semantic class; the repaired code closes mismatched provenance but not dangling provenance.

### 3. The authoritative Final gate can silently omit observations from sibling Cards

- **Affected requirement/contract:** PWV21-REQ-135 and the M02R-T03 requirement that Final Integration cannot complete with any unreconciled open observation.
- **ELI10 explanation:** The old bug checked only the papers handed to it. The repair now goes to the filing cabinet itself, but opens only one drawer and then declares the whole cabinet checked.
- **Concrete counterexample/reproduction:** Construct an otherwise valid Task Board with two terminal Cards. Card A has all observations reconciled. Card B retains `O-B1 = open`. Invoke `verify_final_observation_reconciliation_from_board(..., card_id="A", ...)` with Card A's reconciled observations. The helper enumerates only Card A's `review_attempts`, never examines Card B, and can return `final_observation_reconciliation_complete` while `O-B1` remains open.
- **Why load-bearing:** This leaves a silent observation-loss path at the pre-Final gate. Correctness depends on an external caller remembering to invoke the gate separately for every relevant Card, while the helper presents itself as the authoritative Final reconciliation entry point.
- **Original classification:** Recurrence/incomplete closure of the already-known incomplete-Final-reconciliation semantic class, through sibling-Card/history truncation.

### 4. Fake-but-well-shaped cleanup still satisfies Final reconciliation

- **Affected requirement/contract:** PWV21-REQ-136 and the M02R-T03 cleanup-candidate contract requiring an exact subject, tests/evidence and independent GREEN review.
- **ELI10 explanation:** Previously cleanup could be accepted with only “done = yes.” Now a serial number, test name and “reviewed = yes” are required, but the implementation does not prove that any of those things actually exist.
- **Concrete counterexample/reproduction:** For a canonical `cleanup_candidate`, a cleanup record can use a non-empty repository/path, arbitrary 40-hex commit/blob strings, a non-empty but nonexistent `tests_evidence` string, `complete = true`, and `independent_review_green = true`. `validate_cleanup_work()` checks those claims syntactically but does not Git-read back the subject, read the tests/evidence artifact, or bind the GREEN boolean to an exact independent review attempt. A path such as `../../does-not-exist.md` is also not passed through the normal safe-relative-path validation there.
- **Why load-bearing:** Final Integration can certify a cleanup candidate as completed although the cleanup implementation, evidence and independent review may all be fabricated.
- **Original classification:** Recurrence/incomplete closure of the already-known unbound-cleanup semantic class; the literal bare-boolean reproducer is closed, but a syntactically complete fabricated claim remains possible.

## Original non-blocking observations

The repaired implementation correctly constrains terminal observation dispositions to `resolved`, `cleanup_candidate`, `deferred`, `promoted`, and `tracked`; `open` cannot pass Final reconciliation. Duplicate observation introductions, unknown reconciliation targets, second reconciliation, and same-epoch reuse of a load-bearing finding ID as an advisory observation are rejected.

The repaired origin-prefix check rejects the literal mismatched-provenance reproducer and obvious tracker/Issue provenance. Cleanup termination also behaves as intended: merely conceivable further advisory improvement does not recursively reopen completed cleanup.

No implementation leakage into BOOT-B, BOOT-C, or BOOT-D was identified, and no material attempt to pull later M05 policy into M02R-T03 was found.

Two semantic edges were observed but were not elevated to material findings. First, tracker/Issue text may still appear in free-form disposition basis text; whether that merely references bookkeeping or improperly delegates authority is semantic reviewer judgment rather than a deterministic-code defect established by this audit. Second, the no-downgrade machinery robustly catches identity-preserving relabeling, but a reviewer could describe the same real-world defect under a new advisory ID; semantic defect identity is reasoning-owned, so this was not classified as a mechanical defect.

## Original coverage

The completed shadow review checked the complete applicable M02R-T03 BOOT-A surface requested: load-bearing versus advisory classification; RED-without-evidence paths; explicit PWv2.1 versus legacy review handling; observation introduction, origin binding and dangling provenance; observation history derivation and silent loss/truncation; downgrade guards; tracker/Issue non-authority; all five allowed dispositions; pre-Final completeness; single-Card and sibling-Card negative space; `cleanup_candidate`; cleanup subject/test/review binding; speculative/new-scope admission; cleanup termination; malformed/dangling state behavior; relevant changed tests; and BOOT-B/C/D/M05 scope boundaries.

The audit also inspected the exact one-commit implementation delta `736c55f32cc80f42b8e5c7d6aac80d8a9eb931a5..180cc0af3a9b56c8c2808827bf5548b8ae040608` and the exact repaired consumer result `5b76ffe03259ff141afc6bfb5b7b546041a48b41:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/results/M02R-T03-R02.md@b357ba85d4975540f3ae87b05e73e3fcf8e0471a`.

The shadow review did not independently execute a clean local clone. The already-available formal evidence reported a 258-test passing suite and exact-head CI success; the original findings were negative-space cases outside those reported probes rather than a dispute about the reported passing tests.

## Post-freeze comparison

This section was produced only after the original independent finding set above had been frozen. It does not alter the original verdict or material findings.

The independent shadow result disagreed with the formal R02 GREEN. Formal R01 had four material semantic classes: evidence-free RED, broken observation provenance, incomplete Final reconciliation, and unbound cleanup. Formal R02 verified that the repaired implementation closed the literal R01 reproducers and exercised many adjacent cases.

The frozen shadow review independently found a further bypass in each of those same four semantic classes:

| Formal repair area | Formal R02 conclusion | Frozen shadow negative case |
| --- | --- | --- |
| R01 F1 | Explicit PWv2.1 RED requires severity | A newly manufactured legacy-shaped terminal RED bypasses the requirement |
| R01 F2 | Observation evidence must bind to its origin path | The origin path itself may be nonexistent or dangling |
| R01 F3 | Board-bound history prevents caller truncation | The authoritative helper binds only one Card and can omit sibling-Card observations |
| R01 F4 | Cleanup requires subject/tests/GREEN-review fields | The subject, tests/evidence and review are not durably verified, so a well-shaped fabrication can pass |

Formal R02 explicitly accepted legacy pre-`review_kind` RED for compatibility but did not establish durable historical provenance for that exemption. It also treated full M05 lifecycle wiring as later scope; the shadow review did not classify the absence of M05 wiring itself as an M02R-T03 defect, but retained the narrower finding that the current board-bound helper can certify completion from a one-Card slice.

The formal R02 GREEN therefore did not change the frozen shadow verdict: **FINDINGS FOUND**, with the four material findings listed above.
