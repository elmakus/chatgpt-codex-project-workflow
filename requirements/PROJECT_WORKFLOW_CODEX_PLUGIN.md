# Project Workflow Codex Plugin Requirements

Revision: `R2`
Status: `approved`
Updated: `2026-09-20`

## Goal / target state

Project Workflow is distributable as a Git-backed Codex plugin that can be enabled per repository/project. In an enabled repository, Codex consistently enters and follows the canonical Project Workflow while loading only the route-specific workflow and authority needed for the current obligation.

The plugin is packaging/activation around the existing Project Workflow repository. It must not become a second implementation of `workflow/codex_only/*`.

## Product / system requirements

| ID | Requirement | Priority | Source / decision | Status |
|---|---|---|---|---|
| PWCP-REQ-001 | Package Project Workflow as a Codex plugin from the existing `elmakus/chatgpt-codex-project-workflow` repository unless a verified hard platform constraint makes that impossible. | MUST | brainstorming R1 / ADR-PWCP-001 | accepted |
| PWCP-REQ-002 | Keep `workflow/codex_only/*` and normal Project Workflow routing files as canonical authority; plugin Skill/bootstrap content must not duplicate policy semantics that then require manual synchronization. | MUST | brainstorming R1 / ADR-PWCP-001 | accepted |
| PWCP-REQ-003 | Provide exactly one normal explicit Project Workflow bundled-Skill entrypoint. Under the verified current Codex namespacing contract, use plugin name `pw` + Skill name `pw`, exposed as `$pw:pw`. | MUST | brainstorming R1 / ADR-PWCP-002 / runtime evidence 2026-09-20 / user decision 2026-09-20 | accepted |
| PWCP-REQ-004 | Enabling the plugin for a repository must establish a lightweight always-on Project Workflow invariant for ordinary user prompts; the user must not have to invoke `$pw` on every message. | MUST | brainstorming R1 / ADR-PWCP-002 | accepted |
| PWCP-REQ-005 | The always-on bootstrap/reminder must remain small and must route into canonical workflow progressive disclosure instead of preloading the complete workflow tree. | MUST | brainstorming R1 / ADR-PWCP-002 | accepted |
| PWCP-REQ-006 | The enabled-repository invariant must survive normal fresh session entry and supported resume/compaction lifecycle behavior without silently dropping Project Workflow. | MUST | brainstorming R1 / ADR-PWCP-002 | accepted |
| PWCP-REQ-007 | A repository/project without the plugin enabled must not be implicitly placed under Project Workflow by this feature. | MUST | brainstorming R1 | accepted |
| PWCP-REQ-008 | Preserve `#issue` and `#feature` as the preferred user-facing intake directives if end-to-end verification proves they are reliably recognized under the always-on plugin path. | SHOULD | user choice | accepted |
| PWCP-REQ-009 | If `#issue` / `#feature` are not reliably equivalent to explicit Skill routing, the supported fallback UX must be the one bundled Skill with arguments: `$pw:pw issue ...` and `$pw:pw feature ...`; do not introduce separate duplicate issue/feature Skills merely for aliases. | MUST | user choice + current Codex naming constraint accepted 2026-09-20 | accepted |
| PWCP-REQ-010 | Keep `$pw:pw` as the general explicit entry/recovery/debug path on the verified current Codex bundled-Skill naming contract, regardless of which intake-directive UX wins verification. | MUST | user choice + current Codex naming constraint accepted 2026-09-20 | accepted |
| PWCP-REQ-011 | Use the existing Git-backed Codex marketplace distribution/update model. Individual Project Workflow plugin content must not implement its own marketplace updater. | MUST | existing platform baseline | accepted |
| PWCP-REQ-012 | Reuse previously qualified generic marketplace/plugin/Skill/update evidence where the mechanism is unchanged; verify the Project Workflow-specific delta rather than re-certifying the entire platform stack. | MUST | user choice | accepted |
| PWCP-REQ-013 | Verify that a change to canonical `workflow/codex_only/*` content becomes visible through the installed/updated plugin without requiring a corresponding Skill edit when the bootstrap contract itself did not change. | MUST | source-of-truth invariant | accepted |
| PWCP-REQ-014 | Installation/trust behavior for any plugin hook or equivalent activation mechanism must be explicit, deterministic and testable. | MUST | activation constraint | accepted |
| PWCP-REQ-015 | Plugin activation must route through project `PROJECT.md` / Project Workflow policy routing and therefore honor the selected execution policy rather than hard-coding all consumers directly to one policy module. | MUST | existing workflow authority | accepted |

