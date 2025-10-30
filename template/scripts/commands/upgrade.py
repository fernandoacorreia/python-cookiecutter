from __future__ import annotations

import argparse

from .utils import run_command


def add_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    """Add upgrade command parser."""
    upgrade_help = """Upgrade all dependencies to their latest allowed versions.

This command runs: uv sync --upgrade --all-extras --dev

This will:
- Recreate the virtual environment
- Upgrade all dependencies (including extras and dev dependencies) to their latest allowed versions
- Update the lock file accordingly
"""
    upgrade_parser = subparsers.add_parser(
        "upgrade",
        help="Upgrade all dependencies to latest versions",
        description=upgrade_help,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    upgrade_parser.set_defaults(func=execute)


def execute(args: argparse.Namespace) -> bool:
    """Upgrade all dependencies to their latest allowed versions."""
    return run_command(
        "uv sync --upgrade --all-extras --dev",
        "dependencies upgrade",
    )
