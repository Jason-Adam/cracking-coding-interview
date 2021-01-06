# One Away:
# There are three types of edits that can be performed on strings:
# insert a character, reemove a character, or replace a character.
# Given two strings, write a function to check if they are one edit
# (or zero edits) away.


def one_away(first: str, second: str) -> bool:
    """O(n) time | O(1) space"""
    if len(first) == len(second):
        edits = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                edits += 1
        if edits <= 1:
            return True

    if abs(len(first) - len(second)) == 1:
        f = 0
        s = 0
        while f < len(first) and s < len(second):
            if first[f] != second[s]:
                if f != s:
                    return False
                f += 1
            else:
                f += 1
                s += 1
        return True

    return False
