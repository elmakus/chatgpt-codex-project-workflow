# Research — Operational YAGNI / anti-overengineering practices

Date: `2026-09-21`
Research question: `How do established engineering sources and public repositories operationalize YAGNI / anti-overengineering, and which concrete practices should Project Workflow adopt or avoid compared with the proposed global invariant?`

Research ID: `yagni-practices-r1`
Status: `consumed`
Origin role: `brainstorming`
Origin subject: `yagni-overengineering-guard@R2`
Return target: `brainstorming:yagni-overengineering-guard@R2`
Return reconciliation: `applied`
Return reconciliation result: `brainstorming/YAGNI_OVERENGINEERING_GUARD.md@yagni-overengineering-guard@R3`

## Scope

Compare the proposed Project Workflow invariant with:
- established descriptions of YAGNI / simple design / premature generalization;
- concrete engineering guidance that operationalizes the idea;
- public repository or agent/contributor instructions that explicitly discourage speculative abstractions or unrelated future-proofing.

Identify:
- common operational patterns;
- exceptions/guardrails;
- failure modes and overly simplistic interpretations;
- the smallest evidence-backed wording suitable for Project Workflow.

## Sources / evidence

| Source | What it supports | Freshness / limitations |
|---|---|---|
| Martin Fowler, “Yagni” — https://martinfowler.com/bliki/Yagni.html | YAGNI rejects presumptive future capabilities/extra complexity; it does not reject refactoring, testing or delivery practices that keep the system easy to change. | Canonical explanatory article; 2015, still directly relevant as principle background. |
| Martin Fowler, “Is Design Dead?” — https://martinfowler.com/articles/designDead.html | Simple design means not adding code needed only by future stories; frameworks/flexibility should grow when real needs appear; refactoring supports rather than violates YAGNI. | Older XP/evolutionary-design discussion but directly addresses the principle. |
| Martin Fowler, “Beck Design Rules” — https://martinfowler.com/bliki/BeckDesignRules.html | Simple design balances correctness/tests, duplication, intention-revealing code and minimizing unnecessary classes/methods. | Principle-level guidance, not a project-specific policy. |
| Google Engineering Practices, “What to look for in a code review” — https://google.github.io/eng-practices/review/reviewer/looking-for.html | Reviewers should detect over-engineering: excessive genericity or functionality not currently needed; solve known present problems rather than speculative future problems. | Public general engineering guidance. |
| Google Engineering Practices, “Small CLs” — https://google.github.io/eng-practices/review/developer/small-cls.html | Prefer focused self-contained changes and avoid unused APIs; small changes reduce bugs, wasted work and review complexity. | Supports scope proportionality more than YAGNI wording itself. |
| Kent C. Dodds, “AHA Programming” — https://kentcdodds.com/blog/aha-programming | Avoid hasty abstractions; duplication can be cheaper than a wrong abstraction; learn the actual variation before generalizing; optimize for change. | Practitioner guidance, not a formal standard. |
| Sandi Metz, “The Wrong Abstraction” — https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction | Wrong abstractions create conditional complexity; reintroducing duplication can be cheaper than preserving a bad abstraction. | Practitioner guidance focused specifically on abstraction. |
| ClickHouse/mcp-clickhouse `AGENTS.md` — https://github.com/ClickHouse/mcp-clickhouse/blob/main/AGENTS.md | Concrete agent policy: keep changes small/safe/tied to task, do not add abstractions for hypothetical future needs, preserve security/public contracts, do not bundle unrelated cleanup. | Live public repository instruction; repo-specific constraints should not be copied wholesale. |
| ethanhq/cc-fleet `AGENTS.md` — https://github.com/ethanhq/cc-fleet/blob/main/AGENTS.md | Concrete agent policy: minimal intrusion; simplest correct implementation; no speculative abstraction/dependency/config surface; reuse existing helper first. | Live public repository instruction; useful operational pattern. |
| gszr/lunar `AGENTS.md` — https://github.com/gszr/lunar/blob/main/AGENTS.md | Concrete agent policy: simplest thing that works; no “for later” types/unused flags; smallest useful diff; do not improve unrelated code. | Live public repository instruction; deliberately small-project context. |
| lufre1/opencode-extras `yagni.md` — https://github.com/lufre1/opencode-extras/blob/main/yagni.md | Explicit agent rule: no speculative abstraction/config/plugin points/future-proofing; smallest plan; remove steps whose absence would not fail requirements. | Small public ruleset, useful as a direct example rather than authoritative standard. |

