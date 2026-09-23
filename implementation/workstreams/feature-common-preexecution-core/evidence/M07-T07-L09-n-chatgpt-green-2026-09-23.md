# M07-T07 — L09 N-CHATGPT live qualification

Date: 2026-09-23
Status: GREEN
Candidate: `elmakus/project_workflow_v2@15978113e46abc8498ceaef594461c8613fcadb8`

## Fixture entry

Consumer repository: `elmakus/test-pwv2`
Branch: `feat/m07-l09-topology-n-chatgpt`
Initial L09 entry HEAD: `0709b4cea544e945fad0b058293de7a9b1d0941a`

Both user-started ChatGPT sessions received locator-only prompts. The expected RED/correction/fresh-review/GREEN/finalization sequence was not prescribed in those prompts.

## Fresh ChatGPT context 1

Context 1 reconstructed the workstream from repository state and independently reviewed frozen S1.

Durable sequence:
- R01 verdict: RED;
- R01 preserved append-only against exact S1;
- same ChatGPT context performed the bounded correction;
- S2 implementation commit: `d9a99ec3d835234bfe4baa10974386bbc0ff50ab`;
- S2 product blob: `3a446f6d934b2e63c0466e9f7b2bb596fa416268`;
- exact S2 bytes: `topology-n: GOOD\n`;
- S2 result commit: `124a2945dcc7e28e3f7de64f53b48a9d0e41a6d1`;
- S2 result blob: `482bfb90e65bd5d9735ae09cb2e59999e11004b4`;
- a later R02 attempt was frozen pending;
- Task Board revision 2 kept M01-T01 `in_progress`;
- branch HEAD after context 1: `e97579441d6e7f0e7fdc646d54b826d686836f2d`.

The first context then stopped for a real independence boundary because it had materially repaired S2 and could not independently review that exact subject.

## Fresh ChatGPT context 2

A genuinely fresh top-level ChatGPT context reconstructed the same durable workstream from repository state.

GitHub target-side readback confirms:
- R02 verdict: GREEN;
- R02 exact subject: result commit `124a2945dcc7e28e3f7de64f53b48a9d0e41a6d1`, blob `482bfb90e65bd5d9735ae09cb2e59999e11004b4`;
- R02 independence basis records that the fresh reviewer did not materially produce or repair S2;
- Task Board revision 3 marks M01-T01 `done`;
- final product remains exactly `topology-n: GOOD\n`.

GREEN was not treated as a verdict-only stop. The same second ChatGPT context continued into Close.

## Close and target-side recovery

PR #4 (`Qualify topology-n ChatGPT workflow path`) was created and merged.

Final target:
- `main` merge commit: `145aa5b81f2c222844e20dc14fc90784fc0585ac`;
- merged PR head: `306760fb2011c999ad91af41597ef60ca0120b11`;
- PR #4 state: merged/closed;
- final main contains Task Board revision 3, R01 RED, R02 GREEN and the exact accepted product bytes;
- source branch `feat/m07-l09-topology-n-chatgpt` is absent after automatic cleanup.

The second ChatGPT context reported exact `close_contract.py` progression:
`source_ref_independent_recovery -> automatic_cleanup_complete -> end_of_scope_stop`.

GitHub readback independently confirms the final target merge, canonical state and source-branch absence.

## Verdict

L09 N-CHATGPT: GREEN.

The live run demonstrates the required two-fresh-context topology:
- fresh context 1: independent S1 RED -> same-chat correction -> freeze S2 -> real stop for new independence;
- fresh context 2: independent S2 GREEN -> same-chat deterministic finalization -> Close -> end-of-scope stop.
