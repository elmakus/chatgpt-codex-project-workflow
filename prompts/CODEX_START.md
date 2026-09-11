# Codex start prompt

```text
Use the current main of elmakus/chatgpt-codex-project-workflow.
Project repo: <owner/repo>.
Read PROJECT.md, determine the current execution context, load only the required workflow modules, and continue from durable GitHub state.
```

Codex then:

1. establishes repo root, branch, HEAD and working-tree state;
2. reads workflow `CHATGPT.md`/routing plus project `PROJECT.md`;
3. for execution, reads `workflow/EXECUTION.md` and its required contracts;
4. reads Task Board, latest cumulative handoff, current milestone and current/in-progress or first eligible READY card;
5. loads only relevant requirements/plan/OpenSpec/source;
6. runs the Refresh Gate before coding;
7. follows selective JIT OpenSpec;
8. implements/tests/verifies card by card;
9. persists result pointers/evidence and Git state;
10. uses the correlated `request_id` strategic protocol only for true strategic blockers;
11. performs integrated milestone acceptance and cumulative handoff;
12. when the owner's `codex_workflow` is installed/enabled, follows its installed instructions for internal worker/runtime orchestration rather than duplicating those mechanics from Project Workflow.

Repository state outranks stale conversation history. A local `current.md` is optional convenience only.

## Execution-prep handoff template

When ChatGPT has just completed execution prep, it should generate a project-specific prompt rather than making the user compose one. Prefer a short prompt shaped like:

```text
Use the current main of elmakus/chatgpt-codex-project-workflow.
Project repo: <owner/repo>.
Prepared milestone: <MXX>.
Required prior checkpoint: <checkpoint>.
Start from <repo-relative START_HERE and/or kickoff path>.

Recover the prepared Task Board/card state from the repository, perform the required Refresh Gate, and execute the milestone card-by-card according to dependencies. Continue automatically between deterministic READY cards without asking me which card is next.

Stop only for a genuine strategic blocker, an explicit user-authorization gate, a session handoff that you explicitly recommend for context reasons, or the final milestone checkpoint. Do not start the next milestone.
```

ChatGPT must accompany that prompt with an explicit `CODEX SESSION RECOMMENDATION: FRESH` or `CODEX SESSION RECOMMENDATION: CONTINUE EXISTING` according to `workflow/EXECUTION_PREP.md`.
