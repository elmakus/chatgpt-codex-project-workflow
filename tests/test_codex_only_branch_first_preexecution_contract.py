from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

FILES = {
    name: (ROOT / "workflow/codex_only" / name).read_text(encoding="utf-8")
    for name in (
        "BRAINSTORMING.md",
        "RESEARCH.md",
        "DEFINITION.md",
        "PLANNING.md",
        "PLAN_REVIEW.md",
        "ROUTER.md",
        "WORKSTREAMS.md",
        "EXECUTION_PREP.md",
        "EXECUTION.md",
        "STATE.md",
        "REVIEW.md",
    )
}


class CodexOnlyBranchFirstPreExecutionTests(unittest.TestCase):
    def test_brainstorming_scope_and_research_are_manifest_local(self):
        brainstorming = FILES["BRAINSTORMING.md"]
        self.assertIn("## Durable active scope", brainstorming)
        self.assertIn("routing.exploratory_scope", brainstorming)
        self.assertIn("routing.research_obligation", brainstorming)
        self.assertNotIn("PROJECT.md → Active exploratory scope", brainstorming)
        self.assertNotIn("PROJECT.md → Active research obligation", brainstorming)

    def test_research_ownership_is_split_by_lifecycle(self):
        research = FILES["RESEARCH.md"]
        self.assertIn("selected workstream manifest → `routing.research_obligation`", research)
        self.assertIn("selected canonical Task Board → `research_obligation`", research)
        self.assertIn(
            "Never mirror a Research obligation into root `PROJECT.md`",
            research,
        )
        self.assertIn(
            "Never place implementation/recovery Research in manifest `routing.research_obligation`",
            research,
        )
        self.assertNotIn("PROJECT.md → Active research obligation", research)

    def test_definition_and_planning_research_use_manifest_locator(self):
        definition = FILES["DEFINITION.md"]
        planning = FILES["PLANNING.md"]
        self.assertIn(
            "selected workstream manifest `routing.research_obligation`",
            definition,
        )
        self.assertIn(
            "selected workstream manifest `routing.research_obligation`",
            planning,
        )
        self.assertIn(
            "selected-workstream-manifest pre-execution routing",
            definition,
        )
        self.assertIn(
            "selected-Task-Board implementation/recovery state",
            definition,
        )
        self.assertNotIn("pre-execution PROJECT state", definition)
        self.assertNotIn("PROJECT.md → Active research obligation", definition)
        self.assertNotIn("PROJECT.md → Active research obligation", planning)

    def test_plan_review_is_manifest_located_but_record_owned(self):
        planning = FILES["PLANNING.md"]
        review = FILES["PLAN_REVIEW.md"]
        self.assertIn("routing.plan_review", planning)
        self.assertIn("routing.plan_review", review)
        self.assertIn("review record remains sole owner", review)
        self.assertIn("Codex Main validates", review)
        self.assertIn("Tester independent", review)
        self.assertIn(
            "do not clear manifest `routing.plan_review` in the Tester role",
            review,
        )

    def test_router_uses_manifest_preexecution_locators(self):
        router = FILES["ROUTER.md"]
        self.assertIn("routing.exploratory_scope", router)
        self.assertIn("routing.research_obligation", router)
        self.assertIn("routing.plan_review", router)
        self.assertIn(
            "Historical root `PROJECT.md` exploratory/Research pointers",
            router,
        )
        self.assertNotIn("PROJECT.md → Active exploratory scope", router)
        self.assertNotIn("PROJECT.md → Active research obligation", router)

    def test_locator_lifecycle_is_fail_closed(self):
        workstreams = FILES["WORKSTREAMS.md"]
        self.assertIn("Locator lifecycle is fail-closed and artifact-first", workstreams)
        self.assertIn("the Tester never clears it", workstreams)
        self.assertIn("route to Recovery", workstreams)
        self.assertIn("repository-global mutable registry", workstreams)

    def test_codex_main_and_tester_ownership_remain_intact(self):
        self.assertIn(
            "Codex Main remains the sole writer of shared Task Board/integration state",
            FILES["EXECUTION_PREP.md"],
        )
        self.assertIn(
            "Codex Main alone writes shared Task Board/integration state",
            FILES["EXECUTION.md"],
        )
        self.assertIn(
            "Codex Main is the sole writer of shared Project Workflow Task Board and integration state",
            FILES["STATE.md"],
        )
        self.assertIn("independent Tester", FILES["REVIEW.md"])
        self.assertIn("Tester does not repair production", FILES["EXECUTION.md"])

    def test_bounded_batch_contract_remains_present(self):
        prep = FILES["EXECUTION_PREP.md"]
        execution = FILES["EXECUTION.md"]
        state = FILES["STATE.md"]
        self.assertIn("Serial execution is always the safe/default shape", prep)
        self.assertIn("Freeze batch state", prep)
        self.assertIn("Bounded same-member retry", execution)
        self.assertIn("post-batch review drain", execution)
        self.assertIn("current parallel batch", state)
        self.assertIn("post-batch review drain", state)

    def test_codex_only_lifecycle_does_not_import_chatgpt_only_modules(self):
        for name, text in FILES.items():
            self.assertNotIn(
                "workflow/chatgpt_only/",
                text,
                msg=f"{name} imports ChatGPT-only lifecycle semantics",
            )


if __name__ == "__main__":
    unittest.main()
