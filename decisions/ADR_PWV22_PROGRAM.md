# ADR — PWv2.2 Program Definition R5

- Decision ID: `ADR-PWV22-PROGRAM-R5`
- Status: accepted Definition authority; supersedes the earlier predecessor-rebind/backward-compatibility assumption
- Source subject: `pwv22-program@20`

## Decisions

- PWv2.2 is a semantic workflow contract, not a runtime orchestration specification.
- ChatGPT and Pi/Paseo are required PWv2.2.0 hosts; Codex is non-blocking.
- Runtime/model/session/worker identity is never canonical workflow authority.
- Typed Execution Obligation / Result remain transport-neutral with JSON as the common portable interchange format.
- Exact Result identity is repository + commit + path + blob.
- Freshness is material-input-local.
- Canonical writes are guarded and read back.
- Review attempts are append-only and exact-subject-bound; deterministic finalization remains non-semantic.
- Premium A/B/C/D remain real stops; reviewer model quality is advisory, review independence is mandatory.
- PWv2.2.0 preserves accepted PWv2.1 bounded parallel-safe Card behavior.
- One Card has one mutating ownership domain; runtime worker topology remains runtime-local.
- Worker/subagent cleanup is an explicit runtime expectation, but shutdown/session/capacity mechanics are not canonical state.
- Review convergence ceilings from PWv2.1 remain part of workflow law.
- Falsification/test-first remains SHOULD rather than MUST.
- Simplification Review is mandatory inside Planning before freeze and introduces no new top-level stage.
- Context Compiler/shadow DAG/frontier are disposable projections only.
- Dedicated candidate storage is rejected; Git-native isolation/publication is allowed.
- External-effect uncertainty uses UNKNOWN + exact readback; blind retry is forbidden.
- Policy evolution uses minimal preserve/revalidate/stale/Recovery handling.
- PWv2.2 is a new native workflow contract, not a compatibility layer over PWv1/PWv2.0/PWv2.1 durable state.
- No backward-compatible legacy reader, old-state continuation guarantee, automatic workstream/schema migration, mixed-version mode or downgrade path is required.
- Intentional transfer of an old project into PWv2.2 is a separate owner-authorized reconstruction/adoption task that establishes fresh PWv2.2-native authority from current product facts and useful evidence; preserving old workflow-state semantics is not required.
- Definition completion does not depend on terminal PWv2.1 or a final PWv2.1 rebind.
- The direct pivot must still perform an anti-loss reconciliation so desired capabilities from the unstarted PWv2.1 M03-M07 scope are retained, superseded deliberately, deferred or explicitly rejected rather than disappearing accidentally.


## Execution preparation and hand-back decisions

- Strategic Planning must classify execution seams as `materialization_ready` or `jit_dependent`; JIT requires a real not-yet-durable dependency and is not the default deferral mechanism.
- Premium C remains the real stop before Execution Prep, but its PWv2.2 recommendation is to move to the best available strong reasoning context for the Initial Execution Prep pass rather than to a cheaper context.
- Initial Execution Prep is the one-time high-quality pass that validates Plan decomposition, eagerly materializes every currently knowable stable Card, and leaves only genuinely predecessor-dependent work behind bounded JIT triggers.
- PWv2.2 adds Premium D immediately after Initial Execution Prep and before first Execution. D is a user-facing hand-back gate so the owner can deliberately stay or return to a lighter/normal execution context before implementation begins.
- Premium D is not a new workflow stage and does not alter Plan or Card authority. Once its exact satisfaction is durably read back, normal Execution/Review auto-continuation resumes.
- Routine later JIT refinement stays in the normal execution context by default. A true strategy/outcome ambiguity routes back to Strategic Planning instead of being solved by silently escalating inside Execution Prep.


## R5 retained and updated owner dispositions

