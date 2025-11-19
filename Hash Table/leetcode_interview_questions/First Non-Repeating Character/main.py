### My Solution
def first_non_repeating_char(val):
    data_map = {}
    for item in val:
        if item not in data_map:
            data_map[item] = True   # first time
        else:
            data_map[item] = False  # repeated
    for item in val:  # iterate in original order
        if data_map[item]:
            return item
    return None



### Instructor Solution

def first_non_repeating_char(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None


print(first_non_repeating_char("leetcode"))

print(first_non_repeating_char("hello"))


print(first_non_repeating_char("aabbcc"))
print(first_non_repeating_char("abcbad"))


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
