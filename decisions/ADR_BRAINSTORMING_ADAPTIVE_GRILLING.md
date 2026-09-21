# Decision — Make adaptive grilling intrinsic to every Brainstorming scope

- Decision ID: `ADR-BGR-002`
- Date: `2026-09-21`
- Status: `accepted`
- Authority: `user`
- Supersedes: `ADR-BGR-001`
- Related requirements: `requirements/BRAINSTORMING_GRILLING.md` revision `R2`
- Related milestone/card: `none`

## Context

ADR-BGR-001 introduced dependency-aware grilling as a conditional Brainstorming interaction method and added a manual `#grill` force control. In practice that contract remained easy to satisfy shallowly: an agent could ask a few high-level questions, classify the remainder as non-material, and end Brainstorming even when further decision discovery could materially reduce downstream rework.

The user wants the useful discipline of `grill-me` without requiring a remembered command and without forcing an arbitrary 100–200-question interview for every scope.

## Decision

Replace conditional/manual grilling with one **adaptive grilling method that is intrinsic to every Project Workflow Brainstorming scope**.

- Every active Brainstorming route uses the method regardless of entry path.
- Depth is governed by the expected decision value of further questioning, never by a fixed question/round quota.
- “Enough information to implement” is not itself a completion condition.
- The agent maintains/recomputes a dependency-aware decision tree/frontier and searches the relevant decision surface with adaptive internal lenses.
- User-facing questions are delivered in coherent thematic batches, numbered, with an assistant recommendation for each material decision.
- Each material settled user choice receives one bounded counterfactual challenge; materially new evidence may reopen it.
- Agent-findable facts remain agent-owned and may invoke the normal Research route before the same exploratory subject resumes.
- Normal completion requires a bounded completion audit plus one final challenge/discovery pass.
- A simple scope may still complete quickly when that audit finds no further material decision value.
- A clear user stop ends further questioning immediately, but unresolved material blockers keep Brainstorming tentative.
- `#grill` is removed completely from the active workflow surface; it is not retained as a compatibility alias.
- Equivalent interaction semantics apply across ChatGPT-only, Codex-only, and legacy/mixed Brainstorming paths while policy-local lifecycle mechanics remain isolated.
- `wait-what` remains outside this scope.

## Rationale

Making adaptive grilling intrinsic to Brainstorming eliminates the user-memory dependency and closes the loophole where an agent can avoid deeper discovery by classifying a session as lightweight too early. Expected decision value provides proportional depth without a brittle numeric threshold. Completion audit, counterfactual challenge, and evidence-driven reopening make “done” harder to claim prematurely while preserving a fast path for genuinely simple work.

Removing `#grill` avoids two conceptual interaction modes for the same phase and keeps the operator surface smaller.

## Alternatives considered

- **Keep conditional grilling plus `#grill`** — rejected because the user should not need to remember an implementation-specific trigger and the conditional path permits shallow completion.
- **Mandatory exhaustive interview / fixed minimum question count** — rejected because it creates low-value ceremony and does not correlate reliably with decision quality.
- **Keep `#grill` as hidden compatibility alias** — rejected because it preserves ambiguity about whether normal Brainstorming is sufficiently deep.
- **Challenge every choice repeatedly** — rejected because it creates churn; one bounded challenge is sufficient absent new evidence/contradiction.
- **Dump the full frontier in one round** — rejected because large question blocks reduce usability; thematic batching preserves the same decision coverage.
- **Persist the complete decision tree** — rejected because concise recovery-relevant exploratory state is sufficient and avoids a second mutable authority system.

## Consequences

- Existing BGR R1 conditional/manual semantics are superseded by BGR R2.
- ChatGPT-only and Codex-only Brainstorming contracts must change from conditional grilling to adaptive default grilling.
- The active legacy/mixed Brainstorming path must gain equivalent interaction semantics.
- Active router/Intake/docs/spec/tests must remove supported `#grill` semantics while historical artifacts may retain provenance.
- Tests must cover actual depth/completion behavior and route coverage, not only the presence of required phrases.
- Existing Research return and explicit Definition promotion semantics remain unchanged.

## Required authoritative updates

- Requirements / Project Definition: `requirements/BRAINSTORMING_GRILLING.md` revision R2.
- Planning: create a new Master Plan revision/change plan covering all active Brainstorming route families, `#grill` removal, OpenSpec reconciliation, behavior-focused tests and docs.
- Task Card/OpenSpec: determined by Planning/Execution Prep; changed behavior requires current OpenSpec reconciliation.
- PROJECT.md: no root live-state mirror; the branch-isolated workstream manifest owns scope-local routing/authority pointers.

## Provenance

- Source discussion/request: user-promoted `adaptive-brainstorming-grilling@R1`.
- Evidence/research: current Project Workflow R1 grilling contracts, their existing contract tests, and current active Brainstorming route structure.
- Strategic `request_id`: none.
- Exact `DECISION FOR CODEX:` marker: none.
- Persisting commit: recorded by repository history.
