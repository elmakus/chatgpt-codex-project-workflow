# M01-T02 implementation evidence — 2026-09-20

## Subject

- Card: `M01-T02 — Wire binding lifecycle, recovery and generic dispatch gate`
- Execution-start base: `789ff7c60fa14c9cc525a6b9de9b9ac59a57d2f6`
- Exact implementation/review subject: `94eb7fd074052c5d4420b6edb2fe32ab2de1da13`

## Authority

- `implementation/workstreams/issue-codex-compaction-routing-recovery/cards/M01-T02.md`
- `requirements/CODEX_ORCHESTRATION_CONTEXT_RECOVERY.md` CCOR-R1…CCOR-R10
- `decisions/ADR_CODEX_ORCHESTRATION_POLICY_BINDING.md`
- `planning/CODEX_ORCHESTRATION_CONTEXT_RECOVERY_MASTER_PLAN.md#M01 — Token-light orchestration recovery boundary`
- accepted M01-T01 GREEN subject `319b034ebd3d5afd8643b755e00ab8d7987a0f34`

## Implemented

- Added one role-agnostic Codex-only pre-dispatch binding gate in `workflow/codex/CODEX_ORCHESTRATION.md`.
- New-workstream Intake establishes and reads back the opaque manifest binding before Intake completion or policy-dependent worker realization.
- Router conditionally restores the kernel boundary after compaction/context loss and treats the current-context latch as absent/uncertain.
- Recovery distinguishes pre-schema missing-block migration from already-present invalid binding, performs bounded re-bind recovery, and fails closed without native/internal fallback.
- Executor, bounded-parallel launch/retry/recovery, Tester, plan-review Tester and Investigator realization paths inherit/reference the shared gate.
- `EXECUTION_PREP.md` and `CLOSE.md` explicitly remain non-dispatch owners where appropriate.
- No concrete role→harness/model map was added and no `workflow/chatgpt_only/*` file changed.
- Updated the existing runtime-identity contract assertion only as required to reflect the T01-approved opaque policy/profile exception; focused CCOR-R10 regression additions remain assigned to M01-T03.
- Marked the M01-T02 OpenSpec checklist complete; M01-T03 tasks remain open.

## Verification on exact subject

Fresh detached worktree at `94eb7fd074052c5d4420b6edb2fe32ab2de1da13`:

- `python3 -m unittest tests.test_codex_only_branch_first_execution_state_contract tests.test_codex_only_branch_first_preexecution_contract tests.test_codex_only_continuous_orchestration_contract` → GREEN, 31/31.
- `python3 -m unittest discover -s tests` → GREEN, 78/78.
- Persisted-content T02 audit → GREEN:
  - generic pre-dispatch gate present;
  - Intake binding establishment present;
  - pre-schema-vs-invalid Recovery split present;
  - compaction/reconstruction latch rule present;
  - Execution/Review/Plan Review/Research hooks present;
  - no ChatGPT-only path changed;
  - no concrete GPT/Muse/native worker mapping introduced by the diff.
- `git diff --check 789ff7c60fa14c9cc525a6b9de9b9ac59a57d2f6..94eb7fd074052c5d4420b6edb2fe32ab2de1da13` → GREEN.

## Review boundary

M01-T02 is RECOMMENDED independent review. The exact subject above is frozen; implementation remains non-terminal until an independent reviewer records GREEN.
