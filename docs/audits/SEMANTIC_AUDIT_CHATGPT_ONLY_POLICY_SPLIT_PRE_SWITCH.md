# Semantic Audit — ChatGPT-only Policy Split PRE-SWITCH

Date: 2026-09-18
Base: `main@4476ed77b88adbed77702a193e447a0e520c5440`
Verdict: **GREEN TO SWITCH ROUTER**

## What was checked before activation

The migration first created new files beside legacy authority. No root/router behavior was changed during construction.

### Policy-neutral common

Created:
- `workflow/common/AUTHORITY.md`
- `workflow/common/BRAINSTORMING.md`
- `workflow/common/RESEARCH.md`
- `workflow/common/OPENSPEC.md`

Static scan found no other-policy, alternate-executor, concurrent-card, worker/lane routing semantics.

### Isolated chatgpt_only tree

Created:
- `ROUTER.md`
- `PLANNING.md`
- `EXECUTION_PREP.md`
- `TASK_CARDS.md`
- `TASK_CARD_TEMPLATE.md`
- `STATE.md`
- `EXECUTION.md`
- `REVIEW.md`
- `CLOSE.md`
- `RECOVERY.md`
- `REPOSITORY.md`

Static scan found:
- no alternate execution policy names;
- no alternate executor semantics;
- no project-card concurrency scheduling;
- no lane/worktree ownership;
- no pre-assignment capability router;
- no worker orchestration.

The only lexical occurrence of the other executor name is inside the immutable workflow repository name in the fresh-chat prompt; it is not execution semantics.

## Semantic coverage checks

All passed:

- exactly one READY Card selected at a time;
- execution prep continues directly into execution when legal;
- L1/L2 JIT refinement preserved;
- L3 strategic blocker preserved;
- Refresh Gate preserved;
- no fixed runtime capability inventory;
- external WRITE → READBACK → VERIFY → EVIDENCE preserved;
- selective OpenSpec preserved;
- implementing chat stops before its own REQUIRED/RECOMMENDED verdict;
- fresh independent review preserved;
- RED review same-turn bounded remediation preserved;
- corrected subject returns to `review_state: pending`;
- fresh re-review prompt preserved;
- GREEN review automatic continuation preserved;
- milestone integrated acceptance preserved;
- publication/PR verification preserved;
- next milestone automatic continuation preserved;
- recovery gives review state priority;
- Task Board remains sole mutable execution-state authority;
- more than one `in_progress` Card is invalid in this policy path;
- immutable review subject per attempt preserved;
- Task Card authority preservation preserved;
- recovery does not require prior chat.

## Context footprint

Prior normal ChatGPT execution core:
- `CHATGPT.md`
- `CONTEXT_ROUTING.md`
- `EXECUTION.md`
- `TASK_EXECUTION.md`
- `workflow/chatgpt/EXECUTION.md`

Total: approximately **3350 words** before project artifacts.

New isolated execution core before root-bootstrap rewrite:
- `common/AUTHORITY.md`
- `chatgpt_only/ROUTER.md`
- `chatgpt_only/EXECUTION.md`
- `chatgpt_only/STATE.md`

Total: approximately **2000 words** plus the small root bootstrap.

## Switch strategy

To support existing Project Instructions that already point to `workflow/CONTEXT_ROUTING.md`:

1. copy current pre-split router unchanged to `workflow/legacy/CONTEXT_ROUTING.md`;
2. replace `workflow/CONTEXT_ROUTING.md` with a small execution-policy dispatcher;
3. route `chatgpt_only` exclusively to `workflow/chatgpt_only/ROUTER.md`;
4. route other currently accepted policies to the preserved legacy router until their later migrations;
5. keep all legacy shared execution/contracts in place because other paths still depend on them;
6. run post-switch semantic and contamination audits before merge.

## Pre-switch verdict

**GREEN TO SWITCH ROUTER.** No legacy file should be deleted in this phase.
