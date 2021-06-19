# Is Unique:
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def is_unique_one(string: str) -> bool:
    """O(n) time | O(n) space
    Hashmap Approach
    """
    chars = {}

    for s in string:
        if chars.get(s):
            return False

        chars[s] = 1

    return True


def is_unique_two(string: str) -> bool:
    """O(n) time | O(1) space
    Bool Array - Assumes ASCII character set.
    """
    # Assumes ASCII character set

    if len(string) > 128:
        return False

    # O(1) space due to constant array size
    char_set = [False] * 128

    for char in string:
        val: int = ord(char)

        if char_set[val]:
            return False
        char_set[val] = True

    return True


def is_unique_pythonic(string: str) -> bool:
    """O(n) time | O(n) space
    Set implementation (hashmap under the hood)
    """

    return len(set(string)) == len(string)
