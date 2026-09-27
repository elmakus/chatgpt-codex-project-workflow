# PWv2.2 Program — Master Plan P1

Workstream: `change-pwv22-program-brainstorming`
Planning cycle: 1; entry: `definition:R4|planning-cycle:1`
Definition: R4, GREEN; promoted subject: `pwv22-program@19`
Lifecycle owner: `implementation/workstreams/change-pwv22-program-brainstorming/PLANNING.toml`
Independent Stage-6 Plan Review: REQUIRED for the exact frozen subject.

## 1. Goal and authority

Deliver PWv2.2.0 as a new native, host-neutral semantic workflow contract, with executable validation/routing, published contracts and shared acceptance on ChatGPT and Pi/Paseo. Preserve desired M03–M07 capability directly in PWv2.2 without completing an intermediate full PWv2.1 release or accepting historical workflow state as native.

Authority is the following exact set in `elmakus/chatgpt-codex-project-workflow@3ea6035d169c56316b1755f1f05145d6cf2ca526`:

| Authority | Git blob |
|---|---|
| `requirements/PWV22_PROGRAM.md` — numbered requirements 1–63 | `cbf34ab2df41550c183bfb9e8784f8ff877d4c2a` |
| `decisions/ADR_PWV22_PROGRAM.md` — accepted R4 decisions | `d0478fec6de9db23419769ce413fd8009387d3ab` |
| `decisions/PWV22_M03_M07_DISPOSITION_R4.md` — anti-loss dispositions | `d2bfb87f5cb50bb017b6c14e9cd5a57e2295ca1b` |

The numbered requirements remain authoritative; the coverage table below is navigation, not replacement wording. The complete ADR and anti-loss disposition apply to all seams. Old Brainstorming revisions, PWv2.1 plans, repository README and implementation examples are evidence only where R4 retains their properties. They cannot restore migration, mixed-version or runtime-identity law.

This plan does not approve itself. Implementation requires independent GREEN Plan Review, Planning consumption/approval and exact Premium C satisfaction under the governing router.

## 2. Governance, implementation target and bootstrap boundary

The current consumer workstream remains governed by LIVE `elmakus/project_workflow_v2@main`, observed at `4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`. Its current A/B/C protocol governs this planning transition. PWv2.2-specific C advice, D, native release admission and new schemas are **product deliverables**, not a reason to invent fields or silently switch this existing workstream to the candidate's rules. Test them in isolated native fixtures until an official release exists. Any later adoption of this legacy consumer is a separately authorized reconstruction, never automatic migration or a dependency of shipping the native product.

The product implementation and official package belong in `elmakus/project_workflow_v2`; consumer planning, Results and acceptance evidence belong in this workstream in `elmakus/chatgpt-codex-project-workflow`. Product contributions use an isolated candidate branch with an exact refreshed base, then normal integration/publication. Execution Prep chooses the concrete contribution branch and paths from verified target facts; it must not overwrite canonical `main`, the donor branch or another workstream. This planning task mutates only the consumer planning package.

For P1, product integration/publication targets an isolated versioned release ref and immutable official tag, not replacement of the live default-branch governor. R4 requires an exact official release identity, not that historical projects immediately consume it from `main`. Keep the current governor available through S20 so this non-native consumer can close under its existing contract. Changing the default release channel/governor or adopting this consumer into native PWv2.2 is a separate owner-authorized operation after that boundary; ordinary routing must never normalize this workstream to make a premature cutover appear valid. The versioned package remains a complete usable official release.

The existing product surfaces observed on canonical main are bounded `workflow/` modules, `tools/` validators/router, `schemas/`, `templates/`, `tests/`, `scripts/`, `prompts/` and host delivery entrypoints. These are a location map, not a requirement to preserve their historical schema or module layout. Reuse only components whose retained properties can be demonstrated against R4; remove legacy admission/continuation paths from the native entrypoint. Do not implement a universal state object, runtime scheduler, candidate service or second semantic authority.

### Donor transition

Definition R4's completeness audit identifies the separate pre-M03/M02Q donor boundary as an implementation-transition dependency. At fresh remote inspection on 2026-09-27:

- consumer donor branch `work/pwv21-policy-kernel-brainstorming` was `97646ef848b8d9e5f299d51e9335e74b0679f3fe`;
- its exact `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/TASK_BOARD.toml` was revision 185, with `M02Q-T21` still `in_progress` and R02 closure review pending;
- product donor branch `elmakus/project_workflow_v2@work/pwv21-policy-kernel` was `d338917628d41561635283859675ce93190484cf`.

These are observations, not accepted terminal donor Results. S03 must refetch both repositories, resolve the donor's accepted pre-M03 terminal package and exact implementation/result identities, and verify that the authorized M02Q composition/review boundary actually closed. A last Card being DONE is insufficient. If not terminal, record the concrete external dependency and continue independent S01/S02/S04 work. Do not repair that other workstream, manufacture donor acceptance, materialize its M03, import its full plan as authority or wait for a full PWv2.1 release. No product foundation is consumed/finalized from the unfinished donor. Planning and independent specification/oracle work need not wait.

