# Semantic Audit — Branch-Aware Fresh ChatGPT Prompt

Date: 2026-09-18
Base: `main@e6bbb55cfedd7986607d37d0b25834c775b42cc2`
Audited branch: `docs/fresh-chat-branch-pointer`
Verdict: **GREEN**

## Checks

- Every canonical fresh-ChatGPT prompt includes:
  - project repo;
  - exact active project/implementation branch;
  - continuation target;
  - durable start pointer.
- Branch is included even when it is `main`.
- Branch is treated as a routing locator, not noisy telemetry.
- Exact HEAD/SHA remains omitted when recoverable from durable state.
- Mandatory independent-review and optional context-hygiene semantics are unchanged.
- Codex/worker/reviewer communication is untouched.

## Final assessment

**GREEN.** A fresh ChatGPT session can now recover the correct project state without guessing which branch contains the active milestone/card.
