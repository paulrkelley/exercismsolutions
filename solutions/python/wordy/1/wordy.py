def answer(question):
    valid_math_operators = ["plus", "minus", "multiplied", "divided"]
    words_list = question.replace("?", "").split()
    # Remove the opening words.
    if words_list[:2] != ["What", "is"]:
        raise ValueError("syntax error")
    words_list = words_list[2:]
    if len(words_list) == 0:
        raise ValueError("syntax error")
    # The first meaningful word must be a number.
    if not is_integer(words_list[0]):
        raise ValueError("syntax error")
    total = int(words_list[0])
    index = 1
    while index < len(words_list):
        operator = words_list[index]
        if is_integer(operator):
            raise ValueError("syntax error")            
        if operator not in valid_math_operators:
            raise ValueError("unknown operation")
        index += 1
        # "multiplied" and "divided" must be followed by "by".
        if operator in ["multiplied", "divided"]:
            if index >= len(words_list) or words_list[index] != "by":
                raise ValueError("syntax error")
            index += 1
        # There must be a number after the operator.
        if index >= len(words_list):
            raise ValueError("syntax error")
        if not is_integer(words_list[index]):
            raise ValueError("syntax error")
        next_number = int(words_list[index])
        if operator == "plus":
            total += next_number
        elif operator == "minus":
            total -= next_number
        elif operator == "multiplied":
            total *= next_number
        elif operator == "divided":
            total //= next_number
        index += 1
    return total


def is_integer(val):
    try:
        int(val)
        return True
    except ValueError:
        return False