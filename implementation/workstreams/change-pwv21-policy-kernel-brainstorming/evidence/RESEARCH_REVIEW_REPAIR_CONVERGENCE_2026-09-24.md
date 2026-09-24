# Research — Review/Repair Convergence in Agentic Software-Development Workflows

Date: 2026-09-24  
Status: research evidence only  
Repository: elmakus/chatgpt-codex-project-workflow  
Branch researched: work/pwv21-policy-kernel-brainstorming  
Primary question: What review/repair lifecycle best converges toward correctness when an implementation repeatedly receives findings?

> This document is evidence and analysis only. It does not modify, supersede, approve, or promote Project Workflow authority. Candidate requirement/ADR wording near the end is explicitly a research recommendation, not accepted authority.

## 1. Executive conclusion

The strongest current evidence supports a hybrid review lifecycle:

**initial exhaustive fresh review  
→ freeze the complete material finding set discovered by that pass  
→ class/root-cause repair, including sibling and negative-space cases  
→ bounded scoped verification of the known findings plus the fix's causal blast radius  
→ only after known findings close, one fresh full-scope review  
→ repeat the discovery/closure cycle only when that fresh review finds genuinely new material defect classes.**

The research does not support removing fresh full-scope review. Fresh review is valuable as a de-anchored discovery gate. The problem is using fresh full review as the normal inner-loop mechanism for proving that already-known defects were repaired.

The current PWv2.1 design is therefore best characterized as **strong on correctness and independence, but probably too expensive in the ordinary RED → repair → re-review loop**. It is not too weak. Its exhaustive review rule, class-level repair requirement, stable review epoch, bounded convergence mode switch, layered Card/Milestone/Final review, and post-convergence validation are stronger than most compared systems. The likely overpayment is that the present 5/4/3 hard ceilings count qualifying fresh full-scope reviews, encouraging repeated broad stochastic rediscovery where a narrower closure check would usually suffice.

Superpowers is the clearest directly relevant redesign. Its July 2026 SDD fix-loop specification states that repeated fresh full reviews were the churn engine: a nondeterministic reviewer kept exposing a new frontier of findings instead of verifying the fixes. It therefore changed ordinary re-review to a scoped verification of the original findings and fix diff, kept a five-round circuit breaker, retained the original implementer for early repair rounds, introduced a fresh implementer only after repeated failure, and kept a broad whole-branch review as the final safety net.

BMAD independently supplies evidence that broad repeated adversarial passes can self-perpetuate. Its issue history contains real runs where review-generated patches themselves justified additional review and later passes increasingly found marginal or self-created problems. bmad-loop now uses both a review-cycle cap and a separate follow-up damping limit.

The main caution against copying Superpowers literally is also documented by Superpowers itself: open issue #2266 reports fixes that satisfied the named finding but broke unchanged consumers. Its existing scoped prompt was too diff-centric. The safer hybrid scope is therefore:

**known finding + repair diff + causal blast radius**, not simply “changed lines only.”

The strongest proposed accounting unit for PWv2.1 is **material defect-class discovery epochs**, with a separate small repair/closure budget for a repeatedly failing known class. The existing 5/4/3 numbers can remain provisional until PW gathers more execution data, but they should not count every ordinary fix verification.

## 2. Research method and evidence hierarchy

This review used current official repositories/documentation where available and distinguished normative/current product documentation from issue-reported empirical failures.

Evidence priority:

1. Current official workflow/skill documentation and current accepted PWv2.1 authority.
2. Current official repository design specifications describing intentional lifecycle semantics.
3. Current official repository issue reports containing concrete measured failures. These are empirical evidence, not normative design authority unless corroborated by current docs.
4. Research inference, explicitly identified as such.

Research retrieval date: 2026-09-24.

The PWv2.1 baseline was read directly from the active branch before writing this report:

- requirements/PWV21_POLICY_KERNEL.md
  - blob SHA at research time: 6f2fd5ace3ef20c708c995115f56efd9de009a33
- decisions/ADR_PWV21_REVIEW_LIFECYCLE.md
  - blob SHA at research time: 60f95d9a578b10e367a066599d4a89f02b60717b
- branch head before this evidence commit:
  - 27f83ff3a55c857eb18d42ffec0ab296f02abbbb

## 3. Source catalogue

### Superpowers

Official current sources:

- SDD fix-loop redesign design:
  https://github.com/obra/superpowers/blob/main/docs/superpowers/specs/2026-07-15-sdd-fix-loop-redesign-design.md
- Current subagent-driven-development skill:
  https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md
- Current initial task-reviewer prompt:
  https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/task-reviewer-prompt.md
- Current scoped re-review prompt:
  https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/re-review-prompt.md
- Open empirical defect report on repair blast radius, issue #2266:
  https://github.com/obra/superpowers/issues/2266

The redesign document explicitly says the old loop was “Repeat until approved,” uncapped, and that each re-review was a fresh full review of the whole diff. It reports that this caused a nondeterministic frontier reviewer to surface new findings every round, and says an earlier strict-cost study found review-loop count to be the biggest source of run-to-run cost variance.

### BMAD Method / bmad-loop

Official/current sources:

- bmad-loop feature documentation:
  https://github.com/bmad-code-org/bmad-loop/blob/main/docs/FEATURES.md
- BMAD Method issue #2576 — structurally non-convergent follow-up review:
  https://github.com/bmad-code-org/BMAD-METHOD/issues/2576
- BMAD Method issue #2772 — measured 733 findings / 21 passes case:
  https://github.com/bmad-code-org/BMAD-METHOD/issues/2772
- BMAD Method issue #2760 — duplicated review layers:
  https://github.com/bmad-code-org/BMAD-METHOD/issues/2760
- BMAD Method repository:
  https://github.com/bmad-code-org/BMAD-METHOD

bmad-loop currently documents fresh-context adversarial review, a default limits.max_review_cycles of 3, and a second limits.max_followup_reviews default of 1 specifically to damp structurally non-convergent “review recommends another review” behavior.

### Get Shit Done (GSD)

Official source:

- Commands documentation:
  https://github.com/gsd-build/get-shit-done/blob/main/docs/COMMANDS.md

