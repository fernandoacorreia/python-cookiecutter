import argparse
import subprocess
import sys
from pathlib import Path


def run_command(cmd: str, description: str = "") -> bool:
    """Run a command and handle errors."""
    if description:
        print(f"Running: {description}")

    try:
        result = subprocess.run(cmd, check=True, shell=True, capture_output=False)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {cmd}")
        print(f"Error message: {e}")
        return False


def cmd_run() -> bool:
    """Run the main application."""
    print("Running the application...")
    return run_command(
        "uv run --dev python -m python_scaffolding.main", "Main application"
    )


def cmd_lint() -> bool:
    """Run linting tools (black, ruff, mypy)."""
    print("Running linting tools...")

    # Check if mypy is available
    try:
        subprocess.run(
            "uv run --dev -m mypy --version",
            check=True,
            shell=True,
            capture_output=True,
        )
        mypy_available = True
    except subprocess.CalledProcessError:
        mypy_available = False
        print("Warning: mypy not found in dev dependencies, skipping...")

    success = True

    # Run black
    if not run_command("uv run --dev -m black .", "Black formatter"):
        success = False

    # Run ruff
    if not run_command("uv run --dev -m ruff check --fix .", "Ruff linter"):
        success = False

    # Run mypy if available
    if mypy_available:
        if not run_command("uv run --dev -m mypy .", "MyPy type checker"):
            success = False

    return success


def cmd_build() -> bool:
    """Build the wheel file."""
    print("Building wheel file...")

    # Ensure dist directory exists
    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)

    return run_command("uv build", "Building wheel file")


def main() -> None:
    """Main entry point for dev script."""
    parser = argparse.ArgumentParser(
        description="Development helper script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Run command
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

    # Lint command
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

    # Build command
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

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    success = args.func()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
