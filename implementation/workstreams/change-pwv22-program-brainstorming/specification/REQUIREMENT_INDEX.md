# PWv2.2 requirement and anti-loss index — M01-S01-T01

Card: `M01-S01-T01`. Consumer specification only; not product implementation/native activation.

## Exact source binding
- R7: `requirements/PWV22_PROGRAM_R7.md@486685f17bb4a022e6dfed89383f8b9744b668fa:f326a0778915cfed5ddcecc735f19b59dfd63051`
- ADR: `decisions/ADR_PWV22_PROGRAM.md@486685f17bb4a022e6dfed89383f8b9744b668fa:c1b5f21e91649566525dae1dfbe57b4e40c04d22`
- Anti-loss: `decisions/PWV22_M03_M07_DISPOSITION_R4.md@486685f17bb4a022e6dfed89383f8b9744b668fa:d2bfb87f5cb50bb017b6c14e9cd5a57e2295ca1b`
- Package/handoff: `decisions/PWV22_PI_PACKAGE_HANDOFF_R7.md@486685f17bb4a022e6dfed89383f8b9744b668fa:5a1746626b25a2b4e8a48e75a0d9891d70a2218d`
- P2: `planning/PWV22_PROGRAM_MASTER_PLAN_P2.md@76c46d59566807a4d0f11832d0c30f3123c0c54e:5524876b49320a1f4da6dd0cf8b0cbc38b31c4fc`

The retained “Definition R6” heading in the R7 file is non-semantic; exact locator plus numbered requirements 1–97 govern.

