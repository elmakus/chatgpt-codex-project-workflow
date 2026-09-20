# Proposal — Brainstorming grilling

## Why

Current policy-local Brainstorming contracts do not define dependency-aware decision-frontier grilling, while Intake reserves explicit workstream creation for `#issue` and `#feature`.

## Change

Add conditional decision-tree/frontier grilling inside existing Brainstorming for both migrated policy namespaces, plus a manual `#grill` force control that applies only to the active Brainstorming scope and is never Intake.

The changed behavior keeps lightweight Brainstorming legal, keeps researchable facts agent-owned, requires recommendations on frontier questions, persists only recovery-relevant outcomes/dependencies, honors user-requested early stop, and preserves the existing explicit Brainstorming → Project Definition promotion gate.

## Non-goals

- no new workflow phase, authority layer, intake kind or workstream kind;
- no full transient decision-tree persistence;
- no change to `#issue` / `#feature` intake semantics;
- no `wait-what` implementation or runtime dependency on upstream skills.
