# Research

## Goal

Produce source-grounded findings that can support Project Definition and later planning without conflating evidence with accepted intent.

## Canonical location and durable continuation state

Research artifacts live in `research/`. Use `templates/RESEARCH.md` when useful.

Any Research obligation that may cross a chat/session boundary must have one exact durable research record **before** the origin role yields control.

The record owns at least:
- `Research ID`;
- `Status: active | complete | blocked | consumed`;
- `Origin role`;
- `Origin subject` — exact durable scope/revision/Card/blocker that opened the question;
- `Return target` — exact role/subject that must consume the findings;
- the exact research question.

For pre-execution Brainstorming/Definition/Planning research, project `PROJECT.md → Active research obligation` points to that exact record while it is active or awaiting consumption.

For Research triggered from implementation/recovery, the selected policy's canonical mutable execution state must point to the exact research record instead. Under `chatgpt_only`, that pointer is Task Board `research_obligation`; blocker evidence may be referenced by the record, but `PROJECT.md` must not mirror the execution obligation.

Status semantics:
- `active` — Research is the exact current obligation;
- `blocked` — Research remains current but cannot proceed until its recorded concrete blocker is resolved;
- `complete` — evidence/findings are durably complete and the exact recorded Return target is now the next obligation;
- `consumed` — the Return target durably reconciled the findings; the active pointer may now be cleared.

Do not clear an active research pointer at `complete`. Clear it only after the Return target has durably consumed/reconciled the findings so a crash between research completion and return-role reconciliation is recoverable.

## Research workflow

```text
origin role
→ persist exact research record + active pointer
→ research/source verification
→ persist Status: complete
→ router
→ exact Return target
→ durable reconciliation
→ Status: consumed + clear active pointer
```

Research itself does not silently accept an option or choose a different Return target from chat narrative. A policy-specific Return target whose explicit role is to classify an evidence-dependent continuation may durably refine `Return target` to the exact final owning role/subject after classification; keep `Status: complete` and the owning pointer until that final target durably consumes the findings.

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
- persist findings/evidence and set the exact research record to `Status: complete`;
- preserve its active pointer until the recorded Return target has durably reconciled the result;
- return to the policy router;
- route to the record's exact current Return target; if that target is an authorized continuation classifier, it may durably refine the target as described above, but Research itself may not; Project Definition is legal only when the selected policy's entry conditions for Definition are satisfied;
- if research was entered from exploratory Brainstorming and that policy requires explicit user phase promotion, research completion does **not** count as that promotion;
- Definition promotes verified constraints to `requirements/` and explicit accepted choices to `decisions/` with provenance;
- after the target role persists that reconciliation, set the research record to `consumed` and clear the owning pointer (the pre-execution PROJECT pointer or the selected policy's execution-state pointer).

Implementation-time facts discovered for already-approved work may still flow to the current Task Card/OpenSpec/evidence as appropriate without redefining product intent.

If research evidence contradicts already accepted authority during active work, route to strategic resolution rather than silently rewriting downstream contracts.
