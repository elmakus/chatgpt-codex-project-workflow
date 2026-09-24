# M02R-T03 Shadow Review

## Original independent verdict

FINDINGS FOUND

The findings below are the independently frozen result reached before reading formal M02R-T03 R01/R02 review evidence.

## Original material findings

### F1 — The “truncation-proof” Final gate can lose an entire durable observation history

**Affected requirement/contract:** PWV21-REQ-134, PWV21-REQ-135, and M02R-T03 acceptance requiring no silent observation loss and complete pre-Final reconciliation.

**ELI10 explanation:** The Final checker looks only at the list of review files currently written on the Task Board. If an old review file containing an open observation still exists but its pointer disappears from the Board, the checker behaves as though that review never happened.

`verify_final_observation_reconciliation_from_board()` selects one Card from the current Board, reads only that Card's current `review_attempts` array, reads only the files named there, and passes those attempts to reconciliation. If the array is empty, history validation is skipped and the canonical observation set is empty. It does not prove that the current locator list is append-only or complete and does not discover orphaned review attempts.

**Concrete counterexample/reproduction:**

```text
reviews/M01-T01-R01.toml still exists
  -> contains observation O1, disposition=open

TASK_BOARD.toml currently says:
  card M01-T01
  review_attempts = []

Final proposal:
  observations = []
```

Calling:

```text
verify_final_observation_reconciliation_from_board(
    ...,
    card_id="M01-T01",
    observations=[]
)
```

takes the path:

```text
refs = []
attempts = []
validate_review_history(...) is skipped
canonical observation set = {}
proposed observation set = {}
=> final_observation_reconciliation_complete
```

A sibling version exists because the helper accepts a single `card_id` and derives history only for that Card; observations owned by another Card are outside that derived set.

**Why load-bearing:** Final reconciliation can report success while durable review evidence containing an unreconciled observation remains in the repository. That is the silent-observation-loss failure M02R-T03 was required to reject.

**Original classification:** recurrence / negative-space sibling of the already-known incomplete-history semantic class.

### F2 — Observation provenance can point to review evidence that does not exist

**Affected requirement/contract:** PWV21-REQ-134 and M02R-T03's requirement for durable traceability to the originating review evidence.

**ELI10 explanation:** The code verifies that the observation says “my evidence is in file X” and that the review also says “my evidence file is X.” It does not verify that file X actually exists.

`validate_observation_provenance()` validates a string relationship between the observation evidence locator and the review's `evidence_path`. State validation requires the review evidence path to be a non-empty safe relative path, but this path is not read back as an existing durable evidence artifact by this provenance path.

**Concrete counterexample/reproduction:**

```toml
verdict = "green"
evidence_path = "implementation/workstreams/sample/evidence/DOES_NOT_EXIST.md"

[[observations]]
id = "O1"
category = "advisory"
evidence = "implementation/workstreams/sample/evidence/DOES_NOT_EXIST.md#O1"
disposition = "open"
disposition_basis = ""
```

The two strings bind correctly, so the provenance relationship passes. The same semantic issue applies to a stale locator whose former evidence has disappeared.

**Why load-bearing:** PWV21-REQ-134 requires observations to remain durably traceable to their originating review evidence. A syntactically matching dangling path is not durable provenance, yet it can become the canonical historical origin of the observation.

**Original classification:** recurrence / negative-space sibling of the already-known provenance semantic class.

### F3 — Cleanup completion can still be fabricated without an actual reviewed cleanup subject

**Affected requirement/contract:** PWV21-REQ-136 and the exact M02R-T03 cleanup acceptance.

**ELI10 explanation:** The repaired helper now asks for a subject and test/evidence strings, but it still trusts those fields and the `independent_review_green = true` assertion without proving that the subject, evidence, or independent GREEN review actually exist and correspond to one another.

`validate_cleanup_work()` structurally checks a non-empty repository/path, 40-hex commit/blob values, non-empty test/evidence strings, observation IDs, scope flags, and an `independent_review_green` boolean. It does not perform Git readback of the exact cleanup subject, read back the evidence, or bind an actual independent review attempt to the same subject.

**Concrete counterexample/reproduction:**

For canonical observation `O1` dispositioned `cleanup_candidate`, supply:

```python
{
    "work_id": "cleanup-O1",
    "complete": True,
    "covers_observation_ids": ["O1"],
    "subject": {
        "repository": "owner/repo",
        "commit": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "path": "results/this-does-not-exist.md",
        "blob": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    },
    "tests_evidence": [
        "evidence/this-test-evidence-does-not-exist.md"
    ],
    "independent_review_green": True,
}
```

