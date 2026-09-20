# M03-T01 independent review

Date: 2026-09-20
Card: `M03-T01 — Migrate Codex-only pre-execution routing to workstream-local state`
Review subject: `2abc8ddd2d083fe66e4ba95369cbe2636e610ff5`
Verdict: **RED**

## Authority reviewed

- `planning/BRANCH_FIRST_MANAGED_CHANGES_MASTER_PLAN.md` — M03
- `requirements/BRANCH_FIRST_MANAGED_CHANGES.md` — REQ-BF-002..009, REQ-BF-011, REQ-BF-016..017 and Codex-only REQ-BF-015
- ADR-BF-001, ADR-BF-002, ADR-BF-003
- `openspec/changes/branch-first-m03-codex-lifecycle/`
- M01 GREEN and M02 GREEN checkpoints
- Card contract `implementation/workstreams/feature-branch-first-managed-changes/cards/M03-T01.md`
- Implementation evidence `implementation/workstreams/feature-branch-first-managed-changes/evidence/M03-T01.md`
- Exact reviewed source at the immutable subject

## Independent inspection

The reviewed subject correctly introduces manifest-local `routing.exploratory_scope`, `routing.research_obligation`, and `routing.plan_review`, preserves user-owned promotion, Codex Main/Tester ownership, bounded-batch semantics, and policy separation. Independent runner verification passed the focused suite **9/9** and the repository unittest suite **19/19**.

One blocking in-scope semantic finding remains.

### F1 — Definition still permits pre-execution PROJECT-owned Research

`workflow/codex_only/DEFINITION.md` step 2 still says a completed Research obligation may be owned by “pre-execution PROJECT state or active implementation/recovery state”. For M03-T01, pre-execution Research MUST be located only by the selected workstream manifest `routing.research_obligation`; root `PROJECT.md` must not own or mirror that active pointer.

Impact: the in-scope Definition contract still documents the superseded root-pointer path, contradicting M03-T01 acceptance 2/5/6, REQ-BF-008..009, ADR-BF-002 and the M03 OpenSpec. The committed tests miss this because they only reject the exact legacy field spelling, not this semantic paraphrase.

`workflow/codex_only/RECOVERY.md` and `REPOSITORY.md` also contain historical PROJECT-pointer wording, but those files are explicitly owned by M03-T02 and are not counted as separate M03-T01 defects here.

Required bounded correction: rewrite the Definition step so the two legal ownership contexts are selected-workstream-manifest pre-execution routing and selected-Task-Board implementation/recovery routing, then strengthen the focused regression check so a semantic reintroduction of pre-execution PROJECT ownership is caught.

## Verdict

**RED.** The defect is a bounded L1/L2 correction inside accepted M03-T01 authority. No user/product decision is required.
