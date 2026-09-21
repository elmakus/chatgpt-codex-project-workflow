# Research Investigation Behavior Requirements

Revision: `R1`
Status: `approved`
Updated: `2026-09-21`

## Goal / target state

Project Workflow Research should avoid reinventing solutions when relevant external prior art already exists. Research remains evidence-producing rather than authority-producing, but when the question plausibly benefits from public prior art it actively checks the wider ecosystem for similar problems, known solutions, upstream behavior, implementation examples and practical failure reports.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| RAB-REQ-001 | Research MUST remain an evidence-producing role and MUST NOT directly create accepted requirements, decisions, plans or execution authority. | MUST | existing Research authority; `research-agent-behavior@R2` | accepted |
| RAB-REQ-002 | Research MUST use the smallest evidence path sufficient for the exact research question and MUST remain proportional rather than performing broad external discovery for purely local/private facts when external prior art cannot materially help. | MUST | `research-agent-behavior@R2`; ADR-RAB-001 | accepted |
| RAB-REQ-003 | When a question involves public software, APIs, libraries, protocols, tooling, design patterns, known failure modes or another domain where prior art is reasonably likely to exist and materially help, Research MUST search for relevant external prior art instead of defaulting to an original solution. | MUST | user choice in `research-agent-behavior@R2`; ADR-RAB-001 | accepted |
| RAB-REQ-004 | External prior-art discovery SHOULD include, as relevant, official/upstream documentation and source, changelogs, upstream issues/discussions, public issue trackers, comparable-project implementations and practical community reports/discussions. | MUST | `research-agent-behavior@R2`; ADR-RAB-001 | accepted |
| RAB-REQ-005 | Research MUST distinguish source quality and evidentiary weight. Community/forum/social reports MAY supply practical failure modes, workarounds or candidate solutions, but MUST NOT be treated as authoritative merely by popularity and SHOULD be checked against stronger/primary sources when practical. | MUST | `research-agent-behavior@R2`; ADR-RAB-001 | accepted |
| RAB-REQ-006 | Research MUST distinguish verified facts/sources, current repository observations, assumptions, uncertainties, alternatives and unresolved authority questions; conflicting evidence MUST be surfaced rather than silently normalized. | MUST | existing Research authority; `research-agent-behavior@R2` | accepted |
| RAB-REQ-007 | Research MAY recommend an option when requested or useful, but MUST preserve the existing return-target/authority boundary so the owning role decides what, if anything, becomes accepted authority. | MUST | existing Research authority; `research-agent-behavior@R2` | accepted |
| RAB-REQ-008 | The strengthened evidence behavior MUST apply consistently to both `chatgpt_only` and `codex_only` Research. Project Workflow defines expected evidence behavior; concrete Codex Investigator model/harness/session realization remains owned by `codex_workflow`. | MUST | explicit user choice; ADR-RAB-001 | accepted |
| RAB-REQ-009 | Research MUST have bounded stopping behavior: once enough source-grounded evidence exists to answer the exact question and compare meaningful alternatives, it SHOULD stop rather than continue searching indefinitely. | MUST | `research-agent-behavior@R2`; ADR-RAB-001 | accepted |
| RAB-REQ-010 | Shared templates/documentation MUST describe current policy-local Research pointer ownership correctly. In particular, ChatGPT-only pre-execution Research MUST be described as owned by selected workstream manifest `routing.research_obligation`, not a root `PROJECT.md` active-research pointer. | MUST | verified repository drift; explicit user choice | accepted |

## Constraints

- Preserve the existing Research durable continuation lifecycle, exact origin/return ownership and evidence-versus-authority boundary.
- Preserve branch-first workstream-local routing state.
- Do not move Codex runtime model/harness/session selection into Project Workflow.
- Do not require internet access when unavailable; an unavailable required source path must be reported as a concrete limitation rather than fabricated.
- Keep source-search behavior adaptive to the question rather than a fixed exhaustive checklist.

## Non-goals

- Building a web crawler, search index or separate research database.
- Mandating Reddit/forums/social sources for every Research question.
- Treating community consensus as accepted product/system authority.
- Replacing official/upstream evidence with anecdotal reports.
- Defining a concrete Codex Investigator model, harness, prompt or session lifecycle inside Project Workflow.
- Reworking unrelated Research continuation/routing semantics.

## Global invariants

- Research evidence never silently becomes accepted requirements/decisions/plans.
- The exact recorded Return target continues to own reconciliation.
- External prior-art discovery is required only when it can materially improve the answer.
- Stronger/primary sources take evidentiary precedence over anecdotal community reports when they conflict.
- Policy-local routing remains authoritative over shared template commentary.

## External contracts / dependencies

- Public internet/web search may be used when relevant and available.
- Upstream repositories, documentation, issue trackers and community discussions are evidence sources, not authority owners for this project.
- `codex_workflow` remains authoritative for concrete Codex Investigator realization.

## Data integrity / idempotency / security constraints

- Research must not persist secrets or private-source content into public artifacts unless already authorized for that destination.
- Re-running the same Research obligation must respect the existing durable status/reconciliation lifecycle and must not create duplicate semantic reconciliation.
- Shared documentation must not reintroduce obsolete root-level active Research state.

## Acceptance-level requirements

- A purely repository-local question can complete without broad internet searching when external prior art would not materially help.
- A question about a public library/tool/API with a plausible known failure mode causes Research to inspect relevant external prior art before proposing a bespoke solution.
- Research can cite/use community reports for practical experience while clearly distinguishing them from stronger official/upstream evidence.
- Conflicting official/community findings are surfaced explicitly.
- ChatGPT-only and Codex-only Research contracts expose equivalent evidence-quality/prior-art obligations without duplicating runtime orchestration semantics.
- The stale ChatGPT-only pointer text in `templates/RESEARCH.md` is corrected to match the current manifest-owned pre-execution pointer.
- Existing durable Research return/reconciliation semantics remain unchanged.

## Definition completeness

Definition Complete = GREEN:
- target state and material MUST requirements are explicit;
- proportional prior-art search behavior and source-quality handling are bounded;
- both fixed policies are covered;
- runtime ownership boundaries are explicit;
- template-pointer drift is in scope;
- no unresolved user/product choice remains that can materially alter implementation strategy.

## Downstream coverage

Planning must map these requirements to shared/common Research guidance, both policy-local Research modules, template correction, tests and documentation/verification as appropriate.
