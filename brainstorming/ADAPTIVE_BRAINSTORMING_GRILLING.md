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

- Adaptive grilling should be the natural/default interaction method of **every Brainstorming scope in Project Workflow**, not a behavior tied specifically to `#feature`, `#issue`, or manual `#grill`.
- Entry path must not change this behavior: whenever the workflow is in Brainstorming, the same adaptive method applies.
- The behavior should be meaningfully deeper than the current shallow 2–3-question experience.
- The behavior should not manufacture huge numbers of low-value questions merely to imitate exhaustive `grill-me`.
- The user should not need to remember `#grill`; clear natural-language stop remains the primary escape hatch.

## Chosen direction so far

Replace “lightweight Brainstorming by default, conditional grilling” with “adaptive grilling by default for every Brainstorming scope”. Intensity is determined by the value and materiality of unresolved decisions, not by the entry directive or a fixed question count.

## Trade-offs / questions

Open decisions remain around the stopping heuristic, whether to require an explicit second-pass challenge before completion, whether any numeric cap should exist, and what residual meaning `#grill` should have once grilling is already the default.

## Research needed

No blocking external research identified yet.

## Open questions

- Exact diminishing-value stopping rule.
- Whether apparent completion must always trigger one additional decision-discovery pass.
- Whether there should be any hard round/question cap.
- Whether `#grill` remains as an optional “go deeper / continue” override.

## Outcome of this session

- Tentative conclusions: adaptive grilling becomes the default interaction method of every Project Workflow Brainstorming scope.
- Explicit user/product choices to promote through Project Definition: all choices listed above.
- Research still needed: none blocking at this point.
- Open questions: stopping/depth/override mechanics above.
- Next phase/action: `continue brainstorming`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
