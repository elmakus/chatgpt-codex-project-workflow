# M07 L08 correction blocker handoff

Status: USER ACTION REQUIRED
Workstream: `feature-common-preexecution-core`
Blocked Card: `M07-T06`
Durable start pointer: `implementation/workstreams/feature-common-preexecution-core/TASK_BOARD.yaml`
Blocker evidence: `implementation/workstreams/feature-common-preexecution-core/evidence/M07-T06-L08-durable-evidence-blocker-2026-09-23.md`

The current ChatGPT runtime cannot start the nested capable Codex/multi-agent live run required by M07-T06. No other product/strategy decision is open.

## Ready-to-copy capable Codex task

Use Project Workflow V2 from `elmakus/project_workflow_v2` at exact commit `15978113e46abc8498ceaef594461c8613fcadb8`.

Consumer repository:
`elmakus/test-pwv2`

Branch:
`feat/m07-l08-topology-n`

Entry obligation:
recover the current `topology-n` workstream from repository state and continue according to Project Workflow V2 until the next real workflow stop.

Durable start pointer:
`implementation/workstreams/topology-n/TASK_BOARD.toml`

This is the M07-T06 L08 durability correction. Use a genuinely capable top-level runtime with delegated model contexts; do not replace it with direct/self-simulated execution. Preserve the completed exact Git state on a durable repository ref before reporting success so the controlling workstream can independently read it back. Treat the consumer repository and exact PWv2 candidate as authority; this prompt is only the correction locator.