## 3. Strategy and milestone gates

Milestones are acceptance checkpoints, not automatic reviews or human stops. Every downstream consumption binds exact accepted Results; ordinal labels and DONE alone never suffice. For this program, schedule mutating Cards serially. This is an explicit bounded choice, not removal of the product's required parallel capability; parallel legality is exercised by isolated fixtures. Enabling live parallel Cards later requires a finite exact admission under accepted authority, not mere absence of dependencies.

| Milestone | Seams | Outcome and exit gate |
|---|---|---|
| M01 — Native foundation | S01–S05 | Bounded native semantic contract, independent oracle design, qualified donor baseline and release contract compose into exact native admission/identity/mutation primitives. R01 GREEN before native consumers. |
| M02 — Lifecycle and acceptance | S06–S10 | Gates/preparation, Results/freshness, parallel legality, Review and native Recovery/effects/Close implemented against M01. R02–R05 cover distinct high-risk surfaces. |
| M03 — Core composition | S11 | Full native lifecycle and multiple-Result fan-in behave coherently; R06 integrated compatibility GREEN before adapters consume the composition. |
| M04 — Required hosts and recovery | S12–S15 | ChatGPT and Pi/Paseo share normalized outcomes; destructive recovery and legacy rejection pass; R07/R08 GREEN. |
| M05 — Release qualification | S16–S18 | Exact candidate package, broad independent adversarial sweep, one integrated findings pass, bounded repairs and fresh final acceptance. R09/R10 GREEN and no unresolved release blocker. |
| M06 — Publication and Close | S19–S20 | Exact official release publication and target readback, native activation boundary, consumer integration/readback and durable completion. No remaining authorized obligation. |

Dependency summary (edges mean accepted exact predecessor Results, not runtime waits):

- S01, S02, S03 and S04 have knowable contracts at P1; S03 may be execution-blocked by the donor.
- S05 consumes S01+S03+S04; S06/S07 consume S05; S08/S09 consume S07; S10 consumes S06+S09.
- S11 composes S06+S07+S08+S09+S10; S12/S13 consume S11; S14 consumes S02+S12+S13; S15 consumes S02+S10+S11+S14.
- S16 consumes S04+S11+S14+S15; S17 consumes S16; S18 consumes S17 and any resulting corrective Results plus affected S14/S15 evidence.
- S19 consumes S16+S18; S20 consumes S19 and verified consumer integration facts.

Multiple-input edges explicitly require the integrated compatibility acceptance described in section 6. No hidden milestone gate is a substitute for those facts.

## 4. Execution seams and materialization strategy

Seam IDs below are planning units, **not precreated Cards**. Execution Prep may split a seam into cohesive Cards with one mutating ownership domain each while preserving outcomes, dependencies, review surfaces and tests. It may not combine unrelated risks just to reduce Card count. Any strategy/outcome change returns to Planning; any product change returns to Definition.

`materialization_ready` means the stable Card contract is knowable now, even if execution is blocked. `jit_dependent` means a named future fact determines the substantive write/acceptance scope, not merely its SHA. Missing a future commit hash alone, convenience, distant scheduling and runtime capacity are not JIT reasons. Initial Prep after Plan approval and C must recheck **all** seams, eagerly materialize every then-knowable contract, and retain only bounded triggers for genuinely unknowable ones. Persist exact Result inputs at readiness/launch; never invent predecessor acceptance.

### M01 seams

