# M02R-T03 Shadow Review

## Original independent verdict

FINDINGS FOUND

The frozen independent shadow review found three material defects in the exact repaired implementation subject `elmakus/project_workflow_v2@180cc0af3a9b56c8c2808827bf5548b8ae040608`.

The finding set below is the result reached before any optional comparison with formal R01/R02 review evidence.

## Original material findings

### F1 — The “truncation-proof” Final gate is still truncatable through the Task Board

**Affected requirement/contract:** PWV21-REQ-134, PWV21-REQ-135, and the M02R-T03 requirement that observations cannot silently disappear and Final cannot complete with an unreconciled observation.

**ELI10 explanation:** The repaired Final gate carefully reads every review record currently listed by the Task Board. But it does not prove that the list itself is complete. If an earlier review locator is removed from the Board, the gate can treat that review and its observations as if they never existed.

**Concrete counterexample/reproduction:**

1. A review attempt file exists and contains open observation `O1`.
2. That attempt was previously listed in the Card's `review_attempts`.
3. The current Task Board is changed so that the Card has `review_attempts = []`, while the attempt file itself remains present.
4. `verify_final_observation_reconciliation_from_board(..., observations=[])` reads zero attempts.
5. Because there are no listed attempts, `validate_review_history()` is skipped.
6. The canonical observation state is derived as empty.
7. Final reconciliation can return `final_observation_reconciliation_complete`.

The implementation validates the current locator list but does not prove append-only completeness of that list against prior durable state.

**Why load-bearing:** A real open observation can disappear from the Final gate without ever receiving one of the five required dispositions, defeating the Card's explicit silent-observation-loss protection.

**Original class assessment:** recurrence of the already-targeted R01/F3 semantic class (incomplete observation set / silent observation loss), through a new negative-space vector.

### F2 — Cleanup completion is still self-attested rather than bound to an actual exact subject and independent review

**Affected requirement/contract:** PWV21-REQ-136 and the M02R-T03 cleanup acceptance requiring bounded cleanup to have its own exact subject, tests/evidence, and independent GREEN review.

**ELI10 explanation:** The repair now requires a cleanup entry to contain fields that look like an exact subject, evidence, and a GREEN review. But the validator does not read back those claims. A caller can provide invented hashes, an arbitrary evidence string, and `independent_review_green = true`, and the Final gate can accept the cleanup.

**Concrete counterexample/reproduction:**

For a real `cleanup_candidate` observation `O2`, supply cleanup work shaped like:

```python
{
    "work_id": "cleanup-O2",
    "covers_observation_ids": ["O2"],
    "complete": True,
    "subject": {
        "repository": "owner/repo",
        "commit": "a" * 40,
        "path": "results/not-real.md",
        "blob": "b" * 40,
    },
    "tests_evidence": ["not-a-real-test-or-evidence-object"],
    "independent_review_green": True,
}
```

There need be no actual Git object at that subject and no actual independent review attempt. The cleanup validator checks shape and booleans, not durable readback binding.

Likewise, speculative/new-product cleanup is rejected only when the caller supplies `speculative_redesign = true` or `new_product_scope = true`; those properties are not derived from accepted authority or the cleanup subject.

**Why load-bearing:** Final can declare a cleanup candidate completed even when the purported cleanup or its independent GREEN review never existed, defeating the central REQ-136 guarantee.

**Original class assessment:** recurrence of the already-targeted R01/F4 semantic class. The literal bare-boolean reproducer was repaired, but the broader self-attestation defect class remained open.

### F3 — A newly created legacy-shaped RED can still bypass all PWv2.1 load-bearing evidence requirements

**Affected requirement/contract:** PWV21-REQ-133 and M02R-T03 evidence-gated RED classification.

**ELI10 explanation:** New PWv2.1 RED reviews must show load-bearing evidence, while genuinely historical reviews are grandfathered. The validator decides that a review is historical largely because it omits the new fields. A newly authored review can therefore wear the old schema and bypass the evidence requirement.

**Concrete counterexample/reproduction:**

Create the first review attempt in legacy shape:

