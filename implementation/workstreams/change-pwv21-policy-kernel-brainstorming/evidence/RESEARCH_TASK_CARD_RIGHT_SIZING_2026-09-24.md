# Research Review — Task/Card Right-Sizing in Mature Agentic Software-Development Workflows

Date: 2026-09-24  
Repository: elmakus/chatgpt-codex-project-workflow  
Branch examined: work/pwv21-policy-kernel-brainstorming  
Artifact class: research evidence only  
Authority status: NON-AUTHORITATIVE. This report records external research and design recommendations. It does not amend requirements, ADRs, Planning, Cards, Task Board state, or any Project Workflow authority.

## Research question

What semantics should an agentic software-development workflow use to decide when a milestone, phase, story, or similar higher-level scope should be split into multiple independently executable implementation units rather than being allowed to become one large task/Card for one coding agent?

The concrete PWv2.1 design question is whether the existing decomposition vocabulary — Strategic Planning milestones, JIT Execution Prep, required_seam / preferred_seam / illustrative, decomposition audits for independent implementability, testability/falsifiability, reviewability, invariant family, dependencies, atomicity and coupling, plus independent Card Review and separate Milestone Review — needs a stronger generic Card right-sizing invariant.

A candidate rule considered during this research was:

> A Card is the smallest meaningful unit that produces an independently testable deliverable and is worth an independent review gate. If a reviewer could reasonably approve one surface while rejecting another, those surfaces should normally be separate Cards.

The research conclusion is that the first sentence is strongly supported, but the second sentence needs a semantic qualifier. The strongest transferable rule is not “split every distinct technical surface.” It is “split independently meaningful acceptance/review outcomes unless concrete atomicity or coupling makes separation artificial.”

## Executive conclusion

PWv2.1 should add a stronger generic Card right-sizing invariant.

The current PWv2.1 decomposition rules are already unusually strong in the dimensions they require Execution Prep to inspect, but they remain materially incomplete because they do not contain a sufficiently explicit decision rule for when those dimensions cross the threshold from “audit this topology” to “this candidate Card must normally be split.”

The strongest common pattern across the researched systems is:

**An agent-sized implementation unit should represent one coherent outcome that can be implemented and verified within a bounded context, while preserving useful independent acceptance when a real semantic seam exists.**

Superpowers states the review-boundary form of this principle most directly. Its current writing-plans skill defines a task as the smallest unit carrying its own test cycle and worth a fresh review gate, folds setup/configuration/scaffolding/documentation into the task that needs them, and says to split only where a reviewer could meaningfully reject one task while approving its neighbor.

BMAD provides the most important counterweight: one cohesive user-facing goal may legitimately span several layers and files. It defines multiple goals in terms of top-level independently shippable deliverables that could each be reviewed, tested, and merged separately without breaking the others, and explicitly says not to split cross-layer implementation details merely because they are different surfaces.

GitHub Spec Kit organizes implementation around independently testable user stories and dependency order, but for large features first scopes implementation runs or delegates parallel tasks before escalating to separate specs. GSD makes context budget and dependency topology first-class, but its fresh-context unit is a PLAN containing several tasks, not each tiny task. OpenSpec requires tasks to be small enough for one session and individually verifiable, while deliberately not attaching an independent reviewer to every task.

Together these systems imply that “independently testable” is necessary but not sufficient for a PW Card, because a PW Card carries more lifecycle weight than a checklist item: its own mutating Worker ownership, result identity, evidence, and mandatory independent review.

For PWv2.1, the recommended core rule is therefore:

**A Card should be the smallest meaningful execution-and-review ownership unit that produces one coherent, independently falsifiable outcome. When a candidate Card contains two or more separable acceptance, contract, invariant, or independently useful delivery outcomes such that each can reach a valid state and a reviewer could reasonably GREEN one while REDing another, separate Cards are presumptively required. The presumption is rebutted only by concrete atomicity, invalid-intermediate-state, inseparable-acceptance, or material-coupling evidence. Different files, modules, layers, tools, or implementation steps are not by themselves separate Cards.**

This is a research recommendation only, not accepted PWv2.1 authority.

---

## 1. Research method and source snapshots

The review prioritized current official repositories and implementation-facing workflow instructions rather than marketing descriptions. The source snapshots below were queried on 2026-09-24.

### Superpowers

Repository: obra/superpowers  
Snapshot commit: 5bf4e78011075bcfc0dc295f0724994cd123ee71

Primary sources:

- writing-plans task right-sizing:
  https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/writing-plans/SKILL.md
- subagent-driven-development:
  https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/subagent-driven-development/SKILL.md
- related design rationale for task right-sizing overhead:
  https://github.com/obra/superpowers/blob/5bf4e78011075bcfc0dc295f0724994cd123ee71/docs/superpowers/specs/2026-06-10-strict-cost-sdd-design.md

### GitHub Spec Kit

Repository: github/spec-kit  
Snapshot commit: 25d43a9482af998dc932142d0398794635a3a5e8

Primary sources:

- task generation:
  https://github.com/github/spec-kit/blob/25d43a9482af998dc932142d0398794635a3a5e8/templates/commands/tasks.md
- complex-feature/context handling:
  https://github.com/github/spec-kit/blob/25d43a9482af998dc932142d0398794635a3a5e8/docs/concepts/complex-features.md
- workflow including final converge step:
  https://github.com/github/spec-kit/blob/25d43a9482af998dc932142d0398794635a3a5e8/docs/quickstart.md

### BMAD Method

Repository: bmad-code-org/BMAD-METHOD  
Snapshot commit: 1b59caa7f96459fda6750c225a9330283e108fd6

Primary sources:

- bmad-build scope standard:
  https://github.com/bmad-code-org/BMAD-METHOD/blob/1b59caa7f96459fda6750c225a9330283e108fd6/skills/bmad-build/workflow.md
- build specification/task template:
  https://github.com/bmad-code-org/BMAD-METHOD/blob/1b59caa7f96459fda6750c225a9330283e108fd6/skills/bmad-build/spec-template.md
