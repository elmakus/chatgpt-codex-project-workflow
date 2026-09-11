# Execution Preparation

Execution preparation converts an approved plan into a bounded, executable package without prematurely freezing code-dependent detail.

## Preconditions

Before executable cards exist:
- authoritative requirements are identifiable;
- accepted architecture decisions are recorded;
- current Master Plan/milestone is approved;
- unresolved product questions that would invalidate implementation are resolved or explicitly blocking;
- project `execution_policy` is set to `chatgpt_only` or `mixed`.

## Steps

1. Inspect current project/source state.
2. Define or refresh the milestone and branch policy.
3. Decompose work into bounded Task Cards.
4. Record dependencies, priority, complexity, phase and expected code locations.
5. Define acceptance and required tests/checks.
6. Identify external side effects and any required readback/verification.
7. Add explicit `required_capabilities` only for unusual, external, high-risk or routing-significant cards; infer ordinary repo capabilities.
8. Classify independent review as REQUIRED, RECOMMENDED or OPTIONAL where material.
9. Mark OpenSpec candidates just-in-time according to `workflow/contracts/OPENSPEC.md`.
10. Initialize/update `implementation/TASK_BOARD.yaml` and confirm requirement coverage.
11. Audit sizing, dependencies, side effects, idempotency, security and migration.
12. Set a card `ready` only when dependencies/prerequisites allow execution.
13. For the next executable card, run `workflow/chatgpt/CAPABILITY_GATE.md`.

## Execution result

Execution prep does **not** always end with a Codex prompt.

It ends with exactly one routing outcome for the next executable Task Card:

### `EXECUTOR: CHATGPT`

Use when the current ChatGPT session has the required capabilities, can run the required tests/checks and can obtain required evidence/readback.

ChatGPT may continue in the current chat or recommend a fresh ChatGPT chat for context hygiene. No Codex prompt is generated.

### `EXECUTOR: CODEX`

Allowed only when `execution_policy: mixed` and Codex has a concrete required capability/environment, a material repo/runtime advantage, or an approved explicit assignment.

Generate a short Codex kickoff according to `workflow/codex/HANDOFF.md`. Rely on durable project state rather than restating the whole project.

### `EXECUTOR: BLOCKED`

Use when the required capability/evidence path is unavailable under current policy. Under `chatgpt_only`, missing ChatGPT capability blocks execution; do not silently route to Codex or change policy.

## Required user-visible completion

A completed prep reports:

```text
EXECUTION PREP COMPLETE:
Milestone: <MXX>
Task Card: <MXX-TYY>
Required prior checkpoint: <sha/tag>
Durable start pointer: <path>
Execution policy: <chatgpt_only|mixed>
Required capabilities: <explicit or inferred summary>
EXECUTOR: <CHATGPT|CODEX|BLOCKED>
```

If `CODEX`, include the smallest copy-paste kickoff and session recommendation. If `CHATGPT`, state whether the current chat can continue or a fresh ChatGPT chat is recommended only for context hygiene. If `BLOCKED`, state the exact missing capability/authorization/evidence path.