```toml
attempt = "R01"
verdict = "red"
evidence_path = "evidence/review-R01.md"

[subject]
class = "git_blob"
repository = "owner/repo"
commit = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
path = "results/result.md"
blob = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

[acceptance]
class = "authority"
path = "requirements/PROJECT_WORKFLOW_V2.md"

[independence]
materially_produced_or_repaired_subject = false
basis = "Independent reviewer."
```

Omit `review_kind`, `material_finding_ids`, and `finding_severity`. As an initial terminal record, the history validator accepts this as legacy history, allowing RED without any PWv2.1 load-bearing severity evidence.

Supporting genuine historical records is not the defect. The defect is that historicity is inferred from schema shape rather than bound to durable provenance proving that the record is actually historical.

**Why load-bearing:** This creates an alternate route to manufacture RED and trigger corrective work without satisfying the Card's evidence-gated blocking criterion.

**Original class assessment:** recurrence/adjacent bypass of the already-targeted R01/F1 semantic class.

## Original non-blocking observations

- Observation provenance was strengthened: the original mismatched-path case is rejected because observation evidence is now bound to the originating attempt's `evidence_path`. Common tracker/Issue provenance forms are also rejected.
- All five required terminal dispositions are represented: `resolved`, `cleanup_candidate`, `deferred`, `promoted`, and `tracked`. The Final helper rejects `open`, unknown dispositions, omitted observations relative to the history it sees, fabricated IDs, and disposition relabeling.
- The no-downgrade machinery rejects reuse of a load-bearing finding identity as an advisory observation within an epoch, including history-level cases. No separate convenience-downgrade bypass was frozen beyond F3.
- Non-recursive cleanup behavior was correct: merely setting `further_advisory_improvement_conceivable = true` does not reopen completed cleanup.
- No substantive BOOT-B/C/D implementation leakage was found in the reviewed repair diff, and no material later-M05 semantics were silently pulled into the Card.

## Original coverage

The completed shadow review checked the complete applicable M02R-T03 surface, not only changed lines:

- load-bearing RED versus advisory GREEN classification;
- all declared load-bearing surfaces;
- missing and empty severity;
- legacy-schema negative space;
- observation introduction, updates, origin binding, and cross-history retention;
- convenience/no-downgrade protections;
- all five terminal observation dispositions;
- omitted, fabricated, and relabelled observation cases;
- Task Board history reconstruction, including empty, dangling, and truncated-history cases;
- tracker/Issue non-authority;
- cleanup candidate coverage;
- cleanup exact-subject/evidence/review binding;
- speculative and new-scope cleanup admission;
- cleanup termination/non-recursion;
- malformed and dangling state behavior;
- BOOT-B/C/D and later-M05 scope leakage.

The exact baseline-to-repair diff and focused tests were inspected. Passing tests were not treated as proof. A separate fresh local clone was not practical in the original environment because the network clone attempt could not resolve GitHub, so the frozen findings were based on concrete static execution paths in the exact pinned source rather than a separate local runtime execution.

## Post-freeze comparison

This section was added only after the independent findings above were frozen. It does not alter the original verdict or finding list.

The formal R02 review was GREEN and correctly confirmed that the literal R01 reproducers had been repaired. The shadow review disagreed with that GREEN because it found three remaining semantic bypasses one layer beyond those literal reproducers:

- For the prior incomplete-observation-history defect, R02 verified completeness relative to the review locators currently listed in the Task Board, but did not establish that the locator list itself was append-only complete. F1 preserves that negative-space recurrence.
- For the prior bare-cleanup defect, R02 verified that cleanup carries subject-shaped data, evidence-shaped data, and an `independent_review_green` boolean. F2 preserves the broader finding that those claims are still self-attested rather than durably read back and bound to a real independent review.
- For the prior missing-RED-severity defect, R02 intentionally preserved legacy review compatibility. F3 preserves the independent finding that a newly created legacy-shaped terminal RED cannot be distinguished mechanically from genuine historical legacy state.

Therefore the original independent shadow verdict remains **FINDINGS FOUND** with exactly the three findings above.
