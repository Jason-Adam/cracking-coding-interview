# One Away:
# There are three types of edits that can be performed on strings:
# insert a character, reemove a character, or replace a character.
# Given two strings, write a function to check if they are one edit
# (or zero edits) away.


def one_away(first: str, second: str) -> bool:
    """O(n) time | O(n) space"""
    if len(first) == len(second):
        edits = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                edits += 1

        if edits <= 1:
            return True

    if len(first) - len(second) == 1:
        letters: dict = {}
        for f in first:
            if not letters.get(f):
                letters[f] = 1
            else:
                letters[f] += 1

        for s in second:
            if not letters.get(s):
                return False
            else:
                letters[s] -= 1

        return sum([v for v in letters.values()]) == 1

    return False
