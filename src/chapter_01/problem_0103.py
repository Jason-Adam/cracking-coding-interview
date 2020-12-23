# URLify:
# Write a method to replace all spaces in a string with '%20'. You may assume
# that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.


# O(n) time | O(n) space
def urlify_one(string: str, true_length: int) -> str:
    split = list(string)[0:true_length]
    for idx in range(true_length):
        if split[idx] == " ":
            split[idx] = "%20"

    return "".join(split)
