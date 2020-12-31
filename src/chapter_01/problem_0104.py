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


class PermutationPalindrome:
    def __init__(self, string: str):
        self.string = string

    def _toggle(self, bit_vector: int, index: int) -> int:
        if index < 0:
            return bit_vector

        mask = 1 << index
        bit_vector ^= mask

        return bit_vector

    def _get_char_number(self, letter: str) -> int:
        a = ord("a")
        z = ord("z")
        val = ord(letter)

        if a <= val and val <= z:
            return val - a

        return -1

    def _create_bit_vector(self) -> int:
        bit_vector = 0
        for letter in self.string:
            x = self._get_char_number(letter)
            bit_vector = self._toggle(bit_vector, x)

        return bit_vector

    def _check_at_most_one_bit_set(self, bit_vector: int) -> bool:
        return (bit_vector and (bit_vector - 1)) == 0

    def is_permutation(self) -> bool:
        bit_vector = self._create_bit_vector()
        return self._check_at_most_one_bit_set(bit_vector)