The current /gsd-code-review command documents separate reviewer and fixer agents, severity-classified findings, default repair of Critical + Warning findings, optional Info repair with --all, and a --fix --auto review/fix/re-review loop capped at 3 iterations.

### GitHub Spec Kit

Official sources:

- Agentic SDD workflow:
  https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md
- Workflow engine documentation:
  https://github.com/github/spec-kit/blob/main/workflows/README.md

/speckit.converge assesses current implementation against spec, plan, and tasks, appends remaining work as durable tasks, and instructs the user/agent to implement those tasks and run converge again until converged. The converge command itself does not document a dedicated convergence-attempt ceiling. Separately, Spec Kit's generic workflow engine supports bounded while and do-while steps with explicit max_iterations examples.

### OpenSpec

Official sources:

- Workflows:
  https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md
- Verify skill specification:
  https://github.com/Fission-AI/OpenSpec/blob/main/openspec/specs/opsx-verify-skill/spec.md

/opsx:verify checks completeness, correctness, and coherence. The verify spec differentiates CRITICAL, WARNING, and SUGGESTION findings; CRITICAL findings must be fixed before archive, while warnings/suggestions are weaker. Verification is an optional workflow action rather than an independently enforced iterative review state machine.

### Current PWv2.1 proposal

Repository-local accepted authority at research time:

- requirements/PWV21_POLICY_KERNEL.md
- decisions/ADR_PWV21_REVIEW_LIFECYCLE.md

Key current requirements for this research are PWV21-REQ-056 through 076 and PWV21-REQ-108 through 114.

## 4. Comparison table

| Workflow | Initial review shape | Repair owner | Post-fix verification | Reviewer freshness | Finding-set handling | Circuit breaker | After ceiling | Broad final review |
|---|---|---|---|---|---|---|---|---|
| Superpowers SDD | Task-scoped spec + quality review of the task diff. It is broad within the task, but current prompt does not define PW-style “must finish complete acceptance surface after first blocker” in the same explicit terms. | Rounds 1–3 resume original implementer; rounds 4–5 use fresh implementer on a more capable model. | Scoped re-review of original findings plus new breakage in fix diff. Not a fresh task review. | Re-review is separately dispatched; semantic anchoring to known findings is intentional. | Original finding list is carried into every fix round; no early controller adjudication before cap. Minor findings stay out of the loop. | Five fix rounds. | Controller adjudicates residuals. Wrong/contestable or real non-load-bearing findings may be parked; load-bearing structural problems stop/rule through existing control path. | Yes: broad whole-branch review, one fixer with complete findings, one scoped re-review, then adjudication. |
| BMAD Method + bmad-loop | Fresh-context adversarial review with multiple independent review layers. | Review pipeline triages findings and can auto-apply patch-class findings; ownership is less cleanly separated than Superpowers/PW. | Review cycles are fresh-context adversarial passes, bounded by bmad-loop. | Explicitly fresh context between dev and review; multiple parallel lenses. | Triage log persists findings, but repeated passes can discover or manufacture new findings. | max_review_cycles default 3; max_followup_reviews default 1. | Follow-up recommendation is damped/journaled rather than endlessly honored; ordinary budget exhaustion commits/converges rather than generating another process ticket. | No directly equivalent mandatory Card/Milestone/final hierarchy found. |
| GSD | Reviews changed phase source files; severity classified as Critical/Warning/Info. | Dedicated gsd-code-fixer agent. | --fix --auto performs fix + re-review. Docs do not define a separate scoped-known-finding verifier versus fresh full review. | Not normatively specified in reviewed command docs. | REVIEW.md / REVIEW-FIX.md persist findings and repairs. | Three iterations. | Command docs establish cap but do not specify a PW-style root-cause/convergence owner at cap. | Phase-level review; broader verification/UAT mechanisms exist, but no same layered architecture as PW. |
| GitHub Spec Kit | /speckit.converge compares current implementation to spec/plan/tasks. | /speckit.implement executes appended convergence tasks. | Re-run /speckit.converge against current state. | Reviewer identity is not part of the formal contract. | Gaps become durable appended tasks, reducing dependence on prose review history. | No dedicated converge cap documented; generic workflow engine supports explicit max_iterations. | Depends on workflow/controller; generic engine can gate or branch after bounds. | After convergence, normal code review/PR is expected; not a mandatory semantic final-integration reviewer. |
| OpenSpec | /opsx:verify systematically checks completeness, correctness, coherence. | Return to /opsx:apply for implementation or /opsx:update if planning artifacts are wrong. | Re-run verify as desired; no separate known-finding closure mode. | Reviewer identity/freshness not formalized. | Structured report with priority levels. | No hard automatic review-loop cap in default workflow. | Criticals block “ready”; warnings/suggestions can remain. | Verify is whole-change oriented but optional; archive semantics tolerate non-critical findings. |
| Current PWv2.1 | Fresh full-scope review must evaluate complete applicable acceptance surface and record all independently discovered material findings before repair. | Same Card Worker should persist through ordinary repair; replacement within same Card is allowed. | Explicitly distinguishes bounded finding verification from fresh full-scope review. Current hard ceiling counts qualifying fresh full reviews. | Strong subject-relative independence; fresh Card reviewer; fresh Milestone/final reviewer; no prior verdict rationales by default at broader layers. | Complete material finding set frozen before repair; repair targets defect class/root cause plus siblings/negative space. | Card 5, Milestone 4, Final Integration 3 qualifying fresh full-scope reviews per stable epoch. | Main performs convergence/root-cause analysis; one fresh post-convergence validation; another RED routes to broader structural owner. | Yes: separate Card, Milestone and final-integration reviews. |

## 5. Exhaustive initial review versus first-blocker review

### Why first-blocker review is weak for repair convergence

A reviewer that stops after the first blocker creates a serialized “peel the onion” loop:

review → discover A → repair A → review → discover B → repair B → review → discover C.

This converts one broad discovery pass into several latency-dominated cycles and prevents the implementer from seeing related failures as one defect class.

PWv2.1 explicitly rejects that pattern in REQ-109: a fresh full-scope reviewer must finish the applicable acceptance surface and record the complete independently discovered material set before repair.

