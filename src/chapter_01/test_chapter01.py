import pytest

from .problem_0101 import is_unique_one, is_unique_pythonic, is_unique_two
from .problem_0102 import is_permutation_one, is_permutation_two
from .problem_0103 import urlify_one
from .problem_0104 import is_palindrome_permutation_one, is_palindrome_permutation_two
from .problem_0105 import one_away
from .problem_0106 import run_length_encode
from .problem_0107 import rotate_matrix

is_unique_cases = [
    ("abcd", True),
    ("aabc", False),
    ("abcdefg", True),
    ("abcdefgA", True),
]


@pytest.mark.parametrize("input,expected", is_unique_cases)
def test_is_unqiue_one(input, expected):
    assert is_unique_one(input) == expected


@pytest.mark.parametrize("input,expected", is_unique_cases)
def test_is_unqiue_two(input, expected):
    assert is_unique_two(input) == expected


@pytest.mark.parametrize("input,expected", is_unique_cases)
def test_is_unqiue_pythonic(input, expected):
    assert is_unique_pythonic(input) == expected


is_permutation_cases = [
    ("abcd", "dcba", True),
    ("abcd", "dcb", False),
    ("abcd", "dcbd", False),
    ("abcdefghh", "hhabcdefg", True),
    ("aaaaa", "aaaaa", True),
    ("aa aa", "aa aa", True),
]


@pytest.mark.parametrize("first,second,expected", is_permutation_cases)
def test_is_permutation_one(first, second, expected):
    assert is_permutation_one(first, second) == expected


@pytest.mark.parametrize("first,second,expected", is_permutation_cases)
def test_is_permutation_two(first, second, expected):
    assert is_permutation_two(first, second) == expected


urlify_cases = [
    ("Mr John Smith  ", 13, "Mr%20John%20Smith"),
    ("hello there  ", 11, "hello%20there"),
]


@pytest.mark.parametrize("string,true_length,expected", urlify_cases)
def test_urlify_one(string, true_length, expected):
    assert urlify_one(string, true_length) == expected


is_palindrome_permutation_cases = [
    ("Tact Coa", True),
    ("mom", True),
    ("this is wrong", False),
    ("1", False),
    (" ", False),
    ("r", True),
    ("", False),
    ("siton A potaTopan Otis!", True),
]


@pytest.mark.parametrize("input,expected", is_palindrome_permutation_cases)
def test_is_palindrome_permutation_one(input, expected):
    assert is_palindrome_permutation_one(input) == expected


@pytest.mark.parametrize("input,expected", is_palindrome_permutation_cases)
def test_is_palindrome_permutation_two(input, expected):
    assert is_palindrome_permutation_two(input) == expected


one_away_cases = [
    ("pale", "ple", True),
    ("pales", "pale", True),
    ("pale", "bale", True),
    ("pale", "bake", False),
    ("pale", "p", False),
    ("pale", "pal", True),
    ("pale", "paleaaa", False),
    ("pale", "pale", True),
]


@pytest.mark.parametrize("first,second,expected", one_away_cases)
def test_one_away(first, second, expected):
    assert one_away(first, second) == expected


run_length_encode_cases = [
    ("aabcccccaaa", "a2b1c5a3"),
    ("aa", "aa"),
    ("aaa", "a3"),
    ("aaaffffffaacccceeee", "a3f6a2c4e4"),
]


@pytest.mark.parametrize("input,expected", run_length_encode_cases)
def test_run_length_encode(input, expected):
    assert run_length_encode(input) == expected


rotate_matrix_cases = [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], True, [[7, 4, 1],
                                                                  [8, 5, 2],
                                                                  [9, 6, 3]])]


@pytest.mark.parametrize("input,expected,rotated_input", rotate_matrix_cases)
def test_rotate_matrix(input, expected, rotated_input):
    assert rotate_matrix(input) == expected
    # Check if rotation happened
    assert input == rotated_input
