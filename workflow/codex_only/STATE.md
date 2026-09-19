# Codex-only State Contract

> M02 contract. This namespace remains non-routable from root policy routing until M04.

## Project-state ownership

The canonical Task Board selected by the current project/workstream context is the sole mutable Card/milestone execution-state record. A branch-isolated board is trusted only after manifest identity/branch binding succeeds.

Codex Main is the sole writer of shared Project Workflow Task Board and integration state. Executor/Tester workers return bounded results/evidence to Main; they do not become independent project-state writers.

Runtime worker identity and lifecycle are not Project Workflow state.

## Card and milestone lifecycle

Serial execution remains the valid/default M02 execution shape. M03 owns bounded-parallel readiness/lane semantics.

Use normal lifecycle states:

```text
planned -> ready -> in_progress -> done
                     \-> blocked
```

`superseded` requires accepted authority. Reviewable Cards remain non-terminal until the current required/recommended review attempt is GREEN.

## Semantic implementation provenance

A reviewable implementation records:

```yaml
implementation_owner_role: executor
```

This is a Project Workflow role slot, not a runtime worker identity. It answers which project role owns production repair after RED.

A runtime may resume or fail-closed replace the concrete worker realizing that role without changing `implementation_owner_role`.

Do not persist worker/session/model/profile/invocation/lease identifiers or resume protocol in Project Workflow state.

## Review block

For Card/milestone review, Task Board owns:

```yaml
review:
  requirement: REQUIRED # REQUIRED | RECOMMENDED | none
  current_attempt: R01  # null before activation
  attempts:
    - id: R01
      state: pending    # pending | in_progress | green | red
      subject: "<exact-immutable-subject>"
      reviewer_role: tester
      evidence: null
```

The stable Card/milestone contract remains authority for the review requirement. The Task Board records the resolved requirement for recovery. A mismatch between the stable contract and Task Board is inconsistent state and must be reconciled before execution continues.

### Attempt invariants

- attempt IDs are stable within their owning review block and never reused;
- one attempt covers exactly one immutable subject;
- `current_attempt` is null before activation, otherwise it points to exactly one existing attempt;
- at most one attempt may be non-terminal (`pending | in_progress`);
- prior attempts are append-only project history;
- `green | red` requires durable evidence;
- `reviewer_role: tester` is semantic project provenance only;
- setting `in_progress` requires runtime proof that the reviewer is independent from the exact subject's implementation owner;
- changing implementation after RED appends a new attempt for the new exact subject; it never edits the old attempt;
- replacing/resuming a runtime reviewer for the same unchanged subject does not create a new attempt.

The manifest-owned workstream final-integration review remains a distinct lifecycle. M04 reconciles its full Close/target-refresh representation; it must never be mirrored into a Card/milestone review block.

## Canonical RED -> repair -> recheck sequence

```text
S1 durable
  -> R01 pending
  -> R01 in_progress
  -> R01 red + evidence
  -> owning executor repairs
  -> S2 durable
  -> R02 pending (R01 remains red)
  -> R02 in_progress
  -> R02 green + evidence
  -> post-review finalization
```

Every new reviewable implementation subject gets a distinct attempt. A later review is a full applicable authority/acceptance review, not merely a check of the previously failing line/item.

The same logical Tester may perform R02 when independence remains intact and runtime resume is safe. Runtime may fail closed to a replacement Tester without Project Workflow state changing beyond ordinary attempt progress/verdict.

## Review completion

GREEN is a precondition for terminal Card completion when review is REQUIRED/RECOMMENDED. The verdict itself does not mutate the production subject.

After GREEN, Codex Main verifies the finalized result is still exactly the reviewed subject, then performs normal terminal state reconciliation.

## Recovery integrity

Treat these as inconsistent and fail closed before unrelated work:

- `current_attempt` references no attempt;
- more than one `pending | in_progress` attempt exists;
- an existing attempt's subject changed;
- a terminal review attempt lacks evidence;
- Task Board claims GREEN for a subject different from the result being finalized;
- runtime-only identity appears as required project-state authority;
- a worker directly becomes a competing Task Board writer.

If a corrected implementation is durably present but interruption occurred before the next pending attempt was appended, recovery may append exactly one new attempt for that proven subject. It must not redo the correction merely to recreate bookkeeping.

## Implementation-owned Research

Implementation/recovery Research continues to use one Task Board routing pointer:

```yaml
research_obligation: <exact-record-path> | null
```

The research record owns its lifecycle/Origin/Return target. Runtime worker identity is never part of the pointer.

## M03 boundary

M02 does not define `parallel_safe`, `write_scope`, `exclusive_resources`, compatible-ready-set, lane/worktree or recoverable integration-base schema. M03 adds only the project-level concurrency metadata required by accepted authority while preserving this review-attempt model and runtime-identity prohibition.
