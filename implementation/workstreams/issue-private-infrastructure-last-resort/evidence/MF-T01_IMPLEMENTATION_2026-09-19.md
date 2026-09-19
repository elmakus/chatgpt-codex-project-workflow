# MF-T01 implementation evidence — private infrastructure last-resort rule

## Exact implementation subject

- Implementation commit: `184cdee6171eaf6453484816965a8017841f7a3b`
- Reviewed behavioral file: `CHATGPT.md`
- Exact `CHATGPT.md` blob: `72fc6277f0cfef3a1f1f99c74b3beaf7a37b3557`
- Base: `d64d8c1d7f05ce2a2584ffcb3ade4634263bbc95`

The exact review subject is the behavioral `CHATGPT.md` blob above together with the MF-T01 acceptance surface. Later durable-state commits do not change that subject.

## Verification

### Acceptance 1 — global normal-ChatGPT bootstrap coverage

GREEN. Root `CHATGPT.md` now contains `## Execution-surface selection`. Root `CHATGPT.md` is the mandatory normal-ChatGPT entrypoint before policy routing.

### Acceptance 2 — native/purpose-built path before private infrastructure

GREEN. The section requires a permitted native ChatGPT runtime/tool or appropriate purpose-built connector/plugin when materially equivalent, and explicitly forbids choosing user-owned/private remote infrastructure merely for convenient shell access, compute, temporary storage or another shortcut.

### Acceptance 3 — narrow private-infrastructure escape hatch

GREEN. Private remote infrastructure is permitted only when the task intrinsically depends on that specific host/state/devices/services/environment or no materially equivalent permitted native/purpose-built path can perform the required operation and verification.

### Acceptance 4 — no capability-inventory regression

GREEN. The new text explicitly says this is an execution-surface selection rule, not a capability inventory, and forbids probing private infrastructure merely to discover whether it could be useful.

Branch readback of `workflow/chatgpt/CAPABILITY_GATE.md` is unchanged from base at blob `4b2ac2b782d6fd750451102c7789bacc890b2743`.

### Acceptance 5 — bootstrap remains single source

GREEN. `prompts/CHATGPT_PROJECT_INSTRUCTIONS.md` remains unchanged at blob `5764a4e87cb2c5cc6562b472a2f2d37c59cff545`; the policy was not duplicated there.

## Diff-scope check

Base → implementation commit comparison is 9 commits ahead, 0 behind. Changed files are only:
- `CHATGPT.md` — behavioral workflow change;
- this workstream's `INTAKE.md`, `WORKSTREAM.yaml`, `TASK_BOARD.yaml`, and `cards/MF-T01.md` — durable workflow state/contracts.

No unrelated workflow behavior file changed.

## Result

Implementation verification: GREEN.

Independent review is still required by the Card as `RECOMMENDED`; this evidence is implementation-owned and is not an independent verdict.
