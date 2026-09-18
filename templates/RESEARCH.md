# Research — <question>

Date: `<YYYY-MM-DD>`
Research question: `<exact question>`

## Durable continuation metadata — policy-activated only

Populate these fields when the **selected policy route explicitly requires a durable cross-session Research obligation**. This shared template does not create routing semantics by itself; a policy route that does not define this lifecycle may omit these fields.

Research ID: `<stable-id>`
Status: `active | blocked | complete | consumed`
Origin role: `brainstorming | project_definition | strategic_planning | plan_review | execution_prep | execution_resolution | other`
Origin subject: `<exact durable scope/revision/Card/blocker ref>`
Return target: `<exact role:subject>`
Return reconciliation: `pending | applied`
Return reconciliation result: `<exact durable result ref(s) | none>`

## Scope

...

## Sources / evidence

| Source | What it supports | Freshness / limitations |
|---|---|---|
| ... | ... | ... |

## Verified findings

...

## Repository/current-state findings

...

## Assumptions / uncertainties

...

## Alternatives

...

## Analysis

...

## Recommendation, if requested

...

## Project Definition candidates

- Verified constraint that may need promotion into requirements: ...
- Strategic/high-level choice that still needs accepted authority: ...
- Requirement/target-state candidate: ...
- Open user/product question: ...
- Downstream planning implication if Definition accepts it: ...

Research is evidence, not an accepted requirement/decision/plan by itself. Return to the exact recorded Return target; only changes to accepted product/system authority are promoted through Project Definition under the selected policy's entry rules.

Pointer ownership and lifecycle are defined by the selected policy route, **not by this shared template**. Under `chatgpt_only`, pre-execution Research uses `PROJECT.md → Active research obligation` and implementation/recovery Research uses Task Board `research_obligation`; keep `complete` through any authorized continuation-classifier step until the final owning Return target durably reconciles the findings. A legacy/other-policy route that does not define these pointer semantics must not create PROJECT/Task-Board Research routing state merely because this template exposes optional continuation metadata. Do not infer Origin/Return from chat history.
