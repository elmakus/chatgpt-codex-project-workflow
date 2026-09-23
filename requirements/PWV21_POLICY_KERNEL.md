# PWv2.1 Policy Kernel Requirements

Revision: `R1`
Status: `approved`
Updated: `2026-09-23`
Definition subject: `pwv21-policy-kernel@1`
Source Brainstorming: `brainstorming/PWV21_POLICY_KERNEL.md`
Exact promoted source: `elmakus/chatgpt-codex-project-workflow@e2dd13b6a92cf14233a81a08ee86bcd5f5d84244:brainstorming/PWV21_POLICY_KERNEL.md@2e35a3cc2aeeb8f1bd950de0e1da324615db99b2`

## Goal / target state

Evolve the existing Project Workflow V2 implementation conservatively into PWv2.1 so deterministic workflow mechanics are derived by a small stateless policy kernel while semantic reasoning remains role/LLM-owned, Git/repository state remains canonical, and execution may move between ChatGPT and OR/Paseo without private runtime state becoming authority.

PWv2.1 is an extension of the existing executable V2 router/state-contract baseline in `elmakus/project_workflow_v2`; it is not a rewrite from a Markdown-only router and must not become an orchestration platform.

## Requirements

### Policy kernel and mechanical truth

| ID | Requirement | Priority | Status |
|---|---|---|---|
| PWV21-REQ-001 | PWv2.1 MUST extend the existing V2 executable router/state-contract model only for predicates mechanically derivable from canonical repository state. | MUST | accepted |
| PWV21-REQ-002 | Semantic/product/strategy/review reasoning MUST remain owned by the appropriate workflow role/LLM module rather than being forced into deterministic policy code. | MUST | accepted |
| PWV21-REQ-003 | The policy kernel MUST remain stateless with respect to project authority: no daemon-owned project database, scheduler state, worker/session ownership, or hidden mutable authority. | MUST | accepted |
| PWV21-REQ-004 | The policy kernel MUST be read-only with respect to canonical project state. It MAY validate, route, compile obligations, validate results and perform reconciliation checks, but canonical writes are explicit governed coordinator/role actions. | MUST | accepted |
| PWV21-REQ-005 | PWv2.1 MUST use a deliberately small versioned machine-readable mechanical-policy registry for stable rule IDs, precedence, route/stop/recovery outcomes, owner modules and named typed predicates. | MUST | accepted |
| PWV21-REQ-006 | The mechanical registry MUST NOT become an arbitrary-expression or general-purpose workflow DSL. | MUST | accepted |
| PWV21-REQ-007 | Mechanical policy MUST have one canonical representation with a checked human-readable semantic projection; Markdown and executable code MUST NOT independently encode competing condition trees. | MUST | accepted |
| PWV21-REQ-008 | No executable mechanical routing predicate MAY exist only in Python. Canonical repository contracts MUST describe its meaning and relevant inputs sufficiently for helper-less recovery. | MUST | accepted |
| PWV21-REQ-009 | Contract/parity tests MUST detect mechanically verifiable drift between registry, predicate implementation and human-readable workflow contracts and MUST fail closed on disagreement. | MUST | accepted |
| PWV21-REQ-010 | Exact registry serialization, file naming, schema field naming and internal module layout remain Planning/implementation choices unless they alter authority or user-visible semantics. | MUST | accepted |

### Portability and helper-less recovery

