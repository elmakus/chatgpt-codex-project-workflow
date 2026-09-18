# Audit — ChatGPT-only Brainstorming → Definition Promotion Gate

Date: 2026-09-18  
Base: `main@b8dbe46e8160a0442ffea2216c9c33fbf230a4d3`  
Reviewed subject: `fix/chatgpt-only-brainstorm-promotion-gate@2e0601ba021e3c1c4de060c16718d02ebba9fe3a`

Verdict: **GREEN — bounded semantic self-audit**

## Problem

The prior `chatgpt_only` route allowed Brainstorming to decide that enough facts/accepted choices existed and then continue through Project Definition into Planning as a deterministic role transition.

That could make a normal exploratory conversation leave Brainstorming too early and produce a complete plan before the user intended to formalize the project.

## Intended rule

For a new exploratory `chatgpt_only` definition scope:

```text
BRAINSTORMING ↔ RESEARCH
        ↓
ready_for_definition
        ↓
USER PROMOTION REQUIRED
        ↓
PROJECT DEFINITION
        ↓
Definition Complete = GREEN
        ↓
PLANNING
```

The promotion gate is user-owned.

Brainstorming readiness, research completion, repeated agreement with individual ideas, or assistant confidence do not authorize Project Definition.

Once Project Definition is explicitly authorized for the current scope, bounded Research ↔ Definition loops do not repeatedly ask for promotion. Reopening open-ended Brainstorming resets the gate for the reopened scope.

`Definition Complete = GREEN → Planning` remains deterministic and automatic when planning is in scope.

## Durable semantics

The Brainstorm template now distinguishes:
- `Status: tentative | ready_for_definition`;
- `Definition promotion authorization: pending | user_authorized | not-applicable`.

Under a policy route that requires explicit promotion, only an explicit user instruction may set `user_authorized`.

The `chatgpt_only` router requires either:
- explicit current user promotion; or
- durable `user_authorized` state for the same scope.

If the user promotes in the current turn, the authorization is persisted before Definition starts.

## Regression checks

1. Brainstorming readiness is not phase-promotion authority — PASS.
2. Research completion is not phase-promotion authority — PASS.
3. Project Definition verifies the selected policy's entry gate — PASS.
4. The Brainstorm template has a durable promotion marker — PASS.
5. Only explicit user intent may mark `user_authorized` when the selected route requires it — PASS.
6. The `chatgpt_only` first exploratory transition into Definition is user-owned — PASS.
7. Without authorization, neither Definition nor Planning may begin — PASS.
8. Ready-but-unpromoted Brainstorming is a real user stop — PASS.
9. Explicit authorization is persisted before Definition starts — PASS.
10. Research cannot bypass the promotion gate — PASS.
11. Research ↔ Definition loops after authorized Definition do not reprompt — PASS.
12. Reopened open-ended Brainstorming resets authorization to `pending` — PASS.
13. `Definition Complete = GREEN → Planning` remains automatic — PASS.
14. The old deterministic `RESEARCH → PROJECT DEFINITION → PLANNING` example is removed — PASS.
15. The router recognizes its policy-specific promotion stop as a real turn boundary — PASS.
16. USER_STOP formats the gate without requiring a fresh chat — PASS.
17. README lifecycle matches the new boundary — PASS.
18. CHANGELOG records the behavior — PASS.

Result: **18/18 PASS**.

## Audit finding during implementation

An initial audit pass found one router inconsistency: the old deterministic example still showed `RESEARCH → PROJECT DEFINITION → PLANNING`, and the router said only root-defined boundaries could end the turn.

This was corrected before the frozen reviewed subject:
- the deterministic example now begins at legally entered Project Definition;
- the router explicitly recognizes policy-specific boundaries;
- the promotion gate is checked before Definition.

The final 18/18 pass is against the corrected frozen subject above.

## Scope isolation

The user-owned promotion rule is enforced by `workflow/chatgpt_only/ROUTER.md`.

Policy-neutral common files only expose/obey the concept that a selected policy may own a promotion boundary; they do not impose the `chatgpt_only` user gate on other execution-policy namespaces.

## Verdict

**GREEN. The corrected `chatgpt_only` subject prevents automatic Brainstorming/Research → Project Definition promotion while preserving automatic Definition GREEN → Planning.**

Persisting this audit file adds evidence after the frozen reviewed subject and does not change the reviewed workflow semantics.
