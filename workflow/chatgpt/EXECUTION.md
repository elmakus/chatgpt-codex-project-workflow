# ChatGPT Execution Adapter

Read this when:
- project policy is `chatgpt_only`; or
- project policy is `mixed` and Capability Gate selected `EXECUTE IN CHATGPT`; or
- recovering already ChatGPT-assigned in-progress work or a pending independent ChatGPT review.

ChatGPT executes the shared `workflow/EXECUTION.md` loop using tools/plugins/connectors available in the current **normal ChatGPT chat**.

ChatGPT Work is not part of this workflow.

## Fixed-policy capability rule

Under `chatgpt_only`, do **not** perform a capability preflight, inventory or checklist before starting a Task Card. The policy already selected ChatGPT as executor.

Run the normal state/contract Refresh Gate, then attempt the actual work. If a concrete required operation cannot be performed with the current chat's tools/plugins/connectors, persist the runtime blocker and tell the user the smallest remedy. Do not speculate about capabilities that might be needed later.

A missing capability does not change policy automatically. The user may provide the missing access/tooling or explicitly change `execution_policy`, after which durable Task Board state is reconciled before reassignment.

## Repository execution

When GitHub write capabilities exist, ChatGPT may create branches, modify files, commit, open/update PRs and inspect CI/diffs according to branch policy. After material writes, read back relevant refs/files/status when meaningful.

When executing multiple project-level cards in parallel, isolate mutable lanes, keep Task Board/global state coordinator-owned, integrate one lane at a time and verify post-integration state.

Bounded-parallel Task Board state does not require ChatGPT to manufacture concurrency it does not have. Execute a compatible subset or one card when needed.

## Local execution

Use available Python/container/file-processing capabilities for tests, simulations, transformations and artifacts when they validly exercise target. Do not misrepresent isolated ChatGPT runtime as user's local/production runtime.

## Plugins/external systems

ChatGPT may perform external reads/writes through connected plugins/connectors when contract permits. Follow provider prerequisites and shared `WRITE → READBACK → VERIFY` contract. Shared mutable external targets remain serialized.

## Human-facing ChatGPT control summary

Normal ChatGPT responses to the user are a **human control surface**, not a dump of durable execution telemetry.

By default, report only what the user needs to understand or act:

1. **What happened / what was found** — plain-language result, especially any actual errors, risks or blockers.
2. **What it means** — one short explanation of impact.
3. **What happens next** — whether ChatGPT continues automatically, needs a user decision, or requires/recommends a fresh chat.
4. **Fresh-chat prompt** — when a fresh chat is required or recommended, include the ready-to-copy prompt immediately as required by the shared workflow.

Prefer ELI5-style operational language over internal workflow jargon when both convey the same meaning.

Do **not** include by default:
- commit/review SHAs, blob IDs or tree IDs;
- exact branch/HEAD pointers;
- internal evidence file paths;
- raw Task Board fields;
- long test inventories or exact test counts;
- changed-file lists;
- internal OpenSpec/task bookkeeping;
- worker/session orchestration details.

Those facts must still be persisted correctly in durable project state. Omit them only from the default human-facing response.

Show technical identifiers/details when:
- the user explicitly asks for them;
- the user must copy/use the exact value to perform an action;
- a blocker/ambiguity cannot be explained safely without the exact identifier;
- a security/recovery/debugging situation makes the exact pointer materially useful.

If no user action is required, say that plainly. If there is a blocker, describe the blocker in ordinary language and ask only for the smallest concrete decision/input.

Example review-boundary UX:

```text
Implementacja tej karty jest gotowa i testy nie wykazały problemów.

Teraz potrzebny jest niezależny review w nowym czacie, bo ten czat wykonywał implementację. Nie uruchamiam kolejnej karty przed review.

USER ACTION REQUIRED: otwórz nowy czat i wklej poniższy prompt.

<copy-paste NEW CHAT START PROMPT>
```

Exact review subject, evidence, test details and Git pointers remain in the repository and are recovered by the next chat.

## Independent review handoff

Under `chatgpt_only`, a chat that implemented a subject must **not** issue that subject's REQUIRED or RECOMMENDED independent-review verdict.

At the review boundary:
1. freeze/persist exact `review_subject` and implementation/test evidence;
2. set Task Board `review_state: pending` plus pointers;
3. commit/push durable state when possible;
4. stop execution for this chat;
5. report exactly that user action is required to start a **fresh normal ChatGPT chat** from `implementation/TASK_BOARD.yaml` for independent review;
6. include in the same response a minimal copy-paste-ready fenced `NEW CHAT START PROMPT` pointing to the project repo, exact active project/implementation branch, pending review target and durable start pointer.

The fresh review chat independently reads the exact subject and durable evidence, sets `review_state: in_progress`, persists GREEN/RED evidence, and sets `review_state: green | red`.

After GREEN, that fresh review chat may continue subsequent deterministic `chatgpt_only` work. If it later implements a new subject requiring/recommending review, a further fresh chat is required at that new review boundary.

OPTIONAL review does not force a fresh-chat stop unless the project/card explicitly chooses to perform it.

## Chat/session continuity

Workflow roles are not tied to a specific ChatGPT chat. Under `chatgpt_only`, the same current chat may continue from planning/JIT orchestration into execution when durable authority is clear and context remains useful.

A **fresh chat is mandatory only** for REQUIRED/RECOMMENDED independent review of a subject implemented by the current chat.

Outside that independence boundary, a fresh chat is optional context hygiene. Recommend one when prior conversational context has become stale, contradictory, overly broad, or otherwise likely to obscure the durable project state, especially at a clean checkpoint where recovery is deterministic. Do not impose a fixed token count or “every N milestones” rule. If recommending one, include its copy-paste-ready minimal start prompt immediately; never make the user ask separately for it. The prompt always includes the exact active branch, even when it is `main`.

A fresh chat must recover from `PROJECT.md`, Task Board and exact referenced durable authority. It must not require the previous chat transcript to reconstruct execution truth. Account/project-level context may still exist, but durable repository authority outranks it.

## Continuation

Under `chatgpt_only`, continue deterministic READY work and cross GREEN milestone boundaries automatically when next milestone is already approved, required/recommended review gates are GREEN and shared continuation conditions hold. Do not run Capability Gate or capability preflight at each card/milestone.

Under `mixed`, a new assignment is routed through Capability Gate as required by shared execution semantics.

A fresh ChatGPT chat may be **recommended** for context hygiene at clean boundaries; that is different from the **mandatory** fresh-chat handoff required for independent review of a subject implemented by the current chat.

## Runtime blocker

Do not claim completion when a concrete required operation is unavailable. Persist evidence and mark the affected Task Board card blocked when its contract cannot be met.

Under `chatgpt_only`, ask for the smallest missing capability/access or let the user explicitly change policy. Under `mixed`, do not silently reroute an already-started card.
