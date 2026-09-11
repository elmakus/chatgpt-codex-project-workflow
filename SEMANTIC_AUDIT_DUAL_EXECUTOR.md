# Semantic Audit — Dual-Executor Project Workflow

**Status:** GREEN  
**Audit date:** 2026-09-11  
**Baseline `main`:** `3374232680a9b8a3de440e08257e003bdd706cee` (v3.0.3 behavior)  
**Audited feature state before this audit-only commit:** `e53ee5995102987d1ef0ce8f7b440955c9db3883`

## 1. Audit goal

Verify that the dual-executor redesign changes the executor/routing model without losing the durable execution semantics preserved by v3, while keeping selective loading and avoiding new orchestration machinery.

The operating surface is intentionally limited to **normal ChatGPT chat + Codex**. ChatGPT Work is not an executor, routing target or dependency.

## 2. Architecture checks

### A. One workflow repository — PASS

Project Workflow remains one repository. No ChatGPT-only workflow repo, shared-core repo or capability repo was introduced.

### B. One project repository — PASS

`PROJECT_REPOSITORY.md` preserves ONE PROJECT = ONE REPOSITORY, durable project truth and the existing knowledge-state separation.

### C. Execution policy — PASS

Root `PROJECT.md` has exactly two execution policies:

- `chatgpt_only`;
- `mixed`.

New projects default to `chatgpt_only`. Changing to `mixed` requires explicit user decision. Missing legacy policy is configuration to resolve, not a third mode.

### D. Capability Gate — PASS

`workflow/chatgpt/CAPABILITY_GATE.md` has exactly the intended routing outcomes:

- `EXECUTE IN CHATGPT`;
- `HANDOFF TO CODEX` (mixed only);
- `BLOCKED`.

No executor score, capability database, preferred-executor weight, agent graph or scheduler was added.

### E. ChatGPT is a full executor — PASS

The ChatGPT adapter permits repository work, local Python/container/file execution and connected external-system operations when the current normal ChatGPT chat actually exposes the required capability and can obtain required verification/evidence.

Platform-wide capabilities are not treated as proof of current-session capability.

### F. Codex remains specialized — PASS

Codex is routed work only in `mixed` when it has a required capability/environment, material repo/runtime advantage or an approved explicit assignment. "Technical"/"coding" does not automatically mean Codex.

## 3. Progressive disclosure checks

### ChatGPT path — PASS

`CHATGPT.md → PROJECT.md → CONTEXT_ROUTING → shared phase module → ChatGPT-specific module only when applicable`.

ChatGPT reads `workflow/codex/HANDOFF.md` only when preparing/interpreting a Codex handoff.

### Codex path — PASS

`CODEX_START → PROJECT.md → CONTEXT_ROUTING → shared execution/contracts → workflow/codex/*`.

The Codex start path explicitly forbids automatic loading of `CHATGPT.md` and `workflow/chatgpt/*`.

### Shared execution core — PASS

There is one shared `workflow/EXECUTION.md`; ChatGPT and Codex use thin adapters. The workflow does not duplicate the full card loop for both executors.

## 4. v3 semantic preservation checks

The redesign preserves the following v3 contracts:

- card states `planned | ready | in_progress | blocked | done | superseded` — PASS;
- separate decision state — PASS;
- milestone lifecycle and terminal GREEN state — PASS;
- Task Board as live execution index — PASS;
- `result_commit`, `result_pr`, `evidence`, tests summary before `done` — PASS;
- exact Definition of Done coupling — PASS;
- dependency blocking and deterministic READY progression — PASS;
- Refresh Gate before implementation — PASS;
- just-in-time selective OpenSpec — PASS;
- integrated milestone acceptance after cards are done — PASS;
- corrective work on RED — PASS;
- exact `implementation_head`, checkpoint, acceptance evidence and cumulative handoff on GREEN — PASS;
- failure recovery from durable repository state — PASS;
- optional local `current.md` remains non-authoritative — PASS;
- no mid-milestone repository-topology migration — PASS;
- Codex strategic correlation via `request_id` + `DECISION FOR CODEX:` retained when that channel is used — PASS;
- `codex_workflow` remains authority only for internal Codex runtime orchestration — PASS;
- no shadow task database/Jira clone/generic DAG workflow engine — PASS.

## 5. New execution semantics checks

### Capability requirements — PASS

Task Cards support optional explicit `required_capabilities` only for external/unusual/high-risk/routing-significant cases. Ordinary repository capabilities remain inferred.

