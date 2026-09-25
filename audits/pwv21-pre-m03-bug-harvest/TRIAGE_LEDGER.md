# Triage Ledger

This ledger normalizes candidate classes only. Ownership and downstream relevance are hypotheses for ordering and later verification; they do not discard, defer, confirm, or reject any candidate. Every technical verdict requires independent reproduction against the exact relevant audited subject.

Normalized candidates: 30. Cross-source merged semantic families: 1.

## H001 — Human-authority blocker can coexist with active execution

- Source classes:
  - PWV2:C027
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: STATE Card/blocker coherence; RECOVERY human-authority blocker must remain authoritative.
- Shared core claim: A Card may remain in_progress while carrying a human_authority blocker, and the active execution route can ignore that blocker.
- Distinct reproduction vectors: Keep a valid Card in_progress, attach a valid human_authority blocker, then select the route.
- Existing reproduction artifacts: PWv2 source repros/adversarial_repros.py F4.
- Source limitations: Singleton finding based on direct branch-order reasoning; persisted repro was not reported as freshly executed.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H001.md`
- Current candidate check: `persists` at `8a24fb66c447e7a5dc22d2f398d13ddb54ebf481`

## H002 — Explicit Brainstorming stop can be bypassed by downstream state

- Source classes:
  - PWV2:C008
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 6 independent PWv2 source audits
- Claimed invariant/requirement: BRAINSTORMING explicit stop; USER_STOP; ROUTER human-boundary precedence.
- Shared core claim: Validator-legal downstream Definition/Planning/Board state may route before the durable Brainstorming explicit_user_stop is honored.
- Distinct reproduction vectors: Promoted/GREEN Definition routing to Planning; approved plan plus live Board routing to Execution; active Definition route.
- Existing reproduction artifacts: Multiple source-local promoted-Brainstorm stop fixture scripts.
- Source limitations: Mostly source-mechanical route-order proofs; this class excludes the generic Research-preemption variants.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H002.md`
- Current candidate check: `persists` at `8a24fb66c447e7a5dc22d2f398d13ddb54ebf481`

## H003 — Generic Research dispatch can outrun higher-precedence owner boundaries

- Source classes:
  - PWV2:C007
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 13 independent PWv2 source audits
- Claimed invariant/requirement: ROUTER precedence; explicit/premium stops; INTAKE issue boundaries; Task-Board Research ownership.
- Shared core claim: The top-level generic Research branch may execute before the state owner that should control a stop, Intake obligation, or Board-bound continuation.
- Distinct reproduction vectors: Active Research plus explicit stop; Research plus premium A; unrelated Research plus issue prior-art/alignment; orphan execution Research; legal co-bound execution Research shadowed by pre-execution routing.
- Existing reproduction artifacts: Source-local router scripts across the class findings.
- Source limitations: The reported effects differ and later reproduction may split one ordering issue into multiple owner-specific defects.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

## H004 — DONE status can bypass result and required-review proof

- Source classes:
  - PWV2:C002
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 24 independent PWv2 source audits
- Claimed invariant/requirement: STATE terminal Card semantics; REVIEW blocking lifecycle; ROUTER all-DONE Close handoff.
- Shared core claim: status=done can be trusted without reconstructing the valid result and exact terminal review proof that makes DONE legal.
- Distinct reproduction vectors: No review; pending or RED review; missing result; required-review Card flipped directly to DONE; blocker residue.
- Existing reproduction artifacts: Multiple source-local DONE-state fixture repros.
- Source limitations: Some reports emphasize missing result validity and others required-review bypass, but the terminal-status shortcut is common.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

## H005 — Implementation GREEN can remain bound only to a mutable/path-only acceptance surface