| ID | Requirement | Priority | Status |
|---|---|---|---|
| PWV21-REQ-011 | Canonical Git/repository state plus portable workflow contracts MUST be sufficient for a fresh capable ChatGPT/runtime to reconstruct the exact legal continuation without OR/Paseo private state or helper cache. | MUST | accepted |
| PWV21-REQ-012 | The executable helper/reference implementation SHOULD be used when available but MUST NOT be a prerequisite for legal continuation. | MUST | accepted |
| PWV21-REQ-013 | Helper/router unavailability alone MUST NOT create a user stop when canonical contracts are sufficient to derive the route. | MUST | accepted |
| PWV21-REQ-014 | Helper-derived and helper-less fresh-ChatGPT routing MUST agree on the same legal next obligation/stop for representative canonical states. A disagreement is a workflow parity defect and routes fail-closed to Recovery. | MUST | accepted |
| PWV21-REQ-015 | Acceptance fixtures MUST include RED/recovery, fresh-review boundaries, parallel Cards, migration from PWv2, stale results and other high-risk route states. | MUST | accepted |
| PWV21-REQ-016 | A PWv2.1 feature that cannot be understood/recovered from canonical contracts without the Python helper MUST be rejected. | MUST | accepted |
| PWV21-REQ-017 | A destructive recovery acceptance test MUST prove that after discarding chat memory, OR/Paseo state and helper cache, canonical Git alone identifies the exact legal continuation. | MUST | accepted |

### Typed Execution Obligation and Result contract

| ID | Requirement | Priority | Status |
|---|---|---|---|
| PWV21-REQ-018 | PWv2.1 MUST expose versioned transport-neutral typed `Execution Obligation` and `Execution Result` contracts; JSON is the preferred interchange serialization. | MUST | accepted |
| PWV21-REQ-019 | An `Execution Obligation` MUST bind the exact role, exact subject, applicable authority, prerequisites, mechanically safe constraints and completion/test/evidence contract. | MUST | accepted |
| PWV21-REQ-020 | PW MUST own authority resolution: it determines applicable authority, validates exact refs/hashes and materializes the bounded authority bundle required by the obligation. | MUST | accepted |
| PWV21-REQ-021 | OR/Paseo MUST transport/execute the already-resolved authority bundle and MUST NOT infer, add, drop or reinterpret which Project Workflow authority applies. | MUST | accepted |
| PWV21-REQ-022 | LLM summaries MAY aid navigation but MUST NOT substitute for exact authority refs/materialized required sources. | MUST | accepted |
| PWV21-REQ-023 | An `Execution Obligation` MUST remain derived/disposable and MUST NOT become a second canonical project-state store. | MUST | accepted |
| PWV21-REQ-024 | `obligation_id` MUST be deterministic/content-derived from the applicable rule, subject and relevant canonical fingerprint rather than random identity. | MUST | accepted |
| PWV21-REQ-025 | Obligation/result freshness fingerprints MUST cover only canonical inputs that materially determined the obligation, not the entire repository merely for convenience. | MUST | accepted |
| PWV21-REQ-026 | An `Execution Result` MUST contain only PW-relevant semantic result data: exact obligation/subject binding, result status/subject, changed artifacts or exact refs, tests/evidence/readback outcomes and any real blocker/semantic outcome required for continuation. | MUST | accepted |
| PWV21-REQ-027 | Provider/model/worker/session/retry/worktree/Paseo telemetry MUST remain outside canonical PW state and the canonical Obligation/Result contract. | MUST | accepted |
| PWV21-REQ-028 | Before accepting an Execution Result, PW MUST revalidate its exact obligation identity/fingerprint against current relevant canonical state. Stale results MUST be reconciled/re-routed rather than blindly accepted. | MUST | accepted |
| PWV21-REQ-029 | A stale result SHOULD be reused/rebased/reconciled when safety can be proven; re-execution is required only when reuse cannot be proven safe. | MUST | accepted |
| PWV21-REQ-030 | Unsupported breaking Obligation/Result schema versions MUST fail closed. | MUST | accepted |
| PWV21-REQ-031 | The kernel MUST emit expected canonical mutation preconditions/postconditions; the governed coordinator/role performs the write and mandatory readback/validation follows. | MUST | accepted |
| PWV21-REQ-032 | OR/Paseo MUST NOT directly mutate canonical PW durable state as a consequence of Card execution; it returns typed results for PW/coordinator validation and persistence. | MUST | accepted |
| PWV21-REQ-033 | Unknown completion of an external side effect after interruption MUST be read back/reconciled before retry; blind duplicate effects are forbidden. | MUST | accepted |

### Parallel Cards and execution ownership