- current ticketing/slicing semantics:
  https://github.com/bmad-code-org/BMAD-METHOD/blob/1b59caa7f96459fda6750c225a9330283e108fd6/skills/bmad-preview-ticketing/references/slice.md
- ticketing vs epics explanation:
  https://github.com/bmad-code-org/BMAD-METHOD/blob/1b59caa7f96459fda6750c225a9330283e108fd6/skills/bmod-method/help/ticketing-and-epics.md
- sprint guidance recommending fresh-context code review:
  https://github.com/bmad-code-org/BMAD-METHOD/blob/1b59caa7f96459fda6750c225a9330283e108fd6/skills/bmad-sprint-planning/scripts/sprint_plan.py
- epic-level aggregate review:
  https://github.com/bmad-code-org/BMAD-METHOD/blob/1b59caa7f96459fda6750c225a9330283e108fd6/skills/bmad-retrospective/workflow.md

### Get Shit Done (GSD)

Repository: gsd-build/get-shit-done  
Snapshot commit: bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815

Primary sources:

- planner:
  https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/agents/gsd-planner.md
- phase execution:
  https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/get-shit-done/workflows/execute-phase.md
- user guidance on oversized plans:
  https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/docs/USER-GUIDE.md
- architecture/features background:
  https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/docs/ARCHITECTURE.md
  https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/docs/FEATURES.md

### OpenSpec

Repository: Fission-AI/OpenSpec  
Snapshot commit: db2309783547a14e150dbcbfc19120e4028446c3

Primary sources:

- default spec-driven schema and task-authoring instructions:
  https://github.com/Fission-AI/OpenSpec/blob/db2309783547a14e150dbcbfc19120e4028446c3/schemas/spec-driven/schema.yaml
- concepts:
  https://github.com/Fission-AI/OpenSpec/blob/db2309783547a14e150dbcbfc19120e4028446c3/docs/concepts.md
- overview and iterative artifact semantics:
  https://github.com/Fission-AI/OpenSpec/blob/db2309783547a14e150dbcbfc19120e4028446c3/docs/overview.md
- whole-change verification:
  https://github.com/Fission-AI/OpenSpec/blob/db2309783547a14e150dbcbfc19120e4028446c3/skills/openspec-verify-change/SKILL.md

### Additional system: Task Master

Repository: eyaltoledano/claude-task-master  
Snapshot commit: c0c98d367c55296bfe69e65680625b6db437af02

Primary sources:

- complexity analysis:
  https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/scripts/modules/task-manager/analyze-task-complexity.js
- task expansion:
  https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/packages/claude-code-plugin/commands/expand-task.md
- task structure and complexity report guidance:
  https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/docs/task-structure.md

Task Master is included because it adds a materially different approach: AI-assessed complexity followed by adaptive expansion, rather than defining a strong semantic review boundary.

---

## 2. Cross-workflow comparison

| Workflow | Primary agent-sized implementation unit | Main right-sizing rule | Fresh implementation context? | Independent review per unit? | Higher-level verification/review |
| --- | --- | --- | --- | --- | --- |
| Superpowers | Task | Own test cycle; independently testable deliverable; worth fresh reviewer gate; split where reviewer can reject one and approve neighbor | Yes in SDD: fresh implementer per task | Yes in SDD: task review after every task | Broad whole-branch review |
| GitHub Spec Kit | User-story phase plus tasks; optionally separate sub-spec | User story independently testable; tasks dependency-ordered; scope implementation run to context; decompose into sub-specs only when needed | Optional task subagents; otherwise separate implementation invocations | No universal mandatory review per checklist task | speckit-converge across feature |
| BMAD | Story/spec as meaningful unit; implementation tasks inside it | One cohesive user-facing goal; split top-level independently shippable deliverables; do not split cohesive cross-layer details | Fresh context recommended between story implementation and code review; story sessions are natural boundaries | Story-level code review, not one independent review per internal implementation task | Epic retrospective includes aggregate/diff-scope review |
| GSD | PLAN.md containing 2–3 tasks | One concern; dependency waves; file conflict constraints; explicit context budget; split if plan exceeds reliable context | Yes: executor per plan has fresh context | Verification exists, but lower-level tasks are not each independent review units | Phase verification/UAT |
| OpenSpec | Change with task checklist | Related tasks grouped; dependency ordered; each task small enough for one session and states verification | Not required by core semantics | No mandatory independent review per task | Whole-change verification: completeness/correctness/coherence |
| Task Master | Task/subtask | Complexity analysis and expansion into subtasks | Runtime dependent | Not intrinsic | Not intrinsic |

The critical comparison is that the word “task” has different lifecycle weight in each product. OpenSpec and BMAD internal tasks are closer to checklist/action items. Superpowers Task, GSD Plan, and BMAD Story are closer to a PW Card because they package enough work to justify a separate bounded execution context and, in Superpowers/BMAD, an independent review boundary.

Therefore a PW Card should not be sized like the smallest checklist task in the ecosystem.

---

## 3. Superpowers: strongest direct precedent for review-worthy units

Superpowers provides the most explicit current right-sizing semantics found in the review.

Its writing-plans skill states, in substance:

- a task is the smallest unit with its own test cycle that is worth a fresh reviewer gate;
- setup, configuration, scaffolding, and documentation are folded into the task whose deliverable needs them;
- splitting should occur only where a reviewer could meaningfully reject one task while approving its neighbor;
- every task ends in an independently testable deliverable.

The same skill separately defines “bite-sized” steps as actions such as writing a failing test, running it, implementing the minimum fix, running passing tests, and committing. This is important because it demonstrates an explicit hierarchy:

**Step ≠ Task.**

A 2–5 minute action may be a useful planning step but is intentionally not promoted into an independently reviewed agent ownership unit.

Superpowers SDD then makes the task boundary operationally expensive and therefore semantically meaningful:

- dispatch a fresh implementer subagent per task;
- the implementer tests, commits, and self-reviews;
- dispatch a task reviewer after the task;
- review spec compliance and code quality;
- re-review after repair;
- after all tasks, run a broad final whole-branch review.

