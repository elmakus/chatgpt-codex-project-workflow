# Universal fenced handoff and minimal bootstrap contract — M01-S04-T02

## Envelope
Every handoff carries exactly enough transient continuation data: consumer repository, branch/ref, observed remote commit fence, exact entry obligation, durable start pointer, and workflow-authority bootstrap locator. Optional effect uncertainty is referenced by its durable obligation-local record, never hidden runtime state. Model/provider/session/worker identity is excluded.

Persistent ChatGPT Project Instructions contain only stable workflow authority/router locator, consumer repository locator and non-authoritative coordinator bootstrap. Branch, Card, workstream selection, model/session, research run and transient handoff state are never persisted there.

## Receiver procedure
1. Load canonical router from current official workflow authority.
2. Fetch remote consumer branch and compare with handoff fence.
3. Equal: reconstruct from durable pointer and progressive router reads. Moved: reconstruct current canonical state; never force stale fence. Missing/unreachable/wrong repository/path: fail closed.
4. Inspect the one ordinary same-branch worktree slot. Clean matching slot may be reused. Dirty/local-only residue is evidence only, never accepted continuation truth. Do not create a duplicate slot.
5. Before reset/disposal, reconcile any UNKNOWN external effect by target readback. Never destroy the only evidence of an uncertain effect.
6. Launch only the exact obligation selected from current durable state. Publication uses expected-old and target readback; a race refetches/re-evaluates.

Transport delivery is not handoff satisfaction. Satisfaction requires the receiver to reconstruct the same legal continuation from remote durable state with no hidden setup.

## Final Qualification ownership window
Pi Main/Paseo may own ordinary execution through the mandatory Final Qualification Handoff. After exact handoff satisfaction, Final Qualification remains outside that required Pi/Paseo realization window unless later authority says otherwise.

No helper receipt, local cache, runtime ID or package-local state can override canonical Git.
