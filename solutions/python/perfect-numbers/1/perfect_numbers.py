def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    total = get_factors_total(number)
    if total > number:
        return "abundant"
    if total < number:
        return "deficient"
    if total == number:
        return "perfect"
    raise ValueError("Something went very wrong here!")

def get_factors_total(number):
    total = 0
    # Loop from 1 to n (exclusive)
    for i in range(1, number):
        if number % i == 0:
            total += i
    return total