This architecture gives Superpowers a strong incentive not to over-decompose, because every extra Task incurs both a fresh implementation context and a review cycle. The repository's strict-cost SDD design explicitly documents that tiny tasks such as “create .gitignore” were causing unnecessary dispatch/review overhead and motivates the present right-sizing rule.

### Superpowers lesson for PW

This is the closest external analogue to PWv2.1 because PW also gives a Card its own implementation owner/result and independent review gate.

The transferable part is not a numeric size cap. It is the semantic statement:

**If the lifecycle cost includes a fresh implementation/review boundary, the unit should be large enough to deserve that lifecycle but small enough to admit one coherent independent verdict.**

The reviewer split test is therefore strong evidence for PW — provided “one part” refers to a meaningful acceptance/contract/delivery unit, not merely a file or architectural layer.

---

## 4. GitHub Spec Kit: vertical user-story slices plus execution scoping

Spec Kit's tasks generator organizes implementation around user stories. The current tasks command requires:

- tasks organized by user story;
- a dependency graph showing user-story completion order;
- parallel execution examples;
- completeness validation such that each user story has all required tasks and is independently testable;
- one phase per user story, with a story goal and independent test criteria;
- MVP-first incremental delivery.

This puts the primary semantic boundary at the independently testable user-story increment rather than at a file or layer.

Spec Kit's complex-feature guidance adds a second dimension: implementation context capacity.

It explicitly documents a failure mode where long implementation runs degrade as the context window fills: agents lose the plan, ignore tasks, or hallucinate around context compaction. Its preferred response is graduated:

1. limit how many tasks run in one implementation invocation;
2. delegate suitable parallel tasks to focused subagents;
3. combine scoping and delegation;
4. only when one phase is itself still too large, split the feature into independently specified sub-features, each with its own spec/plan/tasks/implement lifecycle.

This is important because it separates two problems:

- **semantic decomposition** — what the independently meaningful feature/story boundaries are;
- **runtime scoping** — how much of an already-valid plan one agent invocation should execute before refreshing context.

Not every context issue requires inventing a new semantic work unit.

Spec Kit also has a post-implementation speckit-converge stage in its recommended workflow, preserving the principle that completing local implementation tasks does not by itself prove whole-feature correctness.

### Spec Kit lesson for PW

PW should use context pressure as a secondary split signal, not as the primary definition of a Card.

If a Card is semantically coherent but implementation would exceed a reliable worker context, Execution Prep may need to split it — but only along a meaningful internal seam. Conversely, simply needing multiple implementation invocations does not necessarily mean there should be multiple Cards if no independent acceptance/review boundary exists.

---

## 5. BMAD: strongest counterexample to naive surface splitting

BMAD's current bmad-build scope standard is the most important challenge to the raw proposed rule.

It says a specification should target one single user-facing goal. A single goal may be one cohesive feature even if it spans multiple layers or files. It defines “multi-goal” as two or more top-level independent shippable deliverables, each capable of being reviewed, tested, and merged as a separate PR without breaking the others. It explicitly warns not to count surface verbs, conjunctions, or noun phrases as separate goals and not to split cross-layer implementation details within one user goal.

The current build template reinforces this. It says cohesive cross-layer stories such as DB + backend + UI stay in one file. At the lower implementation-task level, it prefers roughly one task per file but says tightly coupled changes should be grouped when splitting would be artificial.

This gives BMAD two different decomposition altitudes:

- story/spec boundary = meaningful cohesive delivery outcome;
- internal task boundary = actionable implementation step.

Its preview ticketing route also shows JIT refinement. Epic inception plans the whole epic into story/bug entries with deliverable, prerequisites, verification, uncertainty, and order. Detailed acceptance is intentionally deferred until a story is pulled/built. When completed work changes the picture, the remaining breakdown is revisited rather than pretending the original decomposition is immutable.

BMAD's review lifecycle also distinguishes local from aggregate review. Sprint guidance recommends code review in a fresh context/different LLM after a story reaches review. Its retrospective workflow performs aggregate views and diff-scope review over the epic, specifically weighting boundaries between stories where no single implementation session saw both sides.

### BMAD lesson for PW

The sentence:

> If one part could reasonably pass independent review while another fails, they should normally be separate tasks/Cards.

is too broad if “part” or “surface” means any technical layer.

A frontend surface and backend surface can receive different local defects while still jointly constituting one inseparable behavioral contract. If neither is useful or valid without the other, separate Cards may add handoff cost without creating durable independent acceptance value.

The stronger form is:

**If two portions form separable acceptance, contract, invariant, or independently useful delivery outcomes, and a reviewer can reasonably issue independent verdicts such that GREEN on one remains valid while the other is RED, those portions should normally be separate Cards.**

This preserves the Superpowers insight without turning every vertical feature into DB/API/UI micro-Cards.

---

## 6. GSD: context budget and dependency topology as first-class constraints

GSD contributes a different and valuable approach: the fresh-context unit is a PLAN, not every small task.

Its planner currently:

- decomposes phases into plans;
- builds dependency graphs and execution waves;
- uses file overlap as a concrete constraint on same-wave parallelism;
- requires each plan to have a single concern;
- targets 2–3 tasks per plan;
- targets roughly 50% of an executor context;
- runs goal-backward derivation of observable truths, required artifacts, wiring, and critical links;
- checks that each plan fits the context budget and splits if necessary.

The phase executor treats same-wave file overlap as a planning defect and serializes conflicting plans. Each plan is dispatched to an executor with a fresh context. The user guide explicitly says that when execution fails or produces stubs, one possible cause is an over-ambitious plan; if tasks are too large for one reliable context window, re-plan with smaller scope.

### GSD lesson for PW

GSD is strong evidence that context capacity is not merely an implementation convenience; it can be a real reliability boundary.

But GSD's numeric “2–3 tasks” and “~50% context” targets should not be copied into PW as generic policy. They are harness/model/runtime heuristics and can age quickly.

PW should import the semantic rule instead:

**A Card must be reliably executable within one bounded Worker ownership assignment. If execution evidence shows it is not, this is legitimate evidence for re-decomposition — but the resulting split must still follow meaningful semantic seams.**

