# M01 handoff — Research agent behavior

## Checkpoint

- Milestone behavior: GREEN.
- Final behavioral implementation head: `25ac000cac86c7421c3632f216be1074f61f64ce`.
- Final integration result: pending until PR #49 is merged and target-side readback is reconciled.

## Achieved state

Research now uses a shared proportional prior-art/source-quality contract: relevant external prior art is actively checked when it can materially help, local/private-only work remains proportional, source quality/conflicts/limitations are explicit, and searching stops when sufficient evidence exists. ChatGPT-only and Codex-only apply equivalent evidence behavior without changing their continuation semantics or Codex runtime ownership. The shared Research template uses selected-workstream manifest ownership for ChatGPT-only pre-execution Research.

## Authority

- `requirements/RESEARCH_AGENT_BEHAVIOR.md` — R1 / RAB-REQ-001..010.
- `decisions/ADR_RESEARCH_AGENT_BEHAVIOR.md` — ADR-RAB-001.
- `planning/RESEARCH_AGENT_BEHAVIOR_MASTER_PLAN.md` — approved RAB-P1.
- `implementation/workstreams/feature-research-agent-behavior/cards/M01-T01.md`.
- `openspec/changes/research-agent-behavior/`.

## Verification and review

- Implementation verification: `implementation/workstreams/feature-research-agent-behavior/evidence/M01-T01.md`.
- Independent Card review GREEN: `implementation/workstreams/feature-research-agent-behavior/evidence/M01-T01-review.md`.
- Integrated M01 acceptance GREEN: `implementation/workstreams/feature-research-agent-behavior/evidence/M01-acceptance.md`.
- No material exceptions or deferred behavioral items remain in approved M01 scope.

## Next durable starting point

Run final-integration refresh/publication for PR #49 against current `main`. Preserve/reconcile the manifest final-integration review gate, merge only the accepted closure-ready subject, then reconcile merge-result-dependent manifest/Task Board/handoff fields from target-side state.