- Source classes:
  - PWV2:C004
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 11 independent PWv2 source audits
- Claimed invariant/requirement: REVIEW exact acceptance surface; STATE review binding; EXECUTION_PREP stable Task Card authority.
- Shared core claim: A GREEN review may remain valid when the selected Card acceptance contract changes at the same path or is not the exact selected contract locator.
- Distinct reproduction vectors: Same-path acceptance or required-test mutation; Review requirement change; same-ID Card relocation; alternate/nonexistent acceptance path.
- Existing reproduction artifacts: Task Card mutation and relocation scripts in source reports.
- Source limitations: Repros were often persisted rather than executed; the class is specifically about acceptance binding, not result-subject identity.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H005.md`
- Current candidate check: `persists` at `31764d82911de523e36d2de5c5d98ce7c3cedb18`

## H006 — Plan Review can bind to unrelated Definition authority

- Source classes:
  - PWV2:C005
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 3 independent PWv2 source audits
- Claimed invariant/requirement: PLAN_REVIEW exact acceptance authority; PLANNING review gate.
- Shared core claim: A Plan Review may accept a syntactically permitted but unrelated authority path instead of the current Definition/requirements/decisions authority.
- Distinct reproduction vectors: Use workflow/ROUTER.md, an unrelated decision file, or a non-current requirements path as acceptance authority.
- Existing reproduction artifacts: Source-local Plan Review validator/router scripts.
- Source limitations: Primarily validator/control-flow demonstrations; no material source disagreement.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H006.md`
- Current candidate check: `persists` at `31764d82911de523e36d2de5c5d98ce7c3cedb18`

## H007 — Plan Review in_progress can be consumed as RED

- Source classes:
  - PWV2:C016
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: Plan Review verdict domain and Planning/Review precedence.
- Shared core claim: The shared validator can admit in_progress while routing handles pending/green and treats the remaining accepted value as RED.
- Distinct reproduction vectors: Take a valid frozen Plan Review, set verdict/state to in_progress, omit terminal evidence, then route.
- Existing reproduction artifacts: repros/router_counterexamples.py F3.
- Source limitations: Singleton finding; persisted reproducer was not reported as executed in the source audit.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H007.md`
- Current candidate check: `persists` at `e75a261df0dea3170f3f9c9c0fd535fd055abd6f`

## H008 — New legacy-shaped RED can receive historical compatibility treatment

- Source classes:
  - M02R-T03:C04
- Source subjects: consumer elmakus/chatgpt-codex-project-workflow@5b76ffe03259ff141afc6bfb5b7b546041a48b41, result blob b357ba85d4975540f3ae87b05e73e3fcf8e0471a; implementation elmakus/project_workflow_v2@180cc0af3a9b56c8c2808827bf5548b8ae040608
- Independent-report frequency: 2 of 4 independent M02R-T03 shadow reviewers
- Claimed invariant/requirement: PWV21-REQ-133; M02R-T03 load-bearing evidence requirement for RED.
- Shared core claim: Legacy compatibility may be inferred from old schema shape rather than durable historicity, allowing a newly authored initial RED to omit PWv2.1 evidence fields.
- Distinct reproduction vectors: Create new terminal R01 for the current subject, omit review_kind, material_finding_ids, and finding_severity, and retain otherwise valid terminal fields.
- Existing reproduction artifacts: Counterexamples described by shadow sources S2-F1 and S4-F3.
- Source limitations: Both source reviews were negative-space/static analyses; one lacked a clean clone and one could not make a fresh clone because of DNS.
- Current ownership hypothesis: `m02r_bootstrap`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H008.md`
- Current candidate check: `persists` at `e75a261df0dea3170f3f9c9c0fd535fd055abd6f`

## H009 — Terminal implementation review attempt can be rewritten in place

- Source classes:
  - PWV2:C026
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: REVIEW append-only attempt history.
- Shared core claim: Board state stores an attempt path but does not prove terminal attempt immutability across history, so the same R01 path/ID may be rewritten from RED to GREEN.
- Distinct reproduction vectors: Persist R01 RED, rewrite the same file/path/ID to GREEN, then observe correction become finalization.
- Existing reproduction artifacts: repros/repro_findings.py F5.
- Source limitations: Singleton; persisted repro was not reported as executed.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H009.md`
- Current candidate check: `persists` at `e75a261df0dea3170f3f9c9c0fd535fd055abd6f`

## H010 — Durable evidence locator can be accepted without proving the artifact exists

- Source classes:
  - PWV2:C003
  - M02R-T03:C02
- Cross-source identity: **CROSS-SOURCE OVERLAP**
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045; consumer elmakus/chatgpt-codex-project-workflow@5b76ffe03259ff141afc6bfb5b7b546041a48b41, result blob b357ba85d4975540f3ae87b05e73e3fcf8e0471a; implementation elmakus/project_workflow_v2@180cc0af3a9b56c8c2808827bf5548b8ae040608
- Independent-report frequency: PWV2:C003 — 16 independent PWv2 source audits; M02R-T03:C02 — 2 of 4 shadow reviewers
- Claimed invariant/requirement: EXECUTION/REVIEW durable evidence existence; PWV21-REQ-134 provenance must terminate at durable evidence.
- Shared core claim: A safe/non-empty evidence locator, or two mutually matching evidence strings, can be consumed without dereferencing the referenced durable artifact.
- Distinct reproduction vectors: Delete result evidence; point terminal review evidence to nonexistent file; bind observation evidence to the same nonexistent review evidence_path; delete both result and review evidence.
- Existing reproduction artifacts: PWv2 evidence-deletion/missing-evidence scripts; M02R shadow S1-F2 and S2-F2 counterexamples.
- Source limitations: CROSS-SOURCE OVERLAP. Both populations identify missing durable readback, but one is broad result/review consumption and one is observation-provenance binding.
- Current ownership hypothesis: `cross_cutting`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H010.md`
- Current candidate check: `persists` at `e75a261df0dea3170f3f9c9c0fd535fd055abd6f`

