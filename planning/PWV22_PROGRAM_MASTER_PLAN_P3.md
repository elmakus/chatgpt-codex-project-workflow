# PWv2.2 Program — Master Plan P3

Workstream: `change-pwv22-program-brainstorming`
Planning cycle: **3**; entry: `plan:P2@5524876b49320a1f4da6dd0cf8b0cbc38b31c4fc|correction:S07-S08-R03-order|planning-cycle:3`
Definition: **R7 GREEN**, promoted subject `pwv22-program@22`
Lifecycle owner: `implementation/workstreams/change-pwv22-program-brainstorming/PLANNING.toml`
Independent Stage-6 Plan Review: **REQUIRED** for the exact frozen subject.

## 1. Goal, exact authority and material re-entry

Deliver PWv2.2.0 as a new native semantic workflow product with shared ChatGPT and Pi/Paseo acceptance, an official installable Project Workflow for Pi package, and universal remote-fenced handoffs. Git/GitHub is the only canonical backend. Native Paseo + Pi + configuration/skills + the qualified thin reconstructible helper is the Pi realization. No full orchestration-runtime, tracker subsystem, legacy migration or intermediate full PWv2.1 release is included.

Authority is pinned to consumer repository `elmakus/chatgpt-codex-project-workflow` at handoff `486685f17bb4a022e6dfed89383f8b9744b668fa`:

| Path | Exact blob / use |
|---|---|
| `requirements/PWV22_PROGRAM_R7.md` | `f326a0778915cfed5ddcecc735f19b59dfd63051`; requirements 1–97 |
| `decisions/ADR_PWV22_PROGRAM.md` | `c1b5f21e91649566525dae1dfbe57b4e40c04d22`; accepted R5/R6 decisions |
| `decisions/PWV22_M03_M07_DISPOSITION_R4.md` | `d2bfb87f5cb50bb017b6c14e9cd5a57e2295ca1b`; authoritative anti-loss disposition |
| `decisions/PWV22_PI_PACKAGE_HANDOFF_R7.md` | `5a1746626b25a2b4e8a48e75a0d9891d70a2218d`; accepted R7 package/handoff decision |
| `definition/PWV22_PI_PASEO_QUALIFICATION_R6.md` | `0a9ac3dad9abeecbdd904e87802d8c9044f5df6e`; architecture evidence, not product authority or release acceptance |

The R7 requirements artifact retains an R6 title; the exact Definition locator, R7 section and numbered requirements govern. No semantic authority is inferred from that stale heading. The complete requirements/decisions override summaries here. R6 qualification covers isolated P0–P6, not the eventual package or current production configuration. Its recorded MCP/relay drift must be addressed in the deployment owner's bounded work, not silently considered fixed.

P1 and its prior GREEN Review remain immutable history. They predate universal Final Qualification, safe deferred findings, native Pi realization and official packaging. P3 is a material corrective re-entry, not `editorial_exempt`: a new exact A/B/Plan Review/C progression is mandatory. P3 preserves P2 scope, milestones, requirement coverage and release barriers except for the S07→S08→R03 ordering correction below. P3 neither accepts itself nor authorizes execution before independent GREEN review, Planning approval and C.

### Cycle-3 ordering correction — S07 → S08 → R03

S07's exact durable Result representation is an implementation input to S08. Once the S07 producing Card has its own REQUIRED independent GREEN acceptance and its exact Result path/commit/blob is read back, Execution Prep may consume that S07 Result to materialize/refine S08 and S08 may execute. This bounded implementation-input consumption does **not** assert that the composed S07/S08 surface is accepted.

R03 remains REQUIRED for the composed S07/S08 acceptance surface. No downstream consumer whose authority requires the composed S07/S08 surface may consume that composition until S08 has its exact durable Result and R03 independently accepts the exact composed subject. Thus R03 is a post-S08 composition gate, not a prerequisite for S08 consuming independently accepted S07.

Any Card/JIT wording that requires R03 before S08 can consume S07 is superseded by this correction. Constituent S07 independent acceptance remains mandatory; DONE alone is insufficient.

## 2. Governing workflow, repository boundaries and prerequisite

### Existing governor versus product under construction

This existing non-native workstream continues under current `elmakus/project_workflow_v2@main`, observed at `4fb4bfb7d7b1481d6f347c182fc96a5a1135e045`. Its published router/owner modules govern actual state records and A/B/C transitions. New native C advice, D, Final Qualification semantics, release admission and schemas are product deliverables exercised in disposable fixtures; do not invent those fields in the current V2 records or self-adopt a candidate release. P2's explicit Final Qualification Handoff is also an accepted program authority boundary before S20.

The product and official Pi package source belong in `elmakus/project_workflow_v2`. The consumer holds this plan and program authority/Results/review/effect evidence. `elmakus/pi-unraid` owns runtime configuration and Pi package installation/pinning/update/rollback/readback; changes there require its own legal branch/workstream binding and exact accepted results before consumption here. This planning entry does not select or mutate that project or authorize a live deployment. The prior orchestration-runtime is frozen/archived prior-art and invariant/fault-test donor only; its scheduler, journal, roles, queue, worktree manager and control plane are not resumed.

Use isolated product contribution branches with refreshed exact bases and bounded write scope. Preserve the live default-branch governor through consumer Close. Publish PWv2.2 to a versioned release ref plus an immutable official tag/package, without replacing the current default governor as a side effect. Default-channel replacement and legacy consumer adoption remain separately owner-authorized operations. The package must still be a complete usable official release with exact provenance; a candidate branch name does not grant official status.

### Donor boundary: hold **all Initial Execution Prep**

Accepted ADR requires the separate pre-M03/M02Q donor boundary to finish before PWv2.2 Initial Execution Prep. Planning and independent Plan Review may finish now, but **no execution Cards, Task Board or initial JIT materialization may be created until exact terminal donor proof is read back**. Do not weaken this to a dependency on S05 alone, and do not infer completion from all current Cards being DONE.

