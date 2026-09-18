# Brainstorming

## Goal

Explore the problem space without accidentally converting possibilities into requirements or decisions.

## Canonical location

Project brainstorming lives in `brainstorming/`.

Use `templates/BRAINSTORM.md` for substantial sessions and `templates/OPEN_QUESTIONS.md` for unresolved questions when those templates are useful.

## Non-negotiable distinction

**BRAINSTORMING != DECISION.**

Brainstorming may contain:
- ideas;
- alternatives;
- hypotheses;
- experiments;
- pros/cons;
- assumptions to verify;
- rejected or merely considered directions.

Nothing in `brainstorming/` becomes authoritative merely because it was written down or discussed repeatedly.

When the user explicitly accepts a choice, preserve that acceptance and route it through Project Definition so canonical requirements/decision authority is reconciled in one place. Do not make Brainstorming a second requirements/planning writer.

Do not rewrite history to make old brainstorming look settled.

## Working method

1. Clarify the problem, current state, target state and constraints.
2. Separate known facts, user decisions, assumptions and implementation-time choices.
3. Identify open questions and research needs.
4. Compare options only at the level justified by current evidence.
5. Delay freezing architecture until adequate verification exists.
6. Persist useful tentative work in the project repository so chat length is not project memory.

Read only already accepted requirements/decisions and source/project context that actually constrain the exploration. Do not load implementation-state machinery unless the question depends on current execution state.

## Exit conditions

Move to research when claims require verification.

Move to Project Definition when enough facts and accepted choices exist to formalize authoritative requirements/decisions and target state.

Do not create implementation Task Cards or detailed OpenSpec prematurely merely because ideas are becoming concrete.
