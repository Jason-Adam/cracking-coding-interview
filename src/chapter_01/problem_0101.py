# Is Unique:
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


# O(n) time | O(n) space
# Hashmap approach
def letters_unique_hm(string: str) -> bool:
    c: dict = {}
    for s in string:
        if c.get(s):
            return False

        c[s] = 1
    return True


# O(n) time | O(1) space
# Bool Array
def letters_unique_ba(string: str) -> bool:
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
