"""Count the string elements in a list of mixed types."""

from typing import Any, List

def count_strings(values: List[Any]) -> int:
    """Return the number of string elements in values."""
    count = 0
    for value in values:
        if isinstance(value, str):
            count += 1
    return count

MIXED_VALUES: List[Any] = [list, "abba", "123", 123, "list", None,
                            True, ["x"], 3.14]


def main():
    """Print how many strings MIXED_VALUES contains."""
    print("Number of strings:", count_strings(MIXED_VALUES))


if __name__ == "__main__":
    main()
