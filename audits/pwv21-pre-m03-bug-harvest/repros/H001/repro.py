#!/usr/bin/env python3
"""H001 checkout reproducer. Mutates only a temporary copy of the router fixture.

Usage:
    python3 repro.py /path/to/project_workflow_v2_checkout
"""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("usage: repro.py /path/to/project_workflow_v2_checkout")

repo = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(repo))

from tools.router import select_route  # noqa: E402

manifest = "implementation/workstreams/sample-workstream/WORKSTREAM.toml"
board_rel = "implementation/workstreams/sample-workstream/TASK_BOARD.toml"
blocker_rel = "implementation/workstreams/sample-workstream/blockers/M01-T04.toml"
fixture = repo / "tests/fixtures/router/valid-project"

with tempfile.TemporaryDirectory() as td:
    project = Path(td) / "project"
    shutil.copytree(fixture, project)

    board = project / board_rel
    text = board.read_text(encoding="utf-8")
    assert 'status = "in_progress"' in text
    assert "[cards.blocker]" not in text
    text = text.replace(
        "[cards.contract]\n",
        "[cards.blocker]\n"
        'class = "blocker"\n'
        f'path = "{blocker_rel}"\n\n'
        "[cards.contract]\n",
        1,
    )
    board.write_text(text, encoding="utf-8")

    blocker = project / blocker_rel
    blocker.parent.mkdir(parents=True, exist_ok=True)
    blocker.write_text(
        'workstream_id = "sample-workstream"\n'
        'card_id = "M01-T04"\n'
        'class = "human_authority"\n'
        'summary = "Human authorization is unresolved."\n'
        'evidence_path = ""\n',
        encoding="utf-8",
    )

    routed = select_route(project, [manifest], package_root=repo)
    print("disposition=", routed.disposition)
    print("obligation=", routed.obligation)
    print("subject=", routed.subject)
    print("read_set=", routed.read_set)
    print("blocker_read=", f"project:{blocker_rel}" in routed.read_set)

    assert (routed.disposition, routed.obligation) == ("route", "execution")
    assert f"project:{blocker_rel}" not in routed.read_set
