"""
Tasks
Hey awesome programmer!

You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

Therefore you need a method, which returns the smallest unused ID for your next new data item...

Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to find or remove them!

Go on and code some pure awesomeness!
"""


def next_id(arr):
    if not arr:
        return 0
    # place in order
    arr.sort()
    # return 0 if index 0 does not have 0
    if arr[0] != 0:
        return 0
    # comparing two values to check if they are chronological
    for k, v in enumerate(arr):
        # if first value is not equal to second value, return first value
        if k != v:
            return k
    # return first value + 1
    return k + 1

# second iter
# def next_id(arr):
#     if not arr:
#         return 0
#     arr.sort()
#     if arr[0] != 0:
#         return 0
#     for i in range(len(arr)-1):
#         if arr[i] - arr[i-1] < -1:
#             return arr[i] + 1
#         return arr[-1] + 1

print(next_id([0,1,2,3,4,5,6,7,8,9,10])) # expected 11
print(next_id([5,4,3,2,1])) # expected 0
print(next_id([0, 1, 2, 3, 5])) # expected 4
print(next_id([])) # expected 0
print(next_id([0,0,0,0,0,0])) # expected 1