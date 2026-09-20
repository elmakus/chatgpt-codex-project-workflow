# Decision — Integrate grilling as a Brainstorming interaction method

- Decision ID: `ADR-BGR-001`
- Date: `2026-09-20`
- Status: `accepted`
- Authority: `user`
- Supersedes: `none`
- Related requirements: `requirements/BRAINSTORMING_GRILLING.md`
- Related milestone/card: `none`

## Context

Project Workflow already has a Brainstorming phase, an explicit Brainstorming → Project Definition promotion gate, and separate Intake semantics for `#feature` / `#issue`. Matt Pocock's `grilling` skill provides a useful dependency-aware interviewing method, while its `grill-me` wrapper demonstrates a separate explicit invocation surface.

The feature needs the interviewing discipline without creating a competing workflow lifecycle or bloating durable state.

## Decision

Adopt decision-tree/frontier grilling as a conditional interaction method inside existing Brainstorming.

- Grilling activates automatically for materially ambiguous, multi-path, or dependency-linked decision scopes.
- `#grill` is an explicit manual force control for the current active Brainstorming scope only.
- `#grill` is not Intake and does not create/recover a workstream.
- Each frontier question includes an assistant recommendation.
- Agent-findable facts are researched by the agent.
- The full transient decision tree is not durable authority; only recovery-relevant outcomes/dependencies are persisted.
- The user may end grilling at any time; the workflow then classifies unresolved remainder by materiality.
- `wait-what` is outside this feature.

## Rationale

This preserves one coherent Brainstorming lifecycle and existing authority boundaries while adding a repeatable method for uncovering dependent decisions. Conditional activation avoids ceremony on trivial scopes. The manual control gives the user an explicit override without expanding the top-level Intake state machine. Concise persistence preserves progressive disclosure instead of turning brainstorming records into transcript logs.

## Alternatives considered

- **Separate Grilling phase** — rejected because it duplicates Brainstorming lifecycle/authority.
- **Mandatory grilling for all Brainstorming** — rejected because it makes simple discovery unnecessarily heavy.
- **`#grill` as workstream intake** — rejected because `#feature` already owns feature workstream creation and recovery.
- **Persist full decision tree** — rejected as low-value mutable telemetry that can be reconstructed from durable choices/open dependencies.
- **Include `wait-what`** — rejected as a distinct communication/repitch concern.

## Consequences

- Policy-local Brainstorming contracts need compatible grilling semantics.
- Routing/intake documentation must distinguish `#grill` from `#feature` / `#issue`.
- Tests should prove automatic triggering behavior, frontier dependency ordering, recommendations, manual force behavior, user-stop behavior, and durable-state minimality.
- Existing Definition promotion semantics remain unchanged.

## Required authoritative updates

- Requirements / Project Definition: `requirements/BRAINSTORMING_GRILLING.md`.
- Planning: create a Master Plan covering policy-local Brainstorming, routing/manual directive semantics, tests and documentation.
- Task Card/OpenSpec: determined by Planning/Execution Prep.
- PROJECT.md: clear the active exploratory pointer after Definition completion; workstream manifest becomes the scope-local authority locator.

## Provenance

- Source discussion/request: user-promoted `brainstorming-grilling@R1`.
- Evidence/research: current Project Workflow Brainstorming/Intake contracts and upstream `mattpocock/skills` productivity skill structure.
- Strategic `request_id`: none.
- Exact `DECISION FOR CODEX:` marker: none.
- Persisting commit: recorded by repository history.
