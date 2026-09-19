# Codex-only State Contract

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **adapt**.

## Project-state ownership

The canonical Task Board selected by the current project/workstream context is the sole mutable Card/milestone execution-state record. A branch-isolated board is trusted only after manifest identity/branch binding succeeds.

## Foundation fields

Project state may record:
- milestone/Card lifecycle and dependencies;
- exact project role/lane ownership needed for recovery;
- branch/integration/result/evidence pointers;
- exact review requirement/state/subject/evidence;
- project-level Research routing;
- acceptance/checkpoint/handoff pointers.

Runtime worker identity and lifecycle are not Project Workflow state.

## Review invariant

One review attempt covers one immutable exact subject. RED evidence is preserved; materially changed implementation creates a new attempt.

## Execution invariant

Serial execution remains valid by default. Codex Main is the only writer of shared Task Board/integration state.

M02 finalizes formal-review/provenance/recovery fields. M03 adds the exact bounded compatible-ready-set and lane metadata needed for opt-in parallel Cards without creating a global scheduler.
