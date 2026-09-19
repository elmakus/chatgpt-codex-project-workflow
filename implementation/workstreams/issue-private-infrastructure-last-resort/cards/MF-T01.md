# MF-T01 — Make private infrastructure a last-resort execution surface

- Milestone: `micro-fix`

> Stable Task Card contract. Mutable execution/review/result state lives only in this workstream's selected Task Board.

## Authority slice

- Master Plan / milestone contract: `none — qualified micro-fix under R6 + implementation/workstreams/issue-private-infrastructure-last-resort/INTAKE.md`
- Requirements: `implementation/workstreams/issue-private-infrastructure-last-resort/INTAKE.md#Operator-intent`
- Accepted decisions: `PROJECT.md#Execution-policy`; `workflow/CONTEXT_ROUTING.md#Policy-invariants`
- Relevant OpenSpec: `none`
- Accepted dependency results: `none`

### Must preserve

- Root `CHATGPT.md` remains the mandatory normal-ChatGPT bootstrap before execution-policy routing.
- The rule is about execution-surface selection, not executor selection.
- Do not introduce or depend on a static capability inventory.
- Do not reuse `workflow/chatgpt/CAPABILITY_GATE.md`; it remains mixed-policy-only.
- Native ChatGPT runtime/tools and appropriate purpose-built connectors/plugins are preferred permitted paths before user-owned/private remote infrastructure when materially equivalent.
- User-owned/private infrastructure remains legal when the task intrinsically depends on that host/state or no materially equivalent permitted native/purpose-built path can perform the required operation.
- Availability or convenience of a general remote-host bridge is not sufficient reason to use private infrastructure.

### Must not / rationale that must travel

Do not duplicate this workflow rule into ChatGPT Project Instructions; those instructions intentionally recover live policy from current workflow `main`.

## Dependencies

- Completed Intake: `implementation/workstreams/issue-private-infrastructure-last-resort/INTAKE.md`

## Outcome

Every normal ChatGPT project task receives a concise bootstrap invariant that prevents unnecessary use of user-owned/private remote infrastructure as a shortcut.

## Scope

### Included

- Add a concise execution-environment selection section to root `CHATGPT.md`.
- Cover user-owned/private hosts reached through general remote desktop/terminal/filesystem bridges generically.
- State both the preferred normal paths and the narrow conditions that justify private-host escalation.

### Excluded

- Capability inventories or matrices.
- Changes to executor routing, `execution_policy`, mixed-policy Capability Gate, Codex orchestration, or plugin-specific configuration.
- Duplicating the rule into per-project bootstrap instructions.
- Host-specific policy limited only to Unraid.

## Acceptance

1. Root `CHATGPT.md` makes user-owned/private remote infrastructure a last-resort execution surface for all normal ChatGPT project tasks.
2. If a materially equivalent native ChatGPT runtime/tool or appropriate purpose-built connector/plugin path exists, private infrastructure must not be selected merely for convenience.
3. Private infrastructure is permitted when the task intrinsically requires that host/state or no materially equivalent permitted normal path can perform the required operation.
4. The text explicitly preserves no-capability-inventory semantics and does not change `workflow/chatgpt/CAPABILITY_GATE.md`.
5. The rule is concise enough for the mandatory bootstrap and does not duplicate policy into Project Instructions.

## Required tests / checks

- Read back branch `CHATGPT.md` and verify all five acceptance points textually.
- Compare the branch against base and verify the behavioral workflow edit is limited to `CHATGPT.md` plus this workstream's durable state/evidence.
- Verify `workflow/chatgpt/CAPABILITY_GATE.md` is unchanged.
- Verify no Project Instructions duplication was introduced.

## Optional execution hints

- Priority: `HIGH`
- Complexity: `LOW`
- Phase: `bootstrap policy`
- Expected/relevant code locations:
  - `CHATGPT.md`

## External write/readback needs

GitHub branch writes only; read back committed files and exact diff/subject.

## Independent review

`RECOMMENDED` — the change is small but affects execution behavior for every normal ChatGPT project task.

## Contract overrides

None.
