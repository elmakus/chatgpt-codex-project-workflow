# Brainstorm — Branch deletion readiness

Date: `2026-09-19`
Scope ID: `branch-delete-prefix`
Revision: `R2`
Status: `tentative`

## Problem / goal

Terminal merged/closed workstream branches need an unambiguous cleanup signal so agents and humans can tell which branch refs are safe to remove.

The first idea was to rename `feat/x` to `delete/feat/x`. Current ChatGPT GitHub connector capability makes that unsafe to express directly: it exposes branch creation/ref movement but not a true branch-rename or ref-delete action. Creating `delete/feat/x` at the same SHA therefore creates a second branch rather than renaming the original.

## Current understanding

### Verified facts

- GitHub itself supports true branch rename and Git-ref deletion.
- The currently available ChatGPT GitHub connector surface does not expose either operation.
- Creating a new branch with the same SHA is only an alias/duplicate ref and MUST NOT be treated as a rename.
- GitHub branch objects do not have a native label/description surface comparable to issue/PR labels.
- Pull requests can carry labels through the connector.
- Current ChatGPT-only workstream finalization already defines the safety gate after which a source branch can be removed.

### Existing accepted user direction

- ChatGPT-only policy should gain an explicit branch-cleanup convention.
- Codex-only should port the accepted convention later rather than being modified by this workstream.

The earlier preference for a `delete/` prefix is reopened because the current connector cannot implement it safely without creating duplicate refs.

## Alternatives

### Option A — Durable cleanup state + PR label (recommended)

Use durable workstream state as authority, for example:

```yaml
branch_cleanup:
  ref: "feat/example"
  state: "safe_to_delete"
  verified_head: "<sha>"
  evidence: "<exact evidence pointer>"
```

Optionally add a human-visible PR label such as `branch-safe-to-delete` when a PR exists.

Rules:
- `safe_to_delete` may be set only after the existing terminal safety gate passes.
- The ChatGPT connector MUST NOT create a `delete/*` alias as a substitute for rename.
- Physical branch deletion is performed only by a surface that actually supports ref deletion (GitHub UI/API/CLI or a future connector capability).
- After successful deletion, durable cleanup state may advance to `deleted` with exact readback/evidence.
- A closed PR alone never proves cleanup safety.

Advantages:
- no duplicate branches;
- recoverable and auditable;
- filterable in PR UI when the optional label is used;
- independent of connector limitations;
- future deletion automation can consume the same durable state.

Trade-off:
- the GitHub Branches page itself does not visually show the marker.

### Option B — True rename to `delete/<original>`

Use only when the executing surface exposes a real branch-rename operation.

Rules:
- never emulate rename by creating a second branch;
- preserve exact head identity;
- old ref must no longer exist after successful rename;
- collision/readback failures route to Recovery.

Advantage:
- visible directly in the branch list.

Trade-off:
- unavailable through the current ChatGPT connector.

### Option C — Automatic deletion after merge

GitHub can automatically delete PR head branches after merge.

This is useful for repositories whose workflow can tolerate deletion immediately at merge time, but current ChatGPT-only finalization requires terminal durable-package/readback proof before source-branch deletion. Therefore automatic deletion must not be enabled as the workflow solution unless Definition deliberately changes that ordering.

### Option D — Cleanup issue/checklist only

Maintain one cleanup issue containing branch names.

Useful as an operator dashboard, but weaker than workstream-owned durable state and easy to drift. Not preferred as authority.

## Proposed eligibility semantics

### Merged/integrated workstream

Set `branch_cleanup.state: safe_to_delete` only when:
- accepted implementation reached the final integration target;
- target-side terminal durable package exists;
- closure/result reconciliation is complete where required;
- final readback is GREEN;
- no Card, Research, review, integration, blocker-recovery or other workstream obligation remains.

### Closed/superseded/non-integrated workstream

Set `safe_to_delete` only when:
- terminal closure/supersession is explicit and durable;
- no live obligation remains;
- unique history/evidence required for recovery no longer depends on the branch;
- the branch is not merely attached to a closed PR whose work remains unresolved.

## Connector capability rule

When cleanup is proven but the current executor lacks real rename/delete capability:

1. persist `safe_to_delete` with exact branch ref/head/evidence;
2. optionally label the associated PR `branch-safe-to-delete`;
3. do not create any replacement/alias branch;
4. report the exact cleanup action only at a real user/runtime boundary;
5. a later cleanup-capable actor deletes the original ref directly.

## Current duplicate-ref incident

If an earlier agent created `delete/<original>` at the same SHA while leaving `<original>` in place:
- treat the `delete/*` ref as an accidental duplicate, not as successful cleanup marking;
- verify exact SHA pairing and terminal safety before deletion;
- do not create further marker branches;
- cleanup should ultimately remove the redundant refs rather than preserve both names.

## Likely policy surfaces

Primary:
- `workflow/chatgpt_only/WORKSTREAMS.md`
- `workflow/chatgpt_only/CLOSE.md`
- `workflow/chatgpt_only/REPOSITORY.md`
- `workflow/chatgpt_only/WORKSTREAM_TEMPLATE.yaml`

Potential:
- `workflow/chatgpt_only/STATE.md` if the cleanup field needs explicit validation/recovery rules;
- regression/audit evidence and CHANGELOG.

Out of scope:
- direct Codex-only policy changes;
- automatically deleting historical repository branches in this feature;
- weakening existing terminal safety gates.

## Research needed

None. Official GitHub capabilities and the current connector surface are sufficient to define the problem.

## Open questions

User choice before Definition:
- prefer **Option A** (durable `safe_to_delete` + optional PR label; no branch rename in ChatGPT-only), or
- keep `delete/` as the desired visible convention but make it conditional on a future/alternate executor that supports true rename.

## Outcome of this session

- Tentative recommendation: Option A.
- The workflow should explicitly forbid “rename by duplicate branch creation”.
- Definition promotion authorization: `pending`
- Definition promotion subject: `none`
- Next phase/action: continue brainstorming until the cleanup marker choice is accepted.

> Nothing in this file becomes accepted requirement/decision authority by itself. Project Definition owns promotion into canonical `requirements/` and `decisions/`.
