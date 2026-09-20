# Plan Review — COCO-P1

Plan revision: COCO-P1
Review requirement: RECOMMENDED
Review state: red
Review subject: 014ddad3969c36c81edd18e13068ba1ddca5362b
Review evidence: RED — the exact COCO-P1 subject is incomplete against COCO-R1 and COCO-R7. Current `main` `workflow/codex_only/PLANNING.md` still lists `coordinating-context refresh boundaries only when materially useful` as valid Master Plan content, so active codex-only planning authority can still schedule coordinator hygiene as a workflow boundary. COCO-P1 does not include `workflow/codex_only/PLANNING.md` in planned work and its verification strategy does not cover that contract. This is a bounded plan-only defect: correct the plan with a new revision that explicitly reconciles/removes that planning allowance and adds regression coverage preventing coordinator Context Health/FRESH/hygiene stop semantics from re-entering through Planning. Approved requirements/ADR remain sufficient; no Definition reopening is required.

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
