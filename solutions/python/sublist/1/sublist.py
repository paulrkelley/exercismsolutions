"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    if list_one == list_two: return 2
    if is_sublist(list_one, list_two): return 0
    if is_sublist(list_two, list_one): return 1
    return 3

def is_sublist(smaller, larger):
    length = len(smaller)
    for start in range(len(larger) - length + 1):
        if larger[start:start + length] == smaller:
            return True

    return False