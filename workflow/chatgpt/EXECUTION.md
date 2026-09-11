# ChatGPT Execution Adapter

Read this only when `workflow/chatgpt/CAPABILITY_GATE.md` selected `EXECUTE IN CHATGPT`.

ChatGPT executes the shared `workflow/EXECUTION.md` card loop using tools/plugins/connectors available in the current **normal ChatGPT chat**.

ChatGPT Work is not part of this workflow.

## Session capability rule

Tool availability is session-specific. Before a material operation, confirm that the current chat has the capability required by the Task Card and its evidence path. Do not substitute a product-level claim such as "ChatGPT can sometimes do X" for an actually available tool.

## Repository execution

When GitHub write capabilities exist, ChatGPT may create branches, modify files, commit, open/update PRs and inspect CI/diffs according to project branch policy. After material writes, read back relevant refs/files/status when that provides meaningful verification.

## Local execution

Use available Python/container/file-processing capabilities for tests, simulations, transformations and artifacts when they can validly exercise the target. An isolated ChatGPT runtime must not be misrepresented as the user's local/production runtime.

## Plugins/external systems

ChatGPT may perform external reads/writes through connected plugins/connectors when the card permits them. Follow provider-specific prerequisites and the shared `WRITE → READBACK → VERIFY` contract.

## Continuation and context hygiene

A routine GREEN card does not require switching to Codex. Continue deterministic READY work when current context remains reliable and policy permits it.

A fresh ChatGPT chat may be **recommended** at a clean milestone or after large context accumulation; this is context hygiene, not a new executor or authorization state. Recovery must use durable repository state.

## Missing capability discovered mid-card

Do not claim completion. Persist available evidence, mark the card blocked when its contract cannot be met, then re-run routing under `execution_policy`.
