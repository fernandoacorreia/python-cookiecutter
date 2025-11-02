from __future__ import annotations

import argparse

from .utils import run_command


def add_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    """Add lint command parser."""
    lint_help = """Run code quality checks using prek hooks on all files.

This command runs prek hooks configured in .pre-commit-config.yaml.
"""
    lint_parser = subparsers.add_parser(
        "lint",
        help="Run prek hooks",
        description=lint_help,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    lint_parser.set_defaults(func=execute)


def execute(args: argparse.Namespace) -> bool:
    """Run prek hooks."""
    return run_command("uv run --dev prek run --all-files", "prek")
