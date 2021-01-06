# String Compression:
# Implement a method to perform basic string compression using the
# counts of repeated characters. For example, the string aabcccccaaa
# would become a2b1c5a3. If the "compressed" string would not become
# smaller than the original string, your method should return the original string.
# you can assume the string has only uppercase and lowercase letters (a - z).


def run_length_encode(string: str) -> str:
    """O(n) time | O(n) space"""
    if len(string) <= 2:
        return string

    new: list = []
    cnt = 1
    current = string[0]

    for i in range(1, len(string)):
        if string[i] == current:
            if i == len(string) - 1:
                new.append(f"{current}{cnt + 1}")
            else:
                cnt += 1
        else:
            new.append(f"{current}{cnt}")
            current = string[i]
            cnt = 1

    compressed = "".join(new)
    if len(compressed) >= len(string):
        return string

    return compressed
