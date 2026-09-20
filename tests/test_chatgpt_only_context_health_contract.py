from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ROUTER = (ROOT / "workflow/chatgpt_only/ROUTER.md").read_text(encoding="utf-8")
CONTEXT = (ROOT / "workflow/chatgpt_only/CONTEXT_HEALTH.md").read_text(encoding="utf-8")
AUDIT = (ROOT / "docs/audits/CHATGPT_ONLY_CONTEXT_HEALTH_GATE.md").read_text(encoding="utf-8")


class ChatGPTOnlyContextHealthContractTests(unittest.TestCase):
    def test_router_does_not_use_workflow_transition_as_standalone_trigger(self):
        self.assertIn(
            "A role, milestone, phase, workstream or authority-area transition is not by itself "
            "a concrete context-health signal",
            ROUTER,
        )
        self.assertNotIn("major role/authority-area transition", ROUTER)
        self.assertIn("If there is no affirmative harmful-context signal", ROUTER)

    def test_context_health_requires_affirmative_transcript_risk(self):
        self.assertIn(
            "If the exact next obligation and its authority are deterministically recoverable "
            "from durable state and there is no affirmative evidence that the accumulated "
            "transcript is harmful, choose CONTINUE.",
            CONTEXT,
        )
        self.assertNotIn(
            "the next obligation uses a substantially different authority/source area than "
            "the work just completed",
            CONTEXT,
        )

    def test_fresh_handoff_has_anti_bounce_rule(self):
        self.assertIn("#### Fresh-handoff anti-bounce", CONTEXT)
        self.assertIn(
            "Another FRESH result requires new concrete context degradation accumulated in "
            "the current chat after recovery.",
            CONTEXT,
        )
        self.assertIn(
            "completion of the recovered obligation and transition to the next deterministic "
            "role are likewise not new degradation",
            ROUTER,
        )

    def test_hard_context_risk_signals_are_preserved(self):
        for signal in (
            "materially superseded/contradictory state",
            "difficulty distinguishing current durable truth",
            "mentally reconstructing substantial prior state",
        ):
            self.assertIn(signal, CONTEXT)

    def test_audit_covers_short_recovery_bounce_regression(self):
        self.assertIn("### 7. Short context-hygiene recovery does not bounce", AUDIT)
        section = AUDIT.split(
            "### 7. Short context-hygiene recovery does not bounce", 1
        )[1].split("### 8.", 1)[0]
        self.assertIn("Result: **CONTINUE**.", section)
        self.assertIn("no new harmful-context evidence accumulated", section)

    def test_audit_says_authority_transition_alone_continues(self):
        section = AUDIT.split(
            "### 6. Milestone finalized, next approved milestone differs materially", 1
        )[1].split("### 7.", 1)[0]
        self.assertIn("different authority/source area only", section)
        self.assertIn("Result: **CONTINUE**.", section)


if __name__ == "__main__":
    unittest.main()
