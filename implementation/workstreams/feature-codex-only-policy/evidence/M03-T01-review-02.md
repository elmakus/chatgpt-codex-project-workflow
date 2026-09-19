# M03-T01 Independent Review 02

Card: `M03-T01`
Exact review subject: `20dd6e7827ab249b3884ab7e10cb49ba61d40c60`
Verdict: **RED**

## Authority reviewed

- `implementation/workstreams/feature-codex-only-policy/cards/M03-T01.md`
- `requirements/CODEX_ONLY_POLICY.md` — CO-REQ-017..025
- `planning/CODEX_ONLY_MASTER_PLAN.md#M03--bounded-parallel-task-cards-and-jit-safety`
- accepted namespace/runtime/parallel ADRs
- accepted M02 checkpoint/handoff and M02 review invariants
- `openspec/changes/codex-only-m03-bounded-parallel-safety/`
- prior M03 RED evidence `implementation/workstreams/feature-codex-only-policy/evidence/M03-T01-review-01.md`
- exact corrected subject `20dd6e7827ab249b3884ab7e10cb49ba61d40c60` and implementation range `43c234e59e6db081a0b3dbf7efd9ae16948e0553..20dd6e7827ab249b3884ab7e10cb49ba61d40c60`

## Independence

This fresh reviewer chat did not implement the exact reviewed subject. The subject remained immutable during review; only review lifecycle state/evidence was written after the subject.

## Independent checks

GREEN:

- Prior RED-01 is repaired coherently across Execution Prep, State, Recovery, Router, OpenSpec and scenario audit: a stale prepared batch cannot clear `current_batch` before batch-owned Card statuses are reconciled back to legal READY/serial state, and the unwind is forbidden after runtime-active/result state.
- Exact implementation range contains 21 changed files; no `workflow/chatgpt_only/*` or root `workflow/CONTEXT_ROUTING.md` change is present.
- Root `workflow/CONTEXT_ROUTING.md` at the subject matches current workflow `main`; current `main` is the workstream base for this branch, so the unchanged `workflow/chatgpt_only/*` tree also remains identical to current `main`.
- Root `PROJECT.md` at the subject still declares `execution_policy: chatgpt_only`.
- `git diff --check 43c234e..20dd6e7` is GREEN and changed files contain no conflict markers.
- Modified `workflow/codex_only/*` M03 contracts contain no active references to `workflow/chatgpt_only/*`, `workflow/legacy/*` or `workflow/contracts/*`, and no forbidden runtime-identity/scheduler schema key was found.

## Finding

### RED-02 — RED correction of an already-integrated batch member has no deterministic batch reconciliation

The M03 contracts intentionally freeze a reviewable Card subject immediately after that member is integrated, and Router gives Review/RED priority over continuing sibling batch integration. That creates this reachable state:

1. B01 contains independent members T1 and T2.
2. Both lane results return; Main integrates T1 first to shared commit S1, records T1 member `integrated_commit: S1`, freezes T1 review, and leaves T2 returned.
3. T1 review is RED. Router correctly prioritizes RED; the owning Executor produces corrected shared Card result S1c and Main freezes a new review subject. T2 remains preserved.
4. `STATE.md` requires an integrated member's `integrated_commit` to remain coherent with Card result state, while `RECOVERY.md` treats mismatch as inconsistent.
5. No M03 contract defines how B01 records S1 -> S1c correction lineage. Keeping `integrated_commit: S1` makes it disagree with the corrected Card result; overwriting it with S1c loses the exact original batch integration ref and no longer directly represents integration of the frozen lane `result_commit`.
6. The next-member integration guard permits only already-integrated earlier members plus authorized Main bookkeeping after the frozen base. The post-review production correction S1c is neither explicitly represented nor classified for that guard.

Therefore a normal M02 RED/repair path can leave an active M03 batch without one deterministic recoverable continuation. This conflicts with CO-REQ-024, M03 deterministic integration/recovery acceptance, and the requirement to preserve M02 review semantics while retaining lane/integration provenance.

## Required correction

Define one canonical active-batch review/correction rule and make State / Execution / Router / Recovery / OpenSpec / audit agree. The rule must:

1. prevent an in-batch RED correction from making `integrated_commit`, Card result and later sibling integration-base/head validation ambiguous;
2. preserve the exact original lane result and original integration provenance;
3. preserve returned/integrated sibling results without replay;
4. keep frozen member order and Main-only shared-state ownership;
5. remain recoverable from repository state alone.

A valid bounded design may defer formal review dispatch for integrated batch members until the current batch is fully integrated/completed (while preserving exact frozen review subjects), or may define explicit append-only corrected-member lineage with equivalent deterministic recovery. One canonical design is required before GREEN.

## Verdict

RED. Prior RED-01 is fixed, but the exact corrected subject still has the active-batch RED-repair reconciliation gap above.
