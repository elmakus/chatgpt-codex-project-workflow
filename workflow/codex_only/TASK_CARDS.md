# Codex-only Task Card Contract

> M01 foundation contract. This namespace is not selected by root routing before M04.

Classification: **adapt**.

## Meaning

A Task Card is a bounded project work-package contract. Codex Main owns project-level execution coordination; concrete worker realization is runtime-owned.

## Required project contract

Each Card identifies:
- stable ID/title/milestone;
- dependencies;
- exact durable authority slice;
- bounded included/excluded scope;
- outcome and acceptance;
- required tests/evidence/readback;
- authorization gates;
- independent-review requirement when applicable.

Mutable execution/review/result state belongs to the selected canonical Task Board, not the stable Card contract.

## JIT and parallel foundation

Do not create speculative Cards before their real contract is knowable. Serial execution is valid by default.

M03 defines optional project-level `parallel_safe`, `write_scope`, `exclusive_resources` and isolated-lane requirements plus current-state JIT eligibility. Those fields describe project safety/ownership, not runtime worker configuration.
