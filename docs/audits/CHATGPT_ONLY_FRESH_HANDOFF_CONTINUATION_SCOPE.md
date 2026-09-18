# ChatGPT-only Fresh-Handoff Continuation — Independent Review Scope

Date: 2026-09-18  
Implementation base: `main@6ddc372b9f3718ea5d9f27e6a01614e8d3da9556`  
Implementation branch: `fix/chatgpt-only-fresh-handoff-continuation`  
Review requirement: **REQUIRED**  
Review subject: freeze the exact branch HEAD at independent-review entry; do not use this file's prose as verdict authority.

## Accepted problem / target behavior

Fresh normal-ChatGPT handoffs must remain thin recovery locators into durable project truth. The obligation named in a fresh-session prompt is the first role to recover, not an implicit session-scope boundary.

After the located role completes, normal `chatgpt_only` router-owned continuation resumes. The chat continues deterministic authorized role transitions until a real workflow stop.

The handoff must not become a second task contract by copying recoverable review/audit scope, prior findings, remediation logic or execution telemetry into the prompt.

## Review objectives

Independently verify the current branch against current workflow authority and actual diff.

At minimum verify:

1. **Pre-response stop proof**
   - a normal ChatGPT workflow-status reply is legal only after current durable state is re-evaluated through the selected router;
   - completion of the user-named role, fresh-handoff entry obligation, Card, milestone or review verdict is not itself a stop;
   - an available deterministic authorized next role prevents a final user-facing status response.

2. **Fresh-session entry semantics**
   - fresh-session target is explicitly a locator/entry obligation, not a session-scope boundary;
   - after the entry role completes, the new chat returns to the policy router;
   - explicit user/project authority can still deliberately narrow scope.

3. **Locator-only prompt contract**
   - canonical fresh prompts remain short and branch-aware;
   - ad-hoc prompt inflation with checklists, prior findings, remediation proposals, test inventories, implementation summaries, recoverable SHAs/diffs or GREEN/RED continuation branches is prohibited;
   - smallest non-durable user intent remains allowed when repository state cannot recover it.

4. **Durable special scope**
   - a nonstandard review/audit scope that cannot be reconstructed from existing authority is persisted before handoff in an appropriate durable artifact;
   - the prompt points to that artifact rather than serializing it into chat text.

5. **Single canonical prompt owner**
   - `workflow/common/USER_STOP.md` remains the canonical user-facing fresh-session format;
   - `prompts/CHATGPT_FRESH_SESSION.md` does not maintain a divergent duplicate template;
   - start/README/review documentation agrees with that ownership.

6. **Independent-review semantics**
   - pending review still requires a fresh independent chat;
   - GREEN review returns to router and continues when deterministic;
   - bounded deterministic RED remediation still occurs in the same reviewer-started chat after the review role ends;
   - once that chat implements the corrected subject, a new pending independent-review boundary still stops it before self-review.

7. **Context Health**
   - `FRESH` remains only a safe-boundary hygiene stop;
   - the fresh hygiene prompt uses the same locator-only/continuation semantics;
   - Context Health does not create a one-obligation session.

8. **Policy isolation / regression**
   - no Codex/mixed/legacy routing semantics are imported into active `chatgpt_only`;
   - no execution-policy, review requirement, authorization or durable-state ownership rule is weakened.

## Required logical E2E scenarios

### A. Pending review → GREEN → deterministic continuation

```text
fresh prompt → recover pending review → GREEN persisted
→ review role ends → router → Post-review finalization / next legal role
→ no intermediate user reply
```

### B. Pending review → RED → bounded remediation → new review boundary

```text
fresh prompt → RED persisted → review role ends → router
→ bounded Execution/Execution Prep correction
→ corrected exact subject frozen as pending
→ real stop → short locator-only fresh-review prompt
```

### C. Milestone entry → milestone complete → next approved milestone

```text
fresh prompt naming Mxx obligation
→ obligation/milestone complete
→ router → next approved deterministic milestone prep/execution
→ no "No action required" merely because the named entry obligation completed
```

### D. Context Health FRESH

```text
safe durable boundary → CONTEXT_HEALTH: FRESH
→ short locator-only handoff for exact next obligation
→ fresh chat recovers it
→ later role completion returns to router normally
```

### E. Nonstandard audit scope

```text
large special review checklist needed
→ checklist persisted durably
→ fresh prompt contains only repo + branch + entry target + durable scope pointer
→ reviewer reconstructs from repository
```

## Implementation-author self-check boundary

Implementation-author validation may check lexical/coherence properties and the scenarios above, but it is not an independent verdict.

If review finds a blocking inconsistency, persist RED evidence and follow current `chatgpt_only` RED corrective routing. If correction is bounded/deterministic/authorized, do not stop merely to report RED.

If review is GREEN, persist independent evidence before PR finalization/merge.
