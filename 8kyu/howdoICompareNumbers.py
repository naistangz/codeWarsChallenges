"""
Task
What could be easier than comparing integer numbers? However, the given piece of code doesn't recognize some of the special numbers for a reason to be found. Your task is to find the bug and eliminate it.
"""


def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'

print(what_is(0))
print(what_is(123))
print(what_is(-1))
print(what_is(42))
print(what_is(42 * 42))