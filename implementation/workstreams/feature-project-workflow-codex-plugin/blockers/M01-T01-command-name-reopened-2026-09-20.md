# M01-T01 Definition Blocker — explicit command name reopened

Date: 2026-09-20
Card: `M01-T01 — Verify current Codex plugin activation contract`
Classification: `user/product authority reopened; hard current Skill-name constraint`
Route: `Project Definition → user decision`

## Trigger

After `PWCP-P2` was approved and M01-T01 had been frozen for independent review, user/product authority changed the desired explicit command from `$pw:pw` to:

`$pw:project_workflow`

Rationale from the user: typing `$pw` already causes Codex to suggest the full namespaced Skill, so a longer descriptive suffix is preferable for readability.

The prior M01-T01 pending review subject `d235e11c78e732d7c06ba4e3a6233c490d6181b3` is therefore obsolete for Card completion and must not be independently reviewed as the current target.

## Verified current constraint

Current Project Workflow runtime evidence already established the bundled-Skill identity shape:

`<plugin-name>:<skill-name>`

Current official Codex/OpenAI Skill creation validation requires Skill names to use lowercase letters, digits and hyphens only (hyphen-case). Underscores are not accepted in normal Skill names.

Therefore Skill name `project_workflow` is not a valid normal bundled-Skill name under the current standard validation contract.

The directly normalized normal bundled-Skill candidate is:

- plugin: `pw`
- Skill: `project-workflow`
- explicit command: `$pw:project-workflow`

This preserves the user's intended `$pw` autocomplete prefix and gives the readable descriptive suffix, while staying inside the normal bundled-Skill naming contract.

## Authority impact

- The user has reopened the explicit-command choice, so `$pw:pw` must not be treated as the settled final UX for further M01 completion/M02 implementation.
- The exact requested underscore spelling `$pw:project_workflow` conflicts with the current normal Skill naming constraint.
- Existing M01 packaging, activation, trust, path-resolution, isolation and namespacing evidence remains historical valid evidence; only the explicit Skill-name choice is reopened.
- The approved `PWCP-P2` plan is no longer executable as-is for the affected command-name clauses and will require a new plan revision after Definition is resolved.

## User decision required

Choose whether to accept the normal hyphen-case command:

`$pw:project-workflow`

If the underscore spelling `$pw:project_workflow` must be retained exactly, further research/architecture work is required for a nonstandard explicit-entry surface outside the normal Skill-name contract.

No implementation or independent M01 review should proceed until this Definition-owned choice is resolved.
