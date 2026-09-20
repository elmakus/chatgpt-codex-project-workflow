# Brainstorm — Decision-tree grilling in Project Workflow

Date: `2026-09-20`
Scope ID: `brainstorming-grilling`
Revision: `R1`
Status: `tentative`

## Problem / goal

Strengthen Project Workflow Brainstorming so the agent systematically exposes unresolved product/design decisions instead of stopping after a shallow question set or silently choosing downstream branches.

The inspiration is Matt Pocock's `grill-me` / `grilling` pair:
- https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me
- https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling

This scope is about the underlying interviewing method, not copying the upstream skill verbatim.

## Current understanding

### Verified facts

- Our ChatGPT-only and Codex-only Brainstorming contracts already require clarification of problem/current state/target state/constraints, separation of facts/decisions/assumptions, identification of open questions/research needs, and delayed architecture freeze.
- They do not currently define a decision-tree model, dependency-aware question frontier, or round-by-round recomputation of unresolved decisions.
- Upstream `grill-me` is intentionally a tiny user-invoked wrapper. Its body only invokes the separate `grilling` skill.
- Upstream `grilling` contains the real behavior: design tree, current frontier, whole-frontier rounds, numbered questions, a recommended answer per question, agent-owned fact finding, user-owned decisions, and completion only when the frontier is empty.
- Upstream separates invocation policy from reusable behavior: `grill-me` has implicit invocation disabled while `grilling` remains model-reachable.
- Upstream `wait-what` is a separate explicitly invoked repitch tool. It asks the agent to re-explain the prior message with missing context, ASD-STE100 Simplified Technical English, and project ubiquitous language from `CONTEXT.md`.

### Existing accepted decisions

- Brainstorming is exploratory and must not become accepted requirement/decision authority.
- User-owned promotion into Project Definition remains a separate gate.
- Facts/research should be obtained by the agent when available; product/strategic decisions belong to the user.
- Project Workflow should preserve progressive disclosure and avoid unnecessary duplicate machinery.

### Explicit user/product choices from this exploration

- Grilling is **not** a new workflow phase. It is a mechanism inside Brainstorming.
- Use the decision-tree/frontier method conditionally rather than for every trivial Brainstorming session.
- Provide an explicit user-facing way to force grilling in addition to automatic/conditional use.
- Every frontier decision question should include the assistant's recommended answer.
- Facts that the agent can establish itself are the agent's responsibility; frontier questions presented to the user should focus on genuine user/product/strategic decisions.
- `wait-what` is outside this feature's scope. The user may separately adapt/install it as a Polish-language skill.

## Chosen direction

Integrate grilling semantics into the existing Brainstorming working method:

1. Model unresolved decisions as a dependency-aware decision tree when the Brainstorming problem warrants it.
2. Compute the current **frontier**: unresolved user decisions whose prerequisites are already settled.
3. Resolve agent-findable facts without asking the user to do research for the agent.
4. Ask the whole currently independent frontier in one round.
5. Number every question and include an explicit recommended answer.
6. Incorporate the user's answers, recompute the decision tree/frontier, and repeat.
7. Keep Brainstorming exploratory; accepted choices are recorded for later reconciliation by Project Definition.
8. Do not create a separate Grilling phase.
9. Support an explicit manual grilling trigger, with exact invocation semantics still to be decided.

## Alternatives rejected or narrowed

### Mandatory grilling for all Brainstorming

Rejected in favor of conditional use because trivial or obvious feature discovery should remain lightweight.

### Separate Grilling workflow phase

Rejected. The mechanism belongs inside Brainstorming and must not create another lifecycle or authority layer.

### Include `wait-what` in this feature

Rejected from this scope. It is a separate communication/repitch capability rather than Brainstorming lifecycle behavior.

## Remaining frontier

1. **Automatic trigger threshold** — define when ordinary Brainstorming must switch into decision-tree/frontier grilling rather than remain lightweight.
2. **Manual trigger semantics** — define whether `#grill` merely forces grilling for the currently active Brainstorming scope, can start/recover Brainstorming by itself, or should be represented through a Skill-style alias instead.
3. **Durable state granularity** — decide whether the complete decision tree/frontier is persisted or remains conversational/internal while only durable choices/open questions/research needs are written to the Brainstorming record.
4. **Completion rule** — decide whether grilling requires an empty frontier, and how explicitly deferred/non-blocking questions affect readiness for Project Definition.

## Research needed

No blocking research currently identified. The upstream pattern and current local Brainstorming contracts are sufficiently concrete for the remaining product decisions.

## Outcome of this session

- Tentative conclusions: one Brainstorming lifecycle with conditional decision-tree/frontier grilling and a manual force mechanism.
- Explicit user/product choices to promote through Project Definition: the six choices recorded above.
- Research still needed: none blocking.
- Open questions: trigger threshold, manual trigger semantics, durable state granularity, completion rule.
- Next phase/action: `continue brainstorming`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`. Only explicit user phase promotion may authorize Definition for the exact current scope revision.