## H011 — RECOMMENDED review has no durable activation state

- Source classes:
  - PWV2:C024
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: REVIEW rule that RECOMMENDED blocks only when activated.
- Shared core claim: Schema exposes none|required|recommended but no activation state, while routing treats every non-none review as blocking.
- Distinct reproduction vectors: Result-bearing Card with Review requirement recommended and no attempt routes to review_freeze.
- Existing reproduction artifacts: repros/router_counterexamples.py F4.
- Source limitations: Singleton state/document parity finding.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `unknown`
- Technical status: `rejected`
- Reproduction status: `rejected`
- Final disposition: `no_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H011.md`
- Current candidate check: `unchanged_nondefect` at `e75a261df0dea3170f3f9c9c0fd535fd055abd6f`

## H012 — editorial_exempt can suppress Plan Review from self-attested metadata

- Source classes:
  - PWV2:C023
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: PLANNING/PLAN_REVIEW material-change exception.
- Shared core claim: A changed plan can declare editorial_exempt with metadata and a non-empty basis without a durable semantic binding proving the change is only editorial.
- Distinct reproduction vectors: Use a new plan blob while retaining the old reviewed base/B/C and provide only a wording-only prose basis.
- Existing reproduction artifacts: repros/repro_counterexamples.py.
- Source limitations: Singleton; source notes editorial classification inherently needs semantic judgment not represented by the schema.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `unknown`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H012.md`
- Current candidate check: `persists` at `e75a261df0dea3170f3f9c9c0fd535fd055abd6f`

## H013 — Close review reuse can treat acceptance-surface shrink as unchanged coverage

- Source classes:
  - PWV2:C025
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: CLOSE final review reuse and exact acceptance surface.
- Shared core claim: Current acceptance being a subset of reviewed acceptance may be treated as reusable GREEN when fingerprints/compatibility match.
- Distinct reproduction vectors: Review {A,B,C}; current acceptance {A,B}; retain compatible content/behavior and request reuse.
- Existing reproduction artifacts: repros/repro_close_acceptance_shrink.py.
- Source limitations: Singleton policy/semantics dispute; repository tests reportedly assert the subset behavior.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `unknown`
- Technical status: `rejected`
- Reproduction status: `rejected`
- Final disposition: `no_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H013.md`
- Current candidate check: `unchanged_nondefect` at `e75a261df0dea3170f3f9c9c0fd535fd055abd6f`

## H014 — Research return target can contradict its durable origin owner

- Source classes:
  - PWV2:C006
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 11 independent PWv2 source audits
- Claimed invariant/requirement: RESEARCH exact return ownership; RECOVERY Board-bound Research return; fail-closed binding.
- Shared core claim: origin_role, origin_subject and return_target can be independently valid yet mutually incoherent, permitting return to a wrong owner or nonexistent Card.
- Distinct reproduction vectors: Intake-origin returning Definition; M01-T04 returning M99-T99; execution: with empty suffix; PHANTOM subject; origin/return role mismatch.
- Existing reproduction artifacts: Numerous Research fixture scripts in source reports.
- Source limitations: Pre-execution and implementation forms share missing cross-field referential integrity but could split during reproduction.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H014.md`
- Current candidate check: `persists` at `e75a261df0dea3170f3f9c9c0fd535fd055abd6f`

## H015 — Issue diagnosis can be converted into alignment stop before repair subject exists

