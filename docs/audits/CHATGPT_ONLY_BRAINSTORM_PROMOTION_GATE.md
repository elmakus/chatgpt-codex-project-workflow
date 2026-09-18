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


## Fresh independent review — 2026-09-18

Reviewed exact GitHub state:

- authority `main`: `b8dbe46e8160a0442ffea2216c9c33fbf230a4d3`
- review branch HEAD reconstructed at review start: `a6d2f524875b59fd856d4a163360bc38f2f96aaf`
- merge base: `b8dbe46e8160a0442ffea2216c9c33fbf230a4d3`
- frozen workflow semantic subject: `2e0601ba021e3c1c4de060c16718d02ebba9fe3a`
- PR: `#25`
- branch: `fix/chatgpt-only-brainstorm-promotion-gate`

Verdict: **GREEN**

This was a fresh independent review reconstructed directly from GitHub. The prompt, PR body, prior chat and the earlier self-audit above were treated only as locators/history, not as proof.

The exact branch HEAD at review start is one commit beyond the frozen semantic subject. The delta `2e0601ba021e3c1c4de060c16718d02ebba9fe3a...a6d2f524875b59fd856d4a163360bc38f2f96aaf` contains only this audit file, so the workflow semantics under review remain frozen at `2e0601ba021e3c1c4de060c16718d02ebba9fe3a`.

### Full diff coverage

The complete `main...review-branch` diff was reconstructed and inspected. It contains exactly these files:

- `CHANGELOG.md`
- `README.md`
- `docs/audits/CHATGPT_ONLY_BRAINSTORM_PROMOTION_GATE.md`
- `templates/BRAINSTORM.md`
- `workflow/chatgpt_only/ROUTER.md`
- `workflow/common/BRAINSTORMING.md`
- `workflow/common/DEFINITION.md`
- `workflow/common/RESEARCH.md`
- `workflow/common/USER_STOP.md`

No other workflow, policy-router, execution or state files differ from current `main` in this PR.

### Independent review results

1. **Brainstorming readiness does not authorize Definition — GREEN.**  
   `workflow/common/BRAINSTORMING.md` now makes `ready_for_definition` a readiness state only. The selected policy owns the promotion boundary. The `chatgpt_only` router explicitly forbids entering Project Definition or Planning while promotion authorization is pending.

2. **Research cannot bypass the promotion gate — GREEN.**  
   Both `workflow/common/RESEARCH.md` and `workflow/chatgpt_only/ROUTER.md` state that research completion from an unpromoted exploratory scope is not phase-promotion authority and returns to Brainstorming/promotion handling.

3. **Only explicit user promotion grants authorization — GREEN.**  
   The `chatgpt_only` router accepts either an explicit current user instruction or already-durable `Definition promotion authorization: user_authorized` for the same scope. `templates/BRAINSTORM.md` explicitly states that, when the selected policy requires promotion, only an explicit user instruction may set `user_authorized`. Agreement with an idea, answering questions, assistant confidence or asking for more research is explicitly insufficient.

4. **Promotion authorization is durably recoverable — GREEN.**  
   `templates/BRAINSTORM.md` carries `Definition promotion authorization: pending | user_authorized | not-applicable`, and the router requires persistence of `user_authorized` before entering Definition. A fresh session can therefore recover phase authority from the active brainstorming record rather than inferring it from stale conversation.

5. **Authorized Research ↔ Definition loops do not reprompt — GREEN.**  
   Both the router and `workflow/common/DEFINITION.md` say that once Definition has been legally authorized for the current scope, ordinary bounded Research ↔ Definition evidence loops do not require another promotion.

6. **Returning to open-ended Brainstorming resets the gate — GREEN.**  
   The router requires resetting promotion authorization to `pending` when Definition deliberately returns to open-ended Brainstorming because the product/problem scope has materially reopened. The common Definition contract mirrors that scope-reset rule.

7. **Definition Complete = GREEN → Planning remains automatic — GREEN.**  
   The router explicitly excludes this transition from the promotion gate and keeps Planning as the deterministic next role when planning is in scope. No fresh user authorization was introduced between completed Definition and Planning.

8. **Policy-specific real-stop handling is coherent — GREEN.**  
   The router now recognizes the Brainstorming → Definition promotion boundary as an explicit policy-specific real stop, and `workflow/common/USER_STOP.md` only formats that stop. It does not become a fresh-chat boundary and does not create a second authority source.

9. **Common/template changes remain policy-neutral — GREEN.**  
   Shared common modules describe a selected-policy-owned entry boundary rather than imposing `chatgpt_only` semantics globally. The shared Brainstorm template includes `not-applicable` and conditions `user_authorized` on a policy actually requiring explicit promotion. The staged non-`chatgpt_only` route still dispatches through `workflow/legacy/CONTEXT_ROUTING.md` and its existing legacy Brainstorming/Research modules; this PR does not modify that policy tree.

10. **No `chatgpt_only` lifecycle regression found — GREEN.**  
    The former deterministic `RESEARCH → PROJECT DEFINITION → PLANNING` same-chat example is removed. Legal same-chat continuation begins only after Project Definition has been entered. Existing plan-review, implementation-review, context-health, execution and close boundaries are untouched by the PR diff.

11. **Prior self-audit does not contaminate the reviewed semantic subject — GREEN.**  
    The current branch HEAD differs from the frozen semantic subject only by the earlier audit-evidence commit. This independent verdict therefore judges the actual semantic diff and also verifies that the present HEAD adds no hidden workflow change after that subject.

### Regression / evidence note

GitHub reports no combined status checks and no pull-request workflow runs for either the frozen semantic subject `2e0601ba021e3c1c4de060c16718d02ebba9fe3a` or the review-start HEAD `a6d2f524875b59fd856d4a163360bc38f2f96aaf`.

This verdict therefore makes **no CI/test-execution claim**. It is an independent static/coherence review of the complete workflow/documentation diff, route semantics and authority graph.

## Independent verdict

**GREEN for the exact reviewed GitHub state rooted at `main@b8dbe46e8160a0442ffea2216c9c33fbf230a4d3`, with workflow semantics frozen at `2e0601ba021e3c1c4de060c16718d02ebba9fe3a` and review-start branch HEAD `a6d2f524875b59fd856d4a163360bc38f2f96aaf`. The user-owned Brainstorming → Project Definition promotion gate satisfies the requested invariants, preserves automatic Definition GREEN → Planning, and introduces no policy-leakage or lifecycle regression found in the complete diff.**

Persisting this section adds review evidence after the reviewed HEAD and does not change the reviewed workflow semantics.

