# M02Q-T27 prelaunch acceptance correction

Before T27 launch, full candidate-router readback against the exact current consumer Board was attempted with `elmakus/project_workflow_v2@5e403db8f82e3fa7b8c7dc12bb1904ff441dcaa3`. It fails before OBL-M02Q-03 serving because the pre-existing consumer Board carries a historical `sizing_audits` record for `M02Q-T23` while that Card is no longer materialized.

The same orphan audit is present in the exact T26 Result-era Board at `04226fefd1e9e8d8a36d7d3239cba4396d4f0e12` and in the frozen T27 source snapshot `660a6adce2e64fd12843a8c20d605ac654f9e1dd`; it was not introduced by T26 or T27 and is outside the 23-record legacy Result migration residual.

Because T27 has not started, Execution Prep narrows only the readback method, not the accepted outcome: verify the exact 23-record inventory and all 23 migration proofs directly through the accepted candidate provenance helper, preserve all Result/Review bytes, prove no statusless DONE Result lacks a proof after the mutation, and record the full-router pre-existing T23 diagnostic separately. T27 must not mutate or silently absorb that unrelated historical-state residual.

M03 remains unmaterialized.
