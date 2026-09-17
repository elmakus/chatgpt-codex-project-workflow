# Semantic Audit — Independent Review Handoff and Runtime Capability Discovery

Date: 2026-09-18

## Scope

Audit the workflow changes that:

1. make REQUIRED/RECOMMENDED `chatgpt_only` independent review a mandatory fresh-chat handoff;
2. keep `codex_only` independent review inside Codex orchestration through an independent reviewer worker/session;
3. remove capability preflight/inventory from fixed execution policies;
4. preserve Capability Gate only for `mixed`;
5. make Task Board durable review state explicit.

## Authority split checked

### Project Workflow

Owns:
- execution policy;
- Task Board/project execution state;
- Task Card/milestone boundaries;
- exact review subject and review requirement;
- durable review verdict/evidence;
- acceptance and milestone continuation;
- strategic/user/authorization blockers.

### Installed `codex_workflow`

Owns internal Codex runtime orchestration when enabled:
- execute/review worker routing;
- worker roles/models;
- delegation/concurrency/lifecycle;
- waiting/event/message behavior;
- worker-runtime recovery.

No duplicate Codex runtime orchestration was introduced in Project Workflow.

## Review semantics

### `chatgpt_only`

PASS.

The implementing chat cannot satisfy its own REQUIRED/RECOMMENDED independent review. It must:
- persist exact `review_subject` and implementation evidence;
- set Task Board `review_state: pending`;
- stop before verdict;
- require the user to start a fresh normal ChatGPT chat.

The fresh review chat reads durable state, transitions review to `in_progress`, persists GREEN/RED evidence and updates Task Board. After GREEN it may continue later deterministic execution. If that chat then implements a later reviewable subject, another fresh review chat is required.

OPTIONAL review does not force a fresh-chat boundary unless activated explicitly.

### `codex_only`

PASS.

Codex Main remains coordinator. The implementing worker cannot review its own subject. Main obtains a distinct reviewer worker/session. When installed/enabled, `codex_workflow` owns the internal reviewer-routing mechanics. Reviewer independence therefore does not force a user or normal-ChatGPT handoff.

## Capability semantics

### Fixed policies

PASS.

`chatgpt_only` and `codex_only` do not run:
- Capability Gate;
- capability inventory;
- tool/MCP availability checklist;
- capability proof inside Refresh Gate.

Execution starts after the ordinary state/contract Refresh Gate. Capability becomes workflow state only when a concrete required operation cannot proceed.

For Codex, ordinary non-secret local tooling/dependency gaps are self-remediable execution details when environment/security/reproducibility constraints permit. User-provided MCP/credential/token/account permission/privileged access is escalated only when concretely required and unavailable.

### `mixed`

PASS.

Capability Gate remains the only pre-assignment capability-routing mechanism. After assignment, runtime capability problems do not silently reroute the card.

## Explicit policy change after blocker

PASS.

No automatic executor/policy fallback exists. If the user explicitly changes `execution_policy`, the blocked Task Board state is reconciled and work may be reassigned under the new policy.

## Refresh Gate semantics

PASS.

Refresh Gate is now explicitly a state/contract drift gate. It checks:
- branch/HEAD/runtime/external state;
- Task Board/dependencies;
- requirements/decisions/plan/OpenSpec;
- current interfaces;
- tests/evidence/readback/review obligations;
- parallel ownership.

It does not inventory fixed-executor capabilities.

## Durable review state

PASS.

Task Board template and GitHub State Contract define:

```yaml
review_state: pending | in_progress | green | red
review_subject: <exact sha/subject>
review_evidence: <path-or-null>
```

This preserves recovery across ChatGPT chats and Codex worker/session boundaries without moving live state back into milestone/Card files.

## Cross-document consistency

Reviewed and aligned:
- `CHATGPT.md`
- `README.md`
- `workflow/EXECUTION.md`
- `workflow/EXECUTION_PREP.md`
- `workflow/REVIEW_AND_HANDOFF.md`
- `workflow/chatgpt/EXECUTION.md`
- `workflow/codex/EXECUTION.md`
- `workflow/codex/CODEX_ORCHESTRATION.md`
- `workflow/contracts/GITHUB_STATE.md`
- `workflow/contracts/TASK_CARDS.md`
- `templates/TASK_BOARD.yaml`
- `templates/TASK_CARD.md`
- ChatGPT/Codex bootstrap prompts
- `CHANGELOG.md`

## Verdict

GREEN.

The workflow now distinguishes three independent concerns cleanly:

1. **executor choice** — fixed by `chatgpt_only`/`codex_only`, routed only in `mixed`;
2. **runtime capability discovery** — concrete-operation blocker, not fixed-policy preflight;
3. **review independence** — fresh user-started ChatGPT chat for `chatgpt_only`, internally orchestrated independent Codex reviewer for `codex_only`.
