# M07-T07 — ChatGPT context 2 handoff

Status: READY FOR USER-MEDIATED CHATGPT CONTEXT 2
Owning Card: `M07-T07`
Qualification: `L09 — N-CHATGPT`

## Exact workflow candidate
- repository: `elmakus/project_workflow_v2`
- commit: `15978113e46abc8498ceaef594461c8613fcadb8`

## Durable consumer state after context 1
- repository: `elmakus/test-pwv2`
- branch: `feat/m07-l09-topology-n-chatgpt`
- required entry HEAD: `e97579441d6e7f0e7fdc646d54b826d686836f2d`

Context 1 was independently verified from GitHub readback:
- R01 is terminal RED and remains bound to immutable S1;
- S2 implementation is `d9a99ec3d835234bfe4baa10974386bbc0ff50ab`;
- S2 result is `124a2945dcc7e28e3f7de64f53b48a9d0e41a6d1`;
- exact S2 file blob is `3a446f6d934b2e63c0466e9f7b2bb596fa416268` and bytes are `topology-n: GOOD\n`;
- R02 is pending;
- Task Board revision 2 keeps M01-T01 in_progress.

The user prompt must remain locator-only and must not prescribe the expected verdict, finalization behavior, or downstream route.

## Ready-to-copy prompt for fresh ChatGPT context 2

Use Project Workflow V2 from `elmakus/project_workflow_v2` at exact commit `15978113e46abc8498ceaef594461c8613fcadb8`.

Repo projektu:
`elmakus/test-pwv2`

Branch:
`feat/m07-l09-topology-n-chatgpt`

Start from `PROJECT.md`, reconstruct the current workstream from repository state, and continue according to Project Workflow until the next real workflow stop.

Treat the repository and exact Project Workflow candidate as authority. Do not treat this prompt or any previous chat as task or workflow authority.