- Source classes:
  - PWV2:C021
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: INTAKE diagnosis-before-alignment lifecycle.
- Shared core claim: Issue plus pending alignment and no response can produce a human stop even when repair_subject is empty and diagnosis is not yet bound to a repair proposal.
- Distinct reproduction vectors: Active issue Intake with repair_subject empty, response_kind none, alignment_state pending.
- Existing reproduction artifacts: repros/f1_pre_repair_issue_stop.py.
- Source limitations: Singleton; script persisted for exact-checkout reproduction.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H015.md`
- Current candidate check: `persists` at `e75a261df0dea3170f3f9c9c0fd535fd055abd6f`

## H016 — Intake diagnosis-prior-art proof can be forged as a non-empty string

- Source classes:
  - PWV2:C022
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 2 independent PWv2 source audits
- Claimed invariant/requirement: INTAKE mandatory issue prior-art; RESEARCH consumed/applied result provenance.
- Shared core claim: Matching prior-art subject plus any non-empty diagnosis_prior_art_result may be treated as completed proof without binding to an actual Research result.
- Distinct reproduction vectors: Use forged:never-produced or forged-no-research as the prior-art result with no qualifying Research record.
- Existing reproduction artifacts: f2_forged_prior_art_binding.py and f4_forged_prior_art_binding.py.
- Source limitations: Source repros were not freshly executed; exact historical and frozen-candidate predicates were inspected directly.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H016.md`
- Current candidate check: `persists` at `003f8a9a7c12a21d0c73b07163e449b8ae63bad8`

## H017 — Close recovery can be certified from an empty caller-declared artifact set

- Source classes:
  - PWV2:C017
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: CLOSE mandatory target-side recovery package before destructive source-ref cleanup.
- Shared core claim: Verifier may only compare caller-supplied required and present sets, allowing empty/empty to certify source-ref-independent recovery.
- Distinct reproduction vectors: Matching heads plus immutable merge evidence true plus empty required/present sets, followed by safe_to_delete/delete_exact_ref.
- Existing reproduction artifacts: repros/f4_empty_close_recovery_package.py.
- Source limitations: Singleton; source repro was not freshly executed; exact historical and frozen-candidate helper control flow was inspected directly.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H017.md`
- Current candidate check: `persists` at `003f8a9a7c12a21d0c73b07163e449b8ae63bad8`

## H018 — Final reconciliation can derive an incomplete durable observation history

- Source classes:
  - M02R-T03:C01
- Source subjects: consumer elmakus/chatgpt-codex-project-workflow@5b76ffe03259ff141afc6bfb5b7b546041a48b41, result blob b357ba85d4975540f3ae87b05e73e3fcf8e0471a; implementation elmakus/project_workflow_v2@180cc0af3a9b56c8c2808827bf5548b8ae040608
- Independent-report frequency: 4 of 4 independent M02R-T03 shadow reviewers
- Claimed invariant/requirement: PWV21-REQ-134/135; no silent observation loss; complete pre-Final reconciliation.
- Shared core claim: Final reconciliation may derive its canonical observation set from a current Board/history slice not proven complete, omitting durable observations outside that slice.
- Distinct reproduction vectors: Remove prior review locator while review file with open observation remains; invoke Final for Card A while Card B has open observation; duplicate-Card shadowing variant.
- Existing reproduction artifacts: Shadow source counterexamples S1-F1, S2-F3, S3-F1, S4-F1.
- Source limitations: The confirmed vector is prior-locator truncation; sibling-Card and malformed duplicate-Card variants were not independently required for this verdict. Fresh runtime execution was unavailable.
- Current ownership hypothesis: `cross_cutting`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H018.md`
- Current candidate check: `persists` at `003f8a9a7c12a21d0c73b07163e449b8ae63bad8`

## H019 — Cleanup completion can rely on self-attested subject, evidence, and review claims

- Source classes:
  - M02R-T03:C03
