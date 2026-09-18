# ChatGPT-only Task Card Contract

## Meaning

A Task Card is one bounded project work-package contract executed by normal ChatGPT.

It defines stable authority, scope, acceptance and tests. It is not live execution state.

Mutable status, branch/result pointers and Card/milestone review state live only in the selected canonical Task Board resolved by `workflow/chatgpt_only/WORKSTREAMS.md`; the legacy/default path remains `implementation/TASK_BOARD.yaml`.

Use `workflow/chatgpt_only/TASK_CARD_TEMPLATE.md`.

## Required contract fields

Each Card defines:
- ID/title/milestone;
- dependencies;
- exact durable authority slice;
- outcome;
- included/excluded scope;
- acceptance criteria;
- required tests/checks;
- material external-write/readback obligations;
- explicit authorization gates when applicable;
- independent-review requirement when material.

Priority, complexity, phase and code-location hints are optional.

## Authority preservation

The authority slice should identify as precisely as practical:
- requirements;
- accepted decisions;
- Master Plan/milestone sections;
- relevant OpenSpec;
- accepted dependency results.

Preserve every applicable implementation-shaping constraint, including when relevant:
- invariants;
- accepted behavior/architecture choices;
- failure semantics;
- compatibility requirements;
- rejected paths/exclusions;
- security/migration/data-integrity boundaries;
- external-write boundaries;
- acceptance/test obligations;
- rationale whose omission could reasonably cause a different implementation.

A summary never outranks exact durable authority.

## Deferred Card creation

A future Card does not need to exist before its scope becomes knowable.

When real scope materially depends on predecessor evidence:
- keep the JIT trigger in accepted durable authority;
- do not create a vague placeholder;
- after predecessor evidence exists, create the real bounded Card;
- bind that accepted predecessor result into its authority slice;
- reconcile Task Board before execution.

Only not-yet-started work may be reshaped this way.

## Readiness

A Card may become `ready` only when:
- dependencies are complete;
- required authoritative inputs exist;
- acceptance is testable;
- no unresolved strategic blocker exists;
- no explicit authorization gate prevents start.

Runtime start semantics live in `workflow/chatgpt_only/EXECUTION.md` and `STATE.md`.

## Independent review

Use exactly one value:
- `REQUIRED` for high-risk work;
- `RECOMMENDED` when an independent review gate is useful but not intrinsically high-risk;
- `none` when no independent review gate is part of the Card contract.

Both REQUIRED and RECOMMENDED are real independent-review gates once recorded on the Card.

For `none`, do not create review state merely as a routine quality check.

If the user later explicitly requests independent review for a `none` Card, update the durable Card/review requirement to `RECOMMENDED` before activating the gate.

For REQUIRED/RECOMMENDED review, the chat that implemented the exact subject cannot issue its independent verdict.

## Near-term versus distant Cards

Near-term Cards may contain detailed implementation expectations.

Distant work stays functionally precise without freezing interfaces that are not yet knowable. Prefer an exact JIT trigger over speculative implementation detail.

## Scope discipline

Do not hide unrelated cleanup/architecture changes inside a Card.

If execution discovers a necessary adjacent change outside current authority:
- add bounded corrective/JIT work when it remains L1/L2;
- otherwise stop affected work and return to the router for Planning / Project Definition / Research classification; user stop only when unresolved user/product authority or another explicit real gate is reached.
