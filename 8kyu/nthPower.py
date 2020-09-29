# first iteration
# def index(array, n):
#     if n in array and n < len(array):
#         return array[n]**n
#     return -1

def index(array, n):
    if n < len(array):
        return array[n]**n
    return -1

# print(index([1, 2, 3, 4],2))
# print(index([1, 3, 10, 100],3))
# print(index([-1, 4, -5, 10],6))
# print(index([-1, 4, -5, 10, 14],2))