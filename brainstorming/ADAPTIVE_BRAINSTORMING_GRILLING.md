# Brainstorm — Adaptive grilling as the default Brainstorming method

Date: `2026-09-21`
Scope ID: `adaptive-brainstorming-grilling`
Revision: `R1`
Status: `tentative`

## Problem / goal

The existing grilling integration is too easy for an agent to satisfy shallowly: a few high-level questions can technically satisfy the contract even when meaningful downstream decisions remain. At the same time, reproducing an intentionally exhaustive 100–200-question interview for every topic would be excessive.

Target direction: every Project Workflow Brainstorming scope should naturally use adaptive grilling, with depth proportional to the decision value still available.

## Current understanding

### Verified facts

- Current policy-local Brainstorming contracts make grilling conditional on ambiguity, multiple solution paths, or decision dependencies.
- Current tests primarily verify that the textual contract contains the expected grilling semantics; they do not prove end-to-end conversational depth.
- The current contract allows normal completion when material branches are resolved or classified deferred/non-blocking.

### Existing accepted decisions

- Brainstorming remains exploratory rather than accepted Definition authority.
- Agent-findable facts remain agent-owned; user-facing questions focus on user/product/strategic choices.
- Questions are dependency-aware, frontier-based, numbered, and include an assistant recommendation.
- The user may stop grilling at any time with clear natural language.
- Project Definition promotion remains a separate user-owned gate.

### Explicit user/product choices from this exploration

- Adaptive grilling is the natural/default interaction method of **every Brainstorming scope in Project Workflow**, not behavior tied specifically to `#feature`, `#issue`, or a manual trigger.
- Entry path does not change the method: whenever Project Workflow is in Brainstorming, the same adaptive mechanism applies.
- The behavior must be meaningfully deeper than the current shallow 2–3-question experience.
- The behavior must not manufacture huge numbers of low-value questions merely to imitate exhaustive `grill-me`.
- The user does not need to remember a grilling directive; clear natural-language stop remains the user-controlled escape hatch.
- Grilling may finish only when another sensible round has low expected value for changing scope, UX, architecture, constraints, acceptance, or important edge cases. Merely knowing enough to implement is not sufficient.
- Apparent completion requires one final challenge/discovery pass asking what has not yet been surfaced that could matter later. If that pass discovers material decisions, grilling continues.
- There is no fixed numeric limit on questions or rounds. Depth is governed by decision value and the user's stop instruction.
- The adaptive mechanism is always active, but a genuinely simple Brainstorming scope may complete after one short round when no further valuable decisions are uncovered.
- `#grill` is removed from the target interaction model rather than retained as an override.

## Chosen direction so far

Replace “lightweight Brainstorming by default, conditional grilling” with “adaptive grilling by default for every Brainstorming scope”.

The agent explores decision consequences iteratively, continues while further questioning has meaningful expected decision value, performs an explicit final challenge pass before completion, and uses no hard question-count threshold. A simple scope can still finish quickly. A complex scope can legitimately require many rounds.

## Trade-offs / questions

The remaining design frontier concerns:
- how the agent systematically searches for missing decision branches without turning that search into a rigid checklist;
- whether settled user choices should receive an adversarial/counterfactual challenge before being treated as stable exploratory choices;
- how large user-facing frontier rounds should be when many independent decisions exist;
- how Research should interleave with grilling when a branch depends on agent-findable facts.

## Research needed

No blocking external research identified yet.

## Open questions

- Decision-discovery lenses / coverage method.
- Challenge policy for already-settled material user choices.
- User-facing frontier batching when the frontier is large.
- Research interleaving behavior.

## Outcome of this session

- Tentative conclusions: adaptive grilling is the default interaction method of every Project Workflow Brainstorming scope; it continues by expected decision value, uses a mandatory final challenge pass, has no numeric cap, permits short simple sessions, and removes `#grill` from the target model.
- Explicit user/product choices to promote through Project Definition: all choices listed above.
- Research still needed: none blocking at this point.
- Open questions: decision-discovery coverage, challenge policy, frontier batching, and Research interleaving.
- Next phase/action: `continue brainstorming`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
