def egg_count(display_value):
    binary_digits = 0
    if display_value == 0:
        return 0
    while display_value > 0:
        remainder = display_value % 2
        if remainder == 1:
            binary_digits += 1
        display_value = display_value // 2  # Integer division
    return binary_digits
