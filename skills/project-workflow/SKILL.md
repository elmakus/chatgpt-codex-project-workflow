---
name: project-workflow
description: Enter or recover Project Workflow by resolving the workspace project contract and delegating to the canonical router.
---

Use this Skill only as a thin Project Workflow entry/recovery bootstrap.

1. Read the active workspace repository's `PROJECT.md` first. It owns the project's execution-policy selection and project-level pointers.
2. Resolve this installed Skill's plugin root (the repository root containing `.codex-plugin/`, `skills/`, and `workflow/`).
3. Read the canonical router at `<plugin-root>/workflow/CONTEXT_ROUTING.md`.
4. Follow the policy selected by that router and load only the route modules, durable state, authority, and evidence required for the current obligation.
5. Recover current truth from durable repository state rather than chat recollection, and continue deterministic authorized transitions until the workflow reaches a real stop.

Do not copy Project Workflow policy into this Skill. Do not hard-code `codex_only` or `chatgpt_only`; the workspace `PROJECT.md` plus the canonical router decide the policy.
