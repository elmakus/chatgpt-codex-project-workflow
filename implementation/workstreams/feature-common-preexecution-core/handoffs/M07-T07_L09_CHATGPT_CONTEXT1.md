# M07-T07 — ChatGPT context 1 handoff

Status: READY FOR USER-MEDIATED CHATGPT CONTEXT 1
Owning Card: `M07-T07`
Qualification: `L09 — N-CHATGPT`

## Exact workflow candidate
- repository: `elmakus/project_workflow_v2`
- commit: `15978113e46abc8498ceaef594461c8613fcadb8`

## Durable consumer fixture
- repository: `elmakus/test-pwv2`
- branch: `feat/m07-l09-topology-n-chatgpt`
- required entry HEAD: `0709b4cea544e945fad0b058293de7a9b1d0941a`

The repository state is the test input. The user prompt must remain locator-only and must not describe expected review verdicts, correction steps, context-stop behavior, or finalization behavior.

## Ready-to-copy prompt for fresh ChatGPT context 1

Use Project Workflow V2 from `elmakus/project_workflow_v2` at exact commit `15978113e46abc8498ceaef594461c8613fcadb8`.

Repo projektu:
`elmakus/test-pwv2`

Branch:
`feat/m07-l09-topology-n-chatgpt`

Start from `PROJECT.md`, reconstruct the current workstream from repository state, and continue according to Project Workflow until the next real workflow stop.

Treat the repository and exact Project Workflow candidate as authority. Do not treat this prompt or any previous chat as task or workflow authority.
