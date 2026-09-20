from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

CHAT_BRAIN = (ROOT / "workflow/chatgpt_only/BRAINSTORMING.md").read_text(encoding="utf-8")
CODEX_BRAIN = (ROOT / "workflow/codex_only/BRAINSTORMING.md").read_text(encoding="utf-8")
CHAT_ROUTER = (ROOT / "workflow/chatgpt_only/ROUTER.md").read_text(encoding="utf-8")
CODEX_ROUTER = (ROOT / "workflow/codex_only/ROUTER.md").read_text(encoding="utf-8")
CHAT_INTAKE = (ROOT / "workflow/chatgpt_only/INTAKE.md").read_text(encoding="utf-8")
CODEX_INTAKE = (ROOT / "workflow/codex_only/INTAKE.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
OPENSPEC = (
    ROOT / "openspec/changes/brainstorming-grilling/specs/brainstorming-grilling.md"
).read_text(encoding="utf-8")


def grilling_section(text: str) -> str:
    return text.split("## Grilling interaction method", 1)[1].split("## Exit conditions", 1)[0]


class BrainstormingGrillingContractTests(unittest.TestCase):
    def test_policy_local_grilling_sections_are_equivalent(self):
        self.assertIn("## Grilling interaction method", CHAT_BRAIN)
        self.assertIn("## Grilling interaction method", CODEX_BRAIN)
        self.assertEqual(grilling_section(CHAT_BRAIN), grilling_section(CODEX_BRAIN))

    def test_activation_is_semantic_and_lightweight_path_remains_legal(self):
        for text in (CHAT_BRAIN, CODEX_BRAIN):
            section = grilling_section(text)
            self.assertIn("ordinary lightweight Brainstorming", section)
            self.assertIn("unresolved user decisions depend on other user decisions", section)
            self.assertIn("goal is materially ambiguous", section)
            self.assertIn("multiple materially different solution paths", section)
            self.assertIn("Do not use a numeric question-count threshold", section)

    def test_grill_is_active_scope_only_and_never_intake(self):
        for text in (CHAT_BRAIN, CODEX_BRAIN):
            section = grilling_section(text)
            self.assertIn("currently active Brainstorming scope only", section)
            self.assertIn("does not create or recover a workstream", section)
            self.assertIn("is not an Intake directive", section)
            self.assertIn("If no active Brainstorming scope exists", section)

        for text in (CHAT_INTAKE, CODEX_INTAKE):
            self.assertIn("The explicit operator directives are:", text)
            self.assertIn("`#issue <problem>`", text)
            self.assertIn("`#feature <goal>`", text)
            self.assertIn("`#grill` is explicitly **not** an Intake directive", text)

        for text in (CHAT_ROUTER, CODEX_ROUTER):
            self.assertLess(text.index("#issue"), text.index("#grill"))
            self.assertIn("does not receive new-workstream operator-directive precedence", text)
            self.assertIn("Only the Brainstorming route may consume `#grill`", text)

    def test_frontier_questions_recommendations_and_fact_ownership(self):
        for text in (CHAT_BRAIN, CODEX_BRAIN):
            section = grilling_section(text)
            self.assertIn("prerequisites are already settled", section)
            self.assertIn("Ask the whole currently independent frontier in one round", section)
            self.assertIn("Number the questions", section)
            self.assertIn("explicit assistant recommendation for every question", section)
            self.assertIn("agent-findable facts", section)
            self.assertIn("recompute the decision tree/frontier before exposing any dependent question", section)

    def test_recovery_completion_stop_and_promotion_boundary(self):
        for text in (CHAT_BRAIN, CODEX_BRAIN):
            section = grilling_section(text)
            self.assertIn("full transient decision tree is working state", section)
            self.assertIn("accepted exploratory choices", section)
            self.assertIn("unresolved material decisions", section)
            self.assertIn("material dependency relations", section)
            self.assertIn("research needs/evidence obligations", section)
            self.assertIn("every material branch to be resolved or explicitly classified as deferred/non-blocking", section)
            self.assertIn("may stop grilling at any time", section)
            self.assertIn("unresolved material product/strategic blockers keep Brainstorming open", section)
            self.assertIn("marginal/non-blocking items may be recorded as deferred", section)
            self.assertIn("does not bypass the policy-owned Brainstorming → Project Definition promotion gate", section)

    def test_openspec_covers_behavior_and_scope_boundary(self):
        for phrase in (
            "MUST remain an interaction method inside Brainstorming",
            "MUST NOT create or recover a workstream",
            "dependency-aware decision tree",
            "assistant recommendation for each question",
            "MUST stop further grilling questions immediately",
            "`#issue` and `#feature` remain the only explicit new-workstream Intake directives",
            "`wait-what` remains outside this change",
        ):
            self.assertIn(phrase, OPENSPEC)

    def test_readme_exposes_manual_and_automatic_behavior(self):
        self.assertIn("`#grill` is **not Intake**", README)
        self.assertIn("automatically use grilling", README)
        self.assertIn("includes an assistant recommendation", README)
        self.assertIn("The user may stop grilling at any time", README)
        self.assertIn("Neither automatic grilling nor `#grill` changes", README)
        self.assertIn("Project Definition promotion gate", README)


if __name__ == "__main__":
    unittest.main()