The external workflows vary:

- **OpenSpec verify** is structurally exhaustive over applicable artifacts: it checks tasks, requirements/scenarios, correctness, and coherence, then produces a prioritized report. It is not designed as a first-failure test.
- **Spec Kit converge** similarly assesses implementation against spec, plan, and tasks and appends all identified remaining work for another implementation pass.
- **GSD code review** produces a severity-classified review artifact over changed source files rather than documenting “stop at first issue.”
- **Superpowers task review** asks for both spec compliance and code quality findings in one report. It is broad within one task, but its current prompt is less explicit than PW about continuing the pass after discovering a blocker.
- **BMAD** deliberately runs multiple adversarial lenses, which favors broad discovery, but BMAD's empirical history also demonstrates that “find more” must not become a quota-driven objective. Issue #2772 reports that a blind-hunter prompt requiring “at least ten issues” contributed to large volumes of low-value findings.

Research conclusion: **the initial discovery pass should be exhaustive over the acceptance surface, but exhaustive means “record all material findings actually supported by evidence,” not “manufacture N findings.”**

## 6. Finding-set freezing

Finding-set freezing is one of the most important convergence mechanisms.

A repair round should know whether it is closing the set discovered by review D0 or whether review D1 has opened a genuinely new defect class. Without that distinction, any newly noticed observation can extend the same loop indefinitely.

PWv2.1 is explicit: the full-scope reviewer completes the acceptance surface and freezes the material set before repair.

Superpowers implements a practical version of the same idea. The fix loop is triggered by spec failure or Critical/Important findings; each re-review receives the **original findings list**, task brief, updated report, and a fix-scoped diff package. The controller is forbidden from early adjudication before the cap except for authority conflict. Minor findings never enter the loop.

Spec Kit achieves another form of freezing by materializing remaining gaps into durable tasks. A subsequent convergence pass evaluates current state and can append new tasks, making the difference between already-known work and newly discovered gaps observable.

BMAD's failure cases show the opposite danger: when every pass can patch low-severity issues and then use those patches as justification for another full pass, the boundary between a finding set and a new review disappears.

Research conclusion: **freeze the material finding set per discovery pass. A scoped closure pass may add only defects causally introduced/exposed by the repair to that open set; unrelated newly noticed observations should be deferred to the next fresh discovery gate.**

## 7. Original implementer versus fresh implementer

### Benefits of the original implementer

The original implementer already holds local task intent, interfaces, test commands, and implementation rationale. Replacing it on the first RED discards useful context and forces another agent to reconstruct the same problem.

Superpowers' current redesign makes this explicit:

- rounds 1–3: resume the original implementer;
- rounds 4–5: fresh implementer, more capable model.

Its design rationale says “ownership beats a drive-by patcher” for ordinary findings, but a loop surviving three resumes usually means the implementer cannot see its own problem. Freshness is introduced only when continuity stops paying.

This strongly supports PWv2.1 REQ-048: the same Worker should persist through ordinary repair loops for the Card, while REQ-049 allows replacement when the Worker struggles without changing Card identity or authority.

### When freshness becomes valuable

Repeated failure of the same class is evidence of implementation anchoring. At that point, a fresh implementer can change perspective while the workflow keeps stable Card/authority identity.

Superpowers combines fresh implementer and stronger model in rounds 4–5. PW should not copy that entire policy because its current accepted authority deliberately separates worker replacement from silent model escalation: stronger/different model use requires explicit authorization. But the **fresh implementer** part remains transferable.

Research conclusion: **continuity first, fresh implementer after repeated non-convergence. Fresh perspective and stronger model should remain separate decisions.**

## 8. Same reviewer versus fresh reviewer

Reviewer freshness and reviewer anchoring are not the same property.

A fresh reviewer can still be intentionally anchored by giving it the prior finding list. Conversely, the same reviewer can be asked to “review everything again,” but its prior mental model may remain strongly anchored.

The best lifecycle uses both modes for different jobs:

### Same/anchored reviewer is useful for closure

For a known finding, the question is intentionally narrow:

- Does the exact defect still exist?
- Did the repair cover its class?
- Did the repair break the causally related surface?

The reviewer who originally found the defect already understands why it failed. Using that same reviewer for a bounded closure check can be efficient, provided it did not materially perform the repair itself.

PWv2.1 already allows this in REQ-061.

### Fresh reviewer is useful for rediscovery

After all known findings close, the question changes:

- What did the previous reviewer miss?
- Is there another independent material defect class?
- Does the current subject satisfy authority when reconstructed without the prior verdict narrative?

That is where a genuinely fresh reviewer provides signal.

PWv2.1 already applies this strongly at Milestone/final boundaries by withholding prior opinions/verdict rationales by default. The research recommends applying the same distinction explicitly within repeated Card discovery cycles: the prior reviewer may close its findings, but the next full-scope discovery pass should be fresh.

## 9. Scoped verification versus fresh full-scope re-review

This is the central trade-off.

### Repeating full review after every fix

Advantages:

- maximal opportunity to discover defects omitted by the previous pass;
- catches changes whose effects were not anticipated by the repairer;
- simple mental model: every changed subject gets reviewed from scratch.

Costs:

- repeatedly pays for already-settled acceptance checks;
- fresh stochastic reviewers may create a moving frontier of unrelated findings;
- increases wall-clock latency and token use;
- can transform review into a generator of perpetual work rather than a proof of closure.

Superpowers explicitly redesigned away from this. Its design spec states that fresh full reviews each round were the churn engine and that review-loop count dominated run-to-run cost variance.

BMAD issue #2576 gives independent empirical evidence. In the reported project, 10 of 10 stories across eight runs used the entire three-cycle budget even though from round 1 every pass was status done, verification was green, and there were zero high / intent_gap / bad_spec findings. Each pass continued because its own review-driven patches triggered the follow-up recommendation. Extra cycles cost approximately 15–36 minutes each plus heavy token spend.