| Seam | Outcome, boundary and verification | Classification and concrete basis | Dependencies / Review |
|---|---|---|---|
| S01 — Native semantic specification | Define bounded state owners, exact release admission and typed portable Obligation/Result interfaces; enumerate legal/illegal transitions, field ownership, material inputs and acceptance surfaces directly from R4. Include JSON interchange, no-runtime-authority and no-legacy constraints. Publish specification artifacts in the consumer workspace for later product assembly. Check completeness against all 63 requirements. | `materialization_ready`: accepted R4 determines this specification task and its complete acceptance; no donor code is needed. | No predecessor; its high-risk decisions are independently checked in R01 against the implemented native surface. No separate review for editorial sub-Cards. |
| S02 — Spec-derived acceptance corpus | Define shared fixture inputs, manually reasoned expected semantic outcomes and mutation/transition assertions independently of the production router. Include positive/negative and interruption/interleaving cases, legacy fixtures and loss-of-projections scenarios. Record requirement derivations and counterexamples; test the oracle against deliberately wrong outcomes. Concrete host adapters belong downstream. | `materialization_ready`: R4 supplies expected properties and case design now. Lack of future implementation APIs does not justify deferring the corpus. | No predecessor; R07/R08 assess corpus independence and cross-host/recovery use. |
| S03 — Exact donor boundary qualification | Read back terminal pre-M03 donor evidence and compose an exact reusable source inventory, exclusions and reproducible regression commands. Only accepted properties surviving R4 are eligible. Read-only donor access; output is consumer evidence, not mutation of donor state. Negative test: pending Card/review or missing milestone composition cannot pass. | `materialization_ready`: repositories, boundary, acceptance and failure behavior are already known. **Execution blocked** until donor terminal proof exists; the Card is not marked runnable merely because it is materialized. | External pre-M03 donor terminal Result; consumed only by S05/R01. |
| S04 — Release/admission acceptance contract | Specify release manifest contents, exact official commit/tag provenance, candidate-versus-official distinction, no-legacy negative acceptance, forward-repair boundary and target-side publication/activation readbacks. Define a bounded late attended-action checklist with no secrets. This contract does not publish anything. | `materialization_ready`: acceptance is fully derivable from R4; exact future package contents are bound by S16, not guessed now. | No predecessor; R01 checks admission coherence and R10 checks final fulfillment. |
| S05 — Native admission, identity and guarded transition foundation | Assemble the qualified source into an isolated native candidate. Implement exact official release/epoch admission, bounded owner validators, material identity checks, expected-old guards and atomic Git-native publication/readback. Reject unsupported/ambiguous/legacy state before mutation. Tests: competing writer, crash before/after publication, wrong repo/path/blob/epoch, missing target readback, no partial multi-file canonical state. | `jit_dependent`: S01 fixes native field/owner interfaces, S03 establishes the actual reusable file/API inventory and S04 fixes the admission/publication envelope. Those determine the coherent patch and executable assertions. Trigger: exact accepted S01/S03/S04 Results are available. | S01+S03+S04; R01 REQUIRED before downstream foundation consumption. |

### M02 seams

| Seam | Outcome, boundary and verification | Classification and concrete basis | Dependencies / Review |
|---|---|---|---|
| S06 — Native routing, premium gates and preparation | Implement owner routing from Intake/Research/Brainstorming/Definition through Planning, mandatory Planning-owned Simplification Review, A/B/C/D and Initial Prep. C recommends strong reasoning; Initial Prep eagerly creates all knowable Cards; D binds the exact prepared subject and stops before first Execution. Wrong/stale D, repeated D confirmation, JIT convenience and JIT strategy invention must fail. Research returns once to its exact owner; exploration is not authority. | `jit_dependent`: S05's native owner/transition interfaces determine gate placement, atomic prepared-subject binding and the exact routing patch. Trigger: accepted S05 Result with R01. | S05; R02 REQUIRED for gates and owner-routing surface. |
| S07 — Obligation/Result, freshness and derived readiness | Implement typed JSON interchange, exact consumed repository+commit+path+blob, direct dependency bindings, immutable result history and material-local freshness. Derive readiness/frontier without separate mutable truth. Tests include same-path replacement, wrong repository, unchanged unrelated edits, affected descendant invalidation, stale authority and session loss after durable completion without replay. | `jit_dependent`: native identity and publication interfaces from S05 determine result assembly, durable readback and dependency encoding. Trigger: accepted S05 Result with R01. | S05; reviewed in R03/R06 when its identity rules govern parallel/fan-in behavior. |
| S08 — Bounded parallel legality and fan-in | Implement explicit finite exact admission, deterministic resource/write/effect claims, conflict/uncertainty serialization without override, one mutating owner per Card, independent workstreams and sibling-local invalidation. Require exact integrated compatibility before combined downstream use. Exercise two disjoint Cards, overlaps, uncertain claims, stale siblings and revoked admission on disposable branches/effect simulators. | `jit_dependent`: S07's concrete dependency/material-input representation fixes conflict subjects and fan-in operands. Trigger: exact accepted S07 Result. | S07; R03 REQUIRED for parallel/fan-in safety. No live parallel execution is authorized by P1. |
| S09 — Review persistence, convergence and finalization | Implement exact-subject independence, append-only attempt/evidence persistence by the assigned Reviewer, and narrow mechanically implied finalization under CAS/readback. Prohibit reviewer/finalizer dispatch or scope growth. Implement subject-driven topology, bounded RED repair, discovery versus closure, fresh full closure after material repair and ceilings 5/4/3 plus 3 failed rounds per defect class; reaching a ceiling changes mode, never accepts RED. | `jit_dependent`: S07 defines subject/result identity and its material changes; these determine attempt binding, evidence completeness and defect-class history checks. Trigger: exact accepted S07 Result. | S07; R04 REQUIRED. Eligibility never uses model/provider/session identity. |
| S10 — Native Recovery, effects, evolution and Close | Implement exact owner recovery, deterministic mechanical repairs versus owner choices, intent/attempt/readback/known-or-UNKNOWN effects, supported stable idempotency IDs and secret exclusion. Native updates classify preserve/revalidate/stale/Recovery at one epoch per lineage; unchanged Result identity survives revalidation. Close requires integration/readback/durable confirmation and no remaining authorized work. Test unknown effects without blind retry, native upgrade locality, source-context loss, changed output/new Result and post-activation forward repair. | `jit_dependent`: S06 defines owner-return/gate interfaces and S09 defines accepted review/finalization facts, which determine recovery/effects/Close transitions. Trigger: accepted S06/S09 Results with R02/R04. | S06+S09; R05 REQUIRED for mutating recovery/effect/Close surface. |

