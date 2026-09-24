# M02R-T03 Shadow Review — Consolidated Independent Results

## Aggregation scope

This document aggregates four already-completed out-of-band M02R-T03 shadow reviews. It performs aggregation only and no new product review, technical confirmation, rejection, repair, or Project Workflow state transition.

Exact audited consumer subject:

- Repository: elmakus/chatgpt-codex-project-workflow
- Commit: 5b76ffe03259ff141afc6bfb5b7b546041a48b41
- Result: implementation/workstreams/change-pwv21-policy-kernel-brainstorming/results/M02R-T03-R02.md
- Result blob: b357ba85d4975540f3ae87b05e73e3fcf8e0471a

Exact implementation subject:

- Repository: elmakus/project_workflow_v2
- Commit: 180cc0af3a9b56c8c2808827bf5548b8ae040608

Source reviews: 4.

Sources are ordered lexicographically by branch, establishing stable source IDs S1 through S4:

1. S1 — audit/m02r-t03-shadow-7owwquaz2gljnl8aioqpf82z — audit commit 78ae6bd1fcbf0e88947a006650db5cba7c06af7e
2. S2 — audit/m02r-t03-shadow-86q4mx6pv3d78czadwdq1h6d — audit commit 3ef63c9c8694d4a33a13b48c98a10b162e1ed306
3. S3 — audit/m02r-t03-shadow-qtwej69101xxxxiuw6a79wly — audit commit b0b613182c46b7189b55d21a8b63fde6959fcf63
4. S4 — audit/m02r-t03-shadow-wnr27ullcdxw8xumgpiiuth1 — audit commit 2bbd4916a9de6e306c533057da681cc15e6fc1da

No formal R01/R02 evidence, canonical PWv2 swarm audit, aggregation branch, or triage branch is treated as a source review.

## Executive summary

- Reviews reporting CLEAN: 0 / 4
- Reviews reporting FINDINGS FOUND: 4 / 4
- Total original material findings before deduplication: 12
- Number of clustered candidate defect classes: 4
- Number of findings that appear unique to one reviewer: 0
- Number of clusters independently reported by 2+ reviewers: 4

These counts describe only the four persisted source reports. Independent rediscovery is not treated as technical confirmation.

## Source review matrix

| Source | Branch | Original verdict | Material findings | Limitations |
| --- | --- | --- | ---: | --- |
| S1 | audit/m02r-t03-shadow-7owwquaz2gljnl8aioqpf82z | FINDINGS FOUND | 3 | Additional local probes were not executed because the available remote execution connection had exhausted its usage allowance. Findings were recorded as deterministic code-path analyses against the exact repaired source. |
| S2 | audit/m02r-t03-shadow-86q4mx6pv3d78czadwdq1h6d | FINDINGS FOUND | 4 | Did not independently execute a clean local clone. The report notes formal evidence of a 258-test passing suite and exact-head CI, while its own findings were negative-space cases outside those reported probes. |
| S3 | audit/m02r-t03-shadow-qtwej69101xxxxiuw6a79wly | FINDINGS FOUND | 2 | No explicit execution-environment limitation was stated. The report deliberately treated missing full Final/router lifecycle wiring and the per-Card nature of the helper as later M05 integration rather than separate findings. |
| S4 | audit/m02r-t03-shadow-wnr27ullcdxw8xumgpiiuth1 | FINDINGS FOUND | 3 | A separate fresh local clone was not practical because the network clone attempt could not resolve GitHub. Findings were based on concrete static execution paths in the exact pinned source. |

## Candidate defect-class clusters

### C01 — Final reconciliation can derive an incomplete canonical observation history

- Independently reported by: 4 / 4 reviewers
- Source findings:
  - S1-F1 — The “truncation-proof” Final gate can lose an entire durable observation history
  - S2-F3 — The authoritative Final gate can silently omit observations from sibling Cards
  - S3-F1 — The supposedly truncation-proof Final gate can lose history by truncating the Task Board itself
  - S4-F1 — The “truncation-proof” Final gate is still truncatable through the Task Board
