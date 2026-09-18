# Fresh ChatGPT Session Start Prompt

Use this template whenever Project Workflow **requires** or **recommends** a fresh normal ChatGPT chat.

The user-facing response must include the completed prompt immediately in a fenced Markdown block. Do not make the user ask for it separately.

## Minimal template

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/implementation branch>.
Kontynuuj: <exact card/milestone/review gate or concise goal>.
Durable start pointer: <implementation/TASK_BOARD.yaml | other exact durable pointer>.
Odtwórz aktualny stan, exact subject, authority slice i wymagane evidence z repo. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

For a pending independent review, prefer:

```text
NEW CHAT START PROMPT:
Użyj Project Workflow z elmakus/chatgpt-codex-project-workflow (current main).
Repo projektu: <owner/repo>.
Branch projektu: <exact active project/implementation branch>.
Kontynuuj: pending independent review dla <MXX-TYY>.
Durable start pointer: implementation/TASK_BOARD.yaml.
Odtwórz exact review_subject, authority slice i evidence z repo, wykonaj niezależny review zgodnie z workflow i zapisz verdict/evidence w durable state. Nie traktuj tego prompta ani poprzedniego czatu jako źródła prawdy.
```

## Inclusion rule

Include:
- project repository;
- exact active project/implementation branch, even when it is `main`;
- exact continuation target;
- smallest durable start pointer;
- one instruction to recover authoritative state from repository;
- only non-durable user intent that cannot be recovered from repository.

Do not duplicate:
- exact SHA/review subject if Task Board already records it;
- test counts/results;
- evidence prose;
- changed files/blobs;
- implementation summary;
- HEAD/SHA details already recoverable from durable state.

The branch is the one deliberate exception: always include the exact active branch because it is a routing locator, not redundant execution telemetry.

The prompt is a router into durable project truth, not a second handoff document.
