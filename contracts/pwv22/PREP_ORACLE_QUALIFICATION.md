# PWv2.2 preparation contract — independent oracle and qualification evidence

Status: bounded acceptance/test contract for the Cards that name it. Not executable native workflow policy.
Authority: R7 requirements 2–8, 13–17, 22–24, 34, 42–44, 52–74, 81–97; P2 §§3–7. Exact source tuples are in the consuming Cards.

## Non-circular oracle boundary

Expected legal outcomes derive from numbered R7 requirements and accepted decisions, not the production/donor router or observed host output. Donor tests may suggest adversarial inputs after expected outcomes have been specified. If a production implementation disagrees with the expectation, investigate authority; never regenerate expected answers from that implementation to make tests pass.

Each corpus case needs: stable case ID; exact authority requirement/decision; input facts; property under test; expected semantic owner/obligation or fail-closed disposition; expected mutation/no-mutation; permitted material-input changes; observable evidence/readback; interruption point if applicable. These are test-record content requirements, not native Obligation JSON fields. Avoid asserting exact prose or provider IDs. A local case format/normalizer may be chosen during S02 without forcing S05's public API.

Separate the **core semantic corpus** (S02-T01) from **delivery/destructive-recovery scenarios** (S02-T02). They use disjoint case-ID namespaces and the semantic observation facts specified above, not two competing expected-answer authorities. Concrete test-only encodings may be authored independently from those facts; S16 must reconcile their accepted union/adapter mapping before consumption. S02-T02 does not require a future S02-T01 API or Result to define its cases and may bind actual host adapters/deletion surfaces later; it must not copy production expectations. Their union must cover 1–97 and all anti-loss families. Later acceptance adds actual observation bindings, not new oracle answers by imitation.

Falsify the oracle itself: mutate a correct expected/observed outcome into wrong owner, skipped gate, stale Result accepted, unrelated Result wrongly invalidated, silent migration, contaminated Review accepted, fake package provenance, and false no-effect after an uncertain external mutation. Each deliberate mutant must be rejected for the intended reason. A case that only round-trips its own fixture is not sufficient.

## Finding evidence interface

Keep findings separate from binary GREEN/RED verdicts. Every finding disposition records origin evidence/subject, alleged violated property/acceptance, reproduction or falsification, material dependency cone, classification with reason, owning obligation and repair timing. Deduplication preserves every source reference and cannot vote a defect away.

Safe deferral requires positive proof that exact Card acceptance remains true and the permitted intervening work does not consume the defective property. State first affected consumption and latest-safe repair boundary, taking the earlier. Unknown impact fails closed. A defect that falsifies acceptance cannot be converted to an advisory label to retain DONE. Current-release violations cannot cross final acceptance/publication. Out-of-scope findings require explicit owner disposition; they do not vanish.

## Ordered program evidence surfaces

S18 freezes candidate/inventory/findings -> S19 exact handoff satisfaction -> S20 known-finding reconciliation and actual required cleanup/closure -> S21 targeted discovery -> S22 global discovery -> S23 integrated findings, actual bounded repair, serial integration and material-local impact disposition -> S24 fresh final independent acceptance -> S25 publication/readback -> S26 Close.

Reconciliation-only Cards can have stable contracts before the concrete finding set exists: they enumerate/classify the exact future inputs and do not implement an unknown repair. Their accepted Result does not claim cleanup/repair completion. Findings-dependent repair and completion remain JIT. When a set is empty, preserve an explicit exact-subject zero-work result; never invent a defect or repair Card.

## Targeted discovery (S21)

Bind the post-cleanup candidate and accepted risk/coverage model. Cover material Cards, integrations, invariants and negative spaces: identity/CAS/provenance, remote races, gates/JIT, Results/locality, parallel claims/fan-in, findings/deferral, independent Review/finalization/convergence, effects/native evolution/Close, package/distribution, injection/messaging/lifecycle and destructive recovery/no-legacy. Record tests attempted, evidence, limitations and uncovered risk. Scale independent contexts proportionally; no universal count. Candidate code remains read-only to discovery.

## Global discovery (S22)

Freeze the exact same post-cleanup subject (or explicitly refreeze and rerun affected targeted coverage if changed). Freeze one broad prompt by exact content identity and execute a positive owner-selected number of independent isolated runs with identical prompt and subject. Preserve each run's evidence and contamination/limitation checks. Runtime IDs/count selection are not workflow law. No majority, duplicate count or zero-findings claim establishes acceptance.

Suggested prompt content is non-authoritative guidance: independently attempt to falsify every current-release acceptance claim; search ignored negative spaces and cross-component assumptions; require exact paths, subject, reproduction, violated requirement, affected cone and uncertainty for each report; do not modify implementation or infer acceptance from passing existing tests. S22 must freeze actual prompt bytes at execution, not a guessed future hash.

## Post-repair and final closure

One integration mutation owner composes only the admitted exact Result set/order. Actual program mutations stay serial under the current governor; finite parallel repair is tested only in admitted disposable native fixtures. Compute preserve/rerun/revalidate/focused-or-full Review/stale/Recovery per material surface. Unchanged implementation keeps Result identity. Keep constituent Reviews and append failures. Material repair requires fresh eligible full-scope closure; original reviewers may verify known findings while eligible.

Required final evidence: R01–R10 exact acceptance surfaces, both-host semantic observations (installed/fallback where applicable), non-circular oracle validity, destructive recovery/no-legacy checks, complete requirements/deferred register disposition, effects readback and no unresolved current-release/stale/unknown proof. Hunts never replace R10. Native ceilings to implement/test are 5 local, 4 integration, 3 final, plus 3 failed repair-to-closure rounds per defect class; reaching a ceiling changes mode, not verdict. They do not change this consumer governor retroactively.

## Evidence execution safety

Only disposable fixtures may undergo destructive recovery or fault injection. Retain their exact canonical inputs and observation mapping while deleting runtime/chat/helper/projection state. Restore/reconstruct using only canonical native state and published contracts, then compare independently expected continuation. Representative PWv1/v2.0/v2.1 inputs must remain byte-identical on rejection. R6 P0–P6 is architecture evidence, never final package/production acceptance. Any future test that invokes a real LLM must use the environment's approved real-test launcher/profile; lack of that capability blocks the test rather than permitting a different model. Synthetic fixture checks need no inference.
