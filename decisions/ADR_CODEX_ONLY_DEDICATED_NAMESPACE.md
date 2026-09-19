# ADR — Dedicated codex_only Policy Namespace

- Decision ID: `ADR-CODEX-NS-001`
- Date: `2026-09-19`
- Status: `accepted`
- Authority: `explicit user/product direction`
- Supersedes: `legacy codex_only/shared-stack architecture for this migrated policy`
- Related requirements: `requirements/CODEX_ONLY_POLICY.md (CO-REQ-001..006, CO-REQ-026..028)`
- Related milestone/card: `none until Planning`

## Context

Current `chatgpt_only` has a complete dedicated policy namespace. `codex_only` still depends on the older shared/legacy routing and execution stack. That stack mixes historical policy mechanisms and is not the desired base for the new Codex Main + `codex_workflow` model.

## Decision

Create a complete `workflow/codex_only/` namespace using current `workflow/chatgpt_only/` as the semantic lifecycle reference, not as a mechanical copy target.

Routing becomes:
- `chatgpt_only -> workflow/chatgpt_only/...`
- `codex_only -> workflow/codex_only/...`
- other not-yet-migrated accepted policies -> existing legacy route

Controlled duplication between ChatGPT-only and Codex-only is accepted. Do not create a new shared execution core merely to deduplicate them. Move a contract to `workflow/common/` only when it is genuinely policy-neutral.

Legacy `workflow/codex/*`, shared `workflow/EXECUTION.md`, `workflow/contracts/*` and legacy routing are compatibility/evidence inventory, not the architectural base.

## Rationale

The two fixed policies share project lifecycle concepts but differ materially in executor identity, review realization, concurrency and runtime recovery. Separate namespaces make those differences explicit and independently evolvable without accumulating conditional branches in one execution core.

## Alternatives considered

### Shared fixed-policy execution core with ChatGPT/Codex conditionals

Rejected. It recreates the coupling this migration is intended to remove.

### Aggressive extraction into workflow/common

Rejected unless each extracted contract is truly policy-neutral. Deduplication alone is not sufficient reason.

### Base new codex_only on legacy workflow/codex

Rejected. The legacy tree is useful evidence but does not represent the target architecture.

## Consequences

- More duplicated text/contracts may exist across policy namespaces.
- Migration must perform an explicit lifecycle-parity and legacy-property inventory.
- Future changes may intentionally diverge between policies.
- Other legacy policies remain unaffected until separately migrated.

## Required authoritative updates

- Requirements / Project Definition: `requirements/CODEX_ONLY_POLICY.md`
- Planning: map lifecycle parity, routing and compatibility work explicitly.
- Task Card/OpenSpec: JIT only where implementation changes behavior/contracts.
- PROJECT.md: point the active workstream to this accepted decision set while keeping project execution policy unchanged.

## Provenance

- Source: initiating feature request, 2026-09-19.
- Evidence: current `main` policy split and legacy branch inventory.
