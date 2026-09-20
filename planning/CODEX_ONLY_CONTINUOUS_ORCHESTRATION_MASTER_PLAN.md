# Master Plan — Codex-only continuous orchestration

Plan revision: COCO-P1
Status: draft
Review requirement: RECOMMENDED

## Authority

- Requirements: `requirements/CODEX_ONLY_CONTINUOUS_ORCHESTRATION.md` R1
- Decision: `decisions/ADR_CODEX_ONLY_CONTINUOUS_MAIN_ORCHESTRATION.md`
- Workstream: `change-codex-only-continuous-orchestration`

## Goal

Make `codex_only` a continuous Main-orchestrated Project Workflow: once accepted Definition and plan authority exist, Main can execute an arbitrary approved milestone chain (for example M01→M15), including Tester reviews and bounded corrections, without context-hygiene user stops.

## Non-goals

- Change `chatgpt_only` Context Health.
- Change `codex_workflow` worker/session mechanics.
- Remove durable Recovery.
- Weaken independent review, strategic authority, or explicit deployment/live-write gates.

## M01 — Continuous Codex Main lifecycle

### Outcome

The active `codex_only` policy contains no Context Health/FRESH transition. Router, orchestration, Close and Recovery consistently define continuous deterministic continuation until a genuine human/project stop or end of approved scope.

### Requirement coverage

Owns COCO-R1 through COCO-R7.

### Planned work

1. Remove Context Health from `workflow/codex_only/ROUTER.md`:
   - remove `context-hygiene boundary` from normal stop conditions;
   - remove the between-role Context Health trigger step/module dispatch;
   - make the role-transition protocol directly persist → route → continue;
   - explicitly state that coordinator/session hygiene is not a Project Workflow stop.
2. Remove `workflow/codex_only/CONTEXT_HEALTH.md` so dormant policy text cannot compete with the active contract.
3. Reconcile `workflow/codex/CODEX_ORCHESTRATION.md`, `workflow/codex_only/CLOSE.md`, and `workflow/codex_only/RECOVERY.md` only as needed to make one-shot multi-milestone continuation and runtime/durable recovery boundaries explicit.
4. Add a dedicated regression contract test for `codex_only` continuous orchestration and preserve the existing ChatGPT-only Context Health test unchanged.
5. Update user-facing repository documentation/changelog where needed so the policy distinction is discoverable.

### Acceptance

- No active `codex_only` workflow file routes to or depends on a Context Health/FRESH decision.
- `workflow/codex_only/CONTEXT_HEALTH.md` is absent.
- Router explicitly continues deterministic legal obligations without a user-facing stop, including across milestone boundaries and internal Tester review cycles.
- True stops remain: unresolved user/product authority, explicit authorization gate, concrete unremediable runtime/input blocker, or end of approved scope.
- Brainstorming → Definition user promotion remains intact.
- Durable Recovery remains authoritative for interrupted coordinator/runtime execution.
- Existing `chatgpt_only` Context Health contracts/tests remain unchanged and GREEN.
- Repository regression tests covering the touched workflow contracts are GREEN.

### Verification strategy

- Static contract assertions over `workflow/codex_only/ROUTER.md`, `CLOSE.md`, `RECOVERY.md`, and `workflow/codex/CODEX_ORCHESTRATION.md`.
- Negative assertion that the codex-only Context Health file/reference is absent.
- Positive assertion that `workflow/chatgpt_only/CONTEXT_HEALTH.md` and its contract test remain present.
- Run targeted tests, then full repository Python unittest/pytest suite available in the repository.

### JIT / implementation boundary

Execution Prep may realize M01 as one bounded Card because all behavior is known and localized. If implementation reveals a hidden dependency on `codex_workflow` runtime internals or requires changing user/product authority beyond R1, stop affected execution and route through the normal strategic boundary instead of expanding scope.

## Planning audit

- Definition completeness: GREEN.
- Requirement coverage: COCO-R1…R7 all owned by M01.
- Strategic ambiguity: none.
- Migration/data risk: none; workflow-contract change only.
- User/deployment authorization gate: none for repository edits/tests/PR; existing downstream deployment/live-write gates remain unchanged.
- Independent plan review: RECOMMENDED because this materially changes lifecycle stop semantics.
