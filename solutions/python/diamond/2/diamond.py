def rows(letter):
    r = []
    spaces = ord(letter) - ord("A")
    for index in range(ord("A"), ord(letter) + 1):
        inside = 2 * (index - ord("A")) - 1
        outside = spaces - (index - ord("A"))
        string = " " * outside
        string += chr(index)
        # A only appears once because it has no inside spacing.
        if chr(index) != "A":
            string += " " * inside
            string += chr(index)
        string += " " * outside
        r.append(string)
    # Mirror everything except the final row.
    diamond = r + r[-2::-1]
    return diamond