- Affected requirements/contracts mentioned by sources: PWV21-REQ-134, PWV21-REQ-135, and M02R-T03 acceptance requiring no silent observation loss and complete pre-Final reconciliation.
- Shared core claim: the Final reconciliation helper can derive its canonical observation set from a board/history slice that the sources say is not proven complete, allowing durable observations outside that slice to be omitted.
- Important differences between source reports:
  - S1, S3, and S4 focus on a previously durable review attempt being removed from the current Card review_attempts locator list.
  - S2 focuses on a sibling Card containing an open observation while Final is invoked only for another Card.
  - S1 also notes the sibling-Card variant.
  - S3 additionally reports a malformed duplicate-Card shadowing variant because the helper itself does not call validate_board and selects the first matching Card.
- Reproduction/counterexample summaries from each source:
  - S1-F1: an old review file still contains open O1, but the current Board has review_attempts = []; Final receives observations = [] and derives an empty canonical set.
  - S2-F3: Card A is reconciled, Card B retains open O-B1; invoking the helper for card_id A can succeed without examining Card B.
  - S3-F1: Board revision N lists R01 with O1, a later Board revision removes R01, and Final derives empty history; a second malformed-state sibling uses duplicate Card IDs with the empty one selected first.
  - S4-F1: an earlier review attempt containing O1 remains durable, but its locator is removed from the current Board; the helper reads zero attempts and can complete reconciliation.
- Why sources considered it load-bearing: each source says this can permit Final completion while a durable unreconciled observation still exists, directly violating the silent-loss/completeness guarantee.
- Source confidence/limitations: all four froze these as material findings. S1 and S4 explicitly relied on static/code-path analysis because local execution was unavailable; S2 did not perform a clean local clone; S3 stated no explicit execution limitation.
- Aggregator note: OVERLAPPING / NEEDS TRIAGE. The sources converge on incomplete Final-history derivation, but not all use the same omission vector.

### C02 — Observation provenance can bind to a dangling or nonexistent evidence artifact

- Independently reported by: 2 / 4 reviewers
- Source findings:
  - S1-F2 — Observation provenance can point to review evidence that does not exist
  - S2-F2 — Observation provenance can still terminate at a nonexistent evidence artifact
- Affected requirements/contracts mentioned by sources: PWV21-REQ-134, durable provenance/origin binding, and fail-closed handling of dangling references.
- Shared core claim: matching an observation evidence locator to the review's declared evidence_path does not, according to these sources, establish that the referenced evidence artifact actually exists durably.
- Important differences between source reports: no material disagreement. S2 additionally emphasizes that the board-bound Final path reads the review-attempt TOML but does not Git-verify the referenced review evidence artifact itself.
- Reproduction/counterexample summaries from each source:
  - S1-F2: review evidence_path is a safe-looking DOES_NOT_EXIST.md path and observation evidence uses the same path plus #O1; string binding passes despite no artifact.
  - S2-F2: a terminal attempt and observation point consistently to DOES_NOT_EXIST.md; provenance validation succeeds because the strings agree.
- Why sources considered it load-bearing: both state that REQ-134 requires durable traceability, and a syntactically matching dangling path can become the canonical historical origin without proving durable evidence exists.
- Source confidence/limitations: both froze the issue as material. S1 did not run additional local probes; S2 did not execute a clean local clone.
- Aggregator note: SAME CLASS.

### C03 — Cleanup completion can be accepted from self-attested subject, evidence, and review claims

- Independently reported by: 4 / 4 reviewers
- Source findings:
  - S1-F3 — Cleanup completion can still be fabricated without an actual reviewed cleanup subject
  - S2-F4 — Fake-but-well-shaped cleanup still satisfies Final reconciliation
  - S3-F2 — Cleanup review/evidence is still self-asserted rather than bound to durable truth
  - S4-F2 — Cleanup completion is still self-attested rather than bound to an actual exact subject and independent review
