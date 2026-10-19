"""Module with a function that finds the two smallest integers."""


def find_two_smallest(numbers):
    """Return the two smallest values of a list of at least two integers.

    The original list is not changed.
    """
    sorted_numbers = numbers[:]
    sorted_numbers.sort()
    return sorted_numbers[0], sorted_numbers[1]