- Source subjects: consumer elmakus/chatgpt-codex-project-workflow@5b76ffe03259ff141afc6bfb5b7b546041a48b41, result blob b357ba85d4975540f3ae87b05e73e3fcf8e0471a; implementation elmakus/project_workflow_v2@180cc0af3a9b56c8c2808827bf5548b8ae040608
- Independent-report frequency: 4 of 4 independent M02R-T03 shadow reviewers
- Claimed invariant/requirement: PWV21-REQ-136; exact cleanup subject, tests/evidence, independent GREEN review, bounded scope.
- Shared core claim: Cleanup validation may accept shape-valid subject/evidence/review declarations without readback and binding to real durable implementation, evidence, and independent review.
- Distinct reproduction vectors: Arbitrary 40-hex commit/blob values; nonexistent result/tests evidence; complete=true; independent_review_green=true; caller-supplied speculative/new-product flags.
- Existing reproduction artifacts: Shadow source counterexamples S1-F3, S2-F4, S3-F2, S4-F2.
- Source limitations: This class partially touches general exact-subject and evidence-existence themes but is retained separately because its semantic claim is the composite cleanup proof contract.
- Current ownership hypothesis: `m02r_bootstrap`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H019.md`
- Current candidate check: `persists` at `003f8a9a7c12a21d0c73b07163e449b8ae63bad8`

## H020 — Declared immutable Git subject can differ from consumed bytes

- Source classes:
  - PWV2:C001
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 34 independent PWv2 source audits
- Claimed invariant/requirement: STATE exact result/dependency identity; EXECUTION_PREP READY refresh; REVIEW exact result subject; PLANNING/PLAN_REVIEW frozen Git subject.
- Shared core claim: repository/commit/path/blob identities may be shape-checked or compared as declarations without proving that consumed bytes are the named Git object.
- Distinct reproduction vectors: Same-path result mutation after GREEN; READY dependency mutation with unchanged tuple; fabricated 40-hex identities; foreign/nonexistent Planning subject; path-only result.
- Existing reproduction artifacts: Numerous source-local selector scripts; several use the repository router fixture.
- Source limitations: Sources agree on the identity gap but differ on consumer and whether path-only results are the same class or a sibling.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H020.md`
- Current candidate check: `persists` at `003f8a9a7c12a21d0c73b07163e449b8ae63bad8`

## H021 — Approved Planning can remain executable after Definition authority changes

- Source classes:
  - PWV2:C011
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 5 independent PWv2 source audits
- Claimed invariant/requirement: DEFINITION current authority; PLANNING entry/premium cycle; PLAN_REVIEW.
- Shared core claim: A self-consistent old Planning/Plan Review/premium chain can remain executable after the current Definition revision or requirements authority changes.
- Distinct reproduction vectors: Definition R1 to R2 with stale R1 plan; change requirements locator while retaining approved plan; live Board still routes Execution.
- Existing reproduction artifacts: Stale-Definition Planning scripts in source reports.
- Source limitations: Sources explicitly distinguish this from the exact serialization format of entry_subject.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`

- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H021.md`
- Current candidate check: `persists` at `003f8a9a7c12a21d0c73b07163e449b8ae63bad8`

## H022 — Definition can bind a Brainstorm revision not durably promoted

- Source classes:
  - PWV2:C018
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: BRAINSTORMING promotion lifecycle; DEFINITION exact promoted source.
- Shared core claim: Cross-record checks prove promotion authorization/subject but do not require the bound Brainstorm revision itself to be durably promoted.
- Distinct reproduction vectors: Take a normal GREEN Definition fixture and change Brainstorm state from promoted to active while preserving exact promotion authorization.
- Existing reproduction artifacts: repros/repro_router_state_gaps.py F4.
- Source limitations: Singleton; persisted selector repro was not reported as freshly executed; exact historical and frozen-candidate predicates were inspected directly.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H022.md`
- Current candidate check: `persists` at `aa729e9a3b06af6e90a6884f8613629d6cd519f0`

## H023 — Card Result can pass shape checks without semantic success or exactness

- Source classes:
  - PWV2:C013
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 4 independent PWv2 source audits
- Claimed invariant/requirement: EXECUTION accepted semantic result; STATE durable result as recovery truth.
- Shared core claim: Result consume boundary accepts non-empty fields without proving semantic success; the confirmed minimal vector is an explicitly FAILED tests/readback summary accepted as a valid result.
- Distinct reproduction vectors: Tests/readback summary explicitly FAILED; Implementation subject banana; nonexistent evidence with otherwise valid shape.
- Existing reproduction artifacts: Parser/router scripts; S024 reports the direct historical parser counterexample was executed.
- Source limitations: The class contains distinct missing predicates and overlaps exact-identity/evidence classes; this verdict is anchored to the independent explicit-FAILED-summary predicate.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H023.md`
- Current candidate check: `persists` at `aa729e9a3b06af6e90a6884f8613629d6cd519f0`

