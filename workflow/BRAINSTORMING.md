# Brainstorming

## Goal

Explore the problem space without accidentally converting possibilities into requirements or decisions.

## Canonical location

Project brainstorming lives in `brainstorming/`. Use `templates/BRAINSTORM.md` for substantial sessions and `templates/OPEN_QUESTIONS.md` for unresolved questions.

## Non-negotiable distinction

**BRAINSTORMING != DECISION.**

Brainstorming may contain:
- ideas;
- alternatives;
- hypotheses;
- experiments;
- pros/cons;
- assumptions to verify;
- rejected or merely considered directions.

Nothing in `brainstorming/` becomes authoritative merely because it was written down or discussed repeatedly.

When the user explicitly accepts a choice:
1. create or update a record in `decisions/`;
2. update canonical requirements or planning if the decision changes them;
3. update `PROJECT.md` pointers/status when material.

Do not rewrite history to make old brainstorming look settled.

## Working method

1. Clarify the problem, current state, target state and constraints.
2. Separate known facts, user decisions, assumptions and implementation-time choices.
3. Identify open questions and research needs.
4. Compare options at the level justified by current evidence.
5. Delay freezing architecture until adequate verification exists.
6. Persist useful tentative work in the project repository so chat length is not project memory.

## Adaptive grilling interaction method

Adaptive grilling is the default interaction method inside every Brainstorming scope. It is **not** a separate workflow phase, Intake kind, workstream kind or authority layer, and no entry route or manual operator directive controls whether it applies.

Depth is proportional to the expected decision value of another sensible round. A genuinely simple scope may finish after one short user round when the completion audit finds no further material decision value. Do not manufacture low-value questions merely to increase depth, and do not use a fixed minimum/maximum question count or round count. Having enough information to implement is **not** by itself a Brainstorming completion condition.

### Decision surface, tree and frontier

During Brainstorming:

1. Model material unresolved **user/product/strategic decisions** as a transient dependency-aware decision tree.
2. Search the relevant decision surface with adaptive internal lenses such as goal/non-goals, user/UX, scope, architecture/interfaces, data/state, dependencies, failure/edge cases, migration/backward compatibility, security/operations and acceptance. Use only lenses that are relevant; do not turn them into a rigid user-facing checklist.
3. Keep agent-findable facts agent-owned. Establish them through permitted tools/evidence or the applicable Research route instead of delegating research to the user.
4. Compute the current **frontier** from material unresolved decisions whose prerequisites are already settled.
5. Select a coherent thematic batch from that frontier. Split a large frontier into digestible groups rather than dumping it at once. Number each material decision question and include an explicit assistant recommendation for it.
6. Incorporate the user's answers as exploratory accepted choices. Give each material settled choice one bounded adversarial/counterfactual challenge before treating it as stable exploratory state.
7. After every user round, Research reconciliation, challenge result or material reopening, recompute the decision tree/frontier before exposing dependent questions or declaring completion.
8. Continue while another sensible round has meaningful expected value for changing scope, UX, architecture, constraints, acceptance or important edge cases.

### Challenge stability and reopening

Once a material choice has received its bounded challenge, do not repeatedly reopen it merely to prolong exploration.

Reopen that choice only when materially new evidence, contradiction or changed context undermines it. Recompute any dependent branches/frontier when a choice reopens.

### Durable state and recovery

The full transient decision tree is working state and is not required durable authority.

Persist only enough Brainstorming state for fresh-session recovery:
- accepted exploratory choices;
- unresolved material decisions;
- material dependency relations between those decisions;
- challenge/reopening state when needed to avoid duplicate challenge churn;
- research needs/evidence obligations.

This durable state remains exploratory and must not become a second requirements/decision authority or a persisted conversation transcript.

### Completion and user-requested stop

Before normal completion, perform a bounded completion audit across the relevant decision surface and one final challenge/discovery pass. Completion is allowed only when another sensible round has low expected value for changing material scope, UX, architecture, constraints, acceptance or important edge cases.

A clear natural-language user stop such as “dobra, wystarczy” halts new Brainstorming questions immediately. Do not manufacture lower-value follow-ups after that stop. Then classify the unresolved remainder:
- unresolved material product/strategic blockers keep the exploratory scope tentative and prevent it from being treated as ready to leave Brainstorming;
- marginal/non-blocking items may be recorded as deferred.

Stopping questions does not authorize a downstream phase transition and does not bypass the active route's existing promotion/authority boundary.

## Exit conditions

Brainstorming can transition to research when claims require verification, or to planning when enough facts and accepted decisions exist to define authoritative requirements and target state.

Do not create implementation Task Cards or a detailed OpenSpec prematurely merely because ideas are becoming concrete.
