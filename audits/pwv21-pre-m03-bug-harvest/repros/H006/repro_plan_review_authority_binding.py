#!/usr/bin/env python3
"""H006 minimal production-validator probe.

Run from the root of an exact project_workflow_v2 checkout.
Expected vulnerable behavior: both validations return normally even though
Plan Review acceptance is unrelated to the current Definition authority.
"""

from tools.state_contract import validate_planning, validate_plan_review

WORKSTREAM = "ws"
PLAN_PATH = "planning/MASTER_PLAN.md"
PLAN_SUBJECT = {
    "repository": "elmakus/example",
    "commit": "1" * 40,
    "path": PLAN_PATH,
    "blob": "2" * 40,
}
PLAN_KEY = (
    f"{PLAN_SUBJECT['repository']}@{PLAN_SUBJECT['commit']}:"
    f"{PLAN_SUBJECT['path']}@{PLAN_SUBJECT['blob']}"
)

planning = {
    "workstream_id": WORKSTREAM,
    "cycle": 1,
    "entry_subject": "definition:R1",
    "revision": "P1",
    "state": "frozen",
    "planner_audit": "green",
    "plan_path": PLAN_PATH,
    "review_mode": "independent",
    "review_exemption_basis": "",
    "review_exemption_base_subject": "",
    "premium_a": "satisfied",
    "premium_a_subject": "definition:R1",
    "premium_b": "satisfied",
    "premium_b_subject": PLAN_KEY,
    "premium_c": "not_due",
    "premium_c_subject": "",
    "subject": PLAN_SUBJECT,
}

plan_review = {
    "attempt": "PR01",
    "verdict": "green",
    "workstream_id": WORKSTREAM,
    "plan_revision": "P1",
    "planning_cycle": 1,
    "subject": {
        "class": "git_blob",
        **PLAN_SUBJECT,
    },
    "acceptance": {
        "class": "authority",
        "path": "workflow/ROUTER.md",
    },
    "independence": {
        "materially_produced_or_repaired_subject": False,
        "basis": "fresh independent review",
    },
    "evidence_path": "implementation/workstreams/ws/evidence/PR01.md",
}

CURRENT_DEFINITION_AUTHORITY = {
    "requirements/current.md",
    "decisions/current.md",
}
assert plan_review["acceptance"]["path"] not in CURRENT_DEFINITION_AUTHORITY

validate_planning(planning, WORKSTREAM)
validate_plan_review(plan_review, WORKSTREAM, planning)

print("ACCEPTED")
print("plan_subject =", PLAN_KEY)
print("review_acceptance =", plan_review["acceptance"]["path"])
print("current_definition_authority =", sorted(CURRENT_DEFINITION_AUTHORITY))