## Complete 1–97 accounting
| # | Requirement | Primary semantic owner/boundary | Authority | Disposition |
|---:|---|---|---|---|
| 1 | Semantic contract first | semantic specification / bounded owners | R7 §1; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 2 | Host neutrality | bounded semantic owner named by R7/P2 | R7 §2; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 3 | No runtime identity as authority | semantic specification / bounded owners | R7 §3; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 4 | Portable execution contract | semantic specification / bounded owners | R7 §4; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 5 | Exact Result identity | exact identity, Result/material-input and recovery contracts | R7 §5; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 6 | Exact dependency binding | exact identity, Result/material-input and recovery contracts | R7 §6; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 7 | Material-local freshness | exact identity, Result/material-input and recovery contracts | R7 §7; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 8 | Guarded canonical mutation | guarded publication / external-effect owner | R7 §8; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 9 | Small semantic owners | semantic specification / bounded owners | R7 §9; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 10 | Task Board scope | routing / Planning / Execution Prep gate owner | R7 §10; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 11 | Immutable Result history | exact identity, Result/material-input and recovery contracts | R7 §11; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 12 | Append-only Review history | Review/finding/final-acceptance owner | R7 §12; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 13 | Review independence | Review/finding/final-acceptance owner | R7 §13; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 14 | Premium stops | routing / Planning / Execution Prep gate owner | R7 §14; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 15 | Bounded parallelism anti-regression | finite admission / fan-in owner | R7 §15; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 16 | One mutating ownership domain per Card | finite admission / fan-in owner | R7 §16; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 17 | Integrated compatibility | finite admission / fan-in owner | R7 §17; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 18 | No self-authorized scope growth | runtime boundary; semantics constrain, runtime realizes | R7 §18; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 19 | Worker lifecycle expectation | runtime boundary; semantics constrain, runtime realizes | R7 §19; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 20 | Automatic continuation | routing / Planning / Execution Prep gate owner | R7 §20; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 21 | Bounded repair | Recovery/evolution/Close owner | R7 §21; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 22 | Fresh final closure after material repair | Review/finding/final-acceptance owner | R7 §22; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 23 | Review convergence ceilings | Review/finding/final-acceptance owner | R7 §23; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 24 | Falsification-first discipline | qualification/evidence owner | R7 §24; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 25 | Planning-owned Simplification Review | routing / Planning / Execution Prep gate owner | R7 §25; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 26 | Simplification boundaries | routing / Planning / Execution Prep gate owner | R7 §26; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 27 | Human-interaction-last | release/delivery/handoff owner | R7 §27; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 28 | Disposable projections | disposable projection boundary | R7 §28; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 29 | Derived readiness | exact identity, Result/material-input and recovery contracts | R7 §29; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 30 | JIT materialization | routing / Planning / Execution Prep gate owner | R7 §30; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 31 | External-effect safety | guarded publication / external-effect owner | R7 §31; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 32 | Idempotency when available | guarded publication / external-effect owner | R7 §32; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 33 | No secrets in canonical state | release/delivery/handoff owner | R7 §33; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 34 | Evidence reuse | exact identity, Result/material-input and recovery contracts | R7 §34; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 35 | Git-native atomic publication | guarded publication / external-effect owner | R7 §35; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 36 | No dedicated candidate store | guarded publication / external-effect owner | R7 §36; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 37 | No backward-compatibility contract | native admission/no-legacy boundary | R7 §37; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 38 | No in-product legacy migration | native admission/no-legacy boundary | R7 §38; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 39 | Legacy project adoption outside semantics | native admission/no-legacy boundary | R7 §39; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 40 | Native semantic evolution | Recovery/evolution/Close owner | R7 §40; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 41 | Release identity | release/delivery/handoff owner | R7 §41; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 42 | Required-host acceptance | qualification/evidence owner | R7 §42; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 43 | Release blockers | qualification/evidence owner | R7 §43; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 44 | Recovery | Recovery/evolution/Close owner | R7 §44; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 45 | Close | Recovery/evolution/Close owner | R7 §45; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 46 | Deferred capabilities remain visible | release/delivery/handoff owner | R7 §46; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 47 | Direct-pivot anti-loss reconciliation | semantic specification / bounded owners | R7 §47; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 48 | Eager stable-Card classification/materialization | routing / Planning / Execution Prep gate owner | R7 §48; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 49 | Initial Execution Prep quality recommendation | routing / Planning / Execution Prep gate owner | R7 §49; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 50 | Premium D hand-back before Execution | routing / Planning / Execution Prep gate owner | R7 §50; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 51 | Routine JIT lightweight by default | routing / Planning / Execution Prep gate owner | R7 §51; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 52 | Subject/acceptance-driven Review topology | Review/finding/final-acceptance owner | R7 §52; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 53 | Universal Final Qualification defect discovery | qualification/evidence owner | R7 §53; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 54 | Explicit bounded parallel authorization | finite admission / fan-in owner | R7 §54; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 55 | Single native release epoch | native epoch/admission owner | R7 §55; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 56 | Revalidation preserves Result identity | exact identity, Result/material-input and recovery contracts | R7 §56; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 57 | Reviewer persistence boundary | Review/finding/final-acceptance owner | R7 §57; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 58 | Research/Brainstorming host asymmetry | Research/Brainstorming shared semantic owner | R7 §58; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 59 | Native release provenance/admission | exact identity, Result/material-input and recovery contracts | R7 §59; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 60 | Canonical sufficiency/destructive recovery | exact identity, Result/material-input and recovery contracts | R7 §60; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 61 | Activation/forward-repair boundary | Recovery/evolution/Close owner | R7 §61; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 62 | Hard no-legacy negative acceptance | exact identity, Result/material-input and recovery contracts | R7 §62; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 63 | M03-M07 anti-loss disposition authority | semantic specification / bounded owners | R7 §63; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 64 | Binary Review verdicts/orthogonal findings | Review/finding/final-acceptance owner | R7 §64; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 65 | Truthful DONE/safe deferral | Review/finding/final-acceptance owner | R7 §65; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 66 | Dependency-local blocking/repair timing | Review/finding/final-acceptance owner | R7 §66; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 67 | Mandatory Final Qualification Handoff | routing / Planning / Execution Prep gate owner | R7 §67; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 68 | Known Defect Cleanup | routing / Planning / Execution Prep gate owner | R7 §68; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 69 | Targeted Bug Hunt | qualification/evidence owner | R7 §69; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 70 | Global identical-prompt Bug Hunt | qualification/evidence owner | R7 §70; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 71 | Repair swarm/serial integration | finite admission / fan-in owner | R7 §71; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 72 | Material-local post-repair reconciliation | Recovery/evolution/Close owner | R7 §72; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 73 | Fresh final acceptance/release barrier | Review/finding/final-acceptance owner | R7 §73; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 74 | Final-qualification orchestration non-authoritative | runtime boundary; semantics constrain, runtime realizes | R7 §74; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 75 | Git-native canonical backend only | semantic specification / bounded owners | R7 §75; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 76 | Minimal ChatGPT Project bootstrap | release/delivery/handoff owner | R7 §76; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 77 | Pi/Paseo execution ownership window | runtime boundary; semantics constrain, runtime realizes | R7 §77; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 78 | Native Paseo baseline | runtime boundary; semantics constrain, runtime realizes | R7 §78; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 79 | No speculative orchestration layers | runtime boundary; semantics constrain, runtime realizes | R7 §79; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 80 | Evidence-triggered thin adapter | runtime boundary; semantics constrain, runtime realizes | R7 §80; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 81 | Pi/Paseo qualification before Definition GREEN | semantic specification / bounded owners | R7 §81; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 82 | Peer messaging default | runtime boundary; semantics constrain, runtime realizes | R7 §82; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 83 | Review enforcement baseline | Review/finding/final-acceptance owner | R7 §83; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 84 | Single integration mutation owner | finite admission / fan-in owner | R7 §84; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 85 | Prior orchestration-runtime disposition | semantic specification / bounded owners | R7 §85; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 86 | Qualified Pi/Paseo realization | runtime boundary; semantics constrain, runtime realizes | R7 §86; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 87 | Thin-helper bounded responsibilities | runtime boundary; semantics constrain, runtime realizes | R7 §87; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 88 | Pi/Paseo runtime configuration acceptance | runtime boundary; semantics constrain, runtime realizes | R7 §88; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 89 | Busy messaging/lifecycle safety | runtime boundary; semantics constrain, runtime realizes | R7 §89; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 90 | Official Project Workflow for Pi package | release/delivery/handoff owner | R7 §90; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 91 | Package-first Pi runtime with Git fallback | release/delivery/handoff owner | R7 §91; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 92 | Universal self-bootstrapping handoff | release/delivery/handoff owner | R7 §92; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 93 | Exact handoff commit fence | release/delivery/handoff owner | R7 §93; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 94 | Remote-published Git state is continuation truth | exact identity, Result/material-input and recovery contracts | R7 §94; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 95 | Superseded local worktree disposal | runtime boundary; semantics constrain, runtime realizes | R7 §95; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 96 | One active worktree slot per branch | runtime boundary; semantics constrain, runtime realizes | R7 §96; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |
| 97 | Pi package update ownership belongs to pi-unraid | release/delivery/handoff owner | R7 §97; P2 §7 | Accounted; downstream implementation/acceptance remains with named seam |

