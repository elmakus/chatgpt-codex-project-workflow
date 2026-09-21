# Specification — Adaptive Brainstorming grilling

## Requirement: intrinsic adaptive method

Every active Project Workflow Brainstorming route MUST use adaptive grilling as its default interaction method. Entry path MUST NOT enable or disable the method. Grilling MUST remain an interaction method inside Brainstorming and MUST NOT create a phase, Intake kind, workstream kind or authority layer.

### Scenario: simple scope

Given a genuinely simple exploratory scope, the agent MAY finish after one short thematic user round only after the completion audit and final discovery/challenge pass find no further material decision value. The agent MUST NOT manufacture low-value questions to increase depth.

### Scenario: implementation readiness is not completion

When the agent has enough information to implement but another sensible Brainstorming round could still materially change scope, UX, architecture, constraints, acceptance or important edge cases, Brainstorming MUST continue.

## Requirement: expected decision value, not quotas

Depth MUST be governed by the expected decision value of further questioning. The contract MUST NOT define a fixed minimum or maximum question count or round count.

## Requirement: dependency-aware decision surface

The agent MUST model material unresolved user/product/strategic decisions as a transient dependency-aware tree and MUST compute a current frontier containing only decisions whose prerequisites are settled.

The agent MUST search relevant decision surface using adaptive internal lenses including, when relevant, goal/non-goals, user/UX, scope, architecture/interfaces, data/state, dependencies, failure/edge cases, migration/backward compatibility, security/operations and acceptance. These lenses MUST NOT become a rigid user-facing checklist.

After each user round, Research reconciliation, challenge result or material reopening, the agent MUST update exploratory state and recompute the frontier before exposing dependent questions or declaring completion.

## Requirement: thematic frontier rounds

User-facing frontier questions MUST be delivered in coherent thematic batches rather than dumping a large frontier at once. Each material decision question MUST be numbered and MUST include an explicit assistant recommendation.

## Requirement: agent-owned facts and Research

Facts the agent can establish through permitted evidence/tools MUST remain agent-owned. When a decision branch depends on such a fact, the applicable Research route MUST establish it, reconcile the result exactly once into the same exploratory subject, and return to that Brainstorming subject before questioning resumes.

## Requirement: bounded challenge and evidence-driven reopening

Each material settled user choice MUST receive one bounded adversarial/counterfactual challenge before it is treated as stable exploratory state.

A challenged choice MUST NOT be repeatedly reopened unless materially new evidence, contradiction or changed context undermines it. When that occurs, the affected choice and dependent frontier MUST be reopened/recomputed.

## Requirement: concise durable recovery state

Durable Brainstorming state MUST preserve accepted exploratory choices, unresolved material decisions, material dependency relations, challenge/reopening state when needed for recovery, and Research needs sufficient for continuation.

The full transient decision tree and conversation transcript MUST NOT become required durable authority.

## Requirement: completion audit and final discovery pass

Before normal completion, the agent MUST perform a bounded audit across the relevant decision surface and one final discovery/challenge pass.

Completion is legal only when another sensible round has low expected value for changing material scope, UX, architecture, constraints, acceptance or important edge cases.

## Requirement: user stop

A clear natural-language request to stop MUST halt new Brainstorming questions immediately. If material product/strategic blockers remain, the exploratory scope MUST stay tentative and MUST NOT be treated as ready to leave Brainstorming. Non-blocking remainder MAY be deferred.

Stopping questions MUST NOT bypass the active route's existing downstream promotion/authority boundary.

## Requirement: route parity and policy isolation

Equivalent adaptive interaction semantics MUST exist in:
- `workflow/chatgpt_only/BRAINSTORMING.md`;
- `workflow/codex_only/BRAINSTORMING.md`;
- active legacy/mixed `workflow/BRAINSTORMING.md`.

Each route MUST retain its own Research, recovery and lifecycle mechanics.

## Requirement: remove the manual operator surface

The previously supported manual grilling operator directive MUST NOT remain an active routing, Intake, Brainstorming, documentation or compatibility surface. Historical artifacts MAY retain it as provenance.

The existing `#issue` and `#feature` Intake semantics MUST remain unchanged.

## Requirement: preserve promotion and scope boundaries

Adaptive grilling MUST NOT bypass or weaken the existing explicit Brainstorming → Project Definition promotion gate where that gate applies. `wait-what` remains outside this change.
