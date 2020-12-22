import unittest
from .problem_0101 import letters_unique_ba, letters_unique_hm


class TestLettersUnique(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("aaaaa", False),
        ("abcdk hh", False),
    ]
    test_functions = [letters_unique_hm, letters_unique_ba]

    def test(self):
        for letters_unique in self.test_functions:
            for text, expected in self.test_cases:
                assert letters_unique(text) == expected


if __name__ == "__main__":
    unittest.main()
