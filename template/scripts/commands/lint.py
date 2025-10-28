import argparse

from .utils import run_command


def add_parser(subparsers: argparse._SubParsersAction) -> None:
    """Add lint command parser."""
    lint_help = """Run code quality checks using pre-commit hooks on all files.

This command runs pre-commit hooks configured in .pre-commit-config.yaml.
"""
    lint_parser = subparsers.add_parser(
        "lint",
        help="Run pre-commit hooks",
        description=lint_help,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    lint_parser.set_defaults(func=execute)


def execute(args: argparse.Namespace) -> bool:
    """Run pre-commit hooks."""
    return run_command("uv run --dev pre-commit run --all-files", "pre-commit")
