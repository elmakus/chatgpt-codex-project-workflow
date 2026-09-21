# Decision — Require proportional external prior-art discovery in Research

- Decision ID: `ADR-RAB-001`
- Date: `2026-09-21`
- Status: `accepted`
- Authority: `user`
- Supersedes: `none`
- Related requirements: `requirements/RESEARCH_AGENT_BEHAVIOR.md`
- Related milestone/card: `none`

## Context

Project Workflow already defines Research as source-grounded evidence gathering with strict separation from accepted requirements/decisions/plans. The current contract allows current external verification when needed, but it does not explicitly require the agent to check whether a public problem already has known prior art, issue reports, established workarounds or comparable implementations.

That omission can cause unnecessary first-principles solution design when the wider ecosystem has already encountered and solved the same problem.

## Decision

Adopt proportional external prior-art discovery as part of the shared Research behavior contract.

- When external prior art is reasonably likely to exist and materially help, Research must actively look for it.
- Relevant sources may include official/upstream documentation/source, changelogs, issues/discussions, comparable implementations and community reports.
- Community evidence is useful supporting evidence for practical failure modes and workarounds, but it is not automatically authoritative and should be checked against stronger sources when practical.
- Research remains bounded: purely local/private facts do not require broad web searching when external prior art cannot materially help, and searching stops once the exact question is adequately answered.
- Equivalent evidence behavior applies to `chatgpt_only` and `codex_only`.
- Project Workflow owns the evidence-quality contract; `codex_workflow` continues to own concrete Codex Investigator model/harness/session realization.
- The stale ChatGPT-only pre-execution pointer description in `templates/RESEARCH.md` is corrected as part of the same feature.

## Rationale

The purpose is to avoid reinventing the wheel without turning every Research task into an expensive literature review. Prior-art discovery is highest value for public software/tooling and recurring technical problems, while proportionality prevents unnecessary external search for local facts. Explicit source-quality handling lets practical community experience inform the answer without confusing anecdote with verified authority.

## Alternatives considered

- **Keep current implicit external-search language only** — rejected because it does not reliably cause the agent to look for existing solutions.
- **Require broad internet search for every Research obligation** — rejected as unnecessary overhead for local/private questions.
- **Use only official sources** — rejected because practical issue reports and community discussions often reveal real failure modes, workarounds and implementation experience absent from formal documentation.
- **Move detailed Investigator procedure/model choice into Project Workflow** — rejected because runtime orchestration belongs to `codex_workflow`.

## Consequences

- Shared/common Research guidance needs an explicit prior-art and source-quality section.
- ChatGPT-only and Codex-only Research modules must apply equivalent evidence expectations.
- Tests/verification should prove both the positive case (relevant prior art is required) and negative/proportional case (pure local facts do not force broad web search).
- Shared Research template commentary must be corrected to current workstream-manifest pointer ownership.
- No new workflow phase, mutable state store or runtime orchestration system is required.

## Required authoritative updates

- Requirements / Project Definition: `requirements/RESEARCH_AGENT_BEHAVIOR.md`.
- Planning: create a Master Plan covering common/policy-local Research contracts, template correction and verification.
- Task Card/OpenSpec: determined by Planning/Execution Prep.
- PROJECT.md: no new root mutable Research state; workstream-local authority is carried by the selected manifest.

## Provenance

- Source discussion/request: user-promoted `research-agent-behavior@R2`.
- Evidence/research: current `workflow/common/RESEARCH.md`, policy-local Research/Router modules, `templates/RESEARCH.md`, and verified pointer drift.
- Strategic `request_id`: none.
- Exact `DECISION FOR CODEX:` marker: none.
- Persisting commit: recorded by repository history.
