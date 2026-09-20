# ChatGPT-only Context Health Gate

This module protects execution quality when one normal ChatGPT chat has accumulated enough stale or irrelevant context that a clean repository-backed restart is safer than continuing.

It is **not** a token counter, task counter, timer or milestone cadence.

## When to evaluate

Evaluate context health only at a safe durable boundary:

- the current role/obligation has finished;
- all material results/evidence/state changes are persisted;
- Task Board, when implementation state exists, is coherent;
- there is no half-completed external mutation or other operation that requires same-session continuity;
- the exact next legal obligation is recoverable from durable repository state.

Never interrupt an active Card, active review inspection, in-flight external write/readback sequence or unresolved state transition merely for context hygiene.

If any real stop already owns the boundary — required fresh-review handoff, unresolved strategic/product decision requiring user authority, explicit authorization, concrete runtime/access/input blocker, or end of approved scope — use that boundary instead. Do not create a separate hygiene handoff.

## Decision

Choose exactly one:

```text
CONTEXT_HEALTH: CONTINUE
CONTEXT_HEALTH: FRESH
```

### CONTINUE

Continue in the same chat when durable authority can be followed without material ambiguity and there is no affirmative evidence that the accumulated transcript is materially harmful to the next obligation.

Routine role completion, Card completion, milestone completion, phase change, workstream change or authority-area change alone is not a reason for FRESH.

If the exact next obligation and its authority are deterministically recoverable from durable state and there is no affirmative evidence that the accumulated transcript is harmful, choose CONTINUE.

### FRESH

Choose FRESH only when continuing with the accumulated conversation creates a concrete material risk of confusion, stale-state carryover or authority omission for the next obligation.

Strong signals — any one may justify FRESH:
- the chat contains materially superseded/contradictory state that could plausibly influence the next obligation;
- the agent is having difficulty distinguishing current durable truth from earlier transient discussion/tool output;
- correct continuation would require mentally reconstructing substantial prior state that is already cleaner and more authoritative in the repository.

Soft signals — use a meaningful combination rather than any one weak signal, and require that the accumulated transcript itself is contributing to the risk:
- prior roles or phases left substantial transient discussion that is now stale enough to plausibly interfere with current authority;
- large prior tool outputs, diffs, diagnostics or failed paths now dominate context and materially obstruct the next obligation;
- the next obligation is complex and existing stale/irrelevant transcript content concretely increases the risk of mixing old assumptions with current authority.

The following are not context-health signals by themselves:
- moving to another role, milestone, phase, workstream or authority/source area;
- completion of the obligation named by a fresh-session handoff;
- the fact that a clean chat could also perform the next obligation;
- elapsed time, turn count, Card count, milestone count or other fixed cadence.

A workflow-topology change may matter only when it has actually left accumulated context that now creates material risk. The topology change itself is not evidence of degradation.

#### Fresh-handoff anti-bounce

A chat that was itself started from a context-hygiene fresh-session handoff MUST NOT select FRESH at the next durable transition merely because the recovered obligation completed or the next deterministic obligation uses a different role, milestone, phase, workstream or authority area.

Another FRESH result requires new concrete context degradation accumulated in the current chat after recovery. If the recovered work is durably persisted, the next obligation is deterministically recoverable from repository state, and no new harmful-context evidence exists, choose CONTINUE.

Do not invent a fixed numeric threshold for any signal.

When uncertain and there is no concrete material context risk, choose CONTINUE.

## FRESH procedure

Before stopping:

1. confirm the current obligation is fully persisted;
2. reconcile Task Board when implementation state exists, plus the exact active branch/state needed for recovery;
3. identify the exact next legal obligation;
4. verify that a fresh chat can recover everything needed from durable state without this transcript;
5. do not start the next obligation;
6. treat the hygiene handoff as a real workflow stop;
7. use `workflow/common/USER_STOP.md` with the context-hygiene fresh-chat variant.

The response should explain only that the completed work is safely persisted and a clean context is now preferable for the next obligation. Do not expose token estimates or internal context-budget speculation.

## Not a blocker or policy change

A context-health FRESH result:
- does not change requirements, plan, execution policy, review requirement or Task Board semantics;
- does not mean current work failed;
- does not authorize skipping a pending gate;
- must not be used to avoid a difficult but legal operation;
- is only a session-continuity handoff.

The new chat reconstructs state from current workflow `main` + project durable state and resumes the exact next obligation.
