# Migration Audit — v2.1 → v3

This audit treats the entire supplied v2.1 ZIP as the normative baseline. The v3 migration prompt is authoritative only where it explicitly changes v2.1.

## Source manifest read in full

- `00_ALL_IN_ONE_v2.1.md` — 1872 lines
- `01_LLM_PROJECT_WORKFLOW_v2.1.md` — 1249 lines
- `02_CHATGPT_START_PROMPT_v2.1.md` — 141 lines
- `03_CODEX_START_PROMPT_v2.1.md` — 246 lines
- `04_DIRECT_CHATGPT_CODEX_PROTOCOL_v2.1.md` — 105 lines
- `05_GITHUB_STATE_CONTRACT_v2.1.md` — 109 lines
- `README.md` — 21 lines
- `CHANGELOG.md` — 24 lines

All eight files were read completely before v3 was finalized. `00_ALL_IN_ONE_v2.1.md` is an aggregate duplication of the standalone workflow/prompt/protocol/state-contract files; its embedded blocks are mapped explicitly below, and the standalone files carry the per-section detail.

## Status definitions

- `RETAINED` — same normative behavior remains explicitly present.
- `MOVED` — behavior is preserved in a different v3 file/section.
- `MERGED` — duplicated or cross-cutting v2.1 material is represented by one or more canonical v3 modules without semantic deletion.
- `SUPERSEDED_BY_NEW_DECISION` — the v3 migration prompt explicitly changes the old rule; unaffected semantics are still preserved.
- `REMOVED_WITH_JUSTIFICATION` — permitted only for contradiction or fully redundant semantics. **No item required this status.**

## Migration matrix

