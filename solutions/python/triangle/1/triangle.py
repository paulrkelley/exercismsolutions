def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0 or b == 0 or c == 0: return False
    if (a+b >= c) and (b+c >= a) and (a+c >= b):
        if a == b == c:
            return True
    return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0 or b == 0 or c == 0: return False
    if (a+b >= c) and (b+c >= a) and (a+c >= b):
        if (a==b) or (a==c) or (b==c):
            return True
    return False

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0 or b == 0 or c == 0: return False
    if (a+b >= c) and (b+c >= a) and (a+c >= b):
        if (a==b) or (a==c) or (b==c):
            return False
        return True
    return False
    
