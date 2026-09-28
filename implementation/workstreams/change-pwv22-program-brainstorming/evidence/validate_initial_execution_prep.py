#!/usr/bin/env python3
"""Read-only snapshot audit for P2 Initial Prep, NOT a workflow router/state owner.

Usage: python3 .../validate_initial_execution_prep.py --governor /verified/package
Optional --root validates an exported readback; --consumer-git-root supplies the
consumer object database. --remote-expected COMMIT also verifies remote HEADs.
No inference, product implementation, donor regression, or canonical mutation.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tomllib
from unittest.mock import patch

W = "implementation/workstreams/change-pwv22-program-brainstorming"
E = W + "/evidence"
WS = "change-pwv22-program-brainstorming"
GOV = "4fb4bfb7d7b1481d6f347c182fc96a5a1135e045"
CARDS = (
    "M01-S01-T01", "M01-S01-T02", "M01-S02-T01", "M01-S02-T02",
    "M01-S03-T01", "M01-S04-T01", "M01-S04-T02", "M04-S19-T01",
    "M04-S20-T01", "M04-S21-T01", "M04-S22-T01", "M04-S23-T01",
)
TRIGGERS = (
    "J-S05", "J-S06", "J-S07", "J-S08", "J-S09", "J-S10-RECOVERY",
    "J-S10-EFFECTS", "J-S10-EVOLUTION", "J-S10-CLOSE", "J-S11",
    "J-S12", "J-S13", "J-S14", "J-S15-DISTRIBUTION", "J-S15-TARGET",
    "J-S16", "J-S17", "J-S18", "J-S20-CLEANUP", "J-S23-REPAIRS",
    "J-S23-INTEGRATE", "J-S23-IMPACT", "J-S24", "J-S25", "J-S26",
)
CONDITIONS = (
    "Producer(s):", "Missing future fact:", "Material effect on Card shape:",
    "Earliest deterministic consumption:", "Bounded refinement envelope:",
    "Must NOT guess:", "Required acceptance surface:", "Satisfaction guard:",
)


def require(value, message):
    if not value:
        raise ValueError(message)


def git(root, *args):
    return subprocess.check_output(
        ["git", "-C", str(root), *args], text=True, timeout=30
    ).strip()


def blob(content):
    return hashlib.sha1(f"blob {len(content)}\0".encode() + content).hexdigest()


def acyclic(graph):
    visited, active = set(), set()

    def visit(node):
        require(node not in active, f"dependency cycle at {node}")
        if node in visited:
            return
        active.add(node)
        for parent in graph.get(node, []):
            visit(parent)
        active.remove(node)
        visited.add(node)
    for node in graph:
        visit(node)


def rejects(operation, name):
    try:
        operation()
    except (ValueError, KeyError):
        return name
    raise ValueError("negative audit did not reject: " + name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--consumer-git-root", type=Path)
    parser.add_argument("--governor", required=True, type=Path)
    parser.add_argument("--remote-expected")
    args = parser.parse_args()
    root = args.root.resolve()
    consumer = (args.consumer_git_root or root).resolve()
    governor = args.governor.resolve()
    inputs = tomllib.loads((root / E / "INITIAL_EXECUTION_PREP_INPUTS.toml").read_text())
    require(git(governor, "rev-parse", "HEAD") == GOV, "wrong governing checkout")
    for db, repository in ((consumer, inputs["consumer_repository"]), (governor, inputs["governing_repository"])):
        require(git(db, "remote", "get-url", "origin") in {
            f"https://github.com/{repository}.git", f"git@github.com:{repository}.git"
        }, "object database origin does not match declared repository")
    checked_pins = 0
    for group in ("authority", "evidence", "governor", "donor_candidate"):
        for pin in inputs[group]:
            db = consumer if pin["repository"] == inputs["consumer_repository"] else governor
            require(git(db, "rev-parse", f"{pin['commit']}:{pin['path']}") == pin["blob"],
                    "wrong immutable pin: " + pin["path"])
            require(git(db, "cat-file", "-t", pin["blob"]) == "blob", "non-blob pin")
            if group == "authority" or (group == "evidence" and pin["path"].startswith("definition/")):
                anchor = inputs["handoff_commit"]
            elif group == "evidence":
                anchor = inputs["consumer_donor_close_commit"]
            elif group == "governor":
                anchor = GOV
            else:
                anchor = inputs["product_donor_commit"]
            git(db, "merge-base", "--is-ancestor", pin["commit"], anchor)
            if group in {"authority", "governor"}:
                serving = root if group == "authority" else governor
                require(blob((serving / pin["path"]).read_bytes()) == pin["blob"],
                        "wrong serving bytes: " + pin["path"])
            checked_pins += 1
    # Import only the verified current governor, never donor or consumer legacy tools.
    sys.path.insert(0, str(governor))
    from tools import state_contract as state
    from tools.router import Reads, refresh_ready_card, select_route

    manifest = state.read_toml(root / W / "WORKSTREAM.toml")
    board = state.read_toml(root / W / "TASK_BOARD.toml")
    state.validate_project(state.read_project(root / "PROJECT.md"))
    state.validate_workstream(manifest)
    state.validate_board(board, manifest, expected_revision=1)
    require(tuple(c["id"] for c in board["cards"]) == CARDS, "unexpected Card inventory")
    require(tuple(t["id"] for t in board["jit_triggers"]) == TRIGGERS, "unexpected JIT inventory")
    require(set(p.stem for p in (root / W / "cards").glob("*.md")) == set(CARDS),
            "placeholder/unregistered Card file")
    for prohibited in ("results", "reviews", "specification", "oracle", "donor", "delivery", "qualification"):
        require(not (root / W / prohibited).exists(), "Execution output was created: " + prohibited)
    require(not any(k.startswith("premium_d") for k in board), "native D in current governor")
    contract_paths, outputs = set(), set()
    texts = {}
    for card in board["cards"]:
        cid = card["id"]
        text = (root / card["contract"]["path"]).read_text()
        texts[cid] = text
        parsed = state.parse_task_card(text, cid, WS)
        require(not parsed["dependencies"], "Initial Prep fabricated a predecessor Result")
        require("result" not in card and not card.get("review_attempts"), "Execution evidence published")
        expected_status = "ready" if cid.startswith("M01-") else "planned"
        require(card["status"] == expected_status, "wrong prepared status: " + cid)
        for pin in inputs["authority"]:
            require(pin["path"] in parsed["authority_refs"], "missing authority path: " + cid)
            require(pin["commit"] in text and pin["blob"] in text, "missing exact authority: " + cid)
        if card["status"] == "ready":
            require("Required predecessor seams: none" in text, "ready with unresolved producer")
            refresh_ready_card(Reads(root, governor), board, manifest, card)
        else:
            require("**Launch prohibition:**" in text and "result-path@40hex-commit:40hex-blob" in text,
                    "unbound planned Card lacks mandatory exact launch refinement")
            require("Required predecessor seams: none" not in text, "planned input omitted")
        for heading in ("## Exact authority bindings", "## Launch bindings", "## Required verification",
                        "## Review surface", "## Runtime-neutral execution guidance"):
            require(heading in text, "incomplete Card: " + cid + " " + heading)
        require("No future commit or blob has been invented" in text, "ambiguous dependency status")
        if parsed["technical_contract"]:
            require((root / parsed["technical_contract"]).is_file(), "missing technical contract")
            contract_paths.add(parsed["technical_contract"])
        write_block = text.split("Bounded consumer outputs (repository-relative):\n", 1)[1].split("\n\n", 1)[0]
        for path in re.findall(r"^- `([^`]+)`$", write_block, re.M):
            require(path not in outputs, "duplicated owned output: " + path)
            require(path.startswith(W + "/"), "output outside selected workstream")
            outputs.add(path)
    require(len(contract_paths) == 3, "wrong selective technical contract inventory")
    for trigger in board["jit_triggers"]:
        require(trigger["state"] == "waiting", "premature trigger satisfaction")
        require(all(label in trigger["condition"] for label in CONDITIONS), "incomplete trigger condition")
        require("not only after_card DONE" in trigger["condition"], "ancestor anchor mistaken for producer proof")

    # Reconstruct seam dependencies from the accepted P2 input column, not this guide.
    plan = (root / "planning/PWV22_PROGRAM_MASTER_PLAN_P2.md").read_text()
    graph = {}
    for line in plan.splitlines():
        match = re.match(r"\| (S\d{2}) —", line)
        if match:
            node = match.group(1)
            graph[node] = set(re.findall(r"\bS\d{2}\b", line.split("|")[-2])) - {node}
    require(set(graph) == {f"S{i:02d}" for i in range(1, 27)}, "P2 seam coverage missing")
    acyclic(graph)
    coverage = []
    for line in plan.splitlines():
        match = re.match(r"\| (\d+)(?:–(\d+))? \|", line)
        if match:
            lo = int(match.group(1)); hi = int(match.group(2) or lo)
            coverage.extend(range(lo, hi + 1))
    require(sorted(coverage) == list(range(1, 98)), "P2 1–97 coverage lost/duplicated")
    guide = (root / E / "INITIAL_EXECUTION_PREP_GUIDANCE.md").read_text()
    require(set(re.findall(r"^\| (S\d{2}) \|", guide, re.M)) == set(graph), "missing final seam classification")
    for t in TRIGGERS:
        require(t in guide, "guide omits trigger: " + t)
    for i in range(1, 11):
        require(f"R{i:02d}" in guide, "missing Review surface")
    for i in range(1, 8):
        require(f"### H{i:02d} —" in guide, "missing hypothesis")

    # Verify terminal donor proof, including its internally pinned Board/review/evidence.
    dw = "implementation/workstreams/change-pwv21-policy-kernel-brainstorming"
    close = inputs["consumer_donor_close_commit"]
    pkg = tomllib.loads(git(consumer, "show", f"{close}:{dw}/evidence/PRE_M03_TERMINAL_DONOR_PACKAGE.toml"))
    require(pkg["status"] == "terminal" and not pkg["m03_materialized"], "nonterminal donor")
    require(pkg["product_donor_commit"] == inputs["product_donor_commit"], "wrong product donor")
    require(pkg["superseding_program_commit"] == inputs["handoff_commit"], "wrong superseding handoff")
    for key in ("task_board", "milestone_review", "milestone_evidence"):
        require(git(consumer, "rev-parse", f"{pkg['source_snapshot_commit']}:{pkg[key+'_path']}") == pkg[key+"_blob"],
                "donor package internal mismatch: " + key)
    donor_board = tomllib.loads(git(consumer, "show", f"{pkg['source_snapshot_commit']}:{pkg['task_board_path']}"))
    require(donor_board["revision"] == 275 and len(donor_board["cards"]) == 46, "wrong donor Board")
    require(all(c["status"] == "done" and not c["id"].startswith("M03") for c in donor_board["cards"]),
            "donor reopened/not complete")
    review = tomllib.loads(git(consumer, "show", f"{pkg['source_snapshot_commit']}:{pkg['milestone_review_path']}"))
    require(review["verdict"] == "green" and review["subject"]["blob"] == pkg["task_board_blob"], "wrong donor verdict")
    subject = review["subject"]
    require(git(consumer, "rev-parse", f"{subject['commit']}:{subject['path']}") == subject["blob"],
            "donor review subject does not resolve")

    route = select_route(root, [W + "/WORKSTREAM.toml"], package_root=governor)
    require(route.disposition == "route" and route.obligation == "execution_prep", "wrong prepared route")
    negative = []
    negative.append(rejects(lambda: state.validate_board(board, manifest, expected_revision=0), "stale Board revision"))
    bad = copy.deepcopy(board); bad["cards"][1]["id"] = bad["cards"][0]["id"]
    negative.append(rejects(lambda: state.validate_board(bad, manifest), "duplicate Card"))
    bad = copy.deepcopy(board); bad["jit_triggers"][0]["after_card"] = "nonexistent"
    negative.append(rejects(lambda: state.validate_board(bad, manifest), "placeholder trigger predecessor"))
    bad = copy.deepcopy(board); bad["jit_triggers"][0]["state"] = "satisfied"
    negative.append(rejects(lambda: state.validate_board(bad, manifest), "premature trigger satisfaction"))
    bad = copy.deepcopy(board); bad["cards"][0]["status"] = bad["cards"][1]["status"] = "in_progress"
    negative.append(rejects(lambda: state.validate_board(bad, manifest), "multiple active program Cards"))
    negative.append(rejects(lambda: state.parse_task_card(texts[CARDS[0]].replace("- Dependencies: none", "- Dependencies: future-result"), CARDS[0], WS), "fabricated dependency"))
    negative.append(rejects(lambda: acyclic({"a": {"b"}, "b": {"a"}}), "dependency cycle"))
    # The current governor rejects exact-shaped dependency refs not owned by a DONE predecessor.
    bad = copy.deepcopy(board)
    fake = texts[CARDS[0]].replace("- Dependencies: none", f"- Dependencies: {W}/results/nonexistent.md@{'a'*40}:{'b'*40}")
    parsed = state.parse_task_card(fake, CARDS[0], WS)
    require(bool(parsed["dependencies"]), "negative dependency fixture not exercised")
    with patch("tools.router.parse_task_card", return_value=parsed):
        negative.append(rejects(
            lambda: refresh_ready_card(Reads(root, governor), bad, manifest, bad["cards"][0]),
            "exact-shaped absent Result",
        ))

    remote = {}
    if args.remote_expected:
        checks = (
            (consumer, "origin", "refs/heads/work/pwv22-program-brainstorming", args.remote_expected),
            (consumer, "origin", "refs/heads/work/pwv21-policy-kernel-brainstorming", close),
            (governor, "origin", "refs/heads/main", GOV),
            (governor, "origin", "refs/heads/work/pwv21-policy-kernel", inputs["product_donor_commit"]),
        )
        for db, origin, ref, expected in checks:
            rows = git(db, "ls-remote", origin, ref).splitlines()
            require(len(rows) == 1 and rows[0].split()[0] == expected, "remote moved: " + ref)
            repository = inputs["consumer_repository"] if db == consumer else inputs["governing_repository"]
            remote[repository + ":" + ref] = expected
    paths = [W + "/WORKSTREAM.toml", W + "/TASK_BOARD.toml"]
    paths += [c["contract"]["path"] for c in board["cards"]]
    paths += sorted(contract_paths)
    paths += sorted(str(p.relative_to(root)) for p in (root / E).glob("INITIAL_EXECUTION_PREP_*"))
    paths += [E + "/validate_initial_execution_prep.py"]
    inventory = {path: blob((root / path).read_bytes()) for path in sorted(set(paths))}
    print(json.dumps({
        "audit": "PASS", "scope": "Initial Prep snapshot only; not product/donor execution or independent Review",
        "board_revision": board["revision"], "cards": len(CARDS), "ready": 7, "planned": 5,
        "first_ready": CARDS[0], "waiting_jit_triggers": len(TRIGGERS),
        "technical_contracts": sorted(contract_paths), "checked_immutable_pins": checked_pins,
        "p2_seams": len(graph), "p2_requirement_coverage": len(coverage),
        "cycles": 0, "negative_checks": negative, "donor_gate": "verified_terminal",
        "route": {"disposition": route.disposition, "obligation": route.obligation, "subject": route.subject},
        "remote_heads": remote, "prepared_file_blobs": inventory,
    }, indent=2))


if __name__ == "__main__":
    main()