## Verified findings

### 1. The proposed Project Workflow direction matches the dominant pattern

Across Fowler, Google engineering guidance and sampled public agent instructions, the recurring rule is not “never abstract” or “always write the fewest lines.” It is:

- solve the concrete current problem;
- avoid capability/genericity added for hypothetical future requirements;
- keep the change/design as small as correctness and current constraints allow;
- require extra machinery to earn its place through a present need.

This matches the proposed Project Workflow invariant closely.

### 2. “Simplest” must be bounded by correctness and accepted constraints

Google's guidance treats complexity as a review dimension alongside design and functionality. Public repository rules likewise pair simplicity with safety, compatibility, security, tests and existing invariants.

Therefore Project Workflow should define “simplest” as **least unnecessary complexity while fully satisfying the complete applicable authority/constraint surface**, never as shortest code, smallest line count or fewest files.

### 3. The strongest operational form is a justification test, not a complexity metric

Useful concrete policies repeatedly ask whether a piece of complexity is tied to the actual task/current system:
- speculative abstraction;
- generic framework or interface;
- configuration/flag with no current variation;
- plugin/extension point “for later”;
- new dependency or infrastructure without a current reason;
- compatibility shim or fallback for an unsupported/hypothetical case;
- unrelated refactor bundled with a feature/fix.

This supports a simple reviewable question:

> What concrete current requirement, accepted constraint, verified evidence, existing contract or demonstrated current reuse justifies this additional complexity?

If no such justification exists, remove/defer it.

A scoring model or numeric “complexity budget” is not supported by the evidence and would itself add process complexity.

### 4. YAGNI must not attack code malleability

Fowler explicitly distinguishes speculative feature complexity from refactoring/testing/continuous-delivery work that makes future change cheap. YAGNI depends on a malleable codebase.

Project Workflow should therefore state that YAGNI does **not** justify:
- skipping tests required by the current acceptance/risk surface;
- avoiding a refactor that is concretely needed to make the current change correct/clear/maintainable;
- degrading security, reliability, compatibility or observability required now;
- preserving confusing duplication indefinitely when current repeated evidence makes the correct abstraction clear.

### 5. AHA adds a useful abstraction-specific corollary

Kent C. Dodds / Sandi Metz provide a practical refinement: do not force DRY too early. Temporary duplication may be cheaper than inventing the wrong generalized abstraction before the real variation is known.

Project Workflow should not create a hard “two/three call sites” threshold, because the sampled practices vary and context matters. A policy-neutral wording can instead say:

- do not generalize from hypothetical reuse;
- prefer learning from concrete current cases;
- introduce an abstraction when current evidence shows a stable shared concept or when another current constraint requires it.

### 6. Focused-diff guidance is a useful consequence, but not the core invariant

Google and several `AGENTS.md` examples pair anti-overengineering with:
- focused/self-contained changes;
- no unrelated cleanup/refactor;
- smallest useful diff.

Project Workflow already has bounded Task Cards/workstreams and proportional paths, so this should be expressed as a consequence of YAGNI where relevant rather than creating a new change-size subsystem.

### 7. Existing primitives are usually preferred over new machinery

Several concrete agent policies explicitly favor existing helpers/platform features before adding dependencies/layers. This is consistent with YAGNI because each new dependency/config/layer expands the maintenance surface.

Project Workflow can include this as a non-absolute preference:
- reuse an existing fitting mechanism before creating a new one;
- create new machinery when the existing mechanism cannot satisfy the current authority cleanly.

### 8. Evidence-based future risk can be a present justification

Fowler's broader evolutionary-design discussion does not imply ignoring known future costs. The relevant distinction is whether complexity today has a concrete justification rather than a guessed use.

