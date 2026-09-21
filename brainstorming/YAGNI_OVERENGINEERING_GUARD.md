# Brainstorm — YAGNI / overengineering guard

Date: `2026-09-21`
Scope ID: `yagni-overengineering-guard`
Revision: `R3`
Status: `ready_for_definition`

## Problem / goal

Project Workflow has several local proportionality rules but no general engineering invariant against adding complexity for hypothetical future needs.

The selected direction is a compact policy-neutral YAGNI / proportional-design rule that rejects speculative complexity while preserving all complexity required by current accepted authority, verified evidence and current quality obligations.

## Current understanding

### Verified facts

Repository baseline:
- current `main` has no general YAGNI / anti-overengineering invariant;
- existing local mechanisms already reduce unnecessary process/context/work in specific situations (lightweight Brainstorming, micro-fix, JIT planning, progressive disclosure, bounded Task Cards).

External Research (`research/YAGNI_PRACTICES_R1.md`) found a consistent pattern across established engineering guidance and public agent instructions:
- solve the concrete current problem;
- avoid genericity/capability added for hypothetical future needs;
- keep changes/design proportional and focused;
- require extra machinery to have a concrete current justification;
- do not interpret YAGNI as permission to skip refactoring, tests, security, compatibility or other current code-health obligations;
- avoid premature abstractions; let abstractions emerge from demonstrated current variation/need.

### Existing accepted decisions

- Project Workflow prefers proportional process for simple versus complex work.
- Planning and execution may not silently invent accepted product/system intent.
- Future implementation detail should be delayed when predecessor evidence is required.
- Progressive disclosure is selective by context but lossless by authority.

### Explicit user/product choices from this exploration

- Adopt the global YAGNI-style direction.
- Treat it as a policy-neutral engineering invariant across the workflow.
- Reject speculative complexity without blocking complexity justified by concrete current requirements/evidence.
- Compare the direction against established external practice before Definition; that Research is complete and supports the direction.

## Chosen direction

Adopt this evidence-refined invariant concept:

> **YAGNI / proportional design:** Prefer the simplest solution that fully satisfies the current accepted requirements, decisions, constraints and verified evidence. Do not add speculative abstractions, generality, extensibility, configuration, dependencies, infrastructure, compatibility paths or future-proofing for hypothetical needs. Every material increase in complexity must have a concrete current justification. YAGNI does not justify skipping current correctness, security, testing, maintainability/refactoring or compatibility obligations. Generalize when current evidence shows the shared abstraction or another current constraint requires it, not merely because reuse might appear later.

Operational review question:

> Which current requirement, accepted constraint, verified evidence, existing contract or demonstrated current reuse justifies each material piece of extra complexity?

## Evidence-backed corollaries

1. “Simplest” means least unnecessary complexity while satisfying the complete applicable authority/constraint surface; it does not mean shortest code or fewest files.
2. Prefer existing fitting mechanisms/helpers/platform capabilities before adding new machinery, unless the existing mechanism cannot cleanly satisfy current authority.
3. Do not generalize from hypothetical reuse. Temporary duplication can be preferable to the wrong abstraction while the real variation is still unknown.
4. Keep changes focused and avoid unrelated cleanup/refactoring unless it is required by the current change.
5. No numeric abstraction threshold, complexity score, budget, registry or new lifecycle gate is needed.
6. Known compatibility, safety/security, migration, integration or measured performance constraints count as current justification when supported by present authority/evidence.

## Alternatives rejected or narrowed

### Bare YAGNI slogan only

Too ambiguous. It could be misread as “do less quality work” rather than “do not add speculative complexity.”

### Planning/execution-only rule

Too narrow. Speculative complexity can be normalized earlier during Brainstorming/Definition and accepted by reviewers later.

### Numeric abstraction thresholds / complexity budgets

Rejected. External practice is context-sensitive, and extra scoring/process machinery would contradict the feature's purpose.

### “Always prefer duplication”

Rejected. AHA/Sandi Metz supports duplication over a **wrong/premature** abstraction, not permanent duplication when a real current shared concept is established.

## Research needed

None blocking. External-practice comparison is complete in `research/YAGNI_PRACTICES_R1.md`.

## Open questions

No material product/strategic questions remain for this scope.

## Outcome of this session

- Tentative conclusions: adopt the evidence-refined global policy-neutral YAGNI/proportional-design invariant above.
- Explicit user/product choices to promote through Project Definition: global YAGNI direction and concrete-current-justification exception/guardrail.
- Research still needed: none blocking.
- Open questions: none material.
- Next phase/action: `ready for definition`
- Definition promotion authorization: `user_authorized`
- Definition promotion subject: `yagni-overengineering-guard@R3`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