| ID | Requirement | Priority | Status |
|---|---|---|---|
| PWV21-REQ-034 | PWv2.1 MAY execute multiple Cards concurrently inside one workstream only when accepted Plan/JIT authority explicitly declares a finite parallel-safe set. | MUST | accepted |
| PWV21-REQ-035 | The kernel MUST NOT infer Card parallelism solely from absence of dependency; Plan/JIT owns the explicit parallel-set declaration and rationale/inputs. | MUST | accepted |
| PWV21-REQ-036 | Kernel validation of a parallel set MUST cover Card dependencies, structured declared write scopes, external effect domains and relevant authority/scope overlap. | MUST | accepted |
| PWV21-REQ-037 | Card write scopes MUST be machine-checkable using repository paths/globs plus named external resources/effect domains; free text cannot be the sole concurrency basis. | MUST | accepted |
| PWV21-REQ-038 | Overlapping mutating write scopes MUST serialize; PWv2.1 MUST NOT provide a parallel-override escape hatch for overlapping mutation. | MUST | accepted |
| PWV21-REQ-039 | Uncertainty about independence MUST collapse execution to a safe serial route rather than guess. | MUST | accepted |
| PWV21-REQ-040 | Plan/JIT is the authority for parallel-set membership and each Card MAY belong to at most one active parallel set at a time. | MUST | accepted |
| PWV21-REQ-041 | A parallel set means Cards MAY overlap, not that they MUST launch simultaneously; legal subsets may start when their prerequisites are satisfied. | MUST | accepted |
| PWV21-REQ-042 | A blocked/RED Card MUST stop itself and dependent successors, not unrelated independent Cards, unless a shared gate/conflict invalidates the whole set. | MUST | accepted |
| PWV21-REQ-043 | OR/Paseo owns concrete scheduling, runtime concurrency count and execution isolation/worktrees for already-legal Cards; PW owns legality, not scheduling. | MUST | accepted |
| PWV21-REQ-044 | Every parallel Card MUST remain a separate PW Card with its own Obligation, Result, review subject and evidence. | MUST | accepted |
| PWV21-REQ-045 | One PW Card MUST have exactly one primary mutating Worker assignment. Parallel mutating ownership inside one Card is forbidden; genuinely parallel mutation must be represented as separate Cards. | MUST | accepted |
| PWV21-REQ-046 | A Card Worker MAY request bounded read-only/advisory helpers through OR, but helpers MUST NOT become additional mutating owners of that Card. | MUST | accepted |
| PWV21-REQ-047 | Workers MUST NOT recursively spawn their own subagents. Additional help is requested through OR/Main and realized as sibling helper capacity under the same Card boundary. | MUST | accepted |
| PWV21-REQ-048 | A new Card gets a fresh Worker assignment; the same Worker SHOULD persist through ordinary implementation repair loops for that Card and is closed/archived when the Card becomes terminal. | MUST | accepted |
| PWV21-REQ-049 | OR MAY replace a struggling Worker within the same Card when scope/authority do not change, without changing Card identity or PW authority. | MUST | accepted |
| PWV21-REQ-050 | Competing duplicate mutating Workers for the same Card are forbidden. Comparative read-only/advisory lanes MAY be used without creating competing mutation ownership. | MUST | accepted |
| PWV21-REQ-051 | If concurrent sibling work invalidates a Card's relevant base/read inputs, that result becomes stale/conflicted and MUST be reconciled/revalidated before integration. | MUST | accepted |
| PWV21-REQ-052 | Valid results from unaffected sibling Cards MUST be preserved when another Card blocks/REDs unless a concrete dependency/invalidation reaches them. | MUST | accepted |
| PWV21-REQ-053 | After parallel results are composed, PW MUST require a distinct integrated compatibility obligation before the first downstream obligation that consumes more than one sibling result. | MUST | accepted |
| PWV21-REQ-054 | Integrated compatibility review/check MUST NOT replace mandatory individual Card review and SHOULD preserve valid Card results when only bounded integration correction is needed. | MUST | accepted |
| PWV21-REQ-055 | Independent workstreams MAY progress concurrently; a blocker in one MUST NOT stop unrelated workstreams. | MUST | accepted |

