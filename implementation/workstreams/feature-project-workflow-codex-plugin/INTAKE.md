# Feature Intake — Project Workflow Codex plugin

## Identity

- Workstream ID: `feature-project-workflow-codex-plugin`
- Intake kind: `feature`
- Branch: `feat/project-workflow-codex-plugin`
- Integration target: `main`
- Base ref: `cdaf47245e45836917b152904d70807bca355e7d`

## Operator intent

Package the existing Project Workflow repository as a Git-backed Codex plugin installable per project/repository, using the same marketplace distribution channel and Workstation marketplace updater model already used for other Codex plugins.

The plugin must make Project Workflow the normal operating contract for repos where it is enabled while preserving progressive disclosure and avoiding repeated loading of the full workflow tree.

## Pre-creation discovery

- No existing Project Workflow Codex-plugin workstream/branch was found.
- Existing unrelated workstreams do not provide parent-only state required by this feature.
- The feature builds on Project Workflow behavior already present on `main`, including the dedicated `workflow/codex_only/` policy namespace.
- Classification: independent workstream based on normal integration target `main`.

## Existing platform baseline to reuse

The feature is allowed to reuse already-qualified evidence for the generic Codex plugin distribution path rather than re-prove it from zero:

- Git-backed Codex marketplace distribution;
- portable plugin manifest/install mechanics;
- plugin-to-Skill discovery;
- marketplace upgrade;
- Workstation global marketplace auto-update.

Project-specific verification remains required for every behavior introduced by this plugin, especially always-on activation, wrapper-to-workflow path resolution, progressive disclosure and operator-directive UX.

## Post-creation classification

- Canonical exploratory record: `brainstorming/PROJECT_WORKFLOW_CODEX_PLUGIN.md`
- Canonical scope: `project-workflow-codex-plugin@R1`
- Path: Brainstorming → Project Definition.
- Research obligation: none before Definition.
- The user explicitly authorized promotion of this exact R1 scope after the concept was agreed.
- Next route: `project_definition:project-workflow-codex-plugin@R1`.

## Intake state

- State: complete
- Downstream owner: `brainstorming/PROJECT_WORKFLOW_CODEX_PLUGIN.md`
