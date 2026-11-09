"""Print a greeting for the name given on the command line."""

import sys


def greet(name: str) -> str:
    """Return the greeting for ``name``."""
    return f"Hello, {name}!"


def main() -> int:
    """Print a greeting for the first argument, or for "world" if absent."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    raise SystemExit(main())