### M03 and M04 seams

| Seam | Outcome, boundary and verification | Classification and concrete basis | Dependencies / Review |
|---|---|---|---|
| S11 — Integrated native core | Compose S06–S10 on an exact candidate; resolve representation/interface mismatches inside accepted strategy. Prove end-to-end gates, two-Result compatibility, repair/review/recovery/Close and no-legacy admission. Publish one exact integrated compatibility Result binding constituent Results and their required reviews. | `jit_dependent`: actual sibling interface composition and executable mismatches are not durable until S06–S10 complete. Trigger: all five accepted Results and R02–R05. | S06+S07+S08+S09+S10; R06 REQUIRED; cannot replace constituent required Reviews. |
| S12 — ChatGPT delivery and continuation | Build a thin host entry/handoff realization over S11 with exact remote reconstruction, real stop presentation and automatic unique legal continuation. Native C/D advice is presented without hard-coded model law. Preserve ChatGPT execution of Research/Brainstorming and typed durable returns. Assert no hidden chat-memory authority. | `jit_dependent`: S11's actual entry/result/stop interfaces determine adapter changes and host observation steps. Trigger: exact S11/R06. | S11; local deterministic checks, independent acceptance at R07. |
| S13 — Pi/Paseo delivery and continuation | Implement the same semantic routing/consumption through Pi/Paseo-native realization. Research/Brainstorming may hand off to ChatGPT and consume exact durable results; Pi-local execution of those stages is not required. Exercise worker cleanup, late/stale output rejection and no self-authorized work when helpers exist; no worker topology is canonical. | `jit_dependent`: S11 fixes portable interfaces; capability readback then determines host-specific integration and lifecycle hooks. A missing concrete capability becomes a bounded blocker, not a silent host substitution. | S11; local checks, independent acceptance at R07. |
| S14 — Required-host semantic acceptance | Run the same spec-derived cases on ChatGPT and Pi/Paseo with normalized semantic comparison. Record exact package, fixture, authority, environment and observed outputs. Test cross-host receiver refetch and result consumption, real A/B/C/D stops and runtime-local differences. Both hosts must pass; Codex may provide extra evidence but cannot substitute. | `jit_dependent`: S12/S13 establish actual executable host surfaces and observation paths. Trigger: exact accepted S02/S12/S13 Results; qualify their composition before relying on comparison. | S02+S12+S13; R07 REQUIRED integrated host acceptance. |
| S15 — Canonical sufficiency and hard negative acceptance | In isolated disposable fixtures, remove chat/runtime/session state and helpers/projections; reconstruct using only canonical native state plus published contracts. Compare against S02's spec-derived oracle, not the production router used twice. Cover pending gates, durable unreconciled Results, review/repair, UNKNOWN effects and interrupted Close. Historical PWv1/v2.0/v2.1 and malformed/unbound/native-unsupported inputs must reject or route outside native without writes, normalization, inherited GREEN/DONE or migration. | `jit_dependent`: the exact native fixture and host persistence surfaces from S10/S11/S14 determine what must be removed, retained and independently observed. Trigger: accepted S02/S10/S11/S14 Results. | S02+S10+S11+S14; R08 REQUIRED; never delete real project state for these tests. |

### M05 and M06 seams

