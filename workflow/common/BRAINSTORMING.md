# Brainstorming

## Purpose

Brainstorming explores possibilities before commitment.

Store tentative ideas, alternatives, hypotheses, rough architecture directions, experiments and unresolved questions under `brainstorming/`.

Brainstorming is not accepted authority. Do not silently promote an idea into requirements, decisions or implementation scope.

## Inputs

Read only:
- current user goal/problem;
- already accepted requirements/decisions that constrain the exploration;
- relevant existing project/source context when needed.

Do not load implementation-state machinery unless the brainstorming question actually depends on current execution state.

## Outputs

Useful outputs may include:
- candidate approaches;
- trade-offs;
- risks/unknowns;
- questions requiring research;
- prototype ideas;
- explicit recommendation candidates.

When the user accepts a real decision, persist it under `decisions/` or the appropriate authoritative artifact. Keep rejected/alternative ideas clearly tentative.

## Transition

Move to research when evidence is needed.

Move to requirements/planning only after the relevant user/product intent is sufficiently clear. Do not create Task Cards/OpenSpec merely because brainstorming exists.
