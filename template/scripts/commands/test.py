from __future__ import annotations

import argparse

from .utils import run_command


def add_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    """Add test command parser."""
    test_help = """Run tests using pytest.

This command runs pytest with pytest-sugar enabled for better output.
pytest-sugar provides instant failure display, progress bars, and improved
test results formatting.

This command runs pytest with any additional arguments passed verbatim.
Examples:
    dev test                    # Run all tests
    dev test tests/test_main.py # Run specific test file
    dev test -v                 # Run with verbose output (one test per line)
    dev test --cov              # Run with coverage report
    dev test --cov=src          # Run with coverage for specific path
    dev test --cov --cov-report=html  # Generate HTML coverage report
    dev test -k test_function   # Run tests matching pattern
    dev test -p no:sugar        # Disable pytest-sugar
    dev test --old-summary      # Show detailed failures instead of one-line tracebacks
    dev test --force-sugar      # Force pytest-sugar in CI/non-interactive environments
"""
    test_parser = subparsers.add_parser(
        "test",
        help="Run tests using pytest",
        description=test_help,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    test_parser.set_defaults(func=execute)


def execute(args: argparse.Namespace) -> bool:
    """Run tests using pytest."""
    # Build the pytest command
    cmd_parts = ["uv", "run", "--dev", "-m", "pytest"]

    # Add any unknown arguments (extra args passed to pytest)
    if hasattr(args, "unknown_args") and args.unknown_args:
        cmd_parts.extend(args.unknown_args)

    cmd = " ".join(cmd_parts)

    return run_command(cmd, "pytest")
