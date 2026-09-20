# Codex-only Independent Review

> Live Codex-only independent-review contract. M02 immutable-subject/role independence applies to Card, milestone, plan and workstream final-integration review.

## Formal review semantics

A qualifying Codex-managed reviewer satisfies the Project Workflow review gate. Normal-ChatGPT session identity is not part of formal independence and no second mandatory normal-ChatGPT review follows a qualifying verdict.

Formal review requires:

- one immutable exact subject;
- the same applicable authority and acceptance surface that governed implementation;
- an independent Tester role distinct from the subject's implementation owner;
- no production repair/mutation by the Tester while reviewing;
- durable verdict/evidence;
- Codex Main as the sole shared Project Workflow state writer.

Concrete worker/session/model/profile/invocation/wait/resume/replacement mechanics belong to `codex_workflow`.

## Review owner

Resolve exactly one project review owner before judging:

- Card/milestone review -> selected canonical Task Board review block;
- workstream final-integration review -> selected manifest `review.requirement/state/subject/evidence/covered_by`; the manifest owns this distinct gate and `WORKSTREAMS.md`/`CLOSE.md` own refresh/coverage reconciliation;
- plan review -> revision-specific plan-review record under `PLAN_REVIEW.md`.

Never mirror one review lifecycle into another.

## Card/milestone attempt lifecycle

The Task Board review block is defined by `STATE.md`.

### Freeze

After a reviewable implementation result is durable, Codex Main:

1. verifies the Card/milestone stable contract requires/recommends review;
2. verifies the exact production result/subject and implementation evidence;
3. records/resolves `implementation_owner_role` on the reviewed Card or milestone (normally `executor`);
4. for a milestone subject, treats that role as aggregate production ownership and requires runtime independence from every concrete Executor realization that contributed production to the exact checkpoint;
5. appends the next stable attempt ID with exact immutable `subject`, `state: pending`, `reviewer_role: tester`, and null evidence;
6. points `current_attempt` to that attempt.

Do not mutate an existing attempt to point at a different subject.

### Start

Before asking runtime to realize or re-realize the Tester, Codex Main satisfies `workflow/codex/CODEX_ORCHESTRATION.md#Codex-only pre-dispatch binding gate`. Only after that gate is satisfied may runtime supply a Tester that is independent from the worker that realized the exact subject's implementation-owner role and Main change the attempt to `in_progress`.

Project Workflow records only the semantic reviewer role. Main persists the state transition; the Tester does not write the shared Task Board.

### Verdict

Tester returns one full verdict package for the exact subject:

- GREEN or RED;
- concise evidence against the complete applicable authority/acceptance surface;
- confirmation that the subject was not mutated/repaired during review;
- confirmation that reviewer independence held.

Codex Main verifies the verdict package identifies the current attempt/subject, writes the durable evidence, then persists `green | red`.

A terminal attempt without durable evidence is invalid.

## GREEN

After GREEN:

1. preserve the attempt/evidence unchanged;
2. reviewer role ends;
3. Main returns through the policy router;
4. for Card completion, Execution performs deterministic post-review finalization only if the result remains exactly the GREEN subject;
5. deterministic authorized continuation proceeds without a user/normal-ChatGPT stop.

Runtime loss after a durable GREEN verdict does not reactivate review.

## RED -> owning-Executor repair

RED is not a user stop when bounded correction is authorized.

After RED:

1. preserve the RED attempt/evidence;
2. Tester role ends and must not repair production;
3. Main classifies the failing evidence against accepted authority;
4. bounded Card-owned L1/L2 production correction returns through Main to that Card's `implementation_owner_role: executor`;
5. bounded milestone-owned production correction returns through Main to Execution Prep, which reopens or creates the exact affected corrective Card(s) with `implementation_owner_role: executor`;
6. plan-only defects route to Planning; accepted product/system authority defects route to Definition; missing evidence routes through Research; unresolved real user/authorization/runtime input gates stop normally;
7. the owning Executor role produces the corrected Card implementation(s), after which Main derives the corrected reviewed owner subject (Card result or milestone checkpoint);
8. Main freezes that corrected exact subject as a new pending attempt while the RED attempt remains unchanged;
9. the next Tester performs a full recheck of the new subject.

The same logical Tester may perform the new attempt when independence remains valid and runtime resume is safe. Runtime may fail closed to a replacement Tester. Neither choice is Project Workflow identity/state.

## Runtime loss during pending/in-progress review

A lost/replaced reviewer does not create a new project attempt when the subject is unchanged.

Main keeps the same attempt/subject. Before runtime resume/replacement of the reviewer, Main re-applies the shared pre-dispatch binding gate; `codex_workflow` then safely resumes or replaces the runtime reviewer. The resumed/replacement reviewer performs the full review required for that subject.

If complete durable verdict evidence exists but Task Board still says `in_progress`, Recovery may reconcile that exact verdict only after proving evidence matches the same attempt/subject. Otherwise perform the full review again on the same attempt.

## Review evidence durability

Prior RED/GREEN attempts remain addressable in the Task Board attempt list. Never overwrite prior evidence merely because a newer subject becomes current.

Review evidence must not include a runtime identifier as a required project key. It may state semantic facts such as `implementation owner role: executor`, `reviewer role: tester`, `independence: verified`.

## Workstream final-integration review

For a REQUIRED/RECOMMENDED manifest gate, run target refresh before first freeze/reuse. If an already-independent Card/milestone verdict covers the identical refreshed workstream subject and complete acceptance surface, `CLOSE.md` may reconcile the manifest gate GREEN with exact `covered_by` evidence. Otherwise freeze exact manifest `review.subject`, set `review.state: pending`, and enter this module's **Start** transition, which applies the shared pre-dispatch binding gate before runtime realizes an independent Tester.

Target movement alone does not invalidate GREEN. Material change to covered workstream content/behavior or acceptance surface does; preserve prior evidence and freeze a new exact subject. Any concrete production worker that contributed to the changed subject cannot be its Tester.

M03 lane/batch provenance remains immutable under these rules. Internal batch review never replaces this distinct final-integration gate unless exact stronger coverage is proven.