### Executor provenance — PASS

Task Card and Task Board record `executor: chatgpt | codex` when execution starts. This supports recovery/provenance and is not a routing score.

### External write contract — PASS

Shared execution defines:

`WRITE → READBACK → VERIFY EXPECTED STATE → EVIDENCE`

only when readback gives meaningful validation. The contract explicitly avoids mechanical fake readback when no useful independent read exists.

### Independent review — PASS

Fresh normal ChatGPT review is:

- REQUIRED for high-risk work;
- RECOMMENDED for major architecture/refactors/complex state machines;
- OPTIONAL by default for low-risk work.

No permanent review-agent role or review-after-every-card requirement exists.

### Competing paths — PASS

Path A / Path B / Hybrid is an optional branch/evidence pattern starting from a stable checkpoint. It does not introduce new lifecycle states or force experimental code merges.

## 6. Execution Prep checks

Execution Prep now prepares branch policy, Task Cards, acceptance/tests, external readback needs, review level and material capability requirements, then runs Capability Gate.

Its terminal routing state is one of:

- `EXECUTOR: CHATGPT`;
- `EXECUTOR: CODEX`;
- `EXECUTOR: BLOCKED`.

A Codex prompt is generated only for the Codex outcome. `chatgpt_only` cannot route to Codex.

Session recommendations are context-hygiene guidance, not authorization gates.

## 7. Migration safety — PASS

`MIGRATION_DUAL_EXECUTOR.md` handles existing projects and the special case of active execution prepared under v3.0.3.

Already-started bounded work may temporarily stay on the frozen pre-cutover workflow revision and adopt `execution_policy` at the next clean GREEN boundary, preventing a silent mid-flight contract change.

Historical evidence/handoffs are not rewritten simply to replace old Codex-specific wording.

## 8. ChatGPT Work exclusion — PASS

Current normative entrypoints, router, Capability Gate, ChatGPT adapter, project contract, migration guide and Project Instructions all state that Project Workflow uses normal ChatGPT chat + Codex only and does not route through ChatGPT Work.

## 9. Context-cost assessment — PASS

The old Codex path loaded ChatGPT router/responsibility material. The new Codex path excludes `CHATGPT.md`, `workflow/chatgpt/CAPABILITY_GATE.md` and `workflow/chatgpt/EXECUTION.md`.

Adding ChatGPT execution therefore does not add ChatGPT-specific daily context cost to Codex; the executor split reduces cross-executor context leakage.

## 10. Validation scenarios

### Fitness / Liftosaur — PASS

The model supports ChatGPT-owned research/design/GitHub/Liftosaur execution when current chat has plugin write + playground + readback capabilities, while still allowing Codex for repo/runtime-heavy work. External deployment requires saved-state readback/evidence and can carry high-risk independent review/protection boundaries.

### Homelab — PASS

A `chatgpt_only` project blocks when current ChatGPT lacks required Home Assistant/Unraid/Node-RED runtime capability. In `mixed`, the same card can route to Codex only when its configured environment actually exposes the required MCP/runtime capability.

### Pure software repo — PASS

Bounded GitHub/code work can remain in ChatGPT when executable/verifiable there; repo-wide refactors and long local code→test→fix loops can route to Codex for a concrete practical/runtime advantage without moving research/architecture/review out of ChatGPT.

## 11. File/path integrity

The active shared contracts directory contains only executor-neutral contracts:

- `GITHUB_STATE.md`;
- `OPENSPEC.md`;
- `PROJECT_REPOSITORY.md`;
- `TASK_CARDS.md`.

The old monolithic `workflow/contracts/CHATGPT_CODEX.md` was removed and its surviving semantics were split by actual consumer.

Old `workflow/contracts/CODEX_ORCHESTRATION.md` moved to `workflow/codex/CODEX_ORCHESTRATION.md`.

References to removed paths in the feature diff are historical deletions or explicit migration instructions, not live normative routing links.

## 12. Anti-overengineering result

Not introduced:

- executor scoring;
- capability registry/database;
- project tool inventory;
- preferred-executor field;
- third execution policy;
- ChatGPT Work routing;
- shared-core third repository;
- mandatory capability declarations on trivial cards;
- mandatory independent review for every card;
- agent graph;
- generic executor scheduler;
- new lifecycle states for research branches.

## 13. Conclusion

**GREEN.** The branch implements the target dual-executor architecture while preserving the important v3 execution-state/evidence/recovery semantics and reducing cross-executor context loading.

No merge to `main` is part of this audit.
