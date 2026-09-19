# Codex-only Close

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **adapt**.

## Ownership

This module owns milestone acceptance, publication/finalization, workstream integration and deterministic continuation for `codex_only`.

## Foundation invariants

- Milestone acceptance is distinct from Card completion.
- Required project review gates must be satisfied for the exact accepted subject.
- Branch-isolated integration refresh compares the workstream against the current integration target before merge/publication.
- Codex Main owns project-level integration and shared durable state updates.
- A qualifying Codex-managed independent review does not require a second normal-ChatGPT review.
- GREEN milestone completion is not automatically a user stop; already-approved continuation proceeds until a real strategic, authorization, runtime/input or end-of-scope boundary.
- Publication must not silently perform an unauthorized live/deployment write.

## Deferred contract work

M02 finalizes formal-review/state consequences used by Close. M03 finalizes bounded lane integration semantics. M04 reconciles target-refresh, stacked-workstream, publication and continuous multi-milestone routing in full before activation.
