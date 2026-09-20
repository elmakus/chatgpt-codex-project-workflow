# Requirements — Codex-only continuous orchestration

Status: approved
Revision: R1
Date: 2026-09-20

## Goal

Under `execution_policy: codex_only`, Codex Main is the persistent project-workflow coordinator. After accepted product/system intent and planning authority exist, Main must continue deterministic authorized work across role and milestone boundaries without returning control to the user merely for coordinator context hygiene.

## Requirements

### COCO-R1 — No normal Context Health gate

The active `codex_only` lifecycle MUST NOT evaluate a Project Workflow Context Health/FRESH gate between deterministic obligations.

Context/session size, role changes, milestone transitions, authority-source changes, accumulated tool output, or the fact that a clean coordinator context might be preferable MUST NOT by themselves create a Project Workflow stop.

### COCO-R2 — Continuous deterministic continuation

Codex Main MUST continue through every deterministically authorized next obligation, including as applicable:

- Execution Prep and Card execution;
- Executor → Tester review cycles;
- bounded RED correction and re-review;
- milestone acceptance and Close;
- final-integration refresh/review;
- automatic transition to the next already-approved milestone.

A run may therefore legally progress through an approved sequence such as M01 → M02 → … → M15 without user interaction.

### COCO-R3 — Formal review is internal orchestration

REQUIRED/RECOMMENDED independent review under `codex_only` MUST remain a Codex-managed Executor/Tester separation boundary. A qualifying Tester verdict returns to Codex Main/router and MUST NOT itself require a normal-ChatGPT/user stop.

### COCO-R4 — Durable recovery replaces hygiene handoffs

Coordinator/session/runtime interruption or replacement MUST be recoverable from current workflow authority plus durable project repository state.

Project Workflow MAY define Recovery invariants needed to reconstruct the exact obligation, but MUST NOT schedule user-facing fresh-session hygiene handoffs as normal `codex_only` continuation.

Concrete worker/session/model/resume/replacement mechanics remain owned by `codex_workflow` or the active Codex runtime.

### COCO-R5 — Human stops remain narrow

Normal `codex_only` continuation stops only when the workflow reaches a genuine human/project boundary, including:

- unresolved user/product/strategic authority;
- an explicit user/deployment/live-write authorization gate;
- a concrete unremediable runtime/access/input blocker requiring user-provided input or access;
- end of approved scope with no deterministic next obligation.

The existing user-owned Brainstorming → Project Definition promotion boundary remains unchanged.

### COCO-R6 — No weakening of durable safety

Removing Context Health MUST NOT weaken:

- durable Task Board/manifest state ownership;
- exact recovery semantics;
- independent review requirements;
- accepted requirements/decisions;
- refresh/integration gates;
- external-write authorization boundaries.

### COCO-R7 — Regression coverage

Repository tests MUST prove that:

1. the active `codex_only` router does not load or invoke Context Health;
2. deterministic role transitions do not include a context-health decision;
3. the router/Close contract explicitly permits multi-milestone automatic continuation;
4. true human stop categories remain;
5. `chatgpt_only` Context Health behavior is unchanged.

## Non-goals

- Changing `chatgpt_only` session-hygiene semantics.
- Reimplementing `codex_workflow` worker/session lifecycle.
- Removing durable Recovery.
- Removing independent Tester review.
- Removing explicit user/product/deployment authorization gates.
- Changing the accepted execution policy of this repository.
