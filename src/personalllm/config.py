"""Load the M0 TOML configuration using the standard library only."""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

from personalllm.paths import DEFAULT_CONFIG_PATH, PROJECT_ROOT


def load_config(path: str | Path | None = None) -> dict[str, Any]:
    """Read a TOML config file and return a nested dictionary.

    Defaults to ``configs/default.toml`` at the project root.
    """
    config_path = Path(path) if path is not None else DEFAULT_CONFIG_PATH
    if not config_path.is_file():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with config_path.open("rb") as handle:
        data = tomllib.load(handle)

    data["_meta"] = {
        "config_path": str(config_path.resolve()),
        "project_root": str(PROJECT_ROOT),
    }
    return data
