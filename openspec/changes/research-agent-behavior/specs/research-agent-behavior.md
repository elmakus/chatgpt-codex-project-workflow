# Specification — Research agent behavior

## Requirement: evidence and authority boundary

Research MUST remain evidence-producing. It MUST distinguish verified facts/sources, repository observations, assumptions, uncertainties, alternatives and unresolved authority questions, and MUST NOT silently create accepted requirements, decisions, plans or execution authority.

Existing Origin/Return-target/reconciliation ownership MUST remain unchanged.

## Requirement: proportional prior-art discovery

Research MUST use the smallest evidence path sufficient for the exact question.

When a question concerns public software, APIs, libraries, protocols, tooling, design patterns, known failure modes or another domain where external prior art is reasonably likely to exist and materially help, Research MUST actively inspect relevant external prior art before defaulting to a bespoke solution.

Purely local/private questions MAY complete without broad external discovery when prior art cannot materially help.

### Scenario: public known-failure question

Given a Research question about a public library/tool/API with a plausible recurring failure mode, Research inspects relevant upstream/public prior art before recommending a bespoke fix.

### Scenario: local-only question

Given a question answerable from exact repository/private state where external prior art cannot materially help, Research uses the local evidence path without mandatory broad web search.

## Requirement: source classes and evidentiary weight

External prior-art discovery SHOULD use relevant classes such as official/upstream documentation and source, changelogs, upstream issues/discussions, public issue trackers, comparable-project implementations and practical community reports.

Research MUST distinguish evidentiary weight. Stronger/primary evidence takes precedence when evidence conflicts. Community/forum/social reports MAY supply practical failure modes, workarounds or candidate solutions, but MUST NOT become authoritative by popularity and SHOULD be checked against stronger sources when practical.

Conflicting or anecdotal evidence MUST be surfaced rather than silently normalized.

## Requirement: availability and stopping

When a materially required external source path is unavailable, Research MUST report the concrete limitation rather than fabricate evidence.

Research SHOULD stop once sufficient source-grounded evidence answers the exact question and compares meaningful alternatives. It MUST NOT turn the obligation into an open-ended exhaustive search.

## Requirement: policy parity and runtime boundary

`chatgpt_only` and `codex_only` Research MUST apply equivalent prior-art/source-quality behavior.

Project Workflow defines the evidence contract only. Concrete Codex Investigator model/harness/session/profile realization MUST remain owned by `codex_workflow`.

## Requirement: pointer ownership

The shared Research template MUST describe pointer ownership as policy-local.

For ChatGPT-only pre-execution Research, the owner is the selected workstream manifest `routing.research_obligation`. Implementation/recovery Research remains owned by the selected canonical Task Board `research_obligation`.

The shared template MUST NOT describe root `PROJECT.md` as the active ChatGPT-only pre-execution Research pointer owner.
