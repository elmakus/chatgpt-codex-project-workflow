# ChatGPT ↔ Codex Contract

## 1. Responsibilities

### ChatGPT — strategic/planning authority

ChatGPT owns primarily:
- research and source verification;
- product/system requirements;
- architecture and frozen strategic decisions;
- global invariants;
- Master Plan and milestone structure;
- requirement coverage;
- initial Task Card decomposition;
- OpenSpec candidate mapping;
- execution-prep handoff to Codex, including an explicit session recommendation and copy-paste-ready start prompt;
- strategic review;
- product/architecture decisions for strategic blockers;
- plan changes when new evidence invalidates a frozen assumption.

ChatGPT should not freeze code-dependent implementation design far ahead of the code.

### Codex — implementation/execution authority

Codex owns primarily:
- repository/source inspection;
- exact branch/HEAD and Git work;
- READY-card selection and recovery;
- Refresh Gate;
- just-in-time OpenSpec creation/reconciliation;
- implementation;
- tests and review;
- durable execution state/evidence;
- milestone acceptance;
- cumulative handoff;
- project-level accountability for delegated work;
- strategic escalation when required.

Codex operates inside accepted requirements, strategic architecture and behavior contracts.

Internal Codex worker/runtime orchestration is not defined here. When the owner's `codex_workflow` is installed and enabled, its installed instructions own runtime mechanics. See `workflow/contracts/CODEX_ORCHESTRATION.md` for the domain boundary.

## 2. GitHub and chat

The project repository is durable project truth.

ChatGPT chat is a strategic communication/control channel. It is not the sole store of decisions, evidence, plans or execution state.

Do not copy huge diffs, entire plans, whole OpenSpec trees or hundreds of test lines into chat. Persist them and send a precise pointer.

## 3. Strategic escalation: when to use it

Do not use ChatGPT as a routine message bus.

Escalate strategically when evidence reveals, for example:
- contradictory requirements;
- a needed architecture change;
- a product decision;
- an impossible or materially wrong acceptance contract;
- new evidence that invalidates a frozen plan/assumption;
- material external-contract change;
- a behavior/security/schema contract choice beyond Codex authority.

Routine implementation details inside approved behavior remain Codex authority.

## 4. Strategic blocker lifecycle

1. Codex stops dependent work and sets the current card `blocked`.
2. Codex writes complete blocker evidence under `implementation/blockers/`.
3. Codex safely commits/pushes the evidence when repository state allows.
4. Codex posts a short structured request to the configured ChatGPT control chat.
5. ChatGPT reads the durable evidence and only the necessary project/source context.
6. ChatGPT researches further when required.
7. ChatGPT replies with the exact same `request_id` and an authoritative `DECISION FOR CODEX:` line.
8. Codex accepts only a matching structured decision.
9. Codex writes the accepted decision under `decisions/` with provenance.
10. Codex reconciles Task Card/OpenSpec/plan/Task Board as required.
11. Codex resumes only after the blocker is resolved.

## 5. Request format

```text
CODEX STRATEGIC REQUEST
request_id: <unique project-milestone-task-nonce>
Project: <project>
Milestone: <milestone>
Task: <task>
Status: BLOCKED

Reason:
<short reason>

Evidence:
<repo-relative path>
Commit: <exact sha>

Options:
A. ...
B. ...

Codex recommendation:
...

Please review the durable evidence and reply with the SAME request_id and one authoritative line beginning:
DECISION FOR CODEX:
```

The request should contain status/problem/pointer/options/recommendation/required response format, not the entire evidence payload.

## 6. Decision format

An authoritative ChatGPT response contains:

```text
request_id: <exact same request_id>
DECISION FOR CODEX: <decision>
```

Examples:

```text
DECISION FOR CODEX: OPTION B
DECISION FOR CODEX: APPROVE
DECISION FOR CODEX: REJECT
DECISION FOR CODEX: MODIFY PLAN
DECISION FOR CODEX: DEFER
```

Short rationale and required authoritative-artifact updates may follow.

## 7. Parsing and correlation rule

Codex:
- never treats arbitrary ChatGPT prose as an execution decision;
- requires the exact matching `request_id`;
- requires the explicit `DECISION FOR CODEX:` marker;
- does not trust "the latest reply" without correlation;
- remains blocked if the ID/marker is absent or ambiguous;
- may use a bounded wait/retry for the expected response, but must not convert that into routine polling.

Do not assume a later unrelated message answers the blocker.

## 8. Decision persistence

After receiving the matching decision, persist a decision record with:
- project/task;
- timestamp;
- chat/thread identity or name when available;
- exact `request_id`;
- exact decision marker;
- concise rationale;
- impact;
- artifacts updated;
- commit that persists the decision.

Chat is transport. The project repository is durable truth.

## 9. Channel asymmetry

Do not design the workflow around a guaranteed ChatGPT → Codex-session-UUID push API.

The proven/fallback interaction model is:

`Codex posts to ChatGPT chat → ChatGPT replies in that chat → Codex reads the correlated reply`.

Codex initiates and closes the exchange.

If product capabilities evolve, the correlation/persistence requirements still apply unless current workflow `main` is deliberately changed.

## 10. User interaction policy

The user should make real product/strategic decisions, not manually transport state.

Do not require the user to:
- copy long outputs between ChatGPT and Codex;
- choose the next card when Task Board selection is deterministic;
- move handoffs;
- copy OpenSpec;
- track dependencies manually;
- rewrite an accepted ChatGPT decision into Codex state;
- infer after execution prep whether to start a fresh Codex session or reuse the current one;
- invent the Codex kickoff prompt after ChatGPT has already prepared the milestone.

When a genuine product decision is necessary, present the smallest useful decision surface.

After execution prep, ChatGPT must explicitly recommend `FRESH` or `CONTINUE EXISTING`, explain the reason briefly, provide a copy-paste-ready Codex start prompt, and state the user's smallest next action. Follow the detailed rules in `workflow/EXECUTION_PREP.md`.

Every user-visible Codex execution status must also make the continuation state explicit:
- if execution can continue deterministically, state that Codex is continuing automatically and that no user action is required;
- if execution is blocked on the user, use an explicit `USER ACTION REQUIRED:` line with the smallest concrete decision, authorization or input;
- if a fresh Codex context is merely recommended, label it `SESSION HANDOFF RECOMMENDED:` and distinguish that recommendation from an authorization/product-decision gate;
- if the milestone is fully closed, state `MILESTONE COMPLETE:` with the checkpoint.

A Task Card completion report must not look like an implicit request to intervene. Informational progress messages do not suspend the standard card loop when the next READY card is deterministic.
