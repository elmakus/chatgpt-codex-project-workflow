# M02R-T01 implementation evidence

Date: 2026-09-24
Card: `M02R-T01`
Implementation repository: `elmakus/project_workflow_v2`
Implementation branch: `work/pwv21-policy-kernel`
Baseline subject: `e7a939e0a37f3cfcb7e39e04d5654b94101a5090`
Candidate subject: `d4c2a89ebf52f975b6c8c5c8912c7616704e0a49`

## Implemented surface

The exact baseline-to-candidate comparison changes nine files:

- `tools/review_contract.py`
- `tools/state_contract.py`
- `tools/router.py`
- `templates/REVIEW_ATTEMPT.toml`
- `workflow/REVIEW.md`
- `workflow/STATE.md`
- `tests/test_review_contract.py`
- `tests/test_state_contract.py`
- `tests/test_router.py`

No BOOT-A convergence-counter/ceiling semantics, advisory-observation lifecycle, BOOT-B/C/D or M03+ implementation was added by this Card.

## Acceptance implementation

- Explicit `discovery` versus `closure_verification` review-pass semantics.
- Historical attempts without explicit PWv2.1 review-kind fields remain interpreted as discovery for compatibility.
- Terminal discovery is complete-pass: it cannot claim completion after first-blocker short-circuit; RED freezes the complete material finding IDs; GREEN cannot retain material blocking findings.
- Closure binds to an earlier RED discovery attempt and only to finding IDs frozen by that source.
- Closure-verification scope explicitly accounts for known findings, repair diff, regression evidence and the materially implicated causal blast radius:
  reachable callers, consumers, providers, contracts, sibling representations and negative-space cases.
- Missing causal categories or omitted materially implicated items fail validation.
- GREEN closure does not satisfy the Card review obligation. Router freezes a new fresh full-scope discovery attempt; only GREEN discovery can finalize review.
- Review documentation requires defect-class/root-cause repair with sibling/negative-space regression coverage.

## Falsification / repair evidence

Draft PR #9 was opened only as a non-mergeable integration/test surface for the candidate branch.

First PR test run:
- GitHub Actions run: `36007946468`
- result: **FAIL**
- failure: direct `tools/state_contract.py` execution could not resolve the package-only import `tools.review_contract`.
- focused state tests including the new explicit review-history test had already passed before the script-mode failure.

Repair:
- commit `d4c2a89ebf52f975b6c8c5c8912c7616704e0a49`
- preserved both package import and direct-script execution via bounded fallback import.
- no Card scope expansion.

Final PR test run:
- GitHub Actions run: `36008463655`
- job: `107662662761`
- conclusion: **SUCCESS**
- repository command: `sh scripts/test.sh`
- focused router suite: 40 tests GREEN.
- focused review-contract suite: 4 tests GREEN.
- state suite includes PWv2.1 discovery/closure-history fixtures GREEN.
- cumulative pre-discovery suite: 80 tests GREEN.
- full Python discovery: 192 tests GREEN.
- final repository check: `M01 baseline checks: PASS`.

## Readback

Read back from exact candidate `d4c2a89ebf52f975b6c8c5c8912c7616704e0a49`:

- `tools/review_contract.py` — blob `31c44f68d35848291d0fd55ada583a93e1c0866a`
- `tools/state_contract.py` — blob `927e31aaad4e3f9524da37305a1ec19dc448bbad`
- `tools/router.py` — blob `cea08202266dd9e866bb1a988436a527832d7913`
- `templates/REVIEW_ATTEMPT.toml` — blob `937b712a3008ff9da108ff7d69677ab65d6e6267`
- `workflow/REVIEW.md` — blob `913eab473e73c70fa51ce3fb291dc4d1f68f6742`
- `workflow/STATE.md` — blob `c16f7c489a189152e429397dc0b81a3ec6b97688`
- `tests/test_review_contract.py` — blob `f57a2be6d926694c1567f728e807335252008390`
- `tests/test_state_contract.py` — blob `0173e79f0790332c8164e5886066a87ca03c9599`
- `tests/test_router.py` — blob `f20d3851376b0bee9e7e5355e9035c552b134e84`

## Execution conclusion

Implementation evidence is GREEN for the Card's self-test/readback obligations. Formal independent Card review remains required and is not satisfied by this implementation context.
