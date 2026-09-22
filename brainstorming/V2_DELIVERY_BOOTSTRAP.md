# Brainstorming — V2 Delivery / Bootstrap Surfaces

Date: 2026-09-22
Scope: common-preexecution-core@R1
Status: active analysis
Production authority: none

## User direction

V2 should be delivered through two runtime-appropriate surfaces while preserving one semantic Project Workflow:

1. **Normal ChatGPT**
   - user creates/uses a ChatGPT Project;
   - Project Instructions contain a small bootstrap saying the project uses Project Workflow V2 and points to the GitHub workflow repository;
   - ChatGPT reads the workflow rules from that repository.

2. **Codex**
   - Project Workflow is packaged as a Codex plugin/Skill and installed/enabled for the target repository;
   - Codex reads the bundled workflow tree from the installed plugin package;
   - ordinary Codex operation should not enter/fetch the remote Project Workflow repository merely to obtain workflow policy.

This is distribution/bootstrap separation, not two semantic workflows.

## Existing V1 evidence

The repository already contains:
- `.codex-plugin/plugin.json`;
- `skills/project-workflow/SKILL.md`;
- repository-local plugin enablement guidance;
- `hooks/session-start.py` + `hooks/hooks.json`;
- `docs/CODEX_PLUGIN.md`;
- `prompts/CHATGPT_PROJECT_INSTRUCTIONS.md`.

The current Codex plugin already bundles the canonical `workflow/` tree and its SessionStart hook resolves `PLUGIN_ROOT` and points Codex at the bundled router.

Therefore V2 should evolve the existing packaging rather than invent a second delivery system.

## Target architecture — one semantics, two bootstrap sources

### Semantic contract

Project Workflow V2 has one common semantic workflow/state machine.

The active project repository contains project truth and a small declaration that it uses Project Workflow V2. It does **not** select `chatgpt_only` versus `codex_only` semantics.

Runtime/product source selection is not project authority.

### ChatGPT bootstrap

ChatGPT Project Instructions are a thin external bootstrap.

They should say, conceptually:

```text
This project uses Project Workflow V2 from elmakus/chatgpt-codex-project-workflow.
For normal ChatGPT, use the workflow repository as the workflow-instruction source.
Read the V2 ChatGPT bootstrap/router from that repository, then read this project's PROJECT.md and continue from durable project state.
Do not copy the full workflow into Project Instructions.
```

The exact repository/ref/version policy remains to be decided.

### Codex bootstrap

The installed/enabled Project Workflow plugin is the Codex instruction source.

SessionStart / Skill should say, conceptually:

```text
Project Workflow V2 is enabled through this installed plugin.
Read workspace PROJECT.md as project truth.
Read Project Workflow semantics from this plugin's bundled workflow tree under PLUGIN_ROOT.
Do not fetch or enter the remote Project Workflow GitHub repository merely to obtain workflow instructions.
If the required bundled V2 workflow is missing/incompatible, fail closed as a plugin installation/version problem rather than reconstructing policy from GitHub or memory.
```

The Skill remains thin. It should not duplicate policy.

### No runtime self-detection

Do not make common Project Workflow ask:
- "am I ChatGPT or Codex?";
- whether a subagent API exists as a proxy for product identity;
- whether a repository can be fetched as a proxy for surface identity.

The bootstrap surface already establishes where workflow instructions come from.

After bootstrap, common Project Workflow uses capabilities for realization decisions where appropriate, not product identity for semantic routing.

## Project repository contract

Recommended project-side shape:

```yaml
project_workflow:
  contract: v2
```

Exact syntax is tentative.

The project repository should not need:
- `execution_policy: chatgpt_only | codex_only`;
- a durable workflow-source path selecting GitHub versus plugin;
- a runtime/model/session identity.

The ChatGPT Project Instructions and Codex plugin provide their own delivery source.

## Failure behavior

Recommended:
- ChatGPT cannot access/resolve the required workflow repository/ref -> fail closed and report the smallest access/source problem; do not invent workflow semantics from memory.
- Codex plugin missing/disabled/incomplete -> fail closed with plugin enable/install/update remediation; do not silently fall back to reading the remote workflow repository.
- project durable state remains usable after switching runtime because semantic state is common.

## Cross-runtime portability

A ChatGPT-created workstream may later be continued by Codex and vice versa without converting project state.

Only the instruction delivery source changes:
- ChatGPT reads V2 workflow from the workflow repository;
- Codex reads V2 workflow from installed plugin package.

