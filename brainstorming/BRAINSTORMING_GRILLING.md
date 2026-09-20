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

### Assumptions to verify

- A decision-tree/frontier discipline will improve substantial Brainstorming sessions without making trivial feature discovery cumbersome.
- The same semantic method should likely apply to both `chatgpt_only` and `codex_only`, with policy-local wording where needed.
- A separate user-facing alias analogous to `grill-me` may not be necessary if `#feature` Brainstorming automatically invokes the method when appropriate.

## Ideas / alternatives considered

### Option A — Make grilling mandatory for every Brainstorming session

Every Brainstorming session builds a decision tree, asks the full frontier in rounds, and finishes only when the frontier is empty.

Pros:
- deterministic;
- hard to leave hidden assumptions;
- easy to test as a workflow contract.

Cons:
- potentially heavy for small or obvious features;
- can turn simple discovery into ceremony.

### Option B — Use grilling conditionally for substantial/open-ended Brainstorming

Keep the existing Brainstorming lifecycle, but require the decision-tree/frontier method when unresolved choices have dependencies, the feature is broad/ambiguous, or the user asks to be grilled.

Pros:
- preserves lightweight discovery;
- adds rigor where it matters;
- fits current workflow rather than creating a new phase.

Cons:
- requires a clear trigger contract so the agent does not under-use it.

### Option C — Add a separate explicit `#grill` / `grill-me` operator route

Create a user-facing operator shortcut that forces the method.

Pros:
- very clear manual control;
- mirrors upstream's explicit `grill-me` entrypoint.

Cons:
- adds another top-level control surface;
- risks duplicating Brainstorming instead of strengthening it;
- unclear whether it should create/recover workstreams or only alter interaction mode.

## Trade-offs / questions

The strongest current direction is Option B: integrate the mechanics into Brainstorming rather than add another lifecycle.

Open product decisions:
1. Conditional versus mandatory use of the decision-tree/frontier method.
2. Whether a dedicated user-facing `#grill` / `grill-me` shortcut is valuable.
3. Whether every frontier question must include an assistant recommendation.
4. Whether the frontier should include only user decisions while fact questions are automatically researched before/alongside the round.
5. Whether `wait-what`-style repitch behavior belongs in this feature or should be a separate future feature.

## Research needed

No blocking research currently identified. The upstream pattern and current local Brainstorming contracts are sufficiently concrete for product decisions.

## Open questions

See the five product decisions above.

## Outcome of this session

- Tentative conclusions: preserve one Brainstorming lifecycle and add decision-tree/frontier interviewing semantics inside it.
- Explicit user/product choices to promote through Project Definition: none yet.
- Research still needed: none blocking.
- Open questions: conditionality, explicit shortcut, recommendations, fact-handling, and scope of `wait-what`.
- Next phase/action: `continue brainstorming`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`. Only explicit user phase promotion may authorize Definition for the exact current scope revision.
