import sys


def main():
    """Print command line arguments and exit."""
    print("Command line arguments:")
    for i, arg in enumerate(sys.argv):
        print(f"  {i}: {arg}")
    sys.exit(0)


if __name__ == "__main__":
    main()
