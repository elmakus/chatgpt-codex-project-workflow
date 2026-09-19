# Intake — private infrastructure last-resort rule

- Workstream ID: `issue-private-infrastructure-last-resort`
- Kind: `issue`
- Branch: `fix/private-infrastructure-last-resort`
- Integration target: `main`
- Base: `d64d8c1d7f05ce2a2584ffcb3ade4634263bbc95`
- Classification: independent
- Path: `micro_fix`
- Next route: `execution_prep:micro_fix`

## Operator intent

Prevent normal ChatGPT from using user-owned private infrastructure (for example an Unraid host reached through Remote Desktop Commander) merely as a convenient shell/compute shortcut when the same required operation can be performed with ChatGPT's native runtime/tools or an appropriate purpose-built connector/plugin.

Private infrastructure is a last-resort execution surface: use it only when the task intrinsically depends on that private host/state, or when the required operation cannot be completed through a materially equivalent permitted native or purpose-built path.

The rule is an environment-selection invariant, not a static capability inventory.

## Problem / diagnostic evidence

A reported project chat copied G-code/code-map material to the user's Unraid host only to hash and parse it. The same hashing/parsing was available in ChatGPT's native isolated environment, so private infrastructure use was unnecessary.

Current `CHATGPT.md` is the mandatory bootstrap for every normal ChatGPT project task, but it has no native-first/private-infrastructure-last rule.

Current `workflow/chatgpt_only/EXECUTION.md#Runtime-operation-rule` deliberately avoids capability inventories and says to attempt concrete operations with actual runtime, but it does not forbid escalating an otherwise local operation to user-owned private infrastructure merely for convenience.

`workflow/chatgpt/CAPABILITY_GATE.md` is mixed-policy-only and is not authority for this issue.

## Base / dependency classification

Independent from current unmerged workstreams. The behavior belongs to normal ChatGPT bootstrap semantics on current `main`; no parent-only source or contract is required.

## Micro-fix qualification

- Root cause and intended behavior are concrete: the mandatory bootstrap lacks an environment-selection invariant; intended behavior is native/purpose-built first and private infrastructure only when intrinsically required or no materially equivalent permitted path exists.
- Bounded and low strategic risk: one bootstrap policy addition; no executor, policy router, state model or orchestration change.
- No accepted requirement/architecture/product decision must change: this constrains tool/environment choice inside existing normal-ChatGPT execution and does not change accepted execution policy.
- Acceptance can be stated directly: `CHATGPT.md` must establish the selection hierarchy, prohibit convenience escalation to user-owned private infrastructure, retain a real-necessity escape hatch, and avoid capability inventory semantics.
- No substantial migration/deployment strategy is needed: repository text contract only.

## Correction target

Add the short invariant to root `CHATGPT.md`, because that file is read before policy routing on every normal ChatGPT project task.

Do not:
- introduce a capability table;
- route the behavior through the mixed-policy Capability Gate;
- name Unraid as the only protected host class. The rule covers user-owned/private remote infrastructure generally.

## Durable continuation

This completed Intake record plus `WORKSTREAM.yaml` is the canonical pre-Task-Board continuation anchor for `workflow/chatgpt_only/MICRO_FIX.md`.