Read-only observations on 2026-09-28: consumer donor branch `work/pwv21-policy-kernel-brainstorming` resolved to `147aca1eebf2f753788dfb72bea812dbb936597d`; its Board revision 275 includes DONE M02Q-T30/T31/T32. Product donor branch `work/pwv21-policy-kernel` resolved to `5352386e4328c967543c1b6cce6ebf80d54b4b88`. These observations are not terminal milestone composition/review/close proof. Before Initial Prep, refetch both repositories and bind the exact accepted terminal pre-M03 package and completion/readback evidence; missing proof is a concrete external prerequisite, not permission to repair or close the donor here. S03 later qualifies reusable source properties; it does not replace this pre-Prep gate.

Never materialize donor M03 or wait for a full PWv2.1 M03–M07 release. No legacy GREEN/DONE or migration semantics transfer into native PWv2.2.

## 3. Strategy, scheduling and materialization rules

| Milestone | Seams | Exit / consumption gate |
|---|---|---|
| M01 — Native foundation | S01–S05 | Spec/oracle/release contracts, qualified donor inventory and native identity/admission/guarded writes; R01 GREEN |
| M02 — Semantic behavior | S06–S11 | Routing/preparation/qualification law, Results, parallelism, Review/findings, Recovery/effects/Close compose; R02–R06 GREEN |
| M03 — Required delivery | S12–S17 | ChatGPT bootstrap, helper, official Pi package and pi-unraid interface; both-host and destructive-recovery acceptance; R07–R09 GREEN |
| M04 — Final Qualification | S18–S24 | Candidate freeze, mandatory handoff, cleanup, targeted/global discovery, reconciliation/repair and fresh final acceptance R10 |
| M05 — Publication / Close | S25–S26 | Official release/package provenance and deployment-boundary readback, consumer integration/readback and durable completion |

Milestones are labels, not automatic Review or user stops. Mutating program Cards execute serially under the current governor. Product finite-parallel semantics are qualified on isolated fixtures; the Plan does not use future product semantics to authorize live concurrent program Cards. Product repair swarms are tested with explicit finite admission; actual program repairs remain serial unless governing authority later expressly allows otherwise. An isolated test with multiple actors is one bounded test obligation, not multiple competing workflow owners.

Each seam below is a planning unit, **not a Card**. Initial Prep, only after Plan approval/C/donor proof, checks every seam against current truth and eagerly materializes every stable contract. `materialization_ready` means its substantive scope and acceptance are knowable now, even if execution must await exact predecessor bindings. A future SHA alone is not a JIT reason. `jit_dependent` identifies a concrete future output that determines substantive write/acceptance scope. Bounded triggers materialize as soon as that fact becomes durable. No speculative placeholder Cards or convenience deferral.

Split seams into cohesive Cards where ownership/write domains differ, without erasing acceptance surfaces. In particular S10 recovery/effects/evolution/Close, S15 distribution versus deployment, and S23 repair versus integration must not become mega-Cards. Every materialized Card specifies its own write/effect envelope, tests, exact authority/Result inputs and review rationale. Routine later JIT is deterministic bounded refinement; genuine strategy ambiguity returns to Planning, not stronger-model improvisation.

### M01 — foundation

| Seam | Outcome, scope and decisive checks | Classification / reason | Exact inputs and review |
|---|---|---|---|
| S01 — Native semantic specification | Define small state owners, typed transport-neutral Obligation/Result JSON, exact identity/material inputs, native release admission, transition ownership and acceptance surfaces for all 97 requirements. Specify findings separately from binary verdicts and keep runtime metadata non-authoritative. Produce consumer spec for product assembly. | `materialization_ready`: complete authority and acceptance are already durable; donor/API shape is not needed to specify law. | R7 authority; composition checked at R01/R06, no extra review for prose-only sub-Cards. |
| S02 — Independent spec-derived oracle/corpus | Derive positive/negative/interruption cases and expected normalized outcomes from requirements, without calling the production router to generate expected answers. Include deliberately incorrect implementations/outcomes to falsify the oracle. Host adapter bindings come later. | `materialization_ready`: behavior is knowable from R7 now; absence of future implementation APIs does not defer case design. | R7; oracle independence checked R08/R09. |
| S03 — Donor source qualification | Read accepted terminal pre-M03 identities, identify reusable files/APIs/tests and exclusions under each anti-loss disposition, rerun cheap regressions. Reject nonterminal/missing composition proof and inherited workflow status. Read-only donor access, consumer evidence output. | `materialization_ready`: qualification procedure, boundary and acceptance are known; execution waits for terminal proof. Pre-Prep hold in §2 applies first. | Exact terminal donor package; R01 checks consumed inventory. |
| S04 — Release, delivery and handoff contract | Specify official commit/tag/package provenance, exact-release compatibility, candidate/official distinction, supported distribution interface, remote-head handoff/worktree procedure and effect intent/readback checks. Define minimal persistent ChatGPT instructions and all four transfer directions. Include late attended-action checklist, no secrets. | `materialization_ready`: R7 fixes the complete contract; actual package layout is a later implementation output. | R7 and qualified R6 evidence; R01/R07/R10 check fulfillment. |
| S05 — Native admission/identity/guarded mutation | Build isolated native foundation using qualified inventory. Validate bounded owners, exact repo/commit/path/blob, one official epoch per lineage, expected-old/CAS plus target readback and Git-native atomic multi-file transitions. Test races/crashes, wrong identities, unsupported/legacy admission and no partial publication. | `jit_dependent`: S01 native field interfaces, S03 reusable API inventory and S04 provenance envelope determine the cohesive implementation patch. Trigger: accepted S01/S03/S04. | S01+S03+S04; R01 REQUIRED before foundation consumption. |

### M02 — semantic core

