import re


special = "!@#$%^&*()_"

def solution(S):
    if len(S) < 6:
        return False
    elif re.search('[0-9]', S) is None:
        return False
    elif re.search('[A-Z]', S) is None:
        return False
    elif re.search('[a-z]', S) is None:
        return False
    elif ' ' in S:
        return False
    elif re.compile('[!@#$%^&*()_]').search(S) is None:
        return False
    return True

# print(solution('FooBar123!'))

def solutioner(N: int, S: str) -> int:
    """
    return option count
    """
    taken = [[] for _ in range(N)]
    for s in S.split(" "):
        row = int(s[:-1]) - 1
        if row > N:
            raise Exception("illegal reservation")

        taken[row].append(ord(s[-1]) - ord('A'))

    total_cnt = 0
    for row in taken:
        row.sort()
        row.append(ord('K') - ord('A') + 1)
        last = -1

        cnt = 0
        for idx in range(len(row)):
            free_seats = row[idx] - last - 1
            cnt += max(0, free_seats - (n - 1))
            last = row[idx]

        total_cnt += cnt

    return total_cnt

print(solutioner(1, ""))


def solutionS(N, S):
    """

    :param N: Number of Rows
    :param S: List of reserved seats
    :return: Number of four person families that can be seated in remaining unreserved seats
    """
    reserved_seats = [[] for _ in range(N)]
    for seat in S.split(" "):
        row = int(seat[:-1]) - 1
        if row > N:
            reserved_seats[row].append(ord(seat[-1]) - ord('A'))

        counter = 0
        for row in reserved_seats:
            row.sort()
            row.append(ord('K') - ord('A') + 1)
            last_row = -1

            count = 0
            for num in range(len(row)):
                available_seats = row[num] - last_row - 1
                count += max(0, available_seats - (num - 1))
                last_row = row[num]

            counter += count

        return counter


print(solutionS(3, "1A 3C 2B 40G 5A"))