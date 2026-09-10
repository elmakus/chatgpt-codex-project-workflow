# Context Routing

## Purpose

Progressive disclosure reduces the amount an agent reads for a particular task while preserving the complete workflow contract.

**Agent reads less at a given stage. Workflow contains no fewer rules.**

The default start sequence is:

1. workflow `CHATGPT.md` or `prompts/CODEX_START.md`, as appropriate;
2. project root `PROJECT.md`;
3. this routing document;
4. phase-specific workflow modules;
5. only the project artifacts and contracts required by the current task.

Do not load the entire workflow or entire project merely because it is available.

## Authority before routing

Before interpreting project content, apply `workflow/contracts/PROJECT_REPOSITORY.md#authority-and-conflicts`.

In particular:
- accepted decisions and canonical requirements outrank brainstorming notes;
- the approved plan outranks abandoned planning alternatives;
- current Task Board / Task Card / Git state govern execution state;
- a cumulative handoff records what became true at a completed milestone;
- local convenience checkpoints never outrank durable repository state.

## BRAINSTORMING

Read primarily:
- `workflow/BRAINSTORMING.md`;
- project `PROJECT.md`;
- current `brainstorming/` notes;
- relevant accepted `decisions/`;
- open questions.

Usually do not load:
- Task Cards;
- the full GitHub State Contract;
- all OpenSpec changes;
- all milestone handoffs;
- implementation evidence.

Load one of those only when the current brainstorming question genuinely depends on it.

## RESEARCH

Read:
- `workflow/RESEARCH.md`;
- project `PROJECT.md`;
- the current research question / relevant `research/` notes;
- relevant `requirements/`;
- relevant accepted `decisions/`;
- only the source material needed for the question.

Do not read the full project history by default.

## PLANNING

Read:
- `workflow/PLANNING.md`;
- project `PROJECT.md`;
- canonical `requirements/`;
- relevant verified `research/`;
- accepted `decisions/`;
- the existing approved plan or plan draft being revised.

Load Task Card/OpenSpec execution contracts only when planning has reached execution decomposition.

## EXECUTION PREP

Read:
- `workflow/EXECUTION_PREP.md`;
- project `PROJECT.md`;
- canonical requirements and approved Master Plan;
- current milestone;
- latest cumulative handoff;
- `workflow/contracts/TASK_CARDS.md`;
- `workflow/contracts/OPENSPEC.md`;
- `workflow/contracts/GITHUB_STATE.md`;
- relevant current source state.

## EXECUTION

Read:
- `workflow/EXECUTION.md`;
- project `PROJECT.md`;
- Task Board;
- current milestone;
- current Task Card;
- latest cumulative handoff;
- relevant OpenSpec;
- relevant Master Plan sections;
- relevant source locations;
- execution contracts referenced by `workflow/EXECUTION.md`.

Do not automatically load unrelated historical cards, all research, or all OpenSpec archives.

## STRATEGIC BLOCKER

Read:
- project `PROJECT.md`;
- `workflow/contracts/CHATGPT_CODEX.md`;
- the specific blocker record and exact referenced commit;
- current Task Card and relevant Task Board state;
- only the accepted decisions, requirements, OpenSpec sections, source and research needed to decide the blocker.

A strategic blocker does not justify loading all project history.

## MILESTONE REVIEW / CLOSE

Read:
- `workflow/REVIEW_AND_HANDOFF.md`;
- project `PROJECT.md`;
- Task Board and current milestone;
- required card results;
- acceptance evidence;
- relevant OpenSpec;
- relevant Git/PR state;
- prior cumulative handoff when needed to make the new handoff cumulative.

## FAILURE RECOVERY

Read:
- project `PROJECT.md`;
- exact remote/local branch and HEAD;
- Task Board;
- any `in_progress` or `blocked` card;
- latest cumulative handoff;
- relevant OpenSpec task state;
- test/evidence pointers and result fields.

A local `current.md` may be read as a convenience hint if present, but recovery must succeed without it.
