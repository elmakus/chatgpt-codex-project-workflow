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
- Clear natural-language stop remains the user-controlled escape hatch.
- Grilling may finish only when another sensible round has low expected value for changing scope, UX, architecture, constraints, acceptance, or important edge cases. Merely knowing enough to implement is not sufficient.
- Apparent completion requires one final challenge/discovery pass asking what has not yet been surfaced that could matter later. If that pass discovers material decisions, grilling continues.
- There is no fixed numeric limit on questions or rounds. Depth is governed by decision value and the user's stop instruction.
- The adaptive mechanism is always active, but a genuinely simple Brainstorming scope may complete after one short round when no further valuable decisions are uncovered.
- `#grill` is removed from the target interaction model rather than retained as an override.
- The agent uses a broad set of decision-discovery lenses internally — including goal/non-goals, user/UX, scope, architecture/interfaces, data/state, dependencies, failure/edge cases, migration/backward compatibility, security/operations and acceptance — but asks only questions that are actually relevant. These lenses are not a user-facing rigid checklist.
- Each material settled user choice receives one bounded adversarial/counterfactual challenge before being treated as stable exploratory state. Once that challenge is passed, the workflow does not repeatedly reopen the choice without new evidence, contradiction or materially changed context.
- User-facing rounds are thematic and digestible. A large independent frontier is split into coherent groups rather than dumped into one huge question block; there is no fixed numeric batch-size threshold.
- When a decision branch depends on an agent-findable fact, the agent performs the required Research itself, reconciles the result back into the same decision tree/frontier, and only then resumes grilling. The user is not used as a substitute research tool.

## Chosen direction so far

Replace “lightweight Brainstorming by default, conditional grilling” with “adaptive grilling by default for every Brainstorming scope”.

The agent explores decision consequences iteratively, searches across relevant decision lenses, challenges material choices once, continues while further questioning has meaningful expected decision value, performs a final challenge/discovery pass before completion, and uses no hard question-count threshold. A simple scope can still finish quickly. A complex scope can legitimately require many rounds.

Research is an interleaved evidence loop inside the same exploratory subject when needed; it does not reset the subject or delegate fact finding to the user.

## Trade-offs / questions

The final challenge pass is now focused on possible loopholes in the completion semantics:
- preventing the agent from prematurely declaring low expected value without actually checking the relevant decision surface;
- deciding what happens when new Research materially undermines a previously challenged/settled exploratory choice;
- ensuring manual user stop remains respected without silently promoting unresolved material blockers;
- deciding whether the removal of `#grill` should be complete across router, Intake, docs/tests/examples rather than leaving a compatibility alias.

## Research needed

No blocking external research identified yet.

## Open questions

- Completion-audit / anti-shortcut semantics.
- Reopening settled choices after materially new evidence.
- User-stop behavior when material blockers remain.
- Scope of `#grill` removal / compatibility behavior.

## Outcome of this session

- Tentative conclusions: adaptive grilling is the default interaction method of every Project Workflow Brainstorming scope; it continues by expected decision value, searches relevant decision lenses, challenges each material settled choice once, uses thematic frontier batching, interleaves agent-owned Research, performs a mandatory final challenge pass, has no numeric cap, permits short simple sessions, and removes `#grill` from the target model.
- Explicit user/product choices to promote through Project Definition: all choices listed above.
- Research still needed: none blocking at this point.
- Open questions: completion anti-shortcut, evidence-driven reopening, blocker-preserving user stop, and complete `#grill` removal semantics.
- Next phase/action: `continue brainstorming`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