| Seam | Outcome, boundary and verification | Classification and concrete basis | Dependencies / Review |
|---|---|---|---|
| S16 — Exact candidate release package | Assemble the policy, validators, templates, required tests/tooling and delivery surfaces into one exact candidate inventory under S04. Bind acceptance evidence with scoped reuse decisions. Verify repeatable package reconstruction, no secrets/runtime stores and no unreachable hidden release dependency. Candidate identity is not official admission; publication later maps a new immutable official tag to the reviewed candidate commit. | `jit_dependent`: S11/S14/S15 establish the actual package inventory and accepted property/environment evidence. Trigger: exact S04/S11/S14/S15. | S04+S11+S14+S15; reviewed across R09/R10. |
| S17 — Final independent adversarial sweep and integrated findings | Independently challenge the complete exact candidate and release acceptance, including owner/gate bypass, stale identity, concurrency, review eligibility, effect uncertainty, reconstruction and legacy rejection. Use isolated semantic fixtures and defensive code/contract review. Reconcile all findings once into an evidence-linked, deduplicated defect set; disagreement is resolved from authority/evidence, not votes. This is specific to building PWv2.2, not universal downstream PW law. | `jit_dependent`: exact candidate/evidence is unknown until S16. Trigger: S16 and all required prior GREEN surfaces. No worker count/model/provider is prescribed; sequential fresh independent contexts suffice. | S16; R09 REQUIRED independent discovery plus one integrated findings pass. |
| S18 — Findings consumption, bounded correction and final acceptance | Classify every finding by exact affected subject/authority. Material findings create bounded repair Cards only after their evidence makes contracts knowable. Rerun affected tests/host acceptance; record reuse justification for unaffected evidence. Freeze corrected candidate/evidence and obtain fresh independent full-scope closure after material repair; original reviewers may verify known findings only while eligible. No blanket replay or acceptance-by-limit. | `jit_dependent`: S17 findings determine whether repair work exists and its exact write/acceptance scope. Trigger: integrated findings Result. Zero findings means no invented repair Cards; still satisfy final acceptance. | S17 + actual correction Results + affected S14/S15 evidence; R10 REQUIRED. |
| S19 — Official publication and native activation readback | Validate exact candidate, acceptance, target HEAD/tag absence and authorized publication scope; publish immutable official identity and read it back from target. Check package/tag/commit agree and required-host evidence still applies. First native activation binds that release in a fresh native fixture/project with appropriate owner authority; never rewrite this existing consumer into native. Failure after activation uses Recovery and forward corrective release/revalidation, not semantic downgrade. | `jit_dependent`: approved corrected release subject, target state and concrete publication/activation effects are not known until S18. Trigger: R10 GREEN with all blockers closed and actual effect authorization/access. | S16+S18; R10 is prepublication acceptance. Target readback is mandatory; an unexpected material change invalidates affected approval and reroutes before continuing. |
| S20 — Consumer integration and durable Close | Integrate the complete namespaced authority/evidence/recovery package into the consumer's exact target, read back target commit/contents and record semantic completion independent of source branch or chat survival. Preserve unique knowable recovery records before integration. Only then consider separately authorized cleanup; no source-ref recreation just for bookkeeping. | `jit_dependent`: exact S19 release/readback Result and actual consumer target/PR state determine merge/conflict/readback scope. Trigger: accepted S19 Result. | S19; mechanical continuation from accepted evidence. New material merge/composition changes require exact affected acceptance/review, not a duplicate review for the milestone label. |

Every JIT trigger is consumed once with exact materialization evidence. Later newly knowable seams must be materialized when facts arrive, not deferred until a convenient session. Routine bounded JIT uses the normal execution context; missing strategy is escalated to Planning rather than invented by a stronger model.

The table's review labels describe acceptance obligations, not an executor assigning itself a verdict. In S17 the independent context performs discovery; a bounded coordinator consolidates findings mechanically without voting or suppressing disagreement. In S18 the executor classifies/repairs only within accepted authority, then yields the exact final subject to an eligible independent R10 reviewer. These are separate roles and, where mutation is needed, separate Cards/attempts. S10 similarly contains distinct effects, evolution and Close outcomes: split them at Initial/JIT Prep unless a concrete inseparable invariant proves joint mutation necessary. The seam grouping is not permission for a mega-Card.

## 5. Native premium and authority acceptance

S06 and S14 must prove the complete product A/B/C/D sequence, including interruption and wrong-subject recovery:

1. GREEN Definition exposes A; its exact satisfaction precedes material Planning.
2. Planning performs Simplification Review with explicit Planning-owner accept/reject of material findings; freeze follows a GREEN audit.
3. B requires fresh independent review of the exact frozen plan; the author/repairer cannot supply its verdict.
4. GREEN review is consumed into approved Planning and C due. Native C recommends strong reasoning for Initial Prep.
5. After C, Initial Prep examines every seam and materializes/readbacks all currently knowable Cards and genuine bounded JIT triggers. D binds the resulting prepared subject before first Execution.
6. D permits remaining or switching to a normal/lighter execution context. Satisfaction and readback resume deterministic continuation once; changing prepared semantics cannot reuse stale D. D does not modify Plan/Card meaning.

No test may substitute a model/session name for gate satisfaction, acceptance or reviewer independence. Only authority-changing or genuinely unresolved choices return to the owner; unique legal in-scope continuation proceeds without redundant permission.

## 6. Subject-driven review and integrated acceptance

