# Decision — PWv2.1 uses a small stateless executable policy kernel with helper-less parity

- Decision ID: `ADR-PWV21-001`
- Date: `2026-09-23`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@1`
- Related requirements: `requirements/PWV21_POLICY_KERNEL.md`

## Context

Project Workflow V2 already has an executable runtime-neutral router and state contracts. The remaining problem is repeated LLM interpretation of finite mechanical state without turning PW into a second orchestration/state platform or making Python the only place legal semantics exist.

## Decision

- Extend the existing V2 kernel conservatively for mechanically derivable predicates.
- Keep the kernel stateless/read-only with no project database, scheduler or worker/session ownership.
- Introduce a small versioned machine-readable registry for stable mechanical rule metadata and named typed predicates.
- Do not create a general workflow DSL.
- Keep semantic product/strategy/review reasoning in the owning Markdown/LLM roles.
- Every executable mechanical predicate must have canonical human-readable contract semantics sufficient for helper-less recovery.
- Continuously test parity between executable helper and fresh helper-less ChatGPT.
- Repository/Git authority remains sufficient even when the helper, OR/Paseo state and chat memory are absent.

## Consequences

The helper is the preferred mechanical implementation, not a mandatory authority dependency. Mechanical-policy/code/documentation disagreement is a Recovery defect, not permission to guess.
