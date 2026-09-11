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

Before starting a Task Card:

1. Read scope, acceptance, required tests/checks, evidence and external side effects.
2. Derive the capabilities genuinely required to complete and verify the card. Merge any explicit `required_capabilities` from the card.
3. Inspect capabilities actually available in the current ChatGPT session. Do not assume a product-wide capability is present in this session.
4. Read `execution_policy` from project `PROJECT.md`.
5. Route using the rules below.

## `chatgpt_only`

### EXECUTE IN CHATGPT

Only when ChatGPT can:
- perform the work;
- run or otherwise satisfy every required test/check;
- obtain required evidence;
- perform required external readback/verification where applicable.

### BLOCKED

If any required capability/evidence path is unavailable. State the concrete missing capability. Do not route to Codex and do not change policy.

## `mixed`

### EXECUTE IN CHATGPT

Default when ChatGPT can correctly execute and verify the card and there is no approved explicit Codex assignment or material Codex practical advantage.

### HANDOFF TO CODEX

Use only when at least one is true:
- ChatGPT lacks a required capability/environment that the mixed policy allows Codex to satisfy;
- the card requires a repo/runtime-heavy loop where Codex has a material practical advantage;
- the approved plan/card explicitly assigns the work to Codex.

Do not equate "technical" or "coding" with Codex.

If Codex capability is not actually known before handoff, do not invent it. Codex verifies the named capability before mutation when necessary. If it is absent at runtime, the assigned Codex card becomes `BLOCKED / USER ACTION REQUIRED`; it does not fall back to ChatGPT.

### BLOCKED

Use when no currently available execution path can satisfy the card contract without user-provided capability/access or another explicit user decision.

## Capability taxonomy for reasoning

Use only as a lightweight mental grouping, not a registry:
- Research;
- Repository;
- Execution/runtime;
- External systems;
- Artifact production;
- Operational assurance (write/readback/verification/rollback where needed).

Task Cards should name concrete explicit capabilities only when useful for routing/safety.
