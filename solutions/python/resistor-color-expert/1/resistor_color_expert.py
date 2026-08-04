def resistor_label(colors):
    color_code = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    tolerance = {"grey": 0.05, "violet":0.1, "blue":0.25, "green":0.5, "brown":1, "red":2, "gold":5, "silver":10}
    
    if len(colors) == 1: return "0 ohms"
    if len(colors) == 4:
        significant_digits = (color_code.index(colors[0]) * 10 + color_code.index(colors[1]))
        multiplier_exponent = color_code.index(colors[2])
        tolerance_value = tolerance[colors[3]]

    elif len(colors) == 5:
        significant_digits = (color_code.index(colors[0]) * 100 + color_code.index(colors[1]) * 10 + color_code.index(colors[2]))
        multiplier_exponent = color_code.index(colors[3])
        tolerance_value = tolerance[colors[4]]

    else:
        raise ValueError("A resistor must have 1, 4, or 5 bands")

    value = significant_digits * (10 ** multiplier_exponent)

    if value >= 1_000_000_000:
        resistance = f"{value / 1_000_000_000:g} gigaohms"
    elif value >= 1_000_000:
        resistance = f"{value / 1_000_000:g} megaohms"
    elif value >= 1_000:
        resistance = f"{value / 1_000:g} kiloohms"
    else:
        resistance = f"{value:g} ohms"

    return f"{resistance} ±{tolerance_value:g}%"