GSD also supports the idea that dependency and write-scope topology should influence decomposition and concurrency, which aligns closely with existing PWv2.1 parallel-Card requirements.

---

## 7. OpenSpec: verification-rich tasks without per-task review ceremony

OpenSpec provides the clearest counterexample to the assumption that every independently verifiable task deserves its own independently reviewed agent boundary.

Its current default spec-driven schema instructs task authors to:

- group related tasks under headings;
- make each task trackable;
- keep tasks small enough to complete in one session;
- order tasks by dependency;
- state how each task is verified by a test, command, observable behavior, or delivered artifact;
- keep the tests/documentation called for by a group's work with that group instead of deferring everything to a final catch-up group.

However, OpenSpec does not attach a fresh implementation subagent or independent reviewer to every checklist task. A change is the higher-level unit, and the verify workflow checks the implementation against the change artifacts across three dimensions: completeness, correctness, and coherence.

OpenSpec's overview also emphasizes that proposal/spec/design/tasks are “enablers, not gates.” If implementation reveals that the design is wrong or scope should shrink, artifacts can be revised. This makes decomposition iterative rather than frozen.

### OpenSpec lesson for PW

Independent verification is necessary for a good Card but cannot be sufficient, because a PW Card has much higher lifecycle cost than an OpenSpec task.

A unit that is testable but trivial, preparatory, or meaningful only as part of another outcome should usually remain an internal implementation step rather than become its own Card.

This is strong evidence for an anti-over-decomposition clause in PW's right-sizing semantics.

---

## 8. Task Master: adaptive complexity expansion

Task Master does not provide as strong a semantic definition as Superpowers/BMAD, but it materially adds the idea of adaptive expansion.

Its tooling can analyze task complexity, produce a complexity report, flag complex tasks, and expand them into subtasks. The expansion command explicitly analyzes task complexity and components to create more manageable subtasks.

This supports a general pattern seen elsewhere:

**Initial planning need not perfectly predict final execution topology.**

A workflow can establish meaningful high-level boundaries during planning, then use later evidence to split a unit that proves too complex.

For PW, this supports JIT and execution-time re-decomposition, but complexity scores themselves should not become canonical Card semantics.

---

## 9. Dimension-by-dimension findings

### 9.1 Independent implementability

Independent implementability is a strong split signal, but not a complete rule.

A candidate boundary is stronger when each side can be implemented without simultaneously mutating the other side. This matters for:

- isolated Worker ownership;
- independent result identity;
- potential parallelism;
- preservation of valid work after sibling failure.

Superpowers expects tasks to be mostly independent for SDD. Spec Kit maps tasks and user stories through dependencies. GSD explicitly builds dependency waves. BMAD defines independent shippable goals partly by whether they could become separate PRs without breaking one another.

But a unit can be independently implementable in a technical sense and still be too trivial to deserve its own Card. A config file may be independently editable; that does not mean it should become a separate execution/review lifecycle.

Therefore independent implementability is **necessary evidence**, not sufficient authority.

### 9.2 Independent testability / falsifiability

This is one of the strongest cross-workflow principles.

- Superpowers: every Task ends with an independently testable deliverable.
- Spec Kit: each user story has independent test criteria and must be independently testable.
- OpenSpec: every task states how completion is verified.
- GSD: plans derive observable truths/must-haves and are verification-oriented.
- BMAD: independent shippable goals are separately testable.

For PW, “falsifiable/verifiable” is preferable to “testable” because Cards may contain docs, migration, workflow semantics, or other work that is not best represented by automated tests.

The key question is not “Can I write any test for this fragment?” It is:

**Can this fragment produce an acceptance result that remains meaningful on its own?**

### 9.3 Independent reviewability

Superpowers makes independent reviewability a direct task-boundary rule. BMAD uses separate reviewability as part of defining multiple independent deliverables. PW already requires every Card to receive independent review, making this dimension especially important.

For PW, the best right-sizing test is not merely whether a reviewer can find different defects in different files. It is whether the reviewer can issue **separable acceptance verdicts**.

A useful diagnostic:

- If portion A is GREEN and portion B is RED, can A's GREEN remain valid, durable, and useful as predecessor evidence?
- Or would B's failure necessarily invalidate A because they jointly constitute one inseparable outcome?

If A's acceptance survives B's failure, that is powerful evidence that A and B are separate Card candidates.

### 9.4 Independently useful deliverable boundaries

The systems generally favor units that create something meaningful:

- a user story;
- a capability;
- a coherent feature;
- a single-concern plan;
- an independently testable deliverable.

This does not require every Card to be end-user visible. A contract, schema, migration primitive, test harness, or platform capability can be independently useful if downstream work can consume it as a stable accepted predecessor.

The stronger formulation for PW is therefore **independently useful or independently consumable**, not merely independently shippable to an end user.

### 9.5 Invariants and contracts

PW's existing invariant-family dimension is stronger than many external systems and should be retained.

A Card spanning several unrelated invariant families is risky because:

- tests and reviewers must reason about multiple failure classes;
- repair of one family can perturb another;
- repeated review findings may arrive incrementally by family;
- one Card Review begins to behave like an integration review.

Superpowers' interface blocks and task contracts, Spec Kit contract-to-story mapping, BMAD architecture spine/shared decisions, and OpenSpec behavioral specs all reinforce the importance of contract ownership.

A strong Card boundary often aligns with one coherent contract/invariant family or a tightly coupled set that only makes sense atomically.

### 9.6 Dependency boundaries

Dependencies influence both ordering and appropriate task granularity.

A boundary is stronger when:

- downstream work can consume a stable output of the earlier Card;
- one unit blocks another through a clear contract;
- completed predecessor evidence can remain valid independently.

Conversely, if two fragments constantly mutate the same state and neither can reach a valid intermediate state, the dependency may be evidence for one atomic Card rather than two Cards.

GSD and Spec Kit are particularly explicit about dependency graphs. PW's existing dependency semantics should remain a central part of the split decision.

### 9.7 File/module boundaries

The research does **not** support file/module count as a primary Card rule.

