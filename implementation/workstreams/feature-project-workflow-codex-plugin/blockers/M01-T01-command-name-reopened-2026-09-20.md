# M01-T01 Definition Blocker — explicit command name reopened

Date: 2026-09-20
Card: `M01-T01 — Verify current Codex plugin activation contract`
Classification: `resolved Definition correction; hard current Skill-name constraint honored`
Route: `Project Definition → Planning`
Status: `resolved`

## Trigger

After `PWCP-P2` was approved and M01-T01 had been frozen for independent review, user/product authority changed the desired explicit command from `$pw:pw` to:

`$pw:project_workflow`

Rationale from the user: typing `$pw` already causes Codex to suggest the full namespaced Skill, so a longer descriptive suffix is preferable for readability.

The prior M01-T01 pending review subject `d235e11c78e732d7c06ba4e3a6233c490d6181b3` is therefore obsolete for Card completion and must not be independently reviewed as the current target.

## Verified current constraint

Current Project Workflow runtime evidence already established the bundled-Skill identity shape:

`<plugin-name>:<skill-name>`

Current official Codex/OpenAI Skill creation validation requires Skill names to use lowercase letters, digits and hyphens only (hyphen-case). Underscores are not accepted in normal Skill names. Exact verified source: `openai/codex@5c5308fc9a9ee789049d646ef11e5400384b9c6f`, `codex-rs/skills/src/assets/samples/skill-creator/scripts/quick_validate.py`, validation regex `^[a-z0-9-]+# M01-T01 Definition Blocker — explicit command name reopened

Date: 2026-09-20
Card: `M01-T01 — Verify current Codex plugin activation contract`
Classification: `resolved Definition correction; hard current Skill-name constraint honored`
Route: `Project Definition → Planning`
Status: `resolved`

## Trigger

After `PWCP-P2` was approved and M01-T01 had been frozen for independent review, user/product authority changed the desired explicit command from `$pw:pw` to:

`$pw:project_workflow`

Rationale from the user: typing `$pw` already causes Codex to suggest the full namespaced Skill, so a longer descriptive suffix is preferable for readability.

The prior M01-T01 pending review subject `d235e11c78e732d7c06ba4e3a6233c490d6181b3` is therefore obsolete for Card completion and must not be independently reviewed as the current target.

## Verified current constraint

Current Project Workflow runtime evidence already established the bundled-Skill identity shape:

`<plugin-name>:<skill-name>`

.

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

## Resolution

User/product authority explicitly accepted the normal hyphen-case command on 2026-09-20:

`$pw:project-workflow`

Canonical explicit-entry identity is therefore:

- plugin: `pw`
- Skill: `project-workflow`
- command: `$pw:project-workflow`

The previous `$pw:pw` choice and the obsolete M01-T01 review subject remain historical provenance only. Definition must be revised and Planning must create a new plan revision before M01 can resume.
