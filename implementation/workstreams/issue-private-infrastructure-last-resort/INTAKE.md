# Intake — private infrastructure last-resort rule

- Workstream ID: `issue-private-infrastructure-last-resort`
- Kind: `issue`
- Branch: `fix/private-infrastructure-last-resort`
- Integration target: `main`
- Base: `d64d8c1d7f05ce2a2584ffcb3ade4634263bbc95`
- Classification: independent
- Path: pending
- Next route: pending

## Operator intent

Prevent normal ChatGPT from using user-owned private infrastructure (for example an Unraid host reached through Remote Desktop Commander) merely as a convenient shell/compute shortcut when the same required operation can be performed with ChatGPT's native runtime/tools or an appropriate purpose-built connector/plugin.

Private infrastructure should be a last-resort execution surface: use it only when the task intrinsically depends on that private host/state, or when the required operation cannot be completed through a materially equivalent native or purpose-built path.

The rule must be expressed as an environment-selection invariant, not as a static capability inventory.

## Problem / diagnostic evidence

A reported project chat copied G-code/code-map material to the user's Unraid host only to hash and parse it. The same hashing/parsing was available in ChatGPT's native isolated environment, so private infrastructure use was unnecessary.

Current `CHATGPT.md` is the mandatory bootstrap for every normal ChatGPT project task, but it does not define a native-first/private-infrastructure-last selection rule.

Current `workflow/chatgpt_only/EXECUTION.md#Runtime-operation-rule` explicitly avoids capability inventories and instructs the executor to attempt concrete operations with actual runtime, but it likewise does not prohibit escalating an otherwise local operation to user-owned private infrastructure for convenience.

`workflow/chatgpt/CAPABILITY_GATE.md` is intentionally scoped to `mixed` policy only and must not be reused for this issue.

## Base / dependency classification

Independent from current unmerged workstreams. The required behavior applies to normal ChatGPT bootstrap semantics on current `main`; no parent-only code or contract is required to diagnose or implement it.

## Candidate correction

Put the short invariant in root `CHATGPT.md`, because that file is read before policy routing on every normal ChatGPT project task. Keep it generic: native/runtime and purpose-built paths first; user-owned private hosts only when intrinsically required or no materially equivalent permitted path exists.

Do not introduce a capability table or route this through the mixed-policy Capability Gate.