- Affected requirements/contracts mentioned by sources: PWV21-REQ-136 and M02R-T03 cleanup acceptance requiring an exact cleanup subject, tests/evidence, independent GREEN review, and bounded/non-speculative scope.
- Shared core claim: validate_cleanup_work checks the shape of cleanup subject/evidence/review fields, but the sources say it does not durably read back and bind those claims to a real exact subject, real tests/evidence, and a real independent GREEN review.
- Important differences between source reports:
  - S1 emphasizes nonexistent subject/evidence plus an asserted independent_review_green boolean.
  - S2 additionally notes a path such as ../../does-not-exist.md is not passed through normal safe-relative-path validation in that path.
  - S3 highlights that speculative_redesign and new_product_scope are caller-supplied flags and points to a positive test fixture using fabricated 40-hex identities.
  - S4 similarly notes speculative/new-product properties are not derived from accepted authority or the cleanup subject.
- Reproduction/counterexample summaries from each source:
  - S1-F3: supply structurally valid arbitrary 40-hex commit/blob values, a nonexistent result path and test/evidence path, complete = true, and independent_review_green = true.
  - S2-F4: use a non-empty repository/path, arbitrary 40-hex subject identities, nonexistent tests_evidence, and independent_review_green = true; the source also cites an unsafe relative-path variant.
  - S3-F2: provide a fabricated exact-subject-shaped object with arbitrary a*40/b*40 identities, arbitrary test pathname, complete = true, and independent_review_green = true; the source says the repository's own positive fixture demonstrates acceptance of such shape-valid data.
  - S4-F2: provide cleanup work covering a real cleanup_candidate but with invented a*40/b*40 subject identities, a not-real evidence string, complete = true, and independent_review_green = true.
- Why sources considered it load-bearing: all four say a cleanup_candidate can be treated as completed and cease blocking Final without proof that the cleanup implementation, evidence, and independent review actually exist and bind to one another.
- Source confidence/limitations: all four froze the issue as material. S1 and S4 explicitly note static analysis constraints; S2 lacked a clean local clone; S3 stated no explicit execution limitation.
- Aggregator note: SAME CLASS.

### C04 — A newly authored legacy-shaped RED can receive the historical compatibility exemption

- Independently reported by: 2 / 4 reviewers
- Source findings:
  - S2-F1 — A brand-new RED can impersonate a legacy review and bypass load-bearing evidence
  - S4-F3 — A newly created legacy-shaped RED can still bypass all PWv2.1 load-bearing evidence requirements
- Affected requirements/contracts mentioned by sources: PWV21-REQ-133 and M02R-T03 acceptance requiring concrete materially load-bearing evidence for RED.
- Shared core claim: the compatibility path distinguishes legacy review state by old schema shape rather than durable historical provenance, so a newly created initial terminal RED can omit the new PWv2.1 evidence fields and be treated as legacy.
- Important differences between source reports: no material disagreement. S4 explicitly frames the issue as historicity inferred from schema shape; S2 describes the same legacy-impersonation vector.
- Reproduction/counterexample summaries from each source:
  - S2-F1: create a new terminal R01 with the current subject, independence and terminal evidence but verdict = red while omitting review_kind, material_finding_ids, and finding_severity; the initial legacy prefix accepts it.
  - S4-F3: create the first review attempt in legacy shape with verdict = red and omit review_kind, material_finding_ids, and finding_severity; the history validator accepts it as legacy history.
- Why sources considered it load-bearing: both say the path can manufacture a blocking RED and trigger correction/recovery without the load-bearing evidence REQ-133 requires.
- Source confidence/limitations: both froze this as material. S2 did not run a clean local clone; S4 could not perform a separate fresh clone because GitHub DNS resolution failed.
- Aggregator note: SAME CLASS.

## Unique findings

No original material finding is unique to a single reviewer at the candidate defect-class level used by this aggregation.

All 12 source findings map to a cluster independently reported by at least two reviewers. This does not mean every reproducer is duplicated: C01 contains reviewer-specific omission variants, especially sibling-Card omission and malformed duplicate-Card shadowing, which are preserved separately for later triage.

## Clean-review coverage

No source reviewer returned CLEAN. Therefore there is no CLEAN-review coverage to compare.

## Cross-review coverage matrix

YES means the source report explicitly says the area was checked/exercised. PARTIAL means it was mentioned or inspected without strong falsification. NO/UNKNOWN means the source report does not establish coverage. This matrix does not infer coverage from silence.

