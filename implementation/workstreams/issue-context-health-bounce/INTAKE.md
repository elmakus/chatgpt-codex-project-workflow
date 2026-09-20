# Intake — issue-context-health-bounce

- Workstream ID: `issue-context-health-bounce`
- Kind: `issue`
- Branch: `fix/chatgpt-only-context-health-bounce`
- Integration target: `main`
- Base: `main@808084a4c7989715f7ee4889a31bce28f778d597`
- Status: `active`

## Operator intent

Prevent ChatGPT-only Context Health from bouncing into another fresh-chat handoff after only a short recovered continuation merely because the next role, milestone, phase, or authority area differs.

The workflow should continue in the same chat unless the current conversation has accumulated affirmative, concrete context degradation that creates material risk of stale-state carryover, authority confusion, omission, or dominant irrelevant history.

A role/milestone/phase/authority-area transition by itself must not be a context-health trigger or sufficient reason for `FRESH`.

A chat that itself started from a context-hygiene fresh handoff must not immediately request another fresh chat at the next durable transition unless new concrete degradation accumulated after recovery.

## Baseline diagnosis

Current `workflow/chatgpt_only/ROUTER.md` lists a "major role/authority-area transition" among examples of a concrete context-health trigger.

Current `workflow/chatgpt_only/CONTEXT_HEALTH.md` treats a substantially different authority/source area as a soft signal, which can be over-applied at ordinary deterministic transitions.

Current `docs/audits/CHATGPT_ONLY_CONTEXT_HEALTH_GATE.md` scenario 6 explicitly allows a milestone transition with a major authority-area shift to trigger `FRESH`, reinforcing the aggressive interpretation.

This permits a healthy newly recovered chat to stop again after a small amount of work even though durable repository truth is clear and the transcript has not materially degraded.

## Base/dependency classification

Independent workstream. The issue exists on current `main`; no unmerged parent-only behavior is required to reproduce or fix it.

## Micro-fix qualification

- Root cause and intended behavior are concrete: yes — trigger wording and audit scenario are identifiable.
- Change is bounded and low strategic risk: yes — ChatGPT-only context-health routing/contract wording plus regression audit only.
- Accepted requirement/architecture/product decision must change: no — this tightens the existing stated intent that `FRESH` requires concrete material context risk.
- Acceptance can be stated directly: yes.
- Substantial migration/deployment strategy needed: no.

Path: `micro_fix`

Next route: `execution_prep:micro_fix`

## Acceptance target

1. Ordinary role/milestone/phase/authority-area transitions are not standalone context-health trigger signals.
2. Context Health is loaded only for affirmative evidence of context degradation, not because workflow structure changed.
3. A fresh-handoff recovery cannot immediately bounce to another `FRESH` solely because the recovered obligation completed or the next authority area differs.
4. `CONTINUE` remains the default when durable next authority is deterministically identifiable and no affirmative harmful-context evidence exists.
5. Existing genuine hard-risk signals and safe-boundary behavior remain intact.
6. Regression checks cover the reported short-session bounce case and nearby scenarios.

## Evidence / tests to perform

- Static semantic inspection of `ROUTER.md` and `CONTEXT_HEALTH.md`.
- Update the Context Health audit scenario matrix to include explicit anti-bounce cases.
- Run repository-wide consistency checks for conflicting ChatGPT-only context-health wording.