BMAD issue #2772 reports another epic: 9 stories, 21 triage passes, 733 findings. 396 findings were rejected or deferred, and rejection rate rose across later passes. The issue also reports that the blind-hunter layer demanded at least ten findings, meaning at least part of the “fresh signal” was prompt-induced rather than defect-induced.

### Scoped verification after a full discovery pass

Advantages:

- directly answers whether known defects are closed;
- keeps acceptance state stable;
- reduces rediscovery of unrelated polish;
- cheaper and faster;
- allows a circuit breaker to count genuine repair failure rather than random reviewer novelty.

Superpowers' current re-review template states explicitly that it is **not a fresh review — the full review already happened**. It verdicts every prior finding as ADDRESSED / NOT ADDRESSED and checks for new breakage in the fix diff.

### The risk: too narrow a scope

Superpowers issue #2266 documents the critical failure mode of diff-only scoping. In three rounds of adversarial review on one PR, later findings were defects created by the preceding fixes; six findings were fix-caused. The sharpest example changed a return value: one fix stopped a double write by returning nil, while unchanged callers still invoked .size on the return value and crashed. Tests called the method but discarded its return value, so tests stayed green.

The issue specifically points out the tension in the current SDD re-review prompt: “inspect the fix diff for new problems” while not re-reviewing untouched code. A defect caused by a changed contract can live in untouched callers.

Research conclusion: **scoped verification is preferable for the inner loop, but scope must be causal rather than textual.**

The verifier should be permitted/required to inspect:

- each known finding;
- the repair diff;
- tests/regressions covering the repaired class;
- consumers/callers of changed contracts;
- providers/dependencies the fix now relies on;
- sibling representations of the same invariant;
- negative-space/edge cases implicated by the root cause.

It should not reopen arbitrary unrelated code.

## 10. Defect-class/root-cause repair

PWv2.1 REQ-110 is unusually strong relative to the compared systems:

> repair must address the defect class/root cause and materially adjacent sibling/negative-space cases, with generalized regression coverage where feasible, rather than patching only the literal reported example.

This is worth preserving.

Superpowers normally sends the findings verbatim to the implementer. The redesign improves convergence mechanics, but issue #2266 demonstrates that literal compliance with a finding can still damage neighboring contracts.

GSD uses a separate fixer but its code-review command documentation is finding-oriented rather than defining a universal “class/root-cause + siblings” contract.

Spec Kit turns gaps into tasks but does not define a repair ontology at the same level.

OpenSpec tells the agent whether to return to implementation or planning, but does not impose PW's generalized defect-class rule.

Research conclusion: **PW should remain stricter here. A finding is evidence of a defect class, not necessarily the complete repair specification.**

## 11. Sibling and negative-space regression checks

Class-level repair should cover both positive siblings and negative space.

Examples:

- one serializer mishandles omitted optional state → inspect sibling serializers and absence/empty/null cases;
- one return-value change fixes a producer → inspect all relevant consumers;
- one authorization path misses a denial case → test equivalent routes and default-deny behavior;
- one mapping misses an enum member → inspect unmapped members and unknown/future values;
- one parser accepts an invalid form → test adjacent malformed forms, not just the reported string.

The external evidence for this is strongest in Superpowers #2266: tests can stay green even when a changed contract breaks a consumer the test does not inspect.

This supports a closure contract based on the **causal blast radius** of the repaired defect class.

## 12. Anchoring risk

Anchoring is harmful when it narrows discovery and useful when it narrows verification.

### Harmful anchoring

A reviewer who has already declared a subject mostly correct may be less likely to question its own earlier assumptions. A reviewer given the previous verdict rationale may simply confirm the prior checklist rather than reconstruct correctness.

PW's fresh Milestone/final reviewer rules correctly combat this by using accepted authority, current subject, and raw evidence without prior GREEN opinions by default.

BMAD's fresh-context adversarial review is also explicitly intended to reduce self-review anchoring.

### Useful anchoring

During closure, the point is to focus on the known defect and the repair evidence. Reusing the finding set is not a bias to eliminate; it is the test oracle.

Superpowers intentionally anchors its scoped re-review on the prior findings.

Research conclusion: **do not optimize for universal reviewer freshness. Optimize reviewer context for the question being asked.**

## 13. New defects introduced by fixes

Every convergent repair loop needs a regression channel.

The minimum is not merely “run tests again.” Issue #2266 demonstrates that the suite can execute the changed path while failing to assert the changed output.

Recommended bounded regression checks:

1. Verify each original finding is actually absent.
2. Inspect the repair diff for direct breakage.
3. Identify every materially edited contract/invariant.
4. Trace both sides of that contract:
   - what depends on the changed thing;
   - what the changed thing now depends on.
5. Run or add focused regression tests for the repaired class and important sibling/negative-space cases.
6. Permit bounded inspection of unchanged causal consumers/providers.
7. Defer unrelated observations to the next fresh full-scope review unless independently load-bearing.

This is stricter than Superpowers' currently shipped diff-only scoped prompt while preserving its convergence advantage.

## 14. Circuit breakers and iteration ceilings

### Superpowers

Hard cap: five fix rounds per task review.

- Rounds 1–3: resume original implementer.
- Rounds 4–5: fresh implementer, more capable model.
- Every round: scoped re-review.
- No early controller adjudication before the cap, except plan-authority conflict.
- After round five: controller adjudicates each remaining finding.

Residual categories:

- contested/wrong → ledger with ruling, continue;
- real but non-load-bearing → known-open/parked, continue;
- real and load-bearing / structural → existing blocked/ruling path; do not let dependents blindly build on it.

Minor findings never enter the repair loop.

Final whole-branch review is separately bounded: one fixer receives the complete final findings set, then exactly one scoped re-review; residuals are adjudicated.

### BMAD / bmad-loop

Current bmad-loop:

- limits.max_review_cycles default: 3.
- limits.max_followup_reviews default: 1.

The second guard exists specifically because a finalized review can keep recommending its own follow-up. After the permitted follow-up count, the recommendation is damped/journaled rather than burning review cycles.

Issue #2576 is important evidence for why the second guard exists: the review could be done and verification green, but review-driven patches generated another recommendation.

### GSD

/gsd-code-review --fix --auto is capped at three iterations.

