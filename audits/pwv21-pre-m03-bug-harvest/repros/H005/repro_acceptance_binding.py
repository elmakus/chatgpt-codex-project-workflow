#!/usr/bin/env python3
"""H005 minimal production-validator probe.

Run from the root of an exact project_workflow_v2 checkout.
Expected vulnerable behavior: validate_review_history returns normally even
though review acceptance is not the selected current Card contract path.
"""

from tools.state_contract import validate_review_history

WORKSTREAM = "ws"
CARD = "M01-T01"
SELECTED_CONTRACT = f"implementation/workstreams/{WORKSTREAM}/cards/{CARD}.md"
REVIEWED_ACCEPTANCE = (
    f"implementation/workstreams/{WORKSTREAM}/cards/archive/{CARD}.md"
)

attempt = {
    "attempt": "R01",
    "verdict": "green",
    "workstream_id": WORKSTREAM,
    "card_id": CARD,
    "subject": {
        "class": "git_blob",
        "repository": "elmakus/example",
        "commit": "1" * 40,
        "path": f"implementation/workstreams/{WORKSTREAM}/results/{CARD}.md",
        "blob": "2" * 40,
    },
    "acceptance": {
        "class": "task_card",
        "path": REVIEWED_ACCEPTANCE,
    },
    "independence": {
        "materially_produced_or_repaired_subject": False,
        "basis": "independent reviewer",
    },
    "evidence_path": f"implementation/workstreams/{WORKSTREAM}/evidence/{CARD}-R01.md",
}

assert SELECTED_CONTRACT != REVIEWED_ACCEPTANCE

validate_review_history(
    [attempt],
    expected_card_id=CARD,
    workstream_id=WORKSTREAM,
)

print("ACCEPTED")
print("selected_contract =", SELECTED_CONTRACT)
print("review_acceptance =", REVIEWED_ACCEPTANCE)
