# M02-T01 Independent Review — Attempt 1

Card: `M02-T01`
Verdict: `RED`
Reviewed subject: `af08ef755cb846118c9dbe1a6edf7f5f139cf0e8`
Implementation base: `10ae410efa05faa24b61417d59c399a2d5a3cb58`
Workflow-main baseline verified: `6b0445256b417f82431fb7b2704f56691eb4e7ae`

## Authority checked

- `implementation/workstreams/feature-codex-only-policy/cards/M02-T01.md`
- `planning/CODEX_ONLY_MASTER_PLAN.md#M02--projectruntime-boundary-formal-independent-review-state-and-recovery`
- `requirements/CODEX_ONLY_POLICY.md` — `CO-REQ-007..016`, `CO-REQ-024..025`
- `decisions/ADR_CODEX_ONLY_RUNTIME_BOUNDARY.md`
- accepted namespace and bounded-parallel ADR constraints applicable to M02
- M01 GREEN checkpoint/handoff `8ded26f50275ab04e35a07438ca1abd2836901c2`
- `openspec/changes/codex-only-m02-formal-review-state/`
- author evidence `implementation/workstreams/feature-codex-only-policy/evidence/M02-T01.md`
- exact reviewed tree/range `10ae410e..af08ef75`

## Independent checks

GREEN:

- exact reviewed range contains the intended M02 OpenSpec/audit plus policy-local State/Review/Execution/Recovery/Router/Plan Review/Context Health/template changes;
- `git diff --check 10ae410e..af08ef75` is GREEN;
- conflict-marker scan is GREEN;
- no forbidden runtime identity key appears as a required M02 schema key;
- no M03-owned `parallel_safe`, `write_scope`, `exclusive_resources`, lane/worktree or integration-base key appears as M02 schema;
- modified M02 contracts contain no active dependency on another policy namespace or legacy/shared execution contracts;
- root `workflow/CONTEXT_ROUTING.md` and the complete `workflow/chatgpt_only/` tree match current workflow `main` at `6b0445256b417f82431fb7b2704f56691eb4e7ae`;
- root `PROJECT.md` remains `execution_policy: chatgpt_only`;
- PyYAML and Ruby YAML parsers are unavailable in the independent-review runtime, so parser-based YAML validation is not claimed.

## RED finding

### R1 — milestone review provenance/recovery is incomplete

M02 repeatedly defines one review-attempt model for **Card/milestone** review:

- `STATE.md` says the Task Board owns a Card/milestone review block;
- `REVIEW.md` selects Card/milestone review and, during freeze, requires Main to record/resolve `implementation_owner_role`;
- `RECOVERY.md` validates active Card/milestone review blocks and routes durable RED through the owning-Executor repair path;
- OpenSpec says a Card/milestone review block is the durable review owner and RED routes to the owning Executor.

But the durable provenance representation is Card-only:

- both Task Board templates place `implementation_owner_role` only on Card entries;
- the default milestone example has a review block but no implementation-owner provenance;
- the branch-isolated template has no concrete milestone review/provenance shape at all;
- `REVIEW.md` / `EXECUTION.md` resolve bounded RED repair specifically through “the Card's `implementation_owner_role: executor`”.

Therefore a recovered milestone-level `pending | in_progress | red` review cannot satisfy the same repository-first independence/RED-repair contract without inferring production ownership from non-authoritative runtime/transcript context or silently converting the milestone obligation into a Card obligation. That contradicts the M02 deterministic-recovery boundary in CO-REQ-024/025 and the Card acceptance that semantic project provenance be sufficient for RED continuation.

## Required bounded correction

Within existing M02 authority, make milestone review semantics explicit and self-consistent. The correction must do one of the following without introducing runtime identity or M03 concurrency state:

1. add durable milestone-level semantic production-owner/recovery provenance and make Review/Execution/Recovery use it consistently; or
2. explicitly define milestone RED as a Main-owned transition to Execution Prep that materializes/reopens the exact bounded corrective Card(s), with Card-level `implementation_owner_role: executor`, and remove any rule that requires a nonexistent milestone owner slot.

In either case, both default and branch-isolated Task Board templates must express the resulting M02 Card/milestone review shape sufficiently for deterministic recovery, OpenSpec/audit must match, and the full M02 verification set must be rerun.

## Verdict

RED. The exact subject does not yet satisfy the M02 formal-review/recovery contract for milestone-owned review state. The defect is bounded inside accepted M02 authority and may route through the normal RED corrective path to implementation.
