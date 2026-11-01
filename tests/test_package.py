"""Scaffold tests that do not depend on third-party packages."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
_SRC = _PROJECT_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from personalllm import __version__, load_config
from personalllm.paths import PROJECT_ROOT


class PackageTests(unittest.TestCase):
    def test_version(self) -> None:
        self.assertEqual(__version__, "0.0.1")

    def test_interpreter_is_python_3_14(self) -> None:
        self.assertEqual(sys.version_info[:2], (3, 14), sys.version)

    def test_project_root_resolves_from_package_location(self) -> None:
        expected_root = Path(__file__).resolve().parents[1]
        self.assertEqual(PROJECT_ROOT, expected_root)
        self.assertTrue((PROJECT_ROOT / "pyproject.toml").is_file())
        self.assertTrue((PROJECT_ROOT / "configs" / "default.toml").is_file())

    def test_default_config_loads(self) -> None:
        config = load_config()
        self.assertEqual(config["project"]["milestone"], "M0")
        self.assertEqual(config["runtime"]["device"], "cpu")
        self.assertEqual(config["model"]["architecture"], "decoder-only-transformer")
        self.assertEqual(config["training"]["objective"], "causal-next-token-prediction")

    def test_missing_config_raises(self) -> None:
        missing = PROJECT_ROOT / "configs" / "does-not-exist.toml"
        with self.assertRaises(FileNotFoundError):
            load_config(missing)


if __name__ == "__main__":
    unittest.main()
