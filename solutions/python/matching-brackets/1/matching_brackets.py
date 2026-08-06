def is_paired(input_string):
    conditional = "()[]{}"
    braces = 0
    brackets = 0
    parens = 0
    containers = []
    for ch in input_string:
        if braces < 0 or brackets < 0 or parens < 0:
            return False
        if ch in conditional:
            if ch == "{":
                braces += 1
                containers.append("{")
            if ch == "}":
                braces -= 1
                if not containers or containers[-1] != "{":
                    return False
                containers.pop()
            if ch == "[":
                brackets += 1
                containers.append("[")
            if ch == "]":
                brackets -= 1
                if not containers or containers[-1] != "[":
                    return False
                containers.pop()
            if ch == "(":
                parens += 1
                containers.append("(")
            if ch == ")":
                parens -= 1
                if not containers or containers[-1] != "(":
                    return False
                containers.pop()
    if braces != 0 or brackets != 0 or parens != 0:
        return False
    return True