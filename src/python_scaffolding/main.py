from pathlib import Path


def greetings(name: str = "World") -> str:
    return f"Hello, {name}!"


def read_file_content(file_path: Path) -> str:
    """Read content from a file."""
    return file_path.read_text()


def write_file_content(file_path: Path, content: str) -> None:
    """Write content to a file."""
    file_path.write_text(content)


def create_directory(dir_path: Path) -> None:
    """Create a directory if it doesn't exist."""
    dir_path.mkdir(parents=True, exist_ok=True)


def list_files_in_directory(dir_path: Path) -> list[Path]:
    """List all files in a directory."""
    return [f for f in dir_path.iterdir() if f.is_file()]


def copy_file(source_path: Path, destination_path: Path) -> None:
    """Copy a file from source to destination."""
    destination_path.write_text(source_path.read_text())


def main() -> None:
    """Hello world main function."""
    print(greetings())


if __name__ == "__main__":
    main()
