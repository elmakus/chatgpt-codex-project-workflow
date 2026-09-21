# Proposal — Adaptive Brainstorming grilling

## Why

The integrated Brainstorming grilling contract is conditional and retains a manual operator trigger. That leaves a shallow path where an agent can ask only a few high-level questions and declare exploration complete even when further decision discovery has material value. The active legacy/mixed Brainstorming route also lacks the newer dependency-aware interaction contract.

## Change

Make adaptive, dependency-aware grilling the intrinsic interaction method of every active Project Workflow Brainstorming route.

The changed behavior:
- scales depth by expected decision value rather than a numeric question/round quota;
- preserves a fast path for genuinely simple scopes only after completion audit;
- recomputes a dependency-aware decision frontier after each user round;
- searches relevant decision lenses internally and asks coherent thematic batches with numbered questions and recommendations;
- challenges each material settled choice once before treating it as stable exploratory state;
- uses normal agent-owned Research for establishable facts and resumes the same exploratory subject;
- requires a bounded completion audit plus one final discovery/challenge pass;
- stops questions immediately when the user clearly asks to stop while keeping material unresolved blockers tentative;
- removes the manual grilling operator surface from active routing, Intake, Brainstorming, docs and tests;
- applies equivalent interaction semantics to ChatGPT-only, Codex-only and legacy/mixed Brainstorming without merging their lifecycle/state mechanics.

## Non-goals

- no new workflow phase, Intake/workstream kind or authority layer;
- no numeric minimum/maximum question or round count;
- no generic questionnaire/scoring runtime or persisted full decision tree;
- no change to user-owned Project Definition promotion;
- no change to policy-local Research/recovery mechanics;
- no rewrite of historical M01/OpenSpec/evidence;
- no `wait-what` implementation.
