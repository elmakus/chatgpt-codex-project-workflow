# Brainstorm — Adaptive grilling as the default Brainstorming method

Date: `2026-09-21`
Scope ID: `adaptive-brainstorming-grilling`
Revision: `R1`
Status: `ready_for_definition`

## Problem / goal

The existing grilling integration is too easy for an agent to satisfy shallowly: a few high-level questions can technically satisfy the contract even when meaningful downstream decisions remain. At the same time, reproducing an intentionally exhaustive 100–200-question interview for every topic would be excessive.

Target direction: every Project Workflow Brainstorming scope should naturally use adaptive grilling, with depth proportional to the decision value still available.

## Current understanding

### Verified facts

- Current ChatGPT-only and Codex-only Brainstorming contracts make grilling conditional on ambiguity, multiple solution paths, or decision dependencies.
- Current grilling tests primarily verify textual contract presence rather than end-to-end conversational depth.
- The current completion rule can be satisfied after a small number of high-level questions if the agent classifies the remainder as non-material.
- The legacy/mixed policy route still reaches `workflow/BRAINSTORMING.md`, so “every Brainstorming in Project Workflow” necessarily includes that active path in addition to the migrated fixed-policy namespaces.

### Existing accepted decisions

- Brainstorming remains exploratory rather than accepted Definition authority.
- Agent-findable facts remain agent-owned; user-facing questions focus on user/product/strategic choices.
- Questions are dependency-aware, frontier-based, numbered, and include an assistant recommendation.
- The user may stop Brainstorming questioning at any time with clear natural language.
- Project Definition promotion remains a separate user-owned gate.

### Explicit user/product choices from this exploration

- Adaptive grilling is the natural/default interaction method of **every Brainstorming scope in Project Workflow**, regardless of how that Brainstorming was entered.
- The behavior is not tied to `#feature`, `#issue`, or any manual grilling trigger.
- The same adaptive method applies across all active Brainstorming routes, including ChatGPT-only, Codex-only and the legacy/mixed Brainstorming path.
- The behavior must be meaningfully deeper than the current shallow 2–3-question experience.
- The behavior must not manufacture huge numbers of low-value questions merely to imitate exhaustive `grill-me`.
- Grilling may finish only when another sensible round has low expected value for changing scope, UX, architecture, constraints, acceptance, or important edge cases. Merely knowing enough to implement is not sufficient.
- Apparent completion requires one final challenge/discovery pass asking what has not yet been surfaced that could matter later. If that pass discovers material decisions, grilling continues.
- There is no fixed numeric limit on questions or rounds. Depth is governed by decision value and the user's stop instruction.
- The adaptive mechanism is always active, but a genuinely simple Brainstorming scope may complete after one short round when no further valuable decisions are uncovered.
- The agent uses a broad set of decision-discovery lenses internally — including goal/non-goals, user/UX, scope, architecture/interfaces, data/state, dependencies, failure/edge cases, migration/backward compatibility, security/operations and acceptance — but asks only questions that are actually relevant. These lenses are not a user-facing rigid checklist.
- Before declaring completion, the agent performs a bounded completion audit across the relevant decision surface so it cannot claim “low expected value” without checking for material omissions.
- Each material settled user choice receives one bounded adversarial/counterfactual challenge before being treated as stable exploratory state.
- A previously challenged/settled choice is automatically reopened when materially new evidence, contradiction or changed context undermines its premises.
- User-facing rounds are thematic and digestible. A large independent frontier is split into coherent groups rather than dumped into one huge question block; there is no fixed numeric batch-size threshold.
- When a decision branch depends on an agent-findable fact, the agent performs the required Research itself, reconciles the result back into the same decision tree/frontier, and only then resumes Brainstorming. The user is not used as a substitute research tool.
- A clear user stop ends further questioning immediately. If unresolved material product/strategic blockers remain, Brainstorming stays tentative and cannot become `ready_for_definition`; the agent reports the blocker briefly and preserves it for later continuation.
- `#grill` is removed completely from the active workflow interaction model rather than retained as an override or compatibility alias. Active router, Intake, Brainstorming, docs/examples/spec/tests should no longer present it as a supported operator directive. Historical records may retain it as provenance.

## Chosen direction

Replace “lightweight Brainstorming by default, conditional grilling” with “adaptive grilling by default for every Brainstorming scope”.

The agent:
1. maintains a dependency-aware decision tree/frontier;
2. searches the relevant decision surface using adaptive internal lenses;
3. asks thematic, digestible frontier rounds with numbered questions and recommendations;
4. owns fact-finding and interleaves Research when needed;
5. incorporates answers and recomputes the frontier after every user round;
6. gives each material settled choice one bounded counterfactual challenge unless new evidence later reopens it;
7. continues while further questioning has meaningful expected decision value;
8. performs a completion audit and one final challenge/discovery pass before declaring the scope complete;
9. uses no hard question/round count;
10. respects an immediate natural-language user stop without hiding unresolved material blockers.

This method applies to every active Project Workflow Brainstorming route, including migrated fixed policies and the legacy/mixed route.

## Alternatives rejected or narrowed

### Keep conditional grilling
Rejected because it permits the current shallow experience and makes depth depend too much on the agent's initial classification.

### Mandatory exhaustive interview
Rejected because forcing large question counts creates low-value ceremony. Depth should follow decision value rather than a quota.

### Keep `#grill` as an override
Rejected because grilling is now intrinsic to Brainstorming. A separate operator command would create two conceptual modes and require the user to remember implementation detail.

### Fixed question or round cap
Rejected because appropriate depth varies by subject.

### Whole-frontier dump
Rejected in favor of thematic batching for usability.

### Permanent closure of challenged choices
Rejected because materially new evidence must be able to reopen an earlier exploratory choice.

## Research needed

No blocking external research identified.

## Open questions

No material product/strategic questions remain for this scope.

## Final discovery / challenge pass

The final pass checked:
- entry-path independence;
- all active Brainstorming policy routes, including legacy/mixed;
- premature-completion loopholes;
- research-driven reopening of settled choices;
- user-stop semantics with unresolved blockers;
- batching/usability;
- numeric-limit avoidance;
- complete removal of the `#grill` active operator surface.

No additional material product decision was found.

## Outcome of this session

- Tentative conclusions: adaptive grilling is the default interaction method of every Project Workflow Brainstorming scope; depth follows expected decision value, relevant decision-surface coverage, iterative consequence discovery, bounded counterfactual challenge and a mandatory final challenge/completion audit.
- Explicit user/product choices to promote through Project Definition: all choices listed above.
- Research still needed: none blocking.
- Open questions: none material.
- Next phase/action: `ready for definition`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