GSD uses file overlap mainly for scheduling safety. BMAD's lower-level task template may prefer one task per file, but the story boundary explicitly ignores file/layer count when the user-facing goal is cohesive. Superpowers says split by responsibility rather than technical layer.

For PW:

- many files can legitimately belong to one Card;
- one file can contain several Card-worthy semantic outcomes;
- file count is a risk/context indicator, not a semantic authority.

### 9.8 Context/task size

Context pressure is real.

Spec Kit explicitly documents context-window exhaustion as a cause of agents losing plan fidelity and hallucinating. GSD explicitly budgets context and tells users to re-plan over-ambitious work.

This supports a secondary PW invariant:

**A Card should be bounded enough for one Worker assignment to execute reliably without uncontrolled context degradation.**

But the research does not support generic PW maximums such as maximum LOC, files, tokens, or minutes. GSD's numbers are implementation heuristics; BMAD's token range concerns its spec artifact, not a universal Card size law.

PW should remain semantic and risk-based.

### 9.9 Risk

Risk can justify more conservative decomposition even where raw separability is ambiguous.

Risk factors include:

- security-sensitive behavior;
- migrations;
- destructive or irreversible state changes;
- concurrency;
- protocol or schema compatibility;
- multiple independently falsifiable invariant families;
- broad cross-system effects;
- high repair blast radius;
- large context burden.

PW already has a risk-based topology challenge. The research supports keeping that challenge as a second layer rather than applying heavyweight review to every trivial topology.

Risk should not be used to create arbitrary microtasks. It should increase the pressure to find real semantic seams and to challenge suspiciously broad Cards.

---

## 10. The proposed reviewer-separation rule

Candidate rule under review:

> If one part could reasonably pass independent review while another fails, they should normally be separate tasks/Cards.

### Evidence supporting the rule

Superpowers nearly states this directly: split where a reviewer could meaningfully reject one task while approving its neighbor.

This is particularly compelling for PW because every Card already incurs mandatory independent review. If a single Card contains several outcomes that naturally admit separate verdicts, one Card identity forces unrelated accepted and rejected work into the same RED/GREEN lifecycle.

That causes:

- unnecessary re-review of already-correct surfaces;
- larger repair blast radius;
- inability to preserve a valid result independently;
- repeated large-context reviewer work;
- hidden opportunities for parallel execution;
- blurred Card-vs-Milestone review responsibilities.

### Evidence against applying the rule literally

BMAD shows why “part” cannot mean arbitrary technical surface.

A cohesive vertical feature may involve:

- data model;
- backend behavior;
- API;
- UI;
- tests.

A reviewer can imagine defects in one layer and not another, but that does not imply five independent deliverables. The feature may have one acceptance contract and no valid or useful intermediate state.

OpenSpec also shows that individually verifiable checklist items do not automatically deserve independent review identities.

### Recommended formulation

The research-supported form is:

> If a proposed Card contains two or more **separable acceptance, contract, invariant, or independently useful delivery outcomes**, and each can reach a valid independently verifiable state such that a reviewer could reasonably GREEN one while REDing another, they should normally be separate Cards.

Add the explicit exception:

> This presumption does not apply when the portions jointly realize one atomic outcome, separation creates an invalid or non-verifiable intermediate state, acceptance is materially inseparable, or concrete coupling makes separate implementation/review artificial.

And the explicit anti-shortcut clause:

> Different files, modules, layers, tests, commands, or implementation steps alone do not establish separate Cards.

This preserves the powerful reviewer-separation heuristic without creating horizontal micro-Cards.

---

## 11. Fresh implementation contexts and review semantics by workflow

### Superpowers

Fresh implementer per Task under SDD. Task review after every Task. Broad final review after all tasks.

This is the strongest “one meaningful unit = one fresh implementation context + one review gate” model in the sample.

### Spec Kit

Fresh contexts are optional and runtime-dependent. It can delegate parallel tasks to subagents, but it can also simply run bounded sets of tasks over repeated implementation invocations. The semantic user-story boundary is separate from the runtime context-refresh mechanism.

No universal mandatory independent review exists for every task. Final convergence provides broader feature-level checking.

### BMAD

Story/build sessions are the meaningful boundary. Sprint guidance explicitly recommends fresh-context code review with a different LLM. Internal file/action tasks are not each independently reviewed.

Epic retrospective performs broader aggregate review over cross-story seams.

### GSD

A PLAN is the fresh executor-context unit. It normally contains multiple tasks. The planner deliberately sizes the PLAN to one concern and a context budget.

This is strong evidence that “fresh context” should attach to the review-worthy ownership unit, not automatically to the smallest task step.

### OpenSpec

Core workflow does not require fresh contexts or per-task independent reviewers. Verification happens at the whole-change level.

### PW implication

Because a PW Card already has:

- exactly one primary mutating Worker;
- its own result;
- independent Card Review;
- downstream dependency identity;

the Card should be compared to Superpowers Task / GSD Plan / BMAD Story, not to OpenSpec checklist task or Superpowers 2–5 minute step.

---

## 12. Higher-level review after task completion

The reviewed systems repeatedly preserve a broader level of validation after local work:

- Superpowers: broad whole-branch final review.
- Spec Kit: speckit-converge after implement.
- BMAD: epic retrospective and diff-scope/aggregate views.
- GSD: phase verification/UAT.
- OpenSpec: whole-change verify.

This validates PWv2.1's layered architecture:

**Card Review should own bounded local correctness. Milestone Review should own composition/integration acceptance.**

A Card is too broad when its review begins to substitute for the integration role that belongs to the milestone.

This directly supports current PWV21-REQ-121 and should remain part of the right-sizing decision.

---

## 13. Failure modes of under-decomposition: Cards that are too large

The external research and PW's own M02 evidence align closely.

### 13.1 Context degradation

Spec Kit and GSD explicitly identify oversized implementation runs as reliability risks. The agent can lose the plan, ignore tasks, hallucinate, produce stubs, or degrade around context compaction.

### 13.2 All-or-nothing result identity

When several separable outcomes share one Card, a defect in one area prevents the whole Card from becoming a stable GREEN predecessor even if other areas are correct.