| Surface | Exact acceptance subject and requirement | Discovery ceiling |
|---|---|---|
| Stage-6 P1 | Frozen plan repository+commit+path+blob; independent Plan Review after B | Governing canonical Planning/Plan Review contract; not self-applied candidate law |
| R01 | S05 native admission/identity/guarded-write implementation + S01/S03/S04 composition evidence; REQUIRED high-risk integration | 4 integration epochs in native fixtures |
| R02 | S06 gate/owner-routing implementation and stale-subject tests; REQUIRED high-risk local surface | 5 local epochs in native fixtures |
| R03 | S07/S08 exact dependency, write/effect claims and multiple-Result acceptance; REQUIRED integration | 4 integration epochs in native fixtures |
| R04 | S09 eligibility, append-only persistence, ceilings and finalizer boundary; REQUIRED high-risk local surface | 5 local epochs in native fixtures |
| R05 | S10 effect/Recovery/evolution/Close surface with S06/S09 composition; REQUIRED integration | 4 integration epochs in native fixtures |
| R06 | S11 complete native lifecycle and constituent compatibility; REQUIRED integration | 4 integration epochs in native fixtures |
| R07 | S14 shared host observations and oracle/corpus validity; REQUIRED integration | 4 integration epochs in native fixtures |
| R08 | S15 destructive reconstruction and legacy-negative proof; REQUIRED integration | 4 integration epochs in native fixtures |
| R09 | S17 broad full-program adversarial discovery and integrated findings | 3 final-closure discovery epochs in native fixtures |
| R10 | S18 exact release closure, coverage, blockers, repair evidence and S04 fulfillment; REQUIRED final acceptance | 3 final-closure discovery epochs in native fixtures |

These numerical product constants are acceptance properties to implement and test; actual program reviews follow the governing published workflow. Per material defect class, 3 failed repair→closure rounds require a mode change/root-cause handling; neither program strategy nor native product accepts RED because a count is reached.

All review subjects bind exact implementation/Result identities, applicable authority, environment-scoped tests and required composition evidence. R09 is discovery; R10 is closure verification and exact release acceptance, not automatic duplicate bug discovery. If material repair occurs, a fresh eligible full-scope reviewer is mandatory. A reviewer may append only its assigned exact attempt/verdict/evidence. A separate deterministic finalizer applies only the validated implied transition; it cannot choose the next Card or enlarge scope.

Routine fixture, prose, adapter or mechanical sub-Cards may complete from exact Results and required checks/readbacks where they create no separate material acceptance surface. They inherit the named downstream required acceptance; they do not acquire an independent review merely because they are Cards. Execution Prep must record that rationale per Card. Conversely, splitting high-risk work cannot erase its required review or allow unchecked downstream consumption.

Integrated compatibility is explicit for every multiple-input edge: bind all accepted exact predecessor Results, state the shared interface/behavior being consumed, verify it on the composed subject and retain required constituent verdicts. If a material sibling changes, invalidate only affected composed acceptance and dependent paths. A shared integration checkpoint cannot substitute for a constituent's required independent review.

## 7. Verification and release decision

Use meaningful failing behavioral cases before the corresponding implementation when possible; this SHOULD practice does not make other valid execution illegal. Tests exercise observable legality, state preservation and target readback, not merely keywords in prose.

The minimum release corpus spans:

- native admission/provenance and one semantic epoch; malformed, ambiguous, foreign and historical states;
- exact repository/commit/path/blob substitution and material-input-local invalidation, unchanged unrelated work and unchanged-Result revalidation;
- stale expected-old mutation, concurrent writers and crashes at multi-file publication/readback boundaries;
- A/B/C/D exact subjects, Simplification Review owner decisions, complete Initial Prep and bounded later JIT;
- explicit finite parallel admission, conflict/uncertainty, one mutating owner, independent workstreams and exact sibling integration;
- review evidence completeness, self-review rejection, append-only history, all convergence ceilings and fresh closure after material repair;
- UNKNOWN effects, supported idempotency, no secrets, native forward correction and semantic Close after context loss;
- ChatGPT/Pi/Paseo normalized acceptance with the allowed Research/Brainstorming handoff asymmetry;
- destructive fixture recovery with disposable helpers removed and an oracle whose expected answers do not call the implementation under test.

Cheap deterministic checks are rerun when proving reuse is harder. Every reused claim identifies the unchanged property, authority and relevant environment; evidence age or same filenames are insufficient. A semantic candidate change reruns affected core tests on **both required hosts**, and full shared release acceptance remains necessary for the final semantic release. A release-blocking defect cannot be deferred as cosmetic.

Required-host access is checked early enough to discover concrete blockers in S12/S13, while human-attended sessions, credentials entry, publication confirmation and activation are batched as late as dependencies safely permit. Prepare the exact subjects, safe test fixtures and readback steps beforehand. Do not combine unrelated authorizations into a mega-Card. Store only non-secret operation/readback identifiers. Simulations do not count as completed host acceptance when actual host behavior is the property at issue.

An official release requires all MUST-semantic, Recovery, required-host, R4 anti-loss and final discovery/closure obligations GREEN. Candidate tags or branch names do not establish official admission. Before any native state is activated, an unaccepted candidate may be abandoned. After official native activation, preserve history and use fail-closed Recovery plus a forward corrective release/revalidation; do not roll a lineage back to an earlier workflow generation.

