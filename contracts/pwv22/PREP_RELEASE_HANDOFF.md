# PWv2.2 preparation contract — release provenance and universal handoff

Status: bounded P2 Execution Prep contract; not package implementation, release admission or deployment authorization.
Authority: R7 requirements 27, 31–43, 55, 59, 61, 75–97; P2 §§2,5,6,8; accepted `decisions/PWV22_PI_PACKAGE_HANDOFF_R7.md`. Exact authority tuples live in each consuming Card.

## Release/package provenance interface

The supported delivery must resolve, without relying on a friendly name or latest version:

- official workflow repository, immutable semantic-release commit and official tag mapping;
- policy, validators/router, required tests/tooling and host bootstrap inventory covered by that identity;
- package artifact identity/content digest and reproducible mapping to the covered source inventory;
- consumer's applicable native release/epoch and supported compatibility relation;
- whether identity is an isolated candidate-fixture identity or a genuinely published/read-back official identity.

These are required semantic facts, not a prescribed manifest serialization or package name. S04 specifies the concrete contract; S14 chooses/builds inventory against accepted core/helper interfaces; S18 freezes contents; S24/R10 accepts the exact final subject; S25 publishes and reads back official identity. Do not embed a commit's own hash in content that determines that commit. Bind tests/Reviews externally to frozen content, then map official tag/artifact to it. Content change requires refreeze and affected acceptance, not retagging old evidence.

Installed package is preferred only if official provenance and exact applicable-release compatibility are proved. Missing, incompatible, wrong or tampered package falls back to canonical Git at the required supported release. If neither source is verifiable, fail closed. Offline cached bytes are not trusted merely because present. Package/fallback must produce the same normalized semantic obligations from the same authority/input subject.

The package bundles Pi bootstrap/skill/instructions plus the qualified helper, not a scheduler, journal, queue, Board, updater or authoritative cache. `pi-unraid` owns install, pin, update, rollback and readback. Delivery rollback must not downgrade an activated semantic lineage; incompatibility returns Recovery. Production target/effect authority remains separately required.

## Universal handoff: minimum semantic fields

Every direction (ChatGPT to Pi, Pi to ChatGPT, Pi to Pi, ChatGPT to ChatGPT) carries:

1. bootstrap instruction: compatible installed official Project Workflow package first, otherwise `elmakus/project_workflow_v2`;
2. consumer repository;
3. exact branch;
4. immutable handoff commit;
5. exact entry obligation;
6. durable start pointer.

Do not add narrative as authority, a second receipt ledger, runtime identity as eligibility or hidden receiver-specific setup. Persistent ChatGPT Project Instructions hold only stable workflow/router, consumer and non-authoritative Coordinator Protocol locators; branch/Card/attempt/model/research-run state stays in the handoff/durable owner records.

## Receiver algorithm and safety checks

- Fetch/read back the exact remote repository and branch before reading local continuation as authority.
- Equal head: reuse the existing ordinary branch slot from that exact remote commit. Clean worktree at that commit needs no destructive reset. Do not create another same-branch slot just to avoid residue.
- Moved head: the handoff is stale. Reconstruct current canonical route; do not force the remote back or silently continue old authority.
- Dirty/local-only state is not an accepted Result. Before disposing it, rule out current canonical obligations bound to it and unresolved external effects. If uncertain, preserve it as non-authoritative evidence and reconcile effects first. No default stash/merge resurrection.
- Missing branch/commit/pointer, wrong repository, unsupported release, ambiguous scope or effect uncertainty fails closed to its owner. Do not invent the missing state.
- Recheck expected remote head at publication. A later race is rejection/reconstruction, never force-overwrite. Verify Result artifact reachability and target blob readback after publication.

## Required matrix

For all four directions, exercise equal head, moved head, missing branch/pointer, dirty older worktree, local-only commit, one existing slot, remote move after initial fetch and unresolved external-effect residue. For installed Pi also cover absent/incompatible/tampered package, canonical fallback parity and unavailable both sources. Each negative case asserts zero unauthorized canonical mutation and no duplicate branch worktree. Environment-dependent behavior requires actual readback; a simulated tool response cannot prove injection or lifecycle.

## Late attended actions / owner-separated effects

Prepare non-secret access/target prerequisites early; execute attended mutations only as late as dependencies safely allow. Keep these separately identified even if a user can attend once:

- product versioned ref/tag/artifact publication (do not replace the governing default channel);
- pi-unraid installation/configuration/update/rollback and target readback;
- consumer integration and any consequential historical auto-tag workflow;
- any explicit owner authorization/adoption decision.

Record operation/readback IDs, not credentials. An unavailable host blocks the affected acceptance; it does not justify a package-local updater or false host proof. R6's observed MCP/relay drift is an input to later inspection, not a claim about the present live host.

## Final Qualification handoff boundary

S19 must publish/read back the exact candidate/entry pointer and stop before Known Defect Cleanup. Continued authority requires the user's exact handoff satisfaction, not sending a message or creating a fresh Pi agent. Pi/Paseo ordinary coordination ends at this boundary; the receiver must be outside that accepted window. This contract does not initiate the handoff now and does not add a native Premium D field to the current governor.
