"""Find the two smallest values of each list and save them to result.txt."""

import int_lists
import smallest


def main():
    """Write the result for every list into result.txt."""
    with open("result.txt", "w", encoding="utf-8") as result_file:
        for numbers in int_lists.ALL_LISTS:
            two_smallest = smallest.find_two_smallest(numbers)
            result_file.write(str(numbers) + " -> " + str(two_smallest) + "\n")


if __name__ == "__main__":
    main()