Prepublication admission tests use an isolated fixture release catalog with independently specified official/unsupported identities; its trust root is explicitly a test input and never makes a candidate official outside the fixture. S19 then proves admission against the real published official identity. Freeze candidate package contents before acceptance and store evidence binding that exact commit in the consumer: do not put a commit's own hash inside its hashed contents. If final repair changes package contents, refreeze and bind all affected acceptance to the new identity before publication.

S19's package/tag readback and S20's consumer integration readback are distinct effects. The consumer repository's observed `auto-patch-tag.yml` runs on `main` and uses historical SemVer tagging; it is not a PWv2.2 official-release authority. S20 must inspect its then-current behavior and include any consequential tag effect in the concrete integration scope. No blind merge/tag action or force-push is authorized by this plan.

## 8. Requirement coverage

Each row assigns a primary implementation owner and a concrete acceptance family. Cross-cutting ADR constraints still apply to every seam.

| Requirement | Primary seam(s) | Acceptance |
|---|---|---|
| 1 | S01, S05 | Published semantic owners; runtime realization cannot change legality |
| 2 | S12, S13, S14 | ChatGPT and Pi/Paseo both pass normalized fixtures; Codex non-blocking |
| 3 | S01, S05, S09 | Remove/change runtime identity without changing route or eligibility |
| 4 | S01, S07 | Typed JSON interchange round-trip with invalid-input rejection |
| 5 | S05, S07 | Reject wrong repository, commit, path or blob |
| 6 | S07, S11 | DONE without accepted exact predecessor Result cannot authorize consumption |
| 7 | S07, S15 | Related change stales affected path; unrelated change preserves work |
| 8 | S05 | Stale expected-old/concurrent writer fails; target readback required |
| 9 | S01, S05 | Bounded ownership; no universal state/ledger |
| 10 | S06 | No Board before implementation state; pre-execution owners remain separate |
| 11 | S07 | Repair/new attempt adds Result without overwriting history |
| 12 | S09 | Append-only exact attempts; finalizer has only mechanical authority |
| 13 | S09 | Material author/repairer cannot issue independent verdict |
| 14 | S06, S14 | A/B/C/D stop sequence and exact-subject readback |
| 15 | S08 | Retained bounded parallel-safe behavior and overlap serialization |
| 16 | S08 | One mutating domain per Card; competing owners rejected |
| 17 | S08, S11 | Exact multiple-Result compatibility plus required constituent reviews |
| 18 | S06, S13 | Follow-on report/late worker output cannot create authority |
| 19 | S13, S14 | Terminal unneeded workers released by host, no canonical session registry |
| 20 | S06, S12, S13 | Unique legal next obligation continues until a real boundary |
| 21 | S09, S10 | In-scope RED repair proceeds; changed strategy/scope returns to owner |
| 22 | S09, S18 | Material repair requires fresh independent full closure |
| 23 | S09, S17, S18 | 5/4/3 discovery and 3 failed-round ceilings change mode, never accept RED |
| 24 | S02, S05–S10 | Meaningful failure-first checks or recorded inapplicability, no invented legality gate |
| 25 | S06 | Material Planning cannot freeze without owner-dispositioned Simplification Review |
| 26 | S06 | Simplification cannot rewrite active/completed scope |
| 27 | S04, S14, S19 | Attended-action dependency review, late safe batching with distinct authority |
| 28 | S15 | Deleting helpers/projections preserves legal continuation |
| 29 | S07, S08 | Minimal direct facts; readiness/frontier recomputed deterministically |
| 30 | S06 | Bounded JIT trigger instead of speculative dependent Card |
| 31 | S10, S19 | Intent/attempt/readback/known-or-UNKNOWN; no blind retry |
| 32 | S10, S19 | Stable idempotency/request identifiers where target supports them |
| 33 | S05, S10, S16 | Canonical package/effects contain no credentials, OTPs or tokens |
| 34 | S14, S16, S18 | Property/authority/environment reuse proof or deterministic rerun |
| 35 | S05 | Validated multi-file transition has one guarded Git publication and readback |
| 36 | S05, S16 | Git-native isolation only; no dedicated candidate backend |
| 37 | S05, S15 | Earlier-generation state cannot continue as native |
| 38 | S05, S15 | No legacy migration engine, mixed reader/writer or downgrade |
| 39 | S04, S19 | Separate owner-authorized reconstruction required for old-project adoption |
| 40 | S10 | Native update classifies preserve/revalidate/stale/Recovery |
| 41 | S04, S16, S19 | Exact official commit/tag covers policy and required tooling/tests |
| 42 | S14, S18 | Final semantic release fixtures pass both required hosts |
| 43 | S16, S18, S19 | MUST/Recovery/required-host failure blocks publication |
| 44 | S10, S15 | Native fact reconstruction, mechanical repair and exact owner return |
| 45 | S10, S19, S20 | Integration, target readback and durable confirmation before Close |
| 46 | S04, S20 | Deferred register survives closure with exact owner/trigger/status |
| 47 | S01, S03 | Direct pivot preserves disposition without waiting for full PWv2.1 |
| 48 | S06 | Every seam classified; all currently knowable Cards materialized/read back |
| 49 | S06, S12, S14 | Native C recommends strong Initial Prep; model identity remains advisory |
| 50 | S06, S14 | Exact prepared-subject D once before first Execution, no semantic mutation |
| 51 | S06 | Bounded routine JIT stays light; strategy ambiguity routes to Planning |
| 52 | S09, S11, S18 | Subject-driven required review, no administrative duplicate |
| 53 | S17, S18 | Broad independent program sweep + one integrated findings pass before release |
| 54 | S08 | Explicit finite exact admission; missing dependency alone is insufficient |
| 55 | S05, S10 | One release epoch per lineage, mixed epochs unsupported |
| 56 | S10 | Unchanged implementation retains Result identity with new acceptance evidence |
| 57 | S09 | Reviewer writes own attempt only; deterministic finalizer cannot route/widen |
| 58 | S12, S13, S14 | Compatible obligations/results with ChatGPT-hosted Research/Brainstorming allowed |
| 59 | S05, S19 | Official exact native release bound before ordinary routing |
| 60 | S02, S15 | Isolated destructive recovery against independent spec-derived oracle |
| 61 | S10, S19 | Pre-activation abandon; post-activation Recovery/forward release, no downgrade |
| 62 | S02, S15 | Legacy rejection leaves bytes/state unchanged; no GREEN/DONE inheritance |
| 63 | S01, S03, S18 | Every M03–M07 family traced to authoritative R4 disposition |

