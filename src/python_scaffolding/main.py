def greetings(name: str = "World") -> str:
    return f"Hello, {name}!"


def main() -> None:
    """Hello world main function."""
    print(greetings())


if __name__ == "__main__":
    main()
