# ChatGPT start prompt

Use this in normal ChatGPT chat. ChatGPT Work is not part of Project Workflow.

## Existing project

```text
Użyj mojego Project Workflow z elmakus/chatgpt-codex-project-workflow.
Repo projektu: <owner/repo>.
Kontynuujemy <phase albo krótki cel>.
```

ChatGPT should:
1. read current workflow `main`, starting with `CHATGPT.md`;
2. read project root `PROJECT.md`;
3. determine phase and `execution_policy`;
4. apply progressive disclosure without semantic loss: resolve the exact applicable authority slice rather than replacing richer durable authority with a summary;
5. treat accepted durable repository knowledge as authority over stale chat memory;
6. when implementation state exists, read Task Board as sole live execution-state authority, including any pending/in-progress review gate;
7. persist accepted state when current GitHub/project capabilities allow it;
8. route execution by policy:
   - `chatgpt_only` → execute in ChatGPT; no Capability Gate and no capability preflight/inventory;
   - `codex_only` → prepare/hand off to Codex or recover Codex stream; no Capability Gate and no capability preflight/inventory;
   - `mixed` → run Capability Gate before new assignment.

Under fixed policy, run state/contract Refresh Gate and attempt the work directly. When predecessor evidence satisfies a recorded JIT trigger, the execution orchestrator may perform L2 refinement and create/revise not-yet-started cards without returning to the original strategic planner. If a concrete required operation cannot proceed, persist/report the runtime blocker rather than speculating before execution.

Under `chatgpt_only`, if this chat implemented the subject and REQUIRED/RECOMMENDED independent review becomes due, persist exact `review_subject`/`review_state: pending`, stop, and instruct the user to open a fresh normal ChatGPT chat for review. In that same response, include a minimal fenced copy-paste `NEW CHAT START PROMPT` containing project repo, continuation target and durable pointer only; do not duplicate durable state. A fresh review chat may continue later deterministic work after GREEN. Outside this independence boundary, a fresh chat is optional context hygiene, not a workflow gate; any such recommendation must also include its ready-to-copy start prompt.

If `mixed`, hand work to Codex only under Capability Gate and use `workflow/codex/HANDOFF.md` for minimal kickoff.

## New project

Create/choose project repository, initialize high-level `PROJECT.md` with explicit `execution_policy`, then create only phase-appropriate artifacts. Do not create Task Cards/OpenSpec merely because repo is new.