The reviewed command documentation does not define a rich post-cap convergence-analysis owner. The cap simply prevents indefinite review/fix/re-review.

### Spec Kit

/speckit.converge instructs repeat until converged and does not document a command-specific iteration ceiling.

However, Spec Kit's generic workflow engine supports explicit bounds:

- while example with max_iterations: 5;
- do-while example with max_iterations: 3.

Thus the engine has the mechanical concept even though the standard converge workflow does not define a dedicated semantic breaker.

### OpenSpec

No hard automatic verify-loop ceiling was found in the default workflow. Its pressure relief is instead semantic severity and optionality: CRITICAL blocks readiness; WARNING/SUGGESTION do not necessarily prevent archive.

### PWv2.1

Current accepted proposal:

- stable authority/acceptance epoch;
- ordinary implementation/test repair does not reset the epoch;
- Card ceiling 5 qualifying fresh full-scope reviews;
- Milestone ceiling 4;
- Final Integration ceiling 3;
- finding-verification passes do not count;
- hitting a hard ceiling exits ordinary loop into Main/root-cause convergence analysis;
- one fresh post-convergence validation may run;
- another RED routes to broader structural classification/restructuring instead of another automatic ordinary loop.

The mode-switch behavior is strong. The main research question is what should consume the 5/4/3 budgets.

## 15. What should happen after the ceiling?

The best circuit breakers do not interpret “limit reached” as “accept RED.”

The useful post-ceiling modes observed or inferred from mature systems are:

- **adjudicate residuals** — Superpowers;
- **replace/de-anchor implementer** — Superpowers before final trip;
- **damp process-generated follow-up** — bmad-loop;
- **convert remaining gaps into explicit work** — Spec Kit;
- **route back to planning/spec when implementation is not the real problem** — OpenSpec;
- **root-cause/convergence analysis and structural reclassification** — current PWv2.1.

PW's post-ceiling approach is the strongest of these for a governed workflow: the ceiling is a **mode switch**, not an acceptance shortcut.

That should remain.

## 16. Minor and non-load-bearing findings

A review loop needs an explicit definition of what is allowed to keep it alive.

Superpowers:

- Minor findings never enter the ordinary fix loop.
- They are ledgered and pointed at the final whole-branch review.
- At the five-round trip, real non-load-bearing residuals may be parked with a ruling.

GSD:

- default fixer scope is Critical + Warning;
- Info findings require --all.

OpenSpec:

- CRITICAL is “must fix before archive”;
- WARNING is “should fix”;
- SUGGESTION is “nice to fix.”

BMAD issue history demonstrates the danger of allowing volume of low-severity patches to justify further review. Issue #2576 specifically argues that many low-severity patches should not by themselves create an endless follow-up chain when verification is green.

Research recommendation for PW:

**Only a material/load-bearing acceptance defect should keep a subject RED. Advisory/minor observations should be recorded durably and surfaced to the next broader review/close disposition, but they should not create an infinite zero-polish requirement.**

If later evidence shows that an advisory finding is actually load-bearing, it can be promoted.

## 17. Broad final review versus per-task review

Per-task review and final broad review serve different purposes.

### Superpowers

The SDD skill deliberately has both:

- one task-scoped review after each implementation task;
- a broad whole-branch review after all tasks.

This layered model is particularly relevant to PW. Superpowers' redesign did not remove broad final review when it narrowed the inner repair loop. It kept the final review as the safety net for:

- defects outside a task's local scope;
- novel observations deferred during scoped re-review;
- cross-task behavior;
- whole-branch integration.

Final repair is also bounded: one fixer gets the complete final finding set, then one scoped re-review, then residual adjudication.

### PWv2.1

PW has an even stronger hierarchy:

- Card review for bounded local correctness;
- Milestone review for broader composition;
- final integration review for the completed workstream.

This layered architecture reduces the need for every Card repair verifier to behave like a branch-wide auditor.

Research conclusion: **narrower Card repair verification is safer in PW than it would be in a workflow with no higher integration layers, because Milestone and Final Integration provide additional fresh discovery surfaces.**

## 18. Evidence of review-loop redesign caused by real failures

### Superpowers — direct redesign evidence

The July 2026 SDD design lists “Pathological review loops” as one of four observed real-session problems. It says:

- the old rule was “Repeat until approved”;
- there was no round cap;
- each re-review was a fresh full review;
- a nondeterministic frontier reviewer surfaced new findings every round;
- strict-cost work independently measured review-loop count as the biggest run-to-run cost variance.

The resulting redesign directly introduced:

- original implementer resume semantics;
- scoped re-review;
- five-round breaker;
- fresh implementer in rounds 4–5;
- controller adjudication at the cap;
- broad final whole-branch review.

This is the closest external precedent to the PW question.

### Superpowers — repair-induced regression evidence

Issue #2266 reports six fix-caused findings and two consecutive repairs of one return-value contract that each solved the immediate reported problem but created another one. This is evidence that scoped verification must trace causal blast radius, not only the textual diff.

The issue is open and therefore should be treated as empirical evidence/proposed improvement, not as already-shipped normative semantics.

### BMAD — structurally non-convergent follow-up

Issue #2576 reports:

- 10/10 stories across eight runs consumed all three review cycles;
- round 1 was already done and verification-green;
- zero high / intent_gap / bad_spec findings from round 1;
- each extra cycle was triggered by the review's own patches;
- later findings became increasingly marginal or self-inflicted;
- each extra cycle cost roughly 15–36 minutes plus heavy token use.

bmad-loop's current max_followup_reviews guard is a direct response class to this behavior.

### BMAD — overproduction and diminishing signal

Issue #2772 reports one epic with:

- 9 stories;
- 21 triage passes;
- 733 findings;
- 271 rejected at P3/P4;
- 125 deferred at P3/P4;
- 396 findings, more than half, going nowhere;
- increasing rejection rate across later passes;
- a blind-hunter prompt that required at least ten findings.

This is strong evidence that “fresh review” can become anti-convergent when the prompt rewards finding production rather than material falsification.

### BMAD — duplicate review seats