## Anti-loss families
| Donor family | Disposition | Native owner / retained property | Explicitly not carried forward |
|---|---|---|---|
| M03 portability/helper-less recovery/parity | RETAIN + SUPERSEDE | canonical sufficiency, fresh-context/destructive recovery, independent spec-derived oracle, normalized required-host semantics | successful legacy migration/continuation fixtures |
| M04 parallel Cards/execution ownership | RETAIN + SUPERSEDE | explicit finite admission, conservative conflicts, one mutation domain/Card, exact Results, local invalidation, fan-in compatibility | canonical Worker IDs, scheduler/queue/worktree topology, mandatory named parallel-set |
| M05 independent Review lifecycle | RETAIN + SUPERSEDE | exact-subject independent binary Review, append-only attempts, findings, 5/4/3 ceilings, fresh final closure | blanket Card/Milestone review; runtime-identity eligibility |
| M06 runtime behavior/handoff | RETAIN + SUPERSEDE | deterministic continuation, durable-state precedence, exact gates, A/B/C/D, eager Prep, runtime-neutral handoff | provider/model/session policy, worker choreography, retry/UI telemetry as law |
| M07 Recovery/migration/continuity/Close | RETAIN + SUPERSEDE + REJECT legacy | native Recovery, exact reuse, effect intent/attempt/readback/UNKNOWN, local evolution, semantic Close | legacy readers/migration/normalization/DONE inheritance/mixed versions/downgrade |

No disposition is inferred from research prose. Deferred items remain visible and cannot excuse a current-release MUST failure.