The same durable workstream/Task Board/review/recovery contracts are consumed.

## Version-skew problem

One material question remains:

ChatGPT may read the latest workflow repository while Codex may have an older installed plugin bundle.

Silent semantic skew would undermine cross-runtime portability.

Candidate strategies:

A. **Current-main everywhere**
- ChatGPT reads current main;
- Codex is expected to keep plugin marketplace upgraded to current main.
- Simple, but an installed plugin may lag silently.

B. **Released workflow version**
- project declares a V2 workflow release/compatibility version;
- ChatGPT reads that release/tag;
- Codex plugin exposes the matching packaged release;
- incompatible/missing version fails closed.
- Stronger reproducibility, slightly more release/version machinery.

C. **Major contract + compatible patch drift**
- project declares only contract major `v2`;
- bootstrap package declares its compatible V2 version;
- patch/minor-compatible changes may differ;
- breaking semantic changes require a new contract major.
- Lower operational friction but requires explicit compatibility discipline.

Recommendation for grilling: C, unless exact reproducibility proves more valuable than simplicity.

## Scope boundary

This bootstrap/delivery design is not a return to policy-local semantic branches.

Two bootstrap files/surfaces are expected and healthy:
- ChatGPT-specific **instruction acquisition**;
- Codex-specific **instruction acquisition**.

Everything after acquiring the common V2 router/contract should converge on common semantics, except intentionally surface-owned UX/runtime realization such as:
- premium-model human handoffs;
- Codex internal worker orchestration;
- ChatGPT user-facing fresh-context handoff where explicitly required.


## Grilling decisions — one product, thin plugin delivery

User clarified and accepted the intended maintenance model:

1. **Project Workflow V2 is one product/authority.**
   - Canonical workflow semantics live once in the V2 workflow tree in this repository.
   - The Codex plugin packages/bundles that same tree.
   - The plugin is not a second independently maintained implementation of Project Workflow.

2. **Normal workflow changes must not require plugin-bootstrap edits.**
   - changing V2 routing/state/review/execution/close semantics changes only the canonical V2 workflow files;
   - after the user updates the installed Codex plugin, Codex receives that updated bundled workflow automatically;
   - edit the plugin manifest, Skill or SessionStart hook only when the bootstrap/package contract itself changes.

3. **ChatGPT Project Instructions are user-owned external configuration.**
   - the workflow repository may provide the recommended minimal text/template;
   - Project Workflow cannot mutate the user's ChatGPT Project Instructions;
   - do not put self-referential instructions such as "do not copy the whole workflow into Project Instructions" inside the text intended for the user's Project Instructions unless it serves an actual runtime purpose.

4. **Version skew is not currently a design priority.**
   - the user's Codex plugins auto-update periodically;
   - after important Project Workflow changes the user will manually force an update;
   - do not add project-level version pinning/schema machinery solely for this operational concern in V2 unless future evidence requires it.

5. **Codex installation model**
   - Project Workflow plugin is installed globally for the user's Codex environment;
   - the user wants an explicit Skill entry named conceptually `project_workflow_v2`;
   - intended user invocation is a short explicit Project Workflow V2 skill marker (current package namespace convention to be validated by implementation tests);
   - the plugin/Skill resolves the bundled V2 workflow under its package root and never treats the remote workflow repository as its ordinary policy source.

## Maintenance invariant

Target invariant:

```text
edit canonical Project Workflow V2 semantics
-> commit/publish repository
-> update Codex plugin package
-> installed plugin now contains the same latest V2 semantics
```

No duplicate semantic copy or manual synchronization step is allowed.

The Skill/hook must stay thin and stable:
- locate package root;
- locate project repository/durable state;
- enter the common V2 router;
- fail closed if the bundled workflow is missing/broken.

They must not restate stage logic, review rules, routing priorities or execution policy.

## Shared human phrase

The user wants the human-facing phrase "use project_workflow_v2" to mean the same workflow regardless of surface.

Target interpretation:
- in a ChatGPT Project, the Project Instructions establish that `project_workflow_v2` is loaded from the linked GitHub workflow repository;
- in Codex, the installed plugin/Skill establishes that `project_workflow_v2` is loaded from the bundled plugin package;
- after bootstrap, both enter the same common V2 semantics and consume the same project durable state.

The phrase itself is not used for runtime self-detection. Each surface's bootstrap resolves its own instruction source.