| Seam | Outcome, scope and decisive checks | Classification / reason | Exact inputs and review |
|---|---|---|---|
| S06 — Owner routing, preparation and qualification law | Implement Intake/Research/Brainstorming/Definition/Planning routing, mandatory owner-dispositioned Simplification Review, exact A/B/C/D and Initial Prep eager materialization. Native C recommends strong reasoning; D binds prepared/read-back subject before first Execution. Encode mandatory Final Qualification Handoff and ordered qualification obligations without a new lifecycle stage or universal state file. Reject stale gates, convenience JIT, auto-promotion, repeated consumed returns and skipped qualification. | `jit_dependent`: S05's concrete owner/publication interface determines gate binding and transition patches. | S05/R01; R02 REQUIRED high-risk owner/gate surface. |
| S07 — Results, material-local freshness and readiness | Implement typed JSON interchange, exact accepted predecessor Result consumption, immutable result history and derived readiness/frontier. Test wrong repo/path/blob, DONE without Result, unrelated preservation, affected-cone staleness and durable completion recovery without replay. | `jit_dependent`: S05 identity/guarded-write APIs determine Result and dependency representation. | S05/R01; constituent S07 implementation must receive its own REQUIRED independent GREEN acceptance before S08 consumes its exact Result; composed acceptance remains R03/R06. |
| S08 — Finite parallel legality / fan-in | Implement explicit finite exact admission, deterministic write/resource/semantic/effect conflict checks, uncertainty/overlap serialization with no override, one mutating owner per Card and exact sibling integrated compatibility. Test disjoint text with semantic mismatch, unknown effects, revoked admission and sibling-local invalidation. | `jit_dependent`: independently GREEN S07 exact material-input/Result representation determines claims and integration operands; S08 may materialize/execute from that exact S07 Result before composed R03. | Exact independently accepted S07 Result is the S08 implementation input; R03 is REQUIRED after S08 for the composed S07/S08 surface and before any downstream composed-surface consumer. Native fixtures, not live program parallel admission. |
| S09 — Review, findings and convergence | Implement subject-driven binary GREEN/RED Review, author/repairer exclusion, append-only attempts, narrow reviewer publication and deterministic CAS/readback finalizer. Findings remain separate: acceptance-falsifying defect forbids DONE; otherwise positive safe-continuation proof and first-consumption/latest-safe boundary govern deferral. Unknown impact fails closed. Test local blocking, fresh closure after material repair and ceilings 5/4/3 plus 3 failed repair→closure rounds per defect class; ceilings change mode, never accept RED. | `jit_dependent`: S07 subject/material relationships determine attempt/finding bindings, defect history and affected cones. | S07; R04 REQUIRED high-risk acceptance surface. |
| S10 — Recovery, external effects, native evolution and Close | Implement exact-owner recovery, mechanical repair versus real owner choice, intent→attempt→readback→known/UNKNOWN and stable idempotency where supported. Classify native updates preserve/revalidate/stale/Recovery; unchanged implementation retains exact Result with new acceptance evidence. Close needs accepted integration/publication/readback/durable confirmation. Reject blind retry, secrets, legacy normalization and post-activation downgrade. | `jit_dependent`: S06 gate/return state and S09 acceptance/finding records determine safe recovery and closure boundaries. Split distinct ownership domains at Prep. | S06/R02 + S09/R04; R05 REQUIRED. |
| S11 — Integrated native lifecycle | Compose S06–S10 with all required constituent verdicts. Exercise happy path and interrupted repair/qualification/gate/effect/Close paths; bind explicit multi-Result compatibility, without replacing required constituent Reviews. | `jit_dependent`: actual sibling APIs, schemas and composition conflicts determine integration patch/test scope. | S06+S07+S08+S09+S10 and R02–R05; R06 REQUIRED before delivery consumes core. |

### M03 — host realization and release acceptance

| Seam | Outcome, scope and decisive checks | Classification / reason | Exact inputs and review |
|---|---|---|---|
| S12 — ChatGPT bootstrap / universal handoff | Deliver minimal persistent instructions (workflow/router, consumer, non-authoritative Coordinator Protocol locators only), runtime-neutral stops/handoffs and canonical receiver reconstruction. Research/Brainstorming may execute on ChatGPT with exact durable returns; no transient state in Project Instructions. Implement the transfer/freshness cases in §5. | `jit_dependent`: S11 entry/stop/result API and S04 envelope determine concrete host delivery changes. | S04+S11/R06; R08 integrated host acceptance. |
| S13 — Qualified thin PW/Pi helper | Implement only assignment/authority/generation fences, branch/workspace correlation, exact Result ancestry/output validation, stale rejection, Review path/frozen-subject gates, accepted finite-admission checks, deterministic fan-in/compatibility binding and bounded cleanup/readback. Use native Paseo lifecycle, not a scheduler/queue/journal. Tests reproduce P2–P6 failures and deletion/reconstruction of helper-local state. | `jit_dependent`: S11 exact native Result/Review/admission contracts determine helper inputs and permissible publication envelope. P0–P6 bounds responsibility, not executable native API. | S11/R06 + R6 evidence; R07 REQUIRED high-risk runtime/publication boundary. |
| S14 — Official Project Workflow for Pi package | Build/install a release-pinned Pi package bundling bootstrap/skill/instructions and S13 helper; normal Pi source only when provenance/compatibility match the exact applicable official release. Fallback to canonical Git when missing/incompatible. Assert the same normalized semantics on both paths. No independent updater or semantic state store. Test install/uninstall/reinstall, absent/wrong/tampered identity and offline/unavailable-source fail-closed behavior. | `jit_dependent`: S13 helper entrypoints, S11 core surface and S04 provenance manifest determine actual package inventory/build/install checks. | S04+S11/R06+S13/R07; R07 package boundary plus R08 installed-host acceptance. |
| S15 — pi-unraid distribution/configuration integration | Through separately bound pi-unraid work, extend existing distribution/regression mechanisms to pin/read back package and stack versions; persist/read back `daemon.mcp.enabled=true` and `daemon.mcp.injectIntoAgents=true`, preserve/read back explicitly desired relay policy. Prove Pi Main/children receive required tools. Test deployment interruption, drift, update and compatible rollback without package self-update. Fixture-first; live writes require exact target/effect authority. | `jit_dependent`: S14 artifact/install contract and fresh pi-unraid mechanism/config inspection determine bounded edits and live effect scope. Missing access is a blocker, never reason to create a second updater. | S14 + accepted exact pi-unraid Result(s); R07 interface integrity / R08 actual host readback. |
| S16 — Required-host semantic acceptance | Run S02 shared behavioral corpus on ChatGPT and installed Pi/Paseo, including compatible-package and canonical-fallback paths. Bind exact package, fixture, authority, environment/config and observations. Test four-direction handoffs, Review contamination, busy-message interruption, lifecycle descendants, stale generations, explicit finite admission and semantic-conflict fan-in. Pi-local Research/Brainstorming is not required. | `jit_dependent`: S12–S15 establish actual entrypoints/configurations and observation paths; a simulated Pi response cannot prove live injection/lifecycle behavior. | S02+S12+S13+S14+S15; R08 REQUIRED integrated host acceptance. |
| S17 — Canonical sufficiency / destructive recovery / no-legacy | On disposable fixtures remove chat/session/runtime state, caches/projections/helper-local state and reconstruct from native canonical Git plus published contracts. Compare to S02 independent oracle. Cover pending gates/results/attempts, deferred findings, UNKNOWN effects and interrupted Close. Hard-negative historical PWv1/v2.0/v2.1, unbound/malformed/unsupported inputs must produce no mutation, inheritance or migration. | `jit_dependent`: S10/S11 native persistence and S16 host surfaces determine exact deletion/retention and observation boundaries. Never delete real project state. | S02+S10/R05+S11/R06+S16/R08; R09 REQUIRED. |

