def value(colors):
    color_code = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return int(str(color_code.index(colors[0]))+str(color_code.index(colors[1])))
