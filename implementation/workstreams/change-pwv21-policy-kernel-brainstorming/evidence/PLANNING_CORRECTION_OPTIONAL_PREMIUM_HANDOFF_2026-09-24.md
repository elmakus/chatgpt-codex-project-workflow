# Planning correction classification — optional Premium A/C fresh-context handoff

Date: 2026-09-24
Workstream: `change-pwv21-policy-kernel-brainstorming`
Status: Main-owned classification implemented as a durable correction entry;
it records an interpretive derivation under already accepted authority and
is neither a product-authority amendment (requirement/ADR/Definition change)
nor a Plan Review.

## Corrected state reconstructed and verified before mutation

- Definition R1 GREEN: 107 accepted requirements
  (`requirements/PWV21_POLICY_KERNEL.md`) + 5 accepted ADRs
  (ADR-PWV21-001…005); promotion `pwv21-policy-kernel@1` authorized.
- Planning cycle 1 / revision P1 frozen, planner audit GREEN, premium A
  satisfied for `definition:R1|planning-cycle:1`, premium B due for the
  exact frozen subject below, premium C not_due, no Plan Review record.
- Pre-mutation canonical route: `stop premium_B` for the exact P1 subject.

## Exact source pins (baseline commit `2e61bfbd9f19a7d756305b7facd2ff7657723260`)

Repo `elmakus/chatgpt-codex-project-workflow`, all blobs resolved at the
baseline commit unless noted; requirements, Definition, WORKSTREAM,
BRAINSTORM and cycle-1 PLANNING identities are recoverable from it.

- Workflow authority: current `elmakus/project_workflow_v2@main` controls
  operational routing; inspected package commit
  `elmakus/project_workflow_v2@986affffb7ba816e260e48549bf56e198ed51c21`,
  sections `workflow/PLANNING.md` (Premium cycle), `workflow/USER_STOP.md`
  (Premium A/B/C handoff behavior), `workflow/ROUTER.md` (Implemented
  routes). Consumer `workflow/` in this repo carries the V2 adoption
  record (`workflow/PWV2_ADOPTION.md`) alongside historical V1 material;
  it is not the operational router.
- Requirements:
  `elmakus/chatgpt-codex-project-workflow@2e61bfbd9f19a7d756305b7facd2ff7657723260:requirements/PWV21_POLICY_KERNEL.md@21ee85e6a306ce106cb26e77b0a395a2e671c054`
  (107 unique IDs, all `accepted`).
- ADR-PWV21-001:
  `elmakus/chatgpt-codex-project-workflow@2e61bfbd9f19a7d756305b7facd2ff7657723260:decisions/ADR_PWV21_POLICY_KERNEL.md@0662b970d80e8b76df79e4dbd458d190ce6d4402`
- ADR-PWV21-002:
  `elmakus/chatgpt-codex-project-workflow@2e61bfbd9f19a7d756305b7facd2ff7657723260:decisions/ADR_PWV21_ORCHESTRATION_CONTRACT.md@051f8fc3f68773349a1fcad39fcf1c60d3157532`
- ADR-PWV21-003:
  `elmakus/chatgpt-codex-project-workflow@2e61bfbd9f19a7d756305b7facd2ff7657723260:decisions/ADR_PWV21_PARALLEL_CARDS.md@437388345d7136cdcdf241bf3ca6aa1016ddb1c0`
- ADR-PWV21-004:
  `elmakus/chatgpt-codex-project-workflow@2e61bfbd9f19a7d756305b7facd2ff7657723260:decisions/ADR_PWV21_REVIEW_LIFECYCLE.md@567988b8789960308d9e5c91ccdc9d004f2f53b1`
- ADR-PWV21-005:
  `elmakus/chatgpt-codex-project-workflow@2e61bfbd9f19a7d756305b7facd2ff7657723260:decisions/ADR_PWV21_RECOVERY_MIGRATION_HANDOFF.md@fbaaaedac492ff9e2dbf4db9f8e86b3376df2023`
  (all five `accepted`, unchanged).
- Promoted Brainstorming source:
  `elmakus/chatgpt-codex-project-workflow@e2dd13b6a92cf14233a81a08ee86bcd5f5d84244:brainstorming/PWV21_POLICY_KERNEL.md@2e35a3cc2aeeb8f1bd950de0e1da324615db99b2`
  (unchanged).
- P1 frozen plan:
  `elmakus/chatgpt-codex-project-workflow@f4d7a13a295918c37afd23f4f55c5b6e4543e1b9:planning/PWV21_POLICY_KERNEL_MASTER_PLAN.md@59c3a3c3927d8572b6a8f98124652c17554cb012`
  (content commit `f4d7a13a295918c37afd23f4f55c5b6e4543e1b9`; bytes preserved).
- Cycle-1 frozen PLANNING record:
  `elmakus/chatgpt-codex-project-workflow@585840afa41b0000f5d5bc5efd0bacda7edb9fc1:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/PLANNING.toml@fb83b128c9a250737a8df5f96512079b9bc8bd27`
  (freeze commit; historical gates unchanged).
- Definition record:
  `elmakus/chatgpt-codex-project-workflow@2e61bfbd9f19a7d756305b7facd2ff7657723260:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/DEFINITION.toml@1708a32ae6fde67f7b7002b96a72d71a55e96310`
  (R1 GREEN, premium A satisfied, unchanged).