- Review topology is subject/acceptance-driven. PWv2.2 does not require blanket independent Review after every Card or every administrative Milestone.
- Routine local Cards may rely on exact Result + required tests/readback when Planning establishes no distinct independent acceptance surface. Material integration/fan-in, explicitly high-risk subjects and final closure after material repair/convergence retain independent Review.
- Final Qualification defect discovery is universal PW law: every PW-managed change receives a proportional Targeted Bug Hunt plus a Global identical-prompt Bug Hunt before fresh final acceptance/release. Worker/chat count and model/provider realization remain runtime/owner choices.
- PWv2.2.0 convergence constants are local/Card=5 discovery epochs, integration/composed=4, final-closure=3, plus 3 failed repair→closure rounds per material defect class. They may be deliberately changed by a later workflow Definition.
- Parallel legality requires an explicit finite accepted admission fact but does not require one particular named parallel-set data structure.
- PWv2.2.0 uses one exact native semantic release/epoch per active project/workstream lineage. Mixed native epochs are deferred until a concrete need exists.
- Native `revalidate` preserves the exact Result identity when implementation/output is unchanged and appends/binds new exact acceptance evidence; a new Result is created only for a genuinely new/materially changed result-producing attempt.
- Reviewer persistence is narrow: an independent Reviewer appends only its exact Attempt/verdict/evidence. A deterministic finalizer/coordinator may apply only mechanically implied validated/CAS/read-back transitions and may not choose downstream work or widen authority.
- ChatGPT and Pi/Paseo must derive compatible Research/Brainstorming obligations and consume the same durable results, but PWv2.2.0 does not require Pi/Paseo-local execution of those stages. ChatGPT-hosted execution plus runtime-neutral handoff is accepted.
- Every native project/workstream must bind exact official PWv2.2 semantic release provenance before ordinary routing.
- Release acceptance requires canonical-sufficiency/destructive-recovery evidence after total loss of runtime/session/helper state using a non-circular oracle.
- Once official native PWv2.2 state exists, semantic defects use fail-closed Recovery + forward corrective release/revalidation; semantic downgrade is unsupported.
- Representative legacy states are negative release fixtures only: they must not be silently read as native, normalized, continued, inherited or migrated.
- The authoritative M03-M07 anti-loss disposition is `decisions/PWV22_M03_M07_DISPOSITION_R4.md`.


## R5 deferred-defect and Final Qualification decisions

- Independent Review remains binary GREEN/RED. Deferred findings are separate durable obligations and never create a third acceptance verdict.
- A Card may be GREEN/DONE with an open finding only when the finding does not falsify its exact acceptance and continuation is positively proven safe. A finding that falsifies exact acceptance prevents DONE.
- Blocking is material-dependency-local. Unaffected Cards may continue; affected consumers wait for repair/accepted revalidation.
- Deferred defects are repaired at the earlier of first affected consumption or the exact latest-safe repair boundary; current-release defects cannot cross final candidate acceptance/publication unresolved.
- Final Qualification Handoff is a mandatory real stop for every PW-managed change, using the existing locator-only handoff primitive rather than a new lifecycle stage.
- Final Qualification proceeds as: Known Defect Cleanup -> Targeted Bug Hunt -> Global identical-prompt Bug Hunt -> integrated finding reconciliation -> bounded repair/integration -> material-local impact/revalidation -> fresh eligible independent full-scope final acceptance -> ordinary release/publication/readback/Close.
- Known Defect Cleanup is a zero-work obligation when there are no durable open findings.
- Targeted and Global hunts are discovery mechanisms, not acceptance by worker count, duplicates, majority or zero findings. Their scale is proportional to project risk/size.
- Multiple independent repairs may run in parallel only under explicit finite admission/conflict analysis. One integration owner serially composes the shared candidate.
- Post-repair invalidation is material-local: preserve implementation when unchanged, revalidate proof when sufficient, make only materially changed downstream outputs stale, and use Recovery for unknown impact.
- Runtime orchestration mechanisms such as branch claims, run-ID allocators and fresh-chat counts remain non-authoritative implementation details.
- The approved P1 predates these material semantics and therefore cannot proceed through Premium C. R5 requires a new Planning cycle P2 with fresh A/B/Plan-Review/C progression.
- PWv2.2 Definition and Planning may continue while the separate PWv2.1 donor workstream finishes its authorized pre-M03 boundary, but PWv2.2 Initial Execution Prep remains held until that donor boundary is complete.
