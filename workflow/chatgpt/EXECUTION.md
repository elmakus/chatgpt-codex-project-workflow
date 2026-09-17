# ChatGPT Execution Adapter

Read this when:
- project policy is `chatgpt_only`; or
- project policy is `mixed` and Capability Gate selected `EXECUTE IN CHATGPT`; or
- recovering already ChatGPT-assigned in-progress work.

ChatGPT executes the shared `workflow/EXECUTION.md` loop using tools/plugins/connectors available in the current **normal ChatGPT chat**.

ChatGPT Work is not part of this workflow.

## Session capability rule

Tool availability is session-specific. Before a material operation, confirm current chat has capability required by Task Card contract/evidence path. A fixed `chatgpt_only` policy removes routing overhead; it does **not** authorize pretending unavailable capability exists.

Bounded-parallel Task Board state does not require ChatGPT to manufacture concurrency it does not have. Execute a compatible subset or one card when needed.

## Repository execution

When GitHub write capabilities exist, ChatGPT may create branches, modify files, commit, open/update PRs and inspect CI/diffs according to branch policy. After material writes, read back relevant refs/files/status when meaningful.

When executing multiple project-level cards in parallel, isolate mutable lanes, keep Task Board/global state coordinator-owned, integrate one lane at a time and verify post-integration state.

## Local execution

Use available Python/container/file-processing capabilities for tests, simulations, transformations and artifacts when they validly exercise target. Do not misrepresent isolated ChatGPT runtime as user's local/production runtime.

## Plugins/external systems

ChatGPT may perform external reads/writes through connected plugins/connectors when contract permits. Follow provider prerequisites and shared `WRITE → READBACK → VERIFY` contract. Shared mutable external targets remain serialized.

## Continuation

Under `chatgpt_only`, continue deterministic READY work and cross GREEN milestone boundaries automatically when next milestone is already approved and shared continuation conditions hold. Do not run Capability Gate at each card or milestone.

Under `mixed`, a new assignment is routed through Capability Gate as required by shared execution semantics.

A fresh ChatGPT chat may be recommended for context hygiene at clean boundaries; this is not a new authorization state.

## Missing capability discovered mid-card

Do not claim completion. Persist evidence and mark affected Task Board card blocked when contract cannot be met. Under `chatgpt_only`, remain blocked until capability is supplied or user explicitly changes policy. Under `mixed`, do not silently reroute an already-started card.
