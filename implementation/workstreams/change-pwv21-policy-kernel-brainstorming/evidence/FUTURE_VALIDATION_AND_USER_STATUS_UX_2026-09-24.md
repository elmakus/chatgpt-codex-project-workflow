# Future validation and user-facing review status ideas

Date: 2026-09-24
Class: non-authoritative future-work / UX evidence
Current workstream: `change-pwv21-policy-kernel-brainstorming`

This note records useful follow-up ideas without changing accepted Definition, Planning, Card authority, or current review state.

## 1. Post-RC Ralph-style adversarial soak

After PWv2.1 reaches a release-candidate state and completes its normal Card/Milestone/Final review obligations, run an additional adversarial soak inspired by the Ralph-loop pattern.

Intended shape:
- immutable PWv2.1 RC as the audit subject;
- many fresh cheap-model iterations rather than one accumulating reviewer context;
- each iteration receives a bounded adversarial angle or generated state/workstream scenario;
- iterations are audit/falsification-first and do not autonomously rewrite canonical authority;
- findings are durably recorded, deduplicated into material defect classes, and triaged by Main/strong review before any repair;
- repairs, if authorized, occur as normal bounded workflow work and receive fresh validation;
- useful corpus ideas include illegal transition attempts, stale subjects/pointers, Premium-B bypass attempts, oversized/micro Card topology, RED→repair→closure→rediscovery, repeated defect classes, advisory finding reconciliation, interrupted/recovered contexts, runtime-state leakage into Git authority, and documentation/validator/router disagreement;
- mutation-testing of a disposable copy of policy/validators may be used to test whether the regression corpus detects intentionally introduced semantic violations;
- termination should be based on bounded convergence criteria such as no genuinely new material defect class across an accepted number of successive fresh iterations, not on an agent deciding that the system is perfect.

This is a post-RC validation idea, not a prerequisite or authority change for current M02R execution.

## 2. User-facing review/convergence counters

At every user-facing handoff/status message produced after a review/repair cycle, show a compact semantic status block so the human can see that convergence rules are actually operating.

Recommended fields where applicable:
- `Card discovery epochs: X / 5`
- `Open material defect classes: N`
- per open class: `repair→closure rounds: Y / 3`
- `Current phase: discovery | repair | closure verification | fresh rediscovery`
- whether the latest RED introduced a genuinely new defect class or only recurrence/persistence of a known class.

The display must derive from durable semantic evidence rather than chat memory and must not create a second authority store.

## 3. Short ELI10 review summaries

User-facing RED/repair handoffs should include a short, non-technical explanation in addition to the exact durable locator:
- `Co było nie tak (ELI10):` 1–2 short sentences.
- `Jak to naprawiono (ELI10):` 1–2 short sentences.
- `Zakres naprawy:` explicitly say whether repair addressed the whole demonstrated defect class / causal siblings or only one literal example.
- `Co teraz sprawdza reviewer:` closure of known classes vs fresh discovery of unknown defects.

Detailed technical findings remain in durable review evidence; the human-facing message should not require reading those files to understand why another review round exists.

## Current motivating example — M02R-T01 R01

R01 discovered two material findings. The bounded repair evidence states that both demonstrated classes were addressed with regression coverage rather than literal one-line/example-only fixes:
- new PWv2.1 attempts can no longer bypass the explicit review-state contract by masquerading as legacy records;
- partial closure of only some findings can no longer advance to fresh rediscovery; cumulative closure must account for every frozen finding from the source discovery.

The accepted 5/4/3 discovery-epoch accounting and three-round same-class convergence breaker are not implemented by M02R-T01; that Card explicitly excludes counter/ceiling/convergence semantics. Therefore any current counter shown before the later BOOT-A convergence Card is implemented is explanatory/manual status, not candidate-enforced state.

Semantically, R01 is one fresh RED discovery event for M02R-T01 that exposed two material findings/classes. R02 is the next independent review of the repaired exact subject.
