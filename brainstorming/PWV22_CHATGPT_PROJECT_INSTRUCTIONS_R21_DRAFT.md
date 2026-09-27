# Draft — ChatGPT Project Instructions bootstrap for PWv2.2

Status: exploratory Revision-21 draft; not Definition authority and not yet a canonical Project Workflow template.

Replace only `<owner/repository>` when preparing instructions for a concrete ChatGPT Project.

---

Use the current Project Workflow from `https://github.com/elmakus/project_workflow_v2` as the workflow authority for this ChatGPT Project.

Consumer project repository: `https://github.com/<owner/repository>`

Research/swarm orchestration convention: `https://github.com/elmakus/project-research/blob/main/COORDINATOR_PROTOCOL.md`

For workflow entry or continuation:
1. read `workflow/ROUTER.md` from the current default branch of `elmakus/project_workflow_v2`;
2. recover the consumer repository's `PROJECT.md`, exact selected workstream, and only the durable pointers required by the Router;
3. progressively load only the exact current workflow module, authority and evidence required by the Router;
4. continue deterministic authorized transitions until the Router reaches a real stop;
5. when the selected workflow obligation requires formal Research, a research swarm, bug-hunt swarm, repair swarm or revalidation swarm, read the current `COORDINATOR_PROTOCOL.md` and use it only as non-authoritative orchestration guidance.

The consumer repository and canonical Project Workflow are semantic authority. `project-research` artifacts and the Coordinator Protocol are evidence/orchestration only unless exact consumer authority explicitly promotes a result.

Treat these Project Instructions as bootstrap locators, not a copy of workflow semantics. Recover truth live from durable repositories. Do not reconstruct missing policy from chat memory, prior session state, model/runtime identity, helper caches or another state store.

Do not pin the persistent Project Instructions to a transient consumer branch, workstream, Card, session, model, workflow patch SHA or research run. Exact transient entry context belongs in the workflow's locator-only fresh-session handoff.

If required repository access cannot be established, fail closed and report the concrete access blocker rather than guessing state.

---

## Current design rationale

Stable persistent fields:
- canonical Project Workflow repository;
- consumer repository;
- Coordinator Protocol locator.

Transient fields intentionally excluded:
- consumer branch/workstream/Card;
- current workflow stage;
- exact model/session;
- current Research package;
- exact workflow patch SHA for ordinary update propagation.

This keeps Android ChatGPT Project Instructions stable while fresh-chat prompts remain tiny exact locators.
