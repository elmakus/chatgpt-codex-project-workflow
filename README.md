# ChatGPT ↔ Codex Project Workflow v3

A GitHub-backed workflow for large technical projects where ChatGPT handles research, requirements, architecture, planning and strategic decisions, while Codex handles repository inspection, implementation, tests, Git state and execution evidence.

## Core model

**ONE PROJECT = ONE REPOSITORY from the first idea.**

The project repository is the durable history of brainstorming, research, accepted decisions, requirements, approved planning, implementation state, OpenSpec, evidence and cumulative handoffs. This workflow repository contains only the rules, contracts, templates and start prompts that define how that work is performed.

Every project repository has a small root `PROJECT.md`. It is the context router: it states the current phase and points to the authoritative requirements, plan, milestone, Task Board, latest handoff, active OpenSpec change, accepted decisions, open questions and blockers.

Agents use progressive disclosure. They read the workflow entrypoint plus `PROJECT.md`, then load only the modules and project artifacts needed for the current phase. Progressive disclosure means **less context per task, not fewer rules**.

## Roles

ChatGPT is the strategic planning and decision layer. Codex is the implementation and execution authority inside approved contracts. GitHub stores durable state. Chat is a strategic communication channel, not the only copy of important state.

## Start an existing project

Use a short instruction such as:

> Użyj mojego Project Workflow z `elmakus/chatgpt-codex-project-workflow`. Repo projektu: `elmakus/example-project`. Kontynuujemy brainstorming.

ChatGPT reads this repository's `CHATGPT.md`, then the project's `PROJECT.md`, determines the phase and loads only the required modules.

## Start a new project

Create an empty project repository first, then initialize it from `templates/PROJECT.md` and the phase-appropriate templates. Project knowledge never goes into this workflow repository.

## Where workflow changes happen

All workflow changes are made in `elmakus/chatgpt-codex-project-workflow`. Its current `main` is the only canonical workflow authority. ZIP files may be release snapshots or exports, but after v3 is published they are not authority.
