def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b == c


def isosceles(sides):
    if not is_valid_triangle(sides):
        return False 
    a, b, c = sides
    return a == b or b == c or c == a

def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a != b and b != c and c != a

def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or b + c <= a or a + c <= b:
        return False
    return True