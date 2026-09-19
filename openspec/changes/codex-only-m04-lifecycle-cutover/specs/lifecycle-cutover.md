# Specification — codex_only lifecycle cutover

## Requirement: dedicated route

For `execution_policy: codex_only`, root routing MUST select `workflow/codex_only/ROUTER.md` and MUST NOT enter another policy namespace or legacy shared execution route.

### Scenario: policy split

Given projects selecting `chatgpt_only`, `codex_only`, and one non-migrated accepted policy, each routes respectively to ChatGPT-only, Codex-only, and legacy authority.

## Requirement: full lifecycle parity

The Codex-only namespace MUST provide repository-recoverable Intake, Brainstorming, Research, Definition, Planning, plan review, Execution Prep, Execution, Review, Recovery, micro-fix, Workstreams and Close semantics.

### Scenario: feature lifecycle

A feature intake can persist exploration, Research return, explicit Definition promotion, planning/review and implementation/Close obligations without consulting another policy namespace.

### Scenario: micro-fix lifecycle

A qualified issue micro-fix can materialize one bounded Card, complete independent review, run target refresh/final-integration review reconciliation and close without a synthetic milestone.

## Requirement: review/runtime boundary

Formal review MUST remain role/subject based. Tester MUST NOT repair production. Concrete runtime worker/session/model/profile/invocation/resume identity MUST NOT become Project Workflow authority.

## Requirement: M03 compatibility

Workstream target refresh/Close MUST preserve bounded-batch result lineage and MUST treat internal batch integration as distinct from final workstream integration.

## Requirement: workstream integration

Branch-isolated work MUST preserve manifest-selected Task Board identity, independent/stacked dependency semantics, current-target refresh, exact final-review coverage rules and terminal target-side durable recovery.

## Requirement: non-regression

The cutover MUST leave `workflow/chatgpt_only/*` unchanged, leave non-migrated policies on legacy routing, and leave this repository's own `execution_policy: chatgpt_only`.
