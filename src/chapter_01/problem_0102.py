# Check Permutation:
# Given two string, write a method to decide if one is a permutation of the other.


def is_permutation_one(first_string: str, second_string: str) -> bool:
    """O(n) time | O(n) space
    Hashmap Approach
    """
    # Assumption is that permutation means each string contains same letters

    if len(first_string) != len(second_string):
        return False

    letters: dict = {}

    # Increment first string

    for f in first_string:
        if letters.get(f) is not None:
            letters[f] += 1
        else:
            letters[f] = 1

    # decrement second string

    for s in second_string:
        if letters.get(s) is None:
            return False
        else:
            letters[s] -= 1

    # Check if any values not equal to zero

    return all([v == 0 for v in letters.values()])


def is_permutation_two(first_string: str, second_string: str) -> bool:
    """O(n log(n)) time | O(n) space
    Sort the strings first and compare.
    Timsort in Python has O(n log(n)) time complexity.
    """

    if len(first_string) != len(second_string):
        return False

    return sorted(first_string) == sorted(second_string)
