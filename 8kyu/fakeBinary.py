"""
Task
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
"""


def fake_bin(x):
    result = []
    for num in x:
        if int(num) < 5:
            result.append(0)
        elif int(num) > 4:
            result.append(1)
    return ''.join(map(str, result))



print(fake_bin("45385593107843568")) # expected "01011110001100111"