## Constraints

- The workflow repository itself remains on `execution_policy: chatgpt_only`; this feature does not change that project-level policy.
- Current Project Workflow authority precedence and durable-state rules remain unchanged.
- Generic Codex plugin distribution/update behavior already proven by platform evidence should be referenced, not redundantly rebuilt.
- Always-on activation may use Codex plugin hooks, a very small repository instruction surface, or a minimal combination, but the chosen mechanism must meet PWCP-REQ-004 through PWCP-REQ-006 and PWCP-REQ-014.
- The plugin must work with progressive disclosure: bootstrap → policy/router → current route module(s) → exact durable authority/evidence.

## Non-goals

- Creating a second repository solely to mirror Project Workflow plugin files.
- Copying `workflow/codex_only/*` into `SKILL.md`.
- Creating a separate updater/timer for this plugin.
- Creating three independent Skills only to provide `pw`, issue and feature aliases.
- Building a Project Workflow MCP execution engine in this scope.
- Replacing existing Project Workflow durable repository state with plugin-local state.
- Changing the workflow repository's own accepted execution policy.

## Global invariants

1. One canonical workflow source: normal Project Workflow files in this repository.
2. Plugin bootstrap and Skill are routing/activation surfaces, not parallel workflow authority.
3. Per-repo opt-in is explicit.
4. Progressive disclosure is preserved.
5. Generic qualified platform evidence is reusable; new behavior receives delta verification.
6. Short operator UX is preserved when reliability permits it; the verified current bundled-Skill command is `$pw:pw`.

## External contracts / dependencies

- Current Codex portable plugin/Skill format and supported lifecycle hooks/instruction surfaces.
- Existing Git-backed Codex marketplace configuration used by the Workstation.
- Workstation marketplace updater, which refreshes configured Git marketplaces independently of LLM sessions.
- Existing Project Workflow `PROJECT.md`, `workflow/CONTEXT_ROUTING.md` and selected policy routers.

## Acceptance-level requirements

The feature is acceptable only when evidence demonstrates all applicable outcomes:

1. The plugin can be installed/enabled from its Git-backed marketplace source and its one `$pw:pw` bundled Skill is discoverable.
2. A normal prompt in an enabled test repository enters Project Workflow without explicit `$pw` invocation.
3. The always-on reminder/bootstrap is bounded and does not cause the complete workflow tree to be loaded on each prompt.
4. Fresh session and supported resume/compaction scenarios preserve the Project Workflow invariant.
5. `$pw:pw` explicitly enters/re-enters the workflow.
6. `#feature` and `#issue` are tested end-to-end against `$pw:pw feature` and `$pw:pw issue`; durable usage docs record the verified convention.
7. A control repository without the plugin remains unaffected.
8. The wrapper resolves and reads canonical workflow files from the installed plugin package.
9. A canonical Codex-only workflow-module change propagates through normal marketplace/plugin update without a Skill edit when bootstrap semantics are unchanged.
10. Generic marketplace/update tests are reused by evidence reference; only genuinely new Project Workflow-specific behavior is retested.
11. Trust/review behavior required by the selected activation mechanism is documented and validated.

## Definition completeness

- Target state and material MUST requirements are explicit.
- Scope boundaries and non-goals are explicit.
- Strategic same-repository/canonical-source and activation architecture choices are recorded in accepted decisions.
- No unresolved user/product choice can materially alter milestone architecture.
- Exact current Codex packaging/hook details and directive reliability are implementation verification items bounded by acceptance requirements, not Definition blockers.

## Downstream coverage

Planning must map every PWCP requirement to one or more milestones and planned work packages/JIT verification. Execution Prep must create concrete Cards before implementation.
