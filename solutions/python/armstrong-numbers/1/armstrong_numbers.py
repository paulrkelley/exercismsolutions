def is_armstrong_number(number):
    total = 0
    string = str(number)
    length = int(len(string))
    for i in string:
        total += int(i) ** length
    if total == number:
        return True
    return False
