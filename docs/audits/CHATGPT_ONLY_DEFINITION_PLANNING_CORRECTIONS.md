# Corrective Package — Definition / Planning Boundary

Date: 2026-09-18  
Base: `main@23b8c368aea160566abdfd3fbc42bd0facb88bd4`  
Implementation branch: `fix/definition-planning-audit-findings`

Status: **INDEPENDENT RE-REVIEW RED — BOUNDED REMEDIATION REQUIRED**

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

## Independent review attempt — 2026-09-18

Reviewed exact subject:

- base: `23b8c368aea160566abdfd3fbc42bd0facb88bd4`
- head: `d769474185218e89c41025d9867cf35db159bfb7`

Verdict: **RED**

### RED-01 — plan-review state is not consistently recoverable outside Task Board

The new plan-review module correctly places mutable pre-execution review state under `planning/reviews/<plan-revision>.md`, but three existing control points still assume review state is Task-Board-owned:

- root `CHATGPT.md` says implementation/review state is recovered from `implementation/TASK_BOARD.yaml`;
- `workflow/chatgpt_only/ROUTER.md` bootstrap says any implementation/review/blocker/recovery state triggers a Task Board read;
- `workflow/common/USER_STOP.md` has only an implementation-review fresh-chat variant whose durable pointer is hard-coded to `implementation/TASK_BOARD.yaml`.

This conflicts with the new state split and can make a pre-execution plan review non-recoverable before a Task Board exists.

Required correction:
- distinguish implementation review state from plan-review state in bootstrap/routing;
- add an explicit plan-review fresh-chat handoff using `planning/reviews/<plan-revision>.md` as the durable start pointer;
- make `PLAN_REVIEW.md` select that handoff explicitly.

### RED-02 — old L3 wording can still create a false user stop

The router/context-health wording was narrowed, but two authoritative paths still retain the old broad shorthand:

- root `CHATGPT.md` still lists “a strategic/L3 decision requires user authority” as a real stop;
- `workflow/chatgpt_only/REVIEW.md` still says corrective work that “requires L3 authority” is a real stop.

After the Definition/Planning split, a plan-only change to milestone structure/order/outcome or execution strategy can be above L1/L2 without requiring user/product authority. Those cases must route to Planning rather than stop for the user.

Required correction:
- remove the generic L3→user-stop implication;
- classify post-review strategic corrections through Planning / Project Definition / Research, with user stop only for unresolved user/product authority or another explicit real gate.

### RED-03 — one revision path can overwrite a prior review attempt

`PLAN_REVIEW.md` says every corrective plan edit creates a new immutable subject and a new review attempt, but the only canonical record path is `planning/reviews/<plan-revision>.md` and the planner is told to create/update that revision-specific record. Without requiring a new plan revision (or another distinct attempt path), a RED record can be overwritten with a different subject under the same review-state file.

Required correction:
- make one review record correspond to one exact plan revision/subject;
- require a new plan revision (or otherwise distinct durable review record) for any substantive corrective edit;
- allow post-GREEN approval to change only deterministic lifecycle metadata while keeping the reviewed plan body identical, otherwise require a new review subject.

## Bounded remediation after RED

The RED findings above were corrected on the same branch after the independent reviewer role ended.

### RED-01 remediation

- root bootstrap no longer assumes every review lifecycle is Task-Board-owned;
- the ChatGPT-only router distinguishes implementation review state in Task Board from pre-execution plan-review state in `planning/reviews/<plan-revision>.md`;
- the router treats a request/handoff only as a locator and reads the plan-review record as authority;
- `workflow/common/USER_STOP.md` now distinguishes implementation-review and plan-review fresh-chat handoffs;
- the plan-review handoff uses `planning/reviews/<plan-revision>.md` as the durable start pointer;
- Context Health now treats Task Board coherence/reconciliation as conditional on implementation state existing.

### RED-02 remediation

- root `CHATGPT.md` no longer uses generic `L3` stop wording;
- implementation-review RED flow classifies corrections through Execution/Execution Prep, Planning, Project Definition or Research before deciding whether a user stop exists;
- State, Execution, Task Cards, Close and Recovery now consistently route plan-only/Definition/evidence changes through the owning role;
- user stop remains only for unresolved user/product authority or another explicit real gate.

### RED-03 remediation

- one plan-review record now corresponds to one exact plan revision/subject;
- a substantive correction after a verdict requires a new plan revision and therefore a distinct review record;
- completed RED/GREEN review records are not reused for another subject;
- after GREEN, only deterministic lifecycle metadata may change without a new review; any substantive plan-body edit requires a new revision and a new independent review subject.

### Additional semantic preservation check

The earlier rule remains “independent plan review when practical.” A substantive plan may use `none` only when independent review is concretely impractical, no project/user authority requires it, and the planning audit records the concrete reason; convenience alone is insufficient. This avoids silently strengthening “when practical” into an unconditional hard gate.

### Implementer self-check after remediation

Static/coherence checks are GREEN for:
- shared Master Plan policy neutrality;
- Requirements/Planning/Execution Prep ownership separation;
- Task Board remaining the sole mutable execution-state authority;
- separate plan-review state and recoverable fresh-chat handoff;
- immutable review subject / distinct review-attempt records;
- router priorities and GREEN/RED role transitions;
- Context Health behavior before Task Board exists and at review boundaries;
- absence of remaining `L3` user-stop shorthand in root/chatgpt-only review flow;
- plan-only replan routing to Planning while Project Definition remains valid.