### 13.3 Re-review amplification

One large Card causes the reviewer to repeatedly reload and re-evaluate a broad subject after every local repair.

### 13.4 Incremental finding discovery across unrelated surfaces

A reviewer may find one defect class per pass because the subject is broad. This can create long RED → fix → re-review sequences even when the underlying issue is decomposition topology rather than uniquely poor implementation.

### 13.5 Repair blast radius

A fix to one part can introduce a bug in another part of the same broad Card, forcing more whole-subject review.

### 13.6 Lost parallelism

Independent work hidden inside one mutating Card cannot be assigned to independent Workers even when write scopes and dependencies would permit it.

### 13.7 Card Review collapses toward Milestone Review

A mega-Card forces Card Review to reason across integration seams that should instead be reviewed at Milestone level.

### 13.8 Weak failure localization

A RED verdict identifies the entire Card as non-accepted even if only one semantic family is defective, reducing the value of durable evidence.

### PW M02 evidence

Current PWv2.1 workstream evidence is particularly relevant.

The Task Board records M02-T01 with review attempts R01 through R12. The accepted decomposition ADR states that Strategic Planning had identified four independently falsifiable implementation surfaces while Execution Prep collapsed them into one whole-milestone Card, materially increasing implementation and review surface.

Current PW sources:

- Task Board:
  https://github.com/elmakus/chatgpt-codex-project-workflow/blob/work/pwv21-policy-kernel-brainstorming/implementation/workstreams/change-pwv21-policy-kernel-brainstorming/TASK_BOARD.toml
- M02 Card:
  https://github.com/elmakus/chatgpt-codex-project-workflow/blob/work/pwv21-policy-kernel-brainstorming/implementation/workstreams/change-pwv21-policy-kernel-brainstorming/cards/M02-T01.md
- decomposition ADR:
  https://github.com/elmakus/chatgpt-codex-project-workflow/blob/work/pwv21-policy-kernel-brainstorming/decisions/ADR_PWV21_DECOMPOSITION_FIDELITY.md
- convergence evidence:
  https://github.com/elmakus/chatgpt-codex-project-workflow/blob/work/pwv21-policy-kernel-brainstorming/implementation/workstreams/change-pwv21-policy-kernel-brainstorming/evidence/M02-T01_CONVERGENCE_ANALYSIS_2026-09-24.md

This is empirical support for stronger generic right-sizing semantics, not by itself authority to change them.

---

## 14. Failure modes of over-decomposition: tasks/Cards that are too small

The research also strongly rejects “smaller is always safer.”

### 14.1 Dispatch and review overhead dominates

Superpowers explicitly revised its guidance because trivial Tasks caused full dispatch + review cycles with little value.

### 14.2 Repeated context reconstruction

Fresh Worker and Reviewer contexts repeatedly reload the same surrounding code/spec information.

### 14.3 Meaningless intermediate states

A Card that only adds scaffolding, a config knob, or a helper no one can yet use may not create a meaningful acceptance result.

### 14.4 Artificial horizontal slices

Separating DB, API, and UI solely by technical layer can destroy the vertical behavior contract and move correctness questions into integration.

### 14.5 Dependency explosion

Too many micro-Cards create more edges, more handoffs, more stale-result opportunities, and more orchestration complexity.

### 14.6 Review ceremony without independent judgment value

If every Card would inevitably receive the same verdict because none is meaningful without its neighbors, separate independent reviews add ceremony rather than evidence.

### 14.7 Integration burden shifts upward

Milestone Review becomes responsible for proving that many individually GREEN fragments form one feature, when a coherent Card could have validated the full behavior locally.

### Anti-over-decomposition principle

A PW Card should be the **smallest meaningful** review-worthy unit, not the smallest technically separable mutation.

Setup, scaffolding, configuration, and documentation should normally ride with the outcome that needs them unless they are independently consumed prerequisites.

---

## 15. Planning, JIT decomposition, and execution-time discovery

The researched systems favor a layered model rather than one-time decomposition.

### Strategic Planning

Strategic Planning should identify meaningful known seams and their strategic importance without pretending it knows exact future Card IDs.

PWv2.1's required_seam / preferred_seam / illustrative model is well aligned with this.

### Execution Prep / JIT

JIT is the natural owner of exact Card materialization because it has:

- real predecessor results;
- current repository paths;
- concrete coupling;
- actual contracts;
- current write scopes;
- changed implementation knowledge.

Execution Prep should be allowed to split further when current evidence justifies it.

It should not silently erase stronger Planning boundaries.

### During execution

The research supports recognizing “Card discovered oversized” as a legitimate execution finding.

Examples:

- the Worker identifies two independent deliverables hidden in the Card;
- a blocker affects only one separable invariant family;
- the Card cannot be completed reliably within one bounded context;
- completed portions could form stable independently reviewable predecessor evidence;
- repeated review findings partition consistently along distinct semantic surfaces.

The Worker should not silently redefine or split its own authority.

At the smallest safe durable boundary, unaccepted remaining scope should return to Execution Prep for bounded re-decomposition.

This is consistent with:

- Superpowers splitting a task that proves too large/broken;
- GSD re-planning over-ambitious execution;
- BMAD revisiting remaining breakdown after completed work teaches the team;
- OpenSpec allowing plan artifacts to evolve;
- Task Master adaptively expanding complex tasks.

---

## 16. Can later execution merge planner-identified boundaries?

The research provides little support for an executor silently merging meaningful planner boundaries.

For PWv2.1, the current ownership model is sound:

- required_seam: Execution Prep must not merge; evidence that the seam is wrong returns to Strategic Planning;
- preferred_seam: preserve by default; deviation needs durable concrete rationale;
- illustrative: JIT may refine freely;
- launched Card boundaries: Worker may not merge sibling Cards or broaden itself into neighboring scope.

Execution can discover evidence that a boundary is wrong. That evidence belongs to the topology owner; it is not self-authorizing topology mutation.

The same principle should apply in reverse: execution can discover that its own Card is too large, but the remaining work returns to Execution Prep rather than the Worker inventing new canonical Card authority.

---