## H024 — Active execution can trust Card existence without stable Task Card contract

- Source classes:
  - PWV2:C019
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: EXECUTION_PREP stable Card contract; EXECUTION recovery; ROUTER fail-closed binding.
- Shared core claim: Active/no-result routing reads the Card file but does not parse the stable Task Card contract before routing Execution.
- Distinct reproduction vectors: The shipped active fixture routes Execution while `parse_task_card` rejects the exact same two-line Card for missing stable fields.
- Existing reproduction artifacts: `repro_router_semantic_holes.py` F4; repository fixture and `test_active_card_routes_to_runtime_neutral_execution`.
- Source limitations: Singleton; fresh execution was not required for triage because the fixture, parser requirements and positive selector expectation remain directly contradictory.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H024.md`
- Current candidate check: `persists` at `aa729e9a3b06af6e90a6884f8613629d6cd519f0`

## H025 — Nonterminal Card status can override durable result and replay work

- Source classes:
  - PWV2:C010
- Source subjects: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Independent-report frequency: 6 independent PWv2 source audits
- Claimed invariant/requirement: STATE durable result recovery truth; EXECUTION/RECOVERY no-replay.
- Shared core claim: Result reconciliation is status-gated to `in_progress` while validators permit result-bearing READY/blocked/planned Cards; the confirmed minimal vector is READY + valid durable result -> Execution Prep.
- Distinct reproduction vectors: READY plus result routes Execution Prep; blocked plus result routes Execution; planned plus result sibling variant.
- Existing reproduction artifacts: READY/blocked fixture scripts in source reports, including S016-F03, S023-F04 and S028-F04.
- Source limitations: READY and blocked variants may require separate repair interactions; this verdict is anchored to the independently reproduced READY vector.
- Current ownership hypothesis: `canonical_pw_v2`
- Downstream relevance hypothesis: `blocks_pre_m03_if_confirmed`
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H025.md`
- Current candidate check: `persists` at `aa729e9a3b06af6e90a6884f8613629d6cd519f0`

## H026 — JIT lifecycle can be omitted from routing and terminal completeness

- Source classes:
  - PWV2:C009
- Exact historical subject: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Frozen current candidate: elmakus/project_workflow_v2@aa729e9a3b06af6e90a6884f8613629d6cd519f0
- Independent-report frequency: 8 independent PWv2 source audits
- Claimed invariant/requirement: EXECUTION_PREP JIT waiting/satisfied/consumed; STATE Task Board; CLOSE end-of-approved-scope.
- Observed historical behavior: a Board with all materialized Cards DONE and a valid JIT trigger in `satisfied` state passes Board validation, but the selector computes terminality from Card statuses and routes Close without dispatching the satisfied JIT obligation. A sibling vector accepts `consumed` after a DONE predecessor/result without a durable consumed-by/materialized-downstream-Card binding.
- Technical verdict: `CONFIRMED_MATERIAL`
- Current-candidate status: `persists`
- Current-candidate observation: at aa729e9a3b06af6e90a6884f8613629d6cd519f0, `validate_board()` still admits `satisfied` and `consumed` from predecessor completion alone (plus the newer bound late-oversize exception), while mechanical rule `PWV21-K012` depends only on `board.cards` and routes all-DONE Cards to Close. The later live-finding/JIT reconciliation branch is below K012 and does not give an ordinary satisfied JIT trigger precedence over terminal routing.
- Smallest relevant implementation boundary: Task Board JIT lifecycle validation in `tools/state_contract.py::validate_board()` plus terminal selection in `tools/router.py` / mechanical predicate `board_all_cards_done` and rule `PWV21-K012`.
- Useful future regression-test shape: (1) all-DONE Cards + one valid `satisfied` trigger must not route Close; (2) `consumed` without exact durable downstream materialization proof must be rejected or remain nonterminal; (3) a genuinely consumed trigger bound to the exact materialized downstream Card must preserve normal terminal routing only after no authorized obligation remains.
- Important limitations: the verdict is anchored to the repeatedly rediscovered `satisfied`-trigger vector. The missing consumed-by proof is a sibling in the same lifecycle family and may require a separate implementation change. Source reports disagreed only about whether Close could theoretically bounce back; the production selector itself still hands Close an already-authorized satisfied trigger.
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H026.md`
- Current candidate check: `persists` at `aa729e9a3b06af6e90a6884f8613629d6cd519f0`

## H027 — Close to end-of-scope stop may be disconnected from production selector

- Source classes:
  - PWV2:C020
- Exact historical subject: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Frozen current candidate: elmakus/project_workflow_v2@aa729e9a3b06af6e90a6884f8613629d6cd519f0
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: ROUTER Close/end-of-scope semantics; CLOSE true-end helper; USER_STOP.
- Observed historical behavior: all-DONE Task Board state routes `select_route()` to `route/close`. Re-running unchanged durable state repeats `route/close`. `tools/close_contract.py::close_continuation()` can independently derive `end_of_scope_stop`, but the production selector neither imports/calls it nor accepts durable Close-completion inputs that can turn the documented Close continuation into a real selector stop.
- Technical verdict: `CONFIRMED_MATERIAL`
- Current-candidate status: `persists`
- Current-candidate observation: `PWV21-K012` still maps all-DONE `board.cards` to `route/close`; current `tools/router.py` contains no `close_continuation` or `end_of_scope_stop` path. Current `tools/close_contract.py` still returns `end_of_scope_stop` only as a separate helper result, and current tests exercise the helper independently rather than an end-to-end selector transition.
- Smallest relevant implementation boundary: the boundary between `tools/router.py` / `PWV21-K012` and `tools/close_contract.py::close_continuation()`, including representation/readback of durable Close completion and conversion to a real `RouteResult(stop, end_of_scope_stop)` that loads USER_STOP.
- Useful future regression-test shape: drive one fixture from all-DONE -> Close ownership -> durable Close completion -> the same production routing entrypoint returning a real `end_of_scope_stop`; assert unchanged pre-completion state continues Close; assert an authorized remaining obligation prevents the stop.
- Important limitations: singleton source finding. The module split could be intentional only if another production composition layer is the documented owner of Close continuation, but no such selector integration or durable input path is present in the exact historical/current production router inspected here.
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H027.md`
- Current candidate check: `persists` at `aa729e9a3b06af6e90a6884f8613629d6cd519f0`

