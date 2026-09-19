# Brainstorm — Deletion-ready branch prefix

Date: `2026-09-19`
Scope ID: `branch-delete-prefix`
Revision: `R1`
Status: `ready_for_definition`

## Problem / goal

Terminal merged/closed workstream branches currently may remain under ordinary active-looking names after the workflow has proven them safe for removal. This leaves humans and agents unable to distinguish active work from branches that can be deleted.

The requested convention is to move every branch that has passed the applicable terminal safety gate to a `delete/`-prefixed name, for example:

`feat/example` → `delete/feat/example`

The prefix is a deletion-readiness marker, not the deletion itself.

## Current understanding

### Verified facts

- Current ChatGPT-only workstream finalization already has a strict safety gate for integrated workstreams: terminal durable package retained on the integration target, closure reconciliation/readback GREEN, and no active Card/Research/review/integration obligation.
- Current repository policy says the source branch may be deleted only after that gate.
- Current workflow does not define an intermediate naming/marking transition before physical deletion.
- The repository currently contains multiple manually renamed `delete/*` branches, so the requested naming convention already exists operationally but is not normative.
- The active `feat/codex-only-policy` branch is not required as a dependency for this feature.

### Existing accepted decisions

Explicit user choices to carry into Project Definition:
- use the exact `delete/` prefix to mark branches that are safe to remove;
- add the rule to ChatGPT-only policy first;
- do not modify the Codex-only feature branch in this workstream; it will port the accepted rule later.

### Assumptions to formalize

- Applying `delete/` should be a branch-name transition preserving the exact source HEAD/content identity, not a new implementation change.
- The original active-looking branch ref should cease to exist after a successful rename/move; merely creating a second `delete/*` alias while leaving the old ref would not solve the ambiguity.
- Physical deletion of the `delete/*` branch is a separate cleanup action and is not automatically required by workstream close.
- The marker must be applied only after the branch is already proven deletion-safe; it must never be used as a shortcut around review, readback, durable-history, or integration obligations.

## Ideas / alternatives considered

### Option A — Delete terminal branches immediately

Use the existing safety gate and physically delete the source branch as part of close.

Trade-off: clean repository, but removes the visible human/automation cue the user wants and makes cleanup timing less controllable.

Not selected.

### Option B — Rename/move deletion-safe branches to `delete/<original>`

After the existing terminal safety gate passes, move the source branch ref to `delete/<original-name>` while preserving the same exact head SHA, then remove the original ref.

This creates a stable, machine-visible queue of branches that are safe for later physical deletion.

This matches the requested behavior.

### Option C — Record deletion readiness only in durable state

Keep the branch name unchanged and add a manifest/evidence flag.

Trade-off: durable state can express readiness, but stale branches still look active in ordinary GitHub branch lists. This does not address the operational problem.

Not selected.

## Proposed eligibility semantics

### Integrated / merged terminal workstream

A source branch becomes eligible for the `delete/` transition only after the existing ChatGPT-only finalization gate is GREEN:
- accepted implementation is integrated into the final target;
- target-side terminal durable package exists and has been read back;
- closure-only metadata reconciliation is complete where required;
- no active Card, Research, review, integration, or other workstream obligation remains.

The prefix transition occurs after those proofs, not before them.

### Closed / intentionally non-integrated workstream

A branch associated with an intentionally closed, abandoned, or superseded workstream is eligible only when:
- the workstream has an explicit terminal durable state/reason;
- no live obligation remains;
- any unique durable evidence/history required for recovery has been preserved somewhere that does not depend on the branch surviving;
- closure does not represent an unresolved blocker or merely a closed PR with still-active work.

A closed PR alone is not sufficient evidence of deletion safety.

## Rename/move semantics

- Normal mapping: `<branch>` → `delete/<branch>`.
- Preserve the exact source head SHA.
- Do not force-overwrite an existing `delete/<branch>` that points elsewhere.
- If `delete/<branch>` already exists at the same exact SHA and the original branch is absent, treat the transition as already complete.
- If both refs exist or the deletion target exists at a different SHA, route to Recovery/reconciliation rather than guessing or silently overwriting.
- The manifest's stable `branch` provenance should continue to name the original workstream branch identity unless Definition decides otherwise; terminal target-side recovery must not depend on the deletion-ready branch existing.

## Likely policy surfaces

Primary ChatGPT-only policy:
- `workflow/chatgpt_only/WORKSTREAMS.md` — terminal durable package / deletion-readiness transition;
- `workflow/chatgpt_only/CLOSE.md` — close/finalization action ordering;
- `workflow/chatgpt_only/REPOSITORY.md` — Git/branch policy and recovery semantics.

Potentially:
- `workflow/chatgpt_only/STATE.md` or templates only if Definition proves a new durable field is necessary. Current preference is to avoid inventing a second readiness state when branch naming itself is sufficient and existing terminal state already proves safety.
- regression/audit docs and CHANGELOG during implementation.

Out of scope:
- direct Codex-only policy changes;
- automatic physical deletion of `delete/*` branches;
- broad repository cleanup of existing historical branches unless separately requested;
- weakening any current terminal durability/review gate.

## Trade-offs / questions

- The prefix should be a visible operational marker while durable terminal state remains the source of truth for why deletion is safe.
- Closed-but-unmerged branches need stricter interpretation than “PR state = closed”; terminal workstream state and durable recovery must prove safety.
- The transition must be idempotent and collision-safe.
- No new global mutable branch registry appears necessary.

## Research needed

None at this stage. Current workflow contracts and Git branch/ref semantics are sufficient to formalize the feature.

## Open questions

None requiring user input before Project Definition. Definition should formalize the exact normative wording and acceptance criteria.

## Outcome of this session

- Tentative conclusions: adopt `delete/<original-branch>` as the post-safety-gate branch-name transition; preserve head identity; remove the old active-looking ref; keep physical deletion separate; require durable terminal proof for both merged and intentionally closed workstreams.
- Explicit user/product choices to promote through Project Definition: `delete/` prefix; ChatGPT-only first; Codex-only port later.
- Research still needed: none.
- Open questions: none blocking Definition.
- Next phase/action: `ready for definition`
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