## 17. Numeric limits: useful heuristics, poor generic policy

The research found numeric guidance, but not enough support for generic PW hard limits.

Examples:

- Superpowers: 2–5 minute **steps**, explicitly not its Task boundary.
- BMAD: target token range for a build spec and a warning for oversized specs.
- GSD: 2–3 tasks per PLAN and roughly 50% context target.
- OpenSpec: “small enough to complete in one session.”

These numbers solve local harness/model problems. They are not stable universal definitions of semantic work units.

PWv2.1 should not add fixed generic maxima for:

- LOC;
- files;
- tokens;
- number of tests;
- wall-clock minutes.

Such metrics can be telemetry or topology-risk evidence. They should not outrank semantic seams, contracts, atomicity, and review independence.

---

## 18. Assessment of current PWv2.1 decomposition semantics

Current R2 authority already contains strong decomposition machinery.

Relevant current requirements include:

- PWV21-REQ-115: Strategic Planning can classify required_seam / preferred_seam / illustrative.
- PWV21-REQ-116: Execution Prep cannot merge required seams.
- PWV21-REQ-117: preferred seam deviation requires concrete durable coupling/atomicity/non-separable-acceptance/predecessor rationale.
- PWV21-REQ-118: decomposition audit covers independent implementability, testability/falsifiability, reviewability, invariant/contract family, dependency ordering, atomic mutation/migration constraints, and cross-surface coupling.
- PWV21-REQ-119: materially risky topology gets fresh independent topology challenge.
- PWV21-REQ-120: topology challenge remains narrower than Plan Review and is not mandatory ceremony for trivial work.
- PWV21-REQ-121: Card topology must preserve layered review architecture so Card Review does not silently substitute for Milestone integration review.

Current authority source:

https://github.com/elmakus/chatgpt-codex-project-workflow/blob/work/pwv21-policy-kernel-brainstorming/requirements/PWV21_POLICY_KERNEL.md

Current decomposition ADR:

https://github.com/elmakus/chatgpt-codex-project-workflow/blob/work/pwv21-policy-kernel-brainstorming/decisions/ADR_PWV21_DECOMPOSITION_FIDELITY.md

### Finding: materially incomplete, not fundamentally deficient

The current rules are strong on **dimensions** but weaker on the **decision function**.

REQ-118 tells Execution Prep what to inspect. It does not clearly state when the combination of those observations makes a split presumptively mandatory.

A broad candidate Card could technically be:

- implementable as a whole;
- testable as a whole;
- reviewable as a whole;
- not blocked by atomicity;

while still containing several independently falsifiable, review-worthy outcomes whose GREEN results could have been preserved separately.

REQ-119 may catch the problem later through a topology challenge, but that puts the key right-sizing decision into the reviewer challenge rather than first-class Card semantics.

Therefore the current PWv2.1 decomposition rules are **materially incomplete** with respect to generic Card right-sizing.

The missing piece is a semantic tie-breaker that states what a Card is and when independent acceptance/review evidence creates a split presumption.

---

## 19. Strongest common patterns

The strongest common patterns found are:

1. **Behavior/deliverable before file count.** Meaningful outcome, user story, capability, concern, contract, or independently consumable result outranks technical layer boundaries.

2. **Every implementation unit needs a verification boundary.** Test, falsification, observable result, command, artifact, or explicit acceptance evidence.

3. **Dependency graphs matter.** Upstream/downstream contracts and ordering are first-class inputs to decomposition.

4. **Fresh context belongs at a meaningful ownership unit.** Superpowers Task, GSD Plan, BMAD Story — not every trivial step.

5. **Local completion does not replace aggregate review.** Mature systems preserve whole-feature/phase/change review or convergence.

6. **Context size is a reliability factor but not the semantic definition.** Scope runtime work first; create new semantic units only when a real seam exists.

7. **Decomposition is revisable.** Planning can establish intent; JIT refines it; execution can surface evidence for re-decomposition.

8. **Over-decomposition is a real failure mode.** Mature systems deliberately fold tightly coupled setup and cross-layer implementation into the meaningful outcome that needs them.

9. **Independent acceptance preservation is a powerful seam test.** If GREEN on A can remain valid while B is RED, separate identity is often useful.

10. **Atomicity and invalid intermediate state rebut otherwise plausible splits.**

---

## 20. Important disagreements and trade-offs

### Per-unit review cost

Superpowers chooses expensive per-Task independent review.

OpenSpec chooses lighter checklist tasks with whole-change verification.

PW has already chosen mandatory Card Review, so PW Cards should be closer to Superpowers review-worthy Tasks than OpenSpec checklist entries.

### Vertical cohesion vs maximal separation

Superpowers' reviewer-separation language encourages split boundaries.

BMAD strongly protects cohesive vertical stories.

PW should combine both: independent verdicts are a split presumption only when they correspond to independently meaningful acceptance/contract/invariant outcomes.

### Context budgeting

GSD treats explicit context budget as a planning rule.

Spec Kit treats it as an execution-scoping problem before escalating to new specs.

PW should use context as a risk/reliability signal, not a universal numeric law.

### Up-front vs JIT decomposition

Spec Kit task generation is comparatively up-front, though execution can be scoped.

BMAD and OpenSpec are more explicitly iterative.

PW's Strategic Planning + JIT Execution Prep split is well supported: preserve meaningful strategic seams early, decide exact Card topology late.

---

## 21. Research recommendations for PWv2.1

**The following wording is research-only. It is not accepted authority and MUST NOT be treated as requirements or ADR content unless separately promoted through the normal PW lifecycle.**

### Candidate research requirement — Card semantic right-sizing

> **RESEARCH RECOMMENDATION ONLY — Card semantic right-sizing**
>
> Execution Prep SHOULD materialize each Card as one coherent, independently falsifiable implementation outcome that is meaningful enough to justify its own Card-level execution, result, and independent review lifecycle. A candidate Card that contains two or more separable acceptance, contract, invariant, or independently useful delivery outcomes SHOULD normally be split when each can reach a valid independently verifiable state and a reviewer could reasonably GREEN one while REDing another. File, module, layer, tool, or implementation-step boundaries alone SHOULD NOT require a split.

