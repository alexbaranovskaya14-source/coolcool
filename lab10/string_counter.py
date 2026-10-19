"""Helpers for counting string elements in a list."""

from typing import Any


def count_strings(values: list[Any]) -> int:
    """Return the number of string elements in values."""
    count = 0
    for value in values:
        if isinstance(value, str):
            count += 1
    return count