### Independent review lifecycle

| ID | Requirement | Priority | Status |
|---|---|---|---|
| PWV21-REQ-056 | Every Project Workflow Card MUST receive independent review. | MUST | accepted |
| PWV21-REQ-057 | Every Milestone MUST receive a separate independent Milestone review. | MUST | accepted |
| PWV21-REQ-058 | Every completed workstream MUST receive a separate fresh final-integration review before close. | MUST | accepted |
| PWV21-REQ-059 | Review independence is subject-relative: any context/agent that materially produced or repaired the exact current subject MUST NOT issue its independent verdict. | MUST | accepted |
| PWV21-REQ-060 | Each new Card MUST receive a fresh independent Reviewer assignment distinct from reviewers of other Cards. | MUST | accepted |
| PWV21-REQ-061 | After Worker repair of the same Card, the same Card Reviewer MAY re-review the repaired subject if that Reviewer did not materially repair the subject. | MUST | accepted |
| PWV21-REQ-062 | If a Reviewer materially repairs the subject, its prior verdict no longer covers the changed subject and a fresh independent Reviewer is required. | MUST | accepted |
| PWV21-REQ-063 | A Milestone Reviewer MUST be fresh, MUST NOT have implemented or reviewed constituent Cards, and MUST NOT receive prior Card-review opinions/verdict rationales by default. | MUST | accepted |
| PWV21-REQ-064 | Milestone review receives the canonical Milestone subject, accepted authority, relevant Card outputs/artifacts and raw/required test evidence needed for independent verification. | MUST | accepted |
| PWV21-REQ-065 | The same Milestone Reviewer MAY recheck a repaired Milestone only if it did not materially produce/repair the changed subject. | MUST | accepted |
| PWV21-REQ-066 | The final-integration Reviewer MUST be fresh relative to Card/Milestone implementation/review and MUST evaluate the final subject from authority/raw evidence rather than prior GREEN opinions. | MUST | accepted |
| PWV21-REQ-067 | A Reviewer contaminated with Worker transcript/context does not satisfy a fresh-independent-review requirement. | MUST | accepted |
| PWV21-REQ-068 | An implementer MAY self-test but self-testing MUST NOT satisfy formal independent review. | MUST | accepted |
| PWV21-REQ-069 | A GREEN verdict without all required evidence is invalid. A required test that cannot run does not become deferred GREEN unless accepted authority already defines an alternate verification path. | MUST | accepted |
| PWV21-REQ-070 | Card RED MUST enter bounded automatic repair/re-review while the defect remains implementation-local and inside accepted scope; ordinary defects remain repair work of that Card rather than new Cards. | MUST | accepted |
| PWV21-REQ-071 | Repeated repair loops MUST be bounded. After the configured failure ceiling, Main analyzes the cause and escalates only if a real user-owned decision/blocker remains. | MUST | accepted |
| PWV21-REQ-072 | A previously GREEN Card MAY be reopened when new evidence invalidates it; a reopened Card gets a fresh Worker and fresh independent Reviewer. | MUST | accepted |
| PWV21-REQ-073 | When an earlier repair can invalidate downstream Cards, PW MUST mark the affected acceptance surface stale and revalidate only materially affected Cards/tests/reviews rather than replay all work. | MUST | accepted |
| PWV21-REQ-074 | Milestone-review corrections MUST route to identified existing Cards or bounded new Cards; they MUST NOT become unstructured global repair. | MUST | accepted |
| PWV21-REQ-075 | Final-integration RED MUST route automatically to bounded corrective work when product goal/scope remain unchanged; earlier GREEN Cards/Milestones may be invalidated only when evidence reaches them. | MUST | accepted |
| PWV21-REQ-076 | If OR/Paseo can automatically launch a qualifying fresh Reviewer, review freshness MUST NOT create a user stop. A fresh-context handoff is required only when the current runtime cannot satisfy the independence obligation. | MUST | accepted |

### Runtime behavior and handoff

