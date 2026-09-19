# Codex-only Router

> M03 contract. Root policy routing MUST NOT select this namespace before M04.

## Policy boundary

This is the future `codex_only` project router. It uses genuinely policy-neutral common authority plus policy-local `workflow/codex_only/*` contracts. It does not depend on another policy namespace or the legacy shared execution core.

Codex Main is the fixed Project Workflow coordinator. `codex_workflow` owns runtime worker realization.

## State-selection prerequisite

Before interpreting implementation/review/recovery state:

1. resolve exact default/workstream context;
2. for branch-isolated work, validate manifest ID/branch binding before trusting its Task Board;
3. recover exact branch/result/review/batch evidence needed for the obligation;
4. never choose another workstream's Task Board to repair this one.

Full lifecycle/intake/stacked-workstream reconciliation is completed in M04.

## M03 durable priority model

Within the selected context, first classify whether a Card review belongs to an integrated member of the exact unresolved `current_batch`. Such an attempt may be frozen only as `pending`; it is a deferred batch-member review and does not outrank completion of that same batch. If that attempt is already `in_progress | red | green` while the batch is unresolved, route Recovery because production review/correction was allowed to interleave with frozen integration.

Then route the highest applicable obligation:

1. inconsistent durable project state -> Recovery;
2. active Intake/manifest binding obligation when applicable;
3. non-deferred Card/milestone current review attempt `pending | in_progress` -> Independent Review;
4. implementation-owned Research `active | blocked | complete` -> Research/exact Return target;
5. non-deferred current review attempt `red` -> RED corrective classification;
6. in-progress Card whose non-deferred current attempt is `green` -> Execution post-review finalization;
7. existing current parallel batch `prepared | running | integrating | blocked` or member `returned`, including batches with deferred pending member reviews -> Execution/Recovery for that exact batch;
8. other existing `in_progress | blocked` Card -> Execution/Recovery;
9. manifest final-integration review obligation -> Review/RED handling as applicable;
10. deterministic READY set -> Execution Prep to evaluate a bounded compatible batch; when no batch of at least two is safe, deterministic serial Execution;
11. milestone/workstream Close when prerequisites are satisfied;
12. Planning/Definition/Research when accepted authority requires escalation.

Outside the exact deferred-review exception, Review/Research/RED obligations keep their normal priority. After `current_batch` is cleared, any frozen member reviews are no longer deferred and are dispatched deterministically in canonical Task Board order. Durable returned/integrated lane results remain preserved throughout.

## Bounded READY selection

Parallelism is optional and per selected Task Board.

- Planning candidate overlap is not runnable authority.
- Execution Prep evaluates current READY Cards in canonical Task Board order.
- A batch is legal only after exact M03 eligibility proof and freeze.
- Batch membership is finite and never dynamically refilled.
- Missing/unsafe parallel proof means serial fallback, not policy switching or a user stop.
- No repository-global scheduler/queue is introduced.

## RED corrective classification

For exact RED evidence:

A RED verdict for a Card's original batch-integrated subject is legal only after that batch is complete/current-null under the M03 deferral rule. If durable state shows such RED while the originating batch is still current, route Recovery before any correction.

- bounded Card-owned production correction inside accepted L1/L2 authority -> Execution, returning through Main to that Card's owning `executor` role;
- bounded milestone-owned production correction -> Execution Prep to reopen/create exact affected corrective Card(s);
- other execution decomposition/detail correction -> Execution Prep;
- plan-only strategy/milestone defect while Definition remains valid -> Planning;
- accepted requirement/strategic/global-target defect -> Definition;
- missing evidence -> materialize exact implementation-owned Research continuation, then Research;
- unresolved user/product authority, explicit live/deployment authorization, or concrete unremediable runtime/input gate -> real stop;
- incoherent evidence/state -> Recovery.

A Card that was formerly a parallel member does not make its RED correction automatically parallel-safe. JIT must re-evaluate new concurrency.

Tester/reviewer never becomes the repair role.

## Parallel blocker classification

For current batch evidence:

- missing/false opt-in, incompatible scope/resource or unavailable isolation discovered before launch -> use the prepared-batch abandonment transition: record blocked history/evidence, reconcile every batch-owned `in_progress` Card back to legal READY/serial state, then clear `current_batch`; rebuild with a new batch ID or fall back serially;
- returned diff outside write scope or touching reserved shared state -> blocked Recovery/correction; do not integrate;
- integration conflict inside accepted technical authority -> Recovery/Execution reconciliation while preserving returned results and frozen order;
- conflict requiring milestone strategy change -> Planning;
- conflict requiring accepted product/system authority change -> Definition;
- missing evidence needed to classify -> Research;
- concrete unremediable runtime/access/input gate -> real stop.

Runtime worker loss alone is not a project blocker when the member can be resumed/replaced from durable batch state.

## Formal-review continuation

Completion of one review role is not a user stop.

- GREEN -> post-review finalization/continuation.
- RED -> preserve verdict and route deterministic correction.
- corrected subject -> freeze a new pending attempt.
- runtime reviewer reuse/replacement does not change project attempt identity.

A qualifying Codex-managed formal review never requires a second normal-ChatGPT review solely for independence.

## No capability policy switching

Fixed `codex_only` does not change execution policy because concurrency or a particular worker realization is unavailable. Parallel-safety failure falls back to serial execution when the Card itself remains executable.

## Continuation

Completing a role is not a stop. Continue deterministic authorized transitions through Codex Main until a real strategic/product decision, explicit authorization, concrete unremediable runtime/input blocker, end of approved scope, or policy-defined safe context handoff owns the boundary.

M04 reconciles the complete lifecycle router and performs root cutover only after namespace completeness is proven.
