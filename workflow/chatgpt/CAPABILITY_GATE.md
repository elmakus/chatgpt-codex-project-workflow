# ChatGPT Capability Gate

## Purpose

Choose execution from actual task requirements and capabilities of the **current normal ChatGPT chat session**, while respecting user `execution_policy`.

Do not use ChatGPT Work. Do not maintain a global/static capability database. Capabilities may change between sessions as connectors/plugins/tools change.

## Capability invariant

Project routing assumes:

`ChatGPT capabilities ⊆ Codex capabilities`

The executor distinction is therefore not that ChatGPT can possess a required capability unavailable to Codex. This gate is a **pre-assignment routing mechanism** for normal ChatGPT. It is not a runtime fallback mechanism after a card has started.

If Codex later discovers that a required capability is missing, do not route the card back to ChatGPT. Persist the blocker, report `USER ACTION REQUIRED`, obtain the missing capability from the user, and resume the same Codex card.

## Gate

Before starting a Task Card or compatible bounded-parallel ready set:

1. Read scope, acceptance, required tests/checks, evidence and external side effects for every candidate card.
2. Derive the capabilities genuinely required to complete and verify each card. Merge any explicit `required_capabilities` from the cards.
3. When Task Board uses `bounded_parallel`, verify the proposed set is dependency-complete, within `parallel_card_limit`, explicitly `parallel_safe` and pairwise compatible by `write_scope`/`exclusive_resources`. Executor routing must not manufacture project-level parallel safety.
4. Inspect capabilities actually available in the current ChatGPT session. Do not assume a product-wide capability is present in this session.
5. Read `execution_policy` from project `PROJECT.md`.
6. Route using the rules below.

## `chatgpt_only`

### EXECUTE IN CHATGPT

Only when ChatGPT can:
- perform the work for the selected card/set;
- safely isolate any concurrent mutable lanes it actually intends to run;
- run or otherwise satisfy every required test/check;
- obtain required evidence;
- perform required external readback/verification where applicable.

A bounded-parallel Task Board does not force actual concurrency. ChatGPT may execute a smaller compatible subset or one READY card when its current tool/runtime surface cannot safely run multiple mutable lanes.

### BLOCKED

If any required capability/evidence path for the selected work is unavailable. State the concrete missing capability. Do not route to Codex and do not change policy.

## `mixed`

### EXECUTE IN CHATGPT

Default when ChatGPT can correctly execute and verify the selected card/set and there is no approved explicit Codex assignment or material Codex practical advantage.

### HANDOFF TO CODEX

Use only when at least one is true:
- ChatGPT lacks a required capability/environment that the mixed policy allows Codex to satisfy;
- the card/set requires a repo/runtime-heavy loop where Codex has a material practical advantage;
- useful bounded-parallel repo execution materially benefits from Codex orchestration;
- the approved plan/card explicitly assigns the work to Codex.

Do not equate "technical" or "coding" with Codex.

If Codex capability is not actually known before handoff, do not invent it. Codex verifies the named capability before mutation when necessary. If it is absent at runtime, the assigned Codex card becomes `BLOCKED / USER ACTION REQUIRED`; it does not fall back to ChatGPT.

### BLOCKED

Use when no currently available execution path can satisfy the selected card/set contract without user-provided capability/access or another explicit user decision.

## Capability taxonomy for reasoning

Use only as a lightweight mental grouping, not a registry:
- Research;
- Repository;
- Execution/runtime;
- External systems;
- Artifact production;
- Operational assurance (write/readback/verification/rollback where needed).

Task Cards should name concrete explicit capabilities only when useful for routing/safety.
