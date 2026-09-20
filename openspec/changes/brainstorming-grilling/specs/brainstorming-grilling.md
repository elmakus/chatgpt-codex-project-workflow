# Specification — Brainstorming grilling

## Requirement: interaction method, not lifecycle

Grilling MUST remain an interaction method inside Brainstorming and MUST NOT create a workflow phase, authority layer, intake kind or workstream.

### Scenario: lightweight Brainstorming

Given a simple scope without material ambiguity, dependent user decisions or materially different solution paths, Brainstorming MAY remain lightweight without entering the full grilling method.

### Scenario: automatic activation

Given materially ambiguous goals, materially different solution paths, or unresolved user decisions whose answers gate other decisions, Brainstorming MUST use grilling without relying on a numeric question-count threshold.

## Requirement: manual force control

An intentional `#grill` directive MUST force grilling only for the currently active Brainstorming scope. It MUST NOT create or recover a workstream and MUST NOT be interpreted as Intake.

## Requirement: dependency-aware frontier

Grilling MUST model material unresolved user decisions as a transient dependency-aware decision tree and compute the current frontier from unresolved decisions whose prerequisites are settled.

Each frontier round MUST:
- ask the currently independent material user decisions together;
- number the questions;
- include an explicit assistant recommendation for each question.

Facts that the agent can establish through permitted tools or Research MUST remain agent-owned work rather than being delegated to the user.

After each user round, the agent MUST incorporate accepted answers and recompute the decision tree/frontier before dependent questions are exposed.

## Requirement: durable recovery

The full transient decision tree MUST NOT be mandatory durable state. Durable Brainstorming state MUST preserve accepted choices, unresolved material decisions, material dependency relations and research needs sufficient for recovery.

## Requirement: completion and user stop

Normal grilling completion MUST require every material branch to be resolved or explicitly classified as deferred/non-blocking.

A clear user request to stop grilling MUST stop further grilling questions immediately. The unresolved remainder MUST then be classified by materiality:
- unresolved material blockers keep Brainstorming open;
- marginal/non-blocking items MAY be recorded as deferred without preventing readiness for Project Definition.

Grilling MUST NOT bypass the existing policy-owned Brainstorming → Project Definition promotion gate.

## Requirement: intake and policy isolation

`#issue` and `#feature` remain the only explicit new-workstream Intake directives.

Equivalent grilling semantics MUST exist in `workflow/chatgpt_only/BRAINSTORMING.md` and `workflow/codex_only/BRAINSTORMING.md` without importing execution mechanics across policy namespaces.

`wait-what` remains outside this change.
