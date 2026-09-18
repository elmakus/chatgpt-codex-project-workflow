# Corrective Package — Definition / Planning Boundary

Date: 2026-09-18  
Base: `main@23b8c368aea160566abdfd3fbc42bd0facb88bd4`  
Implementation branch: `fix/definition-planning-audit-findings`

Status: **IMPLEMENTATION COMPLETE — INDEPENDENT REVIEW PENDING**

## Review subject

The corrective subject is the exact branch diff from the base above to the current head of:

`fix/definition-planning-audit-findings`

A fresh independent reviewer must reconstruct the exact head from GitHub rather than relying on this document for the commit SHA.

## Finding 1 — shared Master Plan template leaked chatgpt_only

Problem:
- `templates/MASTER_PLAN.md` is shared across policies;
- it hard-coded `workflow/chatgpt_only/*` modules.

Correction:
- shared template now references only `workflow/CONTEXT_ROUTING.md`, `workflow/common/DEFINITION.md` and `workflow/common/OPENSPEC.md`;
- policy-specific Planning/plan-review/Execution Prep/Task Card/state modules are selected by the active policy router.

Expected invariant:
- no `workflow/chatgpt_only/*`, legacy, Codex or mixed-specific execution path appears in the shared Master Plan template.

## Finding 2 — requirement coverage had two owners

Problem:
- canonical Requirements carried `Owner milestone`;
- Master Plan also carried requirement → milestone coverage;
- Planning therefore had to mutate Definition-owned requirements and two artifacts could disagree.

Correction:
- removed `Owner milestone` from the Requirements table;
- Requirements remains WHAT/constraints/invariants/acceptance authority;
- Master Plan is the sole requirement → milestone → planned-work-package/JIT coverage owner;
- Execution Prep remains the concrete Task Card mapper.

Expected invariant:
```text
Definition / Requirements = WHAT
Planning / Master Plan = requirement → milestone/work package/JIT
Execution Prep = concrete Task Cards
```

## Finding 3 — independent plan review semantics were accidentally weakened

Problem:
- pre-refactor semantics explicitly required independent plan review when practical;
- PR #21 changed this to “not an implicit lifecycle gate” without an explicit user decision.

Correction:
- restored “independent plan review when practical”;
- added `workflow/chatgpt_only/PLAN_REVIEW.md`;
- new/materially revised Master Plans classify independent review as RECOMMENDED when practical;
- explicit project/user authority may make it REQUIRED;
- trivial/editorial changes may use `none`;
- the authoring chat cannot independently review its exact plan subject;
- mutable review state lives outside the plan under `planning/reviews/<plan-revision>.md`;
- reviewed plan stays `draft` until required/recommended review is GREEN;
- GREEN routes back to Planning for approval;
- RED routes to Planning, Project Definition or Research according to defect ownership.

Expected invariant:
- no review lifecycle mutation changes the exact frozen plan subject.

## Finding 4 — L3/user decision was too broad a stop class

Problem:
- router/context-health shorthand treated generic `L3/user decision` as a user stop;
- after Definition/Planning split, some strategic changes are deterministic plan-only replans.

Correction:
- real stop wording now requires an unresolved strategic/product decision that actually needs user authority;
- plan-only milestone structure/order/outcome or execution-strategy changes route to Planning when Project Definition remains valid;
- Definition changes route to Project Definition;
- evidence gaps route to Research.

Expected invariant:
- “strategic” does not automatically mean “ask user”.

## Independent plan-review routing

The active ChatGPT-only router now has a separate Independent plan review route.

Normal substantial-plan flow:

```text
PROJECT DEFINITION
→ PLANNING (draft + planner self-audit)
→ PLAN_REVIEW pending
→ fresh independent reviewer
→ GREEN
→ PLANNING marks exact reviewed revision approved
→ EXECUTION_PREP
```

RED flow:

```text
PLAN_REVIEW RED
→ router
├─ bounded plan defect → PLANNING
├─ accepted target/decision defect → PROJECT DEFINITION
├─ evidence gap → RESEARCH
└─ unresolved user/product authority → USER STOP
```

A corrected plan that still requires/recommends review becomes a new immutable review subject and requires a fresh independent reviewer.

## Self-check scope

The implementing chat may run static/coherence checks but must not issue the independent verdict for this corrective subject.

The fresh reviewer should specifically verify:
1. all four findings are actually fixed on the branch;
2. no new duplicate authority source was introduced;
3. shared templates remain policy-neutral;
4. plan review is operationally routable without Task Board existing yet;
5. review subject immutability is preserved;
6. planner/Definition/Execution Prep ownership remains non-circular;
7. plan-only replan does not produce a false user stop;
8. no previous ChatGPT-only semantics were unintentionally lost.

## Verdict

**PENDING FRESH INDEPENDENT REVIEW.**