If promoted, MUST/SHOULD strength should be decided by the owning Definition/ADR process; this report does not set normative requirement strength.

### Candidate research requirement — Card cohesion / anti-microtask guard

> **RESEARCH RECOMMENDATION ONLY — Card cohesion**
>
> Execution Prep SHOULD NOT split work solely to minimize implementation size. Tightly coupled changes SHOULD remain one Card when they jointly realize one behavioral or contract outcome, separation would create an invalid or non-verifiable intermediate state, acceptance is materially inseparable, or a resulting Card would consist only of setup/scaffolding/configuration/documentation with no independent acceptance value. Concrete dependency, atomicity, and coupling evidence SHOULD outrank mechanical file/layer separation.

### Candidate research requirement — late oversize discovery

> **RESEARCH RECOMMENDATION ONLY — Late oversize discovery**
>
> When implementation or review produces material evidence that the current Card contains multiple separable review-worthy outcomes or cannot be completed reliably within one bounded Worker assignment, the Card SHOULD NOT silently expand or redefine its scope. At the smallest safe durable boundary, unaccepted remaining scope SHOULD return to Execution Prep for bounded re-decomposition. Accepted planner seams and already-valid predecessor evidence remain authoritative unless revised by their owning workflow stage.

### Candidate research ADR wording

> **RESEARCH RECOMMENDATION ONLY — Card boundaries represent review-worthy semantic outcomes**
>
> PW treats a Card as an execution-and-review ownership boundary, not as a generic checklist item or file-change bundle.
>
> Execution Prep prefers the smallest meaningful Card that preserves one coherent acceptance/contract/invariant outcome and supports one bounded independent Card-review verdict.
>
> A split is presumptively required when a proposed Card contains multiple separable outcomes for which:
>
> 1. each can reach a valid independently verifiable state;
> 2. GREEN on one can remain valid while another is RED;
> 3. each is substantial enough to justify independent execution/result/review identity.
>
> The presumption is rebutted by concrete atomicity, invalid-intermediate-state, inseparable-acceptance, or material-coupling evidence. Different files, modules, architectural layers, tests, or implementation steps are not by themselves separate Cards.
>
> Setup, scaffolding, configuration, and documentation normally fold into the Card whose deliverable requires them unless they form an independently consumed prerequisite.
>
> Strategic Planning owns required_seam and preferred_seam intent; Execution Prep owns exact JIT Card topology within that authority. Execution may report topology evidence but may not silently merge, broaden, or redefine Card boundaries.
>
> When execution reveals an oversized Card, remaining unaccepted scope returns to Execution Prep for bounded re-decomposition at a safe durable boundary.
>
> Card Review remains local to one semantic outcome; Milestone Review remains responsible for composition and integration across Card outcomes.

Again: this is proposed wording captured as research evidence only. It does not amend the current ADR set.

---

## 22. Recommended semantic decision procedure

A practical semantic procedure, if later adopted, would be:

### Step A — preserve accepted Planning topology

- required_seam: never merge in JIT;
- preferred_seam: preserve by default; deviation requires concrete accepted rationale;
- illustrative: refine freely.

### Step B — identify meaningful acceptance units

Ask which portions correspond to distinct:

- acceptance outcomes;
- contracts;
- invariant families;
- independently useful/consumable deliverables.

Do not start from file or layer count.

### Step C — test independent validity

For each candidate split, ask:

- Can each side reach a valid intermediate state?
- Can each side be verified/falsified independently?
- Can one side's GREEN evidence remain valid if the other side is RED?
- Can downstream work consume either result independently?
- Would separate Worker ownership reduce interference rather than add artificial handoff?

### Step D — apply cohesion exceptions

Keep together when:

- mutation/migration must be atomic;
- one side without the other is invalid or non-verifiable;
- acceptance is truly inseparable;
- shared mutable state/coupling makes separate ownership artificial;
- one side would only be setup/scaffolding for the other.

### Step E — apply risk/context pressure

If still coherent but materially broad, inspect:

- context burden;
- number of invariant families;
- repair blast radius;
- destructive/security/migration risk;
- concurrency/write-scope complexity;
- review breadth.

Risk may justify further splitting only where a real semantic seam exists.

### Step F — challenge suspicious topology

Use the existing fresh topology challenge when the resulting Card topology remains materially risky.

This keeps the challenge as a second-order safeguard rather than a substitute for a missing primary rule.

---

## 23. Final conclusion

The researched systems do not support a generic policy of “one file/module/layer per task,” nor do they support hard universal LOC/token/file ceilings.

They converge instead on a semantic unit shaped by:

- coherent outcome;
- independent verification/falsification;
- dependency topology;
- contract/invariant ownership;
- bounded context;
- meaningful acceptance;
- preservation of valid results;
- review cost.

The proposed rule:

> If one part could reasonably pass independent review while another fails, they should normally be separate tasks/Cards.

captures a real and important seam test, especially for PW because each Card already receives an independent review. But it should not be applied to arbitrary technical surfaces.

The research-supported version is:

> **If a proposed Card contains two or more separable acceptance, contract, invariant, or independently useful delivery outcomes, and each can reach a valid independently verifiable state such that a reviewer could reasonably GREEN one while REDing another, those outcomes should normally be separate Cards. Keep them together only when concrete atomicity, invalid-intermediate-state, inseparable-acceptance, or material-coupling evidence makes separation artificial.**

Under that rule, the historical M02-style mega-Card topology would require explicit non-separability/atomicity evidence rather than being allowed merely because all work belongs to one milestone. At the same time, a cohesive vertical DB→backend→UI feature remains legal as one Card when those layers jointly realize one inseparable acceptance outcome.

Therefore:

**PWv2.1's current decomposition semantics are strong but materially incomplete. A generic semantic Card right-sizing invariant is justified, provided it includes both a reviewer-separation split presumption and an explicit anti-over-decomposition/cohesion exception.**

No recommendation in this report is accepted authority. Promotion, if any, belongs to the normal Project Workflow Definition/ADR/Planning lifecycle.