Issue #2760 reports that bmad-build and bmad-code-review duplicated three byte-identical review layers on the same diff. The reported effect is redundant subagent launches and token/time cost with little incremental signal; only the additional acceptance-auditor layer is novel.

This supports a broader principle: **review diversity matters more than review count. Repeating the same lens against the same surface is weak evidence for correctness.**

## 19. Critical comparison with current PWv2.1

### Current strengths that should be preserved

1. **Exhaustive fresh full-scope discovery**
   - REQ-109 prevents first-blocker serialization.
2. **Distinct bounded finding verification**
   - REQ-108 already recognizes that known-finding closure and fresh full review are different operations.
3. **Class/root-cause repair**
   - REQ-110 is stronger than most external workflows.
4. **Stable review epoch**
   - REQ-111 prevents ordinary repair from laundering the attempt history by resetting counters.
5. **Hard ceilings**
   - REQ-112 prevents infinite automatic review.
6. **Convergence mode switch**
   - REQ-113 correctly exits ordinary loop into Main analysis rather than accepting RED.
7. **One post-convergence fresh validation**
   - avoids declaring success from analysis alone.
8. **Structural classification after another RED**
   - REQ-114 prevents “one more normal loop” after systemic failure.
9. **Layered Card / Milestone / Final review**
   - provides distinct independent discovery surfaces.
10. **Reviewer independence rules**
   - subject-relative independence is more precise than merely naming a different runtime/model.

### The likely over-cost

Current REQ-112 counts **qualifying fresh full-scope reviews** toward 5/4/3.

That implies an ordinary pattern could become:

fresh full review → repair → verification → fresh full review → repair → verification → fresh full review …

even when the later full review is mainly sampling another stochastic set of observations over almost the same subject.

External evidence suggests this is where cost/latency and review churn grow fastest.

### Is current PW too weak?

No. If anything, PW has stronger correctness mechanisms than the compared workflows.

The issue is not insufficient review. It is **where full fresh review is spent**.

### Is current PW appropriately balanced?

Not quite, based on the evidence. It is defensible for very high-risk work, but as the default ordinary RED loop it appears more expensive than necessary.

A hybrid can preserve the correctness advantages while making convergence more deterministic.

## 20. Recommended hybrid lifecycle

### D0 — exhaustive fresh discovery

A fresh independent reviewer:

- reconstructs correctness from accepted authority;
- evaluates the full applicable acceptance surface;
- does not stop at first blocker;
- records every independently discovered material finding;
- groups related evidence where possible;
- freezes the material finding set before repair.

### R — class/root-cause repair

The ordinary Card Worker:

- identifies the root cause / defect class;
- repairs sibling representations;
- handles negative-space cases;
- traces materially changed contracts;
- adds generalized regression coverage where feasible;
- reports the exact tests/evidence.

The original Worker should normally remain owner for early repair attempts.

### V — scoped closure verification

The discovering reviewer may perform this if it did not repair the subject.

Scope:

- every known open material finding;
- the repair diff;
- focused tests and regression evidence;
- siblings/negative space implicated by the defect class;
- callers/consumers/providers/contracts causally reached by the fix.

It is intentionally anchored.

Outcomes:

- known class closed;
- known class remains open;
- fix introduced/exposed a causally related new defect;
- unrelated observation, recorded for later fresh discovery rather than automatically extending closure.

### D1 — fresh full-scope rediscovery after closure

Only when the known material set is closed:

- assign a fresh reviewer;
- give accepted authority, current exact subject, and raw evidence;
- withhold prior verdict rationales/repair narrative as a correctness checklist;
- run the full applicable acceptance surface again.

Outcomes:

- GREEN → close this review obligation;
- RED with genuinely new material defect class → open next discovery epoch;
- RED containing only persistence/recurrence of an already known class → reopen that class without counting it as a new discovery epoch.

### Circuit breakers

Two independent bounds:

1. **Defect-class repair/closure budget**
   - suggested default: 3 failed repair/closure rounds for the same class;
   - then Main convergence/root-cause analysis.
2. **Material discovery-epoch budget**
   - provisionally retain Card 5 / Milestone 4 / Final Integration 3;
   - count fresh full-scope RED reviews that discover at least one genuinely new material defect class.

After convergence analysis:

- one fresh full-scope post-convergence validation;
- another material RED → broader structural owner, not another ordinary cycle.

## 21. What should 5/4/3 count?

Three candidate interpretations were evaluated.

### A. Count repair rounds

Not recommended.

Repair/closure rounds are comparatively cheap and directly targeted. Counting each one in the main discovery budget would punish a workflow for carefully verifying a difficult known defect.

A separate smaller class-level closure cap is better.

### B. Count every fresh full-scope review

This is the current PWv2.1 rule.

It is safe but expensive. It counts reviewer sampling events rather than semantic novelty. A fresh review that only rediscovers the same still-broken class consumes the same budget as one that exposes a genuinely new class.

External evidence from Superpowers and BMAD makes this the least attractive default of the three.

### C. Count material defect-class discovery epochs

Recommended.

Definition:

**A material discovery epoch is consumed when a qualifying fresh full-scope RED review discovers at least one material defect class that is neither already open nor previously closed/reopened in the current stable authority/acceptance epoch.**

Consequences:

- one review finding four examples of one root cause consumes one discovery epoch;
- a scoped verification pass consumes none;
- a GREEN fresh review consumes none;
- a fresh review proving that a supposedly fixed old class is still broken reopens that class but does not invent a new discovery epoch;
- a fresh review finding a genuinely different material class consumes the next epoch.

The 5/4/3 values can remain provisional because the external systems do not have PW's exact Card/Milestone/Final hierarchy. What the evidence justifies now is changing the **semantic unit**, not confidently changing the numbers.

## 22. Trade-off summary

### Same-reviewer scoped verification

Best at:

- proving exact closure;
- understanding prior finding rationale;
- low latency;
- stable comparison against known evidence.

Risks:

- may preserve mistaken original assumptions;
- can miss unrelated latent defects;
- can be too diff-local unless causal blast radius is explicit.

Mitigation:

- causal scope;
- later fresh full-scope reviewer.

### Fresh full-scope review

Best at:

- independent rediscovery;
- finding omissions in the prior review;
- testing whether the repaired subject stands without the repair narrative.

Risks:

- expensive;
- stochastic frontier/churn;
- repeated same-lens reviews can duplicate work;
- may manufacture low-value findings when prompts reward issue count;
- can keep already-correct work open.

Mitigation:

- run it after known-finding closure;
- fresh reviewer;
- count genuinely new material defect classes;
- bounded discovery epochs.

## 23. Research recommendation: candidate requirement wording

> **NOT ACCEPTED AUTHORITY.** The wording below is a research recommendation only. It is not a change to requirements/PWV21_POLICY_KERNEL.md.

### Candidate revision — reviewer continuity

**PWV21-REQ-061 — candidate revised wording**

After Worker repair of the same Card, the Reviewer that discovered the findings MAY perform bounded finding-closure verification if that Reviewer did not materially repair the subject. Such verification does not qualify as the subsequent fresh full-scope discovery review.

### Candidate revision — bounded closure scope

**PWV21-REQ-108 — candidate revised wording**

PWv2.1 MUST distinguish bounded finding-closure verification from fresh full-scope discovery review. Finding-closure verification MUST evaluate the known findings, the repair diff, required regression evidence, and any materially reachable caller, consumer, provider, contract, invariant, sibling representation, negative-space case, or other causal blast-radius surface needed to determine whether the repair introduced or exposed related breakage. It MUST NOT broaden into an unrelated whole-subject review merely because other code is available.

### Candidate clarification — complete discovery

**PWV21-REQ-109 — candidate retained with clarification**

A fresh full-scope review MUST evaluate the complete applicable acceptance surface from accepted authority, the exact current subject/artifacts and raw evidence. Discovery of one blocking defect MUST NOT terminate the pass before all independently discovered material findings are recorded. The resulting material finding set is frozen before ordinary repair begins.

### Candidate revision — class-level repair

**PWV21-REQ-110 — candidate revised wording**

After RED, repair MUST target the defect class/root cause represented by the findings, including materially adjacent sibling representations, negative-space cases and causal consumers/providers affected by the proposed repair, with generalized regression coverage where feasible. Literal correction of the reported example alone is insufficient when the same defect class remains materially reachable elsewhere.

### Candidate replacement — discovery accounting

**PWV21-REQ-112 — candidate replacement**

Review-loop accounting MUST distinguish material discovery epochs from repair/closure rounds.

A material discovery epoch occurs when a qualifying fresh full-scope RED review discovers at least one material defect class that is not already open or durably closed/reopened in the current stable authority/acceptance epoch.

Default hard ceilings per stable authority/acceptance epoch SHOULD remain provisionally:

- Card: 5 material discovery epochs;
- Milestone: 4 material discovery epochs;
- Final Integration: 3 material discovery epochs.

A bounded finding-verification pass, an ordinary repair attempt, a GREEN fresh validation, or a fresh RED that contains only previously known or reopened defect classes MUST NOT increment the material-discovery counter.

### Candidate new requirement — closure before rediscovery

**PWV21-REQ-112A — candidate**

Once a fresh full-scope review freezes its material finding set, PW MUST remain in bounded repair/finding-closure mode until every known material finding is either verified closed or durably classified by the correct authority as non-load-bearing/non-blocking. PW MUST NOT launch another ordinary fresh full-scope review merely to verify those known repairs.

### Candidate new requirement — fresh rediscovery gate

**PWV21-REQ-112B — candidate**

After all known material findings from the preceding discovery review are closed, PW MUST require one fresh full-scope discovery review before declaring the applicable Card, Milestone or Final Integration review obligation GREEN.

That fresh review MUST use a fresh Reviewer assignment relative to the preceding discovery reviewer, MUST reconstruct correctness from accepted authority/current subject/raw evidence, and MUST NOT receive prior verdict rationales or repair narratives as its correctness checklist.

### Candidate new requirement — new versus reopened class

**PWV21-REQ-112C — candidate**

A fresh full-scope RED that discovers a genuinely new material defect class opens the next material discovery epoch.

A fresh full-scope RED that demonstrates persistence or recurrence only of an already-known defect class reopens that class but does not create a new material discovery epoch.

### Candidate new requirement — class repair breaker

**PWV21-REQ-112D — candidate**

Each defect-class closure loop MUST have a bounded ordinary repair budget. A provisional default ceiling of three failed repair/finding-verification rounds for the same defect class within one stable authority/acceptance epoch SHOULD be evaluated.

Reaching that ceiling MUST leave ordinary repair mode and route to Main convergence/root-cause analysis. Main MAY replace the Worker or otherwise alter the implementation approach within already accepted authority, but stronger/different model assignment remains governed by the existing runtime/model-authorization rules.

### Candidate new requirement — non-load-bearing findings

**PWV21-REQ-112E — candidate**

A non-load-bearing advisory/minor finding MUST NOT by itself keep a review subject RED. Such findings MUST remain durable and visible to the next applicable broader review or close-time disposition. Promotion to loop-bearing material status requires concrete acceptance, dependency, safety, correctness or other load-bearing evidence.

### Candidate revision — convergence trigger

**PWV21-REQ-113 — candidate revised wording**

Reaching either the material-discovery ceiling or a defect-class repair ceiling MUST switch the workflow out of the ordinary RED/repair/review loop into Main convergence/root-cause analysis. A ceiling never authorizes acceptance of a material RED.

After convergence analysis, one fresh full-scope post-convergence validation MAY run.

### Candidate retained structural stop

**PWV21-REQ-114 — candidate retained**

If the post-convergence validation remains materially RED, PW MUST route to broader structural classification or restructuring through the correct owner rather than automatically starting another ordinary repair or discovery loop.

## 24. Research recommendation: candidate ADR wording

> **NOT ACCEPTED AUTHORITY.** This is research wording only and does not alter decisions/ADR_PWV21_REVIEW_LIFECYCLE.md.

PWv2.1 should model review as two different semantic operations:

1. **Discovery review**
   - fresh;
   - independent;
   - full-scope;
   - de-anchored from prior verdict narratives;
   - intended to discover material defect classes across the complete acceptance surface.

