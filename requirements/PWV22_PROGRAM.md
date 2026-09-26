# PWv2.2 Program Requirements — Definition R1

Status: ACTIVE Definition authority
Source Brainstorming subject: `pwv22-program@19`

## Completion blocker

Definition may proceed before terminal PWv2.1 exists, but it MUST NOT become GREEN and MUST NOT freeze predecessor-dependent representation or implementation choices until the exact terminal accepted PWv2.1 predecessor has been rebound and revalidated.

## Product requirements

1. **Semantic contract first.** Project Workflow defines semantic obligations, authority, invariants, evidence, acceptance, legal transitions, recovery and owner boundaries. Runtime-specific orchestration mechanics remain outside canonical PW unless a mechanism is required to preserve a semantic invariant deterministically and portably.
2. **Host neutrality.** PWv2.2 is host-neutral. ChatGPT and Pi/Paseo are required release hosts for PWv2.2.0. Codex is non-blocking unless explicitly restored as a required host.
3. **No runtime identity as authority.** Model, provider, worker, session and runtime identity MUST NOT determine workflow legality, freshness, routing, review eligibility or acceptance.
4. **Portable execution contract.** Execution Obligation / Execution Result remain typed and transport-neutral, with JSON as the standard portable interchange serialization. Runtime-internal representation may differ.
5. **Exact Result identity.** Consumed Results bind exact repository + commit + path + blob identity.
6. **Exact dependency binding.** A downstream dependency means consumption of an exact accepted predecessor Result, not merely predecessor DONE.
7. **Material-local freshness.** Freshness derives only from exact authority, Results and other material inputs that determined the obligation. Unrelated changes MUST NOT stale unaffected work.
8. **Guarded canonical mutation.** Canonical transitions use expected-old/CAS-style protection plus target-side readback. Concurrent change causes refetch/re-evaluation, not blind overwrite.
9. **Small semantic owners.** Canonical state remains split among bounded semantic owners; do not introduce one universal STATE file/event ledger.
10. **Task Board scope.** Task Board owns current execution/Card state only after implementation state exists and does not absorb Brainstorming, Definition or Planning authority.
11. **Immutable Result history.** Re-execution/repair creates a new Result; prior Results remain immutable history.
12. **Append-only Review history.** Review attempts remain append-only and exact-subject-bound. Finalization is deterministic and non-semantic.
13. **Review independence.** A context/agent that materially authored or repaired the exact subject cannot issue its independent verdict. Model identity is irrelevant to independence.
14. **Premium stops.** Premium A/B/C remain real user-facing stops. Model quality recommendations are advisory; Premium B MUST preserve semantic independence and exact-subject review.
15. **Bounded parallelism anti-regression.** PWv2.2.0 MUST preserve at least accepted PWv2.1 bounded parallel-safe Card semantics. Overlapping mutating write scopes serialize; no override exists.
16. **One mutating ownership domain per Card.** Runtime helpers may exist, but competing independent mutating owners for one Card are forbidden. Independent mutation belongs in separate Cards.
17. **Integrated compatibility.** Downstream consumption of multiple sibling Results requires the accepted integrated compatibility obligation; it does not replace individual Card review.
18. **No self-authorized scope growth.** A worker/subagent may report follow-on work but cannot self-authorize new Cards, siblings, successors, JIT obligations, product scope or authority.
19. **Worker lifecycle expectation.** Runtime workers/subagents that no longer serve an active Card/attempt/role are released/closed automatically. Capacity management, shutdown mechanics and session topology are runtime concerns.
20. **Automatic continuation.** If exactly one legal next obligation exists and no owner, Premium or human-input stop is due, the host SHOULD continue automatically rather than asking redundant permission.
21. **Bounded repair.** RED repair may proceed automatically inside already accepted scope/strategy. New scope/strategy/authority routes back to its proper owner.
22. **Fresh final closure after material repair.** The original reviewer may verify known findings when eligible, but final full-scope closure after material repair requires a fresh independent reviewer.
23. **Review convergence ceilings.** Preserve accepted PWv2.1 discovery/repair ceilings and root-cause/convergence routing. Reaching a ceiling MUST change workflow mode; RED is never accepted merely because a limit was reached.
24. **Falsification-first discipline.** When an accepted Card outcome can meaningfully be expressed as a failing automated/observable check, implementation SHOULD demonstrate failure first and then make the minimum change needed for GREEN. This is guidance, not a legality requirement.
25. **Planning-owned Simplification Review.** Every material Planning cycle receives a mandatory pre-freeze Simplification Review. Material findings require explicit owner accept/reject before freeze.
26. **Simplification boundaries.** Simplification does not rewrite active/completed work. Mid-execution simplification affects only unstarted scope and routes through existing authority owners.
27. **Human-interaction-last.** Planning should defer human-attended work as late as dependencies safely allow and batch compatible attended actions, without collapsing distinct risks/authorities into one mega-Card.
28. **Disposable projections.** Context Compiler, trace index, shadow DAG/frontier, caches and similar projections are optional and non-authoritative. Deleting them MUST NOT change legal workflow behavior.
29. **Derived readiness.** Persist only minimal direct dependency/Result facts needed for canonical legality. READY/frontier/reachability are derived, not competing mutable truth.
30. **JIT materialization.** Do not create speculative placeholder Cards when their stable contract depends on predecessor evidence. Keep a bounded trigger and materialize once knowable.
31. **External-effect safety.** Real external mutations follow intent -> attempt -> readback -> known result. Uncertainty becomes UNKNOWN. Blind retry is forbidden.
32. **Idempotency when available.** External mutation SHOULD use stable request/idempotency identifiers where supported.
33. **No secrets in canonical state.** Credentials, tokens, OTPs and similar secrets never become canonical PW state. Persist only non-secret recovery/readback identifiers.
34. **Evidence reuse.** Reuse is property-, authority- and environment-scoped and fails closed. If proving reuse is harder or less reliable than rerunning a cheap deterministic test, rerun the test.
35. **Git-native atomic publication.** Multi-file canonical transitions may be assembled off-canonical and validated, then published via one guarded Git-native ref/commit transition plus readback.
36. **No dedicated candidate store.** A non-Git candidate backend/store is rejected. Git-native isolation may be used when required.
37. **Migration.** PWv2.1 -> PWv2.2 uses compatible reading where needed, one atomic canonical writer cutover, exact rehearsal, publication/readback and no dual canonical writers.
38. **Backward compatibility direction.** PWv2.2 reads/recovers supported PWv2.1 durable state. Reverse compatibility is not required.
39. **Active legacy migration.** After PWv2.2.0, an active PWv2.1 workstream migrates before its next canonical mutation; new workstreams start natively in PWv2.2.
40. **Semantic evolution.** A workflow update affecting existing durable meaning MUST classify affected state as preserve / revalidate / stale / Recovery.
41. **Release identity.** Every official PWv2.2 release has an exact Git commit/tag identity covering policy package, acceptance tests and migration tooling.
42. **Required-host acceptance.** Semantic releases run shared behavioral fixtures on ChatGPT and Pi/Paseo; host-specific tests exist only where host realization materially differs.
43. **Release blockers.** MUST-semantic, migration/recovery and required-host acceptance failures block release. Dispositioned noncritical UX/diagnostic defects may be deferred.
44. **Recovery.** Recovery reconstructs facts and legal continuation from durable state, automates deterministic mechanical repair where safe, and asks the owner only when a genuine owner choice remains.
45. **Close.** Managed change completes only after accepted implementation, integration, target-side readback and durable confirmation. Purely mechanical Close may proceed automatically when no real user boundary remains.
46. **Deferred capabilities remain visible.** Deferred PWv2.2.x obligations remain durable until implemented or explicitly rejected.
47. **Final predecessor rebind.** Before Definition GREEN, rebind this authority to the exact terminal accepted PWv2.1 predecessor and reopen only requirements/decisions materially affected by that predecessor.
