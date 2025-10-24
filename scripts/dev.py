import argparse
import subprocess
import sys


def run_command(cmd: str, description: str = "") -> bool:
    """Run a command and handle errors."""
    if description:
        print(f"Running: {description}")
    else:
        print(f"Running: {cmd}")

    try:
        result = subprocess.run(cmd, check=True, shell=True, capture_output=False)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}")
        print(f"Error message: {e}")
        return False


def cmd_run() -> bool:
    """Run the main application."""
    return run_command(
        "uv run --dev python -m python_scaffolding.main", "Main application"
    )


def cmd_lint() -> bool:
    """Run linting tools (black, ruff, mypy)."""
    print("Running linting tools...")

    results = [
        run_command("uv run --dev -m black .", "Black formatter"),
        run_command("uv run --dev -m ruff check --fix .", "Ruff linter"),
        run_command("uv run --dev -m mypy .", "MyPy type checker"),
    ]
    return all(results)


def cmd_build() -> bool:
    """Build the wheel file."""
    return run_command("uv build", "Building wheel file")


def _add_run_parser(subparsers: argparse._SubParsersAction) -> None:
    """Add run command parser."""
    run_help = """Run the main application.

This command executes the main application using:
    uv run --dev python -m python_scaffolding.main
"""
    run_parser = subparsers.add_parser(
        "run",
        help="Run the main application",
        description=run_help,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    run_parser.set_defaults(func=cmd_run)


def _add_lint_parser(subparsers: argparse._SubParsersAction) -> None:
    """Add lint command parser."""
    lint_help = """Run linting tools (black, ruff, mypy).

This command runs code formatting and linting tools in sequence:
    • Black: Code formatter (uv run --dev -m black .)
    • Ruff: Linter with auto-fix (uv run --dev -m ruff check --fix .)
    • MyPy: Type checker (uv run --dev -m mypy .) - if available
"""
    lint_parser = subparsers.add_parser(
        "lint",
        help="Run linting tools (black, ruff, mypy)",
        description=lint_help,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    lint_parser.set_defaults(func=cmd_lint)


def _add_build_parser(subparsers: argparse._SubParsersAction) -> None:
    """Add build command parser."""
    build_help = """Build the wheel file.

This command builds a wheel distribution file using:
    uv build
    
The wheel file will be created in the 'dist/' directory.
"""
    build_parser = subparsers.add_parser(
        "build",
        help="Build the wheel file",
        description=build_help,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    build_parser.set_defaults(func=cmd_build)


def _prepare_parser() -> argparse.ArgumentParser:
    """Prepare and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Development helper script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    _add_run_parser(subparsers)
    _add_lint_parser(subparsers)
    _add_build_parser(subparsers)

    return parser


def _execute_command(args: argparse.Namespace) -> None:
    """Execute the command based on parsed arguments."""
    if not args.command:
        parser = _prepare_parser()
        parser.print_help()
        sys.exit(0)

    success = args.func()
    sys.exit(0 if success else 1)


def main() -> None:
    """Main entry point for dev script."""
    parser = _prepare_parser()
    args = parser.parse_args()
    _execute_command(args)


if __name__ == "__main__":
    main()
