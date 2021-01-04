# Palindrom Permutation:
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be
# limited to just dictionary words. You can ignore casing and non-letter characters.


def is_palindrome_permutation_one(string: str) -> bool:
    """O(n) time | O(n) space
    Hashmap approach.
    Palindrome permutations should have character
    counts that are all even and can contain only one character
    (at most) with an odd count.
    """
    if len(string) == 0:
        return False

    if len(string) == 1:
        if string.isalpha():
            return True
        else:
            return False

    letters: dict = {}
    for letter in string:
        if letter.isalpha():
            if not letters.get(letter.lower()):
                letters[letter.lower()] = 1
            else:
                letters[letter.lower()] += 1

    evens = 0
    odds = 0

    for val in letters.values():
        if val % 2 == 0:
            evens += 1
        else:
            odds += 1

    if odds == 0 or odds == 1:
        return True

    return False


def is_palindrome_permutation_two(string: str) -> bool:
    """O(n) time | O(1) space
    This approach uses a fixed array with the unicode
    values for each character.
    """
    if len(string) == 0:
        return False

    if len(string) == 1:
        if string.isalpha():
            return True
        else:
            return False

    table = [0 for _ in range(ord("z") - ord("a") + 1)]
    count_odd = 0
    for letter in string:
        x = char_number(letter)
        if x != -1:
            table[x] += 1
            if table[x] % 2 != 0:
                count_odd += 1
            else:
                count_odd -= 1

    return count_odd <= 1


def char_number(char: str) -> int:
    """Helper Function for determining char number."""
    a = ord("a")
    z = ord("z")
    val = ord(char.lower())

    if a <= val <= z:
        return val - a

    return -1