2. **Finding-closure verification**
   - bounded;
   - intentionally anchored to the already discovered material findings;
   - evaluates the repair diff, regression evidence, and the causal blast radius of repaired contracts/invariants;
   - intended to prove that known defect classes are removed without reopening unrelated discovery.

An initial fresh full-scope RED freezes the complete material finding set independently discovered by that pass. Ordinary repair then remains in finding-closure mode. Another fresh full-scope review is not required merely to verify the known repairs.

The Reviewer that discovered findings may perform their scoped closure verification if it did not materially repair the subject. It cannot satisfy the next fresh full-scope discovery review.

Only after all known material findings close does PW instantiate a fresh full-scope reviewer to search for omitted/new defect classes.

The existing Card/Milestone/Final Integration values 5/4/3 should be treated as provisional **material-discovery-epoch ceilings**, not counts of every review invocation and not repair-round limits. Defect-class repair should have its own smaller bounded budget.

A scoped verification boundary must be causal, not textual: it includes unchanged code materially reached by the repair when a contract, return value, dependency, representation, invariant, data source, or equivalent interface was changed.

This structure retains independent rediscovery after repair while preventing known-finding verification from repeatedly paying the cost and stochastic churn of a complete fresh review.

## 25. Final assessment

### Current PWv2.1 lifecycle

**Assessment: too expensive in the inner loop, not too weak overall.**

The current lifecycle is conservative and correctness-oriented. Its strongest semantics should remain: exhaustive material discovery, root-cause repair, stable epoch, independent layered reviews, hard mode-switch ceilings, convergence analysis, post-convergence fresh validation, and structural escalation after another RED.

The research indicates that the ordinary fix loop is the wrong place to spend repeated fresh full-scope review seats.

### Best-supported lifecycle

**Fresh exhaustive discovery  
→ freeze material findings  
→ class/root-cause repair  
→ scoped causal closure verification  
→ fresh full-scope discovery only after closure  
→ repeat only when a genuinely new material defect class is found.**

This separates two questions that should not share the same mechanism:

- **Did we fix what we already know is wrong?**  
  Use bounded, intentionally anchored causal verification.

- **What material defects do we still not know about?**  
  Use a fresh, de-anchored full-scope reviewer.

That split gives the strongest convergence/cost trade-off found in the current evidence.

## 26. Source verification notes

A fresh context can verify the material claims using the following exact source areas:

1. Superpowers redesign:
   - section “Problems” for uncapped fresh-full-review churn;
   - “Design Decisions” for original implementer, scoped re-review, five-round cap, late fresh implementer;
   - “The Fix Loop” for rounds 1–3 / 4–5;
   - “Adjudication at Trip” for contested/non-load-bearing/load-bearing residuals;
   - “Final Review Loop” for one final fix wave + one scoped re-review.
   - URL:
     https://github.com/obra/superpowers/blob/main/docs/superpowers/specs/2026-07-15-sdd-fix-loop-redesign-design.md

2. Superpowers current SDD skill:
   - process diagram for R≤3 resume / R≥4 fresh;
   - fix-loop section for Minor deferral and round-five breaker;
   - final-review path for broad whole-branch review.
   - URL:
     https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md

3. Superpowers scoped re-review prompt:
   - opening statement “not a fresh review”;
   - per-finding ADDRESSED / NOT ADDRESSED;
   - new breakage in fix diff;
   - out-of-scope observations non-blocking.
   - URL:
     https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/re-review-prompt.md

4. Superpowers issue #2266:
   - six fix-caused findings;
   - return-value / unchanged-caller crash example;
   - argument that fix scope should follow causal contract edges.
   - URL:
     https://github.com/obra/superpowers/issues/2266

5. bmad-loop:
   - “Fresh-context adversarial review” feature;
   - limits.max_review_cycles default 3;
   - limits.max_followup_reviews default 1 and damping semantics.
   - URL:
     https://github.com/bmad-code-org/bmad-loop/blob/main/docs/FEATURES.md

6. BMAD issue #2576:
   - 10/10 stories using full three-cycle budget;
   - green verification from round 1;
   - review-driven patches self-triggering further review;
   - estimated 15–36 minute extra cycles.
   - URL:
     https://github.com/bmad-code-org/BMAD-METHOD/issues/2576

7. BMAD issue #2772:
   - 9 stories, 21 triage passes, 733 findings;
   - 396 rejected/deferred;
   - prompt quota requiring at least ten issues.
   - URL:
     https://github.com/bmad-code-org/BMAD-METHOD/issues/2772

8. BMAD issue #2760:
   - duplicate blind-hunter / edge-case-hunter / verification-gap layers in bmad-build and bmad-code-review;
   - redundant review work on the same diff.
   - URL:
     https://github.com/bmad-code-org/BMAD-METHOD/issues/2760

9. GSD commands:
   - /gsd-code-review;
   - dedicated gsd-code-reviewer and gsd-code-fixer;
   - default Critical + Warning fix scope;
   - --fix --auto max 3 iterations.
   - URL:
     https://github.com/gsd-build/get-shit-done/blob/main/docs/COMMANDS.md

10. Spec Kit agentic SDD:
    - /speckit.converge outcomes “Converged” vs “Tasks appended”;
    - repeat implement/converge until clean.
    - URL:
      https://github.com/github/spec-kit/blob/main/docs/reference/agentic-sdd.md

11. Spec Kit workflow engine:
    - bounded while / do-while examples using max_iterations.
    - URL:
      https://github.com/github/spec-kit/blob/main/workflows/README.md

12. OpenSpec:
    - /opsx:verify completeness/correctness/coherence;
    - CRITICAL / WARNING / SUGGESTION prioritization;
    - workflow route back to apply or update.
    - URLs:
      https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md
      https://github.com/Fission-AI/OpenSpec/blob/main/openspec/specs/opsx-verify-skill/spec.md

13. PWv2.1 current accepted baseline:
    - repository-local requirements/PWV21_POLICY_KERNEL.md, especially PWV21-REQ-048, 056–076, 108–114;
    - repository-local decisions/ADR_PWV21_REVIEW_LIFECYCLE.md.
