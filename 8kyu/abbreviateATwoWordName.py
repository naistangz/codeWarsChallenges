"""
Task
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F
"""


def abbrevName(name):
    # takes first index of each split up word i.e S in Sam and H in Harris, joining it with '.'
    abbrev = '.'.join(initials[0].upper() for initials in name.split())
    return abbrev

print(abbrevName("Sam Harris"))
print(abbrevName("Patrick Feenan"))