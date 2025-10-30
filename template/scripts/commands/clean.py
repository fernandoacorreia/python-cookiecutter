from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def add_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    """Add clean command parser."""
    clean_help = """Clean build artifacts and cache directories.

This command removes:
- dist/ directory (build artifacts)
- .venv/ directory (virtual environment)
- .local/ directory (local development files)
- .pytest_cache/ directory (pytest cache)
- .ruff_cache/ directory (ruff cache)
- __pycache__/ directories (recursively)
"""
    clean_parser = subparsers.add_parser(
        "clean",
        help="Clean build artifacts and cache directories",
        description=clean_help,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    clean_parser.set_defaults(func=execute)


def execute(args: argparse.Namespace) -> bool:
    """Clean build artifacts and cache directories."""
    project_root = Path.cwd()
    success = True

    # Directories to delete at root level
    root_dirs = ["dist", ".venv", ".local", ".pytest_cache", ".ruff_cache"]

    print("Cleaning build artifacts and cache directories...\n")

    # Remove root-level directories
    for dir_name in root_dirs:
        dir_path = project_root / dir_name
        if dir_path.is_dir():
            try:
                shutil.rmtree(dir_path)
                print(f"✓ Deleted: {dir_path}")
            except Exception as e:
                print(f"✗ Error deleting {dir_path}: {e}")
                success = False
        else:
            print(f"  Skipped: {dir_path} (not found)")

    # Find and remove all __pycache__ directories recursively
    pycache_dirs = list(project_root.rglob("__pycache__"))
    if pycache_dirs:
        print(f"\nFound {len(pycache_dirs)} __pycache__ directories:")
        for pycache_dir in pycache_dirs:
            try:
                shutil.rmtree(pycache_dir)
                print(f"✓ Deleted: {pycache_dir}")
            except Exception as e:
                print(f"✗ Error deleting {pycache_dir}: {e}")
                success = False
    else:
        print("\n  No __pycache__ directories found")

    print("\nClean complete!")
    return success