| Coverage area | S1 | S2 | S3 | S4 |
| --- | --- | --- | --- | --- |
| load-bearing/advisory classification | YES | YES | YES | YES |
| RED evidence requirements | YES | YES | YES | YES |
| observation provenance | YES | YES | YES | YES |
| silent/truncated history | YES | YES | YES | YES |
| no-downgrade behavior | YES | YES | YES | YES |
| tracker non-authority | YES | YES | YES | YES |
| Final reconciliation completeness | YES | YES | YES | YES |
| five dispositions | YES | YES | YES | YES |
| cleanup exact subject/evidence/review | YES | YES | YES | YES |
| speculative/new-scope cleanup | YES | YES | YES | YES |
| stale/malformed state | YES | YES | YES | YES |
| sibling/negative-space cases | YES | YES | YES | YES |
| BOOT-B/C/D scope leakage | YES | YES | YES | YES |

Execution depth differed despite the common declared coverage. S1 and S4 explicitly report environment constraints that prevented fresh local execution; S2 did not perform a clean local clone; S3 does not state a comparable execution limitation.

## Post-freeze comparisons

These comparisons were added by source reviewers only after their independent verdicts and material finding sets were frozen. They do not alter the original counts above.

### S1 post-freeze comparison

S1 read formal R01/R02 only after freezing three findings. It says R01 had four blockers and that the repaired subject closed the literal reproducers for all four; S1 specifically agreed that the R01 evidence-free-RED issue was materially fixed. S1 nevertheless disagreed with formal R02 GREEN because it reported adjacent negative-space bypasses in provenance, Final-history completeness, and cleanup proof.

### S2 post-freeze comparison

S2 compared its four frozen findings to formal R01/R02 and disagreed with R02 GREEN. It mapped each frozen finding to one of the four prior R01 semantic classes: legacy-shaped RED bypass, dangling provenance, sibling-Card Final omission, and fake-but-well-shaped cleanup. S2 notes that R02 intentionally accepted legacy pre-review_kind RED for compatibility but, in S2's view, did not establish durable historical provenance for that exemption.

### S3 post-freeze comparison

S3 froze two findings before comparison. It says the repaired subject convincingly closed R01 F1 severity omission and R01 F2 provenance mismatch. Its two findings were presented as deeper variants of R01 F3 and F4: Task-Board locator truncation and self-asserted cleanup proof. S3 says these cases were not covered by the R02 probes it describes.

### S4 post-freeze comparison

S4 froze three findings before comparison and says formal R02 correctly confirmed closure of the literal R01 reproducers. It nevertheless reports one-layer-deeper bypasses for observation-history completeness, cleanup self-attestation, and legacy RED compatibility. Its original FINDINGS FOUND verdict remained unchanged.

## Full source-finding ledger

### S1-F1 — The “truncation-proof” Final gate can lose an entire durable observation history

- Source branch: audit/m02r-t03-shadow-7owwquaz2gljnl8aioqpf82z
- Original affected requirement/contract: PWV21-REQ-134, PWV21-REQ-135, and M02R-T03 acceptance requiring no silent observation loss and complete pre-Final reconciliation.
- Expected behavior: Final reconciliation should account for the complete durable observation history and reject silent loss.
- Actual behavior reported by source: the helper reads only the selected Card's current review_attempts and can derive an empty canonical set if that current list is empty, without proving the locator history is append-only or complete.
- Reproduction/counterexample: keep reviews/M01-T01-R01.toml with open O1, change the current Task Board Card to review_attempts = [], propose observations = [], and invoke the board-bound Final helper. The source says history validation is skipped and reconciliation can complete. It also records a sibling-Card variant.
- Load-bearing rationale: durable review evidence can contain an unreconciled observation while Final reports success.
- Defect-class/sibling notes: source classification was recurrence / negative-space sibling of the known incomplete-history semantic class; sibling Card scope was explicitly noted.
- Original confidence: no numeric confidence was stated; this was frozen as a material finding under FINDINGS FOUND.
- Relevant original limitations: no additional local probes because the remote execution connection had exhausted its usage allowance; source relied on deterministic code-path analysis.

