# M02-T01 root-cause convergence analysis after R11 hard ceiling

Date: 2026-09-24
Workstream: `change-pwv21-policy-kernel-brainstorming`
Mode: Main/root-cause convergence analysis — **not** an independent Card Review
Entry review: `M02-T01-R11`
Stable acceptance surface: `implementation/workstreams/change-pwv21-policy-kernel-brainstorming/cards/M02-T01.md`
Current durable Card Result subject: `elmakus/chatgpt-codex-project-workflow@eb17e9a9fd95195544426d7fc8dba5ae48f30cf0:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/results/M02-T01.md@46ce3ec63f7c0ae82fa5c0c13c90f6428d6e9800`
Current implementation subject: `elmakus/project_workflow_v2@e7a939e0a37f3cfcb7e39e04d5654b94101a5090`

## Purpose and boundary

The user-defined R07-R11 strengthened fresh full-review sequence reached its hard convergence ceiling. This analysis intentionally uses the durable M02 review/repair history to identify root causes and decide whether another implementation correction is justified before one final post-convergence validation review.

This analysis does not issue a Card-review verdict. It does not materialize M03, consume `after-M02-T01`, change accepted product authority, or reopen Planning merely to rewrite history.

## Authority and current evidence reconstructed

The analysis used the approved P2 M02 plan, PWV21-REQ-018 through PWV21-REQ-033, applicable accepted ADRs, the stable M02-T01 Card, initial implementation evidence, ordered R01-R11 review evidence, every material bounded repair record, the current Result, current corrected implementation artifacts, and raw CI/readback.

Approved P2 makes M02 one coherent milestone but explicitly permits Execution Prep to split it into four bounded Card surfaces:

1. schema;
2. derivation/resolution;
3. acceptance/reconciliation;
4. mutation-handoff.

P2 also independently passed planner audit and Stage-6 Plan Review. Its M02 outcome, acceptance and verification strategy are explicit, including real schema validation, deterministic/minimal freshness, stale-result negative cases, direct-mutation boundaries and governed readback.

Current implementation subject `e7a939e0...` is the exact target branch HEAD. GitHub Actions run #403 / ID `35958508100`, job `107501825220`, completed GREEN on that exact SHA with 15/15 dedicated M02 tests, 187/187 full discovery, and M01 baseline PASS.

## Historical defect classes

The repeated REDs are not eleven unrelated mistakes. They cluster into four implementation defect classes plus one process/decomposition class.

### RC-1 — incomplete closure of the canonical determining/binding surface

Representative findings:
- R01: result subject, role and duplicated determining fields were not all identity/freshness-bound;
- R07: the typed Result lacked a distinct immutable produced implementation subject;
- R09: production derivation accepted caller projections rather than deriving the registered rule's actual canonical inputs;
- R09: non-canonical path aliases produced multiple identities for the same logical location;
- R10: registered-rule content that materially determines an obligation was not itself fingerprint-bound;
- R11: collection-valued rule inputs were fingerprinted too broadly instead of by minimal determining projection.

Underlying cause: the implementation initially modeled individual fields/functions correctly enough for examples, but did not define and prove one closed invariant for **all and only** semantic data that determines identity, freshness and acceptance.

### RC-2 — representation parity and host-language semantic traps

Representative findings:
- R01: executable repository validation disagreed with JSON Schema and documentation lagged stale-action semantics;
- R03: checked-in JSON Schemas were not actually executed as contracts and diverged from the Python validator;
- R04: Python JSON serialization admitted NaN/Infinity and schema/runtime whitespace/telemetry behavior still differed;
- R05: Python `True == 1` made executable version validation weaker than the JSON Schema;
- M02 Milestone Review R01: the same Python bool/int equality property weakened mutation pre/postcondition readback.

Underlying cause: executable validator, JSON Schema, canonical JSON, human-readable contract and Python value semantics were treated as related implementations rather than one equivalence class that must accept/reject the same typed language.

### RC-3 — helper-level checks were not always coupled to terminal acceptance

Representative findings:
- R09: direct-mutation protection was tested through an invented closed-schema property rather than the representable `changed_artifacts` path;
- R09: governed readback existed as a helper but was not mandatory on the terminal fresh-result acceptance path;
- R10: exact freshness/binding could turn failed/blocked/non-GREEN semantic Results into acceptance-like actions.

Underlying cause: local helpers encoded pieces of the contract, but the end-to-end acceptance transition was not initially treated as the single composition invariant that must dominate all success/reuse paths.