| ID | Requirement | Priority | Status |
|---|---|---|---|
| PWV21-REQ-077 | PW MUST continue automatically while the next legal obligation is deterministic and already authorized; user stops are reserved for genuine product/strategy/authorization/input/blocker boundaries and existing premium gates. | MUST | accepted |
| PWV21-REQ-078 | Agent-findable uncertainty SHOULD be resolved through permitted tools/readback/Research rather than delegated to the user. | MUST | accepted |
| PWV21-REQ-079 | Normal user-facing progress SHOULD be concise and Card/workstream-level; worker-level telemetry/progress UI belongs entirely to OR/Paseo and is outside PWv2.1 scope. | MUST | accepted |
| PWV21-REQ-080 | Runtime choice is user-directed. Canonical PW state MUST NOT encode a preferred ChatGPT vs OR/Paseo runtime. | MUST | accepted |
| PWV21-REQ-081 | A single runtime-neutral locator-only handoff format MUST work for fresh ChatGPT and OR/Paseo and MUST contain only repository, branch/workstream, entry obligation and durable pointer plus any irreducible non-durable user intent. | MUST | accepted |
| PWV21-REQ-082 | Current canonical Git state MUST outrank stale handoff-prompt narrative. A receiving runtime must reconstruct truth from repo and continue without asking the user what to do when the route is deterministic. | MUST | accepted |
| PWV21-REQ-083 | Runtime switching SHOULD occur at durable boundaries; when requested earlier, the current runtime MUST first persist the smallest safe resumable state before handoff. | MUST | accepted |
| PWV21-REQ-084 | The user MAY switch ChatGPT and OR/Paseo repeatedly within one workstream without changing canonical Task Board semantics. | MUST | accepted |
| PWV21-REQ-085 | If OR/Paseo is unavailable but ChatGPT can legally perform the obligation, PW SHOULD continue without OR rather than block solely on runtime availability. | MUST | accepted |
| PWV21-REQ-086 | Loss of OR/Paseo sessions/private state MUST NOT prevent project recovery from canonical Git. Recovery MUST first look for reusable durable/observable completed results before replay. | MUST | accepted |
| PWV21-REQ-087 | Worker/reviewer model assignment is an OR runtime configuration and MUST remain fixed for the assignment; no silent model/provider fallback or automatic stronger-model escalation is allowed. | MUST | accepted |
| PWV21-REQ-088 | Exceptional use of a stronger/different model when the configured assignment is inadequate requires explicit user approval rather than silent substitution. | MUST | accepted |
| PWV21-REQ-089 | Runtime retry/session mechanics remain OR/Paseo-internal; PW sees semantic success/result or a real unresolved blocker, not retry telemetry. | MUST | accepted |
| PWV21-REQ-090 | Worker-proposed architecture/scope changes outside the current Card MUST return to the owning PW Planning/Definition/Brainstorming authority rather than being accepted by OR. | MUST | accepted |
| PWV21-REQ-091 | Tiny adjacent fixes MAY remain within a Card only when clearly inside its accepted goal/scope/risk; otherwise out-of-scope findings are surfaced for PW/JIT classification. | MUST | accepted |

### Recovery, migration and lifecycle continuity

