import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

BRAIN_FILES = {
    "chatgpt_only": ROOT / "workflow/chatgpt_only/BRAINSTORMING.md",
    "codex_only": ROOT / "workflow/codex_only/BRAINSTORMING.md",
    "legacy_mixed": ROOT / "workflow/BRAINSTORMING.md",
}
BRAIN = {name: path.read_text(encoding="utf-8") for name, path in BRAIN_FILES.items()}

CHAT_ROUTER = (ROOT / "workflow/chatgpt_only/ROUTER.md").read_text(encoding="utf-8")
CODEX_ROUTER = (ROOT / "workflow/codex_only/ROUTER.md").read_text(encoding="utf-8")
CHAT_INTAKE = (ROOT / "workflow/chatgpt_only/INTAKE.md").read_text(encoding="utf-8")
CODEX_INTAKE = (ROOT / "workflow/codex_only/INTAKE.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")

OPENSPEC = (
    ROOT
    / "openspec/changes/adaptive-brainstorming-grilling/specs/adaptive-brainstorming-grilling.md"
).read_text(encoding="utf-8")
HISTORICAL_OPENSPEC = (
    ROOT / "openspec/changes/brainstorming-grilling/specs/brainstorming-grilling.md"
).read_text(encoding="utf-8")

SCENARIOS = json.loads(
    (ROOT / "tests/fixtures/adaptive_brainstorming_grilling_scenarios.json").read_text(
        encoding="utf-8"
    )
)


def adaptive_section(text: str) -> str:
    return text.split("## Adaptive grilling interaction method", 1)[1].split(
        "## Exit conditions", 1
    )[0]