### RC-4 — negative space was specified too narrowly

Representative findings:
- R03/R04: schema negatives covered selected examples but not sibling path/telemetry/whitespace cases;
- R05/Milestone R01: numeric mismatch tests did not initially include JSON boolean/integer type confusion;
- R07: required negative authority/direct-mutation cases were incomplete;
- R08: telemetry exact spellings were rejected, but semantically equivalent key families such as `model_name` and `session_uuid` were not;
- R11: generic unrelated-noise coverage did not prove collection order/metadata/membership minimality.

Underlying cause: tests asked “does this known bad example fail?” more often than “what is the complete forbidden equivalence class and what sibling representations exercise it?”

### RC-5 — M02-T01 was too broad for efficient falsification

The stable M02-T01 Card combined all 16 M02 requirements and all four separable P2 implementation surfaces into one Card. That was permitted, but P2 explicitly offered a split at exactly these seams.

This was the main process multiplier. Schema language, authority derivation, freshness identity, stale-result acceptance, mutation/readback and runtime-boundary negatives are independently falsifiable contract families. Combining them increased reviewer cognitive surface and made a GREEN local suite/review easier to obtain while a different contract family still contained an untested invariant.

The accepted plan itself therefore does **not** need correction. The weaker choice occurred during Execution Prep/JIT decomposition.

## Requested quality assessment

### 1. Strategic / Planning quality

Assessment: adequate and not the root cause.

P2 is explicit about M02 semantics, verification and escalation boundaries, and independently passed both planner audit and Plan Review. It already anticipated bounded decomposition. No reviewed defect requires changing accepted authority-resolution semantics, freshness semantics, mutation ownership, milestone order or product outcome.

The convergence problem came from realization/decomposition and proof strength, not missing strategic authority.

### 2. Execution Prep / Task Card decomposition and scope

Assessment: materially over-broad.

M02-T01 collapsed schema, derivation/resolution, acceptance/reconciliation and mutation-handoff into one Card even though P2 explicitly allowed those as separate Cards. That choice did not violate P2, but it concentrated too many semantic invariants into one review unit and materially increased serial RED/repair discovery.

Retroactively splitting the already-implemented current M02 subject is not justified now. The lesson is prospective: when a milestone contains multiple independently falsifiable contract boundaries, Execution Prep should prefer the accepted functional seams instead of one “complete milestone” Card.

### 3. Implementation / Worker reasoning quality

Assessment: functionally productive but initially insufficiently invariant-driven.

The initial implementation covered nearly every named feature and repeatedly passed the full baseline, yet later reviews found cross-surface binding, parity and acceptance-composition gaps. The recurring pattern is not absence of implementation effort; it is reasoning from feature examples and local helper correctness instead of first defining the semantic invariants that all representations and terminal paths must satisfy.

From R09 onward, repairs became materially stronger because they corrected whole classes and sibling cases rather than only the observed example.

### 4. Test and negative-space / invariant coverage

Assessment: initially too example-driven; materially improved by the later protocol.

Early GREEN tests repeatedly coexisted with defects that were adjacent to already-tested cases:
- schema structure was inspected without executing the schema;
- unsupported numeric version was tested without boolean-version confusion;
- integer mismatch was tested without bool/int type identity;
- exact telemetry names were tested without key families;
- direct mutation was tested via an impossible unknown property rather than the representable artifact field;
- generic unrelated noise was tested without collection order/metadata semantics.

The current 15-test dedicated suite now contains class-level sibling coverage for the known defect families, including real Draft 2020-12 validation, semantic success gating, representable direct-mutation paths, family-level telemetry rejection, rule-content binding, stale-result siblings, and K011/K012 minimal collection projections.

### 5. Review completeness and information-boundary behavior

Assessment: semantic independence was generally sound; completeness protocol was initially insufficient.

R07-R11 correctly enforced fresh subject-relative independence and excluded prior findings/repair narratives from correctness input. That information boundary is valuable and should be preserved.

Earlier lifecycle behavior nevertheless increased the number of cycles. It is not accurate to say every earlier reviewer literally stopped at the first RED: R01, R04 and others recorded multiple findings. The material issue was that reviews did not consistently require an exhaustive continuation across the entire acceptance surface after a blocking finding, and some passes were strongly repair-focused. R02 and R06 both issued GREEN on subjects for which a later independent review established a material defect, proving that “repair checked + current suite GREEN” was not sufficient completeness evidence.

