# Codex Orchestration Contract

## 1. Main as orchestrator

The primary Codex agent is the execution orchestrator, not a manual worker-message manager.

It remains responsible for:
- current Task Card outcome;
- dependency and scope boundaries;
- integration;
- tests/acceptance;
- durable Git state;
- blocker escalation;
- final result/evidence.

Delegation does not transfer accountability for the card.

## 2. Bounded delegation

Delegate only a clearly bounded subproblem with:
- explicit objective;
- relevant inputs/context;
- scope boundaries;
- expected output;
- completion/blocked criteria.

Avoid delegating tiny edits that are cheaper and clearer to perform directly.

Avoid giving a worker the entire project context when a narrower package is sufficient.

## 3. Event-driven coordination

Prefer completion events and long event-driven waits over polling.

Normal worker completion should return through the standard completion path.

Do not repeatedly ask workers:
- "status?";
- "are you done?";
- "what percentage?";
- "send progress";
merely because time has elapsed.

A timeout is not evidence that a worker needs a polling/status request. Use an appropriately long event-driven wait or continue independent work when safe.

## 4. Push only for material events

A worker should proactively interrupt/push only for a material event such as:
- a blocker;
- a required course change;
- a critical partial result needed immediately by Main;
- newly discovered evidence that invalidates the delegated assumptions;
- a safety/integrity issue requiring orchestration action.

Do not send routine progress chatter.

Do not wake Main for non-material status.

## 5. Main behavior while workers run

Main may:
- perform independent non-conflicting work;
- prepare integration/test steps;
- inspect already returned durable evidence;
- wait for normal completion.

Main should not create artificial management traffic.

## 6. Worker completion

Worker output should be concise and execution-useful:
- what was established or changed;
- exact relevant files/commits/evidence when applicable;
- tests/checks performed;
- blocker or remaining uncertainty.

Main integrates and verifies the result against the Task Card; worker completion alone does not make the card `done`.

## 7. Delegation and strategic authority

Workers and subagents do not independently change:
- product requirements;
- frozen architecture;
- milestone acceptance;
- strategic decisions.

If delegated evidence requires such a change, return a material blocker/course-change event to Main. Main follows the ChatGPT ↔ Codex strategic blocker contract when needed.

## 8. No orchestration overengineering

Do not build without a concrete need:
- a task database;
- a Jira clone;
- a message broker;
- a generic DAG engine;
- an agent message service/database;
- a vector database;
- a custom workflow engine;
- a polling/status service.

For normal workflow coordination, GitHub plus Markdown/YAML, selective OpenSpec, the direct strategic ChatGPT control channel and existing standard Codex workflow/agent mechanisms are sufficient. Prefer those existing mechanisms over inventing parallel infrastructure.