### S1-F2 — Observation provenance can point to review evidence that does not exist

- Source branch: audit/m02r-t03-shadow-7owwquaz2gljnl8aioqpf82z
- Original affected requirement/contract: PWV21-REQ-134 and the requirement for durable traceability to originating review evidence.
- Expected behavior: an observation origin should remain durably traceable to an existing originating review evidence artifact.
- Actual behavior reported by source: provenance checks bind the observation evidence locator string to the review evidence_path string but do not read back the referenced artifact to prove it exists.
- Reproduction/counterexample: use review evidence_path implementation/workstreams/sample/evidence/DOES_NOT_EXIST.md and observation evidence with the same path plus #O1. The source says the strings bind successfully even though the artifact can be absent or stale.
- Load-bearing rationale: a dangling path can become canonical historical provenance despite not providing durable traceability.
- Defect-class/sibling notes: recurrence / negative-space sibling of the known provenance semantic class.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: no additional local probes due exhausted remote execution allowance.

### S1-F3 — Cleanup completion can still be fabricated without an actual reviewed cleanup subject

- Source branch: audit/m02r-t03-shadow-7owwquaz2gljnl8aioqpf82z
- Original affected requirement/contract: PWV21-REQ-136 and exact M02R-T03 cleanup acceptance.
- Expected behavior: cleanup should have its own real exact subject, real tests/evidence, and a real independent GREEN review before Final.
- Actual behavior reported by source: structural fields and booleans are checked, but the exact subject, evidence, and independent review are not durably read back or bound to one another.
- Reproduction/counterexample: for cleanup_candidate O1, provide arbitrary 40-hex commit/blob values, a nonexistent result path, nonexistent tests/evidence path, complete = true, and independent_review_green = true.
- Load-bearing rationale: Final can treat cleanup as covered even if the cleanup implementation, evidence, and independent review do not exist.
- Defect-class/sibling notes: recurrence / negative-space sibling of the known cleanup-proof semantic class.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: no additional local probes due exhausted remote execution allowance.

### S2-F1 — A brand-new RED can impersonate a legacy review and bypass load-bearing evidence

- Source branch: audit/m02r-t03-shadow-86q4mx6pv3d78czadwdq1h6d
- Original affected requirement/contract: PWV21-REQ-133 and M02R-T03 acceptance requiring concrete materially load-bearing evidence for RED.
- Expected behavior: a newly authored PWv2.1 RED should provide the required material finding and severity evidence; only genuinely historical records should receive compatibility treatment.
- Actual behavior reported by source: a new initial terminal review can omit review_kind, material_finding_ids, and finding_severity and be accepted as legacy-shaped history.
- Reproduction/counterexample: create a new R01 carrying the current Card/result subject, valid independence and terminal evidence, verdict = red, while omitting the new PWv2.1 evidence fields.
- Load-bearing rationale: a RED can block GREEN and drive correction/recovery without concrete load-bearing evidence.
- Defect-class/sibling notes: recurrence/incomplete closure of the evidence-free-RED semantic class through legacy impersonation.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: no independent clean local clone; the source explicitly separates its negative-space findings from formal passing-test/CI evidence.

### S2-F2 — Observation provenance can still terminate at a nonexistent evidence artifact

- Source branch: audit/m02r-t03-shadow-86q4mx6pv3d78czadwdq1h6d
- Original affected requirement/contract: PWV21-REQ-134, durable provenance/origin binding, and fail-closed dangling-reference handling.
- Expected behavior: observation provenance should terminate at a durable originating evidence artifact.
- Actual behavior reported by source: the attempt evidence_path and observation evidence locator can agree while pointing to a nonexistent artifact; the board-bound Final path does not Git-verify the evidence artifact.
- Reproduction/counterexample: set both the review and observation to implementation/workstreams/ws/evidence/DOES_NOT_EXIST.md, with the observation adding #O1.
- Load-bearing rationale: self-consistent dangling strings are not durable traceability.
- Defect-class/sibling notes: recurrence/incomplete closure of the known provenance class; repaired mismatched provenance but allegedly not dangling provenance.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: no independent clean local clone.

