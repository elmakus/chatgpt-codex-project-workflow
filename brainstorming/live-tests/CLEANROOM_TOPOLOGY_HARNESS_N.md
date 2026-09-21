# Clean-room orchestration-topology harness — N

Status: experimental Brainstorming support only
Scope: common-preexecution-core@R1
Production authority: none

## Purpose

This harness exists specifically to test orchestration topology without allowing the currently active Project Workflow implementation to teach the tested context how to behave.

The tested context MUST NOT load or consult production Project Workflow routing/policy modules.

## Clean-room boundary

The actual tested context must run in a disposable isolated workspace/repository containing only the exact experiment packet required by the selected N variant:

- this clean-room harness;
- the exact N semantic authority;
- the exact N experiment record;
- the exact result fixture;
- minimal Git metadata needed to make durable local transitions.

The clean-room workspace MUST NOT contain or expose:
- root `CHATGPT.md`;
- root `PROJECT.md`;
- `workflow/chatgpt_only/*`;
- `workflow/codex_only/*`;
- `workflow/common/*` other than this copied experimental harness;
- production router/recovery/review/execution modules;
- prior chat handoffs or production Task Boards.

The tested context must derive legal behavior only from the clean-room packet.

## Outer setup versus tested context

An outer setup context may use the real repository only to:

1. refresh the authoritative experiment branch;
2. read the exact N experiment record and immutable refs;
3. materialize a disposable clean-room workspace containing only the allowed packet;
4. initialize minimal Git state for that workspace;
5. start the fresh tested context inside the clean room;
6. collect the tested context's durable clean-room result/transcript;
7. validate it against the experiment contract;
8. persist only the normalized experiment outcome back to the authoritative N record;
9. clean up the disposable workspace.

The outer setup context MUST NOT itself perform the semantic review/correction/re-review/finalization chain being tested.

Any behavior selected by the outer production Project Workflow is therefore setup behavior only and cannot count as evidence for N.

## Prompt contamination rule

The fresh tested context receives only a locator/instruction for the clean-room packet.

Its prompt MUST NOT:
- say what verdict R01 or R02 is expected to produce;
- describe the intended continuation chain beyond telling it to recover and follow the exact clean-room experiment record;
- mention existing Project Workflow policy names;
- mention Tester/Executor/ChatGPT-only/Codex-only semantics;
- tell it that RED or GREEN should continue or stop;
- supply production-workflow guidance.

Those semantics must be discovered from the clean-room N record itself.

## Runtime capability

The clean-room tested context may use capabilities natively available to its runtime, including creation of qualifying independent contexts.

Availability or absence of such capability is discovered at runtime.

A failed invocation is a runtime failure; it is not evidence that the capability is absent.

## Evidence boundary

Canonical N evidence persisted back to the authoritative branch may contain only semantic facts required by the N record.

Concrete runtime/product/model/worker/session/invocation/workspace/worktree identity remains diagnostic-only and MUST NOT become canonical Project Workflow evidence.

## Success meaning

A PASS demonstrates behavior derived from the experimental common contract plus native runtime capability, not behavior copied from current production Project Workflow policy text.
