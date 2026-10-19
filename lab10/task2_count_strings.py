"""Count the string elements in a list of mixed types."""

from typing import Any

from string_counter import count_strings

MIXED_VALUES: list[Any] = [list, "abba", "123", 123, "list", None,
                           True, ["x"], 3.14]


def main() -> None:
    """Print how many strings MIXED_VALUES contains."""
    print("Number of strings:", count_strings(MIXED_VALUES))


if __name__ == "__main__":
    main()
