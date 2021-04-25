def apple(x):
    return 'It\'s hotter than the sun' if int(x**2) > 1000 else 'Help yourself to a honeycomb Yorkie for the glovebox.'

def take(arr, n):
    """
    Create a method take that accepts a list/array and a number n, and returns a list/array array of the first n elements from the list/array.
    :param arr:
    :param n:
    :return:
    """
    return arr[:n]


def twice_as_old(dad_years_old, son_years_old):
    """
    Your function takes two arguments:

    current father's age (years)
    current age of his son (years)
    Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
    :param dad_years_old:
    :param son_years_old:
    :return:
    """
    twice_as_old = son_years_old * 2
    return abs(twice_as_old - dad_years_old)
