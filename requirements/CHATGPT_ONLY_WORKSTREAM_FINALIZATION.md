# ChatGPT-only Workstream Finalization Requirements

Status: draft
Date: 2026-09-19
Scope ID: chatgpt-only-workstream-finalization
Execution policy affected: chatgpt_only

## Problem

Branch-isolated workstreams have canonical namespaced mutable implementation state, but current finalization/handoff rules do not fully define the target-side durable terminal layout, collision-free milestone handoff ownership, or migration of a pre-workstream long-lived branch that still uses the root legacy/default Task Board.

## Goal

Make final integration of independent ChatGPT-only workstreams lossless, collision-free and recoverable after source-branch deletion while preserving backward compatibility for legacy/default single-workstream projects.

## Definition questions to resolve

1. Which workstream artifacts MUST survive on the final integration target?
2. What is the canonical cumulative handoff path for a branch-isolated workstream?
3. What does root `implementation/TASK_BOARD.yaml` mean after branch-isolated workstreams exist?
4. What does `PROJECT.md -> Latest cumulative handoff` mean in a multi-workstream repository?
5. What exact precondition makes source-branch deletion safe?
6. How is a long-lived legacy branch migrated without overwriting the target's unrelated root/default Task Board?
7. Which historical legacy files remain valid in place and which branch-specific files must be namespaced before integration?

## Invariants already accepted

- no mutable global workstream registry is required;
- the manifest identifies one exact branch-isolated workstream and its canonical Task Board;
- existing legacy/default single-workstream projects remain valid;
- historical evidence/handoffs are not rewritten merely because the state model evolved;
- exact branch/workstream state must remain recoverable from durable repository/Git evidence without chat history;
- independent workstreams may reuse milestone IDs such as M01/M02 without colliding in canonical mutable/durable workstream state.