### M04 / M05 — Final Qualification, publication and Close

| Seam | Outcome, scope and decisive checks | Classification / reason | Exact inputs and review |
|---|---|---|---|
| S18 — Exact release candidate assembly | Assemble policy, native validators/router, templates/tests/tooling, ChatGPT surface, Pi package and provenance inventory; bind compatible pi-unraid realization evidence. Reproducibly reconstruct package; check no secrets, hidden services or duplicate state. Freeze exact package commit and record external acceptance bindings without self-referential commit hashes. | `jit_dependent`: S11/S14/S16/S17 determine actual inventory and scoped evidence. | S04+S11+S14+S16/R08+S17/R09; R10 checks final fulfillment. |
| S19 — Mandatory Final Qualification Handoff | Stop once, before Known Defect Cleanup, at an exact candidate/qualification obligation. Publish universal remote-fenced locator for an authorized non-Pi/Paseo-window coordinator. This is a handoff, not acceptance or a new lifecycle stage. After explicit continuation, no extra user stops unless another genuine authority/access/effect boundary arises. | `materialization_ready`: exact boundary, source and receiver obligation are fully known; future candidate identity is a binding, not unknown scope. Execution waits for S18. | S18; §6 ordered protocol. Current Pi/Paseo realization ends here. |
| S20 — Known Defect Cleanup | Reconcile every durable open current-scope finding, exact affected acceptance/property and latest-safe repair boundary. No findings means explicit zero-work pass. Repair/reclassify within authority or route to its owner; acceptance violations cannot be hidden by reclassification. Newly evidenced repairs are separate bounded Cards. | `jit_dependent`: actual S18 finding set and handoff-boundary readback determine cleanup/repair scope; no speculative repair Cards. | S18+S19 satisfaction; cleanup/readback must precede subsequent discovery. |
| S21 — Targeted Bug Hunt | Proportional adversarial discovery with risk/coverage model covering material Cards, integration seams, cross-cutting invariants and negative spaces, especially provenance/CAS, deferral cones, review and Pi lifecycle. Fresh eligible discovery contexts, exact candidate/evidence and coverage gaps recorded. No fixed worker count. | `materialization_ready`: risk classes and discovery acceptance are specified now; candidate and completed cleanup bind at launch. | S20 exact resulting candidate; discovery only, no acceptance verdict substitution. |
| S22 — Global identical-prompt Bug Hunt | Independent isolated runs of the same broad adversarial prompt over one exact frozen post-cleanup candidate; positive run count selected by owner/runtime. Bind prompt/subject and each finding result. Duplicate count, voting or zero findings never accepts a candidate. | `materialization_ready`: discovery protocol/coverage/acceptance are fully known; subject and positive run count are launch facts. | S21 discovery complete, same frozen candidate unless material change requires refreeze/affected rediscovery; discovery only. |
| S23 — Integrated findings / bounded repair / serial integration | Reconcile S21/S22 findings with prior durable findings into one evidence-linked set; classify genuine defects, duplicates, non-defects and scope questions with reasons. Create repair Cards only once stable contracts are known; one integration owner composes exact repair Results in accepted order, workers never self-merge/accept. Apply material-local preserve/rerun/revalidate/Review/stale/Recovery dispositions after repair, respecting earliest consumption/latest-safe boundaries. Test parallel repair realization only in admitted native fixtures; actual program scheduling remains serial. | `jit_dependent`: discovery outputs determine defect scope, dependencies, shared candidate changes and necessary revalidation; zero defects does not invent repairs. | S21+S22+prior findings+actual repairs; constituent high-risk Reviews retained; R10 requires final reconciliation evidence. |
| S24 — Fresh final full-scope acceptance | Freeze final candidate after repairs and sufficient material-local revalidation, verify complete requirements/release checklist and fresh required-host/Recovery acceptance. Obtain eligible independent full-scope binary verdict. Original reviewers may verify known findings while eligible but material repair requires fresh final closure. No unresolved current-release violation, unknown impact or contradictory/stale proof may pass. | `jit_dependent`: S23 actual repaired subject/impact graph determines closure scope and reruns; closure method itself is fixed. | S23 + affected core/host/recovery evidence + S04; R10 REQUIRED final acceptance. |
| S25 — Official release / package / target readback | Guard publication of exact reviewed release ref/tag/package, verify target prior state and effect authority, then read back commit/tag/artifact/provenance. Validate real official admission in a disposable native fixture; no automatic adoption of this consumer. Consume pi-unraid distribution/readback through its owner where deployment is in authorized release scope; do not publish a package privately updating itself. | `jit_dependent`: S24 accepted candidate plus actual repository/artifact/deployment targets determine effect envelope, CAS/readback and attended actions. | S18+S24/R10+S15, exact target authorization/access; material publication change returns to affected acceptance before publication. |
| S26 — Consumer integration and durable Close | Integrate namespaced authority/evidence/results into refreshed consumer target, preserve required recovery records and read back exact target contents. Confirm release obligations, effects, findings and deferred register dispositions; only then durable approved-scope completion. Branch/chat termination is not Close. | `jit_dependent`: S25 exact publication/readback and real consumer merge state determine integration/conflict/effect checks. | S25 plus actual consumer target; mechanical close from accepted evidence, new material conflict repair needs affected acceptance. |

