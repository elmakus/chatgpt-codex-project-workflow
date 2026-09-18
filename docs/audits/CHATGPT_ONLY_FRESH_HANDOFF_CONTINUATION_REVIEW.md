# Fresh independent architecture/coherence review — ChatGPT-only fresh-handoff continuation

Date: 2026-09-18

- Workflow authority reconstructed from: `main@6ddc372b9f3718ea5d9f27e6a01614e8d3da9556`
- PR: `#27`
- Review branch: `fix/chatgpt-only-fresh-handoff-continuation`
- Frozen semantic review subject: `3631cfa8d969f4914618c9313d45cccd60869689`
- Durable scope: `docs/audits/CHATGPT_ONLY_FRESH_HANDOFF_CONTINUATION_SCOPE.md`
- Review method: fresh repository-backed architecture/coherence review of the exact frozen subject. The start prompt, PR body, implementation-author validation and prior chat were treated only as locators/history, not as proof.

Verdict: **RED**

## Coverage

The complete 10-file diff from current main was inspected in context with the active ChatGPT-only authority relevant to routing, review, state, close/publication, Context Health and the policy-neutral user-stop contract.

Logical E2E tracing found no blocker in:
- pending review → GREEN → router → post-review finalization/continuation;
- pending review → RED → bounded remediation → new independent-review boundary;
- milestone completion → CLOSE → next approved deterministic milestone;
- Context Health `FRESH` → locator-only handoff → normal router-owned continuation;
- pre-response router check and no-intermediate-status semantics;
- removal of the old `wykonaj tylko legalny następny krok` wording from changed active handoff contracts;
- single concrete fresh-session template ownership in `workflow/common/USER_STOP.md`;
- ChatGPT-only policy isolation in the changed policy-local files.

GitHub reported no combined status checks and no pull-request workflow runs for the frozen subject, so this review makes no CI-execution claim.

## Blocking finding FHC-01 — durable special-scope pointer semantics diverge across active documentation

**RED.**

The canonical contract is explicit:

- `workflow/common/USER_STOP.md` requires that when a selected route already has a canonical state pointer (for example Task Board), the handoff must keep that canonical pointer and the owning state/contract must reference the durable scope artifact. Direct handoff-to-scope is allowed only when no canonical state pointer already exists.
- `workflow/chatgpt_only/REVIEW.md` independently reinforces that implementation review keeps `implementation/TASK_BOARD.yaml` as the start pointer.

However two changed active documentation surfaces still state the broader rule without that qualifier:

- `README.md` says to persist the special scope and “point the handoff at it”.
- `prompts/CHATGPT_FRESH_SESSION.md` says to “point the canonical handoff at the durable scope artifact”.

For an implementation independent review, following either sentence literally permits replacing the canonical Task Board start pointer with the audit-scope artifact. That contradicts the canonical user-stop/review contracts and can recreate the exact split-state / second-entry-contract ambiguity this change is intended to remove.

This is a coherence blocker, not merely editorial wording, because both files are active operator-facing guidance and the review scope explicitly requires start/README/review documentation to agree with canonical ownership.

## Required bounded remediation

Align both broad statements with the canonical rule:

1. If a selected route already defines a canonical durable state/start pointer, keep it and have that owning state/contract reference the special scope artifact.
2. Point the handoff directly at the special scope artifact only when no canonical state pointer exists.
3. Keep `workflow/common/USER_STOP.md` as the sole concrete template owner; do not add a second template.

All other reviewed continuation semantics may remain unchanged unless the correction itself exposes a new contradiction.

## Review state

The frozen subject `3631cfa8d969f4914618c9313d45cccd60869689` is rejected.

The RED evidence must be persisted before remediation. After bounded correction, the corrected branch subject requires a fresh independent re-review; the correcting chat must not self-review it.


## Bounded remediation completed

The RED finding was corrected without changing the intended continuation model:

- `README.md` now preserves a route-owned canonical durable state/start pointer and allows direct handoff-to-scope only when no canonical pointer exists.
- `prompts/CHATGPT_FRESH_SESSION.md` now states the same rule while remaining a convenience entrypoint with no duplicate concrete template.
- `docs/audits/CHATGPT_ONLY_FRESH_HANDOFF_CONTINUATION_SCOPE.md` now makes the same distinction in the durable special-scope objective.

No GREEN verdict is issued by this correcting chat.

## Next review state

**PENDING fresh independent re-review.**

The corrected exact subject is the final branch HEAD after this remediation/evidence-state update. A fresh independent reviewer must freeze that HEAD at review entry, reconstruct current workflow authority from current `main`, and perform the review again. This chat must not self-review the corrected subject.
