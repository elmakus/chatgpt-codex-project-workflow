# Semantic Audit — v3

## Audit question

> Is there any behavior, restriction, obligation, exception, recovery rule or authority rule in the complete v2.1 baseline that can no longer be reconstructed from v3?

**Result: PASS — no missing normative behavior found after the migration matrix and full v3 review.**

The only intentional changes are those explicitly mandated by the v3 migration prompt: project repository from first brainstorming, one-project-one-repository default, workflow-only workflow repo, state-separated project layout, `PROJECT.md` routing and phase-aware progressive disclosure.

## Forward semantic audit: v2.1 → v3

| Semantic area | v3 authority | Result |
|---|---|---|
| ChatGPT strategic/research/planning responsibility | `workflow/contracts/CHATGPT_CODEX.md` | PASS |
| Codex implementation/execution responsibility | `workflow/contracts/CHATGPT_CODEX.md`, `CODEX_ORCHESTRATION.md` | PASS |
| GitHub as durable state; chat not sole truth | `PROJECT_REPOSITORY.md`, `CHATGPT_CODEX.md` | PASS |
| Project→milestone→Task Card→OpenSpec-task distinction | `PLANNING.md`, `TASK_CARDS.md`, `OPENSPEC.md` | PASS |
| Master Plan content and non-task-tracker rule | `PLANNING.md`, `templates/MASTER_PLAN.md` | PASS |
| Task Card metadata/decomposition | `TASK_CARDS.md`, `templates/TASK_CARD.md` | PASS |
| Separate decision and execution states | `GITHUB_STATE.md`, `TASK_CARDS.md` | PASS |
| Exact card execution states | `GITHUB_STATE.md` | PASS |
| Milestone lifecycle and green close | `GITHUB_STATE.md` | PASS |
| Task Board as live index | `GITHUB_STATE.md`, `templates/TASK_BOARD.yaml` | PASS |
| Done-card `result_commit` / `result_pr` / `evidence` | `GITHUB_STATE.md`, `TASK_CARDS.md` | PASS |
| Card Definition of Done | `TASK_CARDS.md`, `GITHUB_STATE.md` | PASS |
| Refresh Gate | `EXECUTION.md`, `TASK_CARDS.md` | PASS |
| Selective OpenSpec required/skip policy | `OPENSPEC.md` | PASS |
| OpenSpec JIT against current code/handoff/card/dependencies | `OPENSPEC.md` | PASS |
| OpenSpec proposal/specs/design/tasks/apply/verify/archive sequence | `OPENSPEC.md` | PASS |
| Strategic blocker lifecycle | `CHATGPT_CODEX.md` | PASS |
| Unique `request_id` | `CHATGPT_CODEX.md` | PASS |
| Exact `DECISION FOR CODEX:` marker | `CHATGPT_CODEX.md` | PASS |
| Reject uncorrelated "latest reply" | `CHATGPT_CODEX.md` | PASS |
| Persist strategic decision in repository | `CHATGPT_CODEX.md`, `templates/DECISION.md` | PASS |
| Large evidence in Git, concise pointer in chat | `CHATGPT_CODEX.md` | PASS |
| Codex READY-card selection/recover in-progress | `EXECUTION.md` | PASS |
| No user selection when Task Board is deterministic | `EXECUTION.md`, `TASK_CARDS.md` | PASS |
| Dependency handling without generic DAG engine | `TASK_CARDS.md` | PASS |
| Integrated milestone acceptance | `REVIEW_AND_HANDOFF.md`, `GITHUB_STATE.md` | PASS |
| RED corrective work | `REVIEW_AND_HANDOFF.md`, `GITHUB_STATE.md` | PASS |
| GREEN checkpoint/head/evidence/handoff/done | `REVIEW_AND_HANDOFF.md`, `GITHUB_STATE.md` | PASS |
| Cumulative handoff contents and fresh-session sufficiency | `REVIEW_AND_HANDOFF.md`, `templates/HANDOFF.md` | PASS |
| Proven/fallback Codex-post → ChatGPT-reply → correlated read model | `CHATGPT_CODEX.md` | PASS |
| Requirement coverage to milestone/card/OpenSpec | `PLANNING.md` | PASS |
| Research/source verification and alternative analysis | `RESEARCH.md` | PASS |
| Pre-implementation audit topics | `PLANNING.md`, `EXECUTION_PREP.md` | PASS |
| Near-term detailed / distant non-frozen cards | `TASK_CARDS.md`, `PLANNING.md` | PASS |
| Context minimization | `CONTEXT_ROUTING.md` | PASS, generalized by v3 |
| Optional/non-canonical local `current.md` | `PROJECT_REPOSITORY.md`, `GITHUB_STATE.md`, `EXECUTION.md` | PASS |
| Branch/PR/finalization policy | `PROJECT_REPOSITORY.md`, `REVIEW_AND_HANDOFF.md` | PASS |
| User is decision-maker, not message bus | `CHATGPT_CODEX.md` | PASS |
| Fresh-context recovery | `CONTEXT_ROUTING.md`, `EXECUTION.md` | PASS |
| Failure recovery continues same card | `EXECUTION.md`, `GITHUB_STATE.md` | PASS |
| Anti-overengineering | `CODEX_ORCHESTRATION.md`, `TASK_CARDS.md` | PASS |
| Independent system verification gate | `REVIEW_AND_HANDOFF.md` | PASS |
| Runbook/Task-Card-driven cutover/migration | `REVIEW_AND_HANDOFF.md` | PASS |
| Green-boundary legacy topology migration | `PROJECT_REPOSITORY.md` | PASS |