R09 is the inflection point: it explicitly continued the full acceptance pass after the first defect and produced four independent classes in one attempt. R10 then found two classes; R11 found one narrow remaining class. The shrinking complete finding set is evidence of real convergence rather than simple reviewer fatigue.

### 6. Repair behavior: example-local vs defect-class/root-cause

Assessment: early repairs were mostly finding-complete but class-local; later repairs became root-cause/class-level.

R01-R05 and the first Milestone correction correctly fixed their recorded defects, but sibling variants of the same broader classes later resurfaced: schema/runtime parity, JSON/Python type identity, negative-space vocabulary and end-to-end binding.

R09 changed the repair protocol materially: all four findings were repaired at the production seam and generalized to sibling cases. R10 did the same for semantic Result acceptance and registered-rule identity. R11 corrected the collection-minimality class with both K011 and sibling K012 regression coverage rather than only the exact triggering example.

That protocol change explains why the finding set contracted from four classes (R09), to two (R10), to one narrow class (R11).

## Does R09-R11 demonstrate convergence?

Yes, with an important limit: it demonstrates **process and defect-set convergence**, not an independent GREEN verdict.

Evidence supporting convergence:
- R09 was an explicit exhaustive full pass and found four classes;
- its repair generalized each class across sibling paths;
- R10 was another fresh exhaustive pass and found two new classes;
- its repair introduced one shared semantic acceptance gate and rule-content identity binding with sibling stop/recovery cases;
- R11 was another fresh exhaustive pass and established only one remaining material class, freshness minimality for collection-valued inputs;
- the R11 repair covers both current collection-valued registered predicates, K011 and K012, with order/metadata/noise and material-change regressions;
- all other current registry inputs are scalar, so there is no presently known sibling collection class left uncovered;
- raw CI on the exact corrected subject is GREEN.

This progression is consistent with convergence and materially stronger than the pre-R09 repair/recheck loop.

## Current systemic M02 risk and hardening decision

No additional bounded implementation hardening is justified before validation.

The current exact registry has two collection-valued rules, and both now have kernel-owned minimal deterministic projectors plus sibling regressions. The other current rules use scalar declared inputs. The known schema/runtime/type, semantic-acceptance, direct-mutation, telemetry-family, authority-binding, rule-binding, stale-result and mutation-readback classes all have generalized regression coverage on the current subject.

A future milestone could add a new collection-valued predicate and would then need an appropriate minimal projection/invariant. That is a future evolution risk, not evidence of a present M02 defect on the current registry. Changing M02 now for that hypothetical would be speculative hardening, which is not authorized by this convergence analysis.

Therefore the exact implementation subject remains:
`elmakus/project_workflow_v2@e7a939e0a37f3cfcb7e39e04d5654b94101a5090`.

No code/schema/test correction is performed by this analysis.

## Structural decision

M02-T01 was over-broad, but the accepted P2 plan/authority is not defective and does not require material replanning now. Rewriting the already-complete Card topology after convergence would create churn without fixing a demonstrated current defect.

The correct next boundary is validation of the exact current subject, not another ordinary repair/review loop and not a Planning rewrite.

## Exact next durable obligation

Create exactly one post-convergence fresh independent full-scope Card validation attempt for the current Result subject:

- attempt: `M02-T01-R12`;
- subject: `elmakus/chatgpt-codex-project-workflow@eb17e9a9fd95195544426d7fc8dba5ae48f30cf0:implementation/workstreams/change-pwv21-policy-kernel-brainstorming/results/M02-T01.md@46ce3ec63f7c0ae82fa5c0c13c90f6428d6e9800`;
- acceptance: stable `cards/M02-T01.md`;
- implementation named by that Result: `elmakus/project_workflow_v2@e7a939e0a37f3cfcb7e39e04d5654b94101a5090`;
- review method: fresh independent exhaustive full-scope validation from stable accepted authority, exact current artifacts and raw evidence; prior convergence history is lifecycle context only, not correctness evidence.

If R12 is GREEN, normal deterministic Card finalization may proceed under the workflow's exact-subject rules.

If R12 is RED, **do not** start an automatic R13/R14 repair/review sequence. Persist the complete R12 finding set and return to Main/Recovery for broader convergence escalation. Main must classify whether the new evidence requires Card/decomposition/plan restructuring (Strategic Planning), accepted product/global authority correction (Definition), Research, or another real owning boundary. A new ordinary review loop is not authorized merely because the defect is locally patchable.

`after-M02-T01` remains waiting. M03 is not materialized or started.