All dependency edges mean exact **accepted Result identity**, not mere DONE or a URL. Before any multi-input consumption, verify explicit integrated compatibility over the composed subject and retain each required constituent verdict. A material input change stales only affected obligations; unrelated results remain usable. Readiness/finite admission are distinct: no dependency does not imply permission to parallelize.

## 4. Subject-driven Review and finding safety

| Surface | Required independent acceptance subject | Native product ceiling to implement/test |
|---|---|---|
| Stage-6 P2 | Exact frozen Plan repo/commit/path/blob, cycle 2, R7 authority | Current governor's Plan Review law, not candidate rules |
| R01 | S05 native admission/identity/CAS plus S01/S03/S04 composition | Integration: 4 discovery epochs |
| R02 | S06 routing, A/B/C/D, eager Prep and mandatory qualification boundaries | Local/high-risk: 5 |
| R03 | S07/S08 Result/dependency/finite-admission/fan-in semantics | Integration: 4 |
| R04 | S09 independence, attempt/finding persistence, truthful DONE and ceilings | Local/high-risk: 5 |
| R05 | S10 effects/Recovery/evolution/Close composed with gates and findings | Integration: 4 |
| R06 | S11 full core lifecycle and multi-input compatibility | Integration: 4 |
| R07 | S13 helper and subsequent S14/S15 package/distribution trust boundary | Local helper: 5; composed delivery: 4 |
| R08 | S16 exact installed-host observations, fallback parity and independent oracle validity | Integration: 4 |
| R09 | S17 destructive sufficiency and no-legacy negative evidence | Integration: 4 |
| R10 | S24 exact final release candidate, reconciled findings, repair/revalidation and full-scope acceptance | Final closure: 3 |

R07 has staged exact subjects: helper acceptance must precede package consumption; delivery composition then receives its own exact attempt against changed inputs. No single early helper verdict is reused as acceptance of an unbuilt package. Review attempts are immutable and must identify their exact bounded acceptance surface. These are material boundaries, not duplicate administrative Card/Milestone reviews. S21/S22 discovery has no acceptance verdict authority and does not satisfy R10.

For each material defect class, 3 failed repair→closure rounds require mode change/root-cause handling. Native ceilings are product constants to test, not retroactive changes to this consumer's governor. Neither a count nor a zero-finding hunt turns RED into GREEN.

Routine documentation, fixture data or mechanical sub-Cards can finish from exact Results/tests/readback when Prep establishes no distinct independent acceptance surface; name the downstream material acceptance explicitly. High-risk Cards cannot evade review by splitting them. A material author/repairer cannot independently accept the exact subject. Reviewers may append only their assigned Attempt/verdict/evidence; a narrow deterministic finalizer validates/CAS-publishes/read-backs only the mechanically implied transition and cannot select work or widen authority.

Safe-deferral proof binds finding, exact property/acceptance, material dependencies, permitted unaffected continuation and exact latest-safe boundary. If acceptance is falsified, the Card cannot be ordinary DONE. If continuation could consume the defective property, it must wait. Unknown impact means fail closed, not optimistic deferral. Repair occurs at the earlier of first affected consumption or latest-safe boundary, always before final acceptance/publication for a current-release defect. Blocking is local to the materially affected cone. Open out-of-scope findings need explicit owner disposition; no silent renaming of current-release defects as future work.

## 5. Delivery, handoff and Pi/Paseo acceptance

### Official package and fallback

Package version/build metadata resolves to one exact official semantic release/policy and covered tests/tooling. Verify compatibility with the consumer's applicable release before routing; package presence or latest version alone is insufficient. Missing/incompatible package selects canonical Git fallback at the required supported release, not arbitrary latest semantics. If neither path can establish supported exact provenance, fail closed. Test installed/fallback normalized outcomes and provenance tampering independently. Candidate package tests use an isolated fixture trust catalog; only S25 official publication/readback establishes real official identity.

The Pi package contains bootstrap/skill/instructions and qualified helper code, not its own updater, scheduler, semantic queue/journal, Board, database or authoritative cache. Native Paseo remains responsible for agents, workspaces/worktrees, execution, status, messaging and stop/archive mechanics. Helper-local correlation data is disposable. Production pi-unraid distribution owns installs/pins/updates/rollback/readback; rollback of runtime delivery cannot semantically downgrade an already activated native lineage. If the selected package no longer supports the bound epoch, routing fails closed into Recovery rather than accepting old semantics.

### Universal receiver procedure and test matrix

All ChatGPT→Pi, Pi→ChatGPT, Pi→Pi and ChatGPT→ChatGPT handoffs use the same small bootstrap and locators: compatible official package first, otherwise `elmakus/project_workflow_v2`; consumer repo, exact branch, exact handoff commit, entry obligation, durable pointer. No chat narrative, acceptance summary or runtime identity is authority.

Receiver acceptance must demonstrate:

