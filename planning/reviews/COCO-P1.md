# Plan Review — COCO-P1

Plan revision: COCO-P1
Review requirement: RECOMMENDED
Review state: red
Review subject: 014ddad3969c36c81edd18e13068ba1ddca5362b
Author owner role: planner
Reviewer role: tester
Review evidence: RED — the frozen COCO-P1 subject is otherwise aligned with R1/ADR authority: it preserves ChatGPT-only Context Health, the user-owned Brainstorming → Definition promotion gate, independent Tester review, durable Recovery, deterministic multi-milestone continuation, and the `codex_workflow` runtime boundary. One bounded plan-only defect remains: current `main` `workflow/codex_only/PLANNING.md` still authorizes Master Plans to include `coordinating-context refresh boundaries only when materially useful`, but COCO-P1 neither removes/rewords that active codex-only planning contract nor extends regression coverage to prevent coordinator-hygiene boundaries from being reintroduced there. This conflicts with COCO-R1/COCO-R7's intent that context/session hygiene cannot create a Project Workflow stop. Planning must create a new revision that explicitly removes/reconciles this planning-level refresh-boundary allowance and adds regression coverage across the active codex-only lifecycle for coordinator-hygiene/FRESH stop semantics. No Definition or ADR reopening is required.

## Reviewed artifact

`planning/CODEX_ONLY_CONTINUOUS_ORCHESTRATION_MASTER_PLAN.md`

## Authority

- `requirements/CODEX_ONLY_CONTINUOUS_ORCHESTRATION.md` R1
- `decisions/ADR_CODEX_ONLY_CONTINUOUS_MAIN_ORCHESTRATION.md`
- completed Intake at `implementation/workstreams/change-codex-only-continuous-orchestration/INTAKE.md`

## Review focus

Independently verify that the plan:

1. removes only the normal `codex_only` Context Health/FRESH project-workflow gate;
2. preserves ChatGPT-only Context Health unchanged;
3. preserves user-owned Brainstorming → Definition promotion;
4. preserves independent Tester review and durable state/recovery;
5. gives Codex Main deterministic multi-milestone continuation until a genuine human/project stop or end of scope;
6. does not duplicate or invade `codex_workflow` runtime orchestration;
7. has sufficient regression coverage to prevent reintroduction of coordinator hygiene as a stop.

A GREEN verdict should return through the router to Planning for deterministic approval and then Execution Prep. A RED verdict should identify the exact plan defect against the authority above.
