"""
Instructions

In this Kata your task will be to return the count of pairs that have consecutive numbers as follows:

pairs([1,2,5,8,-4,-3,7,6,5]) = 3
The pairs are selected as follows [(1,2),(5,8),(-4,-3),(7,6),5]
--the first pair is (1,2) and the numbers in the pair are consecutive; Count = 1
--the second pair is (5,8) and are not consecutive
--the third pair is (-4,-3), consecutive. Count = 2
--the fourth pair is (7,6), also consecutive. Count = 3.
--the last digit has no pair, so we ignore.
"""

# 1st Iter
# def pairs(arr):
#     count = 0
#     # iterating through list
#     for i in range(len(arr)-1):
#         # checking if next number is consecutive
#         if arr[i] + 1 == arr[i+1]:
#             count += 1
#     return count

# # 2nd Iter
# def pairs(arr):
#     count = 0
#     if len(arr) % 2 != 0:
#         arr.pop() # return arr # returns [1, 2, 5, 8, -4, -3, 7, 6]
#     for i in arr[:-1:]:
#         if arr[i] + 1 == arr[i+1]:
#             count += 1
#     return count


# Unfinished
# 3rd Iter
def pairs(arr):
    print(f"Original List: {arr}")
    resulting = []
    for i in range(len(arr)-1):
        resulting.append([arr[i], arr[i + 1]])
        print(f"Paired element list: {str(resulting)}")

# sample_arr = [1,2,5,8,-4,-3,7,6,5]
# indexing = sample_arr[:-1:] # returns [1, 2, 5, 8, -4, -3, 7, 6]
# print(indexing)

# def pairs(arr):
#     listing = []
#     for i in arr:
#         listing.append(i)
#     return listing

# Returns
# [1, 2, 5, 8, -4, -3, 7, 6, 5]
# [-55, -56, -7, -6, 56, 55, 63, 62]

print(pairs([1,2,5,8,-4,-3,7,6,5])) # 3
print(pairs([-55, -56, -7, -6, 56, 55, 63, 62])) # 4

