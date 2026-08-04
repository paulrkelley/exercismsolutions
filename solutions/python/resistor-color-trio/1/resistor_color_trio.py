def label(colors):
    color_code = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    first_digit = color_code.index(colors[0])
    second_digit = color_code.index(colors[1])
    exponent = color_code.index(colors[2])
    value = (first_digit * 10 + second_digit) * (10 ** exponent)
    if value == 0:
        return "0 ohms"
    if value >= 1_000_000_000:
        return f"{value // 1_000_000_000} gigaohms"
    if value >= 1_000_000:
        return f"{value // 1_000_000} megaohms"
    if value >= 1_000:
        return f"{value // 1_000} kiloohms"
    return f"{value} ohms"