1. Fetch remote and compare exact branch HEAD to the handoff commit before using the snapshot. Equal → reuse/reset the existing slot to that exact remote commit. Moved → stale handoff, reconstruct current canonical state, never force remote back or silently continue old work.
2. Older local checkout, dirty files and local-only commits do not count as accepted continuation/Results. Superseded local residue may be discarded only after excluding unresolved external effects and current canonical obligations bound to it. Do not salvage it by default via merge/stash.
3. One ordinary active worktree slot per branch is reused/recreated; intentionally admitted distinct concurrent Cards/owners use distinct branches/worktrees. No duplicate same-branch recovery clone merely to avoid confronting residue.
4. External effects survive local disposal. Reconcile intent/attempt/readback and UNKNOWN before destructive cleanup; loss of a worktree cannot erase a deployment/API/database/message effect.
5. A remote move between initial fetch and guarded publication is rejected; refetch/re-evaluate. Local commit creation is candidate assembly, never durable acceptance before remote publication/readback. Exact Result artifact blobs must be reachable from the canonical published refs.
6. Missing branch/commit/pointer, wrong repository, divergent scope, unsupported release or ambiguous effect state fails closed to the owning recovery/blocker; no invented state or blind retry.

### Native runtime regressions from qualified evidence

S13/S16 must reproduce detect-and-reject publication integrity: frozen-subject mismatch or non-review implementation edits invalidate a Review branch; valid own-attempt/evidence changes alone can be mechanically published after independent diff/readback. No universal physical sandbox is claimed. P7 becomes required only if a later accepted obligation explicitly demands hard OS/filesystem/network/credential prevention.

Main-mediated peer communication is default; explicitly admitted non-independent exchanges cannot transfer scope/authority. Pre-verdict implementer↔Reviewer contact invalidates the attempt. Busy-agent messages are wakeups/interruption-prone transport, not a semantic FIFO/task queue. Verify status/readback, stop→readback→archive and explicit descendant reconciliation, including cross-workspace detached children and surviving dirty worktrees. Parent archive is not cascade cleanup. Restart recovery must correlate exact assignment/branch/workspace against authority, reject superseded generation output and avoid replay of a remote-durable result after lost notification.

Pi Main may coordinate ordinary Execution/Review/bounded repair/admitted fan-in and Recovery only until S19. Final Qualification after handoff is outside this Pi/Paseo realization window; handing to a fresh Pi agent does not extend that accepted window. ChatGPT is an available required host for that later coordination. Worker counts, provider/model/session IDs, branch/run allocators and prompt launch mechanics remain runtime metadata, never acceptance or a second state machine.

## 6. Final Qualification, evidence and release barrier

The product must impose the same proportional qualification obligation on **every** managed change, including small ones, and this program follows it explicitly:

`S19 mandatory handoff → S20 Known Defect Cleanup → S21 Targeted Bug Hunt → S22 Global identical-prompt Bug Hunt → S23 integrated findings / bounded repair / serial integration / material-local reconciliation → S24 fresh independent acceptance → S25 release/readback → S26 Close`.

Targeted risk coverage includes all material owners and handoffs, exact identity/CAS/remote-fence races, finding cones, Review eligibility/persistence, convergence exits, unknown effects, package provenance/update boundaries, runtime injection/messaging/lifecycle, native evolution and legacy rejection. Record uncovered risk explicitly; a fixed universal worker count is not a coverage model. Global runs share the exact frozen candidate and identical prompt but remain independent/isolated. Positive run count is chosen proportionally outside canonical law. Consolidate evidence rather than voting. If the candidate changes between discovery passes, bind new identity and rerun affected discovery; never aggregate mismatched subject evidence as one frozen pass.

Native repair-swarm acceptance must show explicit finite admission plus conservative write/semantic/effect conflict checks, serialization on uncertainty, exact repair Results, no worker self-merge/accept and one serial integration mutator. After any material repair, compute affected surfaces and choose the least costly sufficient preserve/rerun/revalidate/focused-or-full Review/stale/Recovery disposition. Unchanged implementation retains Result identity; actually changed or genuinely re-executed output creates a new Result. Append attempts/evidence; never edit historical failures. Fresh final full-scope R10 is mandatory even if hunts find nothing; material repair requires a fresh eligible reviewer rather than closure by the repairer.

Release barrier: no unresolved current-release finding, pending affected revalidation, contradictory/unknown evidence, stale required-host/Recovery proof or failed MUST-semantic acceptance. Semantic release shared fixtures must pass on **both ChatGPT and Pi/Paseo** for the final exact candidate. Reuse requires unchanged property, authority and relevant environment with exact bindings; rerun cheap checks when reuse proof is harder. R6 prototypes cannot substitute for package-era host tests. Falsification-first checks are SHOULD where meaningful, not an invented legality condition.

Release publication is Git-native with explicit expected-old guard/readback; distinguish consumer evidence commits from product/package content. Freeze package contents first, bind tests/reviews externally to that commit, then map the official tag/artifact provenance without embedding a commit's own hash in its hashed contents. Any package-content change after review requires refreeze and affected acceptance. No dedicated non-Git candidate store.

Before native activation, an unaccepted candidate may be abandoned. After official native state exists, defects use fail-closed Recovery and forward corrective PWv2.2 release/revalidation; no downgrade to a prior workflow generation or automatic adoption of old projects. S25 may validate real official admission on a disposable native project, never rewrite this consumer as native.

Attended actions are prepared early but executed as late as dependencies safely allow: arrange host access for S16 without deploying production, batch compatible credentials/publication/distribution readbacks in S25 without merging distinct authorization domains. Store only non-secret recovery/operation identifiers. Missing access/effect authorization is a real blocker; do not invent a deployment permission from this plan. Consumer main integration may trigger historical `auto-patch-tag.yml`; inspect then-current behavior and include consequential tag effects explicitly. That tag is not the PWv2.2 official release identity. No unguarded merge or destructive force-push is authorized.

## 7. Requirement-to-acceptance coverage

Every numbered requirement is assigned below; full exact authority remains normative. A range denotes each requirement in that range, not a waiver of separate assertions.

