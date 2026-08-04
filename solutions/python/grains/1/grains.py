def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    total = 1
    for i in range(1, number):
        total *= 2
    return total


def total():
    t = 0
    for i in range(1, 65):
        t += square(i)
    return t