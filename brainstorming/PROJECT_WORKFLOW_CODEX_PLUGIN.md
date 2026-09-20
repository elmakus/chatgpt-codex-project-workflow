# Brainstorm — Project Workflow Codex plugin

Date: `2026-09-20`
Scope ID: `project-workflow-codex-plugin`
Revision: `R1`
Status: `ready_for_definition`

## Problem / goal

Make Project Workflow available to Codex as a Git-backed plugin that can be enabled per repository. When enabled, Codex should consistently work through Project Workflow without requiring the user to restate that rule on every turn, while loading only the workflow material needed for the current route.

## Current understanding

### Verified facts

- Project Workflow's canonical Codex policy already lives under `workflow/codex_only/` on the Project Workflow repository `main`.
- The repository itself currently executes under `execution_policy: chatgpt_only`; this feature packages behavior for Codex consumers and does not change that policy.
- Codex plugin packaging supports plugin-owned Skills.
- The existing `newproject-skill` work established a working Git-backed plugin/Skill distribution pattern.
- Workstation already owns a global marketplace updater and refreshes configured Git-backed marketplaces; individual plugins do not need their own updater.
- Project Workflow already treats `#issue` and `#feature` as explicit operator directives in its routers.

### Explicit user/product choices

1. Keep the plugin in `elmakus/chatgpt-codex-project-workflow`; do not create a second repository solely for Project Workflow plugin packaging unless implementation evidence proves a hard packaging constraint.
2. `workflow/codex_only/*` remains canonical workflow authority. The Skill must be a thin wrapper/bootstrap, never a manually synchronized copy of that policy.
3. Changes inside normal Codex-only workflow modules must not require editing the Skill unless the bootstrap/entry protocol itself changes.
4. Distribute the plugin through the existing Git-backed Codex marketplace model and let the Workstation global updater refresh it with other marketplaces.
5. Installation/enablement is per repo/project. A repo without the plugin must not accidentally become governed by Project Workflow.
6. Prefer an always-on lightweight reminder/activation mechanism so an enabled repo keeps Project Workflow active across ordinary messages and long sessions without repeatedly loading the whole workflow.
7. Preserve short operator UX. Prefer existing `#issue` and `#feature` if practical verification shows they route reliably. If not, use one `$pw` Skill with arguments such as `$pw issue ...` / `$pw feature ...`; do not create three duplicate Skills merely for aliases.
8. Keep `$pw` as the manual/fallback Project Workflow entrypoint.
9. Reuse qualified generic plugin-platform evidence and verify only the delta introduced by Project Workflow rather than re-certifying the whole marketplace/install/updater stack.

### Architecture direction

Preferred conceptual shape:

```text
chatgpt-codex-project-workflow/
├── plugin manifest
├── skills/
│   └── pw/
│       └── SKILL.md          # thin wrapper/bootstrap only
├── plugin activation/reminder surface
└── workflow/
    ├── CONTEXT_ROUTING.md
    ├── common/
    └── codex_only/           # canonical source of truth
```

Runtime flow:

```text
repo with plugin enabled
        ↓
small always-on activation/reminder
        ↓
resolve Project Workflow entry
        ↓
PROJECT.md / policy routing
        ↓
workflow/codex_only/ROUTER.md
        ↓
load only selected route modules
        ↓
load exact durable authority/evidence
```

### Activation direction

A thin repository instruction surface and/or plugin hooks may be used to keep Project Workflow active. The desired behavior is stronger than heuristic Skill discovery alone.

The final mechanism is an implementation choice constrained by these outcomes:

- enabled repo consistently enters Project Workflow;
- reminder/bootstrap context stays very small;
- full workflow files are not loaded on each prompt;
- resume/compaction does not silently lose the workflow invariant;
- installation trust/security behavior is explicit and testable.

### Operator-directive UX verification

Implementation must compare at least:

```text
#feature <goal>
#issue <problem>
```

against the explicit Skill fallback:

```text
$pw feature <goal>
$pw issue <problem>
```

The accepted user-facing convention after testing is:

- keep `#feature` / `#issue` when they are reliably equivalent for intake routing;
- otherwise document and use `$pw feature` / `$pw issue`;
- keep `$pw` as a general explicit entry/recovery invocation.

## Alternatives considered

### Separate plugin repository

Not preferred. It creates another synchronization boundary and increases the chance of workflow/plugin drift.

### Skill-only without always-on bootstrap

Not preferred as the primary guarantee because implicit Skill selection alone is weaker than the desired invariant that an enabled repository always uses Project Workflow.

### Copy Codex-only policy into SKILL.md

Rejected. It would create duplicate workflow authority and require manual synchronization.

### Three Skills: pw / pw-issue / pw-feature

Not preferred. One wrapper Skill plus arguments avoids duplicate entry logic.

### Full workflow in AGENTS.md or other always-loaded instructions

Rejected. It wastes context and defeats progressive disclosure.

## Research needed

No Definition-blocking research is required.

Implementation must verify:
- exact portable-plugin packaging/path layout accepted by the current Codex runtime;
- whether the preferred always-on behavior is best realized by plugin hooks, a tiny repo instruction surface, or a minimal combination;
- wrapper access to canonical workflow files inside the installed plugin root;
- reliability of `#issue/#feature` versus `$pw issue/$pw feature`;
- update propagation from changed canonical `workflow/codex_only/*` content without requiring Skill edits.

## Open questions

None require user authority before Definition. The mechanism choice is delegated to implementation so long as the accepted behavior and UX fallback contract are satisfied.

## Outcome of this session

- Tentative conclusions: one same-repo Git-backed plugin, one thin `$pw` wrapper Skill, canonical `workflow/codex_only/*`, small always-on activation/reminder, progressive disclosure, baseline-evidence reuse.
- Explicit user/product choices to promote through Project Definition: all choices listed above.
- Research still needed: implementation verification only.
- Open questions: none that materially alter Definition.
- Next phase/action: `ready for definition`
- Definition promotion authorization: `user_authorized`
- Definition promotion subject: `project-workflow-codex-plugin@R1`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
