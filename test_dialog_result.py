"""DialogResult behaves as a string on every supported Python.

On Python < 3.11 gui_builder defines its own StrEnum (frozen apps could not
package backports.strenum). Run this file under 3.8/3.10 as well as 3.11+.
"""

import ast
from pathlib import Path

import gui_builder
from gui_builder import CANCEL, OK, DialogResult


def test_dialog_result_is_its_string_value():
    assert OK == "ok"
    assert str(OK) == "ok"
    assert f"{CANCEL}" == "cancel"
    assert DialogResult("yes") is DialogResult.YES
    assert isinstance(DialogResult.NO, str)


def test_no_backports_import():
    tree = ast.parse(Path(gui_builder.__file__).read_text(encoding="utf-8"))
    modules = {
        node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)
    } | {
        alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names
    }
    assert not any(name and name.startswith("backports") for name in modules)
