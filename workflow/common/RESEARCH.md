# Research

## Goal

Produce source-grounded findings that can support Project Definition and later planning without conflating evidence with accepted intent.

## Canonical location

Research artifacts live in `research/`. Use `templates/RESEARCH.md` when useful.

## Research workflow

```text
USER GOAL → discovery → research → source verification → alternatives → selected-policy Definition entry gate → Project Definition → accepted decisions + requirements → planning
```

Later arrows occur only after the appropriate user/authority decisions. Research itself does not silently accept an option.

## Required distinctions

A research artifact should distinguish:
- verified facts and sources;
- observations from the current project/repository;
- assumptions;
- uncertainties;
- alternatives;
- recommendation, if requested;
- questions still requiring user/product authority.

When current external information matters, verify it rather than relying on stale memory.

## Context discipline

Read only:
- the current research question;
- relevant requirements;
- accepted decisions;
- required source material;
- repository areas needed for that question.

Do not load unrelated implementation history.

## Promoting findings

Research does not directly promote itself into accepted product/system authority.

When findings are ready to influence target behavior:
- return to the policy router;
- route through Project Definition only when the selected policy's entry conditions for Definition are satisfied;
- if research was entered from exploratory Brainstorming and that policy requires explicit user phase promotion, research completion does **not** count as that promotion;
- Definition promotes verified constraints to `requirements/` and explicit accepted choices to `decisions/` with provenance.

Implementation-time facts discovered for already-approved work may still flow to the current Task Card/OpenSpec/evidence as appropriate without redefining product intent.

If research evidence contradicts already accepted authority during active work, route to strategic resolution rather than silently rewriting downstream contracts.
