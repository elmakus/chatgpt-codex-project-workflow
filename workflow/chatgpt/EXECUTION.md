# ChatGPT Execution Adapter

Read this only when `workflow/chatgpt/CAPABILITY_GATE.md` selected `EXECUTE IN CHATGPT`.

ChatGPT executes the shared `workflow/EXECUTION.md` execution-set loop using tools/plugins/connectors available in the current **normal ChatGPT chat**.

ChatGPT Work is not part of this workflow.

## Session capability rule

Tool availability is session-specific. Before a material operation, confirm that the current chat has the capability required by the Task Card and its evidence path. Do not substitute a product-level claim such as "ChatGPT can sometimes do X" for an actually available tool.

Bounded-parallel Task Board state does not require ChatGPT to manufacture concurrency it does not have. If the current chat cannot safely isolate/execute multiple mutable lanes, execute a compatible subset or one card while preserving the same project-level readiness/dependency semantics.

## Repository execution

When GitHub write capabilities exist, ChatGPT may create branches, modify files, commit, open/update PRs and inspect CI/diffs according to project branch policy. After material writes, read back relevant refs/files/status when that provides meaningful verification.

When executing multiple project-level cards in parallel, follow the shared coordinator/lane ownership contract: isolate mutable lanes, keep Task Board/global state coordinator-owned, integrate one lane at a time and verify post-integration state.

## Local execution

Use available Python/container/file-processing capabilities for tests, simulations, transformations and artifacts when they can validly exercise the target. An isolated ChatGPT runtime must not be misrepresented as the user's local/production runtime.

## Plugins/external systems

ChatGPT may perform external reads/writes through connected plugins/connectors when the card permits them. Follow provider-specific prerequisites and the shared `WRITE → READBACK → VERIFY` contract. Shared mutable external targets remain serialized when listed as exclusive resources.

## Continuation and context hygiene

A routine GREEN card does not require switching to Codex. Continue deterministic READY work or refill compatible bounded-parallel slots when current context/capabilities remain reliable and policy permits it.

A fresh ChatGPT chat may be **recommended** at a clean milestone or after large context accumulation; this is context hygiene, not a new executor or authorization state. Recovery must use durable repository state.

## Missing capability discovered mid-card

Do not claim completion. Persist available evidence and mark the affected card blocked when its contract cannot be met. Follow the shared runtime-blocker semantics; do not silently reroute an already-started card to another executor.
