# Audit — ChatGPT-only Role Transition / Review State Machine

Date: 2026-09-18  
Base: `main@a8debd2983543553047124377f225e7c53781a5f`  
Audited branch: `refactor/chatgpt-role-transitions-review-none@fc163e5911642c88ef6ffdd1735c79f6f3c68302`

Verdict: **GREEN**

## Architecture

Normal ChatGPT role identity is per current obligation, not permanent for the whole chat.

```text
ROLE
→ persist durable result/state
→ return to chatgpt_only/ROUTER.md
→ router selects next legal ROLE
→ continue same chat
```

Completing a role is not a user stop.

The router owns transitions. A role module owns only the current obligation.

## Independent review requirement

Active ChatGPT-only Card/milestone review requirement is:

```text
REQUIRED | RECOMMENDED | none
```

- REQUIRED: real fresh independent-review gate for high-risk work.
- RECOMMENDED: real fresh independent-review gate intentionally included in accepted contract.
- none: no review state/gate.

If the user later explicitly requests independent review for `none`, durable authority is first changed to RECOMMENDED, then normal review state is created.

There is no active ChatGPT-only OPTIONAL review state.

## Reviewer entry

Fresh reviewer reads only:
- global bootstrap/policy router/common authority;
- `chatgpt_only/REVIEW.md` + `STATE.md`;
- Task Board;
- exact active branch;
- exact review subject;
- reviewed Card/milestone contract;
- same authority slice used by implementation;
- required evidence;
- actual reviewed subject/source/runtime needed for verdict;
- conditional OpenSpec/handoff/dependency/research/readback only when authority requires it.

Previous implementation-chat narrative is not review evidence.

## GREEN transition

```text
REVIEW
→ persist GREEN
→ review role ends
→ ROUTER
→ next legal role
```

No user-facing stop occurs merely because review is GREEN.

Possible next roles include EXECUTION, EXECUTION_PREP or CLOSE.

## RED transition — bounded correction

```text
REVIEW
→ persist RED + evidence
→ determine correction is safely L1/L2 + authorized + unblocked
→ review role ends
→ ROUTER
→ EXECUTION_PREP or EXECUTION
→ implement correction
```

The review module does not perform executor logic.

After the same chat implements a corrected subject that requires/recommends independent review:

```text
EXECUTION
→ freeze new exact subject
→ review_state: pending
→ REAL STOP
→ fresh independent reviewer required
```

The chat cannot review the subject it just implemented.

## RED transition — non-routable correction

If RED correction:
- cannot be bounded safely;
- requires L3 strategic authority;
- reaches explicit user/deployment/live-write authorization;
- has a concrete runtime/access/input blocker;

then the workflow reaches a real stop and uses the common user-stop response contract.

## Other role transitions

### Execution preparation

```text
EXECUTION_PREP
→ READY state persisted
→ role ends
→ ROUTER
→ EXECUTION
```

No prep-only status stop.

### Execution

Routine GREEN Card:
```text
EXECUTION
→ done
→ if another READY Card: continue
→ if JIT refinement: ROUTER → EXECUTION_PREP
→ if review due: pending → REAL STOP
→ if milestone close due: ROUTER → CLOSE
```

### Close

```text
CLOSE
→ finalize/reconcile checkpoint
→ if next approved milestone exists: role ends → ROUTER → EXECUTION_PREP
→ otherwise end of approved scope → REAL STOP
```

### Recovery

```text
RECOVERY
→ coherent durable state restored
→ role ends
→ ROUTER
→ recovered obligation
```

Recovery success alone is not a user stop.

## Real stops

A final workflow-status response is allowed only when:
1. this chat implemented a REQUIRED/RECOMMENDED review subject and a fresh independent reviewer is required;
2. an L3 strategic/user decision is required;
3. an explicit user/deployment/live-write authorization gate is due;
4. a concrete runtime/access/input blocker prevents progress;
5. approved scope is complete with no deterministic authorized next work.

## User response contract

All normal-ChatGPT roles use:

`workflow/common/USER_STOP.md`

Response shape:
1. what happened;
2. what it means now;
3. exact next step.

When user action is required:
`USER ACTION REQUIRED: <smallest exact action>`

When scope is complete with no action:
`No action required.`

When a fresh chat is required/recommended, the same response includes a ready-to-copy branch-aware `NEW CHAT START PROMPT`.

No intermediate status-only response is allowed between deterministic legal role transitions.

## Static checks

PASS:
- no OPTIONAL token in active ChatGPT-only/common execution path;
- REQUIRED/RECOMMENDED/none contract present;
- `none` creates no review state;
- explicit later review request promotes to RECOMMENDED;
- GREEN reviewer returns to router;
- RED bounded reviewer returns to router;
- REVIEW.md contains no direct remediation execution steps;
- EXECUTION_PREP/CLOSE/RECOVERY return role completion to router;
- global real-stop contract present;
- common user-stop contract contains user-action/no-action/fresh-chat variants;
- start/project-instructions prompts contain no stale OPTIONAL/remediation semantics.

## Final verdict

**GREEN.** Reviewer/executor/close/recovery are now bounded roles selected by one router, and user-visible workflow status is emitted only at real stops through one common response contract.
