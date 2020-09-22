"""
Is Unique:
    1. Implement an algorithm to determine if a string has all unique characters.
    2. What if you cannot use additional data structures?
"""

from collections import Counter


# 1
def letters_unique(letters: str) -> bool:
    c = Counter(letters)
    return not any([val > 1 for val in c.values()])