class AdaptiveBrainstormingGrillingContractTests(unittest.TestCase):
    def test_all_active_route_families_share_the_adaptive_interaction_contract(self):
        sections = {name: adaptive_section(text) for name, text in BRAIN.items()}
        self.assertEqual(sections["chatgpt_only"], sections["codex_only"])
        self.assertEqual(sections["chatgpt_only"], sections["legacy_mixed"])

        for section in sections.values():
            self.assertIn("default interaction method inside every Brainstorming scope", section)
            self.assertIn("no entry route or manual operator directive controls", section)
            self.assertIn("expected decision value of another sensible round", section)
            self.assertIn("Having enough information to implement is **not**", section)
            self.assertIn("fixed minimum/maximum question count or round count", section)

    def test_dependency_frontier_lenses_batching_and_recommendations_are_explicit(self):
        for text in BRAIN.values():
            section = adaptive_section(text)
            self.assertIn("transient dependency-aware decision tree", section)
            self.assertIn("prerequisites are already settled", section)
            self.assertIn("adaptive internal lenses", section)
            self.assertIn("rigid user-facing checklist", section)
            self.assertIn("coherent thematic batch", section)
            self.assertIn("Split a large frontier into digestible groups", section)
            self.assertIn("Number each material decision question", section)
            self.assertIn("explicit assistant recommendation", section)
            self.assertIn("recompute the decision tree/frontier", section)

    def test_research_challenge_reopening_and_recovery_semantics_are_explicit(self):
        for text in BRAIN.values():
            section = adaptive_section(text)
            self.assertIn("Keep agent-findable facts agent-owned", section)
            self.assertIn("applicable Research route", section)
            self.assertIn("one bounded adversarial/counterfactual challenge", section)
            self.assertIn("materially new evidence, contradiction or changed context", section)
            self.assertIn("challenge/reopening state", section)
            self.assertIn("full transient decision tree is working state", section)
            self.assertIn("persisted conversation transcript", section)

    def test_completion_and_user_stop_close_the_shallow_exit_loophole(self):
        for text in BRAIN.values():
            section = adaptive_section(text)
            self.assertIn("bounded completion audit", section)
            self.assertIn("one final challenge/discovery pass", section)
            self.assertIn("low expected value", section)
            self.assertIn("halts new Brainstorming questions immediately", section)
            self.assertIn("unresolved material product/strategic blockers", section)
            self.assertIn("prevent it from being treated as ready to leave Brainstorming", section)
            self.assertIn("does not bypass the active route's existing promotion/authority boundary", section)

    def test_manual_grilling_operator_is_absent_from_active_surfaces(self):
        active_surfaces = {
            **BRAIN,
            "chatgpt_router": CHAT_ROUTER,
            "codex_router": CODEX_ROUTER,
            "chatgpt_intake": CHAT_INTAKE,
            "codex_intake": CODEX_INTAKE,
            "readme": README,
        }
        for name, text in active_surfaces.items():
            self.assertNotIn("#grill", text, msg=f"manual operator leaked into {name}")

        # Historical provenance is deliberately retained rather than rewritten.
        self.assertIn("#grill", HISTORICAL_OPENSPEC)

        for text in (CHAT_INTAKE, CODEX_INTAKE):
            self.assertIn("The explicit operator directives are:", text)
            self.assertIn("#issue <problem>", text)
            self.assertIn("#feature <goal>", text)

    def test_new_openspec_covers_r2_without_new_runtime_or_authority_layer(self):
        required = (
            "Every active Project Workflow Brainstorming route MUST use adaptive grilling",
            "expected decision value",
            "MUST NOT define a fixed minimum or maximum question count or round count",
            "dependency-aware tree",
            "adaptive internal lenses",
            "coherent thematic batches",
            "explicit assistant recommendation",
            "same exploratory subject",
            "one bounded adversarial/counterfactual challenge",
            "full transient decision tree and conversation transcript MUST NOT",
            "bounded audit across the relevant decision surface",
            "MUST halt new Brainstorming questions immediately",
            "legacy/mixed",
            "manual grilling operator directive MUST NOT remain",
            "explicit Brainstorming → Project Definition promotion gate",
            "wait-what",
        )
        for phrase in required:
            self.assertIn(phrase, OPENSPEC)

    def test_simple_scenario_can_finish_after_one_audited_round(self):
        scenario = SCENARIOS["simple_scope"]
        self.assertEqual(len(scenario["user_rounds"]), 1)
        round_1 = scenario["user_rounds"][0]
        self.assertTrue(round_1["questions_numbered"])
        self.assertTrue(round_1["recommendations_present"])
        self.assertEqual(scenario["completion_audit"]["remaining_material_decisions"], [])
        self.assertEqual(scenario["final_discovery_pass"]["new_material_decisions"], [])
        self.assertEqual(scenario["expected"], "completion_eligible")

    def test_dependency_rich_scenario_requires_successive_frontier_rounds(self):
        scenario = SCENARIOS["dependency_rich_scope"]
        self.assertGreaterEqual(len(scenario["user_rounds"]), 3)

        dependencies = scenario["dependencies"]
        settled = set()
        frontiers = []
        for round_data in scenario["user_rounds"]:
            frontier = round_data["frontier"]
            frontiers.append(tuple(frontier))
            self.assertTrue(round_data["questions_numbered"])
            self.assertTrue(round_data["recommendations_present"])

            for decision in frontier:
                self.assertTrue(
                    set(dependencies[decision]).issubset(settled),
                    msg=f"{decision} exposed before prerequisites were settled",
                )
            self.assertEqual(set(round_data["challenge_after_settlement"]), set(frontier))
            settled.update(frontier)

        self.assertEqual(len(frontiers), len(set(frontiers)))
        self.assertEqual(set(settled), set(dependencies))
        self.assertEqual(scenario["completion_audit"]["remaining_material_decisions"], [])
        self.assertEqual(scenario["final_discovery_pass"]["new_material_decisions"], [])

    def test_research_stop_and_reopening_scenarios_preserve_boundaries(self):
        research = SCENARIOS["research_interleave"]
        self.assertEqual(research["research_origin_subject"], research["research_return_subject"])
        self.assertEqual(research["frontier_before_research"], research["frontier_after_research"])
        self.assertEqual(research["expected"], "resume_same_exploratory_subject")

        stop = SCENARIOS["user_stop_with_blocker"]
        self.assertTrue(stop["clear_stop"])
        self.assertEqual(stop["new_questions_after_stop"], 0)
        self.assertTrue(stop["unresolved_material_blockers"])
        self.assertEqual(stop["expected"], "tentative_not_ready")

        reopening = SCENARIOS["evidence_reopening"]
        self.assertEqual(reopening["bounded_challenges_before_new_evidence"], 1)
        self.assertTrue(reopening["new_material_evidence"])
        self.assertTrue(reopening["choice_reopened"])
        self.assertTrue(reopening["dependent_frontier_recomputed"])

    def test_policy_local_research_and_definition_promotion_mechanics_remain(self):
        for name in ("chatgpt_only", "codex_only"):
            text = BRAIN[name]
            self.assertIn("Return target", text)
            self.assertIn("brainstorming:<scope-id>@<revision>", text)
            self.assertIn("ready for Project Definition", text)
            self.assertIn("does **not** by itself authorize leaving Brainstorming", text)
            self.assertIn("Do not treat research completion", text)

    def test_readme_describes_intrinsic_adaptive_behavior(self):
        self.assertIn("Every active Brainstorming route uses adaptive dependency-aware grilling by default", README)
        self.assertIn("expected decision value of another round", README)
        self.assertIn("completion audit", README)
        self.assertIn("one bounded counterfactual challenge", README)
        self.assertIn("merely knowing enough to implement is not sufficient", README)
        self.assertIn("Project Definition promotion gate remains unchanged", README)


if __name__ == "__main__":
    unittest.main()
