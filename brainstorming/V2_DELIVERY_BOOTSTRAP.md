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


## Grilling decisions — repository activation boundary and V2 Skill identity

User clarified:

1. Repository-local pinning/enablement of plugins, MCPs and Skills is **out of scope for Project Workflow V2**. The user's separate `newproject-skill` will provision/pin those dependencies into newly created repositories. Project Workflow therefore does not own per-repository Codex plugin activation policy.
2. The official explicit Codex entry is accepted as a short Skill invocation, but it is not required on every prompt when bootstrap/session activation already established Project Workflow.
3. Remove durable `execution_policy: chatgpt_only | codex_only` from the V2 project contract. Runtime/surface may change while consuming the same durable state.

### Codex Skill naming

User clarified the intended Codex namespacing model:
- plugin name: `pw`;
- Skill name: `project_workflow_v2`;
- explicit invocation: `$pw:project_workflow_v2`.

Treat this as the target V2 interface. Acceptance tests during implementation must verify the installed package exposes this exact invocation.

Project Workflow does not need to infer runtime identity from that invocation. The plugin bootstrap already supplies the Codex instruction source.

### Provisioning boundary

Target ownership:

```text
newproject-skill
  -> pins/enables required plugin/MCP/Skill dependencies for repository

Project Workflow V2
  -> assumes its bootstrap surface is available
  -> owns workflow semantics and durable project lifecycle only
```

Do not duplicate new-project provisioning logic inside Project Workflow.


## Grilling decisions — clean V2 repository and canonical workflow tree

User accepted:

1. Every V2 project carries a small durable Project Workflow contract marker in its project state, conceptually `project_workflow: v2`. It identifies the durable-state contract only; it does not identify ChatGPT versus Codex.
2. V2 has exactly one canonical workflow tree consumed by both ChatGPT and Codex. **Because the user intends to create a new clean Project Workflow V2 repository with no legacy/policy-local paths, the canonical path should simply be `workflow/`, not `workflow/v2/`.**
3. Existing legacy projects may be migrated once into V2 rather than forcing V2 to carry permanent `chatgpt_only/codex_only` semantic branches. Migration tooling/reader support may exist as a bounded transition concern, but the new clean V2 repository itself does not need legacy workflow paths.
4. `$pw:project_workflow_v2` is only an entry/recovery Skill. Any accompanying user intent is handed to the common V2 router/intake; the Skill must not grow a second mini-router.

### Clean repository consequence

Target V2 repository shape is conceptually:

```text
project_workflow_v2 repo
├── workflow/          # the one canonical semantic workflow
├── skills/
│   └── project_workflow_v2/
├── hooks/
├── .codex-plugin/
├── prompts/           # thin human/bootstrap helpers only where useful
├── templates/
└── tests/
```

There are no production `workflow/chatgpt_only/`, `workflow/codex_only/`, `workflow/legacy/` or `workflow/v2/` semantic trees in the clean V2 repository.

ChatGPT reads the canonical `workflow/` tree from the GitHub V2 repository.
Codex reads the same canonical `workflow/` tree from its installed plugin package.

The old repository/branches may be used as migration/reference evidence during development, but are not copied forward as permanent production structure.


## Grilling decisions — packaging, clean repo ownership and context economy

User accepted:

1. The Codex plugin packages the **same canonical `workflow/` files directly** from the V2 repository. No generated/copied second semantic tree is maintained for the plugin.
2. Plugin namespace stays short: `pw`. The V2 Skill is named `project_workflow_v2`. Explicit invocation target: `$pw:project_workflow_v2`.
3. A project's `PROJECT.md` declares only the common V2 workflow contract/state. It does not contain the workflow GitHub source URL or plugin package path.
4. Legacy migration belongs in a bounded migration tool/module outside the normal canonical `workflow/` semantics. The common V2 router does not permanently route through V1 policy-local paths.
5. The current `chatgpt-codex-project-workflow` repository becomes historical/development reference once the separate clean V2 repository is production-ready. The production V2 repository is a new clean repository conceptually named `project_workflow_v2`.

## Codex context-economy invariant

The Codex Skill/bootstrap must not become a context hog.

Target behavior:
- SessionStart injects only a very small bounded pointer/reminder;
- `$pw:project_workflow_v2` reads only the minimal bootstrap/router material needed to locate the current obligation;
- router modules use progressive disclosure and load only the exact current stage/module + durable project artifacts + exact authority/evidence refs required for that obligation;
- do not preload all stage files, templates, review contracts, migration docs or historical guidance;
- do not duplicate canonical workflow prose inside `SKILL.md`, SessionStart or plugin metadata;
- once a route is selected, neighboring modules remain unread unless a concrete transition requires them;
- runtime/internal Codex orchestration details stay outside Project Workflow context unless the current operation actually needs them.

The Skill should remain roughly a pointer/entry contract, not a compressed copy of Project Workflow.

### One-product packaging invariant

```text
canonical V2 repo/workflow/
        |
        +--> ChatGPT reads remotely
        |
        +--> Codex plugin bundles same files directly

No second semantic copy.
```

Normal workflow edits therefore update one source tree only.


## Grilling decisions — router as progressive-disclosure index

User accepted:

1. The common V2 router should stay small and own progressive-disclosure routing. Functionally, it replaces the role that a traditional Skill's references/index often plays: the Skill enters Project Workflow, while the router selects the exact workflow module(s) required for the current obligation.
   - Do not create a duplicate `references/` policy tree merely to imitate generic Skill structure.
   - Canonical `workflow/*.md` modules are the referenced material.
2. After route selection, read only the selected stage/module by default. Do not automatically load predecessor/successor modules unless an explicit current-stage dependency/transition requires them.
3. Durable artifacts should carry exact authority/evidence/result refs sufficient to avoid broad scans of `requirements/`, `decisions/`, `research/`, implementation evidence, etc.
4. Do **not** enforce an arbitrary fixed line-count budget for `SKILL.md`. The requirement is semantic/context economy:
   - only bootstrap/location/recovery instructions;
   - no stage logic;
   - no duplicated router rules;
   - no broad reference catalog;
   - as short as practical while remaining robust.
5. Templates, migration material, docs and other support surfaces are outside the ordinary runtime read set and are loaded only on a concrete trigger.

## Progressive disclosure chain

Target:

```text
Codex Skill / ChatGPT bootstrap
  -> small common router
  -> exact current workflow module
  -> exact durable project state
  -> exact authority/evidence refs
```

Not:

```text
Skill
  -> preload all workflow files
  -> preload docs/templates/migration
  -> scan project repository broadly
```

The router therefore acts as the central semantic index and obligation selector for both surfaces.
