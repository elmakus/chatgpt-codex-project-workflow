# Execution Policy Router

This is the small policy dispatcher referenced by normal ChatGPT Project Instructions.

## Route selection

1. Read project root `PROJECT.md`.
2. Read its accepted `execution_policy`.
3. Follow exactly one route:

### `chatgpt_only`

Read:

`workflow/chatgpt_only/ROUTER.md`

After selecting this route:
- use only `workflow/common/*` and `workflow/chatgpt_only/*` workflow modules;
- do not load legacy/shared execution contracts;
- do not load another policy namespace;
- recover mutable state from the canonical source defined by the selected policy route; for `chatgpt_only`, resolve the selected workstream state context first, then use that workstream's canonical Task Board for implementation/implementation-review state, with `implementation/TASK_BOARD.yaml` retained as the legacy/default fallback. Pre-execution plan-review state lives under `planning/reviews/`.

### Other accepted policy

Until its dedicated policy namespace is migrated, read:

`workflow/legacy/CONTEXT_ROUTING.md`

The legacy route remains authoritative for that policy during this staged migration.

## Policy invariants

`execution_policy` never changes automatically because of a blocker, runtime limitation or convenience. Changing policy requires an explicit user decision.

For a brand-new project with no previously accepted execution policy, default to `chatgpt_only` unless the user explicitly selects another accepted policy.

Once a policy is accepted, a runtime blocker does not silently reroute execution through another policy.

## Missing or inconsistent policy

Do not guess an execution route.

If an accepted policy can be recovered unambiguously from durable project authority, reconcile `PROJECT.md` at the next safe edit and route accordingly.

Otherwise, execution is blocked until the policy is explicitly resolved.

Brainstorming/research/Project Definition that does not depend on executor semantics may continue through policy-neutral common modules when safe.

## Migration invariant

A policy route must not import semantics from another policy merely for convenience.

Shared modules are allowed only when they are genuinely policy-neutral.
