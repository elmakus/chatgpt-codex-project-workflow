# Semantic Audit — Delegated JIT Planning + Role/Model Separation

Date: 2026-09-18
Base: `main@384695713c34e26aa6c6e79ef98bc9382a3eea4d`
Audited implementation subject: `docs/delegated-jit-planning@2ccf7219766c8ce7e24c1f78888679d3da466082`
Verdict: **GREEN**

## Scope

Audit the workflow changes that:
1. define planner/orchestrator/executor/reviewer as authority roles rather than model identities;
2. allow future milestone/card detail to remain deferred when predecessor evidence is genuinely required;
3. delegate L1/L2 execution refinement to the execution orchestrator without requiring return to the original planner;
4. reserve L3 changes for strategic replanning;
5. keep ChatGPT fresh-session requirements limited to independent-review boundaries, with optional fresh chats for context hygiene.

## Semantic checks

### GREEN — no model hard-coding

- Workflow roles are strategic planner, execution orchestrator/JIT planner, executor/worker and independent reviewer.
- Changed normative files contain no hard-coded references to Astra, Sol, Luna, Muse or Spark.
- No workflow contract requires a named model or reasoning level.
- The same role may be filled by different model/session choices over project lifetime.
- `codex_workflow` remains responsible for internal Codex worker/model routing when installed; Project Workflow does not integrate with or duplicate those mechanics.

### GREEN — deferred decomposition

- Future Task Cards do not need to exist when correct scope materially depends on predecessor evidence.
- Master Plan may carry a durable JIT decomposition/deferred-detail trigger.
- Placeholder cards with unknowable “whatever predecessor reveals” scope are discouraged.
- Requirement coverage still requires a real implementation Task Card before execution of that requirement, but not necessarily at initial plan approval.
- Task Board may grow the real card set JIT after the recorded trigger becomes durable evidence.

### GREEN — delegated planning authority

- L1 execution detail remains executor/orchestrator authority.
- L2 JIT decomposition/refinement allows the execution orchestrator to create/split/merge/reorder/replace not-yet-started cards, bind predecessor evidence, complete optional milestone execution detail and refine technical tests/acceptance/interfaces.
- L1/L2 work does not require return to the original planning model/session.
- Active `in_progress` cards are not silently rewritten through deferred decomposition.

### GREEN — strategic boundary

L2 authority is bounded by:
- accepted requirements;
- accepted/frozen architecture and decisions;
- global/milestone invariants;
- approved milestone outcome / behavior contract;
- explicit user/deployment/live-write/authorization gates.

Changing any of those is L3 strategic replan. Known L3 ambiguity may not be hidden as “deferred detail.”

### GREEN — authority preservation

- JIT-created cards inherit exact predecessor-result authority.
- Existing Authority Preservation / lossless-by-authority semantics remain intact.
- Orchestrator refinement cannot weaken strategic planner intent by paraphrase.

### GREEN — ChatGPT session semantics

- Under `chatgpt_only`, the same chat may continue planning/JIT orchestration/execution when context remains useful.
- A fresh normal ChatGPT chat remains mandatory only for REQUIRED/RECOMMENDED independent review of a subject implemented by the current chat.
- Outside review independence, a fresh chat is only a context-hygiene recommendation.
- No fixed token count or “every N milestones” fresh-chat rule was introduced.
- Fresh-chat recovery is from durable repo authority; previous chat transcript is not required.

### GREEN — policy semantics preserved

- `chatgpt_only`, `codex_only`, and `mixed` execution-policy behavior remains unchanged.
- Capability Gate remains `mixed`-only.
- Fixed-policy capability preflight remains prohibited.
- Existing independent-review requirements remain intact.
- Explicit authorization/live-write gates remain hard stops.

## Final assessment

**GREEN.** A strong planner can establish durable strategic authority once, while a later execution orchestrator can safely perform evidence-driven JIT milestone/card refinement without model hard-coding or repeated returns to the original planner. Strategic drift still forces explicit replan.
