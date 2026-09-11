# ChatGPT Capability Gate

## Purpose

Choose execution from actual task requirements and capabilities of the **current normal ChatGPT chat session**, while respecting user `execution_policy`.

Do not use ChatGPT Work. Do not maintain a global/static capability database. Capabilities may change between sessions as connectors/plugins/tools change.

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
- Codex has a required capability/environment unavailable to ChatGPT;
- the card requires a repo/runtime-heavy loop where Codex has a material practical advantage;
- the approved plan/card explicitly assigns the work to Codex.

Do not equate "technical" or "coding" with Codex.

If Codex capability is not actually known, do not invent it. A Codex handoff may require Codex to verify the named capability before mutating state and block durably if absent.

### BLOCKED

Use when neither available execution path can satisfy the card contract.

## Capability taxonomy for reasoning

Use only as a lightweight mental grouping, not a registry:
- Research;
- Repository;
- Execution/runtime;
- External systems;
- Artifact production;
- Operational assurance (write/readback/verification/rollback where needed).

Task Cards should name concrete explicit capabilities only when useful for routing/safety.
