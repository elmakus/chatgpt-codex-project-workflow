# M04-T04 — Trigger-only fork lineage and end-of-scope evidence

Date: 2026-09-22
Card: `M04-T04`
Target: `elmakus/project_workflow_v2@feat/pwv2-m04-integration-close`
Accepted implementation subject: `f40250fa2fe88477df3f03c26adfeb2d8024581b`
PR: `elmakus/project_workflow_v2#4`
Predecessor: `cc54b6d590474ebe32c4ade2b2879897f58c99b0`

## Implemented contract

- Added `workflow/FORK_RELEASE_VERSIONING.md` as a trigger-only optional module.
- Added deterministic lineage helper `tools/fork_release_contract.py`.
- Canonical fork releases use accepted upstream repo/tag/SHA plus baseline-local numeric `vX.Y.Z-private.N`.
- Canonical comparison uses numeric `(X,Y,Z,N)`; legacy/upstream-looking and malformed tags do not enter a private lane.
- Historical published tags are immutable.
- Optional native latest alias must identify the exact accepted canonical artifact; synthetic `vlatest` is rejected.
- Fork lineage does not authorize sync/tag/release/deploy and release quality remains separate from lineage.
- Router now sends all-terminal Card state to common Close rather than treating role/milestone completion as a stop.
- Close only returns end-of-approved-scope after durable completion with no already-authorized obligation; live-write/deployment status alone creates no gate, while an explicit accepted authorization boundary still does.

## Deterministic verification

Final target `f40250fa2fe88477df3f03c26adfeb2d8024581b`:

- GitHub Actions push run `35768949267`: PASS.
- GitHub Actions PR run `35768955381`: PASS.
- State suite: 28/28 PASS.
- Router suite: 39/39 PASS, including all-terminal -> Close and negative ordinary-Close read-set assertion excluding `workflow/FORK_RELEASE_VERSIONING.md`.
- Execution suite: 4/4 PASS.
- Review suite: 1/1 PASS.
- Recovery suite: 2/2 PASS.
- Close + fork-lineage suite: 28/28 PASS, including A16 lane/tuple/history/latest-alias fixtures and end-of-scope/live-write authorization cases.

An earlier implementation run `35768681967` on `480f9e1de7bc0105f38d3bbe1789f1e66134a76a` failed because generated regex literals contained doubled escaping. The failure was not accepted as evidence; it was corrected by `5b437da9df75e6389eda0ea83da6549785ff99a4`, then the ordinary-Close negative read-set assertion was added in final `f40250fa2fe88477df3f03c26adfeb2d8024581b`.

## Readback

- Target branch HEAD read back as final accepted implementation subject.
- PR #4 points at the same head for final M04-T04 verification.
- Both push and pull-request workflows are GREEN on that head.
- No actual tag, release, deployment, upstream sync or other publication side effect was performed.

## Acceptance disposition

M04-T04: GREEN / DONE.

Policy reroute after reconciliation: M04-T05 cumulative M04 acceptance and immutable review freeze.
