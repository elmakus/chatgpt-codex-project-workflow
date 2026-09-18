# Task Card Contract

This contract governs **authoring, decomposition and stable metadata** for project Task Cards.

Runtime execution/Refresh/DoD/result semantics for an already-defined card live in `workflow/contracts/TASK_EXECUTION.md`. Executors should not load this authoring contract merely to execute a normal serial card.

## 1. Meaning

A Task Card is a bounded global work-package contract for one project. It defines scope, authority, acceptance, tests and execution boundaries.

It is not the live execution-state record and it is not an OpenSpec `tasks.md` checkbox.

Mutable status, assigned executor, lane/base pointers, review state and result pointers live only in `implementation/TASK_BOARD.yaml`.

## 2. Required contract fields

Keep the mandatory card contract small. Each Task Card defines:
- `id`, `title`, `milestone`;
- `depends_on`;
- exact durable authority refs / authority slice;
- outcome and bounded included/excluded scope;
- acceptance criteria and required tests/checks;
- every material constraint, external-write/readback obligation, authorization gate or independent-review requirement that applies.

Priority, complexity, phase, code-location hints, capability hints and parallel metadata are optional and should exist only when they improve routing/execution/recovery.

Use `templates/TASK_CARD.md`.

### Authority Preservation Rule

Delegation may reduce context volume, but it must not reduce authoritative constraints applicable to delegated scope.

The card's authority slice should point as precisely as practical to:
- requirements;
- accepted decisions;
- Master Plan/milestone sections;
- relevant OpenSpec;
- accepted dependency results.

For downstream execution/review, either:
1. carry every applicable implementation-shaping constraint explicitly without semantic change; or
2. require reading the exact durable authority before acting.

Must-preserve information includes, when applicable:
- invariants and accepted behavior/architecture choices;
- failure semantics and compatibility requirements;
- explicit exclusions/rejected paths that constrain implementation;
- external-write, security, migration and data-integrity boundaries;
- acceptance/test obligations;
- dependency-result contracts;
- rationale when omitting it could reasonably cause a different implementation choice.

A summary/title/coordinator paraphrase never outranks exact authority. Executor and independent reviewer evaluate the same applicable authority slice.

## 3. Optional task requirements for mixed routing

Use `required_capabilities` only when explicit task requirements materially improve **mixed-policy pre-assignment routing** or document an unusual execution prerequisite.

This field describes what the **task requires**. It is not an inventory of what ChatGPT or Codex has.

Do not use it to trigger a fixed-policy preflight. Under `chatgpt_only`/`codex_only`, runtime availability is discovered only when the concrete operation is attempted.

## 4. Executor provenance and status

Executor provenance and execution/review/result state are mutable and live only in Task Board.

Normal card execution states:

```text
planned | ready | in_progress | blocked | done | superseded
```

Optional decision state remains separate:

```text
accepted | deferred | rejected | review
```

Independent review state, when active:

```text
pending | in_progress | green | red
```

Do not mirror these values into the Task Card file.

## 5. Deferred Card creation

Future Task Cards need not exist before their scope becomes knowable.

When correct scope materially depends on predecessor evidence:
- keep the dependency/JIT trigger in accepted durable authority;
- do not create a vague placeholder card;
- after predecessor GREEN evidence, the execution orchestrator creates the real bounded card(s);
- include the accepted predecessor result in the new card's authority slice;
- reconcile stable contracts and Task Board before execution.

This is L2 refinement only while requirements, accepted/frozen architecture/decisions, global invariants, milestone outcome and explicit authorization boundaries stay unchanged.

An already `in_progress` card is not casually rewritten through JIT decomposition.

## 6. Optional bounded-parallel metadata

Serial is default.

A card may participate in a project-level `bounded_parallel` execution set only when it explicitly records:

```yaml
parallel_safe: true
write_scope:
  - <repo-relative path or bounded glob>
exclusive_resources:
  - <logical mutable resource, when applicable>
```

Rules:
- omitted `parallel_safe` means `false`;
- mutable parallel work requires bounded `write_scope`;
- genuinely read-only work may have an empty write scope;
- concurrently active cards must have non-overlapping mutable write scopes and no shared exclusive resources;
- if ownership cannot be bounded confidently, keep the card serial;
- Task Board, milestone-wide handoff/acceptance/review state and shared integration bookkeeping are coordinator-owned;
- external mutable systems may be represented as `exclusive_resources`;
- unexpected overlap is a coordination blocker, not permission to race writes.

Detailed active-lane/coordinator semantics live in `workflow/contracts/GITHUB_STATE.md` and executor-specific orchestration modules.

## 7. Runtime contract

Once a card is defined and selected for execution, use `workflow/contracts/TASK_EXECUTION.md` for:
- readiness/start;
- Refresh Gate;
- runtime-operation behavior;
- blocker handling;
- bounded scope;
- required verification;
- Definition of Done;
- result state;
- review boundary;
- post-card continuation.

Do not load this authoring contract again during ordinary serial execution unless card metadata/decomposition itself must be interpreted or changed.

## 8. Near-term versus distant cards

Near-term cards may contain detailed implementation expectations.

Distant work stays functionally precise without freezing interfaces that are not yet knowable. Prefer an exact JIT trigger over speculative implementation detail.

## 9. Scope discipline while authoring

Cards should be bounded enough that implementation, acceptance and ownership are unambiguous.

Do not hide unrelated cleanup/architecture changes inside a card. If execution discovers a necessary adjacent change outside current authority, use normal corrective/dependency/JIT/strategic paths instead of silently expanding scope.
