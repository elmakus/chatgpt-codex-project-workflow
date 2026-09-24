# Decision — PWv2.1 incorporates live workflow discoveries at safe boundaries

- Decision ID: `ADR-PWV21-007`
- Date: `2026-09-24`
- Status: `accepted`
- Authority: `user`
- Definition subject: `pwv21-policy-kernel@2`
- Related requirements: `PWV21-REQ-122..127`

## Context

Real M02 execution exposed workflow defects that static design/review had not surfaced. Applying fixes only after all PWv2.1 milestones would let downstream work encode known-bad semantics, while changing authority continuously inside active reviewed work would damage reproducibility and truthful history.

## Decision

- Material live observations are classified before changing authority:
  1. implementation defect under existing authority;
  2. review/process realization defect;
  3. Planning-to-Execution-Prep fidelity defect;
  4. accepted-authority defect;
  5. speculative future hardening.
- A durable finding classified as materially affecting the next downstream authority/topology/semantics must be reconciled at the earliest safe boundary before that affected JIT materialization.
- Unrelated/speculative observations do not become blockers merely because they are open.
- Trackers/issues are bookkeeping and evidence locators only; they never become accepted authority or repair authorization.
- Correctly terminal historical Cards/Milestones are not reopened merely because later workflow rules improve.
- Valuable historical failure cases are replayed as immutable regression fixtures against the new workflow semantics.
- Downstream live-consumer validation begins only after the corrected Definition/Planning/review gates are accepted; no special prompt may substitute for missing workflow semantics.
- For this workstream, terminal M02 remains history/regression evidence and M03 is the first intended downstream live consumer of the corrected semantics.

## Consequences

PWv2.1 can improve from real execution before project completion while preserving historical truth, explicit authority ownership and deterministic downstream boundaries.
