# Semantic Audit — Reviewer Auto-Remediation

Date: 2026-09-18
Base: `main@24464958df5aead53035134803bec8949e3675e7`
Audited branch subject: `fix/reviewer-auto-remediation@161cfce861ef4ebfa95d03640cfd8003ff9daffc`
Verdict: **GREEN**

## Scope

Audit the change that:
1. makes normal-ChatGPT human-facing output rules global rather than execution-only;
2. prevents a `chatgpt_only` reviewer from ending the user turn immediately after a deterministic RED verdict;
3. requires the same fresh reviewer chat to perform bounded remediation before replying;
4. preserves reviewer independence by stopping only after the corrected exact subject is frozen as a new pending review;
5. preserves branch-aware fresh-chat prompt behavior;
6. leaves Codex review/orchestration semantics unchanged.

## GREEN — global ChatGPT human control surface

`CHATGPT.md` now applies the human control surface to every normal ChatGPT route, including independent review.

Default user-facing output remains:
- what happened / what was found;
- what it means;
- what happens next / smallest user action.

Durable telemetry such as SHAs, branch/HEAD pointers, evidence paths, Task Board fields and long test inventories remains repository state unless materially needed or explicitly requested.

The duplicated executor-only human-output section was removed from `workflow/chatgpt/EXECUTION.md`.

## GREEN — RED is not an automatic user stop

For `chatgpt_only`, after a fresh reviewer persists a RED verdict, it must continue in the same chat turn when corrective work is:
- bounded;
- deterministic;
- authorized by durable project state;
- L1/L2 rather than L3 strategic change;
- free of explicit user/deployment/live-write/authorization gates;
- not blocked by a concrete runtime failure.

The reviewer must not emit a final user-facing response merely to say that remediation is next.

## GREEN — legal role transition after RED

The reviewer first completes the independent review of the old exact subject and persists RED evidence/state.

It then leaves review-only mode and enters the normal ChatGPT execution route for the corrective subject.

This is legal because independence applies to the subject being reviewed, not permanently to the chat role.

## GREEN — no self-review of remediation

After corrective implementation:
1. required checks run;
2. corrected durable result is persisted;
3. the new exact remediation subject is frozen;
4. review state returns to `pending`;
5. the chat stops before issuing a verdict on the subject it just implemented.

A fresh ChatGPT chat is therefore still required for independent re-review.

## GREEN — prompt is emitted at the actual stop

The final response after successful remediation must include the ready-to-copy branch-aware `NEW CHAT START PROMPT`.

Prompt semantics remain routing-only:
- project repo;
- exact active branch;
- pending independent re-review target;
- durable Task Board pointer;
- repository recovery instruction.

Durable SHAs/test telemetry/evidence prose are not duplicated.

## GREEN — real blockers still stop

The reviewer stops before remediation only when corrective work requires:
- L3 strategic/product/architecture decision;
- explicit user/deployment/live-write/authorization action;
- a concrete runtime blocker;
- scope that cannot yet be safely bounded.

This preserves user authority and runtime safety.

## GREEN — durable-state contract aligned

`workflow/contracts/GITHUB_STATE.md` now records the same automatic corrective transition, so review routing and durable state semantics do not disagree.

## GREEN — Codex behavior unchanged

Automated semantic checks confirmed that:
- `workflow/codex/EXECUTION.md` still owns codex-only independent-review execution;
- `workflow/codex/CODEX_ORCHESTRATION.md` still owns independent reviewer-worker orchestration;
- no Codex user-handoff requirement was introduced;
- no Codex continuous execution/worker semantics were removed.

## Final assessment

**GREEN.** Under `chatgpt_only`, deterministic RED remediation no longer forces the user to send “continue”. The same fresh reviewer chat performs the bounded correction, then stops only at the new independent-review boundary with a ready-to-copy fresh-chat prompt. Reviewer independence and Codex semantics remain intact.
