# ChatGPT-only Independent Plan Review

Independent plan review is performed by a fresh normal ChatGPT chat that did not author the exact reviewed Master Plan subject.

## Review requirement

Use:
- **REQUIRED** when project/user authority explicitly requires independent plan review;
- **RECOMMENDED** for a new or materially revised Master Plan when independent review is practical;
- **none** for trivial/editorial plan changes that do not alter execution strategy, milestone structure, requirement coverage or accepted gates, or when independent review is concretely impractical and no project/user authority requires it. A nontrivial `none` requires a concrete recorded reason; convenience alone is not enough.

This preserves the workflow rule that independent plan review should be performed when practical without turning every mechanical planning edit into a hard gate.

## Durable review state

Plan review state lives outside the reviewed Master Plan so review lifecycle mutations do not change the review subject.

Canonical location:

`planning/reviews/<plan-revision>.md`

Record at minimum:

```text
Plan revision: <R#>
Review requirement: REQUIRED | RECOMMENDED
Review state: pending | in_progress | green | red
Review subject: <exact immutable plan draft commit/blob/ref>
Review evidence: <concise evidence or pointer>
```

The reviewed subject is one exact immutable plan draft.

One review record corresponds to one exact plan revision/subject. Any substantive corrective plan edit must create a new plan revision (and therefore a distinct `planning/reviews/<plan-revision>.md` record) before a new review attempt. Do not overwrite a completed RED/GREEN record with another subject.

For a branch-isolated ChatGPT-only workstream, the selected manifest `routing.plan_review` MUST point to the exact active review record. The review record remains sole owner of requirement/state/subject/evidence; the manifest never mirrors those fields. A missing, mismatched or wrong-subject locator is inconsistent state and routes to Recovery.

## Planner handoff into review

After the planner's own pre-implementation audit is GREEN, when independent review is REQUIRED/RECOMMENDED:

1. keep the Master Plan `Status: draft`;
2. freeze/persist the exact plan draft;
3. create the revision-specific review record as `pending`; do not reuse a completed review record for a different subject;
4. set selected manifest `routing.plan_review` to that exact record and persist record + locator before yielding;
5. commit/push the durable handoff when possible;
6. stop before issuing an independent verdict;
7. use the dedicated independent-plan-review fresh-chat variant from `workflow/common/USER_STOP.md`, with durable start pointer `planning/reviews/<plan-revision>.md`;
8. keep the prompt locator-only; any material nonstandard review scope belongs in the durable plan-review record or another exact durable scope artifact, not in an expanded handoff prompt.

The authoring chat must not independently review its own exact plan subject.

## Reviewer read set

Read:
- root `PROJECT.md` as integrated project authority/navigation only;
- `workflow/chatgpt_only/PLAN_REVIEW.md`;
- selected workstream manifest and validated `routing.plan_review` locator;
- exact review record;
- exact immutable Master Plan subject;
- approved canonical requirements;
- accepted decisions;
- relevant Definition authority;
- only research/baseline/source evidence materially referenced by the plan;
- Task Board/current handoff only when reviewing a replan whose correctness materially depends on active execution state.

Do not use the planning-session narrative as review evidence.

## Review lifecycle

1. recover exact review subject and review requirement;
2. set the separate review record to `in_progress`;
3. independently inspect plan consistency and completeness;
4. audit false assumptions/P0-P1 risks, milestone structure/order, dependencies, outcome-level acceptance, requirement coverage, migration/rollback, verification, data-integrity/security, authorization gates, OpenSpec boundaries and premature detail;
5. persist concise GREEN/RED evidence;
6. set review record to `green | red`.

Do not mutate the reviewed Master Plan while judging it.

## GREEN

After GREEN:
1. persist review evidence/state;
2. review role ends;
3. return to `workflow/chatgpt_only/ROUTER.md`;
4. route to Planning;
5. Planning may mark that reviewed plan revision `approved` when no other planning blocker remains, but only deterministic lifecycle metadata may change after GREEN; any substantive plan-body change requires a new plan revision and a new independent review subject;
6. do not clear manifest `routing.plan_review` in the reviewer role; Planning clears it only after durably consuming the exact GREEN verdict into plan approval;
7. continue to Execution Prep automatically when implementation is already authorized.

GREEN itself is not a user stop.

## RED

After RED:
- persist failing review evidence/state first;
- review role ends;
- return to the router.

Then:
- bounded plan-only defects inside accepted Project Definition → route to Planning for correction;
- defect reveals missing/incorrect accepted product/system authority → route to Project Definition;
- more evidence needed before either can be resolved → create one exact record under `workflow/chatgpt_only/RESEARCH.md#Durable record contract`, with `Status: active`, `Origin role: plan_review`, this exact review record/subject as Origin subject, `Return target: strategic_planning:<exact correction subject>`, and `Return reconciliation: pending`; for a pre-execution plan review set selected manifest `routing.research_obligation`, but for an active-work replan review set Task Board `research_obligation`; never mirror either pointer into root `PROJECT.md`; persist record + pointer before routing to Research;
- unresolved user/product authority → real user stop.

If the same chat corrects the plan, it becomes the authoring chat for the corrected subject. When independent review remains REQUIRED/RECOMMENDED, freeze the new subject as `pending` and stop for a fresh independent re-review.

## User-facing behavior

Use root `CHATGPT.md` + `workflow/common/USER_STOP.md`.

The plan-review module owns review semantics, not a separate response style.
