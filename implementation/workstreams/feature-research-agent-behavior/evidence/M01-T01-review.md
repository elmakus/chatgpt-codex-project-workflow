# Independent review — M01-T01 Research agent behavior

Date: `2026-09-21`
Card: `M01-T01`
Verdict: **GREEN**

## Reviewed subject

- Exact review subject: `25ac000cac86c7421c3632f216be1074f61f64ce`.
- Tested implementation head recorded by implementation evidence: `067d32c07f669df99c2acf3b4d1e0d3eb47613aa`.
- Exact Git comparison proves `067d32c0..25ac000c` is one commit and changes only `implementation/workstreams/feature-research-agent-behavior/evidence/M01-T01.md`; no behavioral/source change exists after the tested implementation head.

## Authority and evidence checked

- `requirements/RESEARCH_AGENT_BEHAVIOR.md` — RAB-REQ-001..010.
- `decisions/ADR_RESEARCH_AGENT_BEHAVIOR.md` — ADR-RAB-001.
- `planning/RESEARCH_AGENT_BEHAVIOR_MASTER_PLAN.md` — approved RAB-P1 / M01.
- `planning/reviews/RAB-P1.md` — independent plan review GREEN.
- `implementation/workstreams/feature-research-agent-behavior/cards/M01-T01.md`.
- JIT OpenSpec under `openspec/changes/research-agent-behavior/`.
- Exact reviewed Research contract/template/test changes and implementation evidence.

## Findings

- Shared Research now requires proportional external prior-art discovery when it is reasonably likely to materially help, while preserving a smaller local/private evidence path.
- Source classes, evidentiary weight, stronger-source precedence, community-evidence limitations, explicit conflict surfacing, unavailable-source limitations and bounded stopping all match approved authority.
- Research remains evidence-producing; existing Origin/Return-target/reconciliation and pointer-ownership semantics are unchanged.
- ChatGPT-only and Codex-only apply equivalent shared evidence behavior.
- Codex Investigator model/harness/session realization remains owned by `codex_workflow`.
- The shared template now points ChatGPT-only pre-execution Research to selected-workstream manifest `routing.research_obligation`, with implementation/recovery Research remaining Task-Board-owned.
- No crawler, search index/database, new Research phase/state owner, root-level active Research pointer, runtime mapping or unrelated routing redesign was introduced.
- Focused static contract coverage maps the accepted behavior and boundaries, and the implementation evidence records the required relevant and full-suite verification as GREEN.

## Conclusion

No P0/P1 blocker or acceptance mismatch found. The exact frozen M01-T01 subject satisfies the approved Card, RAB-P1, RAB-REQ-001..010, ADR-RAB-001 and the JIT OpenSpec. Independent Card review is GREEN.
