# Fresh ChatGPT Session Start Prompt

Use this entrypoint whenever Project Workflow **requires** or **recommends** a fresh normal ChatGPT chat.

The canonical user-facing fresh-session handoff contract is:

`workflow/common/USER_STOP.md#Fresh ChatGPT handoff`

Do not maintain or improvise a second template here.

## Required semantics

A fresh-session prompt is:
- a thin router into durable project truth;
- branch-aware;
- anchored to one exact entry obligation and the smallest durable start pointer;
- explicit that the entry obligation is **not** a session-scope boundary;
- explicit that after the located role completes, the new chat returns to the selected policy router and continues deterministic authorized transitions until a real workflow stop.

Do not expand the prompt with review/audit checklists, findings, remediation proposals, test inventories, implementation summaries, changed-file lists, recoverable SHAs or GREEN/RED continuation branches.

If special review/audit scope cannot be reconstructed from existing durable authority, persist that scope in the project repository first and point the canonical handoff at the durable scope artifact.

The user-facing response must include the completed canonical prompt immediately. Do not make the user ask for it separately.
