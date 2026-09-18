# Research

## Goal

Produce source-grounded findings that can support requirements, accepted decisions and planning without conflating evidence with decisions.

## Canonical location

Research artifacts live in `research/`. Use `templates/RESEARCH.md` when useful.

## Research workflow

```text
USER GOAL → discovery → research → source verification → alternatives → architecture candidates → accepted decisions → requirements → planning
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

Research becomes authoritative project behavior only through the appropriate target:
- product constraint → `requirements/`;
- accepted choice → `decisions/`;
- approved execution approach → `planning/`;
- implementation-time fact → current Task Card/OpenSpec/evidence, as appropriate.

Preserve provenance when promoting a finding.

If research evidence contradicts already accepted authority during active work, route to strategic resolution rather than silently rewriting downstream contracts.