- Workstream manifest:
  `elmakus/chatgpt-codex-project-workflow@2e61bfbd9f19a7d756305b7facd2ff7657723260:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/WORKSTREAM.toml@5daf660934647b3193d3bf311db75685018b4616`.

## Why P1 coverage is semantically incomplete (M06/M07/Appendix)

P1 plans the premium/handoff surface only generically: M06 covers a stop
taxonomy, a locator-only handoff contract, and Git-outranks-narrative
reconstruction; M07 covers the stop-content contract and the
post-authorization re-evaluation loop; Appendix A maps REQ-077/081/082/
106/107 to taxonomy/schema/conflict/content/continuation tests. None of
these plan the concrete optional-gate input event: at an optional A/C
stop the user is offered two valid alternatives (stay in the current
context, or take the rendered locator to a fresh context), and the
deliberate selection of the offered fresh-context alternative is itself
the required gate input. P1 never states that the receiver must persist
the exact gate before continuing, that no second generic confirmation of
the same choice is due, or how already-satisfied recovery, idempotence,
and stale/wrong-subject locator rejection behave at A/C. The Appendix
rows therefore verify the surrounding mechanics without the gate-input
event they exist to serve. This is a Planning semantic/coverage omission
under already accepted R1, not a new product decision.

## Accepted-source derivation (interpretive; stated honestly)

No one accepted sentence says "choice itself satisfies". The obligation
follows from joint application of already accepted authority:

- REQ-077: continue automatically while the next obligation is
  deterministic and already authorized; stops are reserved for genuine
  boundaries and existing premium gates.
- REQ-081 + REQ-106: the optional A/C stop renders a ready-to-copy
  locator-only handoff as a valid offered alternative, not a mere hint.
- REQ-082: the receiving runtime reconstructs truth from canonical Git
  and continues without asking the user what to do when the route is
  deterministic.
- REQ-107: after user-supplied authorization/input, the router
  immediately re-evaluates durable state and continues all deterministic
  authorized transitions until the next real stop.
- REQ-004 + REQ-031: the kernel stays read-only; canonical writes are
  explicit governed coordinator/role actions with preconditions and
  mandatory readback/validation.
- V2 `workflow/PLANNING.md` premium-cycle + `workflow/USER_STOP.md`:
  A/C are optional handoffs (stay or move), B is a mandatory
  fresh-independent boundary; old gate subjects cannot authorize a new
  cycle; Git outranks stale narrative.

Derivation: the offered locator is an authorized alternative user action
for a context recommendation. Deliberately selecting that offered valid
alternative supplies the required gate input; the receiver durably
reconciles satisfaction (coordinator persists the exact gate with
preconditions + mandatory readback) and immediately continues
deterministic obligations. A second generic confirmation of the same
choice has no separate authorized purpose. Current Git/subject/
preconditions still win: this is NOT "any locator auto-authorizes".
REQ-077's premium exception retains each real initial gate; it cannot
create an extra confirmation after that gate's input. B keeps its exact
frozen subject and mandatory independent fresh review.

The promoted Brainstorming choices 70, 114, 115 corroborate the derivation,
and accepted ADR-PWV21-005 is consistent with it and remains part of the
accepted Definition authority; approved requirements and current V2 govern.

Competing reading considered: "no explicit event verb, therefore new
product authority is required". Rejected for this correction because the
missing piece is the recorder/procedure for an already-authorized input
(stay vs take-locator), i.e. executable-input detail, not an additional
user decision. Chat is not cited as durable product authority.

## Correction scope for P2 material planning (at new A, not here)

P2 planning must explicitly plan: both optional A/C alternatives (stay
vs fresh); deliberate offered fresh choice as input satisfying the exact
gate; receiver canonical reconstruction, preconditions, coordinator
persistence and mandatory readback (kernel stays read-only); immediate
deterministic next obligation with no duplicate confirmation;
already-satisfied recovery/idempotence; stale/mismatched old-cycle/
old-plan locator cannot satisfy the current gate; no runtime/session/
model IDs and no new arbitrary policy; B independence and its
exact-subject boundary unchanged. Existing 7 milestones, 107 requirement
ownerships, and robust parity/serialization/OR boundaries are preserved
unless later lawful P2 planning warrants adjustments.

## Required sequence and acceptance scenarios

Resolving this classification entry, or satisfying the new A alone, does
not resolve the plan's omission. The exact required sequence is: cycle-2
A satisfied for `definition:R1|planning-cycle:2` -> material P2
correction incorporates all listed A/C semantics plus the acceptance
scenarios below -> GREEN planner completeness/challenge audit for P2 ->
freeze the new exact P2 subject -> only then make B due for that exact
subject, with still no Plan Review performed in the producer context.

Scenarios the P2 audit must cover: A-stay, A-fresh, C-stay, C-fresh,
interrupted persistence/recovery, stale/wrong-subject locator rejection,
and B-distinct mandatory fresh review, each behaving per the derivation
above.

Current closure: classification + lawful correction entry complete;
material P2 correction still pending A.

## Lifecycle effect of this entry

- Frozen P1 bytes and its exact subject are preserved unchanged.
- Old cycle-1 PLANNING identity is preserved through the exact immutable
  locator pinned above (freeze commit `585840a...`, blob `fb83b128...`);
  no historical gate/review record changes; no review verdict claimed.
- Its pending B is explicitly superseded as the active route by new
  material cycle 2 (revision P2, `definition:R1|planning-cycle:2`,
  state draft, premium A due). Definition R1's satisfied A is unchanged.
