# Codex-only Planning

> M03 contract. This namespace remains non-routable from root policy routing until M04.

## Ownership

Planning organizes an approved Project Definition into milestone outcomes, dependencies, verification/migration strategy, authorization boundaries and JIT triggers.

## Invariants

- Planning does not redefine accepted product/system intent.
- Milestones describe integrated/testable outcomes, not worker sessions.
- Candidate parallel structure may be recorded, but Planning cannot certify future runtime-safe concurrency.
- Exact future Card detail is deferred when predecessor evidence is required.
- New or materially revised plans use independent plan review when required/recommended.
- A qualifying Codex-managed independent plan reviewer may satisfy the project review gate; normal-ChatGPT identity is not a semantic requirement.

## Candidate parallelism

Planning may state:

- dependency relationships;
- packages that appear independent enough to be candidates for overlap;
- expected ownership/write boundaries;
- explicit JIT triggers that must resolve exact Card safety later.

Candidate status is non-executable planning guidance. It does not set `parallel_safe`, freeze a lane, reserve a resource, choose a worktree or establish an integration base.

Execution Prep owns current-state JIT eligibility under `EXECUTION_PREP.md`. A planning candidate that fails current safety simply falls back to serial execution; Planning is reopened only when the failure changes milestone strategy rather than execution detail.

M04 reconciles the complete planning route before root activation.
