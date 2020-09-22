import pytest

from src.chapter_01.problem_0101 import letters_unique


@pytest.mark.parametrize("input,expected", [("abcd", True), ("aabc", False)])
def test_01_01(input, expected):
    assert letters_unique(input) == expected