## v3-mandated semantic additions / supersessions

| v3 decision | Authority | Result |
|---|---|---|
| Workflow repo contains workflow only | `PROJECT_REPOSITORY.md`, root `CHATGPT.md` | PASS |
| One project = one repository from first idea | `PROJECT_REPOSITORY.md` | PASS |
| No default central planning/workspace/control repo | `PROJECT_REPOSITORY.md` | PASS |
| Explicit project knowledge-state separation | `PROJECT_REPOSITORY.md` | PASS |
| Brainstorming is not decision | `BRAINSTORMING.md`, `CONTEXT_ROUTING.md` | PASS |
| Root project `PROJECT.md` as router | `PROJECT_REPOSITORY.md`, `templates/PROJECT.md` | PASS |
| Phase-aware progressive disclosure | `CONTEXT_ROUTING.md` | PASS |
| Small workflow `CHATGPT.md` entrypoint | root `CHATGPT.md` | PASS |
| Workflow current `main` outranks stale prompt/memory/ZIP | root `CHATGPT.md`, `README.md` | PASS |
| Selective loading by phase | `CONTEXT_ROUTING.md` | PASS |
| Bounded Codex multi-agent delegation | `CODEX_ORCHESTRATION.md` | PASS |
| Event-driven wait / no routine polling | `CODEX_ORCHESTRATION.md` | PASS |
| Normal completion path, rare material push only | `CODEX_ORCHESTRATION.md` | PASS |
| No routine progress chatter / no waking Main | `CODEX_ORCHESTRATION.md` | PASS |
| Timeout is not a polling excuse | `CODEX_ORCHESTRATION.md` | PASS |
| Main is orchestrator, not manual worker manager | `CODEX_ORCHESTRATION.md` | PASS |
| Short normal ChatGPT prompt, no required skill/Custom GPT/Work | `prompts/CHATGPT_START.md` | PASS |

## Reverse consistency audit: v3 ↔ v3

Question: do v3 documents create contradictory authority, state or lifecycle rules?

### Authority

- Workflow authority is consistently current workflow `main`.
- Project-specific truth is consistently stored only in the project repository.
- `PROJECT.md` is consistently a router, not a higher-authority copy of detailed artifacts.
- Accepted decisions/requirements outrank brainstorming.
- Codex may reconcile implementation detail, but cannot silently rewrite strategic/product contracts.

**Result: PASS.**

### Repository/path model

Normative v3 documents use:
- `decisions/` for accepted decisions;
- `requirements/` for canonical requirements;
- `planning/` for approved plan;
- `implementation/` for live execution state/evidence/blockers;
- `project-handoffs/` for cumulative handoffs;
- `openspec/` for OpenSpec.

Old `docs/implementation/...` and `docs/project-handoffs/...` paths occur only in migration/history documentation, not as current normative paths.

**Result: PASS.**

### State model

All normative contracts use:
- card execution: `planned | ready | in_progress | blocked | done | superseded`;
- decision state: `accepted | deferred | rejected | review`;
- milestone normal lifecycle: `planned → ready → in_progress → done` with explicit blocked/superseded exceptions.

No competing terminal-state definition was found.

**Result: PASS.**

### Card, milestone and evidence coupling

- Task Card template contains Refresh Gate, strategic escalation, Result and Definition of Done.
- Task Board template exposes result pointers and milestone terminal pointers.
- Acceptance Evidence and Handoff templates contain exact Git state.
- `done` invariants agree across Task Card and GitHub State contracts.

**Result: PASS.**

### OpenSpec coupling

OpenSpec remains selective, JIT and subordinate to accepted requirements/plan while binding implementation behavior when applicable. Task Cards and OpenSpec tasks remain distinct.

**Result: PASS.**

### Strategic communication

All current normative references require matching `request_id` plus `DECISION FOR CODEX:` and durable persistence. No document authorizes arbitrary latest-chat text as a decision.

**Result: PASS.**

### Context routing

Progressive disclosure only changes what is loaded, not what rules exist. Every phase has an explicit route and execution/recovery loads the full contracts it needs.

**Result: PASS.**

### Codex orchestration

Event-driven worker coordination does not weaken Task Card/GitHub-state accountability: Main still integrates and verifies worker output before card close.

**Result: PASS.**

## Static sanity checks

- Project-specific example names from the v2.1 Paperless example are absent from normative v3 files.
- No normative v3 document points at the old `docs/implementation/` or `docs/project-handoffs/` layout.
- `templates/TASK_BOARD.yaml` parses as YAML.
- Required v3 router, phase, contract, template and prompt files are present.
- `MIGRATION_AUDIT_v2.1_to_v3.md` reports 0 unmapped significant elements and 0 unjustified removals.

## Final conclusion

**PASS.** After the second semantic and cross-document audit, no v2.1 behavior/constraint/obligation/exception/recovery/authority rule was found that became unrecoverable in v3, except where the migration prompt explicitly supersedes repository topology, canonical paths or context-routing behavior. No internal v3 contradiction requiring a product decision was found.
