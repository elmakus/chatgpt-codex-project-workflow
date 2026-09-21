# Brainstorm — Research agent behavior

Date: `2026-09-21`
Scope ID: `research-agent-behavior`
Revision: `R2`
Status: `ready_for_definition`

## Problem / goal

Strengthen Project Workflow Research so that, when relevant, it actively checks external prior art and real-world problem reports/solutions instead of solving every problem from first principles, while preserving the evidence-versus-authority boundary.

## Current understanding

### Verified facts

- Shared Research goal today is to produce source-grounded findings that can support Project Definition and later planning without conflating evidence with accepted intent.
- A Research artifact distinguishes verified facts/sources, repository observations, assumptions, uncertainties, alternatives, recommendation when requested, and unresolved authority questions.
- Research is evidence only. It does not directly create accepted requirements, decisions or plan authority.
- Under the current repository policy `chatgpt_only`, ChatGPT itself executes the Research role. There is no separate runtime Investigator realization in the ChatGPT-only Research contract.
- A durable Research obligation records exact origin, exact question, exact Return target, status and reconciliation state so a fresh session can resume without chat history.
- Pre-execution Research is located through the selected workstream manifest `routing.research_obligation`; implementation/recovery Research is located through the selected Task Board `research_obligation`.
- On completion, Research returns to its exact recorded Return target. It cannot choose a new destination from chat history.
- In `codex_only`, an active Research obligation may be realized by a runtime Investigator, but concrete Investigator harness/model/session mechanics belong to `codex_workflow`, not Project Workflow.
- Repository drift exists in `templates/RESEARCH.md`: its explanatory footer still says ChatGPT-only pre-execution Research uses a root `PROJECT.md` active-research pointer. Current `workflow/chatgpt_only/RESEARCH.md`, `workflow/chatgpt_only/ROUTER.md`, and root `PROJECT.md` instead define the selected workstream manifest `routing.research_obligation` as the authoritative pre-execution pointer. The policy-local route owns pointer semantics, so the template footer is stale documentation rather than current authority.

### Existing accepted decisions

- Current project execution policy is `chatgpt_only`.
- Brainstorming routes to Research when material claims require verification.
- Research completion does not authorize Brainstorming → Project Definition promotion.

### Explicit user/product choices from discovery

- Research should not stop at local repository/document inspection when the problem may already have known external solutions.
- When relevant, Research should search the internet for prior art: similar problems, issue reports, discussions and how other people/projects solved them, specifically to avoid reinventing the wheel.
- This stronger Research behavior should apply consistently to both `chatgpt_only` and `codex_only`; only the concrete role realization differs.
- The stale pointer description in `templates/RESEARCH.md` should be repaired in the same feature.

## Target behavior candidates

### Shared Research investigation contract

Research should use the smallest useful evidence path for the question, but when the subject plausibly has external prior art it should include external discovery rather than defaulting to an original solution.

Relevant evidence classes may include:
- current project/repository state;
- official/upstream documentation and primary sources;
- upstream source, changelogs, issues and discussions;
- public issue trackers and implementation examples from comparable projects;
- community reports/forums/discussions when they provide practical failure modes or solutions;
- external web sources needed to verify current behavior or constraints.

Community evidence is supporting evidence, not automatically authoritative. Conflicting or anecdotal reports should be identified as such and checked against stronger sources when possible.

### Applicability

The shared Research quality/evidence contract should apply under both fixed policies:
- `chatgpt_only`: ChatGPT performs the Research role directly;
- `codex_only`: the Research obligation may be realized by a runtime Investigator, while `codex_workflow` continues to own model/harness/session mechanics.

Project Workflow should specify expected evidence behavior, not a concrete model or runtime implementation.

### Boundedness

Research should remain proportional:
- skip broad internet searching for purely local/private/repository-internal facts when external prior art cannot materially help;
- search external prior art when the problem involves public software, APIs, libraries, protocols, tooling, known failure modes, design patterns or other domains where existing solutions are reasonably likely;
- stop when enough source-grounded evidence exists to answer the exact Research question and compare meaningful alternatives, rather than searching indefinitely.

## Trade-offs / questions

- Stronger external discovery improves reuse of established solutions and lowers the chance of reinventing the wheel.
- Community reports can expose real failure modes not covered by official documentation, but they need clear source-quality labeling.
- The contract should require useful prior-art discovery when relevant without forcing expensive web research for every trivial local question.
- Runtime-specific Investigator mechanics must remain outside Project Workflow.

## Research needed

No additional formal Research is required before Project Definition. The remaining work is to formalize the accepted target behavior and its exact boundaries.

## Open questions

No material user/product decision remains blocking Project Definition. Exact source ordering, minimum evidence wording and stopping criteria can be formalized in Definition/Planning as long as they preserve the user choices above.

## Outcome of this session

- Tentative conclusions: Research should explicitly look for relevant external prior art and real-world solutions when that can materially help, rather than relying only on local evidence or inventing a new solution.
- Explicit user/product choices to promote through Project Definition:
  - relevant internet/prior-art/community search becomes part of the Research behavior contract;
  - apply the behavior to both `chatgpt_only` and `codex_only`;
  - preserve runtime ownership boundaries for Codex Investigator realization;
  - repair the stale `templates/RESEARCH.md` ChatGPT-only pointer description.
- Research still needed: none before Definition.
- Open questions: none material at product level.
- Next phase/action: `ready for definition`
- Definition promotion authorization: `user_authorized`
- Definition promotion subject: `research-agent-behavior@R2`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
