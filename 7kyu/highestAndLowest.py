"""
Instructions
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""

# def high_and_low(numbers):
#     split_up = numbers.split(" ")
#     int_values = []
#     for num in split_up:
#         int_values.append(int(num))
#     max_num = str(max(int_values))
#     min_num = str(min(int_values))
#     return max_num + " " + min_num

# second method
def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")) # return '542 -214'