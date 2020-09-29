"""
Instructions
- Simple, given a string of words, return the length of the shortest word(s).
- String will never be empty and you do not need to account for different data types.
"""
def find_short(s):
    convert_to_list = list(s.split(" "))
    shortest_word = min(len(word) for word in convert_to_list)
    return shortest_word