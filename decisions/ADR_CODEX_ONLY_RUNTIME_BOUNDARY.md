# ADR — Project Workflow / codex_workflow Boundary and Formal Review

- Decision ID: `ADR-CODEX-RT-001`
- Date: `2026-09-19`
- Status: `accepted`
- Authority: `explicit user/product direction`
- Supersedes: `fresh-normal-ChatGPT identity as the universal realization of codex_only independent review`
- Related requirements: `requirements/CODEX_ONLY_POLICY.md (CO-REQ-007..016, CO-REQ-024..025)`
- Related milestone/card: `none until Planning`

## Context

Project Workflow must manage durable project intent/state while `codex_workflow` already provides worker orchestration, including stateful Muse logical worker sessions in release `v1.1.17-private.12`.

Encoding runtime session/worker mechanics in Project Workflow would duplicate ownership and couple durable project state to a specific runtime implementation.

## Decision

Project Workflow owns project semantics: milestones, Cards, dependencies, accepted authority, acceptance, review requirement/subject/state/evidence, project-level parallel ownership, workstream/integration semantics and workflow boundaries.

`codex_workflow` owns concrete worker realization: Executor/Tester/Investigator/Senior selection, model/reasoning/profile, invocation, waiting, worker/session lifecycle, resume/replacement, runtime recovery and worker-concurrency mechanics.

Project Workflow must not persist or require runtime identifiers such as `session_id`, `invocation_id`, Muse leases or concrete worker profile/model identifiers.

Formal Project Workflow independent review is defined semantically, not as a required normal-ChatGPT session identity. A Codex-managed independent reviewer may issue the formal verdict when it:
- is independent from the implementation owner for the exact subject;
- judges an immutable exact subject against the same accepted authority/acceptance surface;
- does not mutate that subject while reviewing;
- produces durable verdict/evidence that Codex Main persists into Project Workflow state.

For implementation review:
- Tester cannot perform production repair;
- RED findings return through Main to the owning Executor;
- repair produces a new immutable review subject/attempt;
- the same logical Tester may perform the full recheck of the new subject when it remains independent and runtime resume is safe;
- runtime may fail closed to a replacement Tester without Project Workflow encoding that session transition.

No second mandatory normal-ChatGPT review follows a qualifying formal Codex-managed review.

## Rationale

Independence is a project-review property; session mechanics are a runtime property. Separating them allows Project Workflow to remain durable and runtime-agnostic while `codex_workflow` can evolve worker/session implementation independently.

## Alternatives considered

### Persist worker/session IDs in Task Board

Rejected. It makes runtime mechanics Project Workflow authority and creates brittle recovery coupling.

### Require fresh normal ChatGPT after every Codex Tester

Rejected. It duplicates independent review without adding a distinct required project gate.

### Require a new Tester for every corrected subject

Rejected. A new immutable subject requires a new review attempt, not automatically a new reviewer identity. Replacement is needed only when independence/resume safety requires it.

## Consequences

- codex_only review modules must describe independence without relying on fresh-chat identity.
- Durable review attempts remain immutable and preserve RED history.
- Runtime capability failures become normal blockers; they do not change execution policy.
- Provenance schema must identify project role/lane ownership without leaking runtime session identity.

## Required authoritative updates

- Requirements / Project Definition: `requirements/CODEX_ONLY_POLICY.md`
- Planning: include policy-local Review/Recovery/State adaptation and validation.
- Task Card/OpenSpec: exact review lifecycle changes are execution contract work.
- PROJECT.md: record this ADR in the active workstream authority pointers.

## Provenance

- Source: initiating feature request, 2026-09-19.
- Evidence: `elmakus/codex_workflow v1.1.17-private.12`, source `d285aa1a271258052d23e3a2d3b585117fc1e862`.
