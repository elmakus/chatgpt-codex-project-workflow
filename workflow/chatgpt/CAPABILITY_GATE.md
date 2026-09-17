# ChatGPT Capability Gate

## Scope

This gate is used **only** when project `execution_policy: mixed`.

Do not run it for `chatgpt_only` or `codex_only`; those policies already determine the executor.

## Purpose

Choose the executor for the next Task Card or compatible bounded-parallel ready set from actual task requirements and capabilities of the current normal ChatGPT session, while respecting the user's explicit `mixed` policy.

Do not use ChatGPT Work. Do not maintain a global/static capability database. Capabilities may change between sessions.

## Capability invariant

Project routing assumes:

`ChatGPT capabilities ⊆ Codex capabilities`

The gate therefore asks whether ChatGPT can correctly execute/verify the work **and** whether Codex has a material practical advantage or explicit assignment. It must never route from Codex to ChatGPT on the theory that ChatGPT has a required capability Codex lacks.

The gate is pre-assignment routing only. It is not a runtime fallback mechanism after a card starts.

## Gate

Before assigning a Task Card or compatible ready set under `mixed`:

1. Read Task Board state plus scope, acceptance, required tests/checks, evidence and external side effects for candidate cards.
2. Derive capabilities genuinely required to complete and verify them; merge explicit `required_capabilities` from contracts.
3. When bounded parallel, verify set is dependency-complete, within `parallel_card_limit`, explicitly `parallel_safe` and pairwise compatible by `write_scope`/`exclusive_resources`.
4. Inspect capabilities actually available in current ChatGPT session. Do not assume a product-wide capability is present in this session.
5. Confirm project policy is `mixed`. If it is fixed-policy, stop applying this gate and follow policy-fixed routing.
6. Route using outcomes below.

## Outcomes

### `EXECUTE IN CHATGPT`

Use when ChatGPT can correctly perform the selected work, satisfy required tests/checks/evidence/readback, safely handle intended lane isolation, and there is no explicit Codex assignment or material Codex practical advantage.

A bounded-parallel Task Board does not force ChatGPT to manufacture concurrency. ChatGPT may execute a smaller compatible subset or one READY card.

### `HANDOFF TO CODEX`

Use when at least one is true:
- current ChatGPT session cannot satisfy a required execution/environment path while Codex can;
- work requires a repo/runtime-heavy loop where Codex has a material practical advantage;
- useful bounded-parallel repo execution materially benefits from Codex orchestration;
- approved plan/card explicitly assigns Codex.

Do not equate “technical” or “coding” with Codex automatically.

If a Codex capability is not actually known before handoff, do not invent it. Codex verifies required capability before mutation. If absent, assigned work becomes `BLOCKED / USER ACTION REQUIRED`; it does not fall back to ChatGPT.

### `BLOCKED`

Use when no currently available permitted execution path can satisfy selected contract without user-provided capability/access or another explicit user decision.

## After assignment

Persist actual executor in Task Board. If a required capability is later discovered missing, follow runtime blocker semantics in `workflow/EXECUTION.md`; do not rerun the gate to change executor automatically.
