from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from .utils import run_command

INITIALIZATION_MARKER = Path(".local/dev/initialization.txt")


def add_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    """Add init command parser."""
    init_help = """Initialize the development tools.

This command sets up the development environment by:
- Installing pre-commit hooks (uv run pre-commit install)
- Creating initialization marker file (.local/dev/initialization.txt)
"""
    init_parser = subparsers.add_parser(
        "init",
        help="Initialize the development tools",
        description=init_help,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    init_parser.set_defaults(func=execute)


def execute(args: argparse.Namespace) -> bool:
    """Initialize the development environment."""
    success = True

    # Install pre-commit hooks
    print("\nInstalling pre-commit hooks...")
    if not run_command("uv run --dev pre-commit install", "pre-commit hooks"):
        success = False

    # Create initialization marker file
    print("\nCreating initialization marker file...")
    try:
        # Create parent directories if they don't exist
        INITIALIZATION_MARKER.parent.mkdir(parents=True, exist_ok=True)
        INITIALIZATION_MARKER.write_text(
            "This file marks that the development environment has been initialized.\n"
            "Created by running: ./dev init\n"
            f"Timestamp: {datetime.now().astimezone().isoformat()}\n"
        )
        print(f"Created: {INITIALIZATION_MARKER}")
    except Exception as e:
        print(f"Error creating marker file: {e}")
        success = False

    return success