| Requirement(s) | Primary seams | Decisive acceptance |
|---|---|---|
| 1 | S01/S05 | Bounded semantic owners; orchestration mechanics cannot select legality |
| 2 | S12/S16 | ChatGPT and Pi/Paseo both pass; Codex non-blocking |
| 3 | S01/S09/S17 | Change/remove runtime identity without changing legality/eligibility |
| 4 | S01/S07 | Typed JSON interchange with invalid-input rejection |
| 5 | S05/S07 | Reject wrong repository/commit/path/blob |
| 6 | S07/S11 | DONE without exact accepted predecessor Result cannot authorize consumption |
| 7 | S07/S17/S23 | Affected material cone stale; unrelated work preserved |
| 8 | S05/S25 | Stale expected-old rejected; target readback mandatory |
| 9 | S01/S05 | No universal state file/event ledger |
| 10 | S06 | Board only after implementation; pre-execution owners remain separate |
| 11 | S07/S23 | New execution/repair Result appends immutable history |
| 12 | S09 | Exact append-only attempts; finalization non-semantic |
| 13 | S09/S24 | Author/repairer cannot independently accept exact subject |
| 14 | S06/S16 | Exact A/B/C/D real stops without model-as-authority |
| 15 | S08 | Bounded parallel anti-regression, overlap always serializes |
| 16 | S08/S13 | One mutating ownership domain per Card |
| 17 | S08/S11 | Integrated compatibility plus constituent required Reviews |
| 18 | S06/S13 | Worker follow-on/late output cannot authorize scope |
| 19 | S13/S16 | Unneeded workers/descendants released with readback |
| 20 | S06/S12/S13 | Unique legal next obligation auto-continues until real stop |
| 21 | S09/S10/S23 | In-scope repair automatic; new strategy/authority returns to owner |
| 22 | S09/S24 | Fresh full-scope closure after material repair |
| 23 | S09/S24 | 5/4/3 and 3 failed rounds change mode, never accept RED |
| 24 | S02/S05–S17 | Meaningful fail-first checks where practical, SHOULD not legality |
| 25 | S06 | Material Planning cannot freeze without owner-dispositioned Simplification Review |
| 26 | S06 | Simplification never rewrites active/completed work |
| 27 | S04/S16/S25 | Late safe attended batching preserves distinct authority/risk |
| 28 | S13/S17 | Delete helper/projections without changing legal recovery |
| 29 | S07/S08 | Readiness/frontier derived from minimal direct facts |
| 30 | S06 | Bounded genuinely future-dependent triggers, no placeholders |
| 31 | S10/S25 | Intent/attempt/readback, UNKNOWN and no blind retry |
| 32 | S10/S25 | Stable request/idempotency identifier when supported |
| 33 | S05/S10/S18 | No secrets in canonical package/effect records |
| 34 | S16/S17/S23 | Property/authority/environment-scoped reuse or rerun |
| 35 | S05 | Atomic guarded Git multi-file publication and readback |
| 36 | S05/S18 | Git-native candidate isolation, no dedicated backend |
| 37–39 | S05/S17/S25 | No legacy continuation/migration; old-project adoption separately authorized |
| 40 | S10/S23 | Native preserve/revalidate/stale/Recovery classification |
| 41 | S04/S18/S25 | Official commit/tag covers policy, tooling/tests and package provenance |
| 42 | S16/S24 | Shared behavioral acceptance on both hosts for final semantic candidate |
| 43 | S24/S25 | MUST/Recovery/required-host failures block release |
| 44 | S10/S17 | Canonical reconstruction; mechanical repairs vs genuine owner choice |
| 45 | S10/S25/S26 | Integration/readback/durable confirmation before Close |
| 46 | S04/S26 | Deferred register remains visible until implemented/rejected |
| 47 | S01/S03 | Direct-pivot anti-loss without full PWv2.1 dependency |
| 48 | S06 | All knowable seams eagerly materialized after applicable gates |
| 49 | S06/S12/S16 | Native C recommends strong Initial Prep, identity advisory |
| 50 | S06/S16 | Exact prepared-state D before first Execution, no duplicate confirmation |
| 51 | S06 | Routine JIT bounded; strategy uncertainty escalates to Planning |
| 52 | S09/S11/S24 | Subject-driven topology, no Card/Milestone-only duplicate review |
| 53 | S06/S21/S22/S23 | Universal targeted + global discovery and reconciliation |
| 54 | S08 | Explicit finite exact admission, representation neutral |
| 55 | S05/S10 | One applicable native epoch per active lineage |
| 56 | S10/S23 | Unchanged implementation preserves Result identity under revalidation |
| 57 | S09/S13 | Reviewer own attempt only; finalizer cannot choose downstream work |
| 58 | S12/S16 | Shared Research/Brainstorming obligations; ChatGPT execution allowed |
| 59 | S05/S14/S25 | Exact official native provenance resolved before ordinary route |
| 60 | S02/S17 | Destructive isolated reconstruction versus non-circular oracle |
| 61 | S10/S25 | Pre-activation abandon; post-activation forward correction, no downgrade |
| 62 | S02/S17 | Historical negative fixtures leave state unchanged and inherit nothing |
| 63 | S01/S03/S24 | Every anti-loss family mapped to accepted disposition |
| 64 | S09 | Only GREEN/RED; findings orthogonal, no conditional acceptance |
| 65 | S09/S20 | Acceptance-falsifying finding forbids DONE; safe deferral needs positive proof |
| 66 | S09/S23 | Local blocking; repair before first affected use/latest-safe boundary |
| 67 | S06/S19 | Mandatory handoff before cleanup on every managed change |
| 68 | S06/S20 | All open findings reconciled; explicit zero-work when empty |
| 69 | S21 | Targeted adversarial coverage proportional to accepted risk model |
| 70 | S22 | Positive independent identical-prompt runs, frozen subject, no vote/zero-findings acceptance |
| 71 | S08/S23 | Finite admitted repair units, uncertainty serializes, one integration owner |
| 72 | S10/S23 | Local impact disposition and immutable history/Result-preserving revalidation |
| 73 | S24/S25 | Fresh independent exact final acceptance plus unresolved/stale/unknown barrier |
| 74 | S13/S21/S22 | Swarm counts/IDs/allocators remain runtime metadata, not workflow truth |
| 75 | S01/S05/S18 | Git only; no Projects/Linear canonical or projection subsystem |
| 76 | S04/S12 | Stable minimal Project Instructions, transient facts in exact handoff only |
| 77 | S13/S19 | Pi ordinary execution ownership ends at qualification handoff |
| 78 | S13/S16 | Native Paseo substrate via Pi RPC/adapter path |
| 79 | S13/S18 | No speculative third-party subagent/full OR dependency |
| 80 | S13/S17 | Helper limited to qualified gaps, fully reconstructible |
| 81 | S01/S13/S16 | R6 P0–P6 consumed as prior architecture evidence; production deltas freshly tested; P7 only for hard claims |
| 82 | S13/S16 | Main-mediated default; pre-verdict implementer/reviewer contact rejected |
| 83 | S09/S13 | Detect/reject unauthorized publication; no unproven universal physical prevention |
| 84 | S08/S13/S23 | Exactly one integration mutator with accepted Result set/order/scope |
| 85 | S01/S13/S18 | Prior OR remains archived donor, no resumed backlog/control plane |
| 86 | S13–S16 | Qualified native + config/skills + thin-helper realization |
| 87 | S13/S17 | Enumerated helper responsibilities; no competing semantic queue/authority |
| 88 | S15/S16 | MCP enabled/injection persisted and actually read back; drift blocks host qualification |
| 89 | S13/S16 | Busy messaging not FIFO; explicit stop/archive/descendant cleanup readback |
| 90 | S14/S18/S25 | Official installable Pi package ships in 2.2.0, not deferred |
| 91 | S14/S16 | Compatible official package first; exact canonical fallback parity |
| 92 | S04/S12/S16 | Universal self-bootstrap in all four transfer directions |
| 93 | S12/S14/S16 | Exact remote handoff commit fence; moved branch reconstructs |
| 94 | S05/S12/S14 | Local-only work cannot be accepted Result/continuation truth |
| 95 | S13/S16 | Superseded residue reset only after canonical/effect safety checks |
| 96 | S13/S16 | Reuse one ordinary branch slot, no duplicate recovery worktrees |
| 97 | S14/S15 | pi-unraid owns install/update/rollback/readback; package has no private updater |

