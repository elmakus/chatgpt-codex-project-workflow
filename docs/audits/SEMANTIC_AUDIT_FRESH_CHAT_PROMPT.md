# Semantic Audit — Automatic Fresh-ChatGPT Start Prompt

Date: 2026-09-18
Base: `main@87324ffb314735d3b22551535215913a3886ab31`
Audited implementation subject: `docs/fresh-chat-copy-paste-prompt`
Verdict: **GREEN**

## Scope

Audit the UX rule that any workflow response which requires or recommends a fresh normal ChatGPT chat must immediately provide a copy-paste-ready start prompt.

## Semantic checks

### GREEN — mandatory review handoff

- `chatgpt_only` REQUIRED/RECOMMENDED independent review still requires a fresh normal ChatGPT chat.
- The implementing chat still stops before issuing a verdict on its own subject.
- The same response must now also provide the new-chat prompt; this changes UX only, not the independence boundary.

### GREEN — optional context hygiene

- Fresh chat outside independent review remains optional context hygiene.
- No new mandatory session boundary, token threshold or milestone cadence was introduced.
- Any optional fresh-chat recommendation also includes the start prompt immediately.

### GREEN — durable-state discipline

The fresh-chat prompt is routing-only:
- project repository;
- exact continuation target;
- smallest durable start pointer;
- instruction to recover exact subject/authority/evidence/state from repository.

It does not duplicate:
- SHAs/review subject already stored in Task Board;
- test counts/results;
- evidence prose;
- changed-file lists/blobs;
- implementation summaries;
- branch/HEAD facts already recoverable from durable state.

### GREEN — no-loss recovery

- Fresh chat is told to recover exact state from repository and not treat the start prompt or previous chat as source of truth.
- Card/milestone/review-gate ID may be included as a lightweight routing hint.
- Non-durable user intent may be included only when repository state cannot recover it.

### GREEN — one-copy UX

- User should not need a follow-up request such as “daj prompt do nowego czatu.”
- The current response provides a fenced Markdown `NEW CHAT START PROMPT` suitable for one-click copy/paste.

### GREEN — execution/review semantics unchanged

- Task Board remains sole mutable execution-state authority.
- Authority Preservation remains unchanged.
- L1/L2/L3 delegated planning boundaries remain unchanged.
- `codex_workflow` integration boundary remains unchanged.
- Execution policies and Capability Gate semantics remain unchanged.

## Final assessment

**GREEN.** Fresh ChatGPT handoffs are now one-step for the user without turning the prompt into a duplicate handoff document or weakening durable repository recovery.
