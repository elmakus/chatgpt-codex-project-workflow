# Decision — Project Workflow Codex plugin uses minimal always-on activation plus one explicit Skill

- Decision ID: `ADR-PWCP-002`
- Date: `2026-09-20`
- Status: `accepted`
- Authority: `user/product`
- Supersedes: `none`
- Related requirements: `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md`
- Related milestone/card: `none`

## Context

A normal optional Skill alone does not satisfy the desired repository invariant: when Project Workflow is enabled for a repo, Codex should consistently remember that the repo is governed by Project Workflow without requiring the user to invoke the Skill every turn. Conversely, loading the whole workflow through always-on repository instructions would waste context and weaken progressive disclosure.

The user also wants short issue/feature intake syntax.

## Decision

Use two layers:

1. a minimal always-on activation/reminder surface for repositories where the plugin is enabled; and
2. one explicit concise Project Workflow bundled Skill using the verified current Codex identity `$pw:pw` (plugin `pw` + Skill `pw`), which routes into canonical Project Workflow and can accept subcommands/arguments when needed.

The always-on surface may be implemented using supported plugin hooks, a very small repository instruction mechanism, or the smallest reliable combination proven by implementation evidence. It must not embed full workflow policy.

Prefer existing `#issue` and `#feature` directives when end-to-end tests prove they reliably reach the canonical intake route under this always-on model. If that reliability is not demonstrated, use `$pw:pw issue ...` and `$pw:pw feature ...` as the documented fallback. Do not create separate duplicate Skills merely to provide those aliases.

## Rationale

- always-on behavior protects the repository invariant;
- the small reminder/bootstrap minimizes recurring context cost;
- one Skill keeps the explicit entry surface simple and avoids duplicated command logic;
- existing `#issue/#feature` UX can remain when reliable;
- implementation retains freedom to choose the current Codex mechanism that best satisfies lifecycle/trust constraints.

## Alternatives considered

### Skill-only activation

Rejected as the sole guarantee because implicit Skill selection is not strong enough for the accepted always-on repository invariant.

### Full workflow in AGENTS.md / always-loaded instructions

Rejected due to recurring context waste and authority duplication.

### Hook-only with no explicit Skill

Rejected because a manual/recovery/debug entrypoint remains useful and the accepted UX includes one concise explicit bundled Skill.

### Three Skills (`pw`, `pw-issue`, `pw-feature`)

Rejected as unnecessary duplication.

## Consequences

- Implementation must validate fresh-session/resume/compaction behavior and any trust prompt required by hooks.
- The always-on payload must remain intentionally small.
- Usage docs must record the verified intake syntax after comparing `#issue/#feature` with the `$pw:pw` fallback.
- A failure of one candidate activation mechanism does not permit dropping the always-on invariant; implementation must choose another accepted mechanism or return to Definition if current platform constraints make the invariant impossible.

## Required authoritative updates

- Requirements / Project Definition: `requirements/PROJECT_WORKFLOW_CODEX_PLUGIN.md`.
- Planning: include activation-mechanism verification before final packaging/acceptance.
- Task Card/OpenSpec: materialize current-runtime details during Execution Prep.
- PROJECT.md: point the active workstream to this accepted decision.

## Provenance

- Source discussion/request: user-authorized `project-workflow-codex-plugin@R1`.
- Evidence/research: current Codex plugin/Skill/hook capabilities and existing Project Workflow routing; M01-T01 runtime evidence proved bundled Skills are exposed as `<plugin-name>:<skill-name>` and that plugin `pw` + Skill `pw` yields `$pw:pw`, while literal `$pw` does not invoke the bundled Skill.
- User/product reconciliation: on 2026-09-20 the user explicitly accepted `$pw:pw` as the supported explicit command.
- Strategic `request_id`: none.
- Exact `DECISION FOR CODEX:` marker: none.
- Persisting commit: recorded by Git history.
