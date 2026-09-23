# Intake — PWv2.1 policy-kernel brainstorming

- Workstream ID: `change-pwv21-policy-kernel-brainstorming`
- Kind: `change`
- Branch: `work/pwv21-policy-kernel-brainstorming`
- Integration target: `main`
- Base: `7aa7512ead67a86256089d1af0171e2e655e700d`

## User intent

Create a separate branch in `elmakus/chatgpt-codex-project-workflow` and treat the proposed PWv2.1 design as Brainstorming so the architecture can be continued there without promoting it into requirements, decisions, planning or implementation.

## Bounded scope

Explore an incremental Project Workflow v2.1 direction where:
- Git/repository state remains canonical project memory and authority;
- deterministic code handles mechanical policy/state checks;
- LLM roles keep semantic/reasoning work;
- orchestration stays outside Project Workflow in the separate `orchestration-runtime` layer;
- ChatGPT and Pi remain interchangeable frontends/runtimes over the same durable project state;
- any executable helper remains stateless/rebuildable rather than introducing another project-state database.

This intake does not authorize adopting the architecture.

## Dependency/base classification

Independent workstream from current `main`.

The earlier prior-art research branch is evidence/provenance only; this Brainstorming does not require parent-only implementation state and therefore is not stacked on it.

## Downstream route

Brainstorming.

The exact exploratory record will be materialized before Intake is completed.

## Intake result

- Intake state: complete.
- Independent workstream confirmed.
- Downstream route: Brainstorming.
- Exploratory scope: `brainstorming/PWV21_POLICY_KERNEL.md`.
