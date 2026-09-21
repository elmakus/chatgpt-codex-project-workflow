# Proposal — Research agent behavior

## Why

Project Workflow Research already separates evidence from accepted authority, but it does not explicitly require checking relevant public prior art before inventing a new solution. The shared template also contains stale ChatGPT-only pre-execution pointer commentary.

## Change

Strengthen the shared Research evidence contract so relevant external prior art is actively discovered when it can materially help, while preserving proportional local-only behavior, source-quality distinctions, bounded stopping, existing return/reconciliation semantics and policy-local pointer ownership.

Both migrated fixed policies apply the same evidence behavior. Concrete Codex Investigator model/harness/session realization remains owned by `codex_workflow`.

## Non-goals

- no crawler, search index/database or search service;
- no mandatory broad web search for local/private questions;
- no mandatory forum/social source for every question;
- no new mutable Research lifecycle state;
- no Project Workflow-owned Codex Investigator runtime mapping;
- no unrelated routing/state redesign.
