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
12. uses event-driven bounded multi-agent coordination rather than routine polling.

Repository state outranks stale conversation history. A local `current.md` is optional convenience only.