| Source file | Source section / contract | Status | Destination | Destination section | Explanation |
|---|---|---|---|---|---|
| 00_ALL_IN_ONE_v2.1.md | Bundle wrapper / complete embedded workflow | MERGED | MIGRATION_AUDIT_v2.1_to_v3.md | Detailed mappings for 01–05 | The all-in-one file duplicates the normative component files; every embedded workflow section is covered by the 01 mapping below and no independent rule is dropped. |
| 00_ALL_IN_ONE_v2.1.md | Embedded CHATGPT START PROMPT | MERGED | prompts/CHATGPT_START.md + phase/contracts | Whole prompt | Prompt behavior is routed through v3 modules instead of duplicating the workflow in a long start prompt. |
| 00_ALL_IN_ONE_v2.1.md | Embedded CODEX START PROMPT | MERGED | prompts/CODEX_START.md + workflow/EXECUTION.md + contracts | Whole prompt | Execution instructions are preserved modularly and the start prompt is intentionally short. |
| 00_ALL_IN_ONE_v2.1.md | Embedded DIRECT CHATGPT ↔ CODEX protocol | MERGED | workflow/contracts/CHATGPT_CODEX.md | Strategic escalation | Same correlation/persistence contract; detailed source mapping is under file 04. |
| 00_ALL_IN_ONE_v2.1.md | Embedded GITHUB STATE CONTRACT | MERGED | workflow/contracts/GITHUB_STATE.md | Whole contract | Same state/result/milestone/recovery semantics; detailed source mapping is under file 05. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 0. Status tej specyfikacji | MERGED | CHANGELOG.md + workflow/contracts/CHATGPT_CODEX.md + PROJECT_REPOSITORY.md | v3 history / channel model / durable-state rules | v2.1 lessons are preserved; project-topology defaults are replaced only where v3 explicitly changes them. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 1. Cel workflow | MERGED | README.md + phase modules + contracts | Core model | Goals such as reduced context bloat, durable state, verified done, and no user-as-bus are preserved across modular documents. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 2. Główna architektura | SUPERSEDED_BY_NEW_DECISION | README.md + workflow/contracts/PROJECT_REPOSITORY.md + CHATGPT_CODEX.md | Core model / responsibilities | v2.1's implementation-repo-first diagram is replaced by one project repo from brainstorming; GitHub/chat/Codex semantics remain. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 3.1 ChatGPT — strategic planner / decision layer | MOVED | workflow/contracts/CHATGPT_CODEX.md | Responsibilities / ChatGPT | Role and authority preserved. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 3.2 Codex — implementation orchestrator | MOVED | workflow/contracts/CHATGPT_CODEX.md + CODEX_ORCHESTRATION.md | Responsibilities / Codex | Execution/orchestration responsibilities preserved and event-driven coordination made explicit. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 3.3 GitHub / implementation repository — durable source of truth | SUPERSEDED_BY_NEW_DECISION | workflow/contracts/PROJECT_REPOSITORY.md | One project = one repository / durable state | The implementation repository concept becomes the broader project repository from first idea; durable Git semantics preserved. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 3.4 ChatGPT chat — control plane | MOVED | workflow/contracts/CHATGPT_CODEX.md | GitHub and chat | Chat remains strategic transport/control, not durable truth. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 4. Hierarchia projektu | MERGED | workflow/PLANNING.md + TASK_CARDS.md + OPENSPEC.md | Milestones / Task Card meaning / OpenSpec role | Project→milestone→card→OpenSpec-task hierarchy is preserved without a duplicate diagram. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 5. Master Plan | MOVED | workflow/PLANNING.md + templates/MASTER_PLAN.md | Master Plan | All listed plan contents and non-task-tracker rule are retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 6. Task Decomposition Policy | MOVED | workflow/contracts/TASK_CARDS.md + templates/TASK_CARD.md | Required fields | Metadata, scope, acceptance, tests, refs, Refresh Gate and DoD retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 7. Rozdzielenie decision state i execution state | MOVED | workflow/contracts/GITHUB_STATE.md + TASK_CARDS.md | Card execution states / status model | Exact decision/execution separation and controlled values retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 7. Milestone execution state | MOVED | workflow/contracts/GITHUB_STATE.md | Milestone execution lifecycle | planned→ready→in_progress→done plus blocked/superseded rules retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 8. TASK_BOARD.yaml | MOVED | workflow/contracts/GITHUB_STATE.md + templates/TASK_BOARD.yaml | Task Board / result pointers | Live-index role, fields, lifecycle and result-pointer contract retained with v3 paths. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 8. Result-pointer contract | RETAINED | workflow/contracts/GITHUB_STATE.md | Done-card result pointer contract | `result_commit`, `result_pr`, `evidence` semantics are explicitly preserved. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 9. Definition of Done | RETAINED | workflow/contracts/TASK_CARDS.md + GITHUB_STATE.md | Definition of Done | All twelve semantic conditions are represented; phrasing is reorganized only. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 10. Task Card — rekomendowany format | MOVED | templates/TASK_CARD.md | Whole template | Neutral v3 template replaces project-specific example while keeping the contract. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 11. Refresh Gate | RETAINED | workflow/EXECUTION.md + workflow/contracts/TASK_CARDS.md | Refresh Gate | Inputs and implementation-detail-vs-strategic-drift rule preserved. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 12. OpenSpec Policy | RETAINED | workflow/contracts/OPENSPEC.md | Selective policy | Required/skip categories preserved and expanded only by new prompt wording. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 13. OpenSpec just-in-time | RETAINED | workflow/contracts/OPENSPEC.md | Candidate/JIT reconciliation/standard flow | JIT creation against current code/handoff/card/plan/dependencies and proposal/specs/design/tasks/apply/verify/archive preserved. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 14. Strategic Communication Protocol | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Strategic blocker lifecycle | Full request/decision/correlation/persistence contract retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 14.2 Chat nie jest source of truth | RETAINED | workflow/contracts/CHATGPT_CODEX.md | GitHub and chat / decision persistence | Chat remains transport; accepted decision must become durable project state. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 14.3 Format strategic request | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Request format | Unique `request_id`, evidence commit/path, options, recommendation and response instruction retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 14.4 Format odpowiedzi ChatGPT | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Decision format | Matching ID plus exact `DECISION FOR CODEX:` marker retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 14.5 Ochrona przed błędną interpretacją | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Parsing and correlation rule | Latest-reply-only interpretation remains forbidden; blocked state retained on mismatch. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 14.6 Persist decision | MOVED | workflow/contracts/CHATGPT_CODEX.md + templates/DECISION.md | Decision persistence / provenance | All provenance fields retained; path moves to top-level decisions/ under v3 knowledge-state rule. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 15. Direct message vs GitHub evidence | MOVED | workflow/contracts/CHATGPT_CODEX.md | GitHub and chat / Request format | Large durable payloads stay in Git; chat contains concise pointer/options/recommendation. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 16. GitHub repository layout — default implementation repo | SUPERSEDED_BY_NEW_DECISION | workflow/contracts/PROJECT_REPOSITORY.md | Canonical project layout | Paths change to v3 knowledge-state layout and project repo exists from brainstorming; execution artifact semantics retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 16. Legacy split-repo model | SUPERSEDED_BY_NEW_DECISION | workflow/contracts/PROJECT_REPOSITORY.md | Legacy split-repository migration | Split repo is now a user-approved exception; exact ownership and green-boundary safety remain. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 17. Codex — algorytm wykonania | MOVED | workflow/EXECUTION.md + GITHUB_STATE.md | Standard card loop | READY selection, recovery, refresh, OpenSpec, implementation, verification, result persistence, next-card loop and milestone gate retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 18. Dependency handling | RETAINED | workflow/contracts/TASK_CARDS.md | Dependency handling | Explicit dependencies without generic DAG engine retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 19. Milestone completion | RETAINED | workflow/REVIEW_AND_HANDOFF.md + GITHUB_STATE.md | Milestone completion / GREEN | All-cards-done is insufficient; RED corrective work and GREEN durable close retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 20. Cumulative Handoff | MOVED | workflow/REVIEW_AND_HANDOFF.md + templates/HANDOFF.md | Cumulative handoff | All listed handoff content is retained; path becomes top-level `project-handoffs/` by v3 decision. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 21. Strategic blocker lifecycle | MOVED | workflow/contracts/CHATGPT_CODEX.md | Strategic blocker lifecycle | Lifecycle is preserved in normative prose. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 22. ChatGPT cannot send by Codex session UUID — design consequence | MOVED | workflow/contracts/CHATGPT_CODEX.md | Channel asymmetry | Proven/fallback asymmetric model retained without making future product capabilities a permanent invariant. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 23. Requirement coverage | RETAINED | workflow/PLANNING.md | Requirement coverage | Owner milestone, at least one Task Card and OpenSpec when required are preserved. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 24. Research workflow | MOVED | workflow/RESEARCH.md + workflow/PLANNING.md | Research workflow | Discovery→verification→alternatives→decisions→requirements→planning sequence preserved with clearer promotion boundaries. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 25. Audit przed implementacją | RETAINED | workflow/PLANNING.md + workflow/EXECUTION_PREP.md | Pre-implementation planning audit | All audit topics retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 26. Cards z wyprzedzeniem | RETAINED | workflow/contracts/TASK_CARDS.md + workflow/PLANNING.md | Near-term versus distant cards | Detailed near term, functionally precise distant work, and Refresh Gate retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 27. Context minimization | SUPERSEDED_BY_NEW_DECISION | workflow/CONTEXT_ROUTING.md | Phase routes | v2.1 execution-only context minimization becomes phase-aware progressive disclosure without deleting contracts. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 27. Lokalny task checkpoint current.md | RETAINED | workflow/contracts/PROJECT_REPOSITORY.md + GITHUB_STATE.md + workflow/EXECUTION.md | Durable vs local convenience / recovery | Optional local checkpoint remains non-canonical and unnecessary for recovery. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 28. One canonical home | SUPERSEDED_BY_NEW_DECISION | workflow/contracts/PROJECT_REPOSITORY.md | Knowledge states / authority | Single project repo remains canonical, but v3 deliberately separates knowledge states into explicit top-level domains. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 29. Branch / PR policy | RETAINED | workflow/contracts/PROJECT_REPOSITORY.md + REVIEW_AND_HANDOFF.md | Git and branch policy / finalization | Isolation, coherent commits, shared milestone PR, integrated acceptance, post-merge handoff and green checkpoint retained. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 30. User interaction policy | RETAINED | workflow/contracts/CHATGPT_CODEX.md | User interaction policy | User makes decisions rather than transporting workflow state. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 31. Fresh context policy | SUPERSEDED_BY_NEW_DECISION | workflow/CONTEXT_ROUTING.md + templates/PROJECT.md | Execution / project router | v3 adds PROJECT.md and phase routing while retaining exact Git/handoff/Task Board/card/OpenSpec recovery inputs. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 32. Failure recovery | RETAINED | workflow/EXECUTION.md + workflow/contracts/GITHUB_STATE.md | Failure recovery | Recover same in-progress card, inspect Git/OpenSpec/tests/result pointers, no silent advance, no current.md dependency. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 33. Anti-overengineering | RETAINED | workflow/contracts/CODEX_ORCHESTRATION.md + TASK_CARDS.md | No orchestration overengineering / dependencies | Task DB, Jira clone, broker, generic DAG, message service/vector DB/workflow-engine prohibitions are retained semantically. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 34. Minimalny zestaw plików | SUPERSEDED_BY_NEW_DECISION | workflow/contracts/PROJECT_REPOSITORY.md | Canonical project layout | v3 new state-separated layout replaces docs/implementation paths. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 35. Pełny lifecycle | MERGED | workflow/BRAINSTORMING.md; RESEARCH.md; PLANNING.md; EXECUTION_PREP.md; EXECUTION.md; REVIEW_AND_HANDOFF.md | Phase lifecycle | All phases from discovery through cutover remain representable and are routed modularly. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 35.1 Migracja istniejącego projektu ze split-repo | SUPERSEDED_BY_NEW_DECISION | workflow/contracts/PROJECT_REPOSITORY.md | Legacy split-repository migration | New projects never use central split workspaces by default; legacy migration still waits for green boundary and preserves pointer/provenance. |
| 01_LLM_PROJECT_WORKFLOW_v2.1.md | 36. Fundamentalna zasada v2.1 | MERGED | README.md + CHATGPT_CODEX.md + TASK_CARDS.md + OPENSPEC.md + GITHUB_STATE.md + REVIEW_AND_HANDOFF.md | Core model | Strategic/implementation/spec/Git/board/card/handoff/test/user roles remain explicitly recoverable. |
| 02_CHATGPT_START_PROMPT_v2.1.md | Twoja rola | MOVED | workflow/contracts/CHATGPT_CODEX.md | Responsibilities / ChatGPT | Research/planning/review/blocker-decision role retained. |
| 02_CHATGPT_START_PROMPT_v2.1.md | Shared-state model | SUPERSEDED_BY_NEW_DECISION | workflow/contracts/PROJECT_REPOSITORY.md + CHATGPT_CODEX.md | One project repo / GitHub and chat | Implementation-repo-only start becomes project repo from brainstorming; durable-state, chat-control and request_id semantics retained. |
| 02_CHATGPT_START_PROMPT_v2.1.md | Planning workflow | MERGED | workflow/BRAINSTORMING.md + RESEARCH.md + PLANNING.md + EXECUTION_PREP.md + templates | Planning phases | Fact/decision/assumption split, research, architecture freeze, Master Plan fields, cards, state model, OpenSpec, handoff, context and anti-overengineering retained. |
| 02_CHATGPT_START_PROMPT_v2.1.md | Strategic decision response protocol | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Decision format / correlation | Read evidence, research if needed, exact request_id + marker and durable-artifact update behavior retained. |
| 02_CHATGPT_START_PROMPT_v2.1.md | Do not create Task Cards/OpenSpec at new-project start | RETAINED | workflow/BRAINSTORMING.md + prompts/CHATGPT_START.md | Exit/initialization rules | New project starts with discovery/brainstorming/research, not fabricated execution artifacts. |
| 02_CHATGPT_START_PROMPT_v2.1.md | Aktualny projekt/problem placeholder | SUPERSEDED_BY_NEW_DECISION | prompts/CHATGPT_START.md + templates/PROJECT.md | Short existing/new-project commands | Free-text placeholder is replaced by repo+PROJECT.md routing; no workflow behavior is lost. |
| 03_CODEX_START_PROMPT_v2.1.md | Źródła prawdy | SUPERSEDED_BY_NEW_DECISION | workflow/contracts/PROJECT_REPOSITORY.md + CHATGPT_CODEX.md | Authority / GitHub and chat | Project repo from brainstorming replaces implementation-repo framing; repo over stale chat and explicit ownership semantics retained. |
| 03_CODEX_START_PROMPT_v2.1.md | Na początku | MERGED | workflow/EXECUTION.md + CONTEXT_ROUTING.md + prompts/CODEX_START.md | Standard card loop / EXECUTION | Repo/branch/HEAD, Task Board, handoff, milestone, recover in_progress, READY selection and minimal context retained. |
| 03_CODEX_START_PROMPT_v2.1.md | Refresh Gate | RETAINED | workflow/EXECUTION.md + TASK_CARDS.md | Refresh Gate | Exact strategic-vs-implementation drift rule retained. |
| 03_CODEX_START_PROMPT_v2.1.md | Każda Task Card | MERGED | workflow/EXECUTION.md + TASK_CARDS.md + OPENSPEC.md + GITHUB_STATE.md | Card loop / DoD / JIT | All twelve execution steps preserved modularly. |
| 03_CODEX_START_PROMPT_v2.1.md | Metadata Task Cards | RETAINED | workflow/contracts/TASK_CARDS.md + GITHUB_STATE.md | Required fields / statuses | State values and metadata retained. |
| 03_CODEX_START_PROMPT_v2.1.md | Strategic escalation — stop dependent work | RETAINED | workflow/contracts/CHATGPT_CODEX.md + GITHUB_STATE.md | Strategic blocker lifecycle | Blocked state and dependency stop retained. |
| 03_CODEX_START_PROMPT_v2.1.md | Strategic escalation — persist blocker evidence | MOVED | templates/BLOCKER.md + workflow/contracts/CHATGPT_CODEX.md | Blocker lifecycle | Finding/evidence/source/impact/options/recommendation/green-state requirements retained with v3 path. |
| 03_CODEX_START_PROMPT_v2.1.md | Strategic escalation — commit/push before request | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Strategic blocker lifecycle | Safe durable evidence before request remains normative. |
| 03_CODEX_START_PROMPT_v2.1.md | Strategic escalation — request/read/marker/request_id | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Request/decision/correlation | Exact structured exchange semantics retained. |
| 03_CODEX_START_PROMPT_v2.1.md | Strategic escalation — persist/reconcile/resume | RETAINED | workflow/contracts/CHATGPT_CODEX.md + templates/DECISION.md | Decision persistence | Durable decision, artifact reconciliation and resume only after resolution retained. |
| 03_CODEX_START_PROMPT_v2.1.md | Ważna asymetria kanału | MOVED | workflow/contracts/CHATGPT_CODEX.md | Channel asymmetry | Codex-initiated post/reply/read model retained. |
| 03_CODEX_START_PROMPT_v2.1.md | Milestone completion | RETAINED | workflow/REVIEW_AND_HANDOFF.md + GITHUB_STATE.md | Milestone completion | Integrated acceptance, corrective work, finalization, handoff, evidence, checkpoint, head and milestone done retained. |
| 03_CODEX_START_PROMPT_v2.1.md | Context minimization | SUPERSEDED_BY_NEW_DECISION | workflow/CONTEXT_ROUTING.md | EXECUTION / failure recovery | v3 phase routing generalizes the same minimal execution package; current.md remains optional. |
| 03_CODEX_START_PROMPT_v2.1.md | Cel | MERGED | workflow/EXECUTION.md + CHATGPT_CODEX.md | Standard loop / user interaction | Card-to-card durable execution without user as message bus remains. |
| 04_DIRECT_CHATGPT_CODEX_PROTOCOL_v2.1.md | Empirycznie potwierdzony model | MOVED | workflow/contracts/CHATGPT_CODEX.md | Channel asymmetry | Codex-post → ChatGPT-reply → correlated read behavior is retained as proven/fallback interaction model. |
| 04_DIRECT_CHATGPT_CODEX_PROTOCOL_v2.1.md | Cel protokołu | RETAINED | workflow/contracts/CHATGPT_CODEX.md | When to use strategic escalation | Strategic blockers/approval/options/research/plan-change only; not routine state transport. |
| 04_DIRECT_CHATGPT_CODEX_PROTOCOL_v2.1.md | Durable evidence | RETAINED | workflow/contracts/CHATGPT_CODEX.md | GitHub and chat / blocker lifecycle | Evidence is persisted before request; chat holds a pointer. |
| 04_DIRECT_CHATGPT_CODEX_PROTOCOL_v2.1.md | Request format | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Request format | Fields and marker instruction preserved. |
| 04_DIRECT_CHATGPT_CODEX_PROTOCOL_v2.1.md | Decision format | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Decision format | Exact same request_id plus DECISION FOR CODEX marker preserved. |
| 04_DIRECT_CHATGPT_CODEX_PROTOCOL_v2.1.md | Parsing rule | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Parsing and correlation rule | Arbitrary/latest text is not accepted; mismatch remains blocked; bounded wait/retry preserved. |
| 04_DIRECT_CHATGPT_CODEX_PROTOCOL_v2.1.md | Persistence rule | RETAINED | workflow/contracts/CHATGPT_CODEX.md | Decision persistence | Chat transport vs GitHub durable truth preserved. |
| 05_GITHUB_STATE_CONTRACT_v2.1.md | 1. Kanoniczny repo model | SUPERSEDED_BY_NEW_DECISION | workflow/contracts/PROJECT_REPOSITORY.md + GITHUB_STATE.md | Canonical project layout | Execution state remains in same project repo, but the repo starts at brainstorming and paths are state-separated. |
| 05_GITHUB_STATE_CONTRACT_v2.1.md | 2. Co aktualizować przy starcie karty | RETAINED | workflow/contracts/GITHUB_STATE.md | Starting a card | Card and milestone transitions plus material Refresh Gate note retained. |
| 05_GITHUB_STATE_CONTRACT_v2.1.md | 3. Co aktualizować po zakończeniu karty | RETAINED | workflow/contracts/GITHUB_STATE.md | Done-card result pointer contract | Exact state/result fields and evidence specificity retained. |
| 05_GITHUB_STATE_CONTRACT_v2.1.md | 4. Co aktualizować przy blockerze | RETAINED | workflow/contracts/GITHUB_STATE.md + CHATGPT_CODEX.md | Blocked card | Blocked state, evidence, safe commit, request_id, decision record, reconcile/resume retained. |
| 05_GITHUB_STATE_CONTRACT_v2.1.md | 5. Co aktualizować przy milestone GREEN | RETAINED | workflow/contracts/GITHUB_STATE.md | Milestone GREEN | Finalization, handoff, evidence, implementation_head, checkpoint and milestone done retained. |
| 05_GITHUB_STATE_CONTRACT_v2.1.md | 6. Lokalny current.md | RETAINED | workflow/contracts/PROJECT_REPOSITORY.md + GITHUB_STATE.md | Durable state versus local convenience | All non-canonical/recovery constraints retained. |
| 05_GITHUB_STATE_CONTRACT_v2.1.md | 7. Repo migration rule | SUPERSEDED_BY_NEW_DECISION | workflow/contracts/PROJECT_REPOSITORY.md | Legacy split-repository migration | v3 new-project topology changes, but active-milestone freeze and green-boundary migration remain. |
| README.md | Bundle purpose and file inventory | SUPERSEDED_BY_NEW_DECISION | README.md | Whole document | ZIP bundle inventory is obsolete once repository `main` is canonical; v3 README explains repository workflow and use. |
| README.md | v2.1 key changes summary | MERGED | README.md + CHANGELOG.md + contracts | Core model/history | Result-pointer, milestone-close and green-boundary safety remain documented. |
| CHANGELOG.md | v2.1 history | RETAINED | CHANGELOG.md | v2.1 | Historical change list is retained, with a note where v3 supersedes topology/path defaults. |
| CHANGELOG.md | v2 history | RETAINED | CHANGELOG.md | v2 | Historical v2 change list is retained. |