### S2-F3 — The authoritative Final gate can silently omit observations from sibling Cards

- Source branch: audit/m02r-t03-shadow-86q4mx6pv3d78czadwdq1h6d
- Original affected requirement/contract: PWV21-REQ-135 and the requirement that Final cannot complete with an unreconciled open observation.
- Expected behavior: the authoritative Final reconciliation surface should cover all relevant observations, including those on sibling Cards.
- Actual behavior reported by source: the helper enumerates only the Card named by card_id and can ignore another terminal Card containing an open observation.
- Reproduction/counterexample: Card A is fully reconciled; Card B retains O-B1 = open; call the helper for card_id A with A's reconciled observations.
- Load-bearing rationale: correctness depends on an external caller invoking the gate for every relevant Card, while the helper can certify one Card's slice with another open observation still durable.
- Defect-class/sibling notes: recurrence/incomplete closure of the incomplete-Final-reconciliation class through sibling-Card/history truncation.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: no independent clean local clone; broader lifecycle wiring itself was not classified as the defect.

### S2-F4 — Fake-but-well-shaped cleanup still satisfies Final reconciliation

- Source branch: audit/m02r-t03-shadow-86q4mx6pv3d78czadwdq1h6d
- Original affected requirement/contract: PWV21-REQ-136 and the cleanup-candidate contract requiring exact subject, tests/evidence, and independent GREEN review.
- Expected behavior: cleanup proof should establish actual subject/evidence/review identity and existence.
- Actual behavior reported by source: syntactically complete cleanup claims can pass without Git-readback of subject, readback of tests/evidence, or binding of the GREEN assertion to an exact independent review.
- Reproduction/counterexample: arbitrary 40-hex subject identities, nonexistent tests_evidence, complete = true, independent_review_green = true; the source also notes a ../../does-not-exist.md path variant.
- Load-bearing rationale: Final can certify cleanup when implementation, evidence, or independent review may all be fabricated.
- Defect-class/sibling notes: recurrence/incomplete closure of the unbound-cleanup semantic class.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: no independent clean local clone.

### S3-F1 — The supposedly truncation-proof Final gate can lose history by truncating the Task Board itself

- Source branch: audit/m02r-t03-shadow-qtwej69101xxxxiuw6a79wly
- Original affected requirement/contract: PWV21-REQ-134, PWV21-REQ-135, and acceptance requiring durable observation retention, rejection of silent loss, and complete pre-Final reconciliation.
- Expected behavior: the Board-bound Final gate should establish complete durable history, not just completeness relative to the current locator list.
- Actual behavior reported by source: removing an older review locator from the current Board makes the gate forget that review; the helper also allegedly does not call validate_board before selecting the first matching Card.
- Reproduction/counterexample: Board revision N lists R01 containing open O1; a later Board revision uses review_attempts = []; Final with observations = [] can complete. A sibling malformed-state reproducer uses duplicate Card IDs where the first has empty history and the second has the real history.
- Load-bearing rationale: a durable open observation can silently disappear from the canonical set Final evaluates.
- Defect-class/sibling notes: recurrence/deeper bypass of R01 F3; source says the repair closed caller-input truncation but not truncation of the canonical pointer set.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: no explicit execution-environment limitation stated; full Final/router wiring and per-Card composition were treated as later M05 scope rather than separate defects.

### S3-F2 — Cleanup review/evidence is still self-asserted rather than bound to durable truth

- Source branch: audit/m02r-t03-shadow-qtwej69101xxxxiuw6a79wly
- Original affected requirement/contract: PWV21-REQ-136 and exact cleanup acceptance requiring exact subject, tests/evidence, independent GREEN review, and bounded scope.
- Expected behavior: cleanup certification should be durably bound to an actual subject, actual evidence/test execution, and actual independent review.
- Actual behavior reported by source: the validator accepts shape-valid subject/evidence/review fields without proving existence; speculative_redesign and new_product_scope are caller-supplied booleans.
- Reproduction/counterexample: fabricated a*40/b*40 subject identities, arbitrary test pathname, complete = true, and independent_review_green = true. The source notes the repository's positive helper fixture itself uses fabricated identities.
- Load-bearing rationale: cleanup_candidate can cease blocking Final without the proof required by the Card; scope guards are also self-declared in the input being validated.
- Defect-class/sibling notes: recurrence/deeper bypass of R01 F4; literal bare-Boolean case repaired, broader durable-binding class allegedly remains.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: no explicit execution-environment limitation stated.

