# ADR — Bounded Parallel Task Cards in codex_only

- Decision ID: `ADR-CODEX-PAR-001`
- Date: `2026-09-19`
- Status: `accepted`
- Authority: `explicit user/product direction`
- Supersedes: `chatgpt_only-style one-in-progress-Card invariant for codex_only only`
- Related requirements: `requirements/CODEX_ONLY_POLICY.md (CO-REQ-017..023)`
- Related milestone/card: `none until Planning`

## Context

Current `chatgpt_only` is intentionally serial per selected Task Board. Codex Main with `codex_workflow` can safely realize multiple isolated worker lanes, but planning-time expectations alone cannot prove that future repository state remains safe for concurrent mutation.

## Decision

codex_only remains serial by default but may execute a bounded set of Task Cards concurrently inside one workstream.

Planning may describe:
- dependency relationships;
- planned work packages that are candidates for overlap;
- expected ownership boundaries.

Execution Prep/JIT must decide actual current-state eligibility immediately before concurrency. A Card may join a parallel ready set only when:
- dependencies are complete;
- it is explicitly `parallel_safe`;
- mutable `write_scope` is bounded and disjoint from every concurrent Card;
- `exclusive_resources` do not conflict;
- each concurrent local mutation has a separate worktree/equivalent isolated workspace;
- the integration base and merge/reconciliation path are recoverable.

Codex Main is the only owner/writer of the shared Project Workflow Task Board and integration state. Worker lanes execute their bounded Card contracts and return evidence/results to Main; they do not independently mutate shared project coordination state.

Use bounded deterministic ready-set semantics, not an unrestricted generic scheduler.

## Rationale

This permits real concurrency where current evidence proves it safe while preserving deterministic recovery, clear ownership and simple serial fallback.

Planning can expose useful parallel structure without pretending to know future file/resource overlap before JIT source inspection.

## Alternatives considered

### Keep codex_only fully serial

Rejected because it leaves available isolated worker concurrency unused for demonstrably independent Cards.

### Let Planning permanently certify parallel safety

Rejected because repository/runtime state can change before execution.

### Allow workers to update Task Board independently

Rejected because concurrent project-state writers create coordination races and ambiguous recovery authority.

### Generic DAG scheduler

Rejected as unnecessary complexity. The project needs a bounded compatible ready set, not a second runtime scheduler.

## Consequences

- codex_only Task Board/Card contracts need explicit bounded parallel metadata/ownership semantics.
- Execution Prep gains a current-state safety gate.
- Recovery must preserve lane evidence/results and integrate them deterministically.
- Serial execution remains valid whenever safety proof is absent or fails.

## Required authoritative updates

- Requirements / Project Definition: `requirements/CODEX_ONLY_POLICY.md`
- Planning: define milestone/work-package coverage for schema/contracts, execution/recovery and validation.
- Task Card/OpenSpec: JIT-refine exact `write_scope`, resources and integration expectations.
- PROJECT.md: record this ADR in active workstream authority pointers.

## Provenance

- Source: initiating feature request, 2026-09-19.
- Evidence: legacy bounded-parallel branch used as compatibility inventory only; current ChatGPT-only serial contracts used as contrast.
