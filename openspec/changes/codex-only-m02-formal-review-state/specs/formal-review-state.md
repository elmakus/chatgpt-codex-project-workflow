# Formal review state and recovery specification

## Review state owner

For Card/milestone review, the selected canonical codex_only Task Board owns mutable review state. Stable Card/milestone contracts remain the authority for whether review is REQUIRED, RECOMMENDED or none; the Task Board records the resolved requirement for deterministic recovery.

A branch-isolated workstream final-integration review remains manifest-owned and is not mirrored into Card/milestone Task Board state.

## Project implementation ownership

A reviewable implementation records a semantic project `implementation_owner_role`. For ordinary production implementation this is `executor`. This is a Project Workflow role slot, not a runtime worker/session identifier.

Codex Main is the only writer of shared Task Board/integration state. The runtime may realize or replace the Executor behind the role slot without changing project semantics.

## Review block

A Card/milestone review block has:

```yaml
review:
  requirement: REQUIRED | RECOMMENDED | none
  current_attempt: null | R01
  attempts:
    - id: R01
      state: pending | in_progress | green | red
      subject: <exact-immutable-subject>
      reviewer_role: tester
      evidence: <repo-relative-path-or-null>
```

Rules:

1. Attempt IDs are stable within the owning review block and never reused.
2. One attempt covers exactly one immutable subject.
3. `current_attempt` is null before a gate is activated; otherwise it points to exactly one existing attempt.
4. At most one attempt may be non-terminal (`pending | in_progress`) at a time.
5. Prior attempts remain durable. New attempts append; they never rewrite RED/GREEN history.
6. A verdict requires durable evidence. A `green` or `red` attempt with missing evidence is invalid.
7. `reviewer_role: tester` is semantic project provenance only. Concrete worker/session/profile/model identity is forbidden Project Workflow state.
8. Codex Main may set `in_progress` only after the runtime has supplied a reviewer independent from the exact subject's implementation owner.
9. The Tester returns verdict/evidence to Main and does not repair production or write shared Project Workflow state.

## RED and corrected subjects

For subject S1:

1. Main freezes S1 and appends R01 `pending`.
2. An independent Tester performs a full review of S1; Main records R01 `in_progress`.
3. If RED, Main persists R01 `red` + evidence.
4. Main routes the correction to the Card's owning `executor` role. The Tester does not repair it.
5. The owning Executor produces corrected subject S2.
6. Main appends R02 `pending` for S2 and points `current_attempt` to R02. R01 remains immutable RED history.
7. An independent Tester performs the full applicable authority/acceptance review of S2. It may be the same logical Tester if independence remains valid and runtime resume is safe.
8. GREEN is persisted on R02 with evidence; only then may the normal post-review completion path finalize the Card/milestone.

A changed implementation subject always creates a new attempt. Runtime reviewer replacement against the same unchanged subject does not.

## Runtime loss/replacement

Project Workflow never stores `session_id`, `invocation_id`, Muse lease, model/profile/reasoning selection, worker-resume state or equivalent runtime identity.

If runtime state is lost while an attempt is `pending` or `in_progress`:

- keep the same attempt and exact subject;
- Codex Main asks `codex_workflow` to safely resume or fail-closed replace the logical reviewer;
- the reviewer performs/reperforms the full review required for that subject;
- no new Project Workflow attempt is created solely because runtime realization changed.

If an implementation Executor cannot be safely resumed, runtime replacement may realize the same project `executor` role. The project role and exact implementation obligation remain unchanged.

## Recovery / partial transitions

Recovery is repository-first and fail-closed:

- a missing/nonexistent `current_attempt`, more than one non-terminal attempt, mutable subject within an existing attempt, or terminal verdict without evidence is inconsistent state;
- a durable RED verdict outranks unrelated implementation and routes correction to the owning Executor role;
- if corrected implementation S2 is already durably proven but its next attempt was not frozen before interruption, Execution recovery appends exactly one new pending attempt for S2 instead of redoing the correction;
- if complete verdict evidence for the exact current attempt is durable but Task Board still says `in_progress`, Main may reconcile the matching verdict only after verifying the evidence identifies the same attempt/subject; otherwise perform a full review again on the same attempt/subject;
- a durable GREEN verdict is not replayed merely because runtime worker state is gone;
- recovery never infers project truth from a runtime session handle.

## Plan review

Plan review keeps one immutable plan revision/subject per durable plan-review record. Independence is semantic: the reviewer role must be distinct from the authoring/planning owner for that exact subject, and runtime realization belongs to `codex_workflow`.

A substantive correction creates a new plan revision/review record. Prior RED/GREEN plan-review records remain durable. A qualifying Codex-managed independent verdict satisfies the Project Workflow gate without a second normal-ChatGPT review.

## Serial M02 boundary

M02 does not define bounded-parallel eligibility. `parallel_safe`, `write_scope`, `exclusive_resources`, compatible-ready-set, lane/worktree and recoverable integration-base schema are M03-owned and absent from this change.
