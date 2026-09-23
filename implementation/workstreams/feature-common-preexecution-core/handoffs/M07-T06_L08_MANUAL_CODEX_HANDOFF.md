# M07-T06 — manual Codex handoff for L08 N-CAPABLE

Status: SUPERSEDED — L08 accepted GREEN from completed user-mediated run  
Owning Card: `M07-T06`  
Qualification: `L08 — N-CAPABLE live topology`

## Exact workflow candidate

- repository: `elmakus/project_workflow_v2`
- commit: `15978113e46abc8498ceaef594461c8613fcadb8`

## Durable consumer fixture

- repository: `elmakus/test-pwv2`
- branch: `feat/m07-l08-topology-n`
- required entry HEAD: `7a2cf09bf505ba62e0ecfc32385429b9fe77e7d8`
- prepared fresh local checkout: `/home/codex/Documents/ChatGPT/test-pwv2-l08-rerun`

The repository state is the test input. Do not duplicate task semantics, expected routing, expected verdicts, or acceptance progression in the user prompt.

## Runtime constraint

Use only:
- provider: `codex-lb-clean`
- model: `gpt-6-sol`
- reasoning effort: `low`

This is an external runtime constraint, not Project Workflow policy. For this qualification run, do not use the Muse/codex_workflow worker harness because its active profile does not satisfy the required model/effort constraint. Any delegated model context must be an internal Codex context using the same provider/model/effort; if that is unavailable, stop with a capability blocker.

## Ready-to-copy prompt

Use Project Workflow V2 from `elmakus/project_workflow_v2` at exact commit `15978113e46abc8498ceaef594461c8613fcadb8`.

Repo projektu:
`elmakus/test-pwv2`

Prepared local checkout:
`/home/codex/Documents/ChatGPT/test-pwv2-l08-rerun`

Branch:
`feat/m07-l08-topology-n`

Expected entry HEAD:
`7a2cf09bf505ba62e0ecfc32385429b9fe77e7d8`

Start from `PROJECT.md`, reconstruct the current workstream from repository state, and continue according to the Project Workflow until the next real workflow stop.

Treat the repository and exact Project Workflow candidate as authority. Do not treat this prompt as task or workflow authority.

For this run use only `codex-lb-clean`, model `gpt-6-sol`, reasoning effort `low` for the top-level session and every delegated model context. Do not use Muse or the codex_workflow worker harness for delegated contexts in this run. Do not fall back to another model/provider. If an internal delegated context cannot satisfy the same provider/model/effort, stop and report a capability blocker.
