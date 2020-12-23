import pytest

from .problem_0101 import is_unique_one, is_unique_two
from .problem_0102 import is_permutation_one, is_permutation_two
from .problem_0103 import urlify_one


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
]


@pytest.mark.parametrize("string,true_length,expected", urlify_cases)
def test_urlify_one(string, true_length, expected):
    assert urlify_one(string, true_length) == expected
