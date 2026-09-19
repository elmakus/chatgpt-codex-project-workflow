# Codex-only Execution Preparation

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **adapt**.

## Ownership

Execution Prep converts approved milestone authority and current predecessor evidence into bounded executable Task Cards for Codex Main.

## Foundation invariants

- Decompose only work whose contract is currently knowable; use durable JIT triggers instead of speculative placeholder Cards.
- Preserve exact requirements, accepted decisions, milestone outcomes, exclusions and authorization gates in each authority slice.
- Fixed `codex_only` execution does not run an executor-selection or capability-inventory gate.
- Serial execution is the safe default until current-state parallel eligibility is proven.
- Planning-level parallel candidates are hints only.
- Codex Main remains the sole writer of shared Task Board/integration state.
- Runtime worker selection and lifecycle are not Task Card schema.

## Deferred contract work

M02 finalizes project-level provenance fields needed by review/recovery. M03 defines exact optional dependency, `parallel_safe`, `write_scope`, `exclusive_resources`, isolated-workspace and recoverable-integration eligibility semantics plus bounded ready-set preparation.
