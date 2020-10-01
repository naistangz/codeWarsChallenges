"""
Task

In this Kata, you will be given a number n (n > 0) and your task will be to return the smallest square number N (N > 0)
such that n + N is also a perfect square. If there is no answer, return -1 (nil in Clojure, Nothing in Haskell, None in Rust).

solve(13) = 36
# because 36 is the smallest perfect square that can be added to 13 to form a perfect square => 13 + 36 = 49

solve(3) = 1 # 3 + 1 = 4, a perfect square
solve(12) = 4 # 12 + 4 = 16, a perfect square
solve(9) = 16 # 16 + 9 = 25, a perfect square
solve(4) = -1

"""

import math


def solve(n):
    x = 1e9

    # looping between 1 to square root of N
    for i in range(1, int(math.sqrt(n)) + 1):

        # checking i is factor of N
        if n % i == 0:
            a = i
            b = n // i

            # condition checking factor satisfies equation
            if b - a != 0 and (b - a) % 2 == 0:
                x = min(x, (b - a) // 2)

    return (x * x if x != 1e9 else -1)


# second method
# def solve(n):
#     if (n%2 == 0 and n%4 != 0) or n == 1 or n == 4:
#         return -1
#    # for numbers in range of n
#     for i in range(n-1):
#         if ((n + (i+1)**2)**0.5)%1 == 0:
#             return (i+1)**2

print(solve(3))  # 1
print(solve(7))  # 9 (7 + 9) = 16, a perfect square
