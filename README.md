# ChatGPT ↔ Codex Project Workflow v3

A GitHub-backed workflow for large technical projects where ChatGPT handles research, requirements, architecture, planning and strategic decisions, while Codex handles repository inspection, implementation, tests, Git state and execution evidence.

## Core model

**ONE PROJECT = ONE REPOSITORY from the first idea.**

The project repository is the durable history of brainstorming, research, accepted decisions, requirements, approved planning, implementation state, OpenSpec, evidence and cumulative handoffs. This workflow repository contains only the rules, contracts, templates and start prompts that define how that work is performed.

Every project repository has a small root `PROJECT.md`. It is the context router: it states the current phase and points to the authoritative requirements, plan, milestone, Task Board, latest handoff, active OpenSpec change, accepted decisions, open questions and blockers.

Agents use progressive disclosure. They read the workflow entrypoint plus `PROJECT.md`, then load only the modules and project artifacts needed for the current phase. Progressive disclosure means **less context per task, not fewer rules**.

## Roles and authority domains

ChatGPT is the strategic planning and decision layer. Codex is the implementation and execution authority inside approved contracts. GitHub stores durable project state. Chat is a strategic communication channel, not the only copy of important state.

This repository is authoritative for **project workflow**: lifecycle, Task Cards, selective JIT OpenSpec, GitHub state, evidence, acceptance, strategic escalation and cumulative handoffs.

When the owner's `codex_workflow` is installed and enabled, its installed instructions are authoritative for **internal Codex runtime orchestration**: worker roles/models, delegation mechanics, Companion/worker lifecycle, waits/events/messages, polling/silence and related runtime behavior. Project Workflow intentionally does not duplicate those mechanics.

## Start an existing project

Use a short instruction such as:

> Użyj mojego Project Workflow z `elmakus/chatgpt-codex-project-workflow`. Repo projektu: `elmakus/example-project`. Kontynuujemy brainstorming.

ChatGPT reads this repository's `CHATGPT.md`, then the project's `PROJECT.md`, determines the phase and loads only the required modules.

## Start a new project

Create an empty project repository first, then initialize it from `templates/PROJECT.md` and the phase-appropriate templates. Project knowledge never goes into this workflow repository.

## Versions

Current `main` is always the canonical Project Workflow authority.

Annotated SemVer tags are immutable snapshots. The repository's GitHub Actions workflow automatically creates the next **patch** tag (`vX.Y.Z+1`) for each new push to `main`, starting from the highest existing SemVer tag. Creating a new major/minor baseline remains an explicit decision; after such a tag exists, automatic patch numbering continues from it.

## Where workflow changes happen

All Project Workflow changes are made in `elmakus/chatgpt-codex-project-workflow`. Its current `main` is the canonical Project Workflow authority. ZIP files may be release snapshots or exports, but after v3 is published they are not authority.
