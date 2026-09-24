# M02R-T03 Shadow Review

## Original independent verdict

FINDINGS FOUND

## Original material findings

### F1 — The supposedly truncation-proof Final gate can lose history by truncating the Task Board itself

**Affected requirement/contract:** PWV21-REQ-134, PWV21-REQ-135; M02R-T03 acceptance requiring durable observation retention, rejection of silent observation loss, and complete pre-Final reconciliation.

**ELI10 explanation:** The repair made Final read the list of review files from the Task Board instead of trusting a caller-supplied list. But it assumes the Task Board's current list is complete. If an older review is simply removed from that list, Final forgets that review—and therefore forgets its observations.

**Concrete counterexample/reproduction:**

1. Task Board revision N contains `review_attempts = [R01]`.
2. R01 durably contains open observation `O1`.
3. A later Task Board revision contains `review_attempts = []`. The immutable R01 file can remain untouched.
4. `validate_board()` does not compare the list with the previous board revision or enforce append-only review-attempt history.
5. `verify_final_observation_reconciliation_from_board(... observations=[])` reads the current empty list, derives an empty canonical observation set and can return `final_observation_reconciliation_complete`.

There is an additional malformed-state sibling bypass: the Final helper does not call `validate_board()`. It finds the first Card with `next(...)`. A TOML board containing two entries with the same Card ID—first with empty history, second with the real review history—can therefore make the Final helper select the empty one even though `validate_board()` would reject the duplicate.

The existing test named `test_board_gate_accepts_proven_empty_history_and_reviewed_cleanup` does not actually prove historical emptiness; it creates a current board with an empty list and accepts that as proof.

**Why load-bearing:** This directly permits the exact forbidden condition: a durable observation can silently disappear from the set that Final considers canonical, allowing Final reconciliation to succeed while an unreconciled observation still exists in durable review evidence.

**Originally classified as:** Recurrence/deeper bypass of the already-known R01 F3 semantic class. The repair closed truncation of the caller-supplied observation/history input, but not truncation of the canonical pointer set used as its completeness root.

### F2 — Cleanup review/evidence is still self-asserted rather than bound to durable truth

**Affected requirement/contract:** PWV21-REQ-136 and exact M02R-T03 acceptance requiring cleanup to have its own exact subject, tests/evidence and independent GREEN review, with no speculative redesign/new product scope.

**ELI10 explanation:** The validator now asks for a certificate with a commit, blob, test and “review passed” field. But it never checks whether the certificate, test or review actually exists. A correctly formatted fake certificate passes.

**Concrete counterexample/reproduction:** A cleanup object equivalent to this is accepted:

```text
work_id = "cleanup-O2"

subject.repository = "owner/repo"
subject.commit = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
subject.path = "results/cleanup-O2.md"
subject.blob = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

tests_evidence = ["tests/test_cleanup_o2.py"]
covers_observation_ids = ["O2"]
complete = true
independent_review_green = true
```

Nothing in `validate_cleanup_work()` establishes that:

- commit `aaaa...` exists;
- blob `bbbb...` exists at that path;
- the path identifies an actual cleanup result;
- `tests/test_cleanup_o2.py` exists or ran;
- a review attempt exists;
- that review was GREEN;
- that review was independent;
- that review was for this exact cleanup subject.

`independent_review_green` is trusted as a caller-provided Boolean. `speculative_redesign` and `new_product_scope` are also caller-supplied flags defaulting to `False`, rather than properties established from durable accepted scope.

The repository's own positive `_reviewed_cleanup_work()` test fixture demonstrates this gap: it uses fabricated `a*40` / `b*40` identities, an arbitrary test pathname and `independent_review_green=True`, and that object is deliberately accepted.

**Why load-bearing:** A `cleanup_candidate` is otherwise blocking Final. This bypass lets Final turn it into completed cleanup without the exact subject/evidence/independent-review proof explicitly required by the Card. It also weakens the new-scope/speculative-cleanup guard into a declaration made by the same input being validated.

**Originally classified as:** Recurrence/deeper bypass of the already-known R01 F4 semantic class. R01 caught the bare-Boolean cleanup. The repair requires more fields, but still does not bind those fields to durable truth.

## Original non-blocking observations

Several repaired areas looked materially stronger. New terminal PWv2.1 RED discovery requires complete severity coverage for its blocking finding IDs; observation evidence is bound to the originating attempt's review evidence path; same-epoch finding→observation identity downgrade is rejected; the five permitted dispositions are exact; present-but-dangling review locators fail; and conceivable future advisory improvement does not recursively reopen completed cleanup.

The fact that `close_continuation()` does not itself invoke observation reconciliation was not counted as an M02R-T03 defect. P6 leaves later lifecycle integration to M05, so missing full Final/router wiring was treated as a legitimate later integration boundary rather than folded into this Card. For the same reason, the currently per-Card nature of `verify_final_observation_reconciliation_from_board()` was not promoted into a separate finding; M05 must eventually compose the complete Final surface.

One related lifecycle edge was recorded only as non-blocking: a GREEN discovery can introduce an `open` observation, while the implemented durable reconciliation mechanism is `observation_updates` inside another terminal review attempt. The semantics exist, but the later lifecycle must provide a legitimate route for performing that reconciliation without mutating an immutable review or manufacturing an unnecessary review pass.

## Original coverage

The completed shadow review checked the complete M02R-T03 acceptance surface against exact implementation subject `elmakus/project_workflow_v2@180cc0af3a9b56c8c2808827bf5548b8ae040608`, including:

- load-bearing/advisory classification;
- RED evidence gating;
- advisory-only GREEN;
- observation origin/provenance;
- durable history and silent-loss vectors;
- convenience downgrade;
- tracker non-authority;
- all five dispositions;
- pre-Final completeness;
- cleanup exactness/evidence/review;
- speculative/new-scope cleanup;
- recursion termination;
- stale/dangling/malformed state;
- sibling negative-space cases;
- BOOT-B/C/D and M05 scope boundaries.

The baseline-to-subject delta was also checked as a one-commit change touching the expected review/state/Close implementation, tests and documentation; no BOOT-B/C/D authority implementation leakage was found.

## Post-freeze comparison

This section was formed only after the independent verdict and material finding set above were frozen.

The independent result disagreed with the formal R02 GREEN.

R01 had four findings. The repaired subject convincingly closed its F1 severity omission and F2 provenance mismatch. The two frozen shadow findings were deeper variants of the other two:

- Shadow F1 extends R01 F3. R02 tested omitted observations while the relevant review locator was still present, dangling locators, and a currently empty board. It did not test removing a previously durable review locator from a later Task Board revision or malformed duplicate-Card shadowing. Its “truncation-proof” claim therefore appeared stronger than the implementation.
- Shadow F2 extends R01 F4. R02 tested missing fields, malformed hashes, `independent_review_green=False`, and explicit speculative/new-scope flags. It did not bind an apparently valid 40-hex subject, test evidence or the GREEN-review Boolean to actual durable Git/review state. The positive repository test itself used fabricated-but-well-shaped data.

The comparison did not alter the original verdict or finding list.
