# Shared Execution Core

This module defines executor-neutral project execution semantics. The selected executor must also read its thin adapter:

- ChatGPT → `workflow/chatgpt/EXECUTION.md`
- Codex → `workflow/codex/EXECUTION.md`

Read and obey `workflow/contracts/GITHUB_STATE.md`, `TASK_CARDS.md`, `OPENSPEC.md` and project `PROJECT.md` as applicable.

## Standard Task Card loop

1. Establish repository root, branch, exact HEAD and relevant working/runtime state.
2. Read Task Board and recover a valid `in_progress` card if one exists.
3. Otherwise select the first eligible `ready` card whose dependencies are `done`.
4. Record the selected `executor` when work actually starts; transition card to `in_progress` and milestone to `in_progress` if needed.
5. Run the Refresh Gate.
6. Create/reconcile OpenSpec just-in-time if required.
7. Execute only bounded card scope.
8. Run required tests/checks and verify acceptance.
9. For material external writes, apply `WRITE → READBACK → VERIFY` when readback provides meaningful independent confirmation.
10. Persist exact evidence/result pointers before marking the card `done`.
11. Commit/push durable state according to branch policy.
12. Unblock eligible dependent cards.
13. Continue deterministic READY work only when the selected executor, project policy and current session/context allow it.
14. After required cards are done, run integrated milestone acceptance.
15. RED → corrective work. GREEN → milestone close and cumulative handoff.

## Capability boundary

Starting a card does not authorize pretending a missing capability exists. If execution discovers that required tests, environment access, external write/readback or evidence cannot be produced:

- stop the affected work safely;
- persist available evidence;
- set the card `blocked` when execution cannot meet its contract;
- apply project `execution_policy` and the Capability Gate before any executor change.

An executor change is routing, not evidence that the original card succeeded.

## Refresh Gate

Before implementation compare at minimum:
- actual branch/HEAD and relevant current state;
- latest cumulative handoff;
- current milestone and Task Card;
- relevant requirements/accepted decisions/Master Plan;
- relevant OpenSpec;
- completed dependencies;
- actual code/runtime interfaces;
- required capabilities, tests and evidence path.

Implementation-detail drift inside approved contracts may be reconciled. Material behavior/architecture/requirement/external-contract/milestone-acceptance drift blocks the card and requires strategic resolution.

## External write contract

For a material mutation of GitHub, Liftosaur, APIs, calendars, Drive, configuration or other external systems:

```text
WRITE → READBACK → VERIFY EXPECTED STATE → EVIDENCE
```

Use readback when it materially validates persisted state. Do not apply it mechanically when no meaningful readback exists or the provider already returns sufficient authoritative immutable evidence. When independent readback is unavailable, record that limitation rather than inventing verification.

## Failure recovery

After interruption:
- recover existing `in_progress`/`blocked` card;
- inspect exact Git/runtime state;
- inspect Task Board, relevant OpenSpec, tests and result/evidence pointers;
- continue the same card with its recorded executor unless durable routing/capability state requires reassignment under project policy;
- never assume chat memory is the only recovery source.
