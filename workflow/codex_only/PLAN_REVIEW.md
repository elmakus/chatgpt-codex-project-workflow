# Codex-only Independent Plan Review

> M02 contract. Formal plan-review independence is role/subject based, not normal-ChatGPT-session based.

## Durable record

Plan review state remains outside the reviewed Master Plan so review lifecycle writes do not mutate the review subject.

Use one record per exact plan revision/subject under:

`planning/reviews/<plan-revision>.md`

Record at minimum:

```text
Plan revision: <R#>
Review requirement: REQUIRED | RECOMMENDED
Review state: pending | in_progress | green | red
Review subject: <exact immutable plan draft>
Author owner role: planner
Reviewer role: tester
Review evidence: <evidence-or-null>
```

Role labels are Project Workflow provenance. Do not store runtime worker/session/model/profile/invocation identifiers.

## Independence

Before `in_progress`, runtime must realize a Tester independent from the worker that authored the exact plan subject.

The Tester:

- reads the exact immutable plan subject;
- checks approved Definition/decisions and relevant evidence;
- does not mutate the reviewed plan while judging it;
- returns GREEN/RED + evidence to Codex Main.

Codex Main persists the review record. A qualifying Codex-managed verdict satisfies the Project Workflow gate without another mandatory normal-ChatGPT review.

## GREEN

After GREEN:

- preserve the exact review record/evidence;
- return through the policy router to Planning for deterministic approval metadata;
- Planning may mark that exact reviewed plan revision approved when no blocker remains;
- implementation may continue automatically when already authorized.

Any substantive plan-body change after GREEN creates a new plan revision/subject and separate review record.

## RED

After RED:

- preserve the RED record/evidence;
- return to the router;
- bounded plan-only defects -> Planning;
- accepted product/system authority defect -> Definition;
- missing evidence -> Research with exact Origin/Return target;
- unresolved user/product/authorization/runtime-input gate -> normal real stop.

If Planning corrects the plan, create a new plan revision/review record. Do not overwrite the prior RED record.

## Runtime loss/replacement

Loss of a reviewer runtime does not change the plan review subject/record. Codex Main may let `codex_workflow` safely resume or replace the Tester and repeat the full review of the same immutable plan subject.

A durable GREEN/RED verdict is not replayed merely because runtime worker state disappeared.