These checks are implementer self-checks only. They do not constitute the required fresh independent verdict for the corrected subject.

## Self-check scope

The implementing chat may run static/coherence checks but must not issue the independent verdict for the corrected subject.

The fresh reviewer should specifically verify:
1. all four original findings are actually fixed on the branch;
2. RED-01 and RED-02 above are fixed;
3. no new duplicate authority source was introduced;
4. shared templates remain policy-neutral;
5. plan review is operationally routable without Task Board existing yet;
6. review subject immutability is preserved;
7. planner/Definition/Execution Prep ownership remains non-circular;
8. plan-only replan does not produce a false user stop;
9. no previous ChatGPT-only semantics were unintentionally lost.

## Fresh independent re-review — 2026-09-18

Reviewed exact subject:

- base: `23b8c368aea160566abdfd3fbc42bd0facb88bd4`
- head: `cf34c4cb0c85eb8b37d4b8d75a19bce565021702`

Verdict: **RED**

### Re-review results

The original four findings and the three previously recorded RED findings were rechecked independently against the exact branch diff and current workflow authority.

- Finding 1 — shared Master Plan policy neutrality: **GREEN**. The shared template no longer imports `workflow/chatgpt_only/*`, legacy, Codex or mixed-specific execution paths.
- Finding 2 — requirement coverage ownership: **GREEN**. Canonical Requirements no longer owns milestone mapping; Master Plan owns requirement → milestone/work-package-or-JIT coverage; Execution Prep owns concrete Task Cards.
- Finding 3 — independent plan-review semantics: **PARTIALLY GREEN, but the integrated routing regression check fails**. `PLANNING.md`, `PLAN_REVIEW.md`, root bootstrap and the dedicated user-stop handoff restore the intended fresh independent review lifecycle, but `ROUTER.md` contains a contradictory same-chat transition example described below.
- Finding 4 — broad L3/user-stop classification: **GREEN** in the authoritative root/chatgpt-only routing and review paths. Plan-only strategic replans route to Planning; Definition changes route to Project Definition; evidence gaps route to Research; user stop is reserved for unresolved user/product authority or another explicit real gate.
- RED-01 — plan-review state recoverability outside Task Board: **GREEN**. Plan-review state is separately recoverable from `planning/reviews/<plan-revision>.md`, including a dedicated fresh-chat handoff.
- RED-02 — remaining generic L3 → user-stop wording: **GREEN** in the authoritative root/chatgpt-only review flow.
- RED-03 — reuse/overwrite of a review record for a corrected subject: **GREEN**. One review record maps to one exact plan revision/subject and substantive correction requires a new plan revision/review record.
- Duplicate-authority regression: **GREEN**. Task Board remains sole mutable execution-state authority; pre-execution plan-review state is separate and explicitly not execution state.
- Review-subject immutability regression: **GREEN** in `PLAN_REVIEW.md` / `PLANNING.md`.
- Definition / Planning / Execution Prep ownership regression: **GREEN** and non-circular.
- Plan-only replan false-user-stop regression: **GREEN** in the operational route modules.
- Previous ChatGPT-only semantics preservation: **RED** because the router now contains an internally contradictory same-chat plan-review example that can defeat the restored independence rule.

### RED-04 — authoritative router example permits an impossible same-chat plan review transition

`workflow/chatgpt_only/ROUTER.md` states:

> “The same chat may therefore move, for example:”

and immediately gives:

`RESEARCH → PROJECT DEFINITION → PLANNING → PLAN_REVIEW → PLANNING → EXECUTION_PREP → EXECUTION`

That contradicts the same corrected subject's hard independence rules:

- root `CHATGPT.md` makes a REQUIRED/RECOMMENDED fresh independent review a real fresh-chat boundary;
- `PLANNING.md` says the chat that authored the exact plan subject cannot issue its independent verdict;
- `PLAN_REVIEW.md` requires a fresh normal ChatGPT chat that did not author the exact reviewed Master Plan subject.

Because `ROUTER.md` is authoritative for role transitions, the explicit “same chat” example creates a conflicting legal path in which the plan-authoring chat appears allowed to enter `PLAN_REVIEW` directly. A reviewer/agent following the example rather than the earlier stop clause could self-review the plan subject, which is exactly the independence semantic this corrective package is intended to restore.

Required correction:

- remove `PLANNING → PLAN_REVIEW` from any sequence explicitly described as a same-chat transition;
- represent the authoring path as `... → PLANNING → [fresh independent-plan-review stop]`;
- if an example of post-review continuation is desired, show it from the fresh reviewer session, e.g. `PLAN_REVIEW → PLANNING → EXECUTION_PREP → EXECUTION`;
- keep the existing fresh-review priority and dedicated `planning/reviews/<plan-revision>.md` handoff unchanged.

This is a bounded routing/documentation inconsistency. No GREEN verdict is issued for the reviewed subject.

## Verdict

**RED for `cf34c4cb0c85eb8b37d4b8d75a19bce565021702`. Findings 1, 2 and 4 plus RED-01/02/03 are corrected, but RED-04 leaves the restored independent plan-review lifecycle internally contradictory in the authoritative router. A corrected head requires a fresh independent re-review.**
