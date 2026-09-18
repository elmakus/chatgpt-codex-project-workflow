# Semantic Audit — ChatGPT-only Policy Split POST-SWITCH

Date: 2026-09-18
Base: `main@4476ed77b88adbed77702a193e447a0e520c5440`
Audited branch subject: `refactor/policy-split-chatgpt-only@f1b2b008ff6204456300c8797973f14ed3c4c032`
Verdict: **GREEN**

## Architecture after switch

Normal ChatGPT bootstrap:

```text
CHATGPT.md
→ project PROJECT.md
→ workflow/CONTEXT_ROUTING.md
→ execution-policy route
```

For `execution_policy: chatgpt_only`:

```text
workflow/common/*
+
workflow/chatgpt_only/*
```

The route does not import legacy/shared execution contracts or another policy namespace.

Policies not yet migrated continue through the exact preserved pre-split router at:

`workflow/legacy/CONTEXT_ROUTING.md`

## Isolation audit

Active ChatGPT-only workflow modules were scanned for:
- other policy names;
- pre-assignment capability router semantics;
- project-card concurrency scheduling;
- worker/lane/worktree ownership;
- alternate executor semantics.

Result: **zero semantic hits**.

The only occurrence of the other executor name anywhere in ChatGPT-only supporting material is inside the workflow repository's immutable repository name in a fresh-chat prompt. It is not workflow behavior.

The root bootstrap and policy dispatcher themselves contain zero such semantic hits.

## Legacy preservation audit

The preserved `workflow/legacy/CONTEXT_ROUTING.md` exactly matches the pre-migration `main` router content.

Legacy/shared files required by policies not yet migrated were not edited:
- shared execution core;
- shared execution preparation;
- shared review/handoff;
- shared Task execution/Card/state contracts;
- existing executor adapters/orchestration/handoff modules.

No legacy file was deleted.

## Functional coverage

Verified in the new ChatGPT-only path:

- durable authority precedence;
- strategic planning and Master Plan semantics;
- L1/L2/L3 delegated planning boundaries;
- JIT Card creation/refinement;
- exact authority preservation;
- selective OpenSpec;
- exactly one READY Card active at a time;
- Task Board as sole mutable execution-state authority;
- Refresh Gate;
- no capability inventory/preflight;
- concrete runtime blocker handling;
- bounded scope and DoD;
- material external write readback;
- automatic deterministic Card continuation;
- implementing-chat fresh-review stop;
- fresh independent review;
- GREEN automatic continuation;
- RED same-turn deterministic remediation;
- corrected exact subject returned to `review_state: pending`;
- branch-aware fresh re-review prompt;
- milestone acceptance;
- publication/PR verification;
- cumulative handoff;
- automatic next-milestone continuation;
- recovery without prior chat narrative;
- concise global human control surface.

## Context footprint

Pre-split normal ChatGPT execution core: approximately **3350 words** before project artifacts.

Post-split active ChatGPT-only execution core:
- `CHATGPT.md`: 255
- policy dispatcher: 184
- common authority: 241
- ChatGPT-only router: 415
- ChatGPT-only execution: 651
- ChatGPT-only state: 696

Total: approximately **2440 words** before project artifacts.

This is roughly **27% less always-read workflow text** than the prior already-optimized path, with stronger semantic isolation.

## Bootstrap/template audit

`prompts/CHATGPT_START.md` and `prompts/CHATGPT_PROJECT_INSTRUCTIONS.md` now contain only a live-repository bootstrap and policy-router instruction.

They do not duplicate execution-policy semantics.

The workflow repository name itself naturally remains present in those prompts.

## Deletion decision

**Do not delete legacy/shared execution files in this phase.**

They remain required by policies that have not yet been migrated to dedicated namespaces.

Deletion is deferred until:
1. the remaining policy namespaces are migrated;
2. their semantic audits are GREEN;
3. no live route references the old shared implementation.

## Final verdict

**GREEN.**

The ChatGPT-only path is physically isolated, semantically complete, smaller, and active through the policy-first router without changing or deleting the still-required legacy paths.
