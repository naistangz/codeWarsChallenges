def quarter_of(month):
    q1 = [1, 2, 3]
    q2 = [4, 5, 6]
    q3 = [7, 8, 9]
    q4 = [10, 11, 12]
    if month in q1:
        return 1
    elif month in q2:
        return 2
    elif month in q3:
        return 3
    elif month in q4:
        return 4

print(quarter_of(3))
print(quarter_of(8))
print(quarter_of(11))