## H028 — SessionStart can accept semantically destroyed router content if markers survive

- Source classes:
  - PWV2:C012
- Exact historical subject: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Frozen current candidate: elmakus/project_workflow_v2@aa729e9a3b06af6e90a6884f8613629d6cd519f0
- Independent-report frequency: 6 independent PWv2 source audits
- Claimed invariant/requirement: SessionStart/Skill fail-closed bootstrap; installed canonical router authority.
- Observed historical behavior: `hooks/session-start.py::canonical_router()` establishes router content validity by requiring only two substrings, the V2 router header and production-selector sentence. A truncated/counterfeit router retaining those strings is returned as canonical and `build_context()` advertises the package as enabled rather than emitting the blocking package error.
- Technical verdict: `CONFIRMED_MATERIAL`
- Current-candidate status: `persists`
- Current-candidate observation: the hook's `canonical_router()` implementation and the relevant malformed-router negative test are materially unchanged at aa729e9a3b06af6e90a6884f8613629d6cd519f0; no manifest/hash/version/content-integrity binding was added. The test still uses `not a V2 router`, which removes both required sentinels and therefore does not cover marker-preserving semantic destruction.
- Smallest relevant implementation boundary: `hooks/session-start.py::canonical_router()` and its package-integrity contract/tests; any repair should authenticate the installed router/package strongly enough that marker-preserving truncation or stale payload cannot be certified as canonical.
- Useful future regression-test shape: temporary installed package with an otherwise valid hook and a router containing both accepted sentinels but no routing semantics must produce the blocking package error; add a contradictory/stale marker-preserving body case and a positive exact-installed-package case.
- Important limitations: some source auditors interpreted installed-package trust as sufficient and did not promote this class. The confirmed defect is specifically the hook's explicit claim to fail closed on malformed router authority while its implemented content test accepts semantically empty marker-preserving content.
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H028.md`
- Current candidate check: `persists` at `aa729e9a3b06af6e90a6884f8613629d6cd519f0`

## H029 — Lexically safe locator can escape semantic root after filesystem resolution

- Source classes:
  - PWV2:C014
- Exact historical subject: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Frozen current candidate: elmakus/project_workflow_v2@aa729e9a3b06af6e90a6884f8613629d6cd519f0
- Independent-report frequency: 2 independent PWv2 source audits
- Claimed invariant/requirement: AUTHORITY/WORKSTREAM class confinement; traversal/cross-workstream fail-closed rule.
- Observed historical behavior: locator validation uses `PurePosixPath` and raw prefix/exact-path checks, but `Reads._read_path()` resolves the accepted path with host filesystem semantics and only rechecks containment under the broad project/package root. A repository symlink can therefore keep an authority-looking lexical path while resolving outside that authority class root; on Windows a backslash-containing component can similarly evade POSIX `..` token checks and normalize across a workstream boundary.
- Technical verdict: `CONFIRMED_MATERIAL`
- Current-candidate status: `persists`
- Current-candidate observation: both `_safe_relative_path()` and `Reads._read_path()` retain the same semantic structure at aa729e9a3b06af6e90a6884f8613629d6cd519f0; the latter still records the declared raw locator after resolution and verifies only broad-root containment. No symlink semantic-root or backslash negative test is present in the current state-contract suite.
- Smallest relevant implementation boundary: locator class/workstream validation in `tools/state_contract.py::validate_locator()` plus filesystem realization in `tools/router.py::Reads._read_path()`; the resolved path must preserve the same semantic class/workstream confinement as the declared locator under supported host separator/symlink semantics.
- Useful future regression-test shape: (1) authority locator `workflow/ALIAS.md` symlinked to an in-repo non-authority directory must fail closed; (2) Task Card locator containing Windows backslash traversal must fail before host resolution on Windows semantics; (3) valid in-root nonescaping paths and valid symlinks that remain inside the same allowed semantic root retain expected behavior if symlinks are intentionally supported.
- Important limitations: the Windows traversal impact is platform-conditional. The verdict is independently anchored by the in-repository symlink vector, which does not require Windows. The newer exact Git blob reader solves separate immutable-subject readback paths and does not change the working-tree `Reads._read_path()` semantic-root behavior under test here.
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H029.md`
- Current candidate check: `persists` at `aa729e9a3b06af6e90a6884f8613629d6cd519f0`

## H030 — Malformed TOML parse error can escape Recovery

- Source classes:
  - PWV2:C015
- Exact historical subject: elmakus/project_workflow_v2@4fb4bfb7d7b1481d6f347c182fc96a5a1135e045
- Frozen current candidate: elmakus/project_workflow_v2@aa729e9a3b06af6e90a6884f8613629d6cd519f0
- Independent-report frequency: 1 independent PWv2 source audit
- Claimed invariant/requirement: malformed durable state must fail closed to Recovery.
- Observed historical behavior: `read_toml()` and `read_project()` delegate TOML parsing to `tomllib`, whose syntax failures raise `tomllib.TOMLDecodeError`. The selector's bootstrap and selected-workstream exception boundaries catch `OSError`, `ValidationError` and selected other contract exceptions, but not `TOMLDecodeError`; malformed durable TOML therefore escapes the selector instead of producing `recovery/recovery_boundary`.
- Technical verdict: `CONFIRMED_MATERIAL`
- Current-candidate status: `persists`
- Current-candidate observation: the current `read_toml()/read_project()` parse behavior is unchanged, and the main `select_route()` catch boundaries still omit `tomllib.TOMLDecodeError`. The state-contract CLI explicitly catches that exception, demonstrating that the exception class is known elsewhere but is not normalized by the production selector. Current router tests contain no malformed-TOML negative case.
- Smallest relevant implementation boundary: selector-side TOML read/exception normalization across `tools/state_contract.py::read_toml()/read_project()` and `tools/router.py::select_route()`; syntactic durable-state corruption must be converted to deterministic Recovery at every selector read boundary.
- Useful future regression-test shape: mutate each selector-owned TOML surface one at a time to invalid syntax such as `revision = [`; assert `select_route()` returns `disposition=recovery`, `obligation=recovery_boundary`, and never raises `TOMLDecodeError`; retain a valid-TOML semantic-invalid control for `ValidationError`.
- Important limitations: singleton source finding and no source-side fresh selector run. The technical reproduction is nevertheless direct from the exact exception types and catch lists in both immutable subjects; Python `tomllib` syntax errors are outside the caught exception set.
- Technical status: `confirmed_material`
- Reproduction status: `reproduced`
- Final disposition: `pending_repair`
- Evidence: `audits/pwv21-pre-m03-bug-harvest/evidence/H030.md`
- Current candidate check: `persists` at `aa729e9a3b06af6e90a6884f8613629d6cd519f0`

