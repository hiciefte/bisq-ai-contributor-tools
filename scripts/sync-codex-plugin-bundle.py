#!/usr/bin/env python3
"""Build the Codex marketplace plugin bundle from repository source files."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "plugins" / "bisq-dev-tools"

DIRS = (
    ".codex-plugin",
    "commands",
    "skills",
)

FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    "INSTALLATION.md",
    "LICENSE",
    "README.md",
)


def main() -> None:
    if BUNDLE.exists():
        shutil.rmtree(BUNDLE)
    BUNDLE.mkdir(parents=True)

    for directory in DIRS:
        shutil.copytree(ROOT / directory, BUNDLE / directory)

    for file_name in FILES:
        shutil.copy2(ROOT / file_name, BUNDLE / file_name)

    print(f"Synced Codex plugin bundle: {BUNDLE}")


if __name__ == "__main__":
    main()
