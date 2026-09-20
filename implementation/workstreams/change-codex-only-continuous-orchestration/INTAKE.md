# Intake — Codex-only continuous orchestration

- Workstream ID: `change-codex-only-continuous-orchestration`
- Kind: `change`
- Branch: `work/codex-only-continuous-orchestration`
- Integration target: `main`
- Base: `ce3cf3fc80b923ad26b77d9ac66fb3db5ad31f5f`
- Classification: independent
- Parent workstream: none
- Status: active

## Operator intent

Make `codex_only` operate as a continuous Codex Main orchestration path. Once product/system intent and the project plan are authorized, Main should be able to continue deterministically across milestones (for example M01 through M15), Executor/Tester cycles, bounded repairs, close and next-milestone preparation without returning control to the user merely for context hygiene.

Remove the policy-local Context Health Gate from the normal `codex_only` lifecycle. Context/session reconstruction remains an emergency/runtime recovery concern backed by durable repository state, not a planned project-workflow stop.

## Discovery / diagnosis

Current `main` already establishes the desired orchestration model in several places:

- `workflow/codex/CODEX_ORCHESTRATION.md`: Codex Main owns deterministic continuation across approved milestone boundaries, while `codex_workflow` owns worker/session lifecycle and runtime recovery.
- `workflow/codex_only/REVIEW.md`: independent Tester review returns to Main/router and is not a user stop.
- `workflow/codex_only/CLOSE.md`: after GREEN/finalization, the next approved milestone continues automatically without requiring user “continue”.
- `workflow/codex_only/RECOVERY.md`: durable state is sufficient to reconstruct project continuation.

The inconsistent layer is `workflow/codex_only/ROUTER.md` + `workflow/codex_only/CONTEXT_HEALTH.md`, which still allow coordinator context hygiene to become a normal project-workflow boundary between deterministic obligations.

No matching active workstream, branch or PR was found. The change is independent from current unmerged work.

## Path classification

This is not a micro-fix. It changes accepted lifecycle semantics for `codex_only`, including what may stop a long-running orchestration pass.

Next route: `project_definition`.

Definition must freeze:

- normal `codex_only` continuation does not contain a Context Health/FRESH gate;
- Main continues across all deterministic authorized milestones/reviews/corrections/close transitions;
- formal Tester review does not itself return control to the user;
- session/runtime loss is handled by durable recovery, not by a planned hygiene stop;
- true stops remain unresolved user/product authority, explicit authorization gates, concrete unremediable runtime/input blockers, and end of approved scope;
- the existing Brainstorming → Definition user-promotion gate remains unchanged.

## Scope boundaries

Included:
- `codex_only` router/continuation semantics;
- removal/retirement of active `codex_only` Context Health semantics;
- Codex orchestration/close/recovery wording needed to make one-shot continuation explicit;
- regression tests for the contract.

Excluded:
- changing `chatgpt_only` Context Health;
- changing execution policy;
- changing `codex_workflow` worker/session mechanics;
- weakening independent review or user/deployment authorization gates.
