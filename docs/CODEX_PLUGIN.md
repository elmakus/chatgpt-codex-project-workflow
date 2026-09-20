# Codex plugin

Project Workflow is packaged from this repository as the Git-backed Codex plugin `pw`. The package exposes one bundled Skill, `project-workflow`, invoked explicitly as `$pw:project-workflow`, plus a small SessionStart bootstrap that keeps Project Workflow active in repositories where the plugin is enabled.

Verified runtime for the acceptance evidence in this repository: `codex-cli 0.155.0-alpha.9.2`.

## Install the marketplace and plugin

Add this repository as the marketplace source and install the plugin:

```sh
codex plugin marketplace add elmakus/chatgpt-codex-project-workflow --ref main --json
codex plugin add pw@project-workflow --json
```

The marketplace source is the repository root, so the installed package contains the thin Skill/bootstrap and the canonical `workflow/` tree together.

## Keep activation repository-local

Project Workflow is intended to be opt-in per repository. After installation, keep the user-level plugin entry disabled in `~/.codex/config.toml`:

```toml
[plugins."pw@project-workflow"]
enabled = false
```

Then enable it only in each repository that should use Project Workflow by adding this to that repository's `.codex/config.toml`:

```toml
[plugins."pw@project-workflow"]
enabled = true
```

Codex must also trust the repository/hook through its normal trust flow. The SessionStart hook does not run until the current trust condition is satisfied. `--dangerously-bypass-hook-trust` was used only in disposable acceptance probes and is not part of normal setup.

A repository without the local enable override remains unaffected by this plugin.

## Use Project Workflow

In an enabled and trusted repository, ordinary prompts receive the small Project Workflow bootstrap automatically. You do not need to invoke the Skill on every turn.

Use the verified short intake forms:

```text
#feature <description>
#issue <description>
```

Use `$pw:project-workflow` when you want an explicit general entry, recovery or debugging path.

On the accepted current runtime, `$pw:project-workflow feature ...` and `$pw:project-workflow issue ...` did not route equivalently to the canonical `#feature` / `#issue` Intake paths, so they are not documented as supported intake aliases.

## Progressive disclosure and source of truth

The SessionStart hook injects only a bounded routing reminder. It tells Codex to read the workspace `PROJECT.md`, then the installed canonical `workflow/CONTEXT_ROUTING.md`, and load only the selected route modules, durable state, authority and evidence required for the current obligation.

The Skill and hook are routing surfaces, not a second copy of Project Workflow policy. Canonical workflow semantics remain in the normal `workflow/` files in this repository.

## Updates

The plugin contains no updater, timer or poller. Marketplace refresh remains owned by the existing Codex/Workstation Git-backed marketplace mechanism.

For the current Codex CLI, a configured Git marketplace can be refreshed with:

```sh
codex plugin marketplace upgrade project-workflow --json
```

A canonical `workflow/codex_only/*` change is carried by the same repository-root package and does not require a matching Skill edit unless the bootstrap/entry contract itself changes.

## Verification references

The durable acceptance evidence for this package lives under:

- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M01-acceptance-2026-09-20.md`
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M02-acceptance-2026-09-20.md`
- `implementation/workstreams/feature-project-workflow-codex-plugin/evidence/M03-acceptance-2026-09-20.md`

Final release-readiness and requirement coverage are recorded by M04 in the same workstream.