| ID | Requirement | Priority | Status |
|---|---|---|---|
| PWV21-REQ-092 | Kernel/docs disagreement, helper/manual route disagreement, contradictory durable bindings or other unresolved mechanical ambiguity MUST fail closed to Recovery rather than be guessed. | MUST | accepted |
| PWV21-REQ-093 | Safe automatic Recovery SHOULD continue without user input and MAY be surfaced briefly without creating a stop. | MUST | accepted |
| PWV21-REQ-094 | Recovery MUST follow an already accepted Plan/authority choice without re-asking the user; purely technical equivalent choices may be made automatically, while product/strategy alternatives return to the user. | MUST | accepted |
| PWV21-REQ-095 | Research that invalidates planning strategy but not accepted product intent MUST return automatically to Planning; Research requiring product-goal change returns to the user-owned Definition/Brainstorming boundary. | MUST | accepted |
| PWV21-REQ-096 | PWv2 -> PWv2.1 migration SHOULD be lazy/on-entry at natural durable boundaries rather than a flag-day migration of all projects. | MUST | accepted |
| PWV21-REQ-097 | Unambiguous active PWv2 workstreams SHOULD continue under PWv2.1 after validating authority, subject and evidence bindings; ambiguous legacy state MUST fail closed to Recovery. | MUST | accepted |
| PWV21-REQ-098 | Historical PWv2 GREEN remains valid when its exact subject/evidence still proves the result. Missing newly required evidence triggers bounded revalidation only when material and MUST NOT retroactively label the historical result RED. | MUST | accepted |
| PWV21-REQ-099 | New PWv2.1 review semantics apply to continued active work but MUST NOT automatically reopen correctly closed historical stages. Missing historical Milestone review is backfilled only when material to active continuation. | MUST | accepted |
| PWV21-REQ-100 | Migration MAY add fields only when values are uniquely derivable from canonical legacy state; values requiring interpretation/user choice MUST route to Recovery or the owning user gate. | MUST | accepted |
| PWV21-REQ-101 | Migration MUST preserve history and perform minimal normalization; valid old-format results SHOULD be adapted into the new contract rather than rejected for age/serialization alone. | MUST | accepted |
| PWV21-REQ-102 | Safe mechanical migration MUST NOT create a user stop; contradictions among legacy manifest/Task Board/Git state MUST fail closed rather than choose the most probable source. | MUST | accepted |
| PWV21-REQ-103 | Migration acceptance MUST exercise real-derived PWv2 workstreams in multiple lifecycle states and prove correct PWv2.1 continuation/recovery. | MUST | accepted |
| PWV21-REQ-104 | Independent work unaffected by an ambiguous migration/recovery path MAY continue; only dependent paths are blocked. | MUST | accepted |
| PWV21-REQ-105 | Workstream close MUST require GREEN final integration review plus all required acceptance evidence. | MUST | accepted |
| PWV21-REQ-106 | User Stops MUST state what happened, what the durable state means, and the smallest exact next action. Authorization stops SHOULD provide a ready short approval phrase; optional/mandatory handoffs MUST follow the applicable V2 ready-to-copy locator contract. | MUST | accepted |
| PWV21-REQ-107 | After user-supplied authorization/input, the router MUST immediately re-evaluate durable state and continue all deterministic authorized transitions until the next real stop. | MUST | accepted |

## Constraints

- Canonical project/workflow truth remains repository-backed; no runtime/session database becomes authority.
- PWv2.1 targets the current `elmakus/project_workflow_v2` architecture and should evolve it rather than recreate V1 policy splits.
- OR/Paseo remains a separate runtime/orchestration product; PW defines legal obligations and semantic acceptance, not runtime topology.
- The policy kernel must remain small and YAGNI-driven.
- Exact authority refs outrank summaries.
- Review independence is relative to the exact subject, not runtime product identity.
- Product/strategy/scope changes remain human-owned.
- Existing V2 premium A/B/C planning boundaries remain applicable unless separately changed by accepted authority.

## Non-goals

- Building a general workflow programming language.
- Moving semantic product/strategy/review judgment into deterministic code.
- Making OR/Paseo, worker sessions, worktrees, retries, provider/model identity or telemetry canonical PW state.
- Hiding multiple mutating owners inside one Card.
- Allowing overlapping mutating Card scopes to execute concurrently.
- Replacing individual Card review with integration/compatibility review.
- Requiring the Python helper to recover a project.
- Rewriting historical PWv2 state wholesale during migration.
- Automatically changing worker/reviewer models because a task looks difficult.
- Making worker telemetry/progress UI a PWv2.1 concern.

## Definition completeness statement

The promoted Brainstorming completion audit reports no unresolved material product/strategic decisions and no Research need. This Definition preserves all later supersessions: one primary mutating Worker per Card; no silent model switching; no compatibility-review substitution for Card review; no mutating write-scope overlap override; worker telemetry outside PW; helper-less canonical recovery mandatory.
