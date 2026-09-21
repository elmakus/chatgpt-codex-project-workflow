# Brainstorm — Research agent behavior

Date: `2026-09-21`
Scope ID: `research-agent-behavior`
Revision: `R1`
Status: `tentative`

## Problem / goal

Understand the current Project Workflow Research semantics and the concrete behavior of the active agent when routing enters Research, then decide whether that contract should be changed.

## Current understanding

### Verified facts

- Shared Research goal: produce source-grounded findings that can support Project Definition and later planning without conflating evidence with accepted intent.
- A Research artifact distinguishes verified facts/sources, repository observations, assumptions, uncertainties, alternatives, recommendation when requested, and unresolved authority questions.
- Research is evidence only. It does not directly create accepted requirements, decisions or plan authority.
- Under the current repository policy `chatgpt_only`, ChatGPT itself executes the Research role. There is no separate runtime Investigator realization in the ChatGPT-only Research contract.
- A durable Research obligation records exact origin, exact question, exact Return target, status and reconciliation state so a fresh session can resume without chat history.
- Pre-execution Research is located through the selected workstream manifest `routing.research_obligation`; implementation/recovery Research is located through the selected Task Board `research_obligation`.
- On completion, Research returns to its exact recorded Return target. It cannot choose a new destination from chat history.
- In `codex_only`, an active Research obligation may be realized by a runtime Investigator, but concrete Investigator harness/model/session mechanics belong to `codex_workflow`, not Project Workflow.

### Existing accepted decisions

- Current project execution policy is `chatgpt_only`.
- Brainstorming routes to Research when material claims require verification.
- Research completion does not authorize Brainstorming → Project Definition promotion.

### Assumptions to verify

- Whether the desired feature is to change only Research interaction quality, or to introduce a stronger explicit research-agent contract across both fixed policies.
- Whether Research should prescribe a concrete search procedure/tool strategy or remain outcome/authority oriented.

## Ideas / alternatives considered

### Option A — Keep current contract

Keep Research primarily as an evidence/authority boundary with exact durable continuation, leaving concrete investigation tactics to the active agent/runtime.

### Option B — Strengthen Research behavior contract

Add explicit expectations for how the research role investigates: source hierarchy, repository inspection, web/external verification, competing hypotheses, contradiction handling, stopping criteria and concise return package.

### Option C — Separate Investigator semantics across policies

Keep ChatGPT-only as self-executed Research, while making Codex-only Investigator behavior more explicitly specified through the runtime-owned orchestration contract without moving model/harness ownership into Project Workflow.

## Trade-offs / questions

- More explicit research procedure improves repeatability but risks over-constraining simple research.
- Runtime-specific Investigator rules must not duplicate `codex_workflow` ownership.
- A stronger contract should still preserve the distinction between evidence and accepted authority.

## Research needed

None required to answer the current-state question. Additional research is needed only after the desired behavior change is selected.

## Open questions

- What exactly should improve compared with today's Research behavior?
- Should the change apply to `chatgpt_only`, `codex_only`, or both?
- Should Research define concrete investigation tactics, or only minimum evidence/quality obligations?

## Outcome of this session

- Tentative conclusions: current Research is a durable evidence-producing role, not a decision-making phase; under current `chatgpt_only` policy ChatGPT performs it directly, while `codex_only` may realize an Investigator through runtime orchestration.
- Explicit user/product choices to promote through Project Definition: none yet.
- Research still needed: none for current-state explanation.
- Open questions: desired target behavior remains unspecified.
- Next phase/action: `continue brainstorming`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
