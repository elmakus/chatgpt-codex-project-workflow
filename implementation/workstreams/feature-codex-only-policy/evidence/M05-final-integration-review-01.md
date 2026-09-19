# Workstream final-integration independent review — attempt 01

Workstream: `feature-codex-only-policy`
Review owner: `implementation/workstreams/feature-codex-only-policy/WORKSTREAM.yaml`
Reviewed subject: `feature@15cb08a74fbb50e54bf7f99dfdf3d32f354f6383 + target@92e9f162c3d2fe4b178b04f07edc439c12a33ce8 + M01-M05 acceptance`
Verdict: **RED**

## Independence

This reviewer did not implement the immutable reviewed subject. The subject remained unchanged while it was judged; only review lifecycle state/evidence is written after the frozen subject.

## Authority and evidence checked

- approved `requirements/CODEX_ONLY_POLICY.md` CO-R1 / CO-REQ-001..028;
- accepted namespace, runtime-boundary and bounded-parallel ADRs;
- approved `planning/CODEX_ONLY_MASTER_PLAN.md` M01-M05 acceptance surface;
- M01-M05 acceptance evidence and the latest GREEN independent Card reviews;
- exact subject source for root routing and the Codex-only Router/State/Review/Execution Prep/Execution/Recovery/Workstreams/Close contracts and templates;
- `implementation/workstreams/feature-codex-only-policy/evidence/M05-final-integration-refresh.md`;
- exact target `92e9f162c3d2fe4b178b04f07edc439c12a33ce8`, confirmed still identical to current `main`.

## Independent checks

GREEN:
- root routing isolates `chatgpt_only`, `codex_only` and legacy fallback;
- target-owned root `PROJECT.md` reconciliation is present and the frozen target remains current;
- reviewed Codex-only contracts preserve runtime/project ownership separation, immutable review subjects, Tester non-repair, serial default, Main-only shared state, JIT finite batches, deterministic integration/recovery and terminal workstream refresh/closure;
- Codex-only Task Board/workstream templates do not require runtime session/model/profile/invocation identity;
- no broader stale ChatGPT-only wording pattern was found in the other policy-owner files inspected.

RED finding:
- `workflow/codex_only/WORKSTREAMS.md` says, in its Core model, **“Concurrency exists between workstreams, not between Cards inside one workstream.”**
- The immediately following sentence and the rest of the M03 contracts allow multiple `in_progress` Cards in one workstream under an exact current bounded batch.
- The absolute sentence therefore conflicts with CO-REQ-017 (“codex_only MUST support bounded parallel Task Card execution inside one workstream”) and with ADR-CODEX-PAR-001.
- Because this repository is an executable workflow contract, the contradiction is material: a compliant reader could interpret the first rule as forbidding the very intra-workstream bounded concurrency the accepted authority requires.

## Corrective classification

Bounded L1/L2 documentation-contract correction inside accepted authority. No Definition or Planning change is required.

Replace the contradictory absolute sentence with wording that states:
- independent workstreams may execute concurrently; and
- inside one workstream execution is serial by default, with concurrency legal only through the explicit M03 bounded-batch exception.

Then rerun the affected M03/M04/M05 consistency checks and freeze a new exact final-integration review subject. Prior RED evidence must remain durable.

## Verdict

**RED.** The exact frozen subject is not final-integration GREEN because one normative Workstreams sentence contradicts the accepted bounded-parallel MUST requirement.
