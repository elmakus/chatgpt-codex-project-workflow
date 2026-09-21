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

## Proportional evidence path and external prior art

Use the **smallest evidence path sufficient for the exact research question**.

When the question concerns public software, APIs, libraries, protocols, tooling, design patterns, known failure modes or another domain where relevant external prior art is reasonably likely to exist and materially help, Research MUST actively look for that prior art before defaulting to a bespoke/original solution.

Relevant prior-art sources SHOULD include, as applicable:
- official/upstream documentation and source;
- changelogs and release notes;
- upstream issues/discussions and public issue trackers;
- comparable-project implementations;
- practical community/forum/social reports and discussions.

Purely repository-local or private-state questions do not require broad external discovery when external prior art cannot materially improve the answer.

## Source quality, conflicts and limitations

Distinguish evidentiary weight rather than treating all sources as equivalent.

- Stronger/primary/upstream evidence takes precedence when sources conflict.
- Community/forum/social evidence MAY supply practical failure modes, workarounds or candidate solutions, but popularity does not make it authoritative.
- Check anecdotal/community findings against stronger sources when practical.
- Surface conflicting evidence explicitly instead of silently normalizing it into one conclusion.
- If a materially required external source path is unavailable, record the concrete limitation; never fabricate evidence or imply verification that did not occur.

## Bounded stopping

Research is not an exhaustive crawl. Once enough source-grounded evidence exists to answer the exact question and compare meaningful alternatives, stop searching rather than expanding the source set indefinitely.

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
