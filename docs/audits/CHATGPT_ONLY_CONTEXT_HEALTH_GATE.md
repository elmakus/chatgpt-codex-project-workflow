# Audit — ChatGPT-only Context Health Gate

Date: 2026-09-18  
Base: `main@ac4907c62f6aaecbc3704a79f9cd3b55a0b3eb87`  
Audited branch: `feat/chatgpt-context-health-gate@6e505462e0e063d038d5dd5c09b1e61cbd715043`

Verdict: **GREEN**

## Goal

Provide a clean-context handoff when one normal ChatGPT chat has accumulated materially risky stale/irrelevant context, without:
- imposing fixed token/turn/Card/milestone thresholds;
- interrupting active work;
- duplicating fresh-review resets;
- creating status-only stops after routine role completion.

## Routing position

```text
ROLE/CARD complete
→ persist durable state
→ ROUTER
→ existing real stop?
   ├─ yes → use that boundary
   └─ no
      → context-health trigger?
         ├─ no → next role immediately
         └─ yes → CONTEXT_HEALTH.md
                    ├─ CONTINUE → next role immediately
                    └─ FRESH → hygiene user stop + fresh-chat prompt
```

## Safe-boundary invariant

Context health is evaluated only when:
- the current obligation is finished;
- material state/evidence is durable;
- Task Board is coherent;
- no external write/readback or other same-session operation is half-complete;
- exact next obligation is recoverable from repository state.

It never interrupts:
- an active Card;
- active independent-review inspection;
- an in-flight external mutation/readback sequence;
- an unresolved state transition.

## Natural review reset priority

If a REQUIRED/RECOMMENDED independent-review boundary already requires a fresh chat, no separate hygiene gate is run.

The review handoff is the context reset.

The same applies to other already-owned real stops:
- L3/user decision;
- explicit authorization;
- concrete runtime/access/input blocker;
- end of approved scope.

## Context-health decisions

### CONTINUE

Default when no concrete material context risk exists.

Routine completion of a Card, role or milestone alone is not enough.

### FRESH

Allowed only when accumulated context itself creates concrete material risk for the next obligation, such as:
- materially superseded/contradictory state that could bleed into the next task;
- difficulty distinguishing durable truth from old transient discussion/tool output;
- substantial state reconstruction burden that is already cleaner in the repository;
- a meaningful combination of stale transient history, large irrelevant diagnostic output and a complex next obligation.

A different role, milestone, phase, workstream or authority/source area is not a context-health signal by itself. Workflow topology determines what authority to load next; it does not prove that the transcript is degraded.

A chat started from a context-hygiene fresh-session handoff requires new concrete degradation accumulated after recovery before another `FRESH` result is legal.

No numeric context threshold is used.

## Scenario audit

### 1. Long run of simple Cards, context still clean

```text
T01 done → router → no context-risk → EXECUTION T02
T02 done → router → no context-risk → EXECUTION T03
```

Result: **CONTINUE**. No arbitrary fresh chat.

### 2. Long run of Cards, stale diagnostics now dominate context

```text
T04 done → router
→ concrete context-risk signal
→ Context Health Gate
→ FRESH
→ exact next Card remains ready in durable state
→ hygiene fresh-chat prompt
```

Result: **FRESH** at safe boundary.

### 3. Executor reaches pending independent review

```text
implementation done
→ review_state: pending
→ fresh-review real stop
```

Result: no separate context-health handoff. Review already provides fresh context.

### 4. Reviewer GREEN then next Card

```text
REVIEW GREEN
→ router
→ context trigger absent
→ EXECUTION
```

Result: same chat continues as executor.

If review/tool history makes next obligation materially risky:

```text
REVIEW GREEN
→ router
→ context trigger
→ CONTEXT_HEALTH
→ FRESH
```

Result: hygiene reset before executor role starts.

### 5. RED review → bounded correction

```text
REVIEW RED
→ router
→ EXECUTION correction
→ corrected reviewable subject
→ review_state: pending
→ fresh-review real stop
```

Result: the mandatory review boundary provides the reset; no extra hygiene stop.

### 6. Milestone finalized, next approved milestone differs materially

```text
CLOSE done
→ router
→ next milestone approved
→ different authority/source area only
→ no context-health trigger
→ EXECUTION_PREP
```

Result: **CONTINUE**. The milestone/authority transition is workflow topology, not evidence that the current transcript is harmful.

If substantial stale diagnostics or contradictory transient state accumulated and now create concrete material risk for the next milestone, that separate harmful-context evidence may trigger Context Health.

### 7. Short context-hygiene recovery does not bounce

```text
fresh chat started from context-hygiene handoff
→ recover exact durable obligation
→ finish/persist it after a short continuation
→ next deterministic obligation uses a different authority area
→ no new harmful-context evidence accumulated
→ CONTINUE
```

Result: **CONTINUE**. Completion of the recovered obligation and a different next authority area do not justify another hygiene handoff.

A later `FRESH` remains legal only if new concrete context degradation accumulates in this chat after recovery.

### 8. Runtime/user/authorization blocker already exists

Result: blocker/authorization stop owns the boundary. Context health is not run separately.

### 9. Mid-Card context feels large

Result: no hygiene interruption. Finish/persist the current obligation first, then evaluate at router boundary.

## User-facing hygiene handoff

Uses `workflow/common/USER_STOP.md`.

Required shape:
- completed work is safely persisted;
- clean context is preferable before next obligation;
- `USER ACTION REQUIRED:` asks user to start fresh normal ChatGPT chat;
- branch-aware `NEW CHAT START PROMPT` points to exact next obligation and durable start pointer;
- no guessed token counts/context percentages are exposed.

## Static validation

PASS:
- context-health module exists;
- safe-boundary-only rule exists;
- active Card/review/write interruption prohibited;
- fixed token/turn/Card/milestone thresholds prohibited;
- CONTINUE is default without affirmative material transcript risk;
- role/milestone/phase/workstream/authority-area transitions are not standalone context-health signals;
- a context-hygiene recovery requires new concrete degradation before another FRESH result;
- fresh review and other real stops have priority;
- every completed Card returns to router before another Card starts;
- FRESH requires fully durable current obligation and exact recoverable next obligation;
- common user-stop contract has hygiene variant;
- context-health handoff changes no project authority/policy/review semantics.

## Final verdict

**GREEN.** The workflow now has a qualitative, safe-boundary context refresh mechanism without arbitrary cadence or duplicate review resets.