For Project Workflow, “present justification” can include a verified current constraint or risk such as:
- an existing public compatibility contract;
- a security/safety boundary;
- a migration constraint;
- an already-known integration target;
- measured performance/capacity requirements;
- demonstrated current reuse.

There is no need for a separate speculative-future exception model: these are already present facts/evidence.

## Repository/current-state findings

Current Project Workflow already supplies complementary mechanisms:
- Brainstorming keeps simple scopes lightweight;
- requirements/decisions bound accepted intent;
- JIT planning delays unknown future implementation detail;
- micro-fix avoids full planning machinery for bounded issue fixes;
- progressive disclosure minimizes unnecessary context;
- Task Cards bound implementation scope;
- independent review already has the correct place to challenge unjustified implementation complexity.

Therefore a single policy-neutral engineering invariant can compose with existing workflow mechanics. No new lifecycle phase, gate, scoring system, complexity registry or durable state field is justified.

## Alternatives

### A. Proposed global invariant only

Good baseline but incomplete if it can be misread as “avoid refactoring/tests.”

### B. Global invariant + concise guardrails/corollaries

Best fit with evidence:
- simplest fully correct/current-authority solution;
- no speculative machinery;
- concrete-current-justification test;
- YAGNI does not excuse poor code health/current quality obligations;
- abstract from demonstrated current need, not imagined reuse;
- prefer existing fitting mechanisms before new machinery.

### C. Detailed numeric policy

Examples: maximum layers, minimum number of call sites before abstraction, complexity scoring.

Reject. Not supported consistently by sources and would create the kind of overengineered policy this feature is intended to prevent.

## Analysis

The initial Project Workflow idea is directionally correct and stronger than a bare slogan because it already says “fully satisfies current accepted requirements, decisions and evidence.”

The main improvement from Research is to make **malleability/current quality** explicit. Without that clause, an agent could incorrectly invoke YAGNI to avoid refactoring, tests, security hardening or maintainability work required by the current change.

The second improvement is to make the rule operational at review time through one justification question rather than new process machinery.

The third improvement is an AHA-style abstraction corollary: duplication is not automatically a defect when the alternative is a speculative abstraction whose real shape is not yet known.

## Recommendation, if requested

Adopt a compact policy-neutral invariant approximately in this shape:

> **YAGNI / proportional design:** Prefer the simplest solution that fully satisfies the current accepted requirements, decisions, constraints and verified evidence. Do not add speculative abstractions, generality, extensibility, configuration, dependencies, infrastructure, compatibility paths or future-proofing for hypothetical needs. Every material increase in complexity must have a concrete current justification. YAGNI does not justify skipping current correctness, security, testing, maintainability/refactoring or compatibility obligations. Generalize when current evidence shows the shared abstraction or another current constraint requires it, not merely because reuse might appear later.

Operational review question:

> Which current requirement, accepted constraint, verified evidence, existing contract or demonstrated current reuse justifies each material piece of extra complexity?

No new phase/gate/state is recommended. Apply the invariant through existing Definition/Planning/Execution Prep/Execution/Review semantics.

## Project Definition candidates

- Requirement candidate: Project Workflow SHALL prefer the least-complex solution that fully satisfies the applicable accepted authority and verified current evidence.
- Requirement candidate: speculative abstractions/generalization/extensibility/config/dependencies/infrastructure/compatibility paths/future-proofing SHALL NOT be introduced solely for hypothetical future needs.
- Requirement candidate: material additional complexity SHALL have a concrete current justification traceable to accepted authority, verified evidence, an existing contract or demonstrated current use.
- Guardrail candidate: YAGNI SHALL NOT be used to omit current correctness, security, testing, maintainability/refactoring, compatibility or other applicable acceptance obligations.
- Decision candidate: do not add a new YAGNI lifecycle gate, scoring model or complexity registry; use existing roles/reviews and bounded workflow state.
- Decision candidate: avoid numeric reuse thresholds; abstractions should emerge from demonstrated current need/variation or other concrete current constraints.
- Planning implication: policy-neutral wording likely belongs in common authority/engineering guidance, with existing policy-local planning/execution/review modules referencing or consuming it rather than duplicating divergent versions.

Research is evidence, not an accepted requirement/decision/plan by itself. Return to the exact recorded Return target.
