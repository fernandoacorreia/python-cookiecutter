"""Check if there are unstaged or untracked files (in CI only)."""

import os
import subprocess
import sys


def main() -> None:
    # Only enforce in CI
    if not os.getenv("CI"):
        sys.exit(0)

    fail = False

    # Check for unstaged changes
    # git diff --quiet: exits 0 if no diffs, non-zero if there are differences
    # This detects files that have been modified but not yet staged
    try:
        diff_result = subprocess.run(
            ["git", "diff", "--quiet"],
            capture_output=True,
            check=False,
        )
        if diff_result.returncode != 0:
            print("❌ Commit blocked: you have unstaged changes.")
            subprocess.run(["git", "diff", "--stat"])
            fail = True
    except Exception as e:
        print(f"Error checking git diff: {e}")
        sys.exit(1)

    # Check for untracked files
    # git ls-files --others --exclude-standard: lists files not tracked by git,
    # excluding standard ignore patterns (respects .gitignore)
    try:
        untracked_result = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"],
            capture_output=True,
            text=True,
            check=False,
        )
        untracked = untracked_result.stdout.strip()
        if untracked:
            print("❌ Commit blocked: you have untracked files:")
            print(untracked)
            fail = True
    except Exception as e:
        print(f"Error checking untracked files: {e}")
        sys.exit(1)

    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
