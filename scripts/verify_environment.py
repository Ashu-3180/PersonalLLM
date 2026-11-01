"""Print interpreter and workspace facts. Uses only the standard library."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from personalllm import __version__  # noqa: E402
from personalllm.config import load_config  # noqa: E402


def main() -> int:
    print(f"python_version={sys.version}")
    print(f"executable={sys.executable}")
    print(f"prefix={sys.prefix}")
    print(f"base_prefix={sys.base_prefix}")
    print(f"project_root={PROJECT_ROOT}")
    print(f"package_version={__version__}")
    print(f"milestone={load_config()['project']['milestone']}")
    print(f"venv_active={sys.prefix != sys.base_prefix}")
    if sys.version_info[:2] != (3, 14):
        print("ERROR: expected Python 3.14.x", file=sys.stderr)
        return 1
    expected_venv = PROJECT_ROOT / ".venv"
    if Path(sys.prefix).resolve() != expected_venv.resolve():
        print(
            f"WARNING: interpreter prefix is not {expected_venv}",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
