# Design — codex_only M02 review state

## Chosen representation

Use one Task-Board-local `review` block per Card/milestone with a resolved requirement, a `current_attempt` pointer and append-only attempt entries. Keep semantic production ownership in `implementation_owner_role` on the reviewed Card or milestone. A milestone owner role is aggregate project provenance; RED milestone repair is materialized as bounded corrective Card(s) through Execution Prep rather than inferred from runtime identity.

This avoids two failure modes:

- a flat `review_subject/review_evidence` tuple would overwrite prior RED evidence when S2 replaces S1;
- persisting runtime worker/session IDs would couple project recovery to `codex_workflow` internals.

The attempt ledger is Project Workflow state. Runtime worker mappings are not.

## State-transition ownership

Codex Main performs all shared-state mutations:

```text
Executor result S1
  -> Main appends R01 pending
  -> independent Tester reviews S1
  -> Main records R01 RED
  -> Main returns correction to owning Executor role
  -> Executor result S2
  -> Main appends R02 pending
  -> independent Tester full recheck of S2
  -> Main records R02 GREEN
  -> Main finalizes project state
```

Tester output is bounded verdict/evidence. Tester cannot repair production and does not directly own the Task Board.

## Independence and runtime transparency

The project stores roles (`executor`, `tester`) rather than concrete workers. Runtime must establish that the reviewer realizing `tester` is independent from the worker that realized the subject's implementation owner. Main records only the project attempt/verdict/evidence.

Same logical Tester reuse and fail-closed replacement are runtime choices. Both map to the same project state when the subject is unchanged.

## Compatibility boundary

M02 may expand codex_only templates because the namespace is not routed yet. It does not alter ChatGPT-only templates, root routing, or legacy contracts.

M03 may later extend implementation ownership with lane-scoped project provenance and parallel eligibility fields; it must preserve the M02 attempt ledger and runtime-identity prohibition.
