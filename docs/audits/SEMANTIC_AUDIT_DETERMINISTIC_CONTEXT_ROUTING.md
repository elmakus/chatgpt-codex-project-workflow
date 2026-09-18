# Semantic Audit — Deterministic Context Routing

Date: 2026-09-18
Base: `main@fab85862b3cb6594f4c2f565680194adaaeda8d3`
Audited branch subject: `docs/deterministic-context-routing@c964315109b30c30f9b65a2ee130a1a62736043f`
Verdict: **GREEN**

## Scope

Audit the context-routing optimization that:
1. slims `CHATGPT.md` into a true bootstrap/router;
2. keeps exact route selection in `workflow/CONTEXT_ROUTING.md`;
3. defines a deterministic minimal read set for review-only ChatGPT sessions;
4. avoids loading Codex/execution/contract files without an actual trigger;
5. preserves all authority, execution-policy, review and continuation semantics in their owning modules.

## Context-size check

Always-read normal-ChatGPT workflow bootstrap before:
- `CHATGPT.md`: 763 words
- `workflow/CONTEXT_ROUTING.md`: 690 words
- total: **1453 words**

After:
- `CHATGPT.md`: 405 words
- `workflow/CONTEXT_ROUTING.md`: 701 words
- total: **1106 words**

Reduction: about **24%** while adding more deterministic review routing.

## GREEN — bootstrap remains authoritative

The slim `CHATGPT.md` still preserves:
- current workflow `main` authority;
- project repository as durable truth;
- `PROJECT.md` as high-level router;
- Task Board as sole mutable implementation state;
- durable state over stale chat memory;
- model-agnostic roles;
- explicit-user-only execution-policy changes;
- lossless-by-authority progressive disclosure;
- fixed-policy no-preflight / mixed-only Capability Gate routing;
- ChatGPT Work exclusion.

Detailed policy/continuation/review semantics remain in their owning phase modules/contracts rather than being duplicated in the bootstrap.

## GREEN — full Project Repository Contract no longer mandatory for ordinary routing

The compact authority precedence needed for routing is embedded directly in `CONTEXT_ROUTING.md`.

`workflow/contracts/PROJECT_REPOSITORY.md` is now loaded only for:
- unresolved authority conflict;
- topology/layout/state-ownership ambiguity;
- legacy-state migration;
- detailed branch/topology-policy questions.

Ordinary review no longer needs this extra file merely to establish precedence.

## GREEN — review-only route is explicit

Base workflow files for a normal ChatGPT independent review are now:

1. `CHATGPT.md`
2. `workflow/CONTEXT_ROUTING.md`
3. `workflow/REVIEW_AND_HANDOFF.md`

Project/Git reads are then driven by durable state:
- `PROJECT.md`;
- Task Board;
- active branch;
- exact review subject;
- reviewed Task Card/milestone contract;
- same authority slice used by implementation;
- required evidence;
- actual reviewed diff/source/runtime.

## GREEN — review conditional contracts

Review loads these only on a concrete trigger:
- `TASK_CARDS.md` for generic Task Card/DoD semantics not explicit elsewhere;
- `GITHUB_STATE.md` for closure/state-consistency issues beyond the review-state transitions already defined;
- `OPENSPEC.md` when the authority slice/verdict depends on OpenSpec;
- `PROJECT_REPOSITORY.md` for conflict/topology/legacy/branch-policy cases.

## GREEN — explicit review non-loading

Review-only explicitly does **not** load by default:
- planning;
- execution prep;
- shared execution;
- ChatGPT execution adapter;
- Capability Gate;
- all `workflow/codex/*`;
- `CODEX_START.md`;
- unrelated cards/milestones/OpenSpec/research/history;
- previous implementing-chat narrative as review evidence.

Automated check confirmed that the REQUIRED review section contains no Codex or execution-module dependency.

## GREEN — pending review priority preserved

A REQUIRED/RECOMMENDED pending/in-progress review remains higher priority than later dependent implementation.

Under `chatgpt_only`, the reviewer is still a fresh normal ChatGPT chat independent from the implementing chat.

## GREEN — no executor-path semantic redesign yet

Execution routes remain dispatched to the same existing execution modules. This change does not attempt to redesign/optimize executor/implementer context; that path can be audited separately.

## Final assessment

**GREEN.** The bootstrap is smaller, review routing is more deterministic, unnecessary Codex/execution/contract reads are explicitly suppressed, and no project authority or review semantics were removed.
