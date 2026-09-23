# M05-T01 — ChatGPT bootstrap and locator-only handoff evidence

Date: 2026-09-23
Card: `M05-T01`
Target: `elmakus/project_workflow_v2@feat/pwv2-m05-delivery`
Accepted implementation subject: `5302a06c9ddf5360f71c722c6d78c774a27f51e7`
Tree: `f7cbcc58b441c733d8b56d8800f8017a348421eb`
Base / M04 integrated predecessor: `674fb970913c393cfc6ed82a5ef67dda8b8713b7`
PR: `elmakus/project_workflow_v2#5`

## Implemented contract

- Added canonical `workflow/USER_STOP.md` as the real-stop formatter after the router has already established a genuine stop.
- Added user-owned `prompts/CHATGPT_PROJECT_INSTRUCTIONS.md` as a thin locator to `elmakus/project_workflow_v2`, the common `workflow/ROUTER.md`, the consumer repository and exact durable workstream state.
- Added locator-only `prompts/CHATGPT_FRESH_SESSION.md` with only repository, exact branch, entry obligation and durable start pointer.
- Kept workflow semantics under the canonical `workflow/` tree; the delivery prompts do not copy policy, review state, runtime identity, Context Health/FRESH lifecycle or a per-project workflow patch pin.
- Updated the common router to delegate real-stop formatting to `workflow/USER_STOP.md`.
- Added deterministic ChatGPT-delivery tests and included them in `scripts/test.sh`.
- README exposes only the delivery templates and keeps construction/state authority outside the target repository.

## Acceptance against exact authority slice

- PWV2-REQ-001 / ADR-PWV2-002: one canonical semantic tree remains under `workflow/`; ChatGPT bootstrap points at the V2 repository rather than duplicating semantics.
- PWV2-REQ-007: the Project Instructions template obtains V2 authority from the V2 GitHub repository through user-owned bootstrap configuration.
- PWV2-REQ-013..017 / ADR-PWV2-006: bootstrap is thin and progressively discloses router -> exact consumer/workstream state; it does not preload neighboring workflow semantics or create a second state/control store.
- PWV2-REQ-067..071: automatic continuation remains router-owned; `USER_STOP.md` lists real stops, explicitly rejects a Project Workflow Context Health/FRESH lifecycle, and the fresh-session template is locator-only.
- M05.P1 acceptance: canonical USER_STOP owns concise stop formatting, bootstrap enters the common router and exact durable recovery path, and ordinary canonical workflow edits do not require bootstrap edits unless bootstrap behavior itself changes.

## Deterministic verification

Exact target `5302a06c9ddf5360f71c722c6d78c774a27f51e7`:

- GitHub Actions pull-request run `35776625360`: PASS.
- Workflow step `Run repository checks` executes `sh scripts/test.sh`: PASS.
- State suite: 28/28 PASS.
- Router suite: 39/39 PASS, including exact progressive-disclosure read-set and real-stop foundations.
- Execution suite: 4/4 PASS.
- Review suite: 1/1 PASS.
- Recovery suite: 2/2 PASS.
- Close/fork/ChatGPT-delivery combined unittest invocation: 33/33 PASS.
- Total Python unittest count exercised by `scripts/test.sh`: 107/107 PASS, plus the package/router shell probes.

## Readback

- Target branch `feat/pwv2-m05-delivery` read back at exact HEAD `5302a06c9ddf5360f71c722c6d78c774a27f51e7` and tree `f7cbcc58b441c733d8b56d8800f8017a348421eb`.
- Branch is 7 commits ahead and 0 behind target `main@674fb970913c393cfc6ed82a5ef67dda8b8713b7`.
- Draft PR #5 is open from `feat/pwv2-m05-delivery` to `main` and its head is the exact accepted subject.
- No live ChatGPT Project mutation or user-owned consumer configuration change was performed; those real-surface checkpoints remain M05-T04 scope.

## Acceptance disposition

M05-T01: GREEN / DONE.

Policy reroute after reconciliation: return to the current-main ChatGPT-only router; next deterministic M05 obligation is resolved from durable Task Board state.