### Anti-loss dispositions

| Source family | Retained/superseding seams | Rejected drift |
|---|---|---|
| M03 portability/helper-less recovery/parity | S02/S16/S17, independent oracle and normalized hosts | Successful legacy migration as acceptance |
| M04 finite parallel/ownership/claims/fan-in/locality | S07/S08/S11/S13 | Canonical workers/scheduler; mandatory named parallel-set |
| M05 independent Review/repair/ceilings/fresh closure | S09/S23/S24 | Blanket per-Card review or runtime-identity eligibility |
| M06 continuation/premium/handoff/Prep | S06/S12/S14/S16 | Provider/model/session policy as law |
| M07 Recovery/effects/evolution/Close | S10/S17/S25/S26 | Legacy readers/normalization/migration/DONE inheritance/downgrade |

## 8. Deferred and excluded register

S26 must preserve these dispositions durably. None permits deferring a current-release MUST failure.

| Item | Disposition / owner | Reconsideration trigger |
|---|---|---|
| Mixed native epochs in one active lineage | DEFER beyond 2.2.0; Definition | Concrete use case and accepted new Definition |
| Codex required-host status | OPTIONAL/non-blocking; Definition | Explicit restoration |
| Pi-local Research/Brainstorming | OPTIONAL; host realization | Demonstrated need without changing shared semantics |
| Caches/compiler/trace/shadow DAG | OPTIONAL disposable optimization; runtime | Measured benefit and recovery proof |
| Third-party Pi subagent package / full OR | NOT baseline; Definition/runtime boundary | Exact missing primitive/irreducible supervisory-state evidence and explicit authority; R6 did not justify either |
| Universal hard sandbox / P7 | NOT REQUIRED by R7; exact obligation owner | Explicit physical-prevention requirement and corresponding qualification |
| Default governor/channel cutover / legacy consumer adoption | SEPARATE owner-authorized operation after consumer Close | Exact affected-consumer reconstruction/continuity decision |
| Pi/Paseo Final Qualification orchestration | OUTSIDE accepted realization window; Definition | Explicit changed authority, not merely a fresh Pi session |
| New PWv2.2.x capability beyond R7 | UNSTARTED; Definition | Explicit scope acceptance, not worker follow-on |

Rejected: legacy compatibility/migration/downgrade, universal state/ledger, non-Git candidate backend, tracker/dashboard subsystem, runtime identity as authority, full intermediate PWv2.1 M03–M07 release and package-local self-update. Official Pi packaging and universal fenced handoff are **not deferred**.

## 9. Planner completion and exact next stop

Planning-owned pre-freeze Simplification Review: `implementation/workstreams/change-pwv22-program-brainstorming/evidence/SIMPLIFICATION_REVIEW_P3_2026-09-28.md`.
Completeness/challenge audit: `implementation/workstreams/change-pwv22-program-brainstorming/evidence/PLANNING_AUDIT_P3_2026-09-28.md`.

After explicit owner disposition of material simplification findings and GREEN planner audit, commit the plan, publish/read back its exact blob subject, bind that subject in PLANNING.toml with **Premium B due**, and validate the current canonical route. No P2 review locator/verdict authorizes P3. The planner does not review or internally spawn independent review of this plan.

The next real stop is **Premium B / fresh independent Stage-6 Plan Review of P3**. Approval/C, donor-boundary proof and Initial Prep remain downstream. This planning task creates no execution Card/Board, product implementation, release, deployment or native activation.