## Coverage of explicit v3 decisions from the migration prompt

The following items are new/superseding v3 decisions rather than inventions inferred from v2.1:

- Workflow repository contains workflow only; project workspaces/data are forbidden there → `PROJECT_REPOSITORY.md`.
- One project gets one repository from first brainstorming → `PROJECT_REPOSITORY.md`.
- Explicit project knowledge-state split (`brainstorming/`, `decisions/`, `research/`, `requirements/`, `planning/`, `implementation/`, `project-handoffs/`, `openspec/`) → `PROJECT_REPOSITORY.md` and templates.
- `PROJECT.md` as the project entrypoint/router → `PROJECT_REPOSITORY.md`, `templates/PROJECT.md`.
- Phase-aware progressive disclosure → `CHATGPT.md`, `workflow/CONTEXT_ROUTING.md` and phase modules.
- Small global `CHATGPT.md` router; current workflow `main` outranks stale memory/prompts/ZIPs → root `CHATGPT.md`.
- Workflow `main` as sole post-v3 workflow authority → `CHATGPT.md`, `README.md`.
- Codex bounded multi-agent/event-driven/no-routine-polling coordination → `workflow/contracts/CODEX_ORCHESTRATION.md`.
- Mandatory migration audit and second semantic audit → this file and `SEMANTIC_AUDIT_v3.md`.
- Short normal ChatGPT prompts with no required skill/Custom GPT/Work dependency → `prompts/CHATGPT_START.md`.