Every value satisfies the structural shape checks. Nothing in that path proves that the commit/blob/path exists, the evidence exists, an independent review occurred, that it was GREEN, or that it covered the exact supplied cleanup subject.

**Why load-bearing:** PWV21-REQ-136 requires cleanup to have its own exact subject, tests/evidence, and independent review before Final Integration evaluates the final codebase. A fabricated structural object can satisfy the gate and cause a cleanup observation to be treated as covered.

**Original classification:** recurrence / negative-space sibling of the already-known cleanup-proof semantic class.

## Original non-blocking observations

- The literal RED-without-load-bearing-evidence bypass appeared closed in the repaired subject: explicit PWv2.1 terminal RED discovery requires severity coverage for material findings, while advisory-only observations can coexist with GREEN.
- The five allowed observation dispositions were represented as `resolved`, `cleanup_candidate`, `deferred`, `promoted`, and `tracked`; an `open` observation could not directly pass Final reconciliation.
- Duplicate observation introductions, unknown observation updates, and second reconciliation of an already-terminal observation were rejected.
- The same-ID load-bearing-to-advisory downgrade path within one epoch was guarded.
- Tracker/Issue data was prevented from serving as observation provenance or explicit disposition/epoch authority, and documentation consistently treated trackers as bookkeeping.
- Cleanup termination correctly ignored the mere fact that further advisory improvement was conceivable; completed bounded cleanup was not recursively reopened just because additional advisory improvement could be imagined.
- No implementation leakage into BOOT-B, BOOT-C, or BOOT-D was found in the repaired diff, and no accepted Definition/P6 authority change was observed.
- The absence of direct reconciliation wiring inside `close_continuation()` was not counted as a separate M02R-T03 finding because broader lifecycle wiring was treated as later M05 integration.
- `workflow/CLOSE.md` described the board-bound helper as “truncation-proof” and described cleanup proof more strongly than the implementation actually established; this was noted as a documentation mismatch associated with the material findings.
- Additional local probes were not executed during the original shadow audit because the available remote execution connection had exhausted its usage allowance; the recorded counterexamples were deterministic code-path analyses against the exact repaired source.

## Original coverage

The completed shadow review checked:

- PWV21-REQ-133 load-bearing surfaces, complete RED severity evidence, advisory-only GREEN, and malformed severity cases;
- PWV21-REQ-134 observation introduction, origin binding, durable derivation, update/reconciliation rules, downgrade protection, stale/dangling provenance, and silent-history-loss negative space;
- PWV21-REQ-135 all five dispositions, open/omitted/fabricated observations, Board-bound history, dangling attempt locators, truncated history, malformed/partial Board cases, and tracker non-authority;
- PWV21-REQ-136 cleanup subject identity, tests/evidence, independent GREEN proof, cleanup coverage, speculative/new-scope flags, and non-recursive termination;
- changed implementation modules plus focused review/state/Close tests, not only changed lines;
- exact baseline-to-repaired implementation diff and adjacent unchanged call paths;
- BOOT-B/C/D and later-M05 scope boundaries.

## Post-freeze comparison

Only after freezing the findings above, formal R01/R02 review evidence was read.

Formal R01 had four blockers: RED without severity evidence, provenance pointing at an unrelated review, Final accepting incomplete caller-provided observation history, and cleanup passing with bare completion/review booleans. The repaired implementation closed the literal reproducers for all four; the original shadow audit agreed that R01 F1 was materially fixed.

The frozen shadow result nevertheless disagreed with formal R02 GREEN because it found adjacent negative-space bypasses in three repaired semantic classes:

- provenance: R02 checked a wrong origin path, empty origin, and prefix sibling; the shadow audit found a matching origin path that can itself be dangling/nonexistent;
- Final history completeness: R02 checked omissions from the history currently named by the Board and dangling named locators; the shadow audit found a prior durable attempt omitted from the current Board locator list, so it is never enumerated;
- cleanup proof: R02 checked missing subject/test fields, a false review boolean, malformed SHA, speculative redesign and new scope; the shadow audit found that syntactically plausible but nonexistent subject/evidence plus an unverified `independent_review_green = true` assertion can still satisfy the structural gate.

This comparison did not alter the original verdict or the three frozen material findings.