### S4-F1 — The “truncation-proof” Final gate is still truncatable through the Task Board

- Source branch: audit/m02r-t03-shadow-wnr27ullcdxw8xumgpiiuth1
- Original affected requirement/contract: PWV21-REQ-134, PWV21-REQ-135, and the requirement that observations cannot silently disappear and Final cannot complete with an unreconciled observation.
- Expected behavior: current Board locators should not allow previously durable observation history to disappear from Final's canonical set.
- Actual behavior reported by source: the helper reads the current review_attempts list but does not prove that list is append-only complete against prior durable state.
- Reproduction/counterexample: an attempt file containing open O1 remains present, but its locator is removed so review_attempts = []; the helper reads zero attempts and derives an empty canonical state.
- Load-bearing rationale: a real open observation can disappear without receiving one of the five terminal dispositions.
- Defect-class/sibling notes: recurrence of the targeted incomplete-observation-set / silent-loss semantic class through a new negative-space vector.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: a fresh local clone was not practical because the network clone attempt could not resolve GitHub; finding derived from static execution paths.

### S4-F2 — Cleanup completion is still self-attested rather than bound to an actual exact subject and independent review

- Source branch: audit/m02r-t03-shadow-wnr27ullcdxw8xumgpiiuth1
- Original affected requirement/contract: PWV21-REQ-136 and cleanup acceptance requiring exact subject, tests/evidence, and independent GREEN review.
- Expected behavior: cleanup completion should be tied to a real exact Git subject, real evidence, and a real independent GREEN review.
- Actual behavior reported by source: the validator checks shape and booleans rather than durable readback and binding; speculative/new-product flags are caller declarations rather than derived properties.
- Reproduction/counterexample: for real cleanup_candidate O2, provide invented a*40/b*40 identities, results/not-real.md, a non-real evidence string, complete = true, and independent_review_green = true.
- Load-bearing rationale: Final can declare cleanup completed even when the cleanup or review never existed.
- Defect-class/sibling notes: recurrence of R01 F4; bare-Boolean reproducer repaired but broader self-attestation class allegedly remains.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: fresh local clone unavailable because GitHub DNS resolution failed.

### S4-F3 — A newly created legacy-shaped RED can still bypass all PWv2.1 load-bearing evidence requirements

- Source branch: audit/m02r-t03-shadow-wnr27ullcdxw8xumgpiiuth1
- Original affected requirement/contract: PWV21-REQ-133 and M02R-T03 evidence-gated RED classification.
- Expected behavior: compatibility should grandfather genuine historical reviews without allowing new RED records to bypass the new evidence gate.
- Actual behavior reported by source: historicity can be inferred from schema shape, so a newly authored first review attempt can omit the new fields and be accepted as legacy history.
- Reproduction/counterexample: create initial R01 with verdict = red, normal subject/acceptance/independence fields, and omit review_kind, material_finding_ids, and finding_severity.
- Load-bearing rationale: an alternate path can manufacture RED and trigger corrective work without satisfying the evidence-gated blocking criterion.
- Defect-class/sibling notes: recurrence/adjacent bypass of the targeted R01 F1 semantic class.
- Original confidence: no numeric confidence was stated; frozen as a material finding.
- Relevant original limitations: fresh local clone unavailable because GitHub DNS resolution failed.

## Aggregator limitations

- No independent product review was performed.
- No source finding was technically confirmed or rejected.
- Similarity grouping is an aggregation judgment only and may itself require later analyst verification.
- Candidate defect-class clusters must not be read as confirmed defects merely because multiple reviewers independently reported them.
- The source REPORT.md files and their META.toml files remain authoritative for each reviewer's original wording, evidence, scope, and limitations.
