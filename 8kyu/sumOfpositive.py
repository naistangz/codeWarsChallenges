"""
Task
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""


def positive_sum(arr):
    if not arr:
        return 0
    counter = 0
    for num in arr:
        if num > 0:
            counter += num
    return counter

print(positive_sum([1, 2,3, 4, 5]))
print(positive_sum([1, -2, 3, 4, 5]))
