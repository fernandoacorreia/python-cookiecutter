#!/usr/bin/env python
"""Post-generation hook for Cookiecutter template.

This script runs after the project is generated and performs:
1. Creates CLAUDE.md symlink to AGENTS.md
2. Git repository initialization
3. Initial commit
4. Initializes virtual environment and installs dependencies
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], description: str) -> bool:
    """Run a shell command and return success status."""
    print(f"\n{'='*60}")
    print(f"{description}...")
    print(f"{'='*60}")

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False


def main():
    """Run post-generation tasks."""
    project_dir = Path.cwd()

    print(f"\n{'='*60}")
    print(f"Post-generation setup for: {project_dir.name}")
    print(f"{'='*60}")

    # Create CLAUDE.md symlink to AGENTS.md
    print(f"\n{'='*60}")
    print("Creating CLAUDE.md symlink...")
    print(f"{'='*60}")
    claude_md = project_dir / "CLAUDE.md"
    agents_md = project_dir / "AGENTS.md"
    if agents_md.exists():
        try:
            claude_md.symlink_to("AGENTS.md")
            print("Created CLAUDE.md -> AGENTS.md")
        except Exception as e:
            print(f"Warning: Could not create symlink: {e}")
    else:
        print("Warning: AGENTS.md not found")

    # Initialize git repository
    if not run_command(["git", "init"], "Initializing Git repository"):
        print("Warning: Git initialization failed")

    # Create initial commit
    if not run_command(["git", "add", "."], "Staging all files"):
        print("Warning: Git add failed")

    if not run_command(
        ["git", "commit", "-m", "Initial commit from cookiecutter template"],
        "Creating initial commit",
    ):
        print("Warning: Git commit failed")

    # Initialize virtual environment and install dependencies
    if not run_command(["uv", "sync", "--dev"], "Initializing virtual environment and installing dependencies"):
        print("Warning: Dependency installation failed")

    # Initialize development tools
    if not run_command(["./dev", "init"], "Initializing development tools"):
        print("Warning: Development tools initialization failed")

    # Print success message
    print(f"\n{'='*60}")
    print("Project setup complete!")
    print(f"{'='*60}")
    print(f"\nProject: {{ cookiecutter.project_name }}")
    print(f"Location: {project_dir}")
    print(f"\nNext steps:")
    print(f"  1. cd {project_dir.name}")
    print(f"  2. ./dev --help")
    print(f"\nFor more information, see README.md")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
