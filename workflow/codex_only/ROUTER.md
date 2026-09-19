# Codex-only Router

> M02 contract. Root policy routing MUST NOT select this namespace before M04.

## Policy boundary

This is the future `codex_only` project router. It uses genuinely policy-neutral common authority plus policy-local `workflow/codex_only/*` contracts. It does not depend on another policy namespace or the legacy shared execution core.

Codex Main is the fixed Project Workflow coordinator. `codex_workflow` owns runtime worker realization.

## State-selection prerequisite

Before interpreting implementation/review/recovery state:

1. resolve the exact default/workstream state context;
2. for branch-isolated work, validate manifest ID/branch binding before trusting its selected Task Board;
3. recover exact current branch/result/review evidence needed for the obligation;
4. never choose another workstream's Task Board to repair this one.

Full lifecycle/intake/stacked-workstream reconciliation is completed in M04.

## M02 durable priority model

Within the selected context, route the highest applicable obligation:

1. inconsistent durable project state -> Recovery;
2. active Intake/manifest binding obligation when applicable;
3. Card/milestone current review attempt `pending | in_progress` -> Independent Review;
4. implementation-owned Research `active | blocked | complete` -> Research/exact Return target;
5. current review attempt `red` -> RED corrective classification;
6. in-progress Card whose current attempt is `green` -> Execution post-review finalization;
7. other existing `in_progress | blocked` Card -> Execution/Recovery;
8. manifest final-integration review obligation -> Review/RED handling as applicable;
9. deterministic READY serial implementation -> Execution;
10. milestone/workstream Close when its prerequisites are satisfied;
11. Planning/Definition/Research when accepted authority requires escalation.

M03 replaces only the serial READY selection with bounded compatible-ready-set semantics; it does not change review/Research/RED priority.

## RED corrective classification

For the exact current RED attempt/evidence:

- bounded Card-owned production correction inside accepted L1/L2 authority -> Execution, returning through Main to that Card's owning `executor` role;
- bounded milestone-owned production correction -> Execution Prep to reopen/create the exact affected corrective Card(s) under the semantic `executor` owner role;
- other execution decomposition/detail correction -> Execution Prep;
- plan-only strategy/milestone defect while Definition remains valid -> Planning;
- accepted requirement/strategic/global-target defect -> Definition;
- missing evidence before classification/correction -> materialize exact implementation-owned Research continuation, then Research;
- unresolved user/product authority, explicit live/deployment authorization, or concrete unremediable runtime/input gate -> real stop;
- incoherent evidence/state -> Recovery.

Tester/reviewer never becomes the repair role.

## Formal-review continuation

Completion of one review role is not a user stop.

- GREEN -> return through router to post-review finalization/continuation.
- RED -> preserve verdict, then route deterministic correction when authorized.
- corrected subject -> freeze a new pending attempt and route to independent review.
- same logical Tester reuse or replacement is runtime-owned; router sees only project attempt state.

A qualifying Codex-managed formal review never requires a second normal-ChatGPT review solely for independence.

## No capability policy switching

Fixed `codex_only` does not run capability preflight and never changes execution policy because of runtime convenience. A concrete runtime blocker follows normal Recovery/blocker/user-gate rules.

## Continuation

Completing a role is not a stop. Continue deterministic authorized transitions through Codex Main until a real strategic/product decision, explicit authorization, concrete unremediable runtime/input blocker, end of approved scope, or policy-defined safe context handoff owns the boundary.

M04 reconciles the full Intake/Brainstorming/Research/Definition/Planning/Micro-fix/Close router and performs root cutover only after namespace completeness is proven.
