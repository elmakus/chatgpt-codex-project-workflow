from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

AUTHORITY = (ROOT / "workflow/common/AUTHORITY.md").read_text(encoding="utf-8")
CHAT_ROUTER = (ROOT / "workflow/chatgpt_only/ROUTER.md").read_text(encoding="utf-8")
CODEX_ROUTER = (ROOT / "workflow/codex_only/ROUTER.md").read_text(encoding="utf-8")
CHAT_PLANNING = (ROOT / "workflow/chatgpt_only/PLANNING.md").read_text(encoding="utf-8")
CODEX_PLANNING = (ROOT / "workflow/codex_only/PLANNING.md").read_text(encoding="utf-8")
CHAT_REVIEW = (ROOT / "workflow/chatgpt_only/REVIEW.md").read_text(encoding="utf-8")
CODEX_REVIEW = (ROOT / "workflow/codex_only/REVIEW.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")


def yagni_section(text: str) -> str:
    return text.split("## YAGNI / proportional design", 1)[1].split("## Progressive disclosure", 1)[0]


class YagniProportionalDesignContractTests(unittest.TestCase):
    def test_common_authority_is_the_canonical_full_invariant(self):
        self.assertEqual(AUTHORITY.count("## YAGNI / proportional design"), 1)
        section = yagni_section(AUTHORITY)
        for phrase in (
            "least-complex solution",
            "speculative abstractions",
            "Every material increase in solution complexity must have a concrete current justification",
            "“Maybe later” alone is insufficient",
            "least unnecessary complexity",
            "YAGNI never permits omitting or weakening current correctness",
            "Prefer an existing fitting mechanism",
            "demonstrated current shared need/variation",
            "Keep changes focused",
        ):
            self.assertIn(phrase, section)

    def test_quality_and_no_new_machinery_guardrails_are_explicit(self):
        section = yagni_section(AUTHORITY)
        for phrase in (
            "security",
            "testing",
            "maintainability/refactoring",
            "compatibility",
            "observability",
            "migration",
            "Do not create a YAGNI-specific lifecycle phase",
            "complexity score/budget",
            "numeric abstraction threshold",
        ):
            self.assertIn(phrase, section)

    def test_both_fixed_policy_routers_bootstrap_common_authority(self):
        for text in (CHAT_ROUTER, CODEX_ROUTER):
            self.assertIn("workflow/common/AUTHORITY.md", text)

    def test_planning_applies_current_justification_question_without_copying_full_contract(self):
        for text in (CHAT_PLANNING, CODEX_PLANNING):
            self.assertIn("workflow/common/AUTHORITY.md#YAGNI--proportional-design", text)
            self.assertIn("For each material increase in solution complexity", text)
            self.assertIn("hypothetical future need alone is insufficient", text)
            self.assertNotIn("## YAGNI / proportional design", text)

    def test_review_rejects_speculation_without_weakening_current_obligations(self):
        for text in (CHAT_REVIEW, CODEX_REVIEW):
            self.assertIn("YAGNI/proportional-design invariant", text)
            self.assertIn("Unjustified speculative complexity is a review defect", text)
            self.assertIn("demonstrated current reuse", text)
            self.assertIn("Do not use YAGNI to reject complexity required by current authority/evidence", text)
            self.assertIn("or to weaken current quality obligations", text)
            self.assertNotIn("## YAGNI / proportional design", text)

    def test_readme_exposes_the_principle_without_becoming_a_second_contract(self):
        self.assertIn("one policy-neutral YAGNI / proportional-design rule from common authority", README)
        self.assertIn("material extra complexity needs a concrete current justification", README)


if __name__ == "__main__":
    unittest.main()
