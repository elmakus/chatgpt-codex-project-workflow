# ChatGPT-only Delegated Workers

This contract applies only under `execution_policy: chatgpt_only`.

## Purpose

Normal ChatGPT remains the fixed Task Card executor and may, when a stable Task Card explicitly requires it, delegate bounded execution or verification work to a project-defined worker profile.

Delegation is an execution mechanism inside the ChatGPT-owned Card. It is not a new workflow route, executor identity or mutable state authority.

## Terms

- **Task Card executor** — normal ChatGPT. It owns the active Card obligation, workflow decisions and Task Board transitions.
- **Delegated worker** — a bounded external process/tool/session invoked by ChatGPT to perform one assigned work item.
- **Worker profile** — a project-defined opaque identifier that resolves to a callable worker adapter plus its input/result contract. Generic workflow authority does not encode backend-specific CLI syntax.
- **Normalized result** — the bounded structured result returned to ChatGPT for workflow use.
- **Raw worker log/transcript** — provider/backend-native event, stdout, stderr or trajectory detail retained for evidence/debugging but not injected into the main ChatGPT context by default.

## Authority boundary

Delegated workers are subordinate to the ChatGPT executor.

A worker does not, merely by being delegated:
- select or advance Task Cards;
- edit `implementation/TASK_BOARD.yaml`;
- change requirements, decisions, plans, OpenSpec or workflow authority;
- issue milestone/Card acceptance on behalf of ChatGPT;
- satisfy a REQUIRED/RECOMMENDED Independent Review;
- merge, publish, push or perform a live/deployment write unless the active Card separately and explicitly authorizes that exact external write.

The worker result is evidence/input to the ChatGPT executor. ChatGPT remains responsible for checking the active Card's acceptance, tests, external-readback obligations and review gates.

## Card contract

Delegation is opt-in.

A Card that uses workers includes a stable `## Delegated workers` section. For every required worker step, identify at least:
- semantic role;
- project-defined worker profile;
- invocation point/order;
- exact task/authority input the worker must receive or read;
- workspace/worktree boundary;
- normalized result contract;
- failure/retry behavior when it differs from the default below.

The profile name and result contract must be defined well enough for execution before the Card becomes `ready`. This is contract readiness, not a runtime capability preflight. Do not probe future runtime/tool availability merely to author the Card.

A Card with no delegated-worker section follows ordinary `chatgpt_only` execution unchanged.

## Execution semantics

When execution reaches a declared worker step:

1. ChatGPT remains the active Task Card executor.
2. Resolve the Card's worker profile from project authority at the concrete invocation point.
3. Give the worker only the bounded task package/authority/workspace needed for its role. Progressive disclosure remains lossless by authority.
4. Invoke the project-defined worker interface and **await completion**.
5. Do not implement normal completion as periodic status polling or repeated "are you done?" checks.
6. The adapter/runtime may drain and persist raw worker output so the child cannot block, but the normal parent-facing return is only the normalized result plus bounded evidence/log references.
7. Validate the normalized result contract before treating the worker step as successful.
8. Verify actual repository/runtime/external state required by the Card instead of trusting worker prose alone.
9. Continue, retry or enter normal blocker/corrective handling according to the Card and workflow rules.

If the concrete runtime cannot perform the required worker invocation or await semantics, apply the normal runtime-operation rule: persist the exact blocker and request only the smallest real remedy. Do not silently run the delegated task inline merely to avoid the worker contract.

## Executor / tester separation

A delegated executor may implement the bounded task in its assigned workspace.

A delegated tester/verifier should normally receive:
- the accepted Card/review authority applicable to its check;
- the resulting repository/worktree/runtime state;
- required tests and acceptance criteria.

It should **not** receive the executor's raw transcript by default. This keeps verification independently grounded and avoids copying executor context through the orchestrator.

If debugging a failure genuinely requires raw log detail, escalate explicitly and read only the minimum relevant evidence.

## Leaf-worker invariant

Delegated workers are leaf workers by default.

One worker step maps to one project-assigned worker invocation. Do not enable backend-native nested subagent fan-out unless later accepted authority explicitly defines ownership, cancellation, accounting and review semantics for that nesting.

The ChatGPT executor owns project-level fan-out/sequencing.

## Failure semantics

A worker step is unsuccessful when, as applicable:
- the worker/backend reports failure;
- the invocation times out or is cancelled;
- the process/runtime fails;
- the normalized result is absent, malformed or violates its result contract;
- required resulting state contradicts the claimed success.

Worker failure never advances the Card automatically.

A Card may define a bounded retry policy. Otherwise use normal blocker/corrective handling. Do not turn an unbounded retry loop into hidden orchestration.

## State and evidence

`implementation/TASK_BOARD.yaml` remains the sole mutable execution-state authority.

Even when workers are used:
- Task Board `executor` remains `chatgpt`;
- do not create a second worker task/state ledger as workflow authority;
- raw worker logs are evidence/artifacts, not Task Board payloads;
- persist only the concise worker result/evidence pointers materially needed for Card acceptance/recovery.

The first delegated-worker contract assumes foreground/awaited worker steps. If a future design introduces durable detached workers that outlive the invoking turn/session, that requires a separate accepted state/recovery contract.

If execution is interrupted around a worker call, recover from actual repository/runtime evidence; do not infer completion from stale chat narrative.

## Independent Review remains separate

A delegated tester/verifier is **not** the workflow Independent Review role.

Under `chatgpt_only`, REQUIRED/RECOMMENDED Independent Review still follows `workflow/chatgpt_only/REVIEW.md`: the exact reviewed subject is frozen and a fresh normal ChatGPT chat issues the independent verdict.

Worker verification may be required Card evidence before that gate, but it does not replace the gate.

## Security and live-operation gates

Delegation does not weaken existing secret, external-write or live/deployment authorization boundaries.

Worker tasks and normalized results must not intentionally expose credentials/secrets. Backend-specific adapters own their own secure credential handling and log redaction/avoidance contract.

An explicit user/live authorization gate remains binding even if the intended mutation would be performed by a delegated worker.
