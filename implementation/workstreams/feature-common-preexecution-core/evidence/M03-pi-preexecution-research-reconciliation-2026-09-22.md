# M03 pre-execution Pi Research reconciliation — 2026-09-22

Research: `research/PWV2_PI_RUNTIME_COMPATIBILITY_R1.md`
Return owner: Strategic Planning
Plan revision: `PWV2-P1`
Result: **applied / no plan revision required**

## Planning classification

Current Pi evidence does not contradict accepted Project Definition, ADR-PWV2-001..006, or the approved PWV2-P1 M03 strategy.

The evidence instead validates the existing abstraction boundary:
- Project Workflow owns semantic obligations, durable state, exact-subject review/recovery and integration;
- the runtime owns concrete model/provider/session/worker topology and orchestration;
- one Project Workflow Card remains active while runtime-internal workers may be zero/one/many;
- Main remains the sole semantic state reconciler/writer;
- M03 deliberately does not define a runtime role catalog, model preference, worker-adapter API or persisted invocation schema.

Therefore no requirement, ADR, Master Plan milestone, requirement coverage, gate or milestone ordering changes.

## Runtime qualification status

- Codex remains the currently accepted/qualified V2 plugin/delivery runtime under ADR-PWV2-002 and PWV2-REQ-008..012.
- Pi remains a compatibility/runtime candidate only.
- This reconciliation does not authorize replacing Codex, removing Codex acceptance, or promoting Pi into official Definition authority.
- A future explicit user decision is required before Pi becomes a supported/required production runtime or current ChatGPT/Codex continuity acceptance is expanded to include Pi.

## M03 implication

Proceed with M03 common implementation exactly as approved and keep it runtime-neutral.

Pi-specific implementation is deferred to a later bounded compatibility/qualification slice after a real Pi installation is available. Current Research recommends a minimal `pw for Pi` Pi Package at that later boundary: thin Skill/bootstrap + direct canonical `workflow/` payload + only a small audited runtime extension if delegation/reviewer realization needs it. Large third-party orchestration frameworks, mandatory MCP, web UI and external RPC service are not M03 common-semantic dependencies.

## Evidence preserved

The Research record contains:
- current Pi v0.87.0 upstream harness/extension/package/session/security facts;
- capability classification for PWV2;
- subagent alternative comparison;
- security limits and third-party package risk;
- candidate future Pi live-acceptance tests.

No Pi live acceptance is claimed because Pi was not installed/exercised in this workstream during Research.