## Explicitly superseded topology/path decisions

v3 intentionally changes only these topology-related v2.1 assumptions:

1. The repository is no longer conceptualized as an implementation repository that becomes authoritative around execution. It is the **project repository from the first brainstorming**.
2. Project knowledge no longer defaults to `docs/implementation/...`; it is separated by knowledge state at project root.
3. A separate planning/control repo is not merely an allowed default alternative. It is now an exceptional topology requiring technical justification and an explicit user decision.
4. `docs/project-handoffs/` becomes `project-handoffs/` in the v3 canonical layout.
5. Strategic decisions that v2.1 placed under `docs/implementation/decisions/` become top-level accepted `decisions/`, preserving provenance and request correlation.

The v2.1 green-boundary rule for changing an existing split-repo topology is retained for future migrations; v3 itself does not migrate any existing project.

## Migration totals

- RETAINED: **42**
- MOVED: **20**
- MERGED: **15**
- SUPERSEDED_BY_NEW_DECISION: **16**
- REMOVED_WITH_JUSTIFICATION: **0**
- Total mapped items: **93**
- Unmapped significant items: **0**

## Audit conclusion

Every standalone v2.1 source file and every significant normative section/contract is mapped. The aggregate all-in-one file is also mapped and cross-referenced to its standalone duplicates. No behavior was removed merely to shorten documentation. Items marked `SUPERSEDED_BY_NEW_DECISION` are limited to repository topology, path/authority routing and context-loading decisions explicitly changed by the v3 migration prompt.
