# Feature Intake — Brainstorming grilling

## Identity

- Workstream ID: `feature-brainstorming-grilling`
- Intake kind: `feature`
- Branch: `feat/brainstorming-grilling`
- Integration target: `main`
- Base ref: `cdaf47245e45836917b152904d70807bca355e7d`

## Operator intent

Evaluate Matt Pocock's productivity skills, especially `grill-me` / `grilling`, and determine how the useful mechanics could strengthen this Project Workflow's Brainstorming phase without creating a competing lifecycle. Explain `wait-what` as a related productivity pattern, but do not include it in feature scope unless separately accepted.

Reference:
- https://github.com/mattpocock/skills/tree/main/skills/productivity

## Pre-creation discovery

- Existing branch `feat/branch-first-managed-changes` is unrelated to this feature.
- No open pull request or existing workstream was found for grilling / decision-tree brainstorming.
- The feature does not require parent-only state.
- Classification: independent workstream based on normal integration target `main`.

## External pattern findings

- `grill-me` is a user-invoked wrapper whose entire operational purpose is to invoke `grilling`.
- `grilling` owns the actual method:
  - model the design as a decision tree;
  - maintain a frontier of decisions whose prerequisites are already settled;
  - ask the whole current frontier in one round;
  - number questions and provide a recommended answer for each;
  - after user answers, recompute the frontier;
  - facts are the agent's job to investigate; decisions remain the user's;
  - stop only when the frontier is empty and shared understanding is confirmed.
- `wait-what` is a separate user-invoked repitch command: when the prior message did not land, explain again with more context, ASD-STE100 Simplified Technical English, and project ubiquitous language from `CONTEXT.md`.

## Final intake classification

- Path: Brainstorming discovery.
- Integration direction: strengthen the existing Brainstorming working method rather than add a new workflow phase or duplicate skill.
- Canonical downstream artifact: `brainstorming/BRAINSTORMING_GRILLING.md`.
- Canonical scope: `brainstorming-grilling@R1`.
- `PROJECT.md → Active exploratory scope` points to that exact record.
- Promotion into Project Definition remains user-owned and pending.
- Next route: Brainstorming.

## Open product decisions

- Whether decision-tree/frontier behavior should be mandatory for every substantial Brainstorming session or conditional when unresolved decisions form dependencies.
- Whether a user-facing explicit command/alias analogous to `grill-me` should exist in addition to normal `#feature` discovery.
- Whether each frontier question must always include the assistant's recommended answer.
- How aggressively the agent should investigate environmental facts before asking the next frontier round.
- Whether any useful `wait-what` behavior belongs in this feature or should remain a separate future feature.

## Intake state

- State: complete
- Downstream owner: `brainstorming/BRAINSTORMING_GRILLING.md`