### Anti-loss disposition coverage

| R4 family | Retained/superseding owner | Exclusion maintained |
|---|---|---|
| M03 portability/helper-less recovery/parity | S02/S14/S15; normalized hosts + spec-derived oracle | No successful legacy migration fixtures |
| M04 parallel/ownership/resources/fan-in/locality | S07/S08/S11 | No required named parallel-set, canonical workers or scheduler mechanics |
| M05 Review/repair/convergence/fresh closure | S09/S17/S18 | No blanket Card/Milestone review or runtime-identity eligibility |
| M06 continuation/gates/handoff/Initial Prep | S06/S12/S13/S14 | No provider/session policy as law; native C/D retained |
| M07 Recovery/effects/evolution/Close | S10/S15/S19/S20 | No compatibility readers, normalization, migration, inherited status or downgrade |

## 9. Deferred and excluded scope

This bounded register is durable Planning authority; S20 carries unresolved items forward. None is an excuse to defer a release-blocking MUST requirement.

| Item | Status and owner | Reconsideration trigger |
|---|---|---|
| Mixed native semantic epochs in one active lineage | DEFERRED beyond PWv2.2.0; Definition owner (REQ-55) | Concrete native use case and explicit new Definition |
| Codex as required release host | NON-BLOCKING optional realization; Definition owner (REQ-2) | Explicit restoration as required host |
| Pi/Paseo-local Research/Brainstorming execution | OPTIONAL, not required for 2.2.0; host realization owner within REQ-58 | Demonstrable need; preserve shared durable semantics |
| Context Compiler, trace/shadow indexes and caches | OPTIONAL disposable runtime optimization (REQ-28) | Measured benefit without new canonical authority |
| Additional PWv2.2.x capability beyond accepted R4 core | UNSTARTED; Definition owner | Explicit scope acceptance, never an implicit worker follow-on |
| Default-branch governor/channel replacement and adoption of this existing consumer | SEPARATE owner-authorized operation after this workstream closes; release/adoption owner | Exact affected-consumer reconstruction/continuity decision; never implicit migration |

Rejected: legacy compatibility/migration/downgrade, non-Git candidate storage, universal state/ledger, runtime identity as authority and a full intermediate PWv2.1 M03–M07 release. Separate owner-authorized old-project reconstruction is outside native product semantics.

## 10. Planner completion and continuation

The pre-freeze Simplification Review is recorded in `implementation/workstreams/change-pwv22-program-brainstorming/evidence/SIMPLIFICATION_REVIEW_P1_2026-09-27.md`. The Planning owner explicitly resolves each material finding before freeze; this is not independent Stage-6 Plan Review.

The exact pre-freeze completeness/challenge result and check evidence are recorded in `implementation/workstreams/change-pwv22-program-brainstorming/evidence/PLANNING_AUDIT_P1_2026-09-27.md`.

A GREEN planner completeness/challenge audit must verify exact R4 authority, coverage of all 63 requirements and dispositions, real seam/JIT distinctions, donor locality, review topology, host/recovery/release acceptance, safe publication and no unresolved strategy choice. Then commit this plan, bind its exact repository+commit+path+blob in `PLANNING.toml`, set B due for that subject, validate with the LIVE governing router and read back the published branch.

The next real stop is **Premium B / independent Plan Review**. The planning author must not review this plan or internally dispatch that review. No execution Card, native release, candidate code change or product activation is authorized by freezing P1